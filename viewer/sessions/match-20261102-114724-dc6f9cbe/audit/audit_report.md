# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **3610**
- Achados: **118**
- CRITICAL: 0 | HIGH: 4 | MEDIUM: 75 | LOW: 39

## Metadados da sessão

- Match ID: dc6f9cbe-2e81-4044-a664-06571e49d691
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 8cf3067091353b9d76ede6b21f2c988ffc15c7f382c2654a4fd553f7adf4f766
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **2974**
- Entradas posteriores à eliminação ignoradas: **636**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 3 | 8 | 24 | 3 | 17 | 0 | 1 | não/inconclusivo | 1 |
| Jogador 6 | 43 | 7 | 19 | 10 | 12 | 0 | 0 | sim | 1 |
| Jogador 7 | 30 | 7 | 16 | 9 | 9 | 0 | 0 | sim | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 131 | 22 | 3 | 26 | 0 | 37 | 39 | 0.0642 | 11 | 6 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::ITEM: 2, ALL_IN::PASS: 7, FAST8::BUY: 6, FAST8::BUY_XP: 15, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 17, FAST8::MOVE_BOARD: 1, FAST8::PASS: 14, FAST8::SELL: 2, SLOWROLL::BUY: 2, SLOWROLL::BUY_XP: 4, SLOWROLL::MOVE_BENCH: 2, SLOWROLL::MOVE_BOARD: 3, SLOWROLL::PASS: 3, STABILIZE::BUY: 11, STABILIZE::BUY_XP: 7, STABILIZE::ITEM: 1, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 13, STABILIZE::SELL: 1
- Jogador 1 — recompensas por ação: BUY: média 0.4614 (n=22), BUY_XP: média -0.0250 (n=26), ITEM: média 0.0725 (n=4), MOVE_BENCH: média 0.0706 (n=34), MOVE_BOARD: média -0.0380 (n=5), PASS: média -0.0627 (n=37), SELL: média -0.4233 (n=3)
| Jogador 2 | 139 | 20 | 6 | 47 | 0 | 37 | 25 | 0.0495 | 10 | 2 |
- Jogador 2 — ações por estratégia: ECON::BUY: 6, ECON::BUY_XP: 11, ECON::ITEM: 2, ECON::MOVE_BENCH: 3, ECON::PASS: 10, ECON::SELL: 2, FAST8::BUY: 3, FAST8::BUY_XP: 17, FAST8::MOVE_BENCH: 4, FAST8::MOVE_BOARD: 2, FAST8::PASS: 9, FAST8::SELL: 2, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 5, SLOWROLL::MOVE_BENCH: 6, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 4, STABILIZE::BUY: 4, STABILIZE::BUY_XP: 1, STABILIZE::MOVE_BENCH: 7, STABILIZE::PASS: 5, STABILIZE::SELL: 1, WINSTREAK::BUY: 4, WINSTREAK::BUY_XP: 13, WINSTREAK::ITEM: 2, WINSTREAK::MOVE_BENCH: 2, WINSTREAK::PASS: 9, WINSTREAK::SELL: 1
- Jogador 2 — recompensas por ação: BUY: média 0.3245 (n=20), BUY_XP: média -0.0345 (n=47), ITEM: média 0.0475 (n=4), MOVE_BENCH: média 0.1486 (n=22), MOVE_BOARD: média 0.0267 (n=3), PASS: média 0.0000 (n=37), SELL: média -0.2550 (n=6)
| Jogador 3 | 93 | 16 | 1 | 25 | 0 | 31 | 18 | 0.0517 | 10 | 6 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 2, ALL_IN::PASS: 7, FAST8::BUY: 1, FAST8::BUY_XP: 9, FAST8::MOVE_BENCH: 3, FAST8::PASS: 6, FAST8::SELL: 1, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 11, SLOWROLL::MOVE_BENCH: 3, SLOWROLL::PASS: 7, STABILIZE::BUY: 5, STABILIZE::BUY_XP: 5, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 11
- Jogador 3 — recompensas por ação: BUY: média 0.3844 (n=16), BUY_XP: média -0.0208 (n=25), ITEM: média 0.0900 (n=2), MOVE_BENCH: média 0.0641 (n=17), MOVE_BOARD: média -0.2100 (n=1), PASS: média -0.0342 (n=31), SELL: média -0.8200 (n=1)
| Jogador 4 | 94 | 17 | 3 | 24 | 0 | 27 | 21 | 0.0885 | 6 | 6 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::PASS: 1, FAST8::BUY: 4, FAST8::BUY_XP: 10, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 3, FAST8::PASS: 8, FAST8::SELL: 2, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 4, SLOWROLL::MOVE_BENCH: 3, SLOWROLL::PASS: 3, SLOWROLL::SELL: 1, STABILIZE::BUY: 9, STABILIZE::BUY_XP: 10, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 2, STABILIZE::PASS: 15
- Jogador 4 — recompensas por ação: BUY: média 0.4618 (n=17), BUY_XP: média -0.0013 (n=24), ITEM: média 0.0550 (n=2), MOVE_BENCH: média 0.1269 (n=16), MOVE_BOARD: média -0.0500 (n=5), PASS: média -0.0019 (n=27), SELL: média -0.4467 (n=3)
| Jogador 5 | 77 | 10 | 2 | 18 | 0 | 27 | 18 | 0.0362 | 8 | 4 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::ITEM: 2, ALL_IN::PASS: 3, FAST8::BUY: 3, FAST8::BUY_XP: 12, FAST8::MOVE_BENCH: 3, FAST8::PASS: 10, FAST8::SELL: 1, STABILIZE::BUY: 6, STABILIZE::BUY_XP: 6, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 3, STABILIZE::PASS: 14, STABILIZE::SELL: 1
- Jogador 5 — recompensas por ação: BUY: média 0.3000 (n=10), BUY_XP: média -0.0167 (n=18), ITEM: média 0.0450 (n=2), MOVE_BENCH: média 0.1320 (n=15), MOVE_BOARD: média 0.0167 (n=3), PASS: média -0.0448 (n=27), SELL: média -0.4100 (n=2)
| Jogador 6 | 76 | 12 | 2 | 19 | 0 | 26 | 16 | 0.0726 | 10 | 5 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 1, ALL_IN::PASS: 2, FAST8::BUY: 2, FAST8::BUY_XP: 7, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 1, FAST8::PASS: 8, SLOWROLL::BUY: 4, SLOWROLL::BUY_XP: 9, SLOWROLL::MOVE_BENCH: 5, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 8, SLOWROLL::SELL: 1, STABILIZE::BUY: 4, STABILIZE::BUY_XP: 3, STABILIZE::MOVE_BENCH: 6, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 8, STABILIZE::SELL: 1
- Jogador 6 — recompensas por ação: BUY: média 0.5567 (n=12), BUY_XP: média -0.0342 (n=19), ITEM: média 0.0000 (n=1), MOVE_BENCH: média 0.0862 (n=13), MOVE_BOARD: média -0.0800 (n=3), PASS: média -0.0408 (n=26), SELL: média -0.1650 (n=2)
| Jogador 7 | 58 | 9 | 0 | 16 | 0 | 21 | 12 | 0.0872 | 3 | 6 |
- Jogador 7 — ações por estratégia: ALL_IN::PASS: 1, FAST8::BUY: 2, FAST8::MOVE_BENCH: 1, FAST8::PASS: 4, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 10, SLOWROLL::MOVE_BENCH: 2, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 6, STABILIZE::BUY: 4, STABILIZE::BUY_XP: 6, STABILIZE::MOVE_BENCH: 7, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 10
- Jogador 7 — recompensas por ação: BUY: média 0.3978 (n=9), BUY_XP: média -0.0394 (n=16), MOVE_BENCH: média 0.2800 (n=10), MOVE_BOARD: média -0.1500 (n=2), PASS: média -0.0186 (n=21)
| Jogador 8 | 128 | 16 | 4 | 38 | 0 | 35 | 31 | -0.0041 | 15 | 4 |
- Jogador 8 — ações por estratégia: ALL_IN::PASS: 1, ECON::BUY: 1, ECON::BUY_XP: 4, ECON::ITEM: 2, ECON::MOVE_BENCH: 3, ECON::PASS: 5, FAST8::BUY: 1, FAST8::BUY_XP: 9, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 5, FAST8::PASS: 7, SLOWROLL::BUY: 1, SLOWROLL::BUY_XP: 1, STABILIZE::BUY: 8, STABILIZE::BUY_XP: 14, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 3, STABILIZE::PASS: 14, STABILIZE::SELL: 3, WINSTREAK::BUY: 5, WINSTREAK::BUY_XP: 10, WINSTREAK::ITEM: 1, WINSTREAK::MOVE_BENCH: 2, WINSTREAK::PASS: 8, WINSTREAK::SELL: 1
- Jogador 8 — recompensas por ação: BUY: média 0.2369 (n=16), BUY_XP: média -0.0208 (n=38), ITEM: média 0.0600 (n=4), MOVE_BENCH: média -0.0843 (n=28), MOVE_BOARD: média 0.0400 (n=3), PASS: média -0.0014 (n=35), SELL: média -0.3700 (n=4)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 11:47:28 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.5200 |  |
| Jogador 1 | ? | 11:47:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 11:47:34 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 11:47:34 | MOVE Bench -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3000 |  |
| Jogador 1 | 1-1 | 11:47:35 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 1 | 1-1 | 11:47:35 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 1 | 1-1 | 11:47:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-2 | 11:47:40 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.2100 |  |
| Jogador 1 | 1-2 | 11:47:40 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.2800 |  |
| Jogador 1 | 1-2 | 11:47:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 1 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 1 | 1-4 | 11:47:53 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | 0.0800 |  |
| Jogador 1 | 1-4 | 11:47:53 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | -0.2100 |  |
| Jogador 1 | 1-4 | 11:47:54 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | 0.4000 |  |
| Jogador 1 | 1-4 | 11:47:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Sejuani | -0.0400 |  |
| Jogador 1 | 1-4 | 11:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-1 | 11:48:00 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | 1.0200 |  |
| Jogador 1 | 2-1 | 11:48:00 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | -0.4000 |  |
| Jogador 1 | 2-1 | 11:48:00 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | -0.2200 |  |
| Jogador 1 | 2-1 | 11:48:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-2 | 11:48:06 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Sejuani | -0.4300 |  |
| Jogador 1 | 2-2 | 11:48:07 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Sejuani | 1.1100 |  |
| Jogador 1 | 2-2 | 11:48:07 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Sejuani | -0.1500 |  |
| Jogador 1 | 2-2 | 11:48:08 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Sejuani | 0.2700 |  |
| Jogador 1 | 2-2 | 11:48:08 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Sejuani | 0.2700 |  |
| Jogador 1 | 2-2 | 11:48:08 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Sejuani | 0.5300 |  |
| Jogador 1 | 2-2 | 11:48:09 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Sejuani | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-2 | 11:48:09 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Sejuani | -0.1800 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-2 | 11:48:09 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Sejuani | 0.0500 |  |
| Jogador 1 | 2-2 | 11:48:09 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-3 | 11:48:13 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Sejuani | 0.3000 |  |
| Jogador 1 | 2-3 | 11:48:13 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_18_Sejuani | 0.8200 |  |
| Jogador 1 | 2-3 | 11:48:14 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Sejuani | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-3 | 11:48:14 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-4 | 11:48:20 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Defendente | DA_18_Sejuani | 0.9700 |  |
| Jogador 1 | 2-4 | 11:48:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Defendente | DA_18_Sejuani | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 1 | 2-4 | 11:48:21 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Defendente | DA_18_Sejuani | -0.2300 |  |
| Jogador 1 | 2-4 | 11:48:21 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Defendente | DA_18_Sejuani | 0.1000 |  |
| Jogador 1 | 2-4 | 11:48:21 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Defendente | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-5 | 11:48:26 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Defendente | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-5 | 11:48:27 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Defendente | DA_18_Sejuani | 0.5300 |  |
| Jogador 1 | 2-5 | 11:48:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Defendente | DA_18_Sejuani | 0.9700 |  |
| Jogador 1 | 2-5 | 11:48:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-6 | 11:48:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Inferno | DA_18_Sejuani | -0.0400 |  |
| Jogador 1 | 2-6 | 11:48:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Sejuani | -0.0400 |  |
| Jogador 1 | 2-6 | 11:48:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 2-7 | 11:48:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_18_Sejuani | -0.0100 |  |
| Jogador 1 | 2-7 | 11:48:41 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 3-1 | 11:48:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Inferno | DA_18_Sejuani | -0.0100 |  |
| Jogador 1 | 3-1 | 11:48:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Sejuani | -0.0100 |  |
| Jogador 1 | 3-1 | 11:48:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 3-2 | 11:48:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_18_Sejuani | -0.0100 |  |
| Jogador 1 | 3-2 | 11:48:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Sejuani | 0.0900 |  |
| Jogador 1 | 3-2 | 11:48:56 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Sejuani | 0.4100 |  |
| Jogador 1 | 3-2 | 11:48:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 3-3 | 11:49:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 3-4 | 11:49:09 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Sejuani | 0.6900 |  |
| Jogador 1 | 3-4 | 11:49:10 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_18_Sejuani | 0.5300 |  |
| Jogador 1 | 3-4 | 11:49:10 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_18_Sejuani | 0.1000 |  |
| Jogador 1 | 3-4 | 11:49:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_18_Sejuani | -0.0300 |  |
| Jogador 1 | 3-4 | 11:49:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Sejuani | -0.0300 |  |
| Jogador 1 | 3-4 | 11:49:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 3-5 | 11:49:17 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_18_Shen | 0.2200 |  |
| Jogador 1 | 3-5 | 11:49:17 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_18_Shen | 0.6800 |  |
| Jogador 1 | 3-5 | 11:49:17 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_18_Sejuani | 0.2100 |  |
| Jogador 1 | 3-5 | 11:49:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_18_Sejuani | 0.0000 |  |
| Jogador 1 | 3-6 | 11:49:24 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Inferno | DA_18_Shen | -0.3900 |  |
| Jogador 1 | 3-6 | 11:49:24 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 1 | 3-6 | 11:49:24 | MOVE Bench -> Board: Kog'Maw (i:12.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 1 | 3-6 | 11:49:25 | MOVE Bench -> Board: Shen (i:4.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-6 | 11:49:25 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 3-6 | 11:49:25 | COMPROU: Lux (Feérica) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-6 | 11:49:25 | MOVE Bench -> Board: Lux (Feérica) (i:10.0) <-> Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 3-6 | 11:49:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 11:49:30 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_KogMaw18_AD | 0.3700 |  |
| Jogador 1 | 3-7 | 11:49:31 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 3-7 | 11:49:32 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NeedlesslyLargeRod -> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 1 | 3-7 | 11:49:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 11:49:32 | MOVE Bench -> Board: Rammus (i:6.0) <-> Lux (Feérica) (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 1 | 3-7 | 11:49:32 | MOVE Bench -> Board: Lux (Feérica) (i:10.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 1 | 3-7 | 11:49:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-1 | 11:49:39 | MOVE Bench -> Board: Shen (i:8.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 4-1 | 11:49:39 | MOVE Bench -> Board: Rammus (i:6.0) <-> Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.3200 |  |
| Jogador 1 | 4-1 | 11:49:39 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Inferno | DA_18_Shen | -0.4500 |  |
| Jogador 1 | 4-1 | 11:49:39 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Inferno | DA_18_Shen | 0.4600 |  |
| Jogador 1 | 4-1 | 11:49:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_18_Shen | -0.0900 |  |
| Jogador 1 | 4-1 | 11:49:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-1 | 11:49:40 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-1 | 11:49:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-2 | 11:49:46 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-2 | 11:49:46 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | -0.7000 |  |
| Jogador 1 | 4-2 | 11:49:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-3 | 11:49:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-3 | 11:49:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-4 | 11:50:01 | MOVE Bench -> Board: Shen (i:8.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_18_Shen | 0.1500 |  |
| Jogador 1 | 4-4 | 11:50:01 | MOVE Bench -> Board: Rammus (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_18_Shen | -0.1000 |  |
| Jogador 1 | 4-4 | 11:50:01 | MOVE Bench -> Board: Rammus (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_18_Shen | -0.7000 |  |
| Jogador 1 | 4-4 | 11:50:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-5 | 11:50:09 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 4-5 | 11:50:09 | MOVE Bench -> Board: Shen (i:8.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Inferno | DA_18_Shen | 0.1500 |  |
| Jogador 1 | 4-5 | 11:50:09 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Inferno | DA_18_Shen | 0.4400 |  |
| Jogador 1 | 4-5 | 11:50:10 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 9 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-6 | 11:50:16 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Inferno | DA_18_Shen | 0.3100 |  |
| Jogador 1 | 4-6 | 11:50:17 | MOVE Bench -> Board: Amumu (i:8.0) <-> Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Inferno | DA_18_Shen | -0.3600 |  |
| Jogador 1 | 4-6 | 11:50:17 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 8 | 1 | Inferno | DA_18_Shen | -0.0900 |  |
| Jogador 1 | 4-6 | 11:50:17 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 1 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-6 | 11:50:17 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 1 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-6 | 11:50:18 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 1 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-7 | 11:50:24 | BIGORNA: escolheu componente TFT_Item_RecurveBow | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-7 | 11:50:24 | MOVE Bench -> Board: Shen (i:8.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Inferno | DA_18_Shen | 0.1500 |  |
| Jogador 1 | 4-7 | 11:50:25 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Inferno | DA_18_Shen | 0.1300 |  |
| Jogador 1 | 4-7 | 11:50:25 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-1 | 11:50:33 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 5-1 | 11:50:33 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-2 | 11:50:41 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Inferno | DA_18_Shen | 0.8000 |  |
| Jogador 1 | 5-2 | 11:50:41 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_18_Shen | 0.0300 |  |
| Jogador 1 | 5-2 | 11:50:41 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-3 | 11:50:49 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-4 | 11:50:58 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Inferno | DA_18_Shen | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 5-5 | 11:51:06 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 19 | 1 | Inferno | DA_18_Shen | -0.1900 |  |
| Jogador 1 | 5-6 | 11:51:15 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 27 | 2 | Inferno | DA_18_Shen | -0.2200 |  |
| Jogador 1 | 5-7 | 11:51:23 | BIGORNA: escolheu item completo TFT_Item_UnstableConcoction | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-7 | 11:51:24 | EQUIP_FROM_INVENTORY: TFT_Item_UnstableConcoction -> Lux (Feérica) (i:10.0) (tabuleiro slot 10) | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 5-7 | 11:51:24 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Inferno | DA_18_Shen | 1.0100 |  |
| Jogador 1 | 5-7 | 11:51:24 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 32 | 2 | Inferno | DA_18_Shen | -0.3300 |  |
| Jogador 1 | 6-1 | 11:51:32 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Inferno | DA_18_Shen | -0.3600 |  |
| Jogador 1 | 6-2 | 11:51:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 52 | 4 | Inferno | DA_18_Shen | -0.4000 |  |
| Jogador 1 | 6-3 | 11:51:48 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Inferno | DA_18_Shen | 0.4800 |  |
| Jogador 1 | 6-3 | 11:51:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Inferno | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 6-4 | 11:51:55 | COMPROU: Maokai (Custo 5 \| i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Inferno | DA_18_Shen | 0.1200 |  |
| Jogador 1 | 6-4 | 11:51:56 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Inferno | DA_18_Shen | -0.4100 |  |
| Jogador 2 | ? | 11:47:28 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | -0.0200 |  |
| Jogador 2 | ? | 11:47:28 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3100 |  |
| Jogador 2 | ? | 11:47:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.6000 |  |
| Jogador 2 | ? | 11:47:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-1 | 11:47:34 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 2 | 1-1 | 11:47:34 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.4000 |  |
| Jogador 2 | 1-1 | 11:47:35 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.3600 |  |
| Jogador 2 | 1-1 | 11:47:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-2 | 11:47:40 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1300 |  |
| Jogador 2 | 1-2 | 11:47:40 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.2200 |  |
| Jogador 2 | 1-2 | 11:47:41 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.4600 |  |
| Jogador 2 | 1-2 | 11:47:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 2 | 1-4 | 11:47:53 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | 0.3200 |  |
| Jogador 2 | 1-4 | 11:47:53 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Vi18 | 0.4400 |  |
| Jogador 2 | 1-4 | 11:47:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | -0.0400 |  |
| Jogador 2 | 1-4 | 11:47:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-1 | 11:48:00 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_Vi18 | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-1 | 11:48:00 | COMPROU: Shen (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | 0.0400 |  |
| Jogador 2 | 2-1 | 11:48:00 | MOVE Bench -> Board: Shen (i:4.0) <-> Vi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | -0.3100 |  |
| Jogador 2 | 2-1 | 11:48:01 | MOVE Bench -> Board: Vi (i:6.0) <-> Sejuani (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | -0.3100 |  |
| Jogador 2 | 2-1 | 11:48:01 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-1 | 11:48:05 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | -0.1700 |  |
| Jogador 2 | 2-2 | 11:48:06 | COMPROU: Master Yi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_Vi18 | 0.2500 |  |
| Jogador 2 | 2-2 | 11:48:07 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Shen (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_Vi18 | 0.0800 |  |
| Jogador 2 | 2-2 | 11:48:07 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-2 | 11:48:08 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | 0.0200 |  |
| Jogador 2 | 2-2 | 11:48:08 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-3 | 11:48:13 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_Vi18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-3 | 11:48:13 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_Vi18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-3 | 11:48:14 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | — | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-4 | 11:48:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_Vi18 | 0.0100 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 2 | 2-4 | 11:48:20 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_Vi18 | 0.4500 |  |
| Jogador 2 | 2-4 | 11:48:21 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 2 | 2-5 | 11:48:26 | COMPROU: Master Yi (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.9600 |  |
| Jogador 2 | 2-5 | 11:48:27 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Master Yi (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_MasterYi_AD | -0.4000 |  |
| Jogador 2 | 2-5 | 11:48:27 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 2 | 2-5 | 11:48:27 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 2 | 2-5 | 11:48:28 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 2-6 | 11:48:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 2 | 2-6 | 11:48:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 2 | 2-6 | 11:48:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 2-7 | 11:48:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 2 | 2-7 | 11:48:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 2 | 2-7 | 11:48:41 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 3-1 | 11:48:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 2 | 3-1 | 11:48:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.0800 |  |
| Jogador 2 | 3-1 | 11:48:48 | MOVE Bench -> Board: Shen (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_MasterYi_AD | -0.3200 |  |
| Jogador 2 | 3-1 | 11:48:49 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | -0.3600 |  |
| Jogador 2 | 3-1 | 11:48:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 3-1 | 11:48:53 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_MasterYi_AD | 0.5500 |  |
| Jogador 2 | 3-2 | 11:48:55 | COMPROU: Amumu (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Amumu18 | 0.1300 |  |
| Jogador 2 | 3-2 | 11:48:56 | MOVE Bench -> Board: Amumu (i:8.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Amumu18 | 0.1500 |  |
| Jogador 2 | 3-2 | 11:48:56 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-2 | 11:48:57 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_Amumu18 | 0.2000 |  |
| Jogador 2 | 3-2 | 11:48:57 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-2 | 11:48:57 | MOVE Board -> Board: Master Yi (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | 0.0100 |  |
| Jogador 2 | 3-2 | 11:48:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | 0.0500 |  |
| Jogador 2 | 3-2 | 11:48:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-3 | 11:49:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 3-3 | 11:49:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-3 | 11:49:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-4 | 11:49:09 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 3-4 | 11:49:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-4 | 11:49:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-5 | 11:49:17 | VENDEU: Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Colosso | DA_Amumu18 | -0.4700 |  |
| Jogador 2 | 3-5 | 11:49:17 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_Amumu18 | 0.2000 |  |
| Jogador 2 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-5 | 11:49:18 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-6 | 11:49:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 3-6 | 11:49:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-6 | 11:49:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 3-6 | 11:49:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 3-7 | 11:49:31 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_Amumu18 | 0.0900 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 3-7 | 11:49:32 | MOVE Bench -> Board: Zyra (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Colosso | DA_Amumu18 | 0.6800 |  |
| Jogador 2 | 3-7 | 11:49:32 | COMPROU: Ezreal (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Amumu18 | -0.2900 |  |
| Jogador 2 | 3-7 | 11:49:32 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-1 | 11:49:39 | VENDEU: Ezreal (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 13 | 0 | Colosso | DA_Amumu18 | -0.2700 |  |
| Jogador 2 | 4-1 | 11:49:39 | COMPROU: Nidalee (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Colosso | DA_Amumu18 | 0.1700 |  |
| Jogador 2 | 4-1 | 11:49:39 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-1 | 11:49:39 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-1 | 11:49:40 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-2 | 11:49:46 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 4-2 | 11:49:46 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-2 | 11:49:46 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-3 | 11:49:53 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 11 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-4 | 11:50:01 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 16 | 1 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 4-4 | 11:50:01 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 12 | 1 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-4 | 11:50:01 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 1 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 4-4 | 11:50:02 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 1 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-4 | 11:50:02 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 1 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-4 | 11:50:02 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 1 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-5 | 11:50:09 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-5 | 11:50:09 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-5 | 11:50:09 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-6 | 11:50:16 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_Amumu18 | -0.0900 |  |
| Jogador 2 | 4-6 | 11:50:17 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_Amumu18 | -0.0100 |  |
| Jogador 2 | 4-6 | 11:50:17 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-7 | 11:50:24 | BIGORNA: escolheu componente TFT_Item_TearOfTheGoddess | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Colosso | DA_Amumu18 | 0.0000 |  |
| Jogador 2 | 4-7 | 11:50:24 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_18_Lux_Sunbeam | -0.0900 |  |
| Jogador 2 | 4-7 | 11:50:25 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Amumu (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_18_Lux_Sunbeam | 0.0600 |  |
| Jogador 2 | 4-7 | 11:50:25 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 4-7 | 11:50:29 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_18_Lux_Sunbeam | 0.4500 |  |
| Jogador 2 | 5-1 | 11:50:33 | COMPROU: Ashe (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Colosso | DA_18_Ashe | 0.2100 |  |
| Jogador 2 | 5-1 | 11:50:33 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 9 | 0 | Colosso | DA_18_Ashe | 0.0000 |  |
| Jogador 2 | 5-2 | 11:50:41 | VENDEU: Lux (Solar) (i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 19 | 0 | Colosso | DA_18_Ashe | -0.3800 |  |
| Jogador 2 | 5-2 | 11:50:41 | VENDEU: Ashe (i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 24 | 0 | Colosso | DA_Amumu18 | -0.3800 |  |
| Jogador 2 | 5-2 | 11:50:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 21 | 0 | Colosso | DA_18_MasterYi_AD | 0.8700 |  |
| Jogador 2 | 5-2 | 11:50:42 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 21 | 0 | Colosso | DA_18_MasterYi_AD | 0.5500 |  |
| Jogador 2 | 5-2 | 11:50:42 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 17 | 0 | Colosso | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 2 | 5-2 | 11:50:42 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 13 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:42 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Colosso | DA_18_MasterYi_AD | -0.1100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:42 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:43 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:44 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-3 | 11:50:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_MasterYi_AD | 0.2100 |  |
| Jogador 2 | 5-3 | 11:50:50 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-3 | 11:50:50 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-3 | 11:50:54 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.3900 |  |
| Jogador 2 | 5-4 | 11:50:58 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-5 | 11:51:06 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-6 | 11:51:15 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 1 | Colosso | DA_18_MasterYi_AD | 0.7800 |  |
| Jogador 2 | 5-6 | 11:51:15 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 14 | 1 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-7 | 11:51:23 | BIGORNA: escolheu item completo TFT_Item_IonicSpark | ECON | ECON: acumular até o limite de juros de 50 | 20 | 1 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-7 | 11:51:24 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Amumu (i:8.0) (tabuleiro slot 10) | ECON | ECON: acumular até o limite de juros de 50 | 20 | 1 | Colosso | DA_18_MasterYi_AD | 0.1300 |  |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 16 | 1 | Colosso | DA_18_MasterYi_AD | -0.0900 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 12 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 8 | 1 | Colosso | DA_18_MasterYi_AD | -0.0900 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:25 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:25 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 1 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 6-1 | 11:51:32 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 6-2 | 11:51:40 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Colosso | DA_18_Ahri | 0.7600 |  |
| Jogador 2 | 6-2 | 11:51:40 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Colosso | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 6-2 | 11:51:45 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Colosso | DA_18_Ahri | 0.5800 |  |
| Jogador 2 | 6-3 | 11:51:48 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Colosso | DA_18_Ahri | 0.2000 |  |
| Jogador 2 | 6-3 | 11:51:48 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Colosso | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 6-4 | 11:51:55 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 13 | 0 | Colosso | DA_18_Ahri | 0.0000 |  |
| Jogador 3 | ? | 11:47:28 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 3 | ? | 11:47:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 11:47:34 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 11:47:34 | MOVE Bench -> Board: Yorick (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.7500 |  |
| Jogador 3 | 1-1 | 11:47:35 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.4400 |  |
| Jogador 3 | 1-1 | 11:47:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | 1-1 | 11:47:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 11:47:40 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 11:47:40 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.6600 |  |
| Jogador 3 | 1-2 | 11:47:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 11:47:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0400 |  |
| Jogador 3 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 11:47:53 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.3100 |  |
| Jogador 3 | 1-4 | 11:47:53 | MOVE Bench -> Board: Shen (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | 1-4 | 11:47:54 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.5100 |  |
| Jogador 3 | 1-4 | 11:47:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-1 | 11:48:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 11:48:06 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | — | DA_18_Akali_AD | 0.0200 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-2 | 11:48:07 | COMPROU: Rammus (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Rammus | 0.0200 |  |
| Jogador 3 | 2-2 | 11:48:07 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | — | DA_18_Rammus | 0.4800 |  |
| Jogador 3 | 2-2 | 11:48:08 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Rammus | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-2 | 11:48:08 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 3 | 2-3 | 11:48:13 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Rammus | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-3 | 11:48:13 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Rammus | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-3 | 11:48:14 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Rammus | 0.0000 |  |
| Jogador 3 | 2-4 | 11:48:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Inferno | DA_18_Rammus | 0.0100 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-4 | 11:48:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_18_Tristana | 0.0600 |  |
| Jogador 3 | 2-4 | 11:48:21 | MOVE Bench -> Board: Tristana (i:6.0) <-> Akali (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_18_Tristana | -0.4300 |  |
| Jogador 3 | 2-4 | 11:48:21 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 2-4 | 11:48:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_18_Tristana | 0.5200 |  |
| Jogador 3 | 2-5 | 11:48:26 | COMPROU: Yorick (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Inferno | DA_18_Tristana | 0.9600 |  |
| Jogador 3 | 2-5 | 11:48:27 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Inferno | DA_18_Tristana | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-5 | 11:48:27 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 2-6 | 11:48:33 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Inferno | DA_18_Tristana | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-6 | 11:48:33 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 2-7 | 11:48:41 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Inferno | DA_18_Tristana | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-7 | 11:48:41 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Inferno | DA_18_Tristana | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 2-7 | 11:48:41 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 3-1 | 11:48:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Inferno | DA_18_Tristana | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-1 | 11:48:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_18_Tristana | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 3 | 3-1 | 11:48:48 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 3-2 | 11:48:55 | MOVE Bench -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Tristana | -0.2300 |  |
| Jogador 3 | 3-2 | 11:48:56 | MOVE Bench -> Board: Tristana (i:6.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Tristana | -0.4900 |  |
| Jogador 3 | 3-2 | 11:48:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 3-2 | 11:49:00 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Tristana | 0.5600 |  |
| Jogador 3 | 3-3 | 11:49:02 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_18_Tristana | 0.2800 |  |
| Jogador 3 | 3-3 | 11:49:02 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Inferno | DA_18_Tristana | -0.1800 |  |
| Jogador 3 | 3-3 | 11:49:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Inferno | DA_18_Tristana | -0.0900 |  |
| Jogador 3 | 3-3 | 11:49:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Tristana | -0.0100 |  |
| Jogador 3 | 3-3 | 11:49:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 3-4 | 11:49:09 | VENDEU: Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Inferno | DA_18_Tristana | -0.8200 |  |
| Jogador 3 | 3-4 | 11:49:10 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Inferno | DA_18_Zyra | 0.0500 |  |
| Jogador 3 | 3-4 | 11:49:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-4 | 11:49:10 | MOVE Bench -> Board: Zyra (i:8.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Zyra | -0.7200 |  |
| Jogador 3 | 3-4 | 11:49:10 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Zyra | 0.1800 |  |
| Jogador 3 | 3-4 | 11:49:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-5 | 11:49:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Inferno | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 3-6 | 11:49:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-6 | 11:49:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Inferno | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 3-7 | 11:49:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Inferno | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-7 | 11:49:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 3-7 | 11:49:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 4-1 | 11:49:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_18_Zyra | -0.0100 |  |
| Jogador 3 | 4-1 | 11:49:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Inferno | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 4-2 | 11:49:46 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Inferno | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 4-3 | 11:49:53 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Inferno | DA_18_Zyra | 0.0700 |  |
| Jogador 3 | 4-3 | 11:49:54 | MOVE Bench -> Board: Rammus (i:6.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Inferno | DA_18_Zyra | -0.3500 |  |
| Jogador 3 | 4-3 | 11:49:54 | MOVE Bench -> Board: Zyra (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Inferno | DA_18_Zyra | 0.5000 |  |
| Jogador 3 | 4-3 | 11:49:54 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Inferno | DA_18_Zyra | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-4 | 11:50:01 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Inferno | DA_18_Tristana | 0.8400 |  |
| Jogador 3 | 4-4 | 11:50:01 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 9 | 1 | Inferno | DA_18_Tristana | -0.0900 |  |
| Jogador 3 | 4-4 | 11:50:01 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 5 | 1 | Inferno | DA_18_Tristana | -0.0100 |  |
| Jogador 3 | 4-4 | 11:50:02 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Inferno | DA_18_Tristana | 0.0300 |  |
| Jogador 3 | 4-4 | 11:50:02 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 4-5 | 11:50:09 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 4-6 | 11:50:16 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Inferno | DA_18_Zyra | 0.6500 |  |
| Jogador 3 | 4-6 | 11:50:17 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 8 | 0 | Inferno | DA_18_Zyra | -0.0500 |  |
| Jogador 3 | 4-7 | 11:50:24 | BIGORNA: escolheu componente TFT_Item_SparringGloves | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Inferno | DA_18_Zyra | 0.0000 |  |
| Jogador 3 | 4-7 | 11:50:24 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Inferno | DA_18_Zyra | 0.1800 |  |
| Jogador 3 | 4-7 | 11:50:25 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 14 | 0 | Inferno | DA_18_Zyra | -0.0500 |  |
| Jogador 3 | 5-1 | 11:50:33 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Inferno | DA_18_Tristana | 0.8600 |  |
| Jogador 3 | 5-1 | 11:50:33 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 14 | 1 | Inferno | DA_18_Tristana | -0.1000 |  |
| Jogador 3 | 5-1 | 11:50:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 14 | 1 | Inferno | DA_18_Tristana | -0.0500 |  |
| Jogador 3 | 5-2 | 11:50:41 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Inferno | DA_18_Tristana | -0.1400 |  |
| Jogador 3 | 5-2 | 11:50:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 18 | 1 | Inferno | DA_18_Tristana | -0.1900 |  |
| Jogador 3 | 5-3 | 11:50:49 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 23 | 1 | Inferno | DA_18_Tristana | 0.3400 |  |
| Jogador 3 | 5-3 | 11:50:50 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 23 | 1 | Inferno | DA_18_Tristana | -0.2000 |  |
| Jogador 3 | 5-4 | 11:50:58 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Inferno | DA_18_Tristana | 0.8400 |  |
| Jogador 3 | 5-4 | 11:50:58 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 28 | 2 | Inferno | DA_18_Tristana | -0.2200 |  |
| Jogador 3 | 5-5 | 11:51:06 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | 0.0400 |  |
| Jogador 3 | 5-5 | 11:51:07 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | -0.3000 |  |
| Jogador 4 | ? | 11:47:28 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6000 |  |
| Jogador 4 | ? | 11:47:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 11:47:34 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 11:47:34 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.7400 |  |
| Jogador 4 | 1-1 | 11:47:35 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-1 | 11:47:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | 1-1 | 11:47:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 11:47:40 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.0600 |  |
| Jogador 4 | 1-2 | 11:47:40 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.2700 |  |
| Jogador 4 | 1-2 | 11:47:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 1-4 | 11:47:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | 1.0100 |  |
| Jogador 4 | 1-4 | 11:47:53 | MOVE Bench -> Board: Grompe (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | -1.0100 |  |
| Jogador 4 | 1-4 | 11:47:54 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | 0.4800 |  |
| Jogador 4 | 1-4 | 11:47:54 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 1.1100 |  |
| Jogador 4 | 1-4 | 11:47:55 | MOVE Bench -> Board: Grompe (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 0.0300 |  |
| Jogador 4 | 1-4 | 11:47:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 0.0300 |  |
| Jogador 4 | 1-4 | 11:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-1 | 11:48:00 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | 0.1400 |  |
| Jogador 4 | 2-1 | 11:48:00 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Gromp18_AP | 0.5600 |  |
| Jogador 4 | 2-1 | 11:48:00 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Gromp18_AP | -0.0400 |  |
| Jogador 4 | 2-1 | 11:48:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-2 | 11:48:06 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | — | DA_Gromp18_AP | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-2 | 11:48:07 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-2 | 11:48:07 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_Gromp18_AP | 0.5400 |  |
| Jogador 4 | 2-2 | 11:48:08 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-3 | 11:48:13 | COMPROU: Grompe (Custo 2 \| i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | — | DA_Gromp18_AP | 0.3300 |  |
| Jogador 4 | 2-3 | 11:48:13 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_Gromp18_AP | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-3 | 11:48:14 | MOVE Bench -> Board: Grompe (i:4.0) <-> LeBlanc (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_Gromp18_AP | 0.0500 |  |
| Jogador 4 | 2-3 | 11:48:14 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-4 | 11:48:20 | VENDEU: LeBlanc (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Fera do Rift | DA_Gromp18_AP | -0.3000 |  |
| Jogador 4 | 2-4 | 11:48:20 | COMPROU: Krugue (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | Fera do Rift | DA_Gromp18_AP | 0.8900 |  |
| Jogador 4 | 2-4 | 11:48:21 | MOVE Bench -> Board: Krugue (i:6.0) <-> Grompe (i:4.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 7 | 0 | Fera do Rift | DA_Gromp18_AP | -0.6600 |  |
| Jogador 4 | 2-4 | 11:48:21 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-4 | 11:48:21 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-5 | 11:48:26 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0100 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 4 | 2-5 | 11:48:27 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fera do Rift | DA_Gromp18_AP | 0.4400 |  |
| Jogador 4 | 2-5 | 11:48:27 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fera do Rift | DA_Gromp18_AP | 0.3300 |  |
| Jogador 4 | 2-5 | 11:48:27 | MOVE Board -> Board: Krugue (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0200 |  |
| Jogador 4 | 2-5 | 11:48:28 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-6 | 11:48:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0400 |  |
| Jogador 4 | 2-6 | 11:48:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0400 |  |
| Jogador 4 | 2-6 | 11:48:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 2-7 | 11:48:41 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Fera do Rift | DA_Gromp18_AP | -0.2700 |  |
| Jogador 4 | 2-7 | 11:48:41 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Fera do Rift | DA_Gromp18_AP | -0.4800 |  |
| Jogador 4 | 2-7 | 11:48:41 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Fera do Rift | DA_Gromp18_AP | 0.1400 |  |
| Jogador 4 | 2-7 | 11:48:42 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 2-7 | 11:48:42 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 2-7 | 11:48:42 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-1 | 11:48:48 | VENDEU: Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Fera do Rift | DA_Gromp18_AP | -0.5600 |  |
| Jogador 4 | 3-1 | 11:48:48 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Fera do Rift | DA_Gromp18_AP | 0.2100 |  |
| Jogador 4 | 3-1 | 11:48:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-1 | 11:48:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-2 | 11:48:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-2 | 11:48:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-3 | 11:49:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0800 |  |
| Jogador 4 | 3-3 | 11:49:02 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Fera do Rift | DA_Gromp18_AP | 0.4700 |  |
| Jogador 4 | 3-3 | 11:49:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-3 | 11:49:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-4 | 11:49:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-5 | 11:49:17 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Fera do Rift | DA_Gromp18_AP | 0.7400 |  |
| Jogador 4 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0900 |  |
| Jogador 4 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-5 | 11:49:17 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0100 |  |
| Jogador 4 | 3-5 | 11:49:18 | MOVE Board -> Board: Krugue (i:6.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Fera do Rift | DA_Gromp18_AP | -0.1000 |  |
| Jogador 4 | 3-5 | 11:49:18 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-6 | 11:49:24 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-6 | 11:49:24 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-6 | 11:49:24 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 3-7 | 11:49:31 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Fera do Rift | DA_Gromp18_AP | 0.1100 |  |
| Jogador 4 | 3-7 | 11:49:32 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 3-7 | 11:49:32 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-1 | 11:49:39 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 4-1 | 11:49:39 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-2 | 11:49:46 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Fera do Rift | DA_Gromp18_AP | 0.7600 |  |
| Jogador 4 | 4-2 | 11:49:46 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 4-2 | 11:49:46 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-3 | 11:49:53 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0100 |  |
| Jogador 4 | 4-3 | 11:49:54 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Fera do Rift | DA_Gromp18_AP | 0.3900 |  |
| Jogador 4 | 4-3 | 11:49:54 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-4 | 11:50:01 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Fera do Rift | DA_Gromp18_AP | -0.0400 |  |
| Jogador 4 | 4-4 | 11:50:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-5 | 11:50:09 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.6900 |  |
| Jogador 4 | 4-5 | 11:50:09 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-6 | 11:50:16 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-7 | 11:50:24 | BIGORNA: escolheu componente TFT_Item_BFSword | STABILIZE | STABILIZE: pressão de vida | 13 | 0 | Fera do Rift | DA_Gromp18_AP | 0.0000 |  |
| Jogador 4 | 4-7 | 11:50:24 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.8900 |  |
| Jogador 4 | 4-7 | 11:50:25 | MOVE Bench -> Board: Mamãe Bicuda (i:12.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.3600 |  |
| Jogador 4 | 4-7 | 11:50:25 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Fera do Rift | DA_CrimsonRaptor18 | -0.0900 |  |
| Jogador 4 | 4-7 | 11:50:25 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Fera do Rift | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 4 | 4-7 | 11:50:26 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 4-7 | 11:50:29 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.4500 |  |
| Jogador 4 | 5-1 | 11:50:33 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.3200 |  |
| Jogador 4 | 5-1 | 11:50:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 5 | ? | 11:47:28 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5700 |  |
| Jogador 5 | ? | 11:47:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 11:47:34 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0500 |  |
| Jogador 5 | 1-1 | 11:47:34 | MOVE Bench -> Board: Elise (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.2800 |  |
| Jogador 5 | 1-1 | 11:47:35 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.3100 |  |
| Jogador 5 | 1-1 | 11:47:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | -0.1700 |  |
| Jogador 5 | 1-1 | 11:47:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-2 | 11:47:40 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.2200 |  |
| Jogador 5 | 1-2 | 11:47:40 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.3600 |  |
| Jogador 5 | 1-2 | 11:47:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Elise | 0.0000 |  |
| Jogador 5 | 1-3 | 11:47:47 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Elise | 0.2400 |  |
| Jogador 5 | 1-3 | 11:47:47 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.3000 |  |
| Jogador 5 | 1-3 | 11:47:47 | MOVE Bench -> Board: Elise (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | -0.3700 |  |
| Jogador 5 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 1-4 | 11:47:53 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yunara | 0.3700 |  |
| Jogador 5 | 1-4 | 11:47:53 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 1-4 | 11:47:54 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 1-4 | 11:47:54 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.1000 |  |
| Jogador 5 | 1-4 | 11:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 11:48:00 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 11:48:00 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Cassiopeia | 0.3400 |  |
| Jogador 5 | 2-1 | 11:48:00 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_MasterYi_AD | 0.1300 |  |
| Jogador 5 | 2-1 | 11:48:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 5 | 2-1 | 11:48:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-2 | 11:48:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_MasterYi_AD | 0.0500 |  |
| Jogador 5 | 2-2 | 11:48:07 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_MasterYi_AD | 0.4000 |  |
| Jogador 5 | 2-2 | 11:48:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 5 | 2-2 | 11:48:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-3 | 11:48:13 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_MasterYi_AD | 0.2300 |  |
| Jogador 5 | 2-3 | 11:48:13 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 5 | 2-3 | 11:48:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-4 | 11:48:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 5 | 2-4 | 11:48:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 5 | 2-4 | 11:48:21 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_MasterYi_AD | 0.1200 |  |
| Jogador 5 | 2-4 | 11:48:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-5 | 11:48:26 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_MasterYi_AD | -0.2700 |  |
| Jogador 5 | 2-5 | 11:48:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 5 | 2-5 | 11:48:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-5 | 11:48:32 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_MasterYi_AD | 0.5000 |  |
| Jogador 5 | 2-6 | 11:48:33 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_18_MasterYi_AD | 0.9700 |  |
| Jogador 5 | 2-6 | 11:48:33 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 5 | 2-6 | 11:48:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 2-7 | 11:48:41 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 2-7 | 11:48:41 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 3-1 | 11:48:48 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 3-1 | 11:48:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 3-2 | 11:48:55 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_MasterYi_AD | -0.7800 |  |
| Jogador 5 | 3-2 | 11:48:56 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_18_Ahri | 0.1300 |  |
| Jogador 5 | 3-2 | 11:48:56 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 3-2 | 11:48:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 3-3 | 11:49:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 3-3 | 11:49:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Ahri | 0.0900 |  |
| Jogador 5 | 3-3 | 11:49:03 | MOVE Bench -> Board: Ahri (i:8.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Ahri | 0.1000 |  |
| Jogador 5 | 3-3 | 11:49:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 3-3 | 11:49:07 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Ahri | 0.3400 |  |
| Jogador 5 | 3-4 | 11:49:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_18_Ahri | -0.0900 |  |
| Jogador 5 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 3-5 | 11:49:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 3-6 | 11:49:24 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_18_Ahri | 0.6500 |  |
| Jogador 5 | 3-6 | 11:49:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 3-6 | 11:49:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 3-7 | 11:49:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Florescer | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 3-7 | 11:49:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-1 | 11:49:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-1 | 11:49:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Ahri | -0.0100 |  |
| Jogador 5 | 4-1 | 11:49:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-2 | 11:49:46 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-3 | 11:49:53 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 12 | 0 | Florescer | DA_18_Ahri | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-4 | 11:50:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Florescer | DA_18_Ahri | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-5 | 11:50:09 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Florescer | DA_18_Ahri | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-6 | 11:50:16 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 34 | 2 | Florescer | DA_18_Ahri | -0.2900 |  |
| Jogador 5 | 4-7 | 11:50:24 | BIGORNA: escolheu componente TFT_Item_RecurveBow | ALL_IN | HP crítico: gastar para sobreviver | 42 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 4-7 | 11:50:24 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Florescer | DA_18_Ahri | -0.0400 |  |
| Jogador 5 | 4-7 | 11:50:25 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Master Yi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Florescer | DA_18_Ahri | 0.0900 |  |
| Jogador 5 | 4-7 | 11:50:25 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 38 | 3 | Florescer | DA_18_Ahri | -0.3200 |  |
| Jogador 5 | 5-1 | 11:50:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | -0.3400 |  |
| Jogador 6 | ? | 11:47:28 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | — | 0.0000 |  |
| Jogador 6 | ? | 11:47:28 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 6 | ? | 11:47:29 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6100 |  |
| Jogador 6 | ? | 11:47:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 1-1 | 11:47:34 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 6 | 1-1 | 11:47:34 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.7400 |  |
| Jogador 6 | 1-1 | 11:47:35 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 6 | 1-1 | 11:47:35 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 6 | 1-1 | 11:47:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.4000 |  |
| Jogador 6 | 1-1 | 11:47:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 6 | 1-1 | 11:47:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-2 | 11:47:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0400 |  |
| Jogador 6 | 1-2 | 11:47:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-3 | 11:47:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0400 |  |
| Jogador 6 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-4 | 11:47:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 6 | 1-4 | 11:47:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 1-4 | 11:47:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-4 | 11:47:58 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.1500 |  |
| Jogador 6 | 2-1 | 11:48:00 | COMPROU: Tristana (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Tristana | 0.0900 |  |
| Jogador 6 | 2-1 | 11:48:00 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Tristana | 0.3400 |  |
| Jogador 6 | 2-1 | 11:48:00 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 11:48:06 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 2-2 | 11:48:07 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Tristana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | — | DA_18_Tristana | -0.2900 |  |
| Jogador 6 | 2-2 | 11:48:07 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Tristana | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-2 | 11:48:08 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 11:48:13 | VENDEU: Tristana (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 11 | 0 | — | DA_18_Hecarim | -0.3300 |  |
| Jogador 6 | 2-3 | 11:48:13 | COMPROU: Hecarim (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Hecarim | 0.8700 |  |
| Jogador 6 | 2-3 | 11:48:14 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Hecarim (i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Hecarim | -0.4000 |  |
| Jogador 6 | 2-3 | 11:48:14 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Rakan (i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Hecarim | -0.3300 |  |
| Jogador 6 | 2-3 | 11:48:14 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 6 | 2-4 | 11:48:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 10 | 0 | Colosso | DA_18_Hecarim | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 11:48:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_18_Hecarim | -0.1400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 11:48:21 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_18_Hecarim | 0.0200 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-4 | 11:48:21 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 6 | 2-4 | 11:48:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_18_Hecarim | 0.5300 |  |
| Jogador 6 | 2-5 | 11:48:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 6 | 2-5 | 11:48:27 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-5 | 11:48:27 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-6 | 11:48:33 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-6 | 11:48:33 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 6 | 2-6 | 11:48:34 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-7 | 11:48:41 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-7 | 11:48:41 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 2-7 | 11:48:41 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-1 | 11:48:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 6 | 3-1 | 11:48:48 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-2 | 11:48:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | 3-2 | 11:48:56 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.6700 |  |
| Jogador 6 | 3-2 | 11:48:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-3 | 11:49:02 | COMPROU: Zyra (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Colosso | DA_18_Zyra | -0.0600 |  |
| Jogador 6 | 3-3 | 11:49:02 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 3-3 | 11:49:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 3-4 | 11:49:09 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Zyra | -0.3100 |  |
| Jogador 6 | 3-4 | 11:49:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Zyra | -0.0900 |  |
| Jogador 6 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 3-5 | 11:49:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 3-6 | 11:49:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 3-7 | 11:49:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 3-7 | 11:49:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Zyra | -0.0900 |  |
| Jogador 6 | 3-7 | 11:49:32 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Zyra | -0.0100 |  |
| Jogador 6 | 3-7 | 11:49:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Zyra | 0.0000 |  |
| Jogador 6 | 4-1 | 11:49:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 6 | 4-1 | 11:49:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-2 | 11:49:46 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-3 | 11:49:53 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_KogMaw18_AD | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-4 | 11:50:01 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Colosso | DA_KogMaw18_AD | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-5 | 11:50:09 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 31 | 2 | Colosso | DA_KogMaw18_AD | -0.2100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-6 | 11:50:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Colosso | DA_KogMaw18_AD | 0.9900 |  |
| Jogador 6 | 4-6 | 11:50:17 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 37 | 3 | Colosso | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 6 | 4-7 | 11:50:24 | BIGORNA: escolheu componente TFT_Item_NegatronCloak | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-7 | 11:50:24 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 1.0700 |  |
| Jogador 6 | 4-7 | 11:50:25 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | -0.3300 |  |
| Jogador 6 | 4-7 | 11:50:29 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.4100 |  |
| Jogador 7 | ? | 11:47:28 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6000 |  |
| Jogador 7 | ? | 11:47:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 11:47:34 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 11:47:34 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.9900 |  |
| Jogador 7 | 1-1 | 11:47:35 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.5600 |  |
| Jogador 7 | 1-1 | 11:47:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 11:47:40 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 11:47:40 | MOVE Bench -> Board: Akali (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-2 | 11:47:41 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 7 | 1-2 | 11:47:42 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.3200 |  |
| Jogador 7 | 1-2 | 11:47:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 11:47:53 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 7 | 1-4 | 11:47:53 | MOVE Bench -> Board: Shen (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.1900 |  |
| Jogador 7 | 1-4 | 11:47:54 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.5200 |  |
| Jogador 7 | 1-4 | 11:47:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 7 | 1-4 | 11:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 11:48:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-2 | 11:48:06 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | — | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-3 | 11:48:13 | COMPROU: Azuporã (Custo 4 \| i:8.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 16 | 1 | — | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-3 | 11:48:13 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 16 | 1 | — | DA_Sentinel18 | 0.6100 |  |
| Jogador 7 | 2-3 | 11:48:14 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 12 | 1 | — | DA_Sentinel18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-3 | 11:48:14 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 8 | 1 | — | DA_Sentinel18 | -0.1400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-3 | 11:48:14 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 1 | — | DA_Sentinel18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-3 | 11:48:15 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 1 | — | DA_Sentinel18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-3 | 11:48:15 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 1 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 11:48:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Inferno | DA_Sentinel18 | 0.0200 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-4 | 11:48:20 | COMPROU: Xayah (Custo 1 \| i:2.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 2-4 | 11:48:21 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 2-4 | 11:48:21 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 11:48:25 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_Sentinel18 | 0.3600 |  |
| Jogador 7 | 2-5 | 11:48:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Inferno | DA_Sentinel18 | 0.3200 |  |
| Jogador 7 | 2-5 | 11:48:27 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-6 | 11:48:33 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Inferno | DA_Sentinel18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-6 | 11:48:33 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_Sentinel18 | -0.0600 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-6 | 11:48:34 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 0 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 11:48:41 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Inferno | DA_Sentinel18 | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 2-7 | 11:48:41 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 1 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-1 | 11:48:48 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Inferno | DA_Sentinel18 | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 3-1 | 11:48:48 | PASSOU TURNO | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 11:48:55 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 5 | 0 | Inferno | DA_Sentinel18 | -0.0300 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 7 | 3-2 | 11:48:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Inferno | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 3-2 | 11:48:56 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_Sentinel18 | 0.7800 |  |
| Jogador 7 | 3-2 | 11:48:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-3 | 11:49:02 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_Sentinel18 | 0.7300 |  |
| Jogador 7 | 3-3 | 11:49:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-4 | 11:49:09 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 10 | 0 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-5 | 11:49:17 | COMPROU: Morgana (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Inferno | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 3-5 | 11:49:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-6 | 11:49:24 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Inferno | DA_Sentinel18 | 0.7700 |  |
| Jogador 7 | 3-6 | 11:49:24 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-6 | 11:49:24 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 11 | 1 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-6 | 11:49:25 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 7 | 1 | Inferno | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 3-6 | 11:49:25 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Inferno | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-6 | 11:49:25 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 11:49:31 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 11 | 0 | Inferno | DA_Sentinel18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-1 | 11:49:39 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Inferno | DA_Sentinel18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-2 | 11:49:46 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | -0.2700 |  |
| Jogador 8 | ? | 11:47:28 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.6000 |  |
| Jogador 8 | ? | 11:47:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 11:47:34 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 8 | 1-1 | 11:47:34 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.8200 |  |
| Jogador 8 | 1-1 | 11:47:35 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.5100 |  |
| Jogador 8 | 1-1 | 11:47:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 11:47:40 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.3100 |  |
| Jogador 8 | 1-2 | 11:47:40 | MOVE Bench -> Board: Yorick (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 8 | 1-2 | 11:47:41 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.8200 |  |
| Jogador 8 | 1-2 | 11:47:42 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.2500 |  |
| Jogador 8 | 1-2 | 11:47:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 11:47:45 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4000 |  |
| Jogador 8 | 1-3 | 11:47:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 11:47:53 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 1.0200 |  |
| Jogador 8 | 1-4 | 11:47:53 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 8 | 1-4 | 11:47:54 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-4 | 11:47:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | -0.0400 |  |
| Jogador 8 | 1-4 | 11:47:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0400 |  |
| Jogador 8 | 1-4 | 11:47:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 2-1 | 11:48:00 | COMPROU: Krugue (Custo 3 \| i:6.0) | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 3 | 0 | — | DA_Krug18 | 0.0100 |  |
| Jogador 8 | 2-1 | 11:48:00 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Krug18 | 0.4700 |  |
| Jogador 8 | 2-1 | 11:48:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-2 | 11:48:06 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_Krug18 | 0.0300 |  |
| Jogador 8 | 2-2 | 11:48:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Krug18 | -0.0400 |  |
| Jogador 8 | 2-2 | 11:48:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Krug18 | 0.0000 |  |
| Jogador 8 | 2-3 | 11:48:13 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_Krug18 | -0.3800 |  |
| Jogador 8 | 2-3 | 11:48:13 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_Krug18 | 0.1800 |  |
| Jogador 8 | 2-3 | 11:48:14 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_MasterYi_AD | -0.2200 |  |
| Jogador 8 | 2-3 | 11:48:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_MasterYi_AD | -0.1200 |  |
| Jogador 8 | 2-3 | 11:48:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_MasterYi_AD | -0.0400 |  |
| Jogador 8 | 2-3 | 11:48:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-4 | 11:48:20 | MOVE Bench -> Board: Krugue (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Krug18 | -0.0400 |  |
| Jogador 8 | 2-4 | 11:48:20 | BUY XP | SLOWROLL | SLOWROLL: composição tem alvo de 3 estrelas | 4 | 0 | Colosso | DA_Krug18 | 0.0400 | SLOWROLL_BUY_XP_REVIEW |
| Jogador 8 | 2-4 | 11:48:21 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Krug18 | -0.8000 |  |
| Jogador 8 | 2-4 | 11:48:21 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Krug18 | 0.3700 |  |
| Jogador 8 | 2-4 | 11:48:21 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Krug18 | 0.0400 |  |
| Jogador 8 | 2-4 | 11:48:22 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_MasterYi_AD | -0.3300 |  |
| Jogador 8 | 2-4 | 11:48:22 | MOVE Bench -> Board: Krugue (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_MasterYi_AD | -0.3900 |  |
| Jogador 8 | 2-4 | 11:48:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 8 | 2-4 | 11:48:25 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_MasterYi_AD | 0.5500 |  |
| Jogador 8 | 2-5 | 11:48:26 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Soraka | 0.2900 |  |
| Jogador 8 | 2-5 | 11:48:27 | MOVE Bench -> Board: Soraka (i:8.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Soraka | 0.1700 |  |
| Jogador 8 | 2-5 | 11:48:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Soraka | -0.0400 |  |
| Jogador 8 | 2-5 | 11:48:27 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Soraka | 0.0200 |  |
| Jogador 8 | 2-5 | 11:48:28 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Soraka | 0.0700 |  |
| Jogador 8 | 2-5 | 11:48:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 2-6 | 11:48:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Soraka | -0.1200 |  |
| Jogador 8 | 2-6 | 11:48:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Soraka | -0.0400 |  |
| Jogador 8 | 2-6 | 11:48:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 2-7 | 11:48:41 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Soraka | -0.3000 |  |
| Jogador 8 | 2-7 | 11:48:41 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Soraka | 0.0500 |  |
| Jogador 8 | 2-7 | 11:48:41 | MOVE Bench -> Board: Lillia (i:8.0) <-> Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Lillia | -0.7400 |  |
| Jogador 8 | 2-7 | 11:48:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 2-7 | 11:48:42 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 2-7 | 11:48:42 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-1 | 11:48:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Lillia | -0.0100 |  |
| Jogador 8 | 3-1 | 11:48:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Lillia | 0.0600 |  |
| Jogador 8 | 3-1 | 11:48:48 | MOVE Bench -> Board: Soraka (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Soraka | -0.0500 |  |
| Jogador 8 | 3-1 | 11:48:49 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Soraka | -0.5600 |  |
| Jogador 8 | 3-1 | 11:48:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-1 | 11:48:53 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Soraka | 0.4800 |  |
| Jogador 8 | 3-2 | 11:48:55 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-2 | 11:48:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-3 | 11:49:02 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Soraka | 0.7100 |  |
| Jogador 8 | 3-3 | 11:49:02 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Soraka | -0.4000 |  |
| Jogador 8 | 3-3 | 11:49:03 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-3 | 11:49:03 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Soraka (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Lillia | -0.2900 |  |
| Jogador 8 | 3-3 | 11:49:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Lillia | 0.0000 |  |
| Jogador 8 | 3-4 | 11:49:09 | MOVE Bench -> Board: Soraka (i:8.0) <-> Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-4 | 11:49:10 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-4 | 11:49:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-5 | 11:49:17 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-5 | 11:49:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-6 | 11:49:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-6 | 11:49:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-6 | 11:49:24 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 3-7 | 11:49:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 3-7 | 11:49:32 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Soraka | 0.1300 |  |
| Jogador 8 | 3-7 | 11:49:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-1 | 11:49:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 4-1 | 11:49:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Soraka | -0.0100 |  |
| Jogador 8 | 4-1 | 11:49:39 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-2 | 11:49:46 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Colosso | DA_18_Soraka | 0.0800 |  |
| Jogador 8 | 4-2 | 11:49:46 | VENDEU: Leona (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 5 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-2 | 11:49:46 | COMPROU: Sivir (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_18_Soraka | -0.2300 |  |
| Jogador 8 | 4-2 | 11:49:47 | MOVE Bench -> Board: Sivir (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_18_Soraka | 0.5300 |  |
| Jogador 8 | 4-2 | 11:49:47 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 1 | 0 | Colosso | DA_18_Soraka | 0.0000 |  |
| Jogador 8 | 4-3 | 11:49:53 | COMPROU: Azuporã (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 8 | 4-3 | 11:49:54 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Master Yi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 8 | 4-3 | 11:49:54 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 8 | 4-3 | 11:49:54 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 8 | 4-4 | 11:50:01 | COMPROU: Soraka (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_Sentinel18 | 0.7800 |  |
| Jogador 8 | 4-4 | 11:50:01 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 8 | 4-5 | 11:50:09 | COMPROU: Amumu (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Colosso | DA_Sentinel18 | 0.2600 |  |
| Jogador 8 | 4-5 | 11:50:09 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 8 | 4-5 | 11:50:09 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 8 | 4-6 | 11:50:16 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 8 | 4-7 | 11:50:24 | BIGORNA: escolheu componente TFT_Item_NegatronCloak | WINSTREAK | WINSTREAK: preservar vantagem atual | 15 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 8 | 4-7 | 11:50:24 | COMPROU: Lux (Sabugueiro) (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 10 | 0 | Colosso | DA_18_Lux_Elderwood | -0.1700 |  |
| Jogador 8 | 4-7 | 11:50:25 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 6 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0800 |  |
| Jogador 8 | 4-7 | 11:50:25 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 |  |
| Jogador 8 | 4-7 | 11:50:25 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 2 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-1 | 11:50:33 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 7 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0800 |  |
| Jogador 8 | 5-1 | 11:50:33 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 |  |
| Jogador 8 | 5-1 | 11:50:33 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 3 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-2 | 11:50:41 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 8 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0800 |  |
| Jogador 8 | 5-2 | 11:50:41 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 4 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 |  |
| Jogador 8 | 5-2 | 11:50:41 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 |  |
| Jogador 8 | 5-2 | 11:50:42 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 0 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-3 | 11:50:49 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-3 | 11:50:50 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-4 | 11:50:58 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-4 | 11:50:58 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-5 | 11:51:06 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0600 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-5 | 11:51:07 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-5 | 11:51:11 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0500 |  |
| Jogador 8 | 5-6 | 11:51:15 | COMPROU: Dragão Ancião (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Colosso | DA_18_ElderDragon | 0.0500 |  |
| Jogador 8 | 5-6 | 11:51:15 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_ElderDragon | -0.0100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-6 | 11:51:15 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_ElderDragon | 0.0000 |  |
| Jogador 8 | 5-7 | 11:51:23 | BIGORNA: escolheu item completo TFT_Item_LastWhisper | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_ElderDragon | 0.0000 |  |
| Jogador 8 | 5-7 | 11:51:24 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Azuporã (i:8.0) (tabuleiro slot 10) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_ElderDragon | 0.1100 |  |
| Jogador 8 | 5-7 | 11:51:24 | MOVE Bench -> Board: Soraka (i:8.0) <-> Sivir (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_ElderDragon | -1.0000 |  |
| Jogador 8 | 5-7 | 11:51:24 | MOVE Bench -> Board: Sivir (i:8.0) <-> Azuporã (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_ElderDragon | -0.3000 |  |
| Jogador 8 | 5-7 | 11:51:24 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_ElderDragon | 0.0000 |  |
| Jogador 8 | 6-1 | 11:51:32 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_18_ElderDragon | -0.0900 |  |
| Jogador 8 | 6-1 | 11:51:32 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_ElderDragon | -0.0100 |  |
| Jogador 8 | 6-1 | 11:51:32 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_ElderDragon | 0.0000 |  |
| Jogador 8 | 6-2 | 11:51:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 9 | 0 | Colosso | DA_18_ElderDragon | -0.0500 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 37 | 37 | 185 | 37 | 20 | 131 | 11 | 6 |
| Jogador 2 | 37 | 37 | 185 | 37 | 27 | 139 | 10 | 2 |
| Jogador 3 | 31 | 31 | 155 | 31 | 21 | 93 | 10 | 6 |
| Jogador 4 | 27 | 27 | 135 | 27 | 10 | 94 | 6 | 6 |
| Jogador 5 | 27 | 27 | 135 | 27 | 17 | 77 | 8 | 4 |
| Jogador 6 | 26 | 26 | 130 | 26 | 16 | 76 | 10 | 5 |
| Jogador 7 | 21 | 21 | 105 | 21 | 11 | 58 | 3 | 6 |
| Jogador 8 | 35 | 35 | 175 | 35 | 18 | 128 | 15 | 4 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 131 | 131 | 131 | 0 | 127 | 0 | 131 | 131 | 131 | 22/9 |
| Jogador 2 | 139 | 139 | 139 | 0 | 135 | 0 | 139 | 139 | 139 | 20/10 |
| Jogador 3 | 93 | 93 | 93 | 0 | 91 | 0 | 93 | 93 | 93 | 16/3 |
| Jogador 4 | 94 | 94 | 94 | 0 | 92 | 0 | 94 | 94 | 94 | 17/7 |
| Jogador 5 | 77 | 77 | 77 | 0 | 75 | 0 | 77 | 77 | 77 | 10/2 |
| Jogador 6 | 76 | 76 | 76 | 0 | 75 | 0 | 76 | 76 | 76 | 12/6 |
| Jogador 7 | 58 | 58 | 58 | 0 | 58 | 0 | 58 | 58 | 58 | 9/0 |
| Jogador 8 | 128 | 128 | 128 | 0 | 124 | 0 | 128 | 128 | 128 | 16/4 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5151995420455933 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.298336386680603 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31793826818466187 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 35 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 58 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2148882895708084 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.284455806016922 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 87 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08337453007698059 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2131052017211914 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4028262495994568 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 120 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 121 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 142 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0183649063110352 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 143 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 144 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2228897511959076 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 145 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 170 | SELL | STABILIZE | 94.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4276371896266937 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 2-3 | 171 | BUY | STABILIZE | 94.0 | 4 | 13 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.113450288772583 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f,7aea963f-f0a4-4fa2-8da0-cc5eb260f665 |
| Jogador 1 | 2-3 | 172 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 11 | 1 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15346157550811768 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 173 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2690533697605133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 174 | BUY | STABILIZE | 94.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26912450790405273 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 175 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.534747838973999 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 176 | BUY_XP | STABILIZE | 94.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 177 | BUY_XP | SLOWROLL | 94.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17800000309944153 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 178 | MOVE_BOARD | SLOWROLL | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 179 | PASS | SLOWROLL | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 194 | BUY | SLOWROLL | 89.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29846787452697754 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 195 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8189994096755981 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 196 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 197 | PASS | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 220 | BUY | SLOWROLL | 89.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9661908149719238 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 221 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 22.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 222 | MOVE_BOARD | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | Defendente/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23413696885108948 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 223 | MOVE_BOARD | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | Defendente/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09808357805013657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 224 | PASS | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | Defendente/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 242 | MOVE_BENCH | SLOWROLL | 83.0 | 6 | 6 | 0 | 22.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002918649115599692 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 243 | MOVE_BENCH | SLOWROLL | 83.0 | 6 | 6 | 0 | 18.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5310449004173279 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 244 | BUY | FAST8 | 83.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.965160608291626 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 245 | PASS | FAST8 | 83.0 | 6 | 3 | 0 | 26.0 | Defendente/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 266 | BUY_XP | FAST8 | 83.0 | 6 | 9 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 267 | BUY_XP | FAST8 | 83.0 | 6 | 5 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 268 | PASS | FAST8 | 83.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 292 | BUY_XP | FAST8 | 83.0 | 6 | 6 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 293 | PASS | FAST8 | 83.0 | 6 | 2 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 316 | BUY_XP | FAST8 | 83.0 | 6 | 9 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 317 | BUY_XP | FAST8 | 83.0 | 6 | 5 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 318 | PASS | FAST8 | 83.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 340 | BUY_XP | FAST8 | 83.0 | 6 | 8 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 341 | BUY_XP | FAST8 | 83.0 | 6 | 4 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08860000222921371 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 342 | MOVE_BENCH | FAST8 | 83.0 | 7 | 0 | 0 | 26.0 | Inferno/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4055789113044739 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 343 | PASS | FAST8 | 83.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 361 | PASS | FAST8 | 72.0 | 7 | 5 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 382 | BUY | FAST8 | 72.0 | 7 | 10 | 1 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6859604716300964 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 383 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 8 | 0 | 24.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5331472754478455 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 384 | MOVE_BOARD | FAST8 | 72.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09555917233228683 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 385 | BUY_XP | FAST8 | 72.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 386 | BUY_XP | FAST8 | 72.0 | 7 | 4 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 387 | PASS | FAST8 | 72.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 405 | BUY | FAST8 | 61.0 | 7 | 6 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21597778797149658 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 406 | MOVE_BENCH | FAST8 | 61.0 | 7 | 4 | 0 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6825709342956543 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 407 | BUY | FAST8 | 61.0 | 7 | 4 | 0 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21458622813224792 | 0.0 | 0.0 | +da5abe09-7f54-4361-8d82-84427a9da9e1 / -— |
| Jogador 1 | 3-6 | 408 | PASS | FAST8 | 61.0 | 7 | 2 | 0 | 36.0 | Inferno/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 424 | SELL | FAST8 | 61.0 | 7 | 8 | 0 | 36.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3909077048301697 | 0.0 | 0.0 | +— / -da5abe09-7f54-4361-8d82-84427a9da9e1 |
| Jogador 1 | 3-7 | 425 | BUY | FAST8 | 61.0 | 7 | 10 | 1 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6835959553718567 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 3-7 | 426 | MOVE_BENCH | STABILIZE | 61.0 | 7 | 7 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4090084433555603 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 427 | MOVE_BENCH | FAST8 | 61.0 | 7 | 7 | 0 | 32.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10021308809518814 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 428 | MOVE_BENCH | FAST8 | 61.0 | 7 | 7 | 0 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13648463785648346 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 429 | BUY | FAST8 | 61.0 | 7 | 7 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08391796052455902 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 430 | MOVE_BENCH | FAST8 | 61.0 | 7 | 2 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09058135002851486 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 431 | PASS | FAST8 | 61.0 | 7 | 2 | 0 | 44.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 441 | MOVE_BENCH | FAST8 | 61.0 | 7 | 2 | 0 | 44.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37480056285858154 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 443 | BUY | FAST8 | 61.0 | 7 | 7 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.05127935856580734 | 0.0 | 0.0 | +8ff9f97f-9d27-44d5-ae97-a6d618c568a1 / -— |
| Jogador 1 | 4-1 | 444 | CRAFT_AND_EQUIP | FAST8 | 61.0 | 7 | 4 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22672857344150543 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 445 | BUY_XP | FAST8 | 61.0 | 7 | 4 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 446 | MOVE_BENCH | FAST8 | 61.0 | 7 | 0 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37574541568756104 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 447 | MOVE_BENCH | FAST8 | 61.0 | 7 | 0 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3807571232318878 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 448 | PASS | FAST8 | 61.0 | 7 | 0 | 0 | 44.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 463 | MOVE_BENCH | FAST8 | 61.0 | 7 | 7 | 0 | 44.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15243515372276306 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 464 | MOVE_BENCH | FAST8 | 61.0 | 7 | 7 | 0 | 46.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3176153898239136 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 465 | SELL | FAST8 | 61.0 | 7 | 7 | 0 | 40.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4464474618434906 | 0.0 | 0.0 | +— / -227dbcdb-af5c-4318-94d1-f01a7847d100 |
| Jogador 1 | 4-2 | 466 | BUY | FAST8 | 61.0 | 7 | 15 | 1 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.46408599615097046 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 467 | BUY_XP | FAST8 | 61.0 | 7 | 12 | 1 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 468 | BUY_XP | FAST8 | 61.0 | 7 | 8 | 0 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 469 | BUY_XP | FAST8 | 61.0 | 7 | 4 | 0 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 470 | PASS | FAST8 | 61.0 | 7 | 0 | 0 | 40.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 483 | BUY_XP | FAST8 | 49.0 | 7 | 5 | 0 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 484 | MOVE_BENCH | FAST8 | 49.0 | 7 | 1 | 0 | 40.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6971969604492188 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 485 | PASS | FAST8 | 49.0 | 7 | 1 | 0 | 38.0 | Inferno/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 502 | BUY_XP | FAST8 | 49.0 | 7 | 7 | 0 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 503 | PASS | FAST8 | 49.0 | 7 | 3 | 0 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 522 | MOVE_BENCH | FAST8 | 49.0 | 7 | 8 | 0 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15242226421833038 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 523 | MOVE_BENCH | FAST8 | 49.0 | 7 | 8 | 0 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 524 | MOVE_BENCH | FAST8 | 49.0 | 7 | 8 | 0 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6971969604492188 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 525 | PASS | FAST8 | 49.0 | 7 | 8 | 0 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 542 | BUY_XP | STABILIZE | 37.0 | 7 | 13 | 1 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03490093722939491 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 543 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 9 | 0 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15242226421833038 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 544 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 9 | 0 | 40.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4368264973163605 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 545 | PASS | STABILIZE | 37.0 | 8 | 9 | 0 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 562 | BUY | STABILIZE | 37.0 | 8 | 16 | 1 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31237828731536865 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 1 | 4-7 | 563 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 12 | 1 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3609406650066376 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 564 | BUY_XP | STABILIZE | 37.0 | 8 | 12 | 1 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 565 | BUY_XP | STABILIZE | 37.0 | 8 | 8 | 0 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 566 | BUY_XP | STABILIZE | 37.0 | 8 | 4 | 0 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 567 | PASS | STABILIZE | 37.0 | 8 | 0 | 0 | 46.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 582 | ANVIL_CHOICE | STABILIZE | 37.0 | 8 | 5 | 0 | 46.0 | Inferno/DA_18_Shen | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 583 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 5 | 0 | 46.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15239834785461426 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 584 | BUY | STABILIZE | 37.0 | 8 | 5 | 0 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13477998971939087 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 1 | 5-1 | 585 | PASS | STABILIZE | 37.0 | 8 | 1 | 0 | 48.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 602 | BUY_XP | STABILIZE | 21.0 | 8 | 6 | 0 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 603 | PASS | STABILIZE | 21.0 | 8 | 2 | 0 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 622 | BUY | STABILIZE | 21.0 | 8 | 8 | 0 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8011893630027771 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -— |
| Jogador 1 | 5-3 | 623 | BUY_XP | STABILIZE | 21.0 | 8 | 4 | 0 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 624 | PASS | STABILIZE | 21.0 | 8 | 0 | 0 | 48.0 | Inferno/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 642 | PASS | STABILIZE | 21.0 | 8 | 7 | 0 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 662 | PASS | STABILIZE | 21.0 | 8 | 13 | 1 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 682 | PASS | ALL_IN | 5.0 | 8 | 19 | 1 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19210952520370483 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 702 | PASS | ALL_IN | 5.0 | 8 | 27 | 2 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2192544937133789 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 722 | ANVIL_CHOICE | ALL_IN | 5.0 | 8 | 34 | 3 | 48.0 | Inferno/DA_18_Shen | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 723 | EQUIP_FROM_INVENTORY | ALL_IN | 5.0 | 8 | 34 | 3 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05926163122057915 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 724 | BUY | ALL_IN | 5.0 | 8 | 34 | 3 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0071743726730347 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 1 | 6-1 | 725 | PASS | ALL_IN | 5.0 | 8 | 32 | 3 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32514920830726624 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 742 | PASS | ALL_IN | 5.0 | 8 | 42 | 4 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35647618770599365 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 762 | PASS | ALL_IN | 5.0 | 8 | 52 | 5 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40055057406425476 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 778 | BUY | ALL_IN | 5.0 | 8 | 64 | 5 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4808681309223175 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 1 | 6-4 | 779 | PASS | ALL_IN | 5.0 | 8 | 61 | 5 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40727248787879944 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 795 | BUY | ALL_IN | 5.0 | 8 | 72 | 5 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11753745377063751 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 1 | 6-5 | 796 | PASS | ALL_IN | 5.0 | 8 | 67 | 5 | 48.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4121488630771637 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3124316334724426 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5974857807159424 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35926106572151184 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 34 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 58 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.13341598212718964 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21954044699668884 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46339863538742065 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 61 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 87 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3188125193119049 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4403737783432007 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 119 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 120 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 142 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 143 | BUY | SLOWROLL | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.03889692574739456 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 144 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30646535754203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 145 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30629318952560425 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 146 | PASS | SLOWROLL | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 163 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17107032239437103 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 170 | BUY | SLOWROLL | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24753046035766602 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 171 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 5 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07597079873085022 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 172 | BUY_XP | SLOWROLL | 100.0 | 5 | 5 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 173 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 1 | 0 | 20.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 174 | PASS | SLOWROLL | 100.0 | 5 | 1 | 0 | 20.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 194 | BUY_XP | SLOWROLL | 100.0 | 5 | 8 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 195 | BUY_XP | SLOWROLL | 100.0 | 5 | 4 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 196 | PASS | SLOWROLL | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 220 | BUY_XP | SLOWROLL | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011409999802708626 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 221 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4464481770992279 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 222 | PASS | SLOWROLL | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 242 | BUY | SLOWROLL | 100.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.964647114276886 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 243 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 244 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02349487878382206 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 245 | BUY_XP | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 246 | PASS | FAST8 | 100.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 266 | BUY_XP | FAST8 | 100.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 267 | BUY_XP | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 268 | PASS | FAST8 | 100.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 292 | BUY_XP | FAST8 | 100.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 293 | BUY_XP | FAST8 | 100.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 294 | PASS | FAST8 | 100.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 316 | BUY_XP | FAST8 | 100.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 317 | BUY_XP | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 318 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32382357120513916 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 319 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 2 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35604196786880493 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 320 | PASS | FAST8 | 100.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 333 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5461198091506958 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 340 | BUY | FAST8 | 100.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1255544126033783 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 341 | MOVE_BENCH | FAST8 | 100.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14571718871593475 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 342 | SELL | FAST8 | 100.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008493784815073013 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 3-3 | 343 | BUY | FAST8 | 100.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20345762372016907 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 344 | BUY_XP | FAST8 | 100.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 345 | MOVE_BOARD | FAST8 | 100.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010701649822294712 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 346 | MOVE_BOARD | FAST8 | 100.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047093361616134644 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 347 | PASS | FAST8 | 100.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 361 | BUY_XP | FAST8 | 100.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 362 | BUY_XP | FAST8 | 100.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 363 | PASS | FAST8 | 100.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 382 | BUY_XP | FAST8 | 100.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 383 | BUY_XP | FAST8 | 100.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 384 | PASS | FAST8 | 100.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 405 | SELL | FAST8 | 100.0 | 7 | 11 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47464242577552795 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-6 | 406 | BUY | FAST8 | 100.0 | 7 | 15 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2023088037967682 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 407 | BUY_XP | FAST8 | 100.0 | 7 | 11 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 408 | BUY_XP | FAST8 | 100.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 409 | PASS | FAST8 | 100.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 424 | BUY_XP | FAST8 | 100.0 | 7 | 12 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 425 | BUY_XP | FAST8 | 100.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 426 | BUY_XP | FAST8 | 100.0 | 7 | 4 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 427 | PASS | FAST8 | 100.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 443 | BUY_XP | FAST8 | 100.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0853937491774559 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 444 | MOVE_BENCH | ECON | 100.0 | 8 | 4 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6816802620887756 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 445 | BUY | WINSTREAK | 100.0 | 8 | 4 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2873739004135132 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 446 | PASS | WINSTREAK | 100.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 463 | SELL | WINSTREAK | 100.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2746615409851074 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-2 | 464 | BUY | WINSTREAK | 100.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16872823238372803 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 2 | 4-2 | 465 | BUY_XP | WINSTREAK | 100.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 466 | BUY_XP | WINSTREAK | 100.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 467 | PASS | WINSTREAK | 100.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 483 | BUY_XP | WINSTREAK | 100.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 484 | BUY_XP | WINSTREAK | 100.0 | 8 | 6 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 485 | PASS | WINSTREAK | 100.0 | 8 | 2 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 502 | PASS | WINSTREAK | 100.0 | 8 | 11 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 522 | BUY_XP | WINSTREAK | 100.0 | 8 | 20 | 2 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 523 | BUY_XP | WINSTREAK | 100.0 | 8 | 16 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 524 | BUY_XP | WINSTREAK | 100.0 | 8 | 12 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 525 | BUY_XP | WINSTREAK | 100.0 | 8 | 8 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 526 | BUY_XP | WINSTREAK | 100.0 | 8 | 4 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 527 | PASS | WINSTREAK | 100.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 542 | BUY_XP | WINSTREAK | 100.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 543 | BUY_XP | WINSTREAK | 100.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 544 | PASS | WINSTREAK | 100.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 562 | BUY_XP | WINSTREAK | 100.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 563 | BUY_XP | WINSTREAK | 100.0 | 8 | 6 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 564 | PASS | WINSTREAK | 100.0 | 8 | 2 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 582 | ANVIL_CHOICE | WINSTREAK | 100.0 | 9 | 10 | 1 | 42.0 | Colosso/DA_Amumu18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 583 | BUY | WINSTREAK | 100.0 | 9 | 10 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0896470919251442 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 2 | 5-1 | 584 | CRAFT_AND_EQUIP | WINSTREAK | 100.0 | 9 | 5 | 0 | 42.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.05668513476848602 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 585 | PASS | WINSTREAK | 100.0 | 9 | 5 | 0 | 42.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 600 | MOVE_BENCH | WINSTREAK | 100.0 | 9 | 5 | 0 | 42.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4493187963962555 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 602 | BUY | WINSTREAK | 100.0 | 9 | 14 | 1 | 50.0 | Colosso/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20746761560440063 | 0.0 | 0.0 | +eeb774dc-b3d1-4a90-8a93-b71a9b754169 / -— |
| Jogador 2 | 5-2 | 603 | PASS | WINSTREAK | 100.0 | 9 | 9 | 0 | 50.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 622 | SELL | ECON | 84.0 | 9 | 14 | 1 | 50.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38404616713523865 | 0.0 | 0.0 | +— / -24b29fe6-466c-42d5-9f92-5d6114f0f98f |
| Jogador 2 | 5-3 | 623 | SELL | ECON | 84.0 | 9 | 19 | 1 | 50.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3756938576698303 | 0.0 | 0.0 | +— / -eeb774dc-b3d1-4a90-8a93-b71a9b754169 |
| Jogador 2 | 5-3 | 624 | BUY | ECON | 84.0 | 9 | 24 | 2 | 50.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8650518655776978 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -6f3f86ec-6928-4032-a1ef-533a68865516,8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 5-3 | 625 | MOVE_BENCH | ECON | 84.0 | 9 | 21 | 2 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5452604293823242 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 626 | BUY | ECON | 84.0 | 9 | 21 | 2 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09414844959974289 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 2 | 5-3 | 627 | BUY_XP | ECON | 84.0 | 9 | 17 | 1 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 628 | BUY_XP | ECON | 84.0 | 9 | 13 | 1 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 629 | BUY_XP | ECON | 84.0 | 9 | 9 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 630 | BUY_XP | ECON | 84.0 | 9 | 5 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 631 | PASS | ECON | 84.0 | 9 | 1 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 642 | BUY | ECON | 68.0 | 9 | 7 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21357329189777374 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 2 | 5-4 | 643 | BUY_XP | ECON | 68.0 | 9 | 4 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 644 | PASS | ECON | 68.0 | 9 | 0 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 660 | MOVE_BENCH | ECON | 68.0 | 9 | 0 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3886490762233734 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 662 | PASS | ECON | 68.0 | 9 | 6 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 682 | PASS | ECON | 68.0 | 9 | 12 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 702 | BUY | ECON | 51.0 | 9 | 18 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7849748134613037 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 2 | 5-7 | 703 | PASS | ECON | 51.0 | 9 | 14 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 722 | ANVIL_CHOICE | ECON | 51.0 | 9 | 20 | 2 | 58.0 | Colosso/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 723 | EQUIP_FROM_INVENTORY | ECON | 51.0 | 9 | 20 | 2 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13128811120986938 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 724 | BUY_XP | ECON | 51.0 | 9 | 20 | 2 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 725 | BUY_XP | ECON | 51.0 | 9 | 16 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 726 | BUY_XP | ECON | 51.0 | 9 | 12 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 727 | BUY_XP | ECON | 51.0 | 9 | 8 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 728 | BUY_XP | ECON | 51.0 | 9 | 4 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 729 | PASS | ECON | 51.0 | 9 | 0 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 742 | PASS | ECON | 51.0 | 9 | 5 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 762 | BUY | ECON | 51.0 | 9 | 11 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7596560716629028 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -7a48aa2d-a43b-4e49-8230-77f4f2860cb2,7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 2 | 6-3 | 763 | PASS | ECON | 51.0 | 9 | 7 | 0 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 772 | MOVE_BENCH | ECON | 51.0 | 9 | 7 | 0 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5837870240211487 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 778 | BUY | ECON | 51.0 | 9 | 12 | 1 | 56.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19707249104976654 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 2 | 6-4 | 779 | PASS | ECON | 51.0 | 9 | 8 | 0 | 56.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 795 | PASS | ECON | 51.0 | 9 | 13 | 1 | 56.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7487250566482544 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4381335377693176 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 35 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 58 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.03957998752594 | 0.0 | 0.0 | +477d3aa4-2130-4a0e-8254-2688ac860569 / -— |
| Jogador 3 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.661026120185852 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 87 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 88 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3084445893764496 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20924915373325348 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5100682377815247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 120 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 142 | PASS | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 170 | BUY_XP | STABILIZE | 96.0 | 4 | 14 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.023274999111890793 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 171 | BUY | SLOWROLL | 96.0 | 5 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.021927088499069214 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 172 | MOVE_BENCH | SLOWROLL | 96.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48488083481788635 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 173 | BUY_XP | SLOWROLL | 96.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 174 | PASS | SLOWROLL | 96.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 194 | BUY_XP | SLOWROLL | 91.0 | 5 | 9 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 195 | BUY_XP | SLOWROLL | 91.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 196 | PASS | SLOWROLL | 91.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Rammus | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 220 | BUY_XP | SLOWROLL | 91.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.006550000049173832 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 221 | BUY | SLOWROLL | 91.0 | 6 | 3 | 0 | 16.0 | Inferno/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06018446385860443 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 222 | MOVE_BENCH | SLOWROLL | 91.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42814770340919495 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 223 | PASS | SLOWROLL | 91.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 240 | MOVE_BENCH | SLOWROLL | 91.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5158816576004028 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 242 | BUY | SLOWROLL | 85.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9613050818443298 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -— |
| Jogador 3 | 2-6 | 243 | BUY_XP | SLOWROLL | 85.0 | 6 | 5 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 244 | PASS | SLOWROLL | 85.0 | 6 | 1 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 266 | BUY_XP | SLOWROLL | 78.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 267 | PASS | SLOWROLL | 78.0 | 6 | 3 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 292 | BUY_XP | SLOWROLL | 78.0 | 6 | 9 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 293 | BUY_XP | SLOWROLL | 78.0 | 6 | 5 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 294 | PASS | SLOWROLL | 78.0 | 6 | 1 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 316 | BUY_XP | SLOWROLL | 68.0 | 6 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 317 | BUY_XP | SLOWROLL | 68.0 | 6 | 4 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 318 | PASS | SLOWROLL | 68.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 340 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2303842008113861 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 341 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 18.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48808667063713074 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 342 | PASS | STABILIZE | 57.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 355 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5558575391769409 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 361 | BUY | STABILIZE | 57.0 | 7 | 14 | 1 | 24.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2770167887210846 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 362 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 11 | 1 | 24.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18396086990833282 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 363 | BUY_XP | FAST8 | 57.0 | 7 | 11 | 1 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 364 | BUY_XP | FAST8 | 57.0 | 7 | 7 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 365 | PASS | FAST8 | 57.0 | 7 | 3 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 382 | SELL | FAST8 | 57.0 | 7 | 8 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8229384422302246 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-5 | 383 | BUY | FAST8 | 57.0 | 7 | 9 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052714861929416656 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-5 | 384 | BUY_XP | FAST8 | 57.0 | 7 | 5 | 0 | 28.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 385 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 28.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7169683575630188 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 386 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17501762509346008 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 387 | PASS | FAST8 | 57.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 405 | BUY_XP | FAST8 | 57.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 406 | BUY_XP | FAST8 | 57.0 | 7 | 4 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 407 | PASS | FAST8 | 57.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 424 | BUY_XP | FAST8 | 57.0 | 7 | 7 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 425 | PASS | FAST8 | 57.0 | 7 | 3 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 443 | BUY_XP | FAST8 | 57.0 | 7 | 9 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 444 | BUY_XP | FAST8 | 57.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 445 | PASS | FAST8 | 57.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 463 | BUY_XP | FAST8 | 43.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 464 | PASS | FAST8 | 43.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 483 | PASS | STABILIZE | 31.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 502 | BUY_XP | STABILIZE | 31.0 | 7 | 14 | 1 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07317750155925751 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 503 | MOVE_BENCH | STABILIZE | 31.0 | 8 | 10 | 1 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3476741909980774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 504 | MOVE_BENCH | STABILIZE | 31.0 | 8 | 10 | 1 | 28.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.504921555519104 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 505 | PASS | STABILIZE | 31.0 | 8 | 10 | 1 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 522 | BUY | STABILIZE | 31.0 | 8 | 16 | 1 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8401329517364502 | 0.0 | 0.0 | +1022f12a-84e9-4eeb-81dc-706092de3728 / -— |
| Jogador 3 | 4-5 | 523 | BUY_XP | STABILIZE | 31.0 | 8 | 13 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 524 | BUY_XP | STABILIZE | 31.0 | 8 | 9 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 525 | BUY_XP | STABILIZE | 31.0 | 8 | 5 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 526 | PASS | STABILIZE | 31.0 | 8 | 1 | 0 | 36.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 542 | PASS | STABILIZE | 19.0 | 8 | 6 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 562 | BUY | ALL_IN | 6.0 | 8 | 12 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.649887204170227 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -— |
| Jogador 3 | 4-7 | 563 | PASS | ALL_IN | 6.0 | 8 | 8 | 0 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 582 | ANVIL_CHOICE | ALL_IN | 6.0 | 8 | 14 | 1 | 36.0 | Inferno/DA_18_Zyra | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 583 | CRAFT_AND_EQUIP | ALL_IN | 6.0 | 8 | 14 | 1 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18242864310741425 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 584 | PASS | ALL_IN | 6.0 | 8 | 14 | 1 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 602 | BUY | ALL_IN | 6.0 | 8 | 21 | 2 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8648765087127686 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -1022f12a-84e9-4eeb-81dc-706092de3728,cdb48eea-209d-4833-9a68-79df61990332 |
| Jogador 3 | 5-2 | 603 | BUY | ALL_IN | 6.0 | 8 | 18 | 1 | 30.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10314866900444031 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 3 | 5-2 | 604 | PASS | ALL_IN | 6.0 | 8 | 14 | 1 | 30.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 622 | BUY | ALL_IN | 6.0 | 8 | 22 | 2 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1396755874156952 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 3 | 5-3 | 623 | PASS | ALL_IN | 6.0 | 8 | 18 | 1 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18819491565227509 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 642 | BUY | ALL_IN | 6.0 | 8 | 26 | 2 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34256118535995483 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -— |
| Jogador 3 | 5-4 | 643 | PASS | ALL_IN | 6.0 | 8 | 23 | 2 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20483461022377014 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 662 | BUY | ALL_IN | 6.0 | 8 | 31 | 3 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8435017466545105 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -— |
| Jogador 3 | 5-5 | 663 | PASS | ALL_IN | 6.0 | 8 | 28 | 2 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.221474289894104 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 682 | BUY | ALL_IN | 6.0 | 8 | 37 | 3 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03613974153995514 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 3 | 5-6 | 683 | PASS | ALL_IN | 6.0 | 8 | 33 | 3 | 38.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3041139543056488 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7398668527603149 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4561019539833069 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 35 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 58 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05967247113585472 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2684079706668854 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 87 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0137511491775513 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -— |
| Jogador 4 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0065994262695312 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4846738576889038 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 120 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1147739887237549 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -9819422b-1f51-47b5-89b7-9d6e906ddff2,a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 2-1 | 121 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03309452161192894 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 122 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02891405299305916 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 123 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 142 | BUY | STABILIZE | 94.0 | 4 | 9 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13617399334907532 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 143 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5587088465690613 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 144 | BUY_XP | STABILIZE | 94.0 | 4 | 6 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 145 | PASS | STABILIZE | 94.0 | 4 | 2 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 170 | BUY_XP | STABILIZE | 89.0 | 4 | 8 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 171 | BUY | SLOWROLL | 89.0 | 5 | 4 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0035206773318350315 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 172 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 2 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.542725145816803 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 173 | PASS | SLOWROLL | 89.0 | 5 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 194 | BUY | SLOWROLL | 83.0 | 5 | 8 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3265019953250885 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 195 | BUY_XP | SLOWROLL | 83.0 | 5 | 6 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 196 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05004698410630226 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 197 | PASS | SLOWROLL | 83.0 | 5 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 220 | SELL | SLOWROLL | 83.0 | 5 | 8 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2985999882221222 | 0.0 | 0.0 | +— / -9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 2-5 | 221 | BUY | SLOWROLL | 83.0 | 5 | 10 | 1 | 22.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8898850679397583 | 0.0 | 0.0 | +3825a7ba-319f-48f8-ad2d-8c24eabbc1cc / -— |
| Jogador 4 | 2-5 | 222 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 7 | 0 | 22.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6645073294639587 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 223 | BUY_XP | SLOWROLL | 83.0 | 5 | 7 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 224 | PASS | SLOWROLL | 83.0 | 5 | 3 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 242 | BUY_XP | SLOWROLL | 76.0 | 5 | 9 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011409999802708626 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 243 | MOVE_BENCH | SLOWROLL | 76.0 | 6 | 5 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4406343400478363 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 244 | BUY | FAST8 | 76.0 | 6 | 5 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.33182042837142944 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 245 | MOVE_BOARD | FAST8 | 76.0 | 6 | 2 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020740801468491554 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 246 | PASS | FAST8 | 76.0 | 6 | 2 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 266 | BUY_XP | FAST8 | 69.0 | 6 | 9 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 267 | BUY_XP | FAST8 | 69.0 | 6 | 5 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 268 | PASS | FAST8 | 69.0 | 6 | 1 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 292 | MOVE_BENCH | FAST8 | 69.0 | 6 | 8 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2744893431663513 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 293 | SELL | FAST8 | 69.0 | 6 | 8 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48100000619888306 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 3-1 | 294 | BUY | FAST8 | 69.0 | 6 | 10 | 1 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1359816938638687 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 295 | BUY_XP | FAST8 | 69.0 | 6 | 8 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 296 | BUY_XP | FAST8 | 69.0 | 6 | 4 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 297 | PASS | FAST8 | 69.0 | 6 | 0 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 316 | SELL | FAST8 | 69.0 | 6 | 6 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5609999895095825 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-2 | 317 | BUY | FAST8 | 69.0 | 6 | 8 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2105724811553955 | 0.0 | 0.0 | +3f253868-2de5-4189-95a0-705f62682958 / -— |
| Jogador 4 | 3-2 | 318 | BUY_XP | FAST8 | 69.0 | 6 | 6 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 319 | PASS | FAST8 | 69.0 | 6 | 2 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 340 | BUY_XP | FAST8 | 60.0 | 6 | 7 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 341 | PASS | FAST8 | 60.0 | 6 | 3 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 361 | BUY_XP | FAST8 | 48.0 | 6 | 9 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 362 | MOVE_BENCH | FAST8 | 48.0 | 7 | 5 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47339341044425964 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 363 | BUY_XP | FAST8 | 48.0 | 7 | 5 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 364 | PASS | FAST8 | 48.0 | 7 | 1 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 382 | PASS | FAST8 | 48.0 | 7 | 7 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 405 | BUY | FAST8 | 48.0 | 7 | 13 | 1 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7351539731025696 | 0.0 | 0.0 | +fe3fea0b-bb55-4236-830e-828a00a9e529 / -— |
| Jogador 4 | 3-6 | 406 | BUY_XP | FAST8 | 48.0 | 7 | 11 | 1 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 407 | BUY_XP | FAST8 | 48.0 | 7 | 7 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 408 | MOVE_BOARD | FAST8 | 48.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010701649822294712 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 409 | MOVE_BOARD | FAST8 | 48.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 410 | PASS | FAST8 | 48.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 424 | BUY_XP | STABILIZE | 37.0 | 7 | 8 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 425 | BUY_XP | STABILIZE | 37.0 | 7 | 4 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 426 | PASS | STABILIZE | 37.0 | 7 | 0 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 443 | CRAFT_AND_EQUIP | STABILIZE | 37.0 | 7 | 5 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10612950474023819 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 444 | BUY_XP | STABILIZE | 37.0 | 7 | 5 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 445 | PASS | STABILIZE | 37.0 | 7 | 1 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 463 | BUY_XP | STABILIZE | 37.0 | 7 | 7 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 464 | PASS | STABILIZE | 37.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 483 | BUY | STABILIZE | 37.0 | 7 | 10 | 1 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7629814743995667 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 484 | BUY_XP | STABILIZE | 37.0 | 7 | 7 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 485 | PASS | STABILIZE | 37.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 502 | BUY_XP | STABILIZE | 25.0 | 7 | 8 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 503 | BUY_XP | STABILIZE | 25.0 | 7 | 4 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38776999711990356 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 504 | PASS | STABILIZE | 25.0 | 8 | 0 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 522 | BUY | STABILIZE | 25.0 | 8 | 5 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035768769681453705 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 4 | 4-5 | 523 | PASS | STABILIZE | 25.0 | 8 | 1 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 542 | BUY | STABILIZE | 25.0 | 8 | 7 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6935660243034363 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 4 | 4-6 | 543 | PASS | STABILIZE | 25.0 | 8 | 3 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 562 | PASS | STABILIZE | 25.0 | 8 | 8 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 582 | ANVIL_CHOICE | STABILIZE | 25.0 | 8 | 13 | 1 | 38.0 | Fera do Rift/DA_Gromp18_AP | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 583 | BUY | STABILIZE | 25.0 | 8 | 13 | 1 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8924974799156189 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -60138930-82d5-4f1c-a5fe-a22ea4b70d36,b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 5-1 | 584 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 10 | 1 | 32.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35555407404899597 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 585 | BUY_XP | STABILIZE | 25.0 | 8 | 10 | 1 | 38.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 586 | BUY_XP | STABILIZE | 25.0 | 8 | 6 | 0 | 38.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 587 | PASS | STABILIZE | 25.0 | 8 | 2 | 0 | 38.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 600 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 2 | 0 | 38.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44894149899482727 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 602 | BUY | ALL_IN | 8.0 | 8 | 7 | 0 | 46.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.318801611661911 | 0.0 | 0.0 | +678a6f43-ca48-46c9-8c5b-6790493f4841 / -— |
| Jogador 4 | 5-2 | 603 | PASS | ALL_IN | 8.0 | 8 | 3 | 0 | 46.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5692920684814453 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05371737480163574 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28482919931411743 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3110044598579407 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | -0.17335718870162964 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 35 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 58 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22276738286018372 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3632408082485199 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23642227053642273 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 88 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29831138253211975 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 89 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37272408604621887 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 90 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 117 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36789244413375854 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 118 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2052900344133377 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030117228627204895 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 120 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10373874753713608 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 121 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 142 | SELL | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036942269653081894 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 2-2 | 143 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3407616913318634 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 144 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13256831467151642 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 145 | BUY_XP | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 146 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 170 | BUY_XP | STABILIZE | 90.0 | 4 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 171 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 4 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4034966826438904 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 172 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 173 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 22.0 | —/DA_18_MasterYi_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 194 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22654157876968384 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 195 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 3 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08981139957904816 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 196 | PASS | STABILIZE | 90.0 | 5 | 3 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 220 | BUY_XP | STABILIZE | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 221 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 222 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12118527293205261 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 223 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 242 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2669946849346161 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 243 | BUY_XP | STABILIZE | 83.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 244 | PASS | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 261 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5036304593086243 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 266 | BUY | FAST8 | 83.0 | 6 | 7 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9671581983566284 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 267 | BUY_XP | FAST8 | 83.0 | 6 | 5 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 268 | PASS | FAST8 | 83.0 | 6 | 1 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 292 | BUY_XP | FAST8 | 83.0 | 6 | 6 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 293 | PASS | FAST8 | 83.0 | 6 | 2 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 316 | BUY_XP | FAST8 | 73.0 | 6 | 7 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 317 | PASS | FAST8 | 73.0 | 6 | 3 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 340 | SELL | FAST8 | 73.0 | 6 | 9 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7778464555740356 | 0.0 | 0.0 | +— / -837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-3 | 341 | BUY | FAST8 | 73.0 | 6 | 11 | 1 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12862858176231384 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 342 | BUY_XP | FAST8 | 73.0 | 6 | 7 | 0 | 28.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 343 | PASS | FAST8 | 73.0 | 6 | 3 | 0 | 28.0 | Florescer/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 361 | BUY_XP | FAST8 | 63.0 | 6 | 8 | 0 | 28.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 362 | BUY_XP | FAST8 | 63.0 | 6 | 4 | 0 | 28.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09130000323057175 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 363 | MOVE_BENCH | FAST8 | 63.0 | 7 | 0 | 0 | 28.0 | Florescer/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09852169454097748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 364 | PASS | FAST8 | 63.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 377 | MOVE_BENCH | FAST8 | 63.0 | 7 | 0 | 0 | 30.0 | Florescer/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3406100273132324 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 382 | PASS | FAST8 | 63.0 | 7 | 5 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 405 | BUY_XP | FAST8 | 63.0 | 7 | 11 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 406 | BUY_XP | FAST8 | 63.0 | 7 | 7 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 407 | PASS | FAST8 | 63.0 | 7 | 3 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 424 | BUY | FAST8 | 52.0 | 7 | 8 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6493409872055054 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 425 | BUY_XP | FAST8 | 52.0 | 7 | 5 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 426 | PASS | FAST8 | 52.0 | 7 | 1 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 443 | BUY_XP | FAST8 | 52.0 | 7 | 6 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 444 | PASS | FAST8 | 52.0 | 7 | 2 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 463 | BUY_XP | FAST8 | 41.0 | 7 | 8 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 464 | BUY_XP | FAST8 | 41.0 | 7 | 4 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 465 | PASS | FAST8 | 41.0 | 7 | 0 | 0 | 36.0 | Florescer/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 483 | PASS | STABILIZE | 27.0 | 7 | 6 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 502 | PASS | STABILIZE | 16.0 | 7 | 12 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 522 | PASS | STABILIZE | 16.0 | 7 | 19 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12332381308078766 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 542 | PASS | STABILIZE | 16.0 | 7 | 27 | 2 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14278624951839447 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 562 | PASS | ALL_IN | 4.0 | 7 | 34 | 3 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28688254952430725 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 582 | ANVIL_CHOICE | ALL_IN | 4.0 | 7 | 42 | 4 | 36.0 | Florescer/DA_18_Ahri | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 583 | BUY | ALL_IN | 4.0 | 7 | 42 | 4 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03838535025715828 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 5 | 5-1 | 584 | CRAFT_AND_EQUIP | ALL_IN | 4.0 | 7 | 38 | 3 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09206650406122208 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 585 | PASS | ALL_IN | 4.0 | 7 | 38 | 3 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3244040310382843 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 602 | PASS | ALL_IN | 4.0 | 7 | 46 | 4 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3360349237918854 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6121415495872498 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7398668527603149 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4561019539833069 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.036318302154541 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4104852080345154 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.039830125868320465 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 59 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 87 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 88 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0396544933319092 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 118 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 119 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 136 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14710016548633575 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 142 | BUY | SLOWROLL | 95.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0915418192744255 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 143 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34068799018859863 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 144 | PASS | SLOWROLL | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 170 | BUY | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.009722894057631493 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 171 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29354730248451233 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 172 | BUY_XP | SLOWROLL | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 173 | PASS | SLOWROLL | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 194 | SELL | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3333643674850464 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-4 | 195 | BUY | SLOWROLL | 95.0 | 5 | 11 | 1 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8748176693916321 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 196 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 197 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3334961235523224 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 198 | PASS | SLOWROLL | 95.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 220 | BUY_XP | SLOWROLL | 95.0 | 5 | 14 | 1 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 221 | BUY_XP | SLOWROLL | 95.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 222 | BUY_XP | SLOWROLL | 95.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017079999670386314 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 223 | PASS | SLOWROLL | 95.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 240 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5281329154968262 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 242 | BUY | SLOWROLL | 95.0 | 6 | 9 | 0 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28535163402557373 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 243 | BUY_XP | SLOWROLL | 95.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 244 | PASS | SLOWROLL | 95.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 266 | BUY_XP | SLOWROLL | 89.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 267 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 268 | PASS | SLOWROLL | 89.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 292 | BUY_XP | SLOWROLL | 89.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 293 | BUY_XP | SLOWROLL | 89.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 294 | PASS | SLOWROLL | 89.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 316 | BUY_XP | SLOWROLL | 78.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 317 | PASS | SLOWROLL | 78.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 340 | BUY_XP | SLOWROLL | 78.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04383999854326248 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 341 | MOVE_BENCH | STABILIZE | 78.0 | 7 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6733136773109436 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 342 | PASS | FAST8 | 78.0 | 7 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 361 | BUY | FAST8 | 78.0 | 7 | 11 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.06403809040784836 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 362 | BUY_XP | FAST8 | 78.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 363 | PASS | FAST8 | 78.0 | 7 | 3 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 382 | MOVE_BOARD | FAST8 | 78.0 | 7 | 9 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31234022974967957 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 383 | PASS | FAST8 | 78.0 | 7 | 9 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 405 | BUY_XP | FAST8 | 67.0 | 7 | 14 | 1 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 406 | BUY_XP | FAST8 | 67.0 | 7 | 10 | 1 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 407 | BUY_XP | FAST8 | 67.0 | 7 | 6 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 408 | PASS | FAST8 | 67.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 424 | PASS | FAST8 | 57.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 443 | BUY_XP | FAST8 | 57.0 | 7 | 14 | 1 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019249999895691872 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 444 | BUY_XP | FAST8 | 57.0 | 7 | 10 | 1 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 445 | BUY_XP | FAST8 | 57.0 | 7 | 6 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 446 | PASS | FAST8 | 57.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 463 | BUY | FAST8 | 44.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7316808104515076 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -— |
| Jogador 6 | 4-2 | 464 | PASS | FAST8 | 44.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 483 | PASS | FAST8 | 44.0 | 7 | 11 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 502 | PASS | STABILIZE | 31.0 | 7 | 17 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11223597824573517 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 522 | PASS | STABILIZE | 31.0 | 7 | 23 | 2 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12149947136640549 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 542 | PASS | STABILIZE | 19.0 | 7 | 31 | 3 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20878413319587708 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 562 | BUY | ALL_IN | 5.0 | 7 | 40 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9930381774902344 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb,fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 4-7 | 563 | PASS | ALL_IN | 5.0 | 7 | 37 | 3 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2947142720222473 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 582 | ANVIL_CHOICE | ALL_IN | 5.0 | 7 | 46 | 4 | 28.0 | Colosso/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 583 | BUY | ALL_IN | 5.0 | 7 | 46 | 4 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0731793642044067 | 0.0 | 0.0 | +0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1,a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 5-1 | 584 | PASS | ALL_IN | 5.0 | 7 | 43 | 4 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.331722229719162 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 600 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 43 | 4 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4067860245704651 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9932671189308167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5648271441459656 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 34 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 58 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0492019653320312 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20168310403823853 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3483960032463074 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.32221969962120056 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 87 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.267111212015152 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19451823830604553 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5199721455574036 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 120 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 121 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 142 | PASS | STABILIZE | 95.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 170 | PASS | STABILIZE | 95.0 | 4 | 14 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 194 | BUY | SLOWROLL | 89.0 | 5 | 20 | 2 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02225729264318943 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 195 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 16 | 1 | 10.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6115437150001526 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 196 | BUY_XP | SLOWROLL | 89.0 | 5 | 16 | 1 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 197 | BUY_XP | SLOWROLL | 89.0 | 5 | 12 | 1 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 198 | BUY_XP | SLOWROLL | 89.0 | 5 | 8 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 199 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 200 | PASS | SLOWROLL | 89.0 | 5 | 0 | 0 | 18.0 | —/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 220 | BUY_XP | SLOWROLL | 89.0 | 5 | 5 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.022749999538064003 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 221 | BUY | SLOWROLL | 89.0 | 6 | 1 | 0 | 18.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BOARD, PASS | True | True | 0.2820035517215729 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 222 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 223 | PASS | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 240 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36013028025627136 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 242 | BUY | SLOWROLL | 89.0 | 6 | 6 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3239510953426361 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 243 | PASS | SLOWROLL | 89.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 266 | BUY_XP | SLOWROLL | 84.0 | 6 | 8 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 267 | BUY_XP | SLOWROLL | 84.0 | 6 | 4 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 268 | PASS | SLOWROLL | 84.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 292 | BUY_XP | SLOWROLL | 84.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 293 | PASS | SLOWROLL | 84.0 | 6 | 1 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 316 | BUY_XP | SLOWROLL | 74.0 | 6 | 7 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 317 | PASS | SLOWROLL | 74.0 | 6 | 3 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 340 | BUY_XP | SLOWROLL | 64.0 | 6 | 9 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 341 | BUY_XP | SLOWROLL | 64.0 | 6 | 5 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04383999854326248 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 342 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 1 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7777367830276489 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 343 | PASS | FAST8 | 64.0 | 7 | 1 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 361 | BUY | FAST8 | 54.0 | 7 | 7 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7329428195953369 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 362 | PASS | FAST8 | 54.0 | 7 | 4 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 382 | PASS | FAST8 | 54.0 | 7 | 10 | 1 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 405 | BUY | FAST8 | 44.0 | 7 | 18 | 1 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08419546484947205 | 0.0 | 0.0 | +6caec849-54f8-4ec1-90a4-fc0587510013 / -— |
| Jogador 7 | 3-6 | 406 | PASS | FAST8 | 44.0 | 7 | 14 | 1 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 424 | BUY | STABILIZE | 33.0 | 7 | 23 | 2 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.765093207359314 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 425 | BUY_XP | STABILIZE | 33.0 | 7 | 19 | 1 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 426 | BUY_XP | STABILIZE | 33.0 | 7 | 15 | 1 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 427 | BUY_XP | STABILIZE | 33.0 | 7 | 11 | 1 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 428 | BUY_XP | STABILIZE | 33.0 | 7 | 7 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 429 | PASS | STABILIZE | 33.0 | 7 | 3 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 443 | PASS | STABILIZE | 33.0 | 7 | 11 | 1 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 463 | PASS | STABILIZE | 21.0 | 7 | 20 | 2 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12279365211725235 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 483 | PASS | ALL_IN | 9.0 | 7 | 30 | 3 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26838093996047974 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.011937879957258701 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8217591643333435 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5140626430511475 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 34 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 58 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.306370347738266 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09353116899728775 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8203577399253845 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2514664828777313 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 81 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40278536081314087 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 87 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0226378440856934 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06299486011266708 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 119 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.030939772725105286 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 120 | BUY_XP | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 121 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 122 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 142 | BUY | SLOWROLL | 100.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.00820973888039589 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 143 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4703492224216461 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 144 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 170 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03279787674546242 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 171 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 172 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 194 | SELL | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37844616174697876 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-4 | 195 | BUY | STABILIZE | 100.0 | 5 | 13 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.18048463761806488 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 196 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21564379334449768 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 197 | BUY_XP | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 198 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 199 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 220 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039149798452854156 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 221 | BUY_XP | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 222 | SELL | SLOWROLL | 100.0 | 6 | 4 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.79926997423172 | 0.0 | 0.0 | +— / -fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-5 | 223 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3738403916358948 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 224 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04119361191987991 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 225 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 16.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3262769877910614 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 226 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 16.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3900880515575409 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 227 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 240 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5544328093528748 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 242 | BUY | STABILIZE | 100.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2890952527523041 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 243 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16662120819091797 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 244 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 245 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016619199886918068 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 246 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06559108197689056 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 247 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 266 | BUY_XP | STABILIZE | 100.0 | 6 | 10 | 1 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 267 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 268 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 292 | SELL | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30068936944007874 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 3-1 | 293 | BUY | STABILIZE | 100.0 | 6 | 12 | 1 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05322416499257088 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 294 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7397872805595398 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 295 | BUY_XP | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 296 | BUY_XP | STABILIZE | 100.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 297 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 24.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 316 | BUY_XP | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 317 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06353499740362167 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 318 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05483737960457802 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 319 | MOVE_BENCH | FAST8 | 100.0 | 7 | 1 | 0 | 26.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5592636466026306 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 320 | PASS | STABILIZE | 100.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 333 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4768909215927124 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 340 | BUY_XP | FAST8 | 88.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 341 | PASS | FAST8 | 88.0 | 7 | 2 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 361 | BUY | FAST8 | 88.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.707817554473877 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 362 | MOVE_BENCH | FAST8 | 88.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 363 | BUY_XP | FAST8 | 88.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 364 | MOVE_BENCH | FAST8 | 88.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2935805916786194 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 365 | PASS | FAST8 | 88.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 382 | MOVE_BENCH | FAST8 | 88.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0031958776526153088 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 383 | BUY_XP | FAST8 | 88.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 384 | PASS | FAST8 | 88.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 405 | BUY_XP | FAST8 | 77.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 406 | PASS | FAST8 | 77.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 424 | BUY_XP | FAST8 | 77.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 425 | BUY_XP | FAST8 | 77.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 426 | PASS | FAST8 | 77.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 443 | BUY_XP | FAST8 | 77.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 444 | CRAFT_AND_EQUIP | FAST8 | 77.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1326172649860382 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 445 | PASS | FAST8 | 77.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 463 | BUY_XP | FAST8 | 77.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 464 | BUY_XP | FAST8 | 77.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 465 | PASS | FAST8 | 77.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 483 | BUY_XP | FAST8 | 77.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0772937536239624 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 484 | SELL | WINSTREAK | 77.0 | 8 | 4 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003338461508974433 | 0.0 | 0.0 | +— / -630d9254-3856-4d88-b981-43a8270b4b3d |
| Jogador 8 | 4-3 | 485 | BUY | WINSTREAK | 77.0 | 8 | 5 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.22821645438671112 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 8 | 4-3 | 486 | MOVE_BENCH | WINSTREAK | 77.0 | 8 | 1 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5316468477249146 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 487 | PASS | WINSTREAK | 77.0 | 8 | 1 | 0 | 44.0 | Colosso/DA_18_Soraka | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 502 | BUY | WINSTREAK | 77.0 | 8 | 8 | 0 | 44.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12052624672651291 | 0.0 | 0.0 | +1f7f2a48-1318-4fc6-87cc-03d557bf69ea / -— |
| Jogador 8 | 4-4 | 503 | MOVE_BENCH | WINSTREAK | 77.0 | 8 | 4 | 0 | 44.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11595416069030762 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 504 | BUY_XP | WINSTREAK | 77.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 505 | PASS | WINSTREAK | 77.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 522 | BUY | WINSTREAK | 77.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.781387448310852 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 8 | 4-5 | 523 | PASS | WINSTREAK | 77.0 | 8 | 2 | 0 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 542 | BUY | WINSTREAK | 77.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25808724761009216 | 0.0 | 0.0 | +241a8a03-6e6f-4a9a-8550-e9154f3e1e76 / -— |
| Jogador 8 | 4-6 | 543 | BUY_XP | WINSTREAK | 77.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 544 | PASS | WINSTREAK | 77.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 562 | PASS | WINSTREAK | 77.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 582 | ANVIL_CHOICE | WINSTREAK | 77.0 | 8 | 15 | 1 | 46.0 | Colosso/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 583 | BUY | WINSTREAK | 77.0 | 8 | 15 | 1 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17244355380535126 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 8 | 5-1 | 584 | BUY_XP | WINSTREAK | 77.0 | 8 | 10 | 1 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08293750137090683 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 585 | BUY_XP | WINSTREAK | 77.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 586 | PASS | WINSTREAK | 77.0 | 8 | 2 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 602 | BUY_XP | WINSTREAK | 77.0 | 8 | 11 | 1 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08293750137090683 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 603 | BUY_XP | WINSTREAK | 77.0 | 8 | 7 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 604 | PASS | WINSTREAK | 77.0 | 8 | 3 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 622 | BUY_XP | WINSTREAK | 77.0 | 8 | 12 | 1 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08293750137090683 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 623 | BUY_XP | WINSTREAK | 77.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 624 | BUY_XP | WINSTREAK | 77.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 625 | PASS | WINSTREAK | 77.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 642 | BUY_XP | ECON | 61.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 643 | PASS | ECON | 61.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 662 | BUY_XP | ECON | 61.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 663 | PASS | ECON | 61.0 | 8 | 2 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 682 | BUY_XP | ECON | 45.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0611874982714653 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 683 | PASS | ECON | 45.0 | 9 | 4 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 700 | MOVE_BENCH | ECON | 45.0 | 9 | 4 | 0 | 46.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05322358384728432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 702 | BUY | ECON | 45.0 | 9 | 10 | 1 | 52.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.053343676030635834 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 8 | 5-7 | 703 | BUY_XP | ECON | 45.0 | 9 | 5 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 704 | PASS | ECON | 45.0 | 9 | 1 | 0 | 52.0 | Colosso/DA_18_ElderDragon | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 722 | ANVIL_CHOICE | ECON | 45.0 | 9 | 6 | 0 | 52.0 | Colosso/DA_18_ElderDragon | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 723 | EQUIP_FROM_INVENTORY | ECON | 45.0 | 9 | 6 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10863053798675537 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 724 | MOVE_BENCH | ECON | 45.0 | 9 | 6 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9968090057373047 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 725 | MOVE_BENCH | ECON | 45.0 | 9 | 6 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29736557602882385 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 726 | PASS | ECON | 45.0 | 9 | 6 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 742 | BUY_XP | STABILIZE | 27.0 | 9 | 11 | 1 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 743 | BUY_XP | STABILIZE | 27.0 | 9 | 7 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 744 | PASS | STABILIZE | 27.0 | 9 | 3 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 762 | PASS | ALL_IN | 9.0 | 9 | 9 | 0 | 52.0 | Colosso/DA_18_ElderDragon | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 131 | 165 | 12 | 6 | 23 | 1 | 0 | 0 | 67 | 48.0 |
- Jogador 1 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 61g, BUY_XP: 104g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 3g, stage 2: 44g, stage 3: 42g, stage 4: 50g, stage 5: 16g, stage 6: 10g
| Jogador 2 | 139 | 255 | 21 | 20 | 43 | 2 | 0 | 0 | 13 | 56.0 |
- Jogador 2 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 67g, BUY_XP: 188g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 4g, stage 2: 47g, stage 3: 68g, stage 4: 64g, stage 5: 44g, stage 6: 28g
| Jogador 3 | 93 | 146 | 1 | 7 | 21 | 2 | 0 | 0 | 33 | 38.0 |
- Jogador 3 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 46g, BUY_XP: 100g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 6g, stage 2: 37g, stage 3: 47g, stage 4: 35g, stage 5: 21g
| Jogador 4 | 94 | 140 | 6 | 5 | 20 | 1 | 0 | 0 | 3 | 46.0 |
- Jogador 4 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 44g, BUY_XP: 96g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 3g, stage 2: 45g, stage 3: 46g, stage 4: 31g, stage 5: 15g
| Jogador 5 | 77 | 100 | 4 | 3 | 16 | 1 | 0 | 0 | 46 | 36.0 |
- Jogador 5 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 28g, BUY_XP: 72g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 6g, stage 2: 39g, stage 3: 39g, stage 4: 12g, stage 5: 4g
| Jogador 6 | 76 | 105 | 4 | 6 | 16 | 2 | 0 | 0 | 43 | 28.0 |
- Jogador 6 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 29g, BUY_XP: 76g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 41g, stage 3: 36g, stage 4: 18g, stage 5: 3g
| Jogador 7 | 58 | 87 | 0 | 4 | 14 | 1 | 0 | 0 | 30 | 26.0 |
- Jogador 7 — gasto por ação: BUY: 23g, BUY_XP: 64g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g
- Jogador 7 — gasto por estágio: stage 1: 2g, stage 2: 42g, stage 3: 43g, stage 4: 0g
| Jogador 8 | 128 | 203 | 8 | 10 | 34 | 3 | 0 | 0 | 9 | 52.0 |
- Jogador 8 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 51g, BUY_XP: 152g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 2g, stage 2: 52g, stage 3: 47g, stage 4: 40g, stage 5: 54g, stage 6: 8g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 26 | 4 |
- Jogador 1 · 1-4 · step 87: PASS com 4g, HP 100, nível 3/8 (STABILIZE).
- Jogador 1 · 2-2 · step 145: PASS com 6g, HP 100, nível 4/8 (STABILIZE).
- Jogador 1 · 3-4 · step 361: PASS com 5g, HP 72, nível 7/8 (FAST8).
- Jogador 1 · 4-5 · step 525: PASS com 8g, HP 49, nível 7/8 (FAST8).
| Jogador 2 | 47 | 1 |
- Jogador 2 · 1-4 · step 87: PASS com 4g, HP 100, nível 3/8 (STABILIZE).
| Jogador 3 | 25 | 3 |
- Jogador 3 · 2-2 · step 142: PASS com 9g, HP 100, nível 4/8 (STABILIZE).
- Jogador 3 · 3-3 · step 342: PASS com 8g, HP 57, nível 7/8 (STABILIZE).
- Jogador 3 · 4-3 · step 483: PASS com 8g, HP 31, nível 7/8 (STABILIZE).
| Jogador 4 | 24 | 3 |
- Jogador 4 · 1-4 · step 87: PASS com 4g, HP 100, nível 3/8 (STABILIZE).
- Jogador 4 · 2-1 · step 123: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 4 · 3-5 · step 382: PASS com 7g, HP 48, nível 7/8 (FAST8).
| Jogador 5 | 18 | 8 |
- Jogador 5 · 3-5 · step 382: PASS com 5g, HP 63, nível 7/8 (FAST8).
- Jogador 5 · 4-3 · step 483: PASS com 6g, HP 27, nível 7/8 (STABILIZE).
- Jogador 5 · 4-4 · step 502: PASS com 12g, HP 16, nível 7/8 (STABILIZE).
- Jogador 5 · 4-5 · step 522: PASS com 19g, HP 16, nível 7/8 (STABILIZE).
- Jogador 5 · 4-6 · step 542: PASS com 27g, HP 16, nível 7/8 (STABILIZE).
- Jogador 5 · 4-7 · step 562: PASS com 34g, HP 4, nível 7/8 (ALL_IN).
- Jogador 5 · 5-1 · step 585: PASS com 38g, HP 4, nível 7/8 (ALL_IN).
- Jogador 5 · 5-2 · step 602: PASS com 46g, HP 4, nível 7/8 (ALL_IN).
| Jogador 6 | 19 | 10 |
- Jogador 6 · 3-3 · step 342: PASS com 4g, HP 78, nível 7/8 (FAST8).
- Jogador 6 · 3-5 · step 383: PASS com 9g, HP 78, nível 7/8 (FAST8).
- Jogador 6 · 3-7 · step 424: PASS com 8g, HP 57, nível 7/8 (FAST8).
- Jogador 6 · 4-2 · step 464: PASS com 5g, HP 44, nível 7/8 (FAST8).
- Jogador 6 · 4-3 · step 483: PASS com 11g, HP 44, nível 7/8 (FAST8).
- Jogador 6 · 4-4 · step 502: PASS com 17g, HP 31, nível 7/8 (STABILIZE).
- Jogador 6 · 4-5 · step 522: PASS com 23g, HP 31, nível 7/8 (STABILIZE).
- Jogador 6 · 4-6 · step 542: PASS com 31g, HP 19, nível 7/8 (STABILIZE).
- Jogador 6 · 4-7 · step 563: PASS com 37g, HP 5, nível 7/8 (ALL_IN).
- Jogador 6 · 5-1 · step 584: PASS com 43g, HP 5, nível 7/8 (ALL_IN).
| Jogador 7 | 16 | 9 |
- Jogador 7 · 1-4 · step 87: PASS com 5g, HP 100, nível 3/8 (STABILIZE).
- Jogador 7 · 2-2 · step 142: PASS com 8g, HP 95, nível 4/8 (STABILIZE).
- Jogador 7 · 2-3 · step 170: PASS com 14g, HP 95, nível 4/8 (STABILIZE).
- Jogador 7 · 3-4 · step 362: PASS com 4g, HP 54, nível 7/8 (FAST8).
- Jogador 7 · 3-5 · step 382: PASS com 10g, HP 54, nível 7/8 (FAST8).
- Jogador 7 · 3-6 · step 406: PASS com 14g, HP 44, nível 7/8 (FAST8).
- Jogador 7 · 4-1 · step 443: PASS com 11g, HP 33, nível 7/8 (STABILIZE).
- Jogador 7 · 4-2 · step 463: PASS com 20g, HP 21, nível 7/8 (STABILIZE).
- Jogador 7 · 4-3 · step 483: PASS com 30g, HP 9, nível 7/8 (ALL_IN).
| Jogador 8 | 38 | 1 |
- Jogador 8 · 1-4 · step 87: PASS com 5g, HP 100, nível 3/8 (STABILIZE).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 2 | 2 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 131 | 23 | 21 | 87 | 0.0040 | -0.0563 | 0.0002 | 0.5210 | 0.0039 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ -0.0349 (22 ações), BUY_XP: Δ 0.0000 (26 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0345 (34 ações), MOVE_BOARD: Δ 0.0008 (5 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0400 (3 ações)
| Jogador 2 | 139 | 12 | 11 | 116 | 0.0013 | 0.0044 | -0.0014 | 0.4040 | 0.0027 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ -0.0360 (20 ações), BUY_XP: Δ 0.0000 (47 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0367 (22 ações), MOVE_BOARD: Δ 0.0311 (3 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (6 ações)
| Jogador 3 | 93 | 10 | 9 | 74 | 0.0030 | -0.3032 | -0.0004 | 0.3935 | 0.0035 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ 0.0237 (16 ações), BUY_XP: Δ 0.0000 (25 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0019 (17 ações), MOVE_BOARD: Δ -0.1286 (1 ações), PASS: Δ 0.0000 (31 ações), SELL: Δ 0.0000 (1 ações)
| Jogador 4 | 94 | 11 | 10 | 73 | 0.0024 | -0.7166 | -0.0011 | 0.2796 | 0.0035 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ 0.0686 (17 ações), BUY_XP: Δ 0.0000 (24 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0551 (16 ações), MOVE_BOARD: Δ -0.0122 (5 ações), PASS: Δ 0.0000 (27 ações), SELL: Δ 0.0000 (3 ações)
| Jogador 5 | 77 | 7 | 10 | 60 | 0.0069 | -0.1448 | -0.0012 | 0.5573 | 0.0081 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ 0.0400 (10 ações), BUY_XP: Δ 0.0000 (18 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0055 (15 ações), MOVE_BOARD: Δ 0.0721 (3 ações), PASS: Δ 0.0000 (27 ações), SELL: Δ 0.0000 (2 ações)
| Jogador 6 | 76 | 10 | 9 | 57 | 0.0002 | -0.1213 | -0.0032 | 0.3778 | 0.0034 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0322 (12 ações), BUY_XP: Δ 0.0000 (19 ações), MOVE_BENCH: Δ 0.0568 (13 ações), MOVE_BOARD: Δ -0.1312 (3 ações), PASS: Δ 0.0000 (26 ações), SELL: Δ 0.0300 (2 ações)
| Jogador 7 | 58 | 8 | 7 | 43 | 0.0054 | -0.5242 | -0.0037 | 0.4511 | 0.0091 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0444 (9 ações), BUY_XP: Δ 0.0000 (16 ações), MOVE_BENCH: Δ 0.0488 (10 ações), MOVE_BOARD: Δ -0.2872 (2 ações), PASS: Δ 0.0000 (21 ações)
| Jogador 8 | 128 | 14 | 13 | 101 | 0.0004 | -0.2549 | -0.0024 | 0.3825 | 0.0028 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ 0.0262 (16 ações), BUY_XP: Δ 0.0000 (38 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0198 (28 ações), MOVE_BOARD: Δ 0.0432 (3 ações), PASS: Δ 0.0000 (35 ações), SELL: Δ 0.0150 (4 ações)
- Jogador 1 — rounds avaliados: 37; correlação estrutural/combate: -0.048; posicional/combate: 0.094.
- Jogador 1 — combate positive: score estrutural prévio -0.008
  score posicional prévio 0.543
- Jogador 1 — combate negative: score estrutural prévio 0.038
  score posicional prévio 0.526
- Jogador 2 — rounds avaliados: 37; correlação estrutural/combate: 0.286; posicional/combate: -0.220.
- Jogador 2 — combate positive: score estrutural prévio 0.044
  score posicional prévio 0.401
- Jogador 2 — combate negative: score estrutural prévio -0.118
  score posicional prévio 0.425
- Jogador 3 — rounds avaliados: 31; correlação estrutural/combate: -0.009; posicional/combate: -0.365.
- Jogador 3 — combate positive: score estrutural prévio -0.358
  score posicional prévio 0.346
- Jogador 3 — combate negative: score estrutural prévio -0.335
  score posicional prévio 0.418
- Jogador 4 — rounds avaliados: 27; correlação estrutural/combate: -0.225; posicional/combate: -0.068.
- Jogador 4 — combate positive: score estrutural prévio -0.911
  score posicional prévio 0.241
- Jogador 4 — combate negative: score estrutural prévio -0.702
  score posicional prévio 0.268
- Jogador 5 — rounds avaliados: 27; correlação estrutural/combate: 0.023; posicional/combate: -0.058.
- Jogador 5 — combate positive: score estrutural prévio -0.123
  score posicional prévio 0.577
- Jogador 5 — combate negative: score estrutural prévio -0.135
  score posicional prévio 0.582
- Jogador 6 — rounds avaliados: 26; correlação estrutural/combate: 0.316; posicional/combate: 0.209.
- Jogador 6 — combate positive: score estrutural prévio -0.123
  score posicional prévio 0.378
- Jogador 6 — combate negative: score estrutural prévio -0.214
  score posicional prévio 0.358
- Jogador 7 — rounds avaliados: 21; correlação estrutural/combate: -0.206; posicional/combate: -0.383.
- Jogador 7 — combate positive: score estrutural prévio -0.718
  score posicional prévio 0.429
- Jogador 7 — combate negative: score estrutural prévio -0.493
  score posicional prévio 0.488
- Jogador 8 — rounds avaliados: 35; correlação estrutural/combate: 0.061; posicional/combate: -0.013.
- Jogador 8 — combate positive: score estrutural prévio -0.325
  score posicional prévio 0.370
- Jogador 8 — combate negative: score estrutural prévio -0.443
  score posicional prévio 0.366

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 167 | OK (167) | 2 | 0 | 0 | 1 | 2 | 1 |
- Jogador 1 — IDs equipados observados: TFT_Item_IonicSpark, TFT_Item_UnstableConcoction; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 1 — bigornas: 2 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow.
- Jogador 1 — bigorna 5-1 step 582: seleção TFT_Item_RecurveBow entre TFT_Item_RecurveBow, TFT_Item_BFSword, TFT_Item_Spatula; consistente: True; fit 0.0.
- Jogador 1 — bigorna 6-1 step 722: seleção TFT_Item_UnstableConcoction entre TFT_Item_UnstableConcoction, TFT_Item_RunaansHurricane, TFT_Item_Morellonomicon, TFT_Item_Quicksilver; consistente: True; fit 0.0.
| Jogador 2 | 176 | OK (176) | 2 | 0 | 0 | 1 | 2 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_BlueBuff, TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 2 — bigornas: 2 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_Spatula, TFT_Item_TearOfTheGoddess.
- Jogador 2 — bigorna 5-1 step 582: seleção TFT_Item_TearOfTheGoddess entre TFT_Item_TearOfTheGoddess, TFT_Item_ChainVest, TFT_Item_FryingPan; consistente: True; fit 0.0.
- Jogador 2 — bigorna 6-1 step 722: seleção TFT_Item_IonicSpark entre TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_InfinityEdge, DA_18_EmblemBlossom; consistente: True; fit 0.0.
| Jogador 3 | 123 | OK (123) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 3 — IDs equipados observados: TFT_Item_JeweledGauntlet; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 3 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_NeedlesslyLargeRod, TFT_Item_Spatula.
- Jogador 3 — bigorna 5-1 step 582: seleção TFT_Item_SparringGloves entre TFT_Item_SparringGloves, TFT_Item_FryingPan, TFT_Item_Spatula; consistente: True; fit 0.0.
| Jogador 4 | 120 | OK (120) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_Redemption; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 4 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt.
- Jogador 4 — bigorna 5-1 step 582: seleção TFT_Item_BFSword entre TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak; consistente: True; fit 0.0.
| Jogador 5 | 103 | OK (103) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 5 — IDs equipados observados: TFT_Item_TitansResolve; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 5 — bigornas: 1 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_FryingPan.
- Jogador 5 — bigorna 5-1 step 582: seleção TFT_Item_RecurveBow entre TFT_Item_RecurveBow, TFT_Item_FryingPan, TFT_Item_GiantsBelt; consistente: True; fit 0.0.
| Jogador 6 | 101 | OK (101) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 6 — IDs equipados observados: nenhum observado; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 6 — bigornas: 1 escolhas; craft/equip: 0 (conversões observadas: 0); componentes persistentes entre rounds: TFT_Item_SparringGloves, TFT_Item_Spatula.
- Jogador 6 — revisão de conversão: componentes foram observados, mas nenhuma ação de craft/equip foi registrada; isso não prova receita viável.
- Jogador 6 — bigorna 5-1 step 582: seleção TFT_Item_NegatronCloak entre TFT_Item_NegatronCloak, TFT_Item_GiantsBelt, TFT_Item_BFSword; consistente: True; fit 0.0.
| Jogador 7 | 78 | OK (78) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 7 — IDs equipados observados: nenhum observado; eventos: COMPONENT_LOOT_GRANTED: 16.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 0 (conversões observadas: 0); componentes persistentes entre rounds: TFT_Item_SparringGloves, TFT_Item_Spatula.
- Jogador 7 — revisão de conversão: componentes foram observados, mas nenhuma ação de craft/equip foi registrada; isso não prova receita viável.
| Jogador 8 | 162 | OK (162) | 1 | 1 | 0 | 1 | 2 | 1 |
- Jogador 8 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_LastWhisper; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
- Jogador 8 — bigornas: 2 escolhas; craft/equip: 1 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak.
- Jogador 8 — bigorna 5-1 step 582: seleção TFT_Item_NegatronCloak entre TFT_Item_NegatronCloak, TFT_Item_Spatula, TFT_Item_RecurveBow; consistente: True; fit 0.0.
- Jogador 8 — bigorna 6-1 step 722: seleção TFT_Item_LastWhisper entre TFT_Item_LastWhisper, TFT_Item_SpearOfShojin, TFT_Item_SpectralGauntlet, TFT_Item_ArchangelsStaff; consistente: True; fit 0.0.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 1 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.002 | 0.000 |
| Jogador 1 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.170 | 0.000 |
| Jogador 1 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 1 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 8 → 8 | 6 | 4 → 4 | 0.095 | 0.456 |
| Jogador 1 | 2-2 | 5 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 14% → 14% | 8 → 11 | 2 | 4 → 4 | 0.027 | -0.506 |
| Jogador 1 | 2-3 | 11 | 4.000 | -4.000 | 0 → 1 | 1 → 0 | 14% → 14% | 11 → 7 | 12 | 4 → 5 | 0.011 | -0.216 |
| Jogador 1 | 2-4 | 5 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 7 → 6 | 7 | 5 → 5 | 0.053 | 0.000 |
| Jogador 1 | 2-5 | 6 | 0.000 | 4.000 | 1 → 1 | 0 → 1 | 18% → 18% | 6 → 6 | 6 | 5 → 6 | -0.007 | -0.413 |
| Jogador 1 | 2-6 | 5 | 4.000 | 2.000 | 1 → 1 | 1 → 2 | 18% → 21% | 6 → 9 | 3 | 6 → 6 | 0.008 | 0.541 |
| Jogador 1 | 2-7 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 9 | 4 | 6 → 6 | 0.000 | 0.937 |
| Jogador 1 | 3-2 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | 0.725 |
| Jogador 1 | 3-3 | 5 | 6.000 | -6.000 | 1 → 1 | 2 → 2 | 21% → 25% | 8 → 5 | 8 | 6 → 7 | -0.027 | -0.535 |
| Jogador 1 | 3-4 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 5 → 10 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 3-5 | 7 | 0.000 | 0.000 | 1 → 2 | 2 → 1 | 25% → 21% | 10 → 6 | 10 | 7 → 7 | 0.010 | -0.389 |
| Jogador 1 | 3-6 | 5 | 4.000 | 4.000 | 2 → 2 | 1 → 1 | 21% → 25% | 6 → 8 | 4 | 7 → 7 | 0.022 | 0.570 |
| Jogador 1 | 3-7 | 10 | 10.000 | -4.000 | 2 → 3 | 1 → 0 | 25% → 25% | 8 → 7 | 8 | 7 → 7 | -0.104 | 0.000 |
| Jogador 1 | 4-1 | 7 | -2.000 | 8.000 | 3 → 2 | 0 → 0 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | 0.000 | 0.416 |
| Jogador 1 | 4-2 | 9 | -4.000 | -2.000 | 2 → 2 | 0 → 1 | 25% → 25% | 7 → 5 | 15 | 7 → 7 | 0.076 | -0.296 |
| Jogador 1 | 4-3 | 4 | -2.000 | 2.000 | 2 → 1 | 1 → 1 | 25% → 25% | 5 → 7 | 4 | 7 → 7 | -0.015 | 0.733 |
| Jogador 1 | 4-4 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 8 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 5 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 13 | 0 | 7 → 7 | 0.000 | -0.543 |
| Jogador 1 | 4-6 | 5 | 8.000 | -8.000 | 1 → 2 | 1 → 1 | 25% → 29% | 13 → 16 | 4 | 7 → 8 | 0.020 | 0.597 |
| Jogador 1 | 4-7 | 7 | 0.000 | 8.000 | 2 → 1 | 1 → 1 | 29% → 29% | 16 → 5 | 16 | 8 → 8 | -0.009 | 0.000 |
| Jogador 1 | 5-1 | 5 | 2.000 | 6.000 | 1 → 2 | 1 → 1 | 29% → 29% | 5 → 6 | 4 | 8 → 8 | 0.012 | -0.550 |
| Jogador 1 | 5-2 | 3 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 6 → 8 | 4 | 8 → 8 | 0.000 | 0.974 |
| Jogador 1 | 5-3 | 4 | 0.000 | 8.000 | 2 → 2 | 1 → 2 | 29% → 29% | 8 → 7 | 8 | 8 → 8 | 0.000 | 0.730 |
| Jogador 1 | 5-4 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 29% → 29% | 7 → 13 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 29% → 29% | 13 → 19 | 0 | 8 → 8 | 0.000 | -1.375 |
| Jogador 1 | 5-6 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 29% → 29% | 19 → 27 | 0 | 8 → 8 | 0.000 | 1.478 |
| Jogador 1 | 5-7 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 29% → 29% | 27 → 34 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 5 | 0.000 | 4.000 | 2 → 2 | 2 → 3 | 29% → 29% | 34 → 42 | 2 | 8 → 8 | 0.000 | 0.589 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 29% → 29% | 42 → 52 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-3 | 2 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 29% → 29% | 52 → 64 | 0 | 8 → 8 | 0.000 | 1.473 |
| Jogador 1 | 6-4 | 3 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 29% → 29% | 64 → 72 | 3 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-5 | 3 | -48.000 | -32.000 | 2 → 0 | 3 → 0 | 29% → 0% | 72 → 67 | 5 | 8 → 8 | -0.177 | -0.933 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 11, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 6; mudanças de composição: 1; posicionamento melhorou em 23 ações e piorou em 22.
- Jogador 1 — estado final: ouro 67, nível 8, vida 5.0, colocação 2.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.028 | 0.000 |
| Jogador 2 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.006 | 0.000 |
| Jogador 2 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 2 | 2-1 | 5 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 8 → 7 | 7 | 4 → 4 | -0.002 | 0.512 |
| Jogador 2 | 2-2 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 7 → 8 | 6 | 4 → 5 | -0.014 | 0.384 |
| Jogador 2 | 2-3 | 6 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 8 | 7 | 5 → 5 | 0.005 | 0.419 |
| Jogador 2 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 6 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 2 | 2-5 | 4 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 9 | 4 | 5 → 6 | -0.008 | 0.701 |
| Jogador 2 | 2-6 | 6 | 2.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 10 | 7 | 6 → 6 | 0.000 | 0.459 |
| Jogador 2 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 10 | 8 | 6 → 6 | 0.000 | 0.738 |
| Jogador 2 | 3-2 | 7 | 4.000 | -4.000 | 0 → 0 | 2 → 2 | 21% → 25% | 10 → 11 | 8 | 6 → 7 | -0.000 | 0.426 |
| Jogador 2 | 3-3 | 9 | 4.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 10 | 12 | 7 → 7 | 0.007 | 0.337 |
| Jogador 2 | 3-4 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 10 → 10 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 10 → 11 | 8 | 7 → 7 | 0.000 | 0.738 |
| Jogador 2 | 3-6 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 12 | 12 | 7 → 7 | -0.010 | 0.483 |
| Jogador 2 | 3-7 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 12 → 8 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 5 | 8.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 29% | 8 → 9 | 8 | 7 → 8 | 0.063 | 0.607 |
| Jogador 2 | 4-2 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 10 | 12 | 8 → 8 | 0.000 | 0.506 |
| Jogador 2 | 4-3 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 10 → 11 | 8 | 8 → 8 | 0.000 | 0.740 |
| Jogador 2 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 11 → 20 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 20 → 9 | 20 | 8 → 8 | 0.000 | 0.412 |
| Jogador 2 | 4-6 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 10 | 8 | 8 → 8 | 0.000 | 0.740 |
| Jogador 2 | 4-7 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 10 → 10 | 8 | 8 → 9 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 6 | 8.000 | 2.000 | 0 → 0 | 2 → 2 | 29% → 32% | 10 → 14 | 5 | 9 → 9 | -0.007 | 0.487 |
| Jogador 2 | 5-2 | 3 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 32% → 32% | 14 → 14 | 5 | 9 → 9 | 0.000 | -0.933 |
| Jogador 2 | 5-3 | 11 | 0.000 | -12.000 | 0 → 1 | 2 → 1 | 32% → 29% | 14 → 7 | 23 | 9 → 9 | -0.042 | -0.250 |
| Jogador 2 | 5-4 | 5 | 8.000 | -2.000 | 1 → 1 | 1 → 1 | 29% → 32% | 7 → 6 | 7 | 9 → 9 | -0.022 | 0.000 |
| Jogador 2 | 5-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 6 → 12 | 0 | 9 → 9 | 0.000 | 1.461 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 12 → 18 | 0 | 9 → 9 | 0.000 | -1.400 |
| Jogador 2 | 5-7 | 3 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 32% → 32% | 18 → 20 | 4 | 9 → 9 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 9 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 20 → 5 | 20 | 9 → 9 | 0.000 | 0.000 |
| Jogador 2 | 6-2 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 5 → 11 | 0 | 9 → 9 | 0.000 | 1.473 |
| Jogador 2 | 6-3 | 4 | -2.000 | 2.000 | 1 → 1 | 2 → 1 | 32% → 32% | 11 → 12 | 4 | 9 → 9 | 0.025 | 0.000 |
| Jogador 2 | 6-4 | 3 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 32% → 32% | 12 → 13 | 4 | 9 → 9 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 13 → 14 | 0 | 9 → 9 | 0.000 | 1.498 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 13, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 12 ações e piorou em 11.
- Jogador 2 — estado final: ouro 14, nível 9, vida 51.0, colocação 1.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 3 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.002 | 0.000 |
| Jogador 3 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | 0.022 | 0.000 |
| Jogador 3 | 1-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 5 | 4 | 3 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 5 → 9 | 2 | 4 → 4 | -0.003 | 0.502 |
| Jogador 3 | 2-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 14 | 0 | 4 → 4 | 0.000 | -1.155 |
| Jogador 3 | 2-3 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 14 → 9 | 11 | 4 → 5 | 0.006 | -0.395 |
| Jogador 3 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 7 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 2-5 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 7 → 6 | 7 | 5 → 6 | -0.053 | -0.405 |
| Jogador 3 | 2-6 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 6 → 7 | 5 | 6 → 6 | 0.000 | -0.646 |
| Jogador 3 | 2-7 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | -0.658 |
| Jogador 3 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 8 | 8 | 6 → 7 | 0.000 | -0.681 |
| Jogador 3 | 3-3 | 5 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 25% | 8 → 14 | 0 | 7 → 7 | -0.083 | 0.572 |
| Jogador 3 | 3-4 | 6 | 4.000 | 2.000 | 0 → 0 | 2 → 2 | 25% → 25% | 14 → 8 | 11 | 7 → 7 | 0.001 | 0.000 |
| Jogador 3 | 3-5 | 7 | 2.000 | 4.000 | 0 → 0 | 2 → 1 | 25% → 25% | 8 → 8 | 8 | 7 → 7 | -0.012 | 0.395 |
| Jogador 3 | 3-6 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 7 | 8 | 7 → 7 | 0.000 | 0.703 |
| Jogador 3 | 3-7 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 6 | 8 | 7 → 7 | 0.000 | -0.721 |
| Jogador 3 | 4-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | -0.905 |
| Jogador 3 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | 1.400 |
| Jogador 3 | 4-4 | 5 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 25% → 29% | 14 → 16 | 4 | 7 → 8 | 0.019 | 0.000 |
| Jogador 3 | 4-5 | 6 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 29% → 29% | 16 → 6 | 15 | 8 → 8 | 0.000 | -0.444 |
| Jogador 3 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 6 → 12 | 0 | 8 → 8 | 0.000 | -1.400 |
| Jogador 3 | 4-7 | 3 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 29% → 29% | 12 → 14 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 14 → 21 | 0 | 8 → 8 | 0.000 | 0.746 |
| Jogador 3 | 5-2 | 4 | 2.000 | 6.000 | 0 → 0 | 3 → 2 | 29% → 29% | 21 → 22 | 7 | 8 → 8 | 0.118 | 0.743 |
| Jogador 3 | 5-3 | 3 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 29% → 29% | 22 → 26 | 4 | 8 → 8 | 0.000 | 0.974 |
| Jogador 3 | 5-4 | 3 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 29% → 29% | 26 → 31 | 3 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 3 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 29% → 29% | 31 → 37 | 3 | 8 → 8 | 0.000 | 0.991 |
| Jogador 3 | 5-6 | 3 | -38.000 | -40.000 | 0 → 0 | 3 → 0 | 29% → 0% | 37 → 33 | 4 | 8 → 8 | -0.086 | -0.933 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 8, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 5; mudanças de composição: 0; posicionamento melhorou em 10 ações e piorou em 11.
- Jogador 3 — estado final: ouro 33, nível 8, vida 6.0, colocação 4.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 4 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.002 | 0.000 |
| Jogador 4 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.170 | 0.000 |
| Jogador 4 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 4 | 2-1 | 8 | 4.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 8 → 9 | 4 | 4 → 4 | -0.029 | -0.322 |
| Jogador 4 | 2-2 | 5 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 11% → 14% | 9 → 8 | 7 | 4 → 4 | 0.017 | -0.494 |
| Jogador 4 | 2-3 | 5 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 8 → 8 | 6 | 4 → 5 | 0.023 | -0.496 |
| Jogador 4 | 2-4 | 5 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 8 → 8 | 6 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 2-5 | 6 | 2.000 | 0.000 | 1 → 1 | 0 → 1 | 18% → 18% | 8 → 9 | 7 | 5 → 5 | -0.024 | -0.439 |
| Jogador 4 | 2-6 | 6 | 4.000 | 2.000 | 1 → 1 | 1 → 1 | 18% → 21% | 9 → 9 | 7 | 5 → 6 | -0.033 | -0.423 |
| Jogador 4 | 2-7 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 3-1 | 7 | 2.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 8 → 6 | 10 | 6 → 6 | 0.000 | 0.402 |
| Jogador 4 | 3-2 | 5 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | -0.012 | -0.507 |
| Jogador 4 | 3-3 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | -0.955 |
| Jogador 4 | 3-4 | 5 | 4.000 | -4.000 | 1 → 1 | 1 → 1 | 21% → 25% | 9 → 7 | 8 | 6 → 7 | 0.010 | 0.000 |
| Jogador 4 | 3-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 13 | 0 | 7 → 7 | 0.000 | 1.450 |
| Jogador 4 | 3-6 | 7 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 25% → 25% | 13 → 8 | 10 | 7 → 7 | 0.002 | -0.382 |
| Jogador 4 | 3-7 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 5 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 5 → 7 | 4 | 7 → 7 | 0.000 | 0.733 |
| Jogador 4 | 4-2 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 7 → 10 | 4 | 7 → 7 | 0.000 | 0.961 |
| Jogador 4 | 4-3 | 4 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 10 → 8 | 7 | 7 → 7 | -0.000 | -0.691 |
| Jogador 4 | 4-4 | 4 | 4.000 | -4.000 | 1 → 1 | 3 → 3 | 25% → 29% | 8 → 5 | 8 | 7 → 8 | -0.008 | 0.000 |
| Jogador 4 | 4-5 | 3 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 29% → 29% | 5 → 7 | 4 | 8 → 8 | 0.000 | 0.945 |
| Jogador 4 | 4-6 | 3 | 0.000 | 8.000 | 1 → 1 | 3 → 4 | 29% → 29% | 7 → 8 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 4-7 | 2 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 29% → 29% | 8 → 13 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-1 | 8 | 8.000 | -8.000 | 1 → 2 | 4 → 3 | 29% → 29% | 13 → 7 | 11 | 8 → 8 | 0.111 | -0.350 |
| Jogador 4 | 5-2 | 3 | -46.000 | -14.000 | 2 → 0 | 3 → 0 | 29% → 0% | 7 → 3 | 4 | 8 → 8 | -0.064 | -0.917 |
- Jogador 4 — valor marginal das compras: COMPOSITION_COMPATIBILITY: 10, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 5; mudanças de composição: 0; posicionamento melhorou em 11 ações e piorou em 12.
- Jogador 4 — estado final: ouro 3, nível 8, vida 8.0, colocação 6.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 5 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 5 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.066 | 0.000 |
| Jogador 5 | 1-4 | 5 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.016 | 0.000 |
| Jogador 5 | 2-1 | 6 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 7 | 3 | 4 → 4 | -0.060 | -0.404 |
| Jogador 5 | 2-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 8 | 7 | 4 → 4 | 0.000 | -0.404 |
| Jogador 5 | 2-3 | 5 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 14% → 18% | 8 → 6 | 8 | 4 → 5 | -0.012 | 0.502 |
| Jogador 5 | 2-4 | 4 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 8 | 3 | 5 → 5 | 0.130 | 0.000 |
| Jogador 5 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 5 | 8 | 5 → 6 | 0.033 | -0.527 |
| Jogador 5 | 2-6 | 5 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 21% | 5 → 7 | 4 | 6 → 6 | 0.027 | 0.502 |
| Jogador 5 | 2-7 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 21% → 21% | 7 → 6 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-1 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 7 | 4 | 6 → 6 | 0.000 | -0.894 |
| Jogador 5 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | 0.905 |
| Jogador 5 | 3-3 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 0 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | -0.537 |
| Jogador 5 | 3-4 | 6 | 8.000 | -8.000 | 0 → 0 | 0 → 0 | 21% → 25% | 8 → 5 | 8 | 6 → 7 | -0.024 | 0.000 |
| Jogador 5 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 5 → 11 | 0 | 7 → 7 | 0.000 | 1.425 |
| Jogador 5 | 3-6 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 11 → 8 | 8 | 7 → 7 | 0.000 | -0.669 |
| Jogador 5 | 3-7 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 25% → 25% | 8 → 6 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | -0.875 |
| Jogador 5 | 4-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | 0.000 | -0.721 |
| Jogador 5 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 12 | 0 | 7 → 7 | 0.000 | -1.313 |
| Jogador 5 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 19 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 19 → 27 | 0 | 7 → 7 | 0.000 | 1.442 |
| Jogador 5 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 27 → 34 | 0 | 7 → 7 | 0.000 | -1.382 |
| Jogador 5 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 34 → 42 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 5 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 42 → 46 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-2 | 2 | -36.000 | -14.000 | 0 → 0 | 1 → 0 | 25% → 0% | 46 → 46 | 0 | 7 → 7 | -0.267 | -1.425 |
- Jogador 5 — valor marginal das compras: COMPOSITION_COMPATIBILITY: 8, PAIR_POTENTIAL: 2; mudanças de composição: 0; posicionamento melhorou em 7 ações e piorou em 11.
- Jogador 5 — estado final: ouro 46, nível 7, vida 4.0, colocação 5.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 6 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.003 | 0.000 |
| Jogador 6 | 1-3 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 0 | 3 → 3 | 0.015 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 5 | 4 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 5 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 5 | -0.024 | -0.474 |
| Jogador 6 | 2-2 | 4 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 5 → 8 | 3 | 5 → 5 | -0.067 | 0.653 |
| Jogador 6 | 2-3 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 8 → 8 | 7 | 5 → 5 | 0.033 | 0.537 |
| Jogador 6 | 2-4 | 6 | 4.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 8 → 14 | 3 | 5 → 5 | 0.019 | 0.000 |
| Jogador 6 | 2-5 | 6 | 2.000 | -2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 14 → 9 | 12 | 5 → 6 | -0.009 | 0.440 |
| Jogador 6 | 2-6 | 4 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 9 → 7 | 7 | 6 → 6 | -0.015 | -0.607 |
| Jogador 6 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 8 | 4 | 6 → 6 | 0.009 | 0.000 |
| Jogador 6 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 6 | 8 | 6 → 6 | 0.000 | -0.694 |
| Jogador 6 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | 0.937 |
| Jogador 6 | 3-3 | 4 | 6.000 | -6.000 | 0 → 0 | 3 → 3 | 21% → 25% | 8 → 11 | 4 | 6 → 7 | 0.082 | 0.713 |
| Jogador 6 | 3-4 | 4 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 25% → 25% | 11 → 9 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 3-5 | 3 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 9 → 14 | 0 | 7 → 7 | -0.159 | -0.892 |
| Jogador 6 | 3-6 | 5 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 14 → 8 | 12 | 7 → 7 | 0.000 | -0.527 |
| Jogador 6 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 5 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 14 → 8 | 12 | 7 → 7 | 0.000 | -0.550 |
| Jogador 6 | 4-2 | 3 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 8 → 11 | 3 | 7 → 7 | 0.000 | 0.978 |
| Jogador 6 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 11 → 17 | 0 | 7 → 7 | 0.000 | -1.400 |
| Jogador 6 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 17 → 23 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 23 → 31 | 0 | 7 → 7 | 0.000 | -1.357 |
| Jogador 6 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 31 → 40 | 0 | 7 → 7 | 0.000 | -1.416 |
| Jogador 6 | 4-7 | 3 | 2.000 | -2.000 | 0 → 0 | 4 → 3 | 25% → 25% | 40 → 46 | 3 | 7 → 7 | -0.003 | 0.000 |
| Jogador 6 | 5-1 | 5 | -28.000 | -12.000 | 0 → 0 | 3 → 0 | 25% → 0% | 46 → 43 | 3 | 7 → 7 | -0.021 | -0.580 |
- Jogador 6 — valor marginal das compras: COMPOSITION_COMPATIBILITY: 6, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 11 ações e piorou em 10.
- Jogador 6 — estado final: ouro 43, nível 7, vida 5.0, colocação 7.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 7 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.146 | 0.000 |
| Jogador 7 | 1-3 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | 0.004 | 0.000 |
| Jogador 7 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 9 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 9 → 8 | 6 | 4 → 4 | 0.001 | -0.404 |
| Jogador 7 | 2-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 8 → 14 | 0 | 4 → 4 | 0.000 | 1.215 |
| Jogador 7 | 2-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 14 → 20 | 0 | 4 → 5 | 0.000 | -1.265 |
| Jogador 7 | 2-4 | 8 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 20 → 5 | 20 | 5 → 5 | 0.024 | 0.000 |
| Jogador 7 | 2-5 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 5 → 6 | 5 | 5 → 6 | -0.021 | 0.467 |
| Jogador 7 | 2-6 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 8 | 3 | 6 → 6 | 0.000 | -0.791 |
| Jogador 7 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 8 → 5 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 3-1 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 5 → 7 | 4 | 6 → 6 | 0.000 | -0.878 |
| Jogador 7 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | -0.878 |
| Jogador 7 | 3-3 | 5 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 25% | 9 → 7 | 8 | 6 → 7 | 0.010 | -0.517 |
| Jogador 7 | 3-4 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 7 → 10 | 3 | 7 → 7 | 0.173 | 0.000 |
| Jogador 7 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 10 → 18 | 0 | 7 → 7 | 0.000 | -1.291 |
| Jogador 7 | 3-6 | 3 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 18 → 23 | 4 | 7 → 7 | 0.000 | -0.908 |
| Jogador 7 | 3-7 | 7 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 25% → 25% | 23 → 11 | 20 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 11 → 20 | 0 | 7 → 7 | 0.000 | -1.382 |
| Jogador 7 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 20 → 30 | 0 | 7 → 7 | 0.000 | -1.382 |
| Jogador 7 | 4-3 | 2 | -26.000 | -22.000 | 0 → 0 | 3 → 0 | 25% → 0% | 30 → 30 | 0 | 7 → 7 | -0.157 | -1.425 |
- Jogador 7 — valor marginal das compras: COMPOSITION_COMPATIBILITY: 6, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 8 ações e piorou em 8.
- Jogador 7 — estado final: ouro 30, nível 7, vida 9.0, colocação 8.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 8 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.028 | 0.000 |
| Jogador 8 | 1-3 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | -0.023 | 0.000 |
| Jogador 8 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 9 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 8 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 9 → 6 | 9 | 4 → 5 | -0.002 | 0.366 |
| Jogador 8 | 2-2 | 4 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 6 → 10 | 3 | 5 → 5 | 0.005 | 0.641 |
| Jogador 8 | 2-3 | 4 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 10 | 7 | 5 → 5 | -0.015 | 0.659 |
| Jogador 8 | 2-4 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 8 | 11 | 5 → 5 | 0.015 | 0.000 |
| Jogador 8 | 2-5 | 10 | 8.000 | -6.000 | 0 → 0 | 1 → 0 | 18% → 21% | 8 → 10 | 6 | 5 → 6 | -0.004 | 0.259 |
| Jogador 8 | 2-6 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 10 | 8 | 6 → 6 | 0.012 | 0.370 |
| Jogador 8 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 7 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 9 | 12 | 6 → 6 | -0.002 | 0.409 |
| Jogador 8 | 3-2 | 7 | 8.000 | -8.000 | 0 → 0 | 0 → 0 | 21% → 25% | 9 → 6 | 8 | 6 → 7 | -0.092 | -0.402 |
| Jogador 8 | 3-3 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | 0.921 |
| Jogador 8 | 3-4 | 6 | -2.000 | 8.000 | 0 → 0 | 0 → 1 | 25% → 25% | 8 → 6 | 7 | 7 → 7 | 0.098 | 0.000 |
| Jogador 8 | 3-5 | 4 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 7 | 4 | 7 → 7 | -0.146 | -0.694 |
| Jogador 8 | 3-6 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.950 |
| Jogador 8 | 3-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 6 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 9 | 4 | 7 → 7 | 0.000 | 0.700 |
| Jogador 8 | 4-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 8 | 8 | 7 → 7 | 0.000 | 0.708 |
| Jogador 8 | 4-3 | 6 | 8.000 | -2.000 | 0 → 0 | 1 → 1 | 25% → 29% | 8 → 8 | 8 | 7 → 8 | 0.010 | 0.502 |
| Jogador 8 | 4-4 | 5 | 2.000 | 6.000 | 0 → 0 | 1 → 1 | 29% → 29% | 8 → 6 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 29% → 29% | 6 → 8 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 4-6 | 4 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 29% → 29% | 8 → 8 | 8 | 8 → 8 | 0.000 | 0.733 |
| Jogador 8 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 8 → 15 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 6 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 29% → 29% | 15 → 11 | 13 | 8 → 8 | 0.000 | 0.514 |
| Jogador 8 | 5-2 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 11 → 12 | 8 | 8 → 8 | 0.000 | 0.751 |
| Jogador 8 | 5-3 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 12 → 5 | 12 | 8 → 8 | 0.000 | -0.550 |
| Jogador 8 | 5-4 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 5 → 6 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 6 → 8 | 4 | 8 → 8 | 0.000 | -0.933 |
| Jogador 8 | 5-6 | 4 | 6.000 | -6.000 | 0 → 0 | 2 → 2 | 29% → 32% | 8 → 10 | 4 | 8 → 9 | -0.008 | 0.746 |
| Jogador 8 | 5-7 | 4 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 32% → 32% | 10 → 6 | 9 | 9 → 9 | 0.150 | 0.000 |
| Jogador 8 | 6-1 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 32% → 32% | 6 → 11 | 0 | 9 → 9 | -0.061 | -0.458 |
| Jogador 8 | 6-2 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 32% → 32% | 11 → 9 | 8 | 9 → 9 | 0.000 | -0.688 |
| Jogador 8 | 6-3 | 2 | -52.000 | -36.000 | 0 → 0 | 2 → 0 | 32% → 0% | 9 → 9 | 0 | 9 → 9 | -0.027 | -1.375 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 11, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 14 ações e piorou em 14.
- Jogador 8 — estado final: ouro 9, nível 9, vida 9.0, colocação 3.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 22 | 3 | 0 | 0 | 1 | 0 | 3 | 1 | 5.4844 |
| Jogador 2 | 20 | 6 | 0 | 0 | 1 | 0 | 2 | 2 | 3.4135 |
| Jogador 3 | 16 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 2.4753 |
| Jogador 4 | 17 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 7.1451 |
| Jogador 5 | 10 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 3.3108 |
| Jogador 6 | 12 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 4.8604 |
| Jogador 7 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4.2237 |
| Jogador 8 | 16 | 4 | 0 | 0 | 1 | 0 | 0 | 2 | 2.5406 |
- Jogador 1 — venda DA_KogMaw18_AD (4-2, step 465): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Nidalee18_AP (3-6, step 405): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Ezreal (4-2, step 463): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Lux_Sunbeam (5-3, step 622): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Ashe (5-3, step 623): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_Yorick (3-5, step 382): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 4 — venda DA_18_LeBlanc (2-5, step 220): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Yunara (3-3, step 340): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Leona (2-5, step 222): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Krug18 (3-1, step 292): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **3**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente. Ganhos nas três ações seguintes do mesmo round podem compensar uma venda; falta de ganho imediato isoladamente não gera penalidade.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| MEDIUM | Jogador 1 | 3-7 | 424 | PURCHASE_REVERSED | Compra de DA_18_Sejuani desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 4-2 | 465 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-3 | 186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-4 | 221 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 6-5 | 2432 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-5 | 2433 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-2 | 458 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-2 | 469 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-3 | 551 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 2-4 | 611 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-4 | 2095 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 2 | 3-6 | 405 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-2 | 463 | SOLD_CORE_UNIT | Venda de 'DA_18_Ezreal' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-2 | 463 | PURCHASE_REVERSED | Compra de DA_18_Ezreal desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| LOW | Jogador 2 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 139 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-1 | 328 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-2 | 447 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-3 | 505 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-3 | 516 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-4 | 562 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-7 | 1293 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1935 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1946 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1957 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1968 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-3 | 2027 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2230 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2241 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2252 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2263 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2274 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-3 | 186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-4 | 232 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 5-6 | 1813 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-6 | 1814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 2-2 | 351 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-2 | 386 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-3 | 432 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-3 | 443 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-4 | 489 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-5 | 583 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-6 | 629 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 675 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 686 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-1 | 732 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-1 | 743 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-3 | 1312 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 1-3 | 186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 1-4 | 221 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 5-2 | 1732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-2 | 1733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-2 | 410 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-3 | 493 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-4 | 587 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-5 | 633 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-3 | 340 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-2 | 1530 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-2 | 1531 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-3 | 1292 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-4 | 1327 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-5 | 1362 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-4 | 269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-1 | 1496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-1 | 1497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 2-2 | 436 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 566 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 577 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-4 | 588 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-5 | 658 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-6 | 704 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-7 | 762 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 2-7 | 773 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-1 | 819 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-3 | 1282 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-4 | 1317 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-5 | 1352 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 1-3 | 199 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 1-4 | 234 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 4-3 | 1164 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-3 | 1165 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-2 | 363 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-3 | 422 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-3 | 433 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-3 | 444 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-3 | 455 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-4 | 501 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-6 | 631 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-6 | 642 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-7 | 688 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-1 | 734 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-2 | 780 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-7 | 1070 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-1 | 1105 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-4 | 194 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-5 | 222 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Leona' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 3-1 | 292 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 6-3 | 2318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-3 | 2319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-4 | 572 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-3 | 1936 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-4 | 1982 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-5 | 2028 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-6 | 2101 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
