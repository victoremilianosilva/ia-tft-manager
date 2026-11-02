# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **0**
- Achados: **226**
- CRITICAL: 0 | HIGH: 0 | MEDIUM: 77 | LOW: 149

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
| Jogador 3 | 99 | 16 | 1 | 25 | 0 | 37 | 18 | 0.0486 | 10 | 18 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 2, ALL_IN::PASS: 13, FAST8::BUY: 1, FAST8::BUY_XP: 9, FAST8::MOVE_BENCH: 3, FAST8::PASS: 6, FAST8::SELL: 1, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 11, SLOWROLL::MOVE_BENCH: 3, SLOWROLL::PASS: 7, STABILIZE::BUY: 5, STABILIZE::BUY_XP: 5, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 11
- Jogador 3 — recompensas por ação: BUY: média 0.3844 (n=16), BUY_XP: média -0.0208 (n=25), ITEM: média 0.0900 (n=2), MOVE_BENCH: média 0.0641 (n=17), MOVE_BOARD: média -0.2100 (n=1), PASS: média -0.0286 (n=37), SELL: média -0.8200 (n=1)
| Jogador 4 | 104 | 17 | 3 | 24 | 0 | 37 | 21 | 0.0800 | 6 | 26 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::PASS: 11, FAST8::BUY: 4, FAST8::BUY_XP: 10, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 3, FAST8::PASS: 8, FAST8::SELL: 2, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 4, SLOWROLL::MOVE_BENCH: 3, SLOWROLL::PASS: 3, SLOWROLL::SELL: 1, STABILIZE::BUY: 9, STABILIZE::BUY_XP: 10, STABILIZE::ITEM: 2, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 2, STABILIZE::PASS: 15
- Jogador 4 — recompensas por ação: BUY: média 0.4618 (n=17), BUY_XP: média -0.0013 (n=24), ITEM: média 0.0550 (n=2), MOVE_BENCH: média 0.1269 (n=16), MOVE_BOARD: média -0.0500 (n=5), PASS: média -0.0014 (n=37), SELL: média -0.4467 (n=3)
| Jogador 5 | 87 | 10 | 2 | 18 | 0 | 37 | 18 | 0.0321 | 8 | 24 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::ITEM: 2, ALL_IN::PASS: 13, FAST8::BUY: 3, FAST8::BUY_XP: 12, FAST8::MOVE_BENCH: 3, FAST8::PASS: 10, FAST8::SELL: 1, STABILIZE::BUY: 6, STABILIZE::BUY_XP: 6, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 3, STABILIZE::PASS: 14, STABILIZE::SELL: 1
- Jogador 5 — recompensas por ação: BUY: média 0.3000 (n=10), BUY_XP: média -0.0167 (n=18), ITEM: média 0.0450 (n=2), MOVE_BENCH: média 0.1320 (n=15), MOVE_BOARD: média 0.0167 (n=3), PASS: média -0.0327 (n=37), SELL: média -0.4100 (n=2)
| Jogador 6 | 87 | 12 | 2 | 19 | 0 | 37 | 16 | 0.0635 | 10 | 27 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::ITEM: 1, ALL_IN::MOVE_BENCH: 1, ALL_IN::PASS: 13, FAST8::BUY: 2, FAST8::BUY_XP: 7, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 1, FAST8::PASS: 8, SLOWROLL::BUY: 4, SLOWROLL::BUY_XP: 9, SLOWROLL::MOVE_BENCH: 5, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 8, SLOWROLL::SELL: 1, STABILIZE::BUY: 4, STABILIZE::BUY_XP: 3, STABILIZE::MOVE_BENCH: 6, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 8, STABILIZE::SELL: 1
- Jogador 6 — recompensas por ação: BUY: média 0.5567 (n=12), BUY_XP: média -0.0342 (n=19), ITEM: média 0.0000 (n=1), MOVE_BENCH: média 0.0862 (n=13), MOVE_BOARD: média -0.0800 (n=3), PASS: média -0.0286 (n=37), SELL: média -0.1650 (n=2)
| Jogador 7 | 74 | 9 | 0 | 16 | 0 | 37 | 12 | 0.0684 | 3 | 38 |
- Jogador 7 — ações por estratégia: ALL_IN::PASS: 17, FAST8::BUY: 2, FAST8::MOVE_BENCH: 1, FAST8::PASS: 4, SLOWROLL::BUY: 3, SLOWROLL::BUY_XP: 10, SLOWROLL::MOVE_BENCH: 2, SLOWROLL::MOVE_BOARD: 1, SLOWROLL::PASS: 6, STABILIZE::BUY: 4, STABILIZE::BUY_XP: 6, STABILIZE::MOVE_BENCH: 7, STABILIZE::MOVE_BOARD: 1, STABILIZE::PASS: 10
- Jogador 7 — recompensas por ação: BUY: média 0.3978 (n=9), BUY_XP: média -0.0394 (n=16), MOVE_BENCH: média 0.2800 (n=10), MOVE_BOARD: média -0.1500 (n=2), PASS: média -0.0105 (n=37)
| Jogador 8 | 130 | 16 | 4 | 38 | 0 | 37 | 31 | -0.0041 | 15 | 8 |
- Jogador 8 — ações por estratégia: ALL_IN::PASS: 3, ECON::BUY: 1, ECON::BUY_XP: 4, ECON::ITEM: 2, ECON::MOVE_BENCH: 3, ECON::PASS: 5, FAST8::BUY: 1, FAST8::BUY_XP: 9, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 5, FAST8::PASS: 7, SLOWROLL::BUY: 1, SLOWROLL::BUY_XP: 1, STABILIZE::BUY: 8, STABILIZE::BUY_XP: 14, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 3, STABILIZE::PASS: 14, STABILIZE::SELL: 3, WINSTREAK::BUY: 5, WINSTREAK::BUY_XP: 10, WINSTREAK::ITEM: 1, WINSTREAK::MOVE_BENCH: 2, WINSTREAK::PASS: 8, WINSTREAK::SELL: 1
- Jogador 8 — recompensas por ação: BUY: média 0.2369 (n=16), BUY_XP: média -0.0208 (n=38), ITEM: média 0.0600 (n=4), MOVE_BENCH: média -0.0843 (n=28), MOVE_BOARD: média 0.0400 (n=3), PASS: média -0.0014 (n=37), SELL: média -0.3700 (n=4)

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
| Jogador 2 | 3-7 | 11:49:31 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_Amumu18 | 0.0900 | ECON_SPEND_BELOW_50_REVIEW |
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
| Jogador 2 | 5-2 | 11:50:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 21 | 0 | Colosso | DA_18_MasterYi_AD | 0.8700 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:42 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 21 | 0 | Colosso | DA_18_MasterYi_AD | 0.5500 |  |
| Jogador 2 | 5-2 | 11:50:42 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 17 | 0 | Colosso | DA_18_MasterYi_AD | 0.0900 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:42 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 13 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:42 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 9 | 0 | Colosso | DA_18_MasterYi_AD | -0.1100 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:42 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:43 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-2 | 11:50:44 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-3 | 11:50:49 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_MasterYi_AD | 0.2100 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-3 | 11:50:50 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_MasterYi_AD | -0.0300 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-3 | 11:50:50 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-3 | 11:50:54 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 0 | 0 | Colosso | DA_18_MasterYi_AD | 0.3900 |  |
| Jogador 2 | 5-4 | 11:50:58 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 6 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-5 | 11:51:06 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 12 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-6 | 11:51:15 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 14 | 1 | Colosso | DA_18_MasterYi_AD | 0.7800 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-6 | 11:51:15 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 14 | 1 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-7 | 11:51:23 | BIGORNA: escolheu item completo TFT_Item_IonicSpark | ECON | ECON: acumular até o limite de juros de 50 | 20 | 1 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 5-7 | 11:51:24 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Amumu (i:8.0) (tabuleiro slot 10) | ECON | ECON: acumular até o limite de juros de 50 | 20 | 1 | Colosso | DA_18_MasterYi_AD | 0.1300 |  |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 16 | 1 | Colosso | DA_18_MasterYi_AD | -0.0900 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 12 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 8 | 1 | Colosso | DA_18_MasterYi_AD | -0.0900 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:24 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:25 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 0 | 1 | Colosso | DA_18_MasterYi_AD | -0.0100 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 5-7 | 11:51:25 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 0 | 1 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 6-1 | 11:51:32 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Colosso | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 2 | 6-2 | 11:51:40 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Colosso | DA_18_Ahri | 0.7600 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 2 | 6-2 | 11:51:40 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Colosso | DA_18_Ahri | 0.0000 |  |
| Jogador 2 | 6-2 | 11:51:45 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 7 | 0 | Colosso | DA_18_Ahri | 0.5800 |  |
| Jogador 2 | 6-3 | 11:51:48 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 8 | 0 | Colosso | DA_18_Ahri | 0.2000 | ECON_SPEND_BELOW_50_REVIEW |
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
| Jogador 3 | 5-6 | 11:51:15 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 5-7 | 11:51:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 6-1 | 11:51:32 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 6-2 | 11:51:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 6-3 | 11:51:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | 0.0000 |  |
| Jogador 3 | 6-4 | 11:51:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 33 | 2 | Inferno | DA_18_Tristana | 0.0000 |  |
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
| Jogador 4 | 5-2 | 11:50:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 5-3 | 11:50:49 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 5-4 | 11:50:58 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 5-5 | 11:51:06 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 5-6 | 11:51:15 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 5-7 | 11:51:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 6-1 | 11:51:32 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 6-2 | 11:51:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 6-3 | 11:51:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 4 | 6-4 | 11:51:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Fera do Rift | DA_CrimsonRaptor18 | 0.0000 |  |
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
| Jogador 5 | 5-2 | 11:50:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 5-3 | 11:50:49 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 5-4 | 11:50:58 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 5-5 | 11:51:06 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 5-6 | 11:51:15 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 5-7 | 11:51:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 6-1 | 11:51:32 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 6-2 | 11:51:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 6-3 | 11:51:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
| Jogador 5 | 6-4 | 11:51:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 46 | 3 | Florescer | DA_18_Ahri | 0.0000 |  |
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
| Jogador 6 | 5-1 | 11:50:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-2 | 11:50:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-3 | 11:50:49 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-4 | 11:50:58 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-5 | 11:51:06 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-6 | 11:51:15 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-7 | 11:51:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 6-1 | 11:51:32 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 6-2 | 11:51:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 6-3 | 11:51:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 6-4 | 11:51:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 43 | 3 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
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
| Jogador 7 | 4-3 | 11:49:53 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-4 | 11:50:01 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-5 | 11:50:09 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-6 | 11:50:16 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-7 | 11:50:24 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 11:50:33 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 11:50:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-3 | 11:50:49 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-4 | 11:50:58 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-5 | 11:51:06 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-6 | 11:51:15 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-7 | 11:51:23 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-1 | 11:51:32 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-2 | 11:51:40 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-3 | 11:51:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 6-4 | 11:51:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 30 | 2 | Inferno | DA_Sentinel18 | 0.0000 |  |
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
| Jogador 8 | 5-3 | 11:50:49 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-3 | 11:50:50 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-4 | 11:50:58 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0100 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-4 | 11:50:58 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 2 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-5 | 11:51:06 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0600 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-5 | 11:51:07 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Lux_Elderwood | 0.0000 |  |
| Jogador 8 | 5-5 | 11:51:11 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 4 | 0 | Colosso | DA_18_Lux_Elderwood | -0.0500 |  |
| Jogador 8 | 5-6 | 11:51:15 | COMPROU: Dragão Ancião (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 5 | 0 | Colosso | DA_18_ElderDragon | 0.0500 | ECON_SPEND_BELOW_50_REVIEW |
| Jogador 8 | 5-6 | 11:51:15 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 1 | 0 | Colosso | DA_18_ElderDragon | -0.0100 | ECON_SPEND_BELOW_50_REVIEW |
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
| Jogador 8 | 6-3 | 11:51:48 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 9 | 0 | Colosso | DA_18_ElderDragon | 0.0000 |  |
| Jogador 8 | 6-4 | 11:51:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 9 | 0 | Colosso | DA_18_ElderDragon | 0.0000 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
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
| LOW | Jogador 2 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 139 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-1 | 328 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-2 | 447 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-3 | 505 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-3 | 516 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-4 | 562 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-7 | 1293 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1898 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1923 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1935 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1946 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1957 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-2 | 1968 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-3 | 2014 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-3 | 2027 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-6 | 2155 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2230 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2241 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2252 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2263 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-7 | 2274 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 6-2 | 2355 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 6-3 | 2415 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-3 | 186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-4 | 232 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 5-6 | 1813 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-6 | 1814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 5-7 | 1855 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-7 | 1856 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 6-1 | 1891 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 6-1 | 1892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 6-2 | 1927 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 6-2 | 1928 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 6-3 | 1963 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 6-3 | 1964 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 6-4 | 1999 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 6-4 | 2000 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 6-5 | 2035 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 6-5 | 2036 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
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
| LOW | Jogador 4 | 5-3 | 1771 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-3 | 1772 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 5-4 | 1807 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-4 | 1808 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 5-5 | 1843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-5 | 1844 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 5-6 | 1879 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-6 | 1880 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 5-7 | 1915 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-7 | 1916 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 6-1 | 1951 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 6-1 | 1952 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 6-2 | 1987 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 6-2 | 1988 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 6-3 | 2023 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 6-3 | 2024 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 6-4 | 2059 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 6-4 | 2060 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 6-5 | 2095 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 6-5 | 2096 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-2 | 410 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-3 | 493 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-4 | 587 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-5 | 633 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-2 | 1530 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-2 | 1531 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-3 | 1568 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-3 | 1569 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-4 | 1604 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-4 | 1605 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-5 | 1640 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-5 | 1641 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-6 | 1676 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-6 | 1677 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 5-7 | 1712 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-7 | 1713 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 6-1 | 1748 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-1 | 1749 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 6-2 | 1784 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-2 | 1785 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 6-3 | 1820 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-3 | 1821 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 6-4 | 1856 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-4 | 1857 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 6-5 | 1892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-5 | 1893 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 4-3 | 1292 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-4 | 1327 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-5 | 1362 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-4 | 269 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-1 | 1496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-1 | 1497 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-2 | 1535 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-2 | 1536 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-3 | 1571 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-3 | 1572 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-4 | 1607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-4 | 1608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-5 | 1643 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-5 | 1644 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-6 | 1679 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-6 | 1680 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 5-7 | 1715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-7 | 1716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 6-1 | 1751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-1 | 1752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 6-2 | 1787 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-2 | 1788 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 6-3 | 1823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-3 | 1824 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 6-4 | 1859 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-4 | 1860 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 6-5 | 1895 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 6-5 | 1896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
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
| LOW | Jogador 7 | 4-4 | 1203 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-4 | 1204 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 4-5 | 1239 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-5 | 1240 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 4-6 | 1275 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-6 | 1276 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 4-7 | 1311 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-7 | 1312 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 5-1 | 1347 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-1 | 1348 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 5-2 | 1383 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-2 | 1384 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 5-3 | 1419 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-3 | 1420 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 5-4 | 1455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-4 | 1456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 5-5 | 1491 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-5 | 1492 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 5-6 | 1527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-6 | 1528 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 5-7 | 1563 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-7 | 1564 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 6-1 | 1599 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-1 | 1600 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 6-2 | 1635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-2 | 1636 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 6-3 | 1671 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-3 | 1672 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 6-4 | 1707 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-4 | 1708 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 7 | 6-5 | 1743 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 6-5 | 1744 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
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
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 6-3 | 2318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-3 | 2319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 6-4 | 2357 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-4 | 2358 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 6-5 | 2393 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-5 | 2394 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-4 | 572 | SLOWROLL_BUY_XP_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-3 | 1936 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-4 | 1982 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-5 | 2028 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-6 | 2088 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-6 | 2101 | ECON_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
