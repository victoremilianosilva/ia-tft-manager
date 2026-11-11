# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4312**
- Achados: **495**
- CRITICAL: 0 | HIGH: 10 | MEDIUM: 34 | LOW: 451

## Metadados da sessão

- Match ID: 13a20a8f-ccb5-4ba2-a7bf-145ee939104c
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **3455**
- Entradas posteriores à eliminação ignoradas: **857**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 122 | 6 | 5 | 0 | 46 | 2 | 1 | não/inconclusivo | 0 |
| Jogador 6 | 126 | 7 | 7 | 1 | 47 | 6 | 0 | não/inconclusivo | 0 |
| Jogador 7 | 295 | 7 | 9 | 0 | 71 | 6 | 0 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 45 | 19 | 5 | 1 | 12 | 33 | 0.1429 | 11 | 31 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 5, ALL_IN::ITEM: 2, ALL_IN::REROLL: 1, ALL_IN::SELL: 4, STABILIZE::BUY: 40, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 18, STABILIZE::PASS: 12, STABILIZE::SELL: 15
- Jogador 1 — recompensas por ação: BUY: média 0.3824 (n=45), BUY_XP: média -0.0180 (n=5), ITEM: média 0.1943 (n=7), MOVE_BENCH: média 0.1373 (n=15), MOVE_BOARD: média 0.0061 (n=18), PASS: média -0.0017 (n=12), REROLL: média -0.0700 (n=1), SELL: média -0.1647 (n=19)
| Jogador 2 | 124 | 50 | 19 | 9 | 1 | 6 | 32 | 0.1485 | 3 | 19 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::REROLL: 1, STABILIZE::BUY: 47, STABILIZE::BUY_XP: 9, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 18, STABILIZE::PASS: 6, STABILIZE::SELL: 19
- Jogador 2 — recompensas por ação: BUY: média 0.3912 (n=50), BUY_XP: média -0.0089 (n=9), ITEM: média 0.1886 (n=7), MOVE_BENCH: média 0.2364 (n=14), MOVE_BOARD: média -0.0172 (n=18), PASS: média -0.0117 (n=6), REROLL: média -0.0700 (n=1), SELL: média -0.2763 (n=19)
| Jogador 3 | 169 | 64 | 32 | 5 | 0 | 11 | 46 | 0.1230 | 4 | 34 |
- Jogador 3 — ações por estratégia: FAST8::BUY: 30, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 2, FAST8::SELL: 24, STABILIZE::BUY: 34, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 29, STABILIZE::MOVE_BOARD: 15, STABILIZE::PASS: 11, STABILIZE::SELL: 8
- Jogador 3 — recompensas por ação: BUY: média 0.3972 (n=64), BUY_XP: média -0.0220 (n=5), ITEM: média 0.1418 (n=11), MOVE_BENCH: média -0.0248 (n=31), MOVE_BOARD: média 0.0000 (n=15), PASS: média -0.0327 (n=11), SELL: média -0.1550 (n=32)
| Jogador 4 | 108 | 46 | 17 | 5 | 0 | 7 | 28 | 0.1951 | 8 | 6 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::MOVE_BOARD: 3, ALL_IN::SELL: 5, STABILIZE::BUY: 38, STABILIZE::BUY_XP: 5, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 12, STABILIZE::MOVE_BOARD: 13, STABILIZE::PASS: 7, STABILIZE::SELL: 12
- Jogador 4 — recompensas por ação: BUY: média 0.5430 (n=46), BUY_XP: média -0.0420 (n=5), ITEM: média 0.2180 (n=5), MOVE_BENCH: média 0.2958 (n=12), MOVE_BOARD: média 0.0056 (n=16), PASS: média 0.0000 (n=7), SELL: média -0.4959 (n=17)
| Jogador 5 | 122 | 58 | 30 | 6 | 0 | 6 | 15 | 0.1608 | 9 | 40 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::ITEM: 2, ALL_IN::SELL: 5, STABILIZE::BUY: 49, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 5, STABILIZE::PASS: 6, STABILIZE::SELL: 25
- Jogador 5 — recompensas por ação: BUY: média 0.4140 (n=58), BUY_XP: média -0.0333 (n=6), ITEM: média 0.1971 (n=7), MOVE_BENCH: média 0.3310 (n=10), MOVE_BOARD: média 0.0320 (n=5), PASS: média 0.0000 (n=6), SELL: média -0.3013 (n=30)
| Jogador 6 | 117 | 47 | 21 | 7 | 0 | 8 | 24 | 0.1242 | 5 | 39 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 2, ALL_IN::ITEM: 1, ALL_IN::SELL: 1, STABILIZE::BUY: 45, STABILIZE::BUY_XP: 7, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 6, STABILIZE::PASS: 8, STABILIZE::SELL: 20
- Jogador 6 — recompensas por ação: BUY: média 0.3987 (n=47), BUY_XP: média -0.0586 (n=7), ITEM: média 0.1570 (n=10), MOVE_BENCH: média 0.1139 (n=18), MOVE_BOARD: média -0.0283 (n=6), PASS: média -0.0163 (n=8), SELL: média -0.3391 (n=21)
| Jogador 7 | 174 | 71 | 38 | 9 | 0 | 7 | 35 | 0.1698 | 7 | 22 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 11, ALL_IN::ITEM: 1, ALL_IN::MOVE_BOARD: 1, ALL_IN::SELL: 7, FAST8::BUY: 1, FAST8::ITEM: 1, FAST8::MOVE_BOARD: 2, FAST8::SELL: 1, STABILIZE::BUY: 59, STABILIZE::BUY_XP: 9, STABILIZE::ITEM: 12, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 17, STABILIZE::PASS: 7, STABILIZE::SELL: 30
- Jogador 7 — recompensas por ação: BUY: média 0.4041 (n=71), BUY_XP: média 0.0300 (n=9), ITEM: média 0.1407 (n=14), MOVE_BENCH: média 0.3027 (n=15), MOVE_BOARD: média 0.0030 (n=20), PASS: média 0.0000 (n=7), SELL: média -0.1574 (n=38)
| Jogador 8 | 117 | 55 | 24 | 1 | 1 | 4 | 24 | 0.1830 | 4 | 25 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 2, STABILIZE::BUY: 48, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 9, STABILIZE::PASS: 4, STABILIZE::SELL: 22
- Jogador 8 — recompensas por ação: BUY: média 0.3616 (n=55), BUY_XP: média 0.0500 (n=1), ITEM: média 0.1537 (n=8), MOVE_BENCH: média 0.1660 (n=15), MOVE_BOARD: média -0.0300 (n=9), PASS: média 0.0000 (n=4), REROLL: média -0.0700 (n=1), SELL: média -0.0796 (n=24)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 12:37:39 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 12:37:40 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 12:37:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 12:37:46 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 12:37:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 12:37:47 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 12:37:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 12:37:48 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 12:37:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 12:37:51 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 12:37:54 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 12:37:54 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 12:37:54 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 12:37:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 12:37:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 12:38:01 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 12:38:02 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 12:38:03 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 12:38:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 12:38:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 12:38:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-1 | 12:38:19 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 12:38:20 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 12:38:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 12:38:21 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 12:38:22 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 12:38:22 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 12:38:23 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-1 | 12:38:24 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-1 | 12:38:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 12:38:31 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 1 | 2-2 | 12:38:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 12:38:33 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 1 | 2-2 | 12:38:34 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 12:38:35 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 2-2 | 12:38:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 12:38:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 12:38:41 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 12:38:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3600 |  |
| Jogador 1 | 2-3 | 12:38:43 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 2-3 | 12:38:44 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 12:38:44 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-3 | 12:38:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-4 | 12:38:53 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_18_Ornn | 1.0200 |  |
| Jogador 1 | 2-4 | 12:38:58 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Inferno | DA_18_Ornn | 0.3300 |  |
| Jogador 1 | 2-4 | 12:38:59 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Inferno | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-5 | 12:39:06 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-5 | 12:39:07 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 1 | 2-5 | 12:39:08 | MOVE Bench -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Inferno | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 1 | 2-5 | 12:39:08 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 2-5 | 12:39:09 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 12:39:10 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 1 | 2-5 | 12:39:11 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 12:39:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Inferno | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 1 | 2-6 | 12:39:25 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 1 | 2-6 | 12:39:26 | MOVE Bench -> Board: Kayle (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.7200 |  |
| Jogador 1 | 2-6 | 12:39:27 | MOVE Bench -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | -0.6900 |  |
| Jogador 1 | 2-6 | 12:39:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 12:39:29 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Inferno | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 1 | 2-7 | 12:39:37 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.7000 |  |
| Jogador 1 | 2-7 | 12:39:38 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 3-1 | 12:39:54 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 1 | 3-1 | 12:39:54 | MOVE Bench -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 1 | 3-1 | 12:39:56 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 1 | 3-1 | 12:39:57 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-1 | 12:39:58 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 12:39:59 | MOVE Bench -> Board: Kayle (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 3-1 | 12:39:59 | MOVE Board -> Board: Kayle (i:8.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 12:40:10 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 12:40:26 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 1 | 3-3 | 12:40:28 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | -0.2900 |  |
| Jogador 1 | 3-3 | 12:40:29 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-3 | 12:40:30 | MOVE Board -> Board: Akali (i:4.0) <-> Kayle (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 12:40:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Inferno | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-4 | 12:40:42 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 1 | 3-4 | 12:40:43 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-5 | 12:41:03 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Inferno | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 1 | 3-5 | 12:41:05 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Inferno | DA_18_Shen | 0.8200 |  |
| Jogador 1 | 3-5 | 12:41:06 | MOVE Board -> Board: Hecarim (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Inferno | DA_18_Shen | -0.0700 |  |
| Jogador 1 | 3-5 | 12:41:07 | MOVE Board -> Board: Xayah (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-5 | 12:41:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Inferno | DA_18_Shen | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-6 | 12:41:20 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Inferno | DA_18_Kayle | -0.5800 |  |
| Jogador 1 | 3-6 | 12:41:21 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Inferno | DA_18_Kayle | 0.2600 |  |
| Jogador 1 | 3-6 | 12:41:22 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Inferno | DA_18_Kayle | 0.0400 |  |
| Jogador 1 | 3-7 | 12:41:45 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_18_Kayle | 0.1900 |  |
| Jogador 1 | 3-7 | 12:41:46 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Inferno | DA_18_Kayle | 0.2000 |  |
| Jogador 1 | 3-7 | 12:41:47 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Inferno | DA_18_Kayle | -0.0100 |  |
| Jogador 1 | 3-7 | 12:41:49 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Inferno | DA_18_Kayle | 0.0200 |  |
| Jogador 1 | 3-7 | 12:41:50 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Inferno | DA_18_Kayle | 0.0300 |  |
| Jogador 1 | 4-1 | 12:42:03 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Inferno | DA_18_Kayle | 0.0800 |  |
| Jogador 1 | 4-1 | 12:42:04 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Inferno | DA_18_Kayle | -0.0100 |  |
| Jogador 1 | 4-1 | 12:42:06 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Inferno | DA_18_Kayle | 0.0200 |  |
| Jogador 1 | 4-2 | 12:42:29 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Inferno | DA_18_Kayle | -0.0300 |  |
| Jogador 1 | 4-2 | 12:42:30 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Inferno | DA_18_Kayle | 0.9600 |  |
| Jogador 1 | 4-2 | 12:42:31 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Inferno | DA_18_Kayle | 0.0100 |  |
| Jogador 1 | 4-2 | 12:42:33 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Inferno | DA_18_Kayle | -0.2600 |  |
| Jogador 1 | 4-2 | 12:42:34 | MOVE Board -> Board: Grompe (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Inferno | DA_18_Kayle | 0.0000 |  |
| Jogador 1 | 4-3 | 12:42:48 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Inferno | DA_18_Kayle | -0.6000 |  |
| Jogador 1 | 4-3 | 12:42:49 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Inferno | DA_18_Kayle | 0.0900 |  |
| Jogador 1 | 4-3 | 12:42:51 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Inferno | DA_18_Kayle | -0.0300 |  |
| Jogador 1 | 4-4 | 12:43:16 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Inferno | DA_18_Kayle | 0.3300 |  |
| Jogador 1 | 4-4 | 12:43:18 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Inferno | DA_18_Kayle | -0.0300 |  |
| Jogador 1 | 4-4 | 12:43:19 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Inferno | DA_18_Kayle | -0.1300 |  |
| Jogador 1 | 4-4 | 12:43:20 | MOVE Board -> Board: Xayah (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Inferno | DA_18_Kayle | 0.0100 |  |
| Jogador 1 | 4-4 | 12:43:21 | MOVE Board -> Board: Hecarim (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Inferno | DA_18_Kayle | -0.0200 |  |
| Jogador 1 | 4-5 | 12:43:39 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Inferno | DA_18_Kayle | 0.0200 |  |
| Jogador 1 | 4-5 | 12:43:41 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Inferno | DA_18_Kayle | 0.8600 |  |
| Jogador 1 | 4-5 | 12:43:43 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Inferno | DA_18_Kayle | -0.0200 |  |
| Jogador 1 | 4-6 | 12:44:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Adaptador | DA_18_Kayle | 0.0400 |  |
| Jogador 1 | 4-6 | 12:44:21 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Adaptador | DA_18_Kayle | -0.0500 |  |
| Jogador 1 | 4-6 | 12:44:22 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Adaptador | DA_18_Kayle | -0.1600 |  |
| Jogador 1 | 4-6 | 12:44:24 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 100 | 5 | Adaptador | DA_18_Kayle | -0.0700 |  |
| Jogador 1 | 4-6 | 12:44:25 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Adaptador | DA_18_Kayle | 0.0000 |  |
| Jogador 1 | 4-7 | 12:44:41 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Adaptador | DA_18_Kayle | 0.9200 |  |
| Jogador 1 | 4-7 | 12:44:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Adaptador | DA_18_Kayle | 0.1700 |  |
| Jogador 1 | 4-7 | 12:44:44 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Adaptador | DA_18_Kayle | 0.1800 |  |
| Jogador 1 | 5-1 | 12:45:16 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Adaptador | DA_18_Kayle | -0.0200 |  |
| Jogador 1 | 5-1 | 12:45:17 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Adaptador | DA_18_Kayle | 0.5500 |  |
| Jogador 1 | 5-1 | 12:45:19 | VENDEU: Caitlyn (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Adaptador | DA_18_Kayle | -0.5400 |  |
| Jogador 1 | 5-1 | 12:45:20 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Adaptador | DA_18_Kayle | 0.2800 |  |
| Jogador 2 | ? | 12:37:39 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 12:37:40 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 12:37:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:37:46 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 12:37:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 12:37:47 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 12:37:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 12:37:51 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 12:37:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 12:37:54 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 12:37:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 12:37:59 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 12:38:01 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 12:38:02 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 12:38:03 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 12:38:03 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 12:38:04 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 12:38:04 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 12:38:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 12:38:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 12:38:12 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 1-4 | 12:38:13 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 12:38:13 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 12:38:14 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 2-1 | 12:38:19 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 12:38:20 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 12:38:21 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 12:38:21 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-1 | 12:38:22 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 2-1 | 12:38:22 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 12:38:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 12:38:24 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-1 | 12:38:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 12:38:31 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 12:38:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 12:38:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 12:38:37 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-3 | 12:38:41 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.9700 |  |
| Jogador 2 | 2-3 | 12:38:42 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 2-3 | 12:38:43 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 12:38:44 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-3 | 12:38:44 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-3 | 12:38:45 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-3 | 12:38:46 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-3 | 12:38:47 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 2-4 | 12:38:53 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 2-4 | 12:38:58 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 2-4 | 12:38:59 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-5 | 12:39:06 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-5 | 12:39:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 12:39:08 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-5 | 12:39:08 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.1200 |  |
| Jogador 2 | 2-5 | 12:39:09 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-5 | 12:39:10 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 2-5 | 12:39:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-6 | 12:39:24 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.5500 |  |
| Jogador 2 | 2-6 | 12:39:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-6 | 12:39:26 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | 0.5900 |  |
| Jogador 2 | 2-6 | 12:39:27 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 2-6 | 12:39:28 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 12:39:29 | MOVE Board -> Board: Veigar (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 12:39:37 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-7 | 12:39:38 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 3-1 | 12:39:54 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | 0.7600 |  |
| Jogador 2 | 3-1 | 12:39:54 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 3-1 | 12:39:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 12:39:57 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 12:39:58 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-1 | 12:39:59 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-1 | 12:39:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 12:40:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-3 | 12:40:26 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 3-3 | 12:40:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 12:40:29 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-3 | 12:40:30 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-3 | 12:40:31 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-3 | 12:40:32 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 3-4 | 12:40:42 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | 0.7600 |  |
| Jogador 2 | 3-4 | 12:40:43 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | 0.5400 |  |
| Jogador 2 | 3-5 | 12:41:03 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 3-5 | 12:41:05 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 3-5 | 12:41:06 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Veigar | -0.4600 |  |
| Jogador 2 | 3-5 | 12:41:07 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 3-5 | 12:41:08 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 3-6 | 12:41:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Tristana | 0.8500 |  |
| Jogador 2 | 3-6 | 12:41:21 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Tristana | 0.8400 |  |
| Jogador 2 | 3-6 | 12:41:22 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Tristana | 0.3200 |  |
| Jogador 2 | 3-7 | 12:41:45 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Tristana | 0.8400 |  |
| Jogador 2 | 3-7 | 12:41:46 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Tristana | 0.1400 |  |
| Jogador 2 | 3-7 | 12:41:47 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Tristana | 0.2100 |  |
| Jogador 2 | 3-7 | 12:41:49 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Tristana | 0.1100 |  |
| Jogador 2 | 3-7 | 12:41:50 | MOVE Bench -> Board: Tristana (i:12.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Tristana | 0.1000 |  |
| Jogador 2 | 4-1 | 12:42:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Feérico | DA_18_Tristana | 0.8700 |  |
| Jogador 2 | 4-1 | 12:42:04 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Feérico | DA_18_Tristana | -0.4000 |  |
| Jogador 2 | 4-1 | 12:42:06 | MOVE Bench -> Board: Tristana (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 27 | 2 | Feérico | DA_18_Tristana | 0.3300 |  |
| Jogador 2 | 4-2 | 12:42:29 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 35 | 2 | Feérico | DA_18_Tristana | 0.4000 |  |
| Jogador 2 | 4-2 | 12:42:30 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-2 | 12:42:31 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Feérico | DA_18_Tristana | -0.3700 |  |
| Jogador 2 | 4-2 | 12:42:33 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-2 | 12:42:34 | MOVE Board -> Board: Veigar (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 29 | 2 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-3 | 12:42:48 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 35 | 3 | Feérico | DA_18_Tristana | 0.8100 |  |
| Jogador 2 | 4-3 | 12:42:49 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 34 | 3 | Feérico | DA_18_Tristana | 0.1200 |  |
| Jogador 2 | 4-3 | 12:42:51 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 34 | 3 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-4 | 12:43:16 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Feérico | DA_18_Tristana | 0.2000 |  |
| Jogador 2 | 4-4 | 12:43:18 | MOVE Board -> Board: Tristana (i:12.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-4 | 12:43:19 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Feérico | DA_18_Tristana | -0.0500 |  |
| Jogador 2 | 4-4 | 12:43:20 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 39 | 3 | Feérico | DA_18_Tristana | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-5 | 12:43:39 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 58 | 4 | Feérico | DA_18_Tristana | -0.1000 |  |
| Jogador 2 | 4-5 | 12:43:41 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Tristana | 0.3900 |  |
| Jogador 2 | 4-5 | 12:43:43 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Feérico | DA_18_Tristana | -0.5900 |  |
| Jogador 2 | 4-6 | 12:44:19 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Feérico | DA_18_Tristana | 0.5000 |  |
| Jogador 2 | 4-6 | 12:44:21 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 2 | 4-6 | 12:44:22 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Feérico | DA_18_Tristana | 0.0300 |  |
| Jogador 2 | 4-6 | 12:44:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 4-6 | 12:44:25 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 2 | 4-7 | 12:44:41 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Feérico | DA_18_Tristana | 0.1400 |  |
| Jogador 2 | 4-7 | 12:44:43 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Feérico | DA_18_Tristana | 0.1700 |  |
| Jogador 2 | 4-7 | 12:44:44 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 5-1 | 12:45:16 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 90 | 5 | Feérico | DA_18_Tristana | 0.7400 |  |
| Jogador 2 | 5-1 | 12:45:17 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 2 | 5-1 | 12:45:19 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Feérico | DA_18_Tristana | 0.1000 |  |
| Jogador 2 | 5-1 | 12:45:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Feérico | DA_18_Tristana | -0.0700 |  |
| Jogador 3 | ? | 12:37:39 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 12:37:40 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 12:37:41 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 12:37:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:37:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 12:37:46 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 12:37:47 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 12:37:48 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 12:37:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 12:37:51 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 12:37:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 12:37:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 12:37:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 12:37:55 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 12:37:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 12:37:59 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 12:38:01 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 12:38:02 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 12:38:03 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 12:38:03 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 12:38:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 12:38:10 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 12:38:12 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 12:38:13 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 12:38:13 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 12:38:14 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-1 | 12:38:19 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 12:38:20 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 12:38:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 12:38:31 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 12:38:32 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 12:38:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 12:38:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 12:38:41 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 12:38:42 | MOVE Bench -> Board: Camille (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.3900 |  |
| Jogador 3 | 2-3 | 12:38:43 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-3 | 12:38:44 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-3 | 12:38:44 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 2-3 | 12:38:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-3 | 12:38:46 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 12:38:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 12:38:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 12:38:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 12:38:59 | MOVE Bench -> Board: Camille (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.3900 |  |
| Jogador 3 | 2-5 | 12:39:06 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 2-5 | 12:39:07 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.8700 |  |
| Jogador 3 | 2-5 | 12:39:08 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-5 | 12:39:08 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 12:39:09 | MOVE Bench -> Board: Yorick (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.1100 |  |
| Jogador 3 | 2-5 | 12:39:10 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.0600 |  |
| Jogador 3 | 2-5 | 12:39:11 | MOVE Bench -> Board: Camille (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | -0.7400 |  |
| Jogador 3 | 2-6 | 12:39:24 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Colosso | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 12:39:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-6 | 12:39:26 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 2-6 | 12:39:27 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 12:39:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-6 | 12:39:29 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 2-7 | 12:39:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 2-7 | 12:39:38 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.6100 |  |
| Jogador 3 | 3-1 | 12:39:54 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 3-1 | 12:39:54 | MOVE Bench -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Akali_AD | -0.6500 |  |
| Jogador 3 | 3-1 | 12:39:56 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Akali_AD | 0.6300 |  |
| Jogador 3 | 3-1 | 12:39:57 | MOVE Board -> Board: Diana (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-1 | 12:39:58 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-1 | 12:39:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Akali_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 12:40:10 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Akali_AD | -0.2300 |  |
| Jogador 3 | 3-3 | 12:40:26 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | 3-3 | 12:40:28 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 12:40:29 | MOVE Board -> Board: Diana (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-3 | 12:40:30 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-3 | 12:40:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-4 | 12:40:42 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Colosso | DA_18_Akali_AD | -0.4200 |  |
| Jogador 3 | 3-4 | 12:40:43 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 3-5 | 12:41:03 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 3-5 | 12:41:05 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Colosso | DA_18_Akali_AD | 0.8600 |  |
| Jogador 3 | 3-5 | 12:41:06 | MOVE Bench -> Board: Vi (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-5 | 12:41:07 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 12:41:08 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_18_Akali_AD | 0.3900 |  |
| Jogador 3 | 3-6 | 12:41:20 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Colosso | DA_18_Akali_AD | -0.4500 |  |
| Jogador 3 | 3-6 | 12:41:21 | MOVE Bench -> Board: Vi (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Colosso | DA_18_Akali_AD | -0.5700 |  |
| Jogador 3 | 3-6 | 12:41:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Colosso | DA_18_Akali_AD | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-7 | 12:41:45 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Colosso | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 3-7 | 12:41:46 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Colosso | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 3-7 | 12:41:47 | MOVE Bench -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-7 | 12:41:49 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Colosso | DA_18_Akali_AD | -0.7700 |  |
| Jogador 3 | 3-7 | 12:41:50 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Colosso | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 4-1 | 12:42:03 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Colosso | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 4-1 | 12:42:04 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Kha'Zix (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 4-1 | 12:42:06 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Kha'Zix (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Colosso | DA_18_Akali_AD | 0.0400 |  |
| Jogador 3 | 4-2 | 12:42:29 | MOVE Bench -> Board: Grompe (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Colosso | DA_18_Akali_AD | -0.9700 |  |
| Jogador 3 | 4-2 | 12:42:30 | MOVE Bench -> Board: Diana (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Colosso | DA_18_Akali_AD | -0.3700 |  |
| Jogador 3 | 4-2 | 12:42:31 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Colosso | DA_18_Akali_AD | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-3 | 12:42:48 | MOVE Bench -> Board: Vi (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Colosso | DA_18_Akali_AD | -0.1300 |  |
| Jogador 3 | 4-3 | 12:42:49 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-3 | 12:42:51 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 108 | 5 | Colosso | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 4-4 | 12:43:16 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 122 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-4 | 12:43:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Colosso | DA_18_Akali_AD | 0.3600 |  |
| Jogador 3 | 4-4 | 12:43:19 | MOVE Bench -> Board: Grompe (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 4-4 | 12:43:20 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Colosso | DA_18_Akali_AD | -0.7600 |  |
| Jogador 3 | 4-4 | 12:43:21 | MOVE Bench -> Board: Vi (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Colosso | DA_18_Akali_AD | -0.3400 |  |
| Jogador 3 | 4-5 | 12:43:39 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 136 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-5 | 12:43:41 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 134 | 5 | Colosso | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 4-5 | 12:43:43 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 132 | 5 | Colosso | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 4-6 | 12:44:19 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 143 | 5 | Colosso | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 4-6 | 12:44:21 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 141 | 5 | Colosso | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 4-6 | 12:44:22 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 141 | 5 | Colosso | DA_18_Akali_AD | 0.3700 |  |
| Jogador 3 | 4-6 | 12:44:24 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 139 | 5 | Colosso | DA_18_Akali_AD | 0.0600 |  |
| Jogador 3 | 4-6 | 12:44:25 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 139 | 5 | Colosso | DA_18_Akali_AD | 0.5600 |  |
| Jogador 3 | 4-7 | 12:44:41 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 150 | 5 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 4-7 | 12:44:43 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 149 | 5 | Colosso | DA_18_Akali_AD | -0.0800 |  |
| Jogador 3 | 4-7 | 12:44:44 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Aronguejo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 149 | 5 | Colosso | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 5-1 | 12:45:16 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 163 | 5 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 5-1 | 12:45:17 | VENDEU: Grompe (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Colosso | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 5-1 | 12:45:19 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Colosso | DA_18_Akali_AD | 0.8600 |  |
| Jogador 3 | 5-1 | 12:45:20 | VENDEU: Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 5-2 | 12:45:37 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 5-2 | 12:45:38 | VENDEU: Vi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 187 | 5 | Colosso | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 5-2 | 12:45:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 184 | 5 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 5-2 | 12:45:41 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 186 | 5 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 5-3 | 12:46:13 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 197 | 5 | Colosso | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 5-3 | 12:46:14 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 195 | 5 | Colosso | DA_18_Akali_AD | 0.3700 |  |
| Jogador 3 | 5-3 | 12:46:16 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 198 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-3 | 12:46:17 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 196 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 5-4 | 12:46:35 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 211 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 5-4 | 12:46:37 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 208 | 5 | Colosso | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 3 | 5-4 | 12:46:39 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 205 | 5 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 3 | 5-4 | 12:46:40 | COMPROU: Lux (Espinhos Negros) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 200 | 5 | Colosso | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 3 | 5-5 | 12:47:15 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 222 | 5 | Colosso | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 5-5 | 12:47:17 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 219 | 5 | Colosso | DA_Scuttlecrab18 | 0.3000 |  |
| Jogador 3 | 5-5 | 12:47:18 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 222 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-5 | 12:47:20 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 219 | 5 | Colosso | DA_Scuttlecrab18 | -0.1100 |  |
| Jogador 3 | 5-6 | 12:47:37 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 236 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 5-6 | 12:47:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 235 | 5 | Colosso | DA_Scuttlecrab18 | 0.8700 |  |
| Jogador 3 | 5-6 | 12:47:41 | VENDEU: Lux (Espinhos Negros) (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 240 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 5-6 | 12:47:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 237 | 5 | Colosso | DA_Scuttlecrab18 | 0.8200 |  |
| Jogador 3 | 5-7 | 12:48:15 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Kha'Zix (i:6.0) (tabuleiro slot 25) | FAST8 | FAST8: composição planejada exige nível 8 | 250 | 5 | Colosso | DA_Scuttlecrab18 | 0.0100 |  |
| Jogador 3 | 5-7 | 12:48:17 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 253 | 5 | Colosso | DA_Scuttlecrab18 | -0.0100 |  |
| Jogador 3 | 5-7 | 12:48:18 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 250 | 5 | Colosso | DA_Scuttlecrab18 | 0.1900 |  |
| Jogador 3 | 5-7 | 12:48:20 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 252 | 5 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 6-1 | 12:48:39 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 264 | 5 | Colosso | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 6-1 | 12:48:40 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 267 | 5 | Colosso | DA_Scuttlecrab18 | -0.5300 |  |
| Jogador 3 | 6-1 | 12:48:42 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 264 | 5 | Colosso | DA_Scuttlecrab18 | -0.2000 |  |
| Jogador 3 | 6-1 | 12:48:43 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 267 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-2 | 12:49:19 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 279 | 5 | Colosso | DA_Scuttlecrab18 | 1.0100 |  |
| Jogador 3 | 6-2 | 12:49:21 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 277 | 5 | Colosso | DA_Scuttlecrab18 | -0.0200 |  |
| Jogador 3 | 6-2 | 12:49:22 | VENDEU: Sejuani (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 282 | 5 | Colosso | DA_Scuttlecrab18 | -0.5900 |  |
| Jogador 3 | 6-2 | 12:49:24 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 282 | 5 | Colosso | DA_Scuttlecrab18 | 0.4200 |  |
| Jogador 3 | 6-3 | 12:49:43 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 294 | 5 | Colosso | DA_Scuttlecrab18 | 0.8500 |  |
| Jogador 3 | 6-3 | 12:49:45 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 290 | 5 | Colosso | DA_Scuttlecrab18 | 0.1400 |  |
| Jogador 3 | 6-3 | 12:49:47 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 292 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 6-3 | 12:49:48 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 289 | 5 | Colosso | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 6-4 | 12:50:23 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 305 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-4 | 12:50:25 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 302 | 5 | Colosso | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 6-4 | 12:50:26 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 305 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 6-4 | 12:50:28 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 303 | 5 | Colosso | DA_Scuttlecrab18 | 0.0400 |  |
| Jogador 3 | 6-5 | 12:50:47 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 315 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 6-5 | 12:50:48 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 311 | 5 | Colosso | DA_Scuttlecrab18 | 0.1800 |  |
| Jogador 3 | 6-5 | 12:50:50 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 314 | 5 | Colosso | DA_Scuttlecrab18 | -0.0500 |  |
| Jogador 3 | 6-5 | 12:50:52 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 313 | 5 | Colosso | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 6-6 | 12:51:30 | VENDEU: Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 325 | 5 | Colosso | DA_Scuttlecrab18 | -0.0300 |  |
| Jogador 3 | 6-6 | 12:51:31 | COMPROU: Aphelios (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 321 | 5 | Colosso | DA_Scuttlecrab18 | 0.0800 |  |
| Jogador 3 | 6-6 | 12:51:33 | VENDEU: Aphelios (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 325 | 5 | Colosso | DA_Scuttlecrab18 | -0.0400 |  |
| Jogador 3 | 6-6 | 12:51:35 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 322 | 5 | Colosso | DA_Scuttlecrab18 | -0.1000 |  |
| Jogador 3 | 6-7 | 12:51:55 | EQUIP_FROM_INVENTORY: TFT_Item_Deathblade -> Kha'Zix (i:6.0) (tabuleiro slot 25) | FAST8 | FAST8: composição planejada exige nível 8 | 333 | 5 | Colosso | DA_Scuttlecrab18 | 0.0300 |  |
| Jogador 3 | 6-7 | 12:51:56 | VENDEU: Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 336 | 5 | Colosso | DA_Scuttlecrab18 | 0.0000 |  |
| Jogador 3 | 6-7 | 12:51:58 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 335 | 5 | Colosso | DA_Scuttlecrab18 | 0.4300 |  |
| Jogador 3 | 6-7 | 12:51:59 | VENDEU: Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 339 | 5 | Colosso | DA_Scuttlecrab18 | -0.0600 |  |
| Jogador 4 | ? | 12:37:39 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 12:37:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 12:37:41 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 12:37:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:37:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 12:37:46 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:37:47 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 12:37:48 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 12:37:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 12:37:51 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4700 |  |
| Jogador 4 | 1-2 | 12:37:54 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 12:37:54 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 12:37:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 12:37:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 12:37:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 12:38:01 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 12:38:02 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 12:38:03 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 12:38:10 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 12:38:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 12:38:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-1 | 12:38:19 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 12:38:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 12:38:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 12:38:31 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 12:38:32 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 12:38:33 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 12:38:34 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 12:38:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 12:38:35 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 12:38:36 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 12:38:37 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 4 | 2-3 | 12:38:41 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 12:38:42 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 12:38:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 12:38:44 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 12:38:44 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | -0.5700 |  |
| Jogador 4 | 2-3 | 12:38:45 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 12:38:46 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 12:38:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-4 | 12:38:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 4 | 2-4 | 12:38:58 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 12:38:59 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 4 | 2-5 | 12:39:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Florescer | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 4 | 2-5 | 12:39:07 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_KogMaw18_AD | -0.5700 |  |
| Jogador 4 | 2-5 | 12:39:08 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Florescer | DA_18_Rakan | -0.6300 |  |
| Jogador 4 | 2-5 | 12:39:08 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Florescer | DA_CrimsonRaptor18 | 0.1900 |  |
| Jogador 4 | 2-5 | 12:39:09 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Florescer | DA_18_Rakan | -0.1300 |  |
| Jogador 4 | 2-5 | 12:39:10 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Florescer | DA_18_Rakan | -1.0200 |  |
| Jogador 4 | 2-5 | 12:39:11 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Florescer | DA_18_Rakan | 0.3200 |  |
| Jogador 4 | 2-6 | 12:39:24 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Florescer | DA_18_Rakan | 1.0500 |  |
| Jogador 4 | 2-6 | 12:39:25 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_18_Akali_AD | 1.1200 |  |
| Jogador 4 | 2-6 | 12:39:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Florescer | DA_18_Akali_AD | -0.0900 |  |
| Jogador 4 | 2-6 | 12:39:27 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Florescer | DA_18_Akali_AD | 0.2400 |  |
| Jogador 4 | 2-6 | 12:39:28 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_18_Akali_AD | 0.3900 |  |
| Jogador 4 | 2-6 | 12:39:29 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Florescer | DA_18_Akali_AD | 0.4000 |  |
| Jogador 4 | 2-7 | 12:39:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Florescer | DA_18_Akali_AD | 0.8700 |  |
| Jogador 4 | 2-7 | 12:39:38 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Florescer | DA_18_Akali_AD | 0.3400 |  |
| Jogador 4 | 3-1 | 12:39:54 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Florescer | DA_18_Akali_AD | 0.8700 |  |
| Jogador 4 | 3-1 | 12:39:54 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Florescer | DA_18_Akali_AD | 0.2400 |  |
| Jogador 4 | 3-1 | 12:39:56 | MOVE Bench -> Board: Akali (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Florescer | DA_18_Akali_AD | -0.3700 |  |
| Jogador 4 | 3-1 | 12:39:57 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Florescer | DA_18_Akali_AD | 0.2800 |  |
| Jogador 4 | 3-1 | 12:39:58 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Florescer | DA_18_Akali_AD | 0.3200 |  |
| Jogador 4 | 3-1 | 12:39:59 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Florescer | DA_18_Akali_AD | 0.6000 |  |
| Jogador 4 | 3-1 | 12:39:59 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Florescer | DA_18_Akali_AD | 0.0700 |  |
| Jogador 4 | 3-2 | 12:40:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Florescer | DA_18_Akali_AD | 0.3400 |  |
| Jogador 4 | 3-3 | 12:40:26 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Florescer | DA_18_Akali_AD | 0.8700 |  |
| Jogador 4 | 3-3 | 12:40:28 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Florescer | DA_18_Akali_AD | 0.7700 |  |
| Jogador 4 | 3-3 | 12:40:29 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 12:40:30 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Florescer | DA_18_Akali_AD | 0.3100 |  |
| Jogador 4 | 3-3 | 12:40:31 | MOVE Board -> Board: Rakan (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 12:40:32 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Florescer | DA_18_Akali_AD | -0.0200 |  |
| Jogador 4 | 3-4 | 12:40:42 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Florescer | DA_18_Akali_AD | 0.8400 |  |
| Jogador 4 | 3-4 | 12:40:43 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Florescer | DA_18_Akali_AD | -0.2600 |  |
| Jogador 4 | 3-5 | 12:41:03 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Florescer | DA_18_Akali_AD | 0.8300 |  |
| Jogador 4 | 3-5 | 12:41:05 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 12:41:06 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Florescer | DA_18_Akali_AD | 0.9100 |  |
| Jogador 4 | 3-5 | 12:41:07 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 12:41:08 | MOVE Board -> Board: Rakan (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Florescer | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 3-6 | 12:41:20 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Florescer | DA_18_Akali_AD | 0.9100 |  |
| Jogador 4 | 3-6 | 12:41:21 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Florescer | DA_18_Akali_AD | 0.5900 |  |
| Jogador 4 | 3-6 | 12:41:22 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Florescer | DA_18_Akali_AD | 0.0400 |  |
| Jogador 4 | 3-7 | 12:41:45 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Florescer | DA_18_Akali_AD | 0.2100 |  |
| Jogador 4 | 3-7 | 12:41:46 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Florescer | DA_18_Akali_AD | 0.2400 |  |
| Jogador 4 | 3-7 | 12:41:47 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Florescer | DA_18_Akali_AD | 0.4000 |  |
| Jogador 4 | 3-7 | 12:41:49 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Florescer | DA_18_Akali_AD | 0.6200 |  |
| Jogador 4 | 3-7 | 12:41:50 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 4-1 | 12:42:03 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Florescer | DA_18_Akali_AD | -0.6000 |  |
| Jogador 4 | 4-1 | 12:42:04 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Florescer | DA_18_Akali_AD | 0.3600 |  |
| Jogador 4 | 4-1 | 12:42:06 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Florescer | DA_18_Akali_AD | 0.0100 |  |
| Jogador 4 | 4-2 | 12:42:29 | VENDEU: Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Florescer | DA_18_Akali_AD | -0.7100 |  |
| Jogador 4 | 4-2 | 12:42:30 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Florescer | DA_18_Akali_AD | 0.9300 |  |
| Jogador 4 | 4-2 | 12:42:31 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 4-2 | 12:42:33 | VENDEU: Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 96 | 5 | Florescer | DA_18_Akali_AD | -0.7000 |  |
| Jogador 4 | 4-2 | 12:42:34 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Florescer | DA_18_Akali_AD | 0.4100 |  |
| Jogador 4 | 4-3 | 12:42:48 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Florescer | DA_18_Akali_AD | -0.6100 |  |
| Jogador 4 | 4-3 | 12:42:49 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Florescer | DA_18_Akali_AD | 1.0400 |  |
| Jogador 4 | 4-3 | 12:42:51 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Florescer | DA_18_Akali_AD | 1.0400 |  |
| Jogador 4 | 4-4 | 12:43:16 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Florescer | DA_18_Akali_AD | 0.4700 |  |
| Jogador 4 | 4-4 | 12:43:18 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Florescer | DA_18_Akali_AD | 0.0600 |  |
| Jogador 4 | 4-4 | 12:43:19 | MOVE Board -> Board: Akali (i:4.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 12:43:20 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Florescer | DA_18_Akali_AD | -0.2600 |  |
| Jogador 4 | 4-4 | 12:43:21 | MOVE Board -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Florescer | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 4-5 | 12:43:39 | VENDEU: Warwick (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Florescer | DA_18_Akali_AD | -0.7400 |  |
| Jogador 4 | 4-5 | 12:43:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Florescer | DA_18_Akali_AD | 0.9300 |  |
| Jogador 4 | 4-5 | 12:43:43 | VENDEU: Yunara (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Florescer | DA_18_Akali_AD | -0.7400 |  |
| Jogador 5 | ? | 12:37:39 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 12:37:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 12:37:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:37:46 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 12:37:46 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 12:37:47 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 12:37:48 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 12:37:48 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 12:37:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 12:37:51 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 12:37:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 12:37:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 12:38:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 12:38:02 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 12:38:03 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 12:38:10 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 12:38:12 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 12:38:13 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 12:38:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 12:38:19 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 12:38:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 12:38:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 12:38:31 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 12:38:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 12:38:33 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 12:38:34 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 12:38:35 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 12:38:35 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 12:38:36 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 12:38:37 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-3 | 12:38:41 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 12:38:42 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 12:38:43 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 12:38:44 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 12:38:44 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 12:38:45 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.1700 |  |
| Jogador 5 | 2-3 | 12:38:46 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0800 |  |
| Jogador 5 | 2-3 | 12:38:47 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-4 | 12:38:53 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 2-4 | 12:38:58 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 12:38:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-5 | 12:39:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2500 |  |
| Jogador 5 | 2-5 | 12:39:07 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4200 |  |
| Jogador 5 | 2-5 | 12:39:08 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-5 | 12:39:08 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-5 | 12:39:09 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.2800 |  |
| Jogador 5 | 2-5 | 12:39:10 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.4100 |  |
| Jogador 5 | 2-5 | 12:39:11 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0800 |  |
| Jogador 5 | 2-6 | 12:39:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Cassiopeia | 1.0500 |  |
| Jogador 5 | 2-6 | 12:39:25 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-6 | 12:39:26 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Cassiopeia | -0.6300 |  |
| Jogador 5 | 2-6 | 12:39:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.0400 |  |
| Jogador 5 | 2-6 | 12:39:28 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.4400 |  |
| Jogador 5 | 2-6 | 12:39:29 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_18_Cassiopeia | -0.0500 |  |
| Jogador 5 | 2-7 | 12:39:37 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.5600 |  |
| Jogador 5 | 2-7 | 12:39:38 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 3-1 | 12:39:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_18_Yunara | 0.7500 |  |
| Jogador 5 | 3-1 | 12:39:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Yunara | 0.1900 |  |
| Jogador 5 | 3-1 | 12:39:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Yunara | 0.0300 |  |
| Jogador 5 | 3-1 | 12:39:57 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Yunara | 0.1600 |  |
| Jogador 5 | 3-1 | 12:39:58 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Vivaz | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 3-1 | 12:39:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Vivaz | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 3-1 | 12:39:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Vivaz | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 3-2 | 12:40:10 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Vivaz | DA_KogMaw18_AD | 0.7300 |  |
| Jogador 5 | 3-3 | 12:40:26 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Vivaz | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 5 | 3-3 | 12:40:28 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Vivaz | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 5 | 3-3 | 12:40:29 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Vivaz | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 5 | 3-3 | 12:40:30 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Vivaz | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 3-3 | 12:40:31 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Vivaz | DA_KogMaw18_AD | -0.3700 |  |
| Jogador 5 | 3-3 | 12:40:32 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Vivaz | DA_KogMaw18_AD | -0.4400 |  |
| Jogador 5 | 3-4 | 12:40:42 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Vivaz | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 5 | 3-4 | 12:40:43 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Vivaz | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 3-5 | 12:41:03 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Vivaz | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 5 | 3-5 | 12:41:05 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Vivaz | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 5 | 3-5 | 12:41:06 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Vivaz | DA_KogMaw18_AD | -0.5500 |  |
| Jogador 5 | 3-5 | 12:41:07 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Vivaz | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 5 | 3-5 | 12:41:08 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Vivaz | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 5 | 3-6 | 12:41:20 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Vivaz | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 5 | 3-6 | 12:41:21 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Vivaz | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 5 | 3-6 | 12:41:22 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Vivaz | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 5 | 3-7 | 12:41:45 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Vivaz | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 5 | 3-7 | 12:41:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Vivaz | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 5 | 3-7 | 12:41:47 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Vivaz | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 5 | 3-7 | 12:41:49 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Vivaz | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 5 | 3-7 | 12:41:50 | MOVE Bench -> Board: Teemo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Vivaz | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 5 | 4-1 | 12:42:03 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Vivaz | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 4-1 | 12:42:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Vivaz | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 5 | 4-1 | 12:42:06 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Vivaz | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 4-2 | 12:42:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Vivaz | DA_KogMaw18_AD | 0.9000 |  |
| Jogador 5 | 4-2 | 12:42:30 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Vivaz | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 5 | 4-2 | 12:42:31 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Vivaz | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 5 | 4-2 | 12:42:33 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Vivaz | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 5 | 4-2 | 12:42:34 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Vivaz | DA_KogMaw18_AD | -0.6400 |  |
| Jogador 5 | 4-3 | 12:42:48 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Vivaz | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 5 | 4-3 | 12:42:49 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Vivaz | DA_KogMaw18_AD | 0.4200 |  |
| Jogador 5 | 4-3 | 12:42:51 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Vivaz | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 5 | 4-4 | 12:43:16 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 94 | 5 | Vivaz | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 5 | 4-4 | 12:43:18 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 94 | 5 | Vivaz | DA_KogMaw18_AD | 0.5700 |  |
| Jogador 5 | 4-4 | 12:43:19 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Vivaz | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 5 | 4-4 | 12:43:20 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 93 | 5 | Vivaz | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 4-4 | 12:43:21 | VENDEU: Kobuko (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Vivaz | DA_KogMaw18_AD | -0.6400 |  |
| Jogador 5 | 4-5 | 12:43:39 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Vivaz | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 5 | 4-5 | 12:43:41 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Vivaz | DA_KogMaw18_AD | 0.3700 |  |
| Jogador 5 | 4-5 | 12:43:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Vivaz | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 4-6 | 12:44:19 | VENDEU: Teemo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Vivaz | DA_KogMaw18_AD | -0.7000 |  |
| Jogador 5 | 4-6 | 12:44:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Vivaz | DA_KogMaw18_AD | 0.4900 |  |
| Jogador 5 | 4-6 | 12:44:22 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Vivaz | DA_KogMaw18_AD | -0.6000 |  |
| Jogador 5 | 4-6 | 12:44:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Vivaz | DA_KogMaw18_AD | 1.0300 |  |
| Jogador 5 | 4-6 | 12:44:25 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Vivaz | DA_KogMaw18_AD | -0.2300 |  |
| Jogador 5 | 4-7 | 12:44:41 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Vivaz | DA_KogMaw18_AD | 0.9800 |  |
| Jogador 5 | 4-7 | 12:44:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Vivaz | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 5 | 4-7 | 12:44:44 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Vivaz | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 5 | 5-1 | 12:45:16 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Vivaz | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 5 | 5-1 | 12:45:17 | VENDEU: Rek'Sai (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Vivaz | DA_KogMaw18_AD | -0.6900 |  |
| Jogador 5 | 5-1 | 12:45:19 | COMPROU: Kobuko (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Vivaz | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 5 | 5-1 | 12:45:20 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Vivaz | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 5 | 5-2 | 12:45:37 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Vivaz | DA_KogMaw18_AD | 0.9700 |  |
| Jogador 5 | 5-2 | 12:45:38 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Vivaz | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 5-2 | 12:45:40 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Vivaz | DA_KogMaw18_AD | 1.0500 |  |
| Jogador 5 | 5-2 | 12:45:41 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Vivaz | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 6 | ? | 12:37:39 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 12:37:40 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 12:37:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 12:37:46 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 12:37:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 12:37:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 12:37:51 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 12:37:54 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 12:37:54 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 12:37:54 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 12:37:55 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 12:37:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 12:37:59 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5800 |  |
| Jogador 6 | 1-3 | 12:38:01 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0300 |  |
| Jogador 6 | 1-3 | 12:38:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 12:38:10 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 12:38:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 12:38:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 12:38:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 2-1 | 12:38:19 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 12:38:20 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 12:38:21 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 12:38:21 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 12:38:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 12:38:31 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 12:38:32 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 12:38:33 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 12:38:34 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-2 | 12:38:35 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 12:38:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 12:38:41 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 12:38:42 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 12:38:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 12:38:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 12:38:44 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 12:38:45 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 12:38:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 12:38:47 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.4100 |  |
| Jogador 6 | 2-4 | 12:38:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 12:38:58 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 2-4 | 12:38:59 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Tristana | -0.1200 |  |
| Jogador 6 | 2-5 | 12:39:06 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.7700 |  |
| Jogador 6 | 2-5 | 12:39:07 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-5 | 12:39:08 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Feérico | DA_18_Tristana | -0.4400 |  |
| Jogador 6 | 2-5 | 12:39:08 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Tristana | -1.0200 |  |
| Jogador 6 | 2-5 | 12:39:09 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_18_Tristana | -0.5700 |  |
| Jogador 6 | 2-5 | 12:39:10 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_Tristana | 0.3500 |  |
| Jogador 6 | 2-5 | 12:39:11 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Feérico | DA_18_Tristana | -0.5600 |  |
| Jogador 6 | 2-6 | 12:39:24 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Feérico | DA_18_Tristana | -0.9000 |  |
| Jogador 6 | 2-6 | 12:39:25 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-6 | 12:39:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Tristana | -0.1200 |  |
| Jogador 6 | 2-6 | 12:39:27 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-6 | 12:39:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 2-6 | 12:39:29 | MOVE Bench -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_Tristana | 0.4000 |  |
| Jogador 6 | 2-7 | 12:39:37 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Tristana | 0.1000 |  |
| Jogador 6 | 2-7 | 12:39:38 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Feérico | DA_18_Tristana | 0.2200 |  |
| Jogador 6 | 3-1 | 12:39:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Feérico | DA_18_Tristana | 0.8900 |  |
| Jogador 6 | 3-1 | 12:39:54 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 3-1 | 12:39:56 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 3-1 | 12:39:57 | MOVE Bench -> Board: Cascalho (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Tristana | 0.3900 |  |
| Jogador 6 | 3-1 | 12:39:58 | MOVE Board -> Board: Cascalho (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 3-1 | 12:39:59 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 6 | 3-1 | 12:39:59 | MOVE Bench -> Board: Alistar (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Feérico | DA_18_Tristana | -0.4000 |  |
| Jogador 6 | 3-2 | 12:40:10 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 3-3 | 12:40:26 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 3 | Feérico | DA_18_Tristana | 0.2300 |  |
| Jogador 6 | 3-3 | 12:40:28 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Feérico | DA_18_Tristana | 0.3100 |  |
| Jogador 6 | 3-3 | 12:40:29 | MOVE Board -> Board: Alistar (i:4.0) <-> Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-3 | 12:40:30 | MOVE Board -> Board: Cascalho (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 3-3 | 12:40:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 3 | Feérico | DA_18_Tristana | -0.0800 |  |
| Jogador 6 | 3-3 | 12:40:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 3 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 3-4 | 12:40:42 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Tristana | 0.7500 |  |
| Jogador 6 | 3-4 | 12:40:43 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Feérico | DA_18_Tristana | -0.5500 |  |
| Jogador 6 | 3-5 | 12:41:03 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Tristana | 0.5500 |  |
| Jogador 6 | 3-5 | 12:41:05 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Tristana | 0.0400 |  |
| Jogador 6 | 3-5 | 12:41:06 | MOVE Bench -> Board: Alistar (i:4.0) <-> Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Tristana | -0.4100 |  |
| Jogador 6 | 3-5 | 12:41:07 | MOVE Bench -> Board: Cascalho (i:4.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Tristana | -0.3300 |  |
| Jogador 6 | 3-5 | 12:41:08 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Tristana | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-6 | 12:41:20 | MOVE Bench -> Board: Alistar (i:4.0) <-> Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Feérico | DA_18_Tristana | -0.3500 |  |
| Jogador 6 | 3-6 | 12:41:21 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Feérico | DA_18_Tristana | -0.5600 |  |
| Jogador 6 | 3-6 | 12:41:22 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 6 | 3-7 | 12:41:45 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 3-7 | 12:41:46 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_18_Tristana | 0.2300 |  |
| Jogador 6 | 3-7 | 12:41:47 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 3-7 | 12:41:49 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Alistar (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 3-7 | 12:41:50 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Alistar (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_18_Tristana | 0.0900 |  |
| Jogador 6 | 4-1 | 12:42:03 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Feérico | DA_18_Tristana | 1.0100 |  |
| Jogador 6 | 4-1 | 12:42:04 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Feérico | DA_18_Tristana | 0.3600 |  |
| Jogador 6 | 4-1 | 12:42:06 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Feérico | DA_18_Tristana | 0.1100 |  |
| Jogador 6 | 4-2 | 12:42:29 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_18_Tristana | 0.9000 |  |
| Jogador 6 | 4-2 | 12:42:30 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Feérico | DA_18_Tristana | -0.2200 |  |
| Jogador 6 | 4-2 | 12:42:31 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Lillia | -0.6500 |  |
| Jogador 6 | 4-2 | 12:42:33 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Feérico | DA_18_Lillia | -0.1900 |  |
| Jogador 6 | 4-2 | 12:42:34 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Lillia | -0.3600 |  |
| Jogador 6 | 4-3 | 12:42:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Feérico | DA_18_Lillia | 0.3600 |  |
| Jogador 6 | 4-3 | 12:42:49 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Feérico | DA_18_Lillia | -0.2100 |  |
| Jogador 6 | 4-3 | 12:42:51 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 6 | 4-4 | 12:43:16 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Feérico | DA_18_Lillia | 0.9600 |  |
| Jogador 6 | 4-4 | 12:43:18 | MOVE Bench -> Board: Xayah (i:4.0) <-> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Feérico | DA_18_Lillia | -0.1300 |  |
| Jogador 6 | 4-4 | 12:43:19 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Feérico | DA_18_Lillia | 0.1400 |  |
| Jogador 6 | 4-4 | 12:43:20 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Feérico | DA_18_Lillia | 0.1500 |  |
| Jogador 6 | 4-4 | 12:43:21 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Feérico | DA_18_Lillia | 0.5000 |  |
| Jogador 6 | 4-5 | 12:43:39 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Feérico | DA_18_Lillia | 0.9000 |  |
| Jogador 6 | 4-5 | 12:43:41 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 6 | 4-5 | 12:43:43 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 6 | 4-6 | 12:44:19 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_18_Lillia | 0.3700 |  |
| Jogador 6 | 4-6 | 12:44:21 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 114 | 5 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 6 | 4-6 | 12:44:22 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_18_Lillia | 0.8100 |  |
| Jogador 6 | 4-6 | 12:44:24 | MOVE Bench -> Board: Alistar (i:8.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_18_Lillia | -0.1800 |  |
| Jogador 6 | 4-6 | 12:44:25 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_18_Lillia | 0.3300 |  |
| Jogador 6 | 4-7 | 12:44:41 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 121 | 5 | Feérico | DA_18_Lillia | 1.0200 |  |
| Jogador 6 | 4-7 | 12:44:43 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Feérico | DA_18_Lillia | 0.0600 |  |
| Jogador 6 | 4-7 | 12:44:44 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Alistar (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 117 | 5 | Feérico | DA_18_Lillia | 0.1300 |  |
| Jogador 6 | 5-1 | 12:45:16 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Feérico | DA_18_Lillia | 0.1500 |  |
| Jogador 6 | 5-1 | 12:45:17 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Feérico | DA_18_Lillia | 0.1300 |  |
| Jogador 6 | 5-1 | 12:45:19 | VENDEU: Xayah (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Feérico | DA_18_Lillia | -0.7100 |  |
| Jogador 6 | 5-1 | 12:45:20 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 7 | ? | 12:37:39 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 12:37:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:37:46 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 12:37:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 12:37:47 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 12:37:48 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 12:37:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 12:37:49 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 12:37:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 12:37:51 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 12:37:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 12:37:54 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 12:37:54 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 12:37:55 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 12:37:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 12:37:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 12:38:01 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 12:38:02 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-3 | 12:38:03 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 12:38:03 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 12:38:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 12:38:10 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 12:38:12 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 12:38:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 12:38:19 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 12:38:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 12:38:21 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 12:38:21 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 12:38:22 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 12:38:22 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 12:38:23 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-1 | 12:38:24 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-1 | 12:38:24 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Varus (i:2.0) (tabuleiro slot 9) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1500 |  |
| Jogador 7 | 2-2 | 12:38:31 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 12:38:32 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6500 |  |
| Jogador 7 | 2-2 | 12:38:33 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-2 | 12:38:34 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 12:38:35 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | -0.6200 |  |
| Jogador 7 | 2-2 | 12:38:35 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 12:38:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.0200 |  |
| Jogador 7 | 2-2 | 12:38:37 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Hecarim | 0.1700 |  |
| Jogador 7 | 2-3 | 12:38:41 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Hecarim | 0.3200 |  |
| Jogador 7 | 2-3 | 12:38:42 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2600 |  |
| Jogador 7 | 2-3 | 12:38:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-3 | 12:38:47 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.4200 |  |
| Jogador 7 | 2-4 | 12:38:53 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.2900 |  |
| Jogador 7 | 2-4 | 12:38:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.3100 |  |
| Jogador 7 | 2-4 | 12:38:59 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 12:39:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.9100 |  |
| Jogador 7 | 2-5 | 12:39:07 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 2-5 | 12:39:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 12:39:08 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 12:39:09 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 12:39:10 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.4800 |  |
| Jogador 7 | 2-5 | 12:39:11 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-6 | 12:39:24 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.2700 |  |
| Jogador 7 | 2-6 | 12:39:25 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 2-6 | 12:39:26 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-6 | 12:39:27 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.4800 |  |
| Jogador 7 | 2-6 | 12:39:28 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-6 | 12:39:29 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 12:39:37 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 2-7 | 12:39:38 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.1900 |  |
| Jogador 7 | 3-1 | 12:39:54 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 3-1 | 12:39:54 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-1 | 12:39:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-1 | 12:39:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-2 | 12:40:10 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 3-3 | 12:40:26 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 3-3 | 12:40:28 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 7 | 3-3 | 12:40:29 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 7 | 3-3 | 12:40:30 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 7 | 3-3 | 12:40:31 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 7 | 3-3 | 12:40:32 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 7 | 3-4 | 12:40:42 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 7 | 3-4 | 12:40:43 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 7 | 3-5 | 12:41:03 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Colosso | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 7 | 3-5 | 12:41:05 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Colosso | DA_KogMaw18_AD | 0.6500 |  |
| Jogador 7 | 3-5 | 12:41:06 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Yorick (i:2.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Colosso | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 7 | 3-5 | 12:41:07 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Yorick (i:2.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Colosso | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 7 | 3-5 | 12:41:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 3-6 | 12:41:20 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 2 | Colosso | DA_Sentinel18 | -0.4900 |  |
| Jogador 7 | 3-6 | 12:41:21 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Colosso | DA_Sentinel18 | 0.1900 |  |
| Jogador 7 | 3-6 | 12:41:22 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 2 | Colosso | DA_Sentinel18 | -0.3100 |  |
| Jogador 7 | 3-7 | 12:41:45 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Sentinel18 | 0.3500 |  |
| Jogador 7 | 3-7 | 12:41:46 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 3-7 | 12:41:47 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NegatronCloak -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 3-7 | 12:41:49 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 3-7 | 12:41:50 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Colosso | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 4-1 | 12:42:03 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-1 | 12:42:04 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Colosso | DA_Sentinel18 | 0.8700 |  |
| Jogador 7 | 4-1 | 12:42:06 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Colosso | DA_Sentinel18 | -0.4700 |  |
| Jogador 7 | 4-2 | 12:42:29 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 4-2 | 12:42:30 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 4-2 | 12:42:31 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 4-2 | 12:42:33 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Colosso | DA_Sentinel18 | 0.3700 |  |
| Jogador 7 | 4-2 | 12:42:34 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 77 | 5 | Colosso | DA_Sentinel18 | 0.4900 |  |
| Jogador 7 | 4-3 | 12:42:48 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Colosso | DA_Sentinel18 | 0.8800 |  |
| Jogador 7 | 4-3 | 12:42:49 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-3 | 12:42:51 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-4 | 12:43:16 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 4-4 | 12:43:18 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 103 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 4-4 | 12:43:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Colosso | DA_Sentinel18 | 0.1900 |  |
| Jogador 7 | 4-4 | 12:43:20 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 103 | 5 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-4 | 12:43:21 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 4-5 | 12:43:39 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 117 | 5 | Colosso | DA_Sentinel18 | -0.0500 |  |
| Jogador 7 | 4-5 | 12:43:41 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 114 | 5 | Colosso | DA_Sentinel18 | 0.9500 |  |
| Jogador 7 | 4-5 | 12:43:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 113 | 5 | Colosso | DA_Sentinel18 | 0.3800 |  |
| Jogador 7 | 4-6 | 12:44:19 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 125 | 5 | Colosso | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 4-6 | 12:44:21 | VENDEU: Hecarim (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 133 | 5 | Colosso | DA_Sentinel18 | -0.5300 |  |
| Jogador 7 | 4-6 | 12:44:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 130 | 5 | Colosso | DA_Sentinel18 | 0.1800 |  |
| Jogador 7 | 4-6 | 12:44:24 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 130 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-6 | 12:44:25 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 134 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-7 | 12:44:41 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 145 | 5 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 4-7 | 12:44:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 145 | 5 | Colosso | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 4-7 | 12:44:44 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 145 | 5 | Colosso | DA_Sentinel18 | 0.1300 |  |
| Jogador 7 | 5-1 | 12:45:16 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 161 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-1 | 12:45:17 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 159 | 5 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 5-1 | 12:45:19 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 161 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-1 | 12:45:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 158 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 5-2 | 12:45:37 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 175 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-2 | 12:45:38 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 172 | 5 | Colosso | DA_Sentinel18 | -0.2300 |  |
| Jogador 7 | 5-2 | 12:45:40 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 175 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 12:45:41 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 174 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-3 | 12:46:13 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 188 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-3 | 12:46:14 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 185 | 5 | Colosso | DA_Sentinel18 | 0.3800 |  |
| Jogador 7 | 5-3 | 12:46:16 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 188 | 5 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 5-3 | 12:46:17 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 184 | 5 | Colosso | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 5-4 | 12:46:35 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 201 | 5 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 5-4 | 12:46:37 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 198 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 5-4 | 12:46:39 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 201 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-4 | 12:46:40 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 199 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-5 | 12:47:15 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 211 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-5 | 12:47:17 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 208 | 5 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 5-5 | 12:47:18 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 211 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-5 | 12:47:20 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 208 | 5 | Colosso | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 5-6 | 12:47:37 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 222 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-6 | 12:47:39 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 219 | 5 | Colosso | DA_CrimsonRaptor18 | 1.0200 |  |
| Jogador 7 | 5-6 | 12:47:41 | MOVE Bench -> Board: Mamãe Bicuda (i:12.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 219 | 5 | Colosso | DA_CrimsonRaptor18 | 0.3500 |  |
| Jogador 7 | 5-6 | 12:47:42 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 216 | 5 | Colosso | DA_CrimsonRaptor18 | 0.1600 |  |
| Jogador 7 | 5-7 | 12:48:15 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 224 | 5 | Colosso | DA_CrimsonRaptor18 | -0.0700 |  |
| Jogador 7 | 5-7 | 12:48:17 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Mamãe Bicuda (i:12.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 224 | 5 | Colosso | DA_CrimsonRaptor18 | 0.1500 |  |
| Jogador 7 | 5-7 | 12:48:18 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 224 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 5-7 | 12:48:20 | MOVE Board -> Board: Mamãe Bicuda (i:12.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 224 | 5 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 7 | 6-1 | 12:48:39 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 238 | 5 | Colosso | DA_CrimsonRaptor18 | -0.0200 |  |
| Jogador 7 | 6-1 | 12:48:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 236 | 5 | Colosso | DA_CrimsonRaptor18 | 1.0100 |  |
| Jogador 7 | 6-1 | 12:48:42 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 241 | 5 | Colosso | DA_CrimsonRaptor18 | -0.5900 |  |
| Jogador 7 | 6-1 | 12:48:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 240 | 5 | Colosso | DA_CrimsonRaptor18 | 1.0800 |  |
| Jogador 7 | 6-2 | 12:49:19 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 248 | 5 | Colosso | DA_CrimsonRaptor18 | 0.5300 |  |
| Jogador 7 | 6-2 | 12:49:21 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 245 | 5 | Colosso | DA_CrimsonRaptor18 | 0.1600 |  |
| Jogador 7 | 6-2 | 12:49:22 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 245 | 5 | Colosso | DA_CrimsonRaptor18 | 0.1500 |  |
| Jogador 7 | 6-2 | 12:49:24 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 245 | 5 | Colosso | DA_CrimsonRaptor18 | 0.5700 |  |
| Jogador 7 | 6-3 | 12:49:43 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 254 | 5 | Colosso | DA_CrimsonRaptor18 | 0.9500 |  |
| Jogador 7 | 6-3 | 12:49:45 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 252 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 7 | 6-3 | 12:49:47 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 252 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 6-3 | 12:49:48 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 254 | 5 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 7 | 6-4 | 12:50:23 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 264 | 5 | Colosso | DA_CrimsonRaptor18 | 1.1100 |  |
| Jogador 7 | 6-4 | 12:50:25 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 263 | 5 | Colosso | DA_CrimsonRaptor18 | 0.1200 |  |
| Jogador 7 | 6-4 | 12:50:26 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 260 | 5 | Colosso | DA_CrimsonRaptor18 | -0.2200 |  |
| Jogador 7 | 6-4 | 12:50:28 | VENDEU: Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 265 | 5 | Colosso | DA_CrimsonRaptor18 | -0.6900 |  |
| Jogador 7 | 6-5 | 12:50:47 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 273 | 5 | Colosso | DA_CrimsonRaptor18 | 1.0400 |  |
| Jogador 7 | 6-5 | 12:50:48 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 276 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 6-5 | 12:50:50 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 273 | 5 | Colosso | DA_CrimsonRaptor18 | 0.9700 |  |
| Jogador 7 | 6-5 | 12:50:52 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 276 | 5 | Colosso | DA_CrimsonRaptor18 | -0.0500 |  |
| Jogador 7 | 6-6 | 12:51:30 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 285 | 5 | Colosso | DA_CrimsonRaptor18 | 0.1100 |  |
| Jogador 7 | 6-6 | 12:51:31 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 288 | 5 | Colosso | DA_CrimsonRaptor18 | -0.0300 |  |
| Jogador 7 | 6-6 | 12:51:33 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 286 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 7 | 6-6 | 12:51:35 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 288 | 5 | Colosso | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 7 | 6-7 | 12:51:55 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 296 | 5 | Colosso | DA_CrimsonRaptor18 | 0.7400 |  |
| Jogador 7 | 6-7 | 12:51:56 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Cassiopeia (i:6.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 296 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0700 |  |
| Jogador 7 | 6-7 | 12:51:58 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 299 | 5 | Colosso | DA_CrimsonRaptor18 | -0.1000 |  |
| Jogador 7 | 6-7 | 12:51:59 | COMPROU: Lillia (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 295 | 5 | Colosso | DA_CrimsonRaptor18 | 0.0300 |  |
| Jogador 8 | ? | 12:37:39 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 12:37:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 12:37:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:37:46 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 12:37:46 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 12:37:47 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 12:37:48 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 12:37:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 12:37:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 12:37:51 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 12:37:54 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 12:37:54 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 12:37:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 12:38:01 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 12:38:02 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 12:38:03 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 12:38:03 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 12:38:04 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 12:38:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 12:38:10 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 12:38:11 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 12:38:12 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 12:38:13 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 12:38:13 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 12:38:14 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 2-1 | 12:38:19 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 12:38:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-1 | 12:38:21 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-1 | 12:38:21 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-1 | 12:38:22 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-1 | 12:38:22 | MOVE Board -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-1 | 12:38:23 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.5200 |  |
| Jogador 8 | 2-1 | 12:38:24 | MOVE Bench -> Board: Karma (i:4.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-1 | 12:38:24 | MOVE Bench -> Board: Xayah (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 2-2 | 12:38:31 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.9800 |  |
| Jogador 8 | 2-2 | 12:38:32 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.9500 |  |
| Jogador 8 | 2-2 | 12:38:33 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.3300 |  |
| Jogador 8 | 2-2 | 12:38:34 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-2 | 12:38:35 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.2700 |  |
| Jogador 8 | 2-2 | 12:38:35 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.4300 |  |
| Jogador 8 | 2-2 | 12:38:36 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.2300 |  |
| Jogador 8 | 2-2 | 12:38:37 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | -0.2200 |  |
| Jogador 8 | 2-3 | 12:38:41 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 2-3 | 12:38:42 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1600 |  |
| Jogador 8 | 2-3 | 12:38:43 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_Karma18 | -0.6300 |  |
| Jogador 8 | 2-3 | 12:38:44 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 2-3 | 12:38:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-3 | 12:38:45 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 2-3 | 12:38:46 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 2-3 | 12:38:47 | MOVE Board -> Board: Kobuko (i:2.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-4 | 12:38:53 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 2-4 | 12:38:58 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 2-4 | 12:38:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_Karma18 | 0.5400 |  |
| Jogador 8 | 2-5 | 12:39:06 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-5 | 12:39:07 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | 0.8200 |  |
| Jogador 8 | 2-5 | 12:39:08 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 2-5 | 12:39:08 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-5 | 12:39:09 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_Karma18 | 0.0400 |  |
| Jogador 8 | 2-5 | 12:39:10 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-5 | 12:39:11 | MOVE Board -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 2-6 | 12:39:24 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-6 | 12:39:25 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | 0.8700 |  |
| Jogador 8 | 2-6 | 12:39:26 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-6 | 12:39:27 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-6 | 12:39:28 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Enfeitiçador | DA_Karma18 | -0.0200 |  |
| Jogador 8 | 2-6 | 12:39:29 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 2-7 | 12:39:37 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-7 | 12:39:38 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 3-1 | 12:39:54 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Enfeitiçador | DA_Karma18 | -0.1800 |  |
| Jogador 8 | 3-1 | 12:39:54 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 3-1 | 12:39:56 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.1100 |  |
| Jogador 8 | 3-1 | 12:39:57 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 3-1 | 12:39:58 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_Karma18 | -0.1600 |  |
| Jogador 8 | 3-1 | 12:39:59 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 3-1 | 12:39:59 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_Karma18 | -0.3300 |  |
| Jogador 8 | 3-2 | 12:40:10 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Enfeitiçador | DA_Karma18 | 0.0100 |  |
| Jogador 8 | 3-3 | 12:40:26 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Enfeitiçador | DA_Karma18 | 0.8800 |  |
| Jogador 8 | 3-3 | 12:40:28 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Enfeitiçador | DA_Karma18 | 0.8800 |  |
| Jogador 8 | 3-3 | 12:40:29 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Enfeitiçador | DA_Karma18 | 0.3100 |  |
| Jogador 8 | 3-3 | 12:40:30 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Enfeitiçador | DA_Karma18 | 0.5400 |  |
| Jogador 8 | 3-3 | 12:40:31 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_Karma18 | -0.2600 |  |
| Jogador 8 | 3-3 | 12:40:32 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 3-4 | 12:40:42 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Enfeitiçador | DA_Karma18 | 0.8400 |  |
| Jogador 8 | 3-4 | 12:40:43 | VENDEU: Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Enfeitiçador | DA_Karma18 | -0.5400 |  |
| Jogador 8 | 3-5 | 12:41:03 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 3-5 | 12:41:05 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 3-5 | 12:41:06 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Enfeitiçador | DA_Karma18 | -0.4900 |  |
| Jogador 8 | 3-5 | 12:41:07 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Karma (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Enfeitiçador | DA_Karma18 | 0.1500 |  |
| Jogador 8 | 3-5 | 12:41:08 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 57 | 4 | Enfeitiçador | DA_Karma18 | 0.4700 |  |
| Jogador 8 | 3-6 | 12:41:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Enfeitiçador | DA_Karma18 | 0.3400 |  |
| Jogador 8 | 3-6 | 12:41:21 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 3-6 | 12:41:22 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Karma (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 3-7 | 12:41:45 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 3-7 | 12:41:46 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Warwick (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 3-7 | 12:41:47 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Karma (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Enfeitiçador | DA_Karma18 | 0.2500 |  |
| Jogador 8 | 3-7 | 12:41:49 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_SparringGloves -> Warwick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 3-7 | 12:41:50 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Enfeitiçador | DA_Karma18 | 0.0200 |  |
| Jogador 8 | 4-1 | 12:42:03 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Enfeitiçador | DA_Karma18 | -0.2400 |  |
| Jogador 8 | 4-1 | 12:42:04 | MOVE Board -> Board: Karma (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-1 | 12:42:06 | MOVE Board -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 4-2 | 12:42:29 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 98 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-2 | 12:42:30 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Enfeitiçador | DA_Karma18 | 0.3500 |  |
| Jogador 8 | 4-2 | 12:42:31 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Enfeitiçador | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 4-2 | 12:42:33 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Enfeitiçador | DA_Karma18 | -0.1800 |  |
| Jogador 8 | 4-2 | 12:42:34 | MOVE Board -> Board: Warwick (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Enfeitiçador | DA_Karma18 | -0.1500 |  |
| Jogador 8 | 4-3 | 12:42:48 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 4-3 | 12:42:49 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Enfeitiçador | DA_Karma18 | 0.9100 |  |
| Jogador 8 | 4-3 | 12:42:51 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 4-4 | 12:43:16 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_Karma18 | 1.0300 |  |
| Jogador 8 | 4-4 | 12:43:18 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Enfeitiçador | DA_18_Tristana | 0.8800 |  |
| Jogador 8 | 4-4 | 12:43:19 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Enfeitiçador | DA_18_Tristana | -0.0700 |  |
| Jogador 8 | 4-4 | 12:43:20 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Enfeitiçador | DA_18_Tristana | 1.1000 |  |
| Jogador 8 | 4-4 | 12:43:21 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Enfeitiçador | DA_18_Tristana | 0.5800 |  |
| Jogador 8 | 4-5 | 12:43:39 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_Tristana | 0.0300 |  |
| Jogador 8 | 4-5 | 12:43:41 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Enfeitiçador | DA_18_Tristana | -0.2800 |  |
| Jogador 8 | 4-5 | 12:43:43 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Enfeitiçador | DA_18_Tristana | -0.2800 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 27 | 28 | 140 | 27 | 16 | 122 | 11 | 31 |
| Jogador 2 | 27 | 28 | 140 | 27 | 16 | 124 | 3 | 19 |
| Jogador 3 | 39 | 39 | 195 | 39 | 20 | 169 | 4 | 34 |
| Jogador 4 | 24 | 24 | 120 | 24 | 15 | 108 | 8 | 6 |
| Jogador 5 | 28 | 28 | 140 | 28 | 16 | 122 | 9 | 40 |
| Jogador 6 | 27 | 27 | 135 | 27 | 19 | 117 | 5 | 39 |
| Jogador 7 | 39 | 39 | 195 | 39 | 18 | 174 | 7 | 22 |
| Jogador 8 | 24 | 25 | 125 | 24 | 17 | 117 | 4 | 25 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 122 | 122 | 0 | 115 | 0 | 122 | 122 | 122 | 45/31 |
| Jogador 2 | 124 | 124 | 124 | 0 | 117 | 0 | 124 | 124 | 124 | 50/35 |
| Jogador 3 | 169 | 169 | 169 | 0 | 158 | 0 | 169 | 169 | 169 | 64/50 |
| Jogador 4 | 108 | 108 | 108 | 0 | 103 | 0 | 108 | 108 | 108 | 46/33 |
| Jogador 5 | 122 | 122 | 122 | 0 | 115 | 0 | 122 | 122 | 122 | 58/44 |
| Jogador 6 | 117 | 117 | 117 | 0 | 107 | 0 | 117 | 117 | 117 | 47/33 |
| Jogador 7 | 174 | 174 | 174 | 0 | 160 | 0 | 174 | 174 | 174 | 71/56 |
| Jogador 8 | 117 | 117 | 117 | 0 | 109 | 0 | 117 | 117 | 117 | 55/42 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.20922301709651947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.25060486793518066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22248587012290955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013312771916389465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4272024929523468 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3464421331882477 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2493164837360382 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387929677963257 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0313351154327393 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 46 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 47 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3355763852596283 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 53 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13010208308696747 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 54 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060082387179136276 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27574819326400757 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 58 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17249611020088196 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-2 | 59 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32773715257644653 | 0.0 | 0.0 | +e76c0caf-1c3d-493f-9a21-659dd8587fc2 / -— |
| Jogador 1 | 2-2 | 60 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3528463542461395 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 63 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 64 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3343530297279358 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 65 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17810221016407013 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 66 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15125100314617157 | 0.0 | 0.0 | +— / -e76c0caf-1c3d-493f-9a21-659dd8587fc2 |
| Jogador 1 | 2-3 | 67 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 68 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 71 | BUY | STABILIZE | 93.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1169943809509277 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 72 | BUY | STABILIZE | 93.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3641270399093628 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42868706583976746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 74 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012633305042982101 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 75 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 76 | PASS | STABILIZE | 93.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 80 | BUY | STABILIZE | 93.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0241254568099976 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 81 | BUY | STABILIZE | 93.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.325840026140213 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 82 | SELL | STABILIZE | 93.0 | 5 | 2 | 0 | 12.0 | Inferno/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-6 | 84 | BUY | STABILIZE | 93.0 | 5 | 11 | 1 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479967594146729 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 85 | BUY | STABILIZE | 93.0 | 5 | 10 | 1 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15169169008731842 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 86 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 7 | 0 | 10.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22373852133750916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 87 | BUY | STABILIZE | 93.0 | 5 | 7 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06715136766433716 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 88 | BUY_XP | STABILIZE | 93.0 | 5 | 4 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001724999980069697 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 89 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 0 | 0 | 12.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16764943301677704 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 90 | PASS | STABILIZE | 93.0 | 6 | 0 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 92 | BUY | STABILIZE | 93.0 | 6 | 7 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0474058389663696 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 93 | BUY | STABILIZE | 93.0 | 6 | 6 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04939080774784088 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 94 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 4 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7151246070861816 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 95 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 4 | 0 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6917133927345276 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 96 | PASS | STABILIZE | 93.0 | 6 | 4 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 97 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 4 | 0 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42569252848625183 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 99 | BUY | STABILIZE | 93.0 | 6 | 10 | 1 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6986255049705505 | 0.0 | 0.0 | +8980fd33-79c8-4825-95e9-9298680cbc6d / -— |
| Jogador 1 | 3-1 | 100 | CRAFT_AND_EQUIP | STABILIZE | 93.0 | 6 | 8 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25157490372657776 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 102 | BUY | STABILIZE | 82.0 | 6 | 13 | 1 | 22.0 | Fumegante/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8356629014015198 | 0.0 | 0.0 | +5204a655-be8f-4607-8fa3-28c981ac1397 / -8980fd33-79c8-4825-95e9-9298680cbc6d,b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 3-2 | 103 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 11 | 1 | 14.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.357859343290329 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 104 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 11 | 1 | 16.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15709108114242554 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 105 | BUY | STABILIZE | 82.0 | 6 | 11 | 1 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023504728451371193 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 8 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013986314879730344 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 107 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 8 | 0 | 18.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3995804190635681 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 108 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 8 | 0 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014687101356685162 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 110 | BUY | STABILIZE | 71.0 | 6 | 14 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022353680804371834 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-4 | 112 | BUY | STABILIZE | 62.0 | 6 | 18 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07976885139942169 | 0.0 | 0.0 | +54b47885-6cb9-42e7-a9bb-049e0e2d2956 / -— |
| Jogador 1 | 3-4 | 113 | BUY | STABILIZE | 62.0 | 6 | 17 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2915230393409729 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 114 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 15 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.6367674788853037e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 115 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 15 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016130834817886353 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 116 | PASS | STABILIZE | 62.0 | 6 | 15 | 1 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 119 | BUY | STABILIZE | 62.0 | 6 | 22 | 2 | 26.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8492928743362427 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 120 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 20 | 2 | 18.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10349401831626892 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 122 | BUY | STABILIZE | 62.0 | 6 | 28 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2967488169670105 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 123 | BUY | STABILIZE | 62.0 | 6 | 26 | 2 | 28.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8164594173431396 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 124 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 24 | 2 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06925182789564133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 125 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 24 | 2 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0072157601825892925 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 126 | PASS | STABILIZE | 62.0 | 6 | 24 | 2 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02199999988079071 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 128 | SELL | STABILIZE | 62.0 | 6 | 33 | 3 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 1 | 3-7 | 129 | BUY | STABILIZE | 62.0 | 6 | 38 | 3 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25516754388809204 | 0.0 | 0.0 | +0d8cf876-2884-4724-ab79-246f8e0406f0 / -— |
| Jogador 1 | 3-7 | 130 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04072440788149834 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 132 | CRAFT_AND_EQUIP | STABILIZE | 62.0 | 6 | 45 | 4 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18881523609161377 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 133 | CRAFT_AND_EQUIP | STABILIZE | 62.0 | 6 | 45 | 4 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1957186907529831 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 134 | SELL | STABILIZE | 62.0 | 6 | 45 | 4 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008766666986048222 | 0.0 | 0.0 | +— / -54b47885-6cb9-42e7-a9bb-049e0e2d2956 |
| Jogador 1 | 4-1 | 135 | BUY | STABILIZE | 62.0 | 6 | 46 | 4 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022593088448047638 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 136 | SELL | STABILIZE | 62.0 | 6 | 43 | 4 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 4-2 | 138 | BUY | STABILIZE | 52.0 | 6 | 55 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07702304422855377 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 139 | SELL | STABILIZE | 52.0 | 6 | 52 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010333333164453506 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 4-2 | 140 | BUY | STABILIZE | 52.0 | 6 | 55 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022897711023688316 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 1 | 4-3 | 142 | SELL | STABILIZE | 52.0 | 6 | 64 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -301afc05-ad23-4ed2-a835-108235c399e0 |
| Jogador 1 | 4-3 | 143 | BUY | STABILIZE | 52.0 | 6 | 66 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9619682431221008 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-3 | 144 | BUY | STABILIZE | 52.0 | 6 | 64 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00972900539636612 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 1 | 4-3 | 145 | BUY | STABILIZE | 52.0 | 6 | 63 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2642749547958374 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 1 | 4-3 | 146 | MOVE_BOARD | STABILIZE | 52.0 | 6 | 60 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 148 | SELL | STABILIZE | 41.0 | 6 | 70 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 |
| Jogador 1 | 4-4 | 149 | BUY | STABILIZE | 41.0 | 6 | 75 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09175723791122437 | 0.0 | 0.0 | +94e3fa7e-029d-4de6-a1e4-9e67ce1b699e / -— |
| Jogador 1 | 4-4 | 150 | SELL | STABILIZE | 41.0 | 6 | 73 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -ba7f039a-929c-4537-9eb6-f1dc4563cca8 |
| Jogador 1 | 4-5 | 152 | BUY | STABILIZE | 41.0 | 6 | 84 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3319928050041199 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 1 | 4-5 | 153 | SELL | STABILIZE | 41.0 | 6 | 81 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -94e3fa7e-029d-4de6-a1e4-9e67ce1b699e |
| Jogador 1 | 4-5 | 154 | BUY | STABILIZE | 41.0 | 6 | 83 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1305382400751114 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 1 | 4-5 | 155 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 79 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013280492275953293 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 156 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 79 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01502221543341875 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 158 | SELL | STABILIZE | 29.0 | 6 | 90 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -6388773b-0e99-40a9-8d68-895dcf16fce6 |
| Jogador 1 | 4-6 | 159 | BUY | STABILIZE | 29.0 | 6 | 93 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8622563481330872 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 1 | 4-6 | 160 | SELL | STABILIZE | 29.0 | 6 | 91 | 5 | 28.0 | Inferno/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 4-7 | 162 | BUY | ALL_IN | 17.0 | 6 | 105 | 5 | 28.0 | Inferno/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03752972185611725 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 1 | 4-7 | 163 | SELL | ALL_IN | 17.0 | 6 | 103 | 5 | 28.0 | Adaptador/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04586666822433472 | 0.0 | 0.0 | +— / -d1bc6c5b-74a5-46db-b00f-e91265546f5d |
| Jogador 1 | 4-7 | 164 | BUY | ALL_IN | 17.0 | 6 | 105 | 5 | 28.0 | Adaptador/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.159292072057724 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 1 | 4-7 | 165 | REROLL | ALL_IN | 17.0 | 6 | 102 | 5 | 28.0 | Adaptador/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 166 | SELL | ALL_IN | 17.0 | 6 | 100 | 5 | 28.0 | Adaptador/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -f8a93323-530e-4f9c-99d7-a5ec83b78992 |
| Jogador 1 | 5-1 | 168 | BUY | ALL_IN | 17.0 | 6 | 114 | 5 | 28.0 | Adaptador/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9188652634620667 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 1 | 5-1 | 169 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 6 | 111 | 5 | 28.0 | Adaptador/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17469331622123718 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 170 | CRAFT_AND_EQUIP | ALL_IN | 17.0 | 6 | 111 | 5 | 28.0 | Adaptador/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1809816062450409 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 172 | SELL | ALL_IN | 2.0 | 6 | 122 | 5 | 28.0 | Adaptador/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 1 | 5-2 | 173 | BUY | ALL_IN | 2.0 | 6 | 126 | 5 | 28.0 | Adaptador/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5517268180847168 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 1 | 5-2 | 174 | SELL | ALL_IN | 2.0 | 6 | 125 | 5 | 28.0 | Adaptador/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5383333563804626 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 5-2 | 175 | BUY | ALL_IN | 2.0 | 6 | 127 | 5 | 28.0 | Adaptador/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27527791261672974 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5006924271583557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178046464920044 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11945630609989166 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3084914982318878 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4079708158969879 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0722225904464722 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.201566681265831 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40031522512435913 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 40 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0379269123077393 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18184421956539154 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 46 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.27360159158706665 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 47 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2647325098514557 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 48 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1475684940814972 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048402830958366394 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19665099680423737 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-2 | 52 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479713678359985 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 53 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23212109506130219 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 54 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14894025027751923 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 55 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047096773982048035 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 56 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24561917781829834 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 57 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 58 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 59 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19457465410232544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 60 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01434213388711214 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 62 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2976941168308258 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 63 | BUY_XP | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 64 | PASS | STABILIZE | 90.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 69 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40171101689338684 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 71 | BUY | STABILIZE | 90.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9691769480705261 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 72 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3296371102333069 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 73 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008978793048299849 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 74 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-4 | 75 | BUY | STABILIZE | 90.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12602375447750092 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 76 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1526757776737213 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-4 | 77 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19187059998512268 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 2 | 2-4 | 78 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39907389879226685 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 80 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31064656376838684 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 81 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11375081539154053 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 82 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19276323914527893 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-6 | 84 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18691162765026093 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 85 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 86 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10230773687362671 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-6 | 87 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-6 | 88 | SELL | STABILIZE | 85.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42233332991600037 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 2-6 | 89 | BUY | STABILIZE | 85.0 | 5 | 9 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07305749505758286 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 90 | BUY_XP | STABILIZE | 85.0 | 5 | 7 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 92 | BUY | STABILIZE | 80.0 | 5 | 9 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.549433171749115 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 93 | BUY_XP | STABILIZE | 80.0 | 5 | 6 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 94 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5931441783905029 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 95 | BUY | STABILIZE | 80.0 | 6 | 2 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18160781264305115 | 0.0 | 0.0 | +0067f61f-504d-440a-b071-de7f18886e3d / -— |
| Jogador 2 | 2-7 | 96 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002667901280801743 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 97 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014767679385840893 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 99 | BUY | STABILIZE | 80.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13456185162067413 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 100 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 6 | 4 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2080308198928833 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 102 | BUY | STABILIZE | 72.0 | 6 | 10 | 1 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7579249739646912 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -7ca9b803-76eb-4283-9648-7f98bfd81149,d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 3-2 | 103 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 9 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40027299523353577 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 104 | BUY_XP | STABILIZE | 72.0 | 6 | 9 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 105 | BUY_XP | STABILIZE | 72.0 | 6 | 5 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 107 | SELL | STABILIZE | 72.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-2 | 108 | BUY_XP | STABILIZE | 72.0 | 6 | 4 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 110 | BUY | STABILIZE | 62.0 | 6 | 6 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8037915229797363 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-4 | 112 | BUY | STABILIZE | 62.0 | 6 | 9 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.234888955950737 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 113 | BUY_XP | STABILIZE | 62.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 114 | SELL | STABILIZE | 62.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-4 | 115 | SELL | STABILIZE | 62.0 | 6 | 5 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04172957316040993 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 3-4 | 116 | BUY | STABILIZE | 62.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0628819391131401 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 117 | SELL | STABILIZE | 62.0 | 6 | 5 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3583333194255829 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-5 | 119 | BUY | STABILIZE | 62.0 | 6 | 12 | 1 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7599327564239502 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 120 | BUY | STABILIZE | 62.0 | 6 | 11 | 1 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5386149883270264 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-6 | 122 | BUY | STABILIZE | 62.0 | 6 | 15 | 1 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28793397545814514 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 123 | SELL | STABILIZE | 62.0 | 6 | 14 | 1 | 18.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5879999995231628 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 3-6 | 124 | SELL | STABILIZE | 62.0 | 6 | 15 | 1 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4645501375198364 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 3-6 | 125 | BUY | STABILIZE | 62.0 | 6 | 18 | 1 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15227456390857697 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -— |
| Jogador 2 | 3-6 | 126 | SELL | STABILIZE | 62.0 | 6 | 15 | 1 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36500000953674316 | 0.0 | 0.0 | +— / -33a860e2-992f-4355-ab24-85b4a2576f90 |
| Jogador 2 | 3-7 | 128 | BUY | STABILIZE | 50.0 | 6 | 24 | 2 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8489342927932739 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 129 | BUY | STABILIZE | 50.0 | 6 | 21 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8421447277069092 | 0.0 | 0.0 | +813260b6-a1b8-4a5c-978e-acd60b6b1082 / -c5a8f36d-74b1-4944-a3db-bfb601a89b59,ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 2 | 3-7 | 130 | BUY | STABILIZE | 50.0 | 6 | 20 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3198486566543579 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 4-1 | 132 | BUY | STABILIZE | 50.0 | 6 | 23 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8387210965156555 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 2 | 4-1 | 133 | CRAFT_AND_EQUIP | STABILIZE | 50.0 | 6 | 22 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14385002851486206 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 134 | CRAFT_AND_EQUIP | STABILIZE | 50.0 | 6 | 22 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2138085514307022 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 135 | BUY | STABILIZE | 50.0 | 6 | 22 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11214382946491241 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 136 | MOVE_BENCH | STABILIZE | 50.0 | 6 | 20 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09997107088565826 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 138 | BUY | STABILIZE | 38.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8679606318473816 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 139 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 27 | 2 | 20.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000351130962372 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 140 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 27 | 2 | 14.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33472940325737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 142 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 35 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4007568955421448 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 143 | BUY | STABILIZE | 28.0 | 7 | 35 | 3 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013415180146694183 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 2 | 4-3 | 144 | BUY | STABILIZE | 28.0 | 7 | 32 | 3 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3655128479003906 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 2 | 4-3 | 145 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 29 | 2 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007085343822836876 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 146 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 29 | 2 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00791271310299635 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 148 | BUY | STABILIZE | 28.0 | 7 | 38 | 3 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8110490441322327 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -cce8de69-f877-4e86-b720-6aea91e68f47,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 4-4 | 149 | BUY | STABILIZE | 28.0 | 7 | 35 | 3 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12346452474594116 | 0.0 | 0.0 | +157648c2-e9b6-4eb2-b42c-19c554a3a41e / -— |
| Jogador 2 | 4-4 | 150 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 34 | 3 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.241046604467556e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 152 | BUY | STABILIZE | 28.0 | 7 | 42 | 4 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19792921841144562 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 2 | 4-5 | 153 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 39 | 3 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009517063735984266 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 154 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 39 | 3 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04564814269542694 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 155 | PASS | STABILIZE | 28.0 | 7 | 39 | 3 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07135767489671707 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 158 | SELL | STABILIZE | 28.0 | 7 | 50 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09763965010643005 | 0.0 | 0.0 | +— / -e1867f53-f97a-4c7a-bce3-24aa037ce27f |
| Jogador 2 | 4-6 | 159 | BUY | STABILIZE | 28.0 | 7 | 58 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3869971036911011 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 2 | 4-6 | 160 | SELL | STABILIZE | 28.0 | 7 | 57 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 2 | 4-7 | 162 | BUY | STABILIZE | 28.0 | 7 | 72 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49817007780075073 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 2 | 4-7 | 163 | SELL | STABILIZE | 28.0 | 7 | 71 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -157648c2-e9b6-4eb2-b42c-19c554a3a41e |
| Jogador 2 | 4-7 | 164 | BUY | STABILIZE | 28.0 | 7 | 72 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031004469841718674 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 2 | 4-7 | 165 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 70 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.051610135822557e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 166 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 70 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015002161264419556 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 168 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 7 | 81 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13549332320690155 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 169 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 7 | 81 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17444759607315063 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 170 | SELL | STABILIZE | 28.0 | 7 | 81 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011020994745194912 | 0.0 | 0.0 | +— / -3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 |
| Jogador 2 | 5-2 | 172 | BUY | ALL_IN | 13.0 | 7 | 93 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7435165047645569 | 0.0 | 0.0 | +2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 / -104aaac3-252c-4c1b-9ad8-fc10a35c6cda,d1f19609-8b5f-489d-a2cf-d015fe7ed27e |
| Jogador 2 | 5-2 | 173 | BUY | ALL_IN | 13.0 | 7 | 90 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03597446531057358 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -— |
| Jogador 2 | 5-2 | 174 | BUY | ALL_IN | 13.0 | 7 | 87 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09557425230741501 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -— |
| Jogador 2 | 5-2 | 175 | REROLL | ALL_IN | 13.0 | 7 | 83 | 5 | 36.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4068913459777832 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.039654016494751 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179771423339844 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.589362621307373 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22690066695213318 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2120411992073059 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2657451331615448 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 46 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3955826759338379 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21830201148986816 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007552699651569128 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012296375818550587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9576538801193237 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 53 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3375449478626251 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 54 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3327644169330597 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 63 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2665497064590454 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 65 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 71 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901286125183105 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3921666145324707 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4147171974182129 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 74 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15196292102336884 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 75 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034331925213336945 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 76 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.047020673984662e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 78 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 80 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8984256982803345 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 81 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3943612277507782 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 84 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07140234112739563 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 2-6 | 85 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8675545454025269 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 86 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4047930836677551 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 87 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499921202659607 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 88 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10867002606391907 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 89 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06023341044783592 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7375186085700989 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 92 | BUY | STABILIZE | 100.0 | 5 | 15 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8874425888061523 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 93 | BUY | STABILIZE | 100.0 | 5 | 12 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33233001828193665 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 94 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08651655167341232 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 95 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01118701882660389 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 96 | BUY_XP | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 97 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050634998828172684 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 99 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24933190643787384 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 100 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6109686493873596 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 102 | BUY | STABILIZE | 100.0 | 6 | 17 | 1 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8253876566886902 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-2 | 103 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 16 | 1 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6525434851646423 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 104 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 16 | 1 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.630698561668396 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 105 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016304239630699158 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02261360175907612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 107 | PASS | STABILIZE | 100.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05649999901652336 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 110 | BUY | STABILIZE | 100.0 | 6 | 26 | 2 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22951540350914001 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-4 | 112 | BUY | STABILIZE | 100.0 | 6 | 33 | 3 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29365700483322144 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 30 | 3 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001556185889057815 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 114 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 30 | 3 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018327200785279274 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 115 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 30 | 3 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0159743744879961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 116 | PASS | STABILIZE | 100.0 | 6 | 30 | 3 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 119 | SELL | STABILIZE | 100.0 | 6 | 41 | 4 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41575556993484497 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-5 | 120 | BUY | STABILIZE | 100.0 | 6 | 44 | 4 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8188460469245911 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-6 | 122 | SELL | STABILIZE | 91.0 | 6 | 50 | 5 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 |
| Jogador 3 | 3-6 | 123 | BUY | STABILIZE | 91.0 | 6 | 55 | 5 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8615983128547668 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 124 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 53 | 5 | 26.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0999860018491745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 125 | SELL | STABILIZE | 91.0 | 6 | 53 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0034687586594372988 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 3-6 | 126 | BUY | STABILIZE | 91.0 | 6 | 54 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39063769578933716 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-7 | 128 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44676634669303894 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 129 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5735440254211426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 130 | PASS | STABILIZE | 91.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1590963453054428 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 132 | CRAFT_AND_EQUIP | STABILIZE | 91.0 | 6 | 72 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17436330020427704 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 133 | CRAFT_AND_EQUIP | STABILIZE | 91.0 | 6 | 72 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.236711323261261 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 134 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 72 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10047879070043564 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 135 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 72 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7716274261474609 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 136 | SELL | STABILIZE | 91.0 | 6 | 72 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 4-2 | 138 | BUY | STABILIZE | 91.0 | 6 | 87 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8527601957321167 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 3 | 4-2 | 139 | EQUIP_FROM_INVENTORY | STABILIZE | 91.0 | 6 | 85 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05007951706647873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 140 | EQUIP_FROM_INVENTORY | STABILIZE | 91.0 | 6 | 85 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.041245218366384506 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 142 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 97 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9674683809280396 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 143 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 97 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37437358498573303 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 144 | PASS | STABILIZE | 91.0 | 6 | 97 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11268653720617294 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 148 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 109 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13362041115760803 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 149 | SELL | STABILIZE | 91.0 | 6 | 109 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028113825246691704 | 0.0 | 0.0 | +— / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 4-4 | 150 | BUY | STABILIZE | 91.0 | 6 | 111 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2415032833814621 | 0.0 | 0.0 | +f4173576-aa2e-4a93-94ec-ecd49d90d2b7 / -— |
| Jogador 3 | 4-5 | 152 | SELL | STABILIZE | 91.0 | 6 | 119 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -f4173576-aa2e-4a93-94ec-ecd49d90d2b7 |
| Jogador 3 | 4-5 | 153 | BUY | STABILIZE | 91.0 | 6 | 122 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3602411448955536 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -— |
| Jogador 3 | 4-5 | 154 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 119 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10355965793132782 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 155 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 119 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7629966735839844 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 156 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 119 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33775612711906433 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 158 | SELL | STABILIZE | 91.0 | 6 | 132 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -527f78df-1e51-4731-9175-1c4812aa82ad |
| Jogador 3 | 4-6 | 159 | BUY | STABILIZE | 91.0 | 6 | 136 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9625794887542725 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -0e31b1ec-3ead-480e-8577-f59bb5486d00,bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 4-6 | 160 | BUY | STABILIZE | 91.0 | 6 | 134 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33277982473373413 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -— |
| Jogador 3 | 4-7 | 162 | BUY | STABILIZE | 91.0 | 6 | 146 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9637945890426636 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -a9c52953-4532-455b-851f-04079adfd354,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 4-7 | 163 | BUY | STABILIZE | 91.0 | 6 | 143 | 5 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9611599445343018 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -9bd6852a-b7a4-468c-a8cc-5318f7906eae,ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 4-7 | 164 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 141 | 5 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3725837767124176 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 165 | BUY | STABILIZE | 91.0 | 6 | 141 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059961527585983276 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -— |
| Jogador 3 | 4-7 | 166 | MOVE_BENCH | STABILIZE | 91.0 | 6 | 139 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5583252310752869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 168 | BUY | FAST8 | 91.0 | 6 | 152 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8054702281951904 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 3 | 5-1 | 169 | BUY | FAST8 | 91.0 | 6 | 150 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07991378754377365 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -— |
| Jogador 3 | 5-1 | 170 | CRAFT_AND_EQUIP | FAST8 | 91.0 | 6 | 149 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22150222957134247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 172 | CRAFT_AND_EQUIP | FAST8 | 91.0 | 6 | 163 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06628479063510895 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 173 | SELL | FAST8 | 91.0 | 6 | 163 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 3 | 5-2 | 174 | BUY | FAST8 | 91.0 | 6 | 168 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8622293472290039 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -— |
| Jogador 3 | 5-2 | 175 | SELL | FAST8 | 91.0 | 6 | 167 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -b0c8ce74-5ce1-4ed0-82ac-f95013475f3c |
| Jogador 3 | 5-3 | 177 | BUY | FAST8 | 91.0 | 7 | 182 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04973626509308815 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 3 | 5-3 | 178 | SELL | FAST8 | 91.0 | 7 | 179 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -1388df2e-8cb4-4e29-8b30-776c29406917 |
| Jogador 3 | 5-3 | 179 | BUY | FAST8 | 91.0 | 7 | 187 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08507661521434784 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -— |
| Jogador 3 | 5-3 | 180 | SELL | FAST8 | 91.0 | 7 | 184 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036816712468862534 | 0.0 | 0.0 | +— / -6722b147-c2a7-4fd0-a943-5036adb3e3a1 |
| Jogador 3 | 5-4 | 182 | BUY | FAST8 | 91.0 | 7 | 200 | 5 | 40.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8273452520370483 | 0.0 | 0.0 | +499f10b9-47ba-4cab-add1-31b452acae6d / -— |
| Jogador 3 | 5-4 | 183 | BUY | FAST8 | 91.0 | 7 | 197 | 5 | 40.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3698597848415375 | 0.0 | 0.0 | +ad363fca-33b7-4257-99d6-7093df66caf6 / -— |
| Jogador 3 | 5-4 | 184 | SELL | FAST8 | 91.0 | 7 | 195 | 5 | 40.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -22f3c707-2635-41cb-a228-10d5ed1883b3 |
| Jogador 3 | 5-4 | 185 | BUY | FAST8 | 91.0 | 7 | 198 | 5 | 40.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01731344312429428 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 3 | 5-5 | 187 | SELL | FAST8 | 91.0 | 7 | 209 | 5 | 40.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027990415692329407 | 0.0 | 0.0 | +— / -908d49c8-626c-44b5-9b03-6a85442f358b |
| Jogador 3 | 5-5 | 188 | BUY | FAST8 | 91.0 | 7 | 211 | 5 | 40.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9489918351173401 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -499f10b9-47ba-4cab-add1-31b452acae6d,a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 3 | 5-5 | 189 | BUY | FAST8 | 91.0 | 7 | 208 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.090012326836586 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 3 | 5-5 | 190 | BUY | FAST8 | 91.0 | 7 | 205 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10303949564695358 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -— |
| Jogador 3 | 5-6 | 192 | SELL | FAST8 | 91.0 | 7 | 214 | 5 | 40.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10783333331346512 | 0.0 | 0.0 | +— / -f0264dc3-6749-4682-929e-fab42383532a |
| Jogador 3 | 5-6 | 193 | BUY | FAST8 | 91.0 | 7 | 222 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3040131628513336 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 3 | 5-6 | 194 | SELL | FAST8 | 91.0 | 7 | 219 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.000366666674381122 | 0.0 | 0.0 | +— / -4e6b6f57-7f94-46ba-b832-c3198d4a5949 |
| Jogador 3 | 5-6 | 195 | BUY | FAST8 | 91.0 | 7 | 222 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10571222007274628 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -— |
| Jogador 3 | 5-7 | 197 | SELL | FAST8 | 91.0 | 7 | 233 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0037137402687221766 | 0.0 | 0.0 | +— / -2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d |
| Jogador 3 | 5-7 | 198 | BUY | FAST8 | 91.0 | 7 | 236 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8656764030456543 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 3 | 5-7 | 199 | SELL | FAST8 | 91.0 | 7 | 235 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01769999973475933 | 0.0 | 0.0 | +— / -1512b230-15a6-405f-9b6b-4387a3091648 |
| Jogador 3 | 5-7 | 200 | BUY | FAST8 | 91.0 | 7 | 240 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8234721422195435 | 0.0 | 0.0 | +dcb61be2-9a58-49bc-9f11-2f5fce42e7ea / -— |
| Jogador 3 | 6-1 | 202 | EQUIP_FROM_INVENTORY | FAST8 | 91.0 | 7 | 250 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.01303293090313673 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 203 | SELL | FAST8 | 91.0 | 7 | 250 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008166667073965073 | 0.0 | 0.0 | +— / -64d87de4-68df-4a72-8b8d-f78039ae4ce5 |
| Jogador 3 | 6-1 | 204 | BUY | FAST8 | 91.0 | 7 | 253 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.190023273229599 | 0.0 | 0.0 | +edd2748e-d629-4a8a-8174-4c1ef3f5f852 / -— |
| Jogador 3 | 6-1 | 205 | SELL | FAST8 | 91.0 | 7 | 250 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5899999737739563 | 0.0 | 0.0 | +— / -ad363fca-33b7-4257-99d6-7093df66caf6 |
| Jogador 3 | 6-2 | 207 | BUY | FAST8 | 91.0 | 7 | 266 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03537968546152115 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -— |
| Jogador 3 | 6-2 | 208 | SELL | FAST8 | 91.0 | 7 | 264 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5293333530426025 | 0.0 | 0.0 | +— / -a267d973-f857-4dda-89e1-209bff42ab6f |
| Jogador 3 | 6-2 | 209 | BUY | FAST8 | 91.0 | 7 | 267 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20303575694561005 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 3 | 6-2 | 210 | SELL | FAST8 | 91.0 | 7 | 264 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004833333194255829 | 0.0 | 0.0 | +— / -2b89bd83-8449-4c63-9da2-62a46c68bdf5 |
| Jogador 3 | 6-3 | 212 | BUY | FAST8 | 91.0 | 7 | 281 | 5 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0090386867523193 | 0.0 | 0.0 | +551e9535-d584-4055-a544-ed78d65ecacb / -4a885bc0-41b4-43f1-94d3-8e755a10645c,ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 |
| Jogador 3 | 6-3 | 213 | BUY | FAST8 | 91.0 | 7 | 279 | 5 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019077474251389503 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 3 | 6-3 | 214 | SELL | FAST8 | 91.0 | 7 | 277 | 5 | 36.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5899999737739563 | 0.0 | 0.0 | +— / -551e9535-d584-4055-a544-ed78d65ecacb |
| Jogador 3 | 6-3 | 215 | MOVE_BENCH | FAST8 | 91.0 | 7 | 282 | 5 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41877955198287964 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 217 | BUY | FAST8 | 91.0 | 7 | 296 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8460068106651306 | 0.0 | 0.0 | +caeaaabc-213a-4018-97f3-8797a0711863 / -— |
| Jogador 3 | 6-4 | 218 | BUY | FAST8 | 91.0 | 7 | 294 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13852326571941376 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -— |
| Jogador 3 | 6-4 | 219 | SELL | FAST8 | 91.0 | 7 | 290 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029484031721949577 | 0.0 | 0.0 | +— / -3c5f5211-f30d-44e7-ac68-0ce513a3d614 |
| Jogador 3 | 6-4 | 220 | BUY | FAST8 | 91.0 | 7 | 292 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09745713323354721 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 3 | 6-5 | 222 | SELL | FAST8 | 91.0 | 7 | 302 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001422631903551519 | 0.0 | 0.0 | +— / -b250e22d-7193-4ea5-879d-5c7b41145719 |
| Jogador 3 | 6-5 | 223 | BUY | FAST8 | 91.0 | 7 | 305 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04453311115503311 | 0.0 | 0.0 | +8faad4f9-9f15-49e8-94af-b4d28879cc0d / -— |
| Jogador 3 | 6-5 | 224 | SELL | FAST8 | 91.0 | 7 | 302 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02983333356678486 | 0.0 | 0.0 | +— / -8faad4f9-9f15-49e8-94af-b4d28879cc0d |
| Jogador 3 | 6-5 | 225 | BUY | FAST8 | 91.0 | 7 | 305 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04113518074154854 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -— |
| Jogador 3 | 6-6 | 227 | SELL | FAST8 | 75.0 | 7 | 313 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028952838853001595 | 0.0 | 0.0 | +— / -27079fe2-8808-47b7-8b10-9fb2834bb6ed |
| Jogador 3 | 6-6 | 228 | BUY | FAST8 | 75.0 | 7 | 315 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18425264954566956 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 3 | 6-6 | 229 | SELL | FAST8 | 75.0 | 7 | 311 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051500000059604645 | 0.0 | 0.0 | +— / -dcb61be2-9a58-49bc-9f11-2f5fce42e7ea |
| Jogador 3 | 6-6 | 230 | BUY | FAST8 | 75.0 | 7 | 314 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030023852363228798 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 3 | 6-7 | 232 | SELL | FAST8 | 59.0 | 7 | 324 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026322079822421074 | 0.0 | 0.0 | +— / -68a0405b-6231-471f-98a5-1661d32f4ac4 |
| Jogador 3 | 6-7 | 233 | BUY | FAST8 | 59.0 | 7 | 325 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07825043052434921 | 0.0 | 0.0 | +2a2b613e-8850-4c70-ab66-bc18356178e8 / -— |
| Jogador 3 | 6-7 | 234 | SELL | FAST8 | 59.0 | 7 | 321 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03720000013709068 | 0.0 | 0.0 | +— / -2a2b613e-8850-4c70-ab66-bc18356178e8 |
| Jogador 3 | 6-7 | 235 | BUY | FAST8 | 59.0 | 7 | 325 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09783665835857391 | 0.0 | 0.0 | +7d8564c6-8151-4e04-b028-2121cb064215 / -— |
| Jogador 3 | 7-1 | 237 | EQUIP_FROM_INVENTORY | FAST8 | 59.0 | 7 | 333 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.029400000348687172 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 238 | SELL | FAST8 | 59.0 | 7 | 333 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.000366666674381122 | 0.0 | 0.0 | +— / -7d8564c6-8151-4e04-b028-2121cb064215 |
| Jogador 3 | 7-1 | 239 | BUY | FAST8 | 59.0 | 7 | 336 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4343869090080261 | 0.0 | 0.0 | +56332309-e8e8-464a-904f-e9253912cd2f / -— |
| Jogador 3 | 7-1 | 240 | SELL | FAST8 | 59.0 | 7 | 335 | 5 | 42.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0570974126458168 | 0.0 | 0.0 | +— / -0a6e3194-ed55-43ad-ac66-31e08ccda7aa |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46534693241119385 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1641255021095276 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0601743720471859 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128427743911743 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3392719626426697 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9801466464996338 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18347884714603424 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 46 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21585871279239655 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 47 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 52 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9552463889122009 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 53 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 54 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 62 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9439225196838379 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 63 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0434540510177612 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 64 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3042444884777069 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 65 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 66 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 67 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10035374760627747 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 69 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3853921592235565 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 71 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13521350920200348 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 72 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 73 | BUY_XP | STABILIZE | 90.0 | 5 | 6 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 74 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 2 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015655194874852896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 75 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5714284181594849 | 0.0 | 0.0 | +— / -57f213f7-34b1-4a4a-8047-afa5e404e5c4 |
| Jogador 4 | 2-4 | 76 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23961131274700165 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 77 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 78 | PASS | STABILIZE | 90.0 | 5 | 3 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 80 | BUY | STABILIZE | 90.0 | 5 | 8 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3509345054626465 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 81 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 10.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3821297287940979 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 82 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 10.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6038581728935242 | 0.0 | 0.0 | +— / -c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 2-6 | 84 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 10.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0534586906433105 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 85 | SELL | STABILIZE | 84.0 | 5 | 10 | 1 | 10.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5679555535316467 | 0.0 | 0.0 | +— / -a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 2-6 | 86 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 10.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 2-6 | 87 | BUY | STABILIZE | 84.0 | 5 | 16 | 1 | 10.0 | Florescer/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1947345733642578 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 88 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 10.0 | Florescer/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13234472274780273 | 0.0 | 0.0 | +— / -b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 2-6 | 89 | SELL | STABILIZE | 84.0 | 5 | 16 | 1 | 10.0 | Florescer/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -814d07bd-0296-44af-9626-26a8a224d86f |
| Jogador 4 | 2-6 | 90 | BUY | STABILIZE | 84.0 | 5 | 17 | 1 | 10.0 | Florescer/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3198799788951874 | 0.0 | 0.0 | +f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 / -— |
| Jogador 4 | 2-7 | 92 | BUY | STABILIZE | 76.0 | 5 | 23 | 2 | 10.0 | Florescer/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.05120849609375 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -— |
| Jogador 4 | 2-7 | 93 | BUY | STABILIZE | 76.0 | 5 | 22 | 2 | 10.0 | Florescer/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1176574230194092 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -eddd35aa-7d38-4d71-8984-e4768f06379e,ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-7 | 94 | BUY_XP | STABILIZE | 76.0 | 5 | 21 | 2 | 8.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0945499986410141 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 95 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 17 | 1 | 8.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2394329309463501 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 96 | BUY | STABILIZE | 76.0 | 6 | 17 | 1 | 10.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3874454200267792 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 97 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 14 | 1 | 10.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39923280477523804 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 99 | BUY | STABILIZE | 76.0 | 6 | 21 | 2 | 12.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8726214170455933 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -4a0403a3-c999-4d4c-83f0-7270e8576aed,9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 3-1 | 100 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 20 | 2 | 8.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3409195840358734 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 102 | BUY | STABILIZE | 67.0 | 6 | 28 | 2 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8733106255531311 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 103 | CRAFT_AND_EQUIP | STABILIZE | 67.0 | 6 | 27 | 2 | 14.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2379813939332962 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 104 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 27 | 2 | 14.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3738798499107361 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 105 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 27 | 2 | 14.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2804812788963318 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 106 | BUY | STABILIZE | 67.0 | 6 | 27 | 2 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3233107626438141 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 107 | MOVE_BENCH | STABILIZE | 67.0 | 6 | 26 | 2 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6000127196311951 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 108 | BUY | STABILIZE | 67.0 | 6 | 26 | 2 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0664665624499321 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-3 | 110 | BUY | STABILIZE | 57.0 | 6 | 32 | 3 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3357495665550232 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-4 | 112 | BUY | STABILIZE | 48.0 | 6 | 42 | 4 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8729329705238342 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 113 | BUY | STABILIZE | 48.0 | 6 | 41 | 4 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7729451656341553 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 114 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 38 | 3 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00017364518134854734 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 115 | BUY | STABILIZE | 48.0 | 6 | 38 | 3 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31187742948532104 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 116 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 36 | 3 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 117 | MOVE_BOARD | STABILIZE | 48.0 | 6 | 36 | 3 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016105636954307556 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 119 | BUY | STABILIZE | 48.0 | 6 | 47 | 4 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8357311487197876 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 120 | BUY | STABILIZE | 48.0 | 6 | 45 | 4 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25543197989463806 | 0.0 | 0.0 | +805375b9-df52-4342-b581-4b92fcd12033 / -— |
| Jogador 4 | 3-6 | 122 | BUY | STABILIZE | 39.0 | 6 | 54 | 5 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8344658017158508 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 123 | SELL | STABILIZE | 39.0 | 6 | 51 | 5 | 22.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -805375b9-df52-4342-b581-4b92fcd12033 |
| Jogador 4 | 3-6 | 124 | BUY | STABILIZE | 39.0 | 6 | 54 | 5 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.910551905632019 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -7fd03119-ac82-49e1-b3bb-3a0caa31011f,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 3-6 | 125 | MOVE_BOARD | STABILIZE | 39.0 | 6 | 52 | 5 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001781567232683301 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 126 | MOVE_BOARD | STABILIZE | 39.0 | 6 | 52 | 5 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 128 | BUY | STABILIZE | 39.0 | 6 | 63 | 5 | 22.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9134323596954346 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-7 | 129 | MOVE_BENCH | STABILIZE | 39.0 | 6 | 60 | 5 | 16.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5858411192893982 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 130 | BUY | STABILIZE | 39.0 | 6 | 60 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04417809471487999 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 4 | 4-1 | 132 | CRAFT_AND_EQUIP | STABILIZE | 39.0 | 6 | 68 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21380899846553802 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 133 | CRAFT_AND_EQUIP | STABILIZE | 39.0 | 6 | 68 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24281050264835358 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 134 | BUY | STABILIZE | 39.0 | 6 | 68 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39709222316741943 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 135 | BUY | STABILIZE | 39.0 | 6 | 67 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6246119141578674 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 4 | 4-1 | 136 | MOVE_BOARD | STABILIZE | 39.0 | 6 | 65 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009321800316683948 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 138 | SELL | STABILIZE | 26.0 | 6 | 75 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -23f4d10f-2614-47b2-bfb2-4fb276764b5e |
| Jogador 4 | 4-2 | 139 | BUY | STABILIZE | 26.0 | 6 | 80 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35546359419822693 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 4 | 4-2 | 140 | MOVE_BOARD | STABILIZE | 26.0 | 6 | 78 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007706463802605867 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 142 | SELL | ALL_IN | 15.0 | 6 | 89 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7084000110626221 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-3 | 143 | BUY | ALL_IN | 15.0 | 6 | 97 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9293949604034424 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 4 | 4-3 | 144 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 95 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002730169566348195 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 145 | SELL | ALL_IN | 15.0 | 6 | 95 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6992999911308289 | 0.0 | 0.0 | +— / -465ecc70-f5da-47f4-a7c0-2005a8ed24c1 |
| Jogador 4 | 4-3 | 146 | BUY | ALL_IN | 15.0 | 6 | 96 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41032737493515015 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 4 | 4-4 | 148 | SELL | ALL_IN | 15.0 | 6 | 104 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6112836003303528 | 0.0 | 0.0 | +— / -421bcbcb-ecb2-4af8-88d4-7be6cd284d27 |
| Jogador 4 | 4-4 | 149 | BUY | ALL_IN | 15.0 | 6 | 107 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0428454875946045 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -3bbd7105-b508-437d-ac84-11e01a499779,4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 4 | 4-4 | 150 | BUY | ALL_IN | 15.0 | 6 | 105 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0423862934112549 | 0.0 | 0.0 | +ea88d306-ae6b-4dbe-b559-3371ba39613a / -210d2415-663d-4768-bbc2-238766c2b863,eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 4 | 4-5 | 152 | BUY | ALL_IN | 15.0 | 6 | 113 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4728591740131378 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 4 | 4-5 | 153 | BUY | ALL_IN | 15.0 | 6 | 111 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058295369148254395 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 4 | 4-5 | 154 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 108 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00045138646964915097 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 155 | BUY | ALL_IN | 15.0 | 6 | 108 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26221197843551636 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -— |
| Jogador 4 | 4-5 | 156 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 105 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00027827106532640755 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 158 | SELL | ALL_IN | 3.0 | 6 | 115 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.738099992275238 | 0.0 | 0.0 | +— / -ea88d306-ae6b-4dbe-b559-3371ba39613a |
| Jogador 4 | 4-6 | 159 | BUY | ALL_IN | 3.0 | 6 | 120 | 5 | 18.0 | Florescer/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9320592284202576 | 0.0 | 0.0 | +51a5a5d7-c5ea-43e2-a521-22fe0275c231 / -— |
| Jogador 4 | 4-6 | 160 | SELL | ALL_IN | 3.0 | 6 | 117 | 5 | 18.0 | Florescer/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.738099992275238 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43023744225502014 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21626177430152893 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3311046063899994 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28997573256492615 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0324440002441406 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1991048902273178 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 46 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21308495104312897 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4089720547199249 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2265952229499817 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 49 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9718320369720459 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 54 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 62 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441315174102783 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12275926768779755 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 65 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2461560219526291 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43634504079818726 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 67 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16283415257930756 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 69 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2578115463256836 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-4 | 71 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3107227683067322 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21753132343292236 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 73 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 74 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08821522444486618 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 76 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1672990918159485 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 77 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07833333313465118 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-4 | 78 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09809103608131409 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-5 | 80 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21031410992145538 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 81 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32201483845710754 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 82 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 84 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25400736927986145 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 85 | SELL | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42199409008026123 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 2-6 | 86 | SELL | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0020810512360185385 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-6 | 87 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008304029703140259 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 88 | SELL | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2823333442211151 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 89 | SELL | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40817776322364807 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-6 | 90 | BUY | STABILIZE | 95.0 | 5 | 11 | 1 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08399112522602081 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-7 | 92 | BUY | STABILIZE | 89.0 | 5 | 16 | 1 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0479344129562378 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-7 | 93 | BUY | STABILIZE | 89.0 | 5 | 15 | 1 | 12.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9719330668449402 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 94 | SELL | STABILIZE | 89.0 | 5 | 14 | 1 | 12.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 95 | BUY | STABILIZE | 89.0 | 5 | 17 | 1 | 12.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03862300515174866 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 96 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 15 | 1 | 12.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44134071469306946 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 97 | SELL | STABILIZE | 89.0 | 5 | 15 | 1 | 18.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04769999906420708 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 3-1 | 99 | BUY | STABILIZE | 89.0 | 6 | 22 | 2 | 18.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5633504390716553 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -— |
| Jogador 5 | 3-1 | 100 | BUY | STABILIZE | 89.0 | 6 | 20 | 2 | 18.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21074001491069794 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-2 | 102 | BUY | STABILIZE | 80.0 | 6 | 25 | 2 | 24.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7508726119995117 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -837b2d09-a207-4830-b36d-29e493bbcc22,ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-2 | 103 | BUY | STABILIZE | 80.0 | 6 | 23 | 2 | 24.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19398511946201324 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 104 | BUY | STABILIZE | 80.0 | 6 | 20 | 2 | 24.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.033331889659166336 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 105 | CRAFT_AND_EQUIP | STABILIZE | 80.0 | 6 | 18 | 1 | 24.0 | Vivaz/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15893356502056122 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 106 | SELL | STABILIZE | 80.0 | 6 | 18 | 1 | 24.0 | Vivaz/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08856899291276932 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-2 | 107 | BUY_XP | STABILIZE | 80.0 | 6 | 23 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 108 | BUY_XP | STABILIZE | 80.0 | 6 | 19 | 1 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 110 | BUY | STABILIZE | 80.0 | 6 | 22 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7325227856636047 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-4 | 112 | BUY | STABILIZE | 70.0 | 6 | 25 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.831279456615448 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 113 | BUY | STABILIZE | 70.0 | 6 | 24 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23480230569839478 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 5 | 3-4 | 114 | SELL | STABILIZE | 70.0 | 6 | 22 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09166666865348816 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-4 | 115 | BUY | STABILIZE | 70.0 | 6 | 24 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0170497614890337 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 116 | SELL | STABILIZE | 70.0 | 6 | 22 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36899998784065247 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-4 | 117 | SELL | STABILIZE | 70.0 | 6 | 24 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43744444847106934 | 0.0 | 0.0 | +— / -46fc5f36-cf3e-422e-89f3-9501ec9d7d12 |
| Jogador 5 | 3-5 | 119 | BUY | STABILIZE | 70.0 | 6 | 33 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3010041117668152 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 5 | 3-5 | 120 | BUY | STABILIZE | 70.0 | 6 | 32 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037116639316082 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-6 | 122 | BUY | STABILIZE | 61.0 | 6 | 37 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8253554105758667 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 123 | SELL | STABILIZE | 61.0 | 6 | 35 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07056666910648346 | 0.0 | 0.0 | +— / -4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 3-6 | 124 | SELL | STABILIZE | 61.0 | 6 | 38 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.551111102104187 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-6 | 125 | BUY | STABILIZE | 61.0 | 6 | 39 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.248361274600029 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 126 | SELL | STABILIZE | 61.0 | 6 | 38 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40817776322364807 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 3-7 | 128 | BUY | STABILIZE | 51.0 | 6 | 48 | 4 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034507978707551956 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 129 | SELL | STABILIZE | 51.0 | 6 | 45 | 4 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3948458433151245 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 3-7 | 130 | BUY | STABILIZE | 51.0 | 6 | 48 | 4 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2150762379169464 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 4-1 | 132 | BUY | STABILIZE | 51.0 | 6 | 55 | 5 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3575785756111145 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 133 | BUY | STABILIZE | 51.0 | 6 | 52 | 5 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3370327949523926 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 5 | 4-1 | 134 | CRAFT_AND_EQUIP | STABILIZE | 51.0 | 6 | 51 | 5 | 24.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20043934881687164 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 135 | CRAFT_AND_EQUIP | STABILIZE | 51.0 | 6 | 51 | 5 | 24.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19030725955963135 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 136 | MOVE_BENCH | STABILIZE | 51.0 | 6 | 51 | 5 | 24.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036862991750240326 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 138 | SELL | STABILIZE | 51.0 | 6 | 62 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028073731809854507 | 0.0 | 0.0 | +— / -f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 5 | 4-2 | 139 | BUY | STABILIZE | 51.0 | 6 | 63 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3258325755596161 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 5 | 4-2 | 140 | SELL | STABILIZE | 51.0 | 6 | 62 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 4-3 | 142 | BUY | STABILIZE | 51.0 | 6 | 77 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8970722556114197 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-3 | 143 | SELL | STABILIZE | 51.0 | 6 | 74 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4587889015674591 | 0.0 | 0.0 | +— / -9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 5 | 4-3 | 144 | BUY | STABILIZE | 51.0 | 6 | 75 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3258315920829773 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 5 | 4-3 | 145 | SELL | STABILIZE | 51.0 | 6 | 74 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4587889015674591 | 0.0 | 0.0 | +— / -333b0a0b-8868-40b2-96e9-71e468c5dd1f |
| Jogador 5 | 4-3 | 146 | SELL | STABILIZE | 51.0 | 6 | 75 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6388999819755554 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 5 | 4-4 | 148 | BUY | STABILIZE | 40.0 | 6 | 88 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9625020027160645 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -750eedbe-93d9-46de-b3b8-a88e41f395f0,a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 4-4 | 149 | MOVE_BENCH | STABILIZE | 40.0 | 6 | 86 | 5 | 18.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4164009094238281 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 150 | BUY | STABILIZE | 40.0 | 6 | 86 | 5 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36132898926734924 | 0.0 | 0.0 | +e4764e13-e26d-4358-980a-c7c625e26726 / -— |
| Jogador 5 | 4-5 | 152 | BUY | STABILIZE | 40.0 | 6 | 95 | 5 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9611877202987671 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -5627d898-cff3-4664-87d1-40a8f3656ab3,ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 4-5 | 153 | MOVE_BENCH | STABILIZE | 40.0 | 6 | 94 | 5 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5704503059387207 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 154 | BUY | STABILIZE | 40.0 | 6 | 94 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08531556278467178 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 5 | 4-5 | 155 | MOVE_BOARD | STABILIZE | 40.0 | 6 | 93 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04259498417377472 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 156 | SELL | STABILIZE | 40.0 | 6 | 93 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6388999819755554 | 0.0 | 0.0 | +— / -b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 5 | 4-6 | 158 | BUY | STABILIZE | 26.0 | 6 | 107 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7160803079605103 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 5 | 4-6 | 159 | BUY | STABILIZE | 26.0 | 6 | 106 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3675921857357025 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 5 | 4-6 | 160 | BUY | STABILIZE | 26.0 | 6 | 103 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019972549751400948 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 5 | 4-7 | 162 | SELL | ALL_IN | 15.0 | 6 | 113 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7045000195503235 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 5 | 4-7 | 163 | BUY | ALL_IN | 15.0 | 6 | 118 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4863791763782501 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -— |
| Jogador 5 | 4-7 | 164 | SELL | ALL_IN | 15.0 | 6 | 117 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.598633348941803 | 0.0 | 0.0 | +— / -f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 5 | 4-7 | 165 | BUY | ALL_IN | 15.0 | 6 | 118 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0284839868545532 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -57d86f23-f167-472f-9878-21dcddc0a5f7,e4764e13-e26d-4358-980a-c7c625e26726 |
| Jogador 5 | 4-7 | 166 | BUY | ALL_IN | 15.0 | 6 | 117 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2264547199010849 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 5 | 5-1 | 168 | BUY | ALL_IN | 15.0 | 7 | 124 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.978266716003418 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 5 | 5-1 | 169 | CRAFT_AND_EQUIP | ALL_IN | 15.0 | 7 | 121 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21555164456367493 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 170 | CRAFT_AND_EQUIP | ALL_IN | 15.0 | 7 | 121 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1983567178249359 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 172 | BUY | ALL_IN | 15.0 | 7 | 132 | 5 | 34.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44563785195350647 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -— |
| Jogador 5 | 5-2 | 173 | SELL | ALL_IN | 15.0 | 7 | 130 | 5 | 34.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6884999871253967 | 0.0 | 0.0 | +— / -943437ce-e190-4790-986b-4e66e49637a7 |
| Jogador 5 | 5-2 | 174 | BUY | ALL_IN | 15.0 | 7 | 133 | 5 | 34.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42906999588012695 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 5 | 5-2 | 175 | SELL | ALL_IN | 15.0 | 7 | 132 | 5 | 34.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -6fb9f857-4ee1-4b52-8825-57f514dc2d0f |
| Jogador 5 | 5-3 | 177 | BUY | ALL_IN | 15.0 | 7 | 145 | 5 | 34.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9655998945236206 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 5 | 5-3 | 178 | SELL | ALL_IN | 15.0 | 7 | 143 | 5 | 34.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 5 | 5-3 | 179 | BUY | ALL_IN | 15.0 | 7 | 147 | 5 | 34.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0509580373764038 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -0f1b15a2-9978-4691-a15e-483ccd03db7f,27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 5 | 5-3 | 180 | BUY | ALL_IN | 15.0 | 7 | 144 | 5 | 28.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042828269302845 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2209876924753189 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0373761653900146 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5750680565834045 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.025546908378601 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 35 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 44 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12904232740402222 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1527068316936493 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 46 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28811851143836975 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 47 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 52 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26156291365623474 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 53 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24635206162929535 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 54 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 55 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 56 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 62 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28903836011886597 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 63 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18041175603866577 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 64 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23842322826385498 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 65 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14490053057670593 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 66 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15178057551383972 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 67 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 71 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.183040589094162 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 72 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.240580216050148 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 73 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8068996667861938 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 74 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 75 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 76 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10962510854005814 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 77 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 78 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4091598689556122 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 80 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8595998287200928 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 81 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2841041684150696 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 82 | SELL | STABILIZE | 83.0 | 5 | 3 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12314929068088531 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-6 | 84 | BUY | STABILIZE | 77.0 | 5 | 11 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7707262635231018 | 0.0 | 0.0 | +53bbd605-d60b-4555-b5e8-29f1cfbb83b4 / -— |
| Jogador 6 | 2-6 | 85 | SELL | STABILIZE | 77.0 | 5 | 9 | 0 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044203441590070724 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-6 | 86 | SELL | STABILIZE | 77.0 | 5 | 11 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43693333864212036 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-6 | 87 | SELL | STABILIZE | 77.0 | 5 | 14 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0201680660247803 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 88 | SELL | STABILIZE | 77.0 | 5 | 15 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5728331208229065 | 0.0 | 0.0 | +— / -908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-6 | 89 | BUY | STABILIZE | 77.0 | 5 | 16 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3466024100780487 | 0.0 | 0.0 | +f5511428-5be8-475d-949c-1d840a0aed4d / -— |
| Jogador 6 | 2-6 | 90 | SELL | STABILIZE | 77.0 | 5 | 15 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5599655508995056 | 0.0 | 0.0 | +— / -f5511428-5be8-475d-949c-1d840a0aed4d |
| Jogador 6 | 2-7 | 92 | SELL | STABILIZE | 72.0 | 5 | 24 | 2 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9004630446434021 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-7 | 93 | BUY | STABILIZE | 72.0 | 5 | 26 | 2 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2854924201965332 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 94 | BUY_XP | STABILIZE | 72.0 | 5 | 23 | 2 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 95 | SELL | STABILIZE | 72.0 | 5 | 19 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10604888945817947 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 2-7 | 96 | BUY_XP | STABILIZE | 72.0 | 5 | 22 | 2 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030220000073313713 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 97 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 18 | 1 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40045782923698425 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 99 | BUY | STABILIZE | 72.0 | 6 | 26 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1045161560177803 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 100 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 6 | 23 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2192787379026413 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 102 | BUY | STABILIZE | 72.0 | 6 | 31 | 3 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8925250768661499 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 103 | BUY | STABILIZE | 72.0 | 6 | 30 | 3 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8121318221092224 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 104 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 29 | 2 | 14.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2400551736354828 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 105 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 29 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3886748254299164 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 29 | 2 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01592494733631611 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 107 | BUY | STABILIZE | 72.0 | 6 | 29 | 2 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014783038757741451 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 6 | 3-2 | 108 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 27 | 2 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3987364172935486 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 110 | BUY | STABILIZE | 62.0 | 6 | 34 | 3 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8564262390136719 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-4 | 112 | BUY | STABILIZE | 62.0 | 6 | 40 | 4 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23453480005264282 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 113 | BUY | STABILIZE | 62.0 | 6 | 36 | 3 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30921199917793274 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-4 | 114 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 33 | 3 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006740673561580479 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 115 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 33 | 3 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016718918457627296 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 116 | BUY_XP | STABILIZE | 62.0 | 6 | 33 | 3 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07949499785900116 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 117 | BUY_XP | STABILIZE | 62.0 | 6 | 29 | 2 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005050000036135316 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 119 | BUY | STABILIZE | 62.0 | 6 | 32 | 3 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7530015707015991 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 120 | SELL | STABILIZE | 62.0 | 6 | 29 | 2 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490000247955322 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-6 | 122 | BUY | STABILIZE | 62.0 | 6 | 42 | 4 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5485924482345581 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 123 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 40 | 4 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03926140069961548 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 124 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 40 | 4 | 24.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41141676902770996 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 125 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 40 | 4 | 24.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32761693000793457 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 126 | PASS | STABILIZE | 62.0 | 6 | 40 | 4 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 128 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 49 | 4 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35055574774742126 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 129 | SELL | STABILIZE | 52.0 | 6 | 49 | 4 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5555999875068665 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-7 | 130 | EQUIP_FROM_INVENTORY | STABILIZE | 52.0 | 6 | 52 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15578892827033997 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 132 | BUY | STABILIZE | 52.0 | 6 | 62 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | True | 0.24715952575206757 | 0.0 | 0.0 | +3d7ba32f-3349-479e-bb6f-9cd1f2006149 / -— |
| Jogador 6 | 4-1 | 133 | CRAFT_AND_EQUIP | STABILIZE | 52.0 | 6 | 61 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.22672857344150543 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 134 | CRAFT_AND_EQUIP | STABILIZE | 52.0 | 6 | 61 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.24980567395687103 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 135 | EQUIP_FROM_INVENTORY | STABILIZE | 52.0 | 6 | 61 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07925136387348175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 136 | EQUIP_FROM_INVENTORY | STABILIZE | 52.0 | 6 | 61 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08922143280506134 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 138 | BUY | STABILIZE | 52.0 | 6 | 72 | 5 | 22.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0106264352798462 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -43da0d73-facd-488b-b856-94e9496a97f9,ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b |
| Jogador 6 | 4-2 | 139 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 69 | 5 | 16.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.360201358795166 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 140 | BUY | STABILIZE | 52.0 | 6 | 69 | 5 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10760244727134705 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 6 | 4-3 | 142 | BUY | STABILIZE | 41.0 | 6 | 77 | 5 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8979485034942627 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 6 | 4-3 | 143 | BUY | STABILIZE | 41.0 | 6 | 75 | 5 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22036154568195343 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 144 | SELL | STABILIZE | 41.0 | 6 | 71 | 5 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6453999876976013 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 6 | 4-3 | 145 | BUY | STABILIZE | 41.0 | 6 | 79 | 5 | 18.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18552106618881226 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 6 | 4-3 | 146 | SELL | STABILIZE | 41.0 | 6 | 78 | 5 | 18.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3629666566848755 | 0.0 | 0.0 | +— / -a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 6 | 4-4 | 148 | BUY | STABILIZE | 30.0 | 6 | 90 | 5 | 18.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35787320137023926 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 6 | 4-4 | 149 | BUY | STABILIZE | 30.0 | 6 | 89 | 5 | 18.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20961277186870575 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 6 | 4-4 | 150 | SELL | STABILIZE | 30.0 | 6 | 86 | 5 | 18.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03336767852306366 | 0.0 | 0.0 | +— / -ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 6 | 4-5 | 152 | BUY | STABILIZE | 30.0 | 6 | 99 | 5 | 18.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9612980484962463 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -3cb4d077-df9a-4fd2-9a68-7301aff1b657,3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 4-5 | 153 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 98 | 5 | 14.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13257579505443573 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 154 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 98 | 5 | 16.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13917331397533417 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 155 | BUY | STABILIZE | 30.0 | 6 | 98 | 5 | 18.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15415506064891815 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 6 | 4-5 | 156 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 97 | 5 | 18.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5048555731773376 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 158 | BUY | STABILIZE | 30.0 | 7 | 108 | 5 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8994776010513306 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 6 | 4-6 | 159 | SELL | STABILIZE | 30.0 | 7 | 104 | 5 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030857237055897713 | 0.0 | 0.0 | +— / -a72137b3-498b-40e1-938a-639f56745f08 |
| Jogador 6 | 4-6 | 160 | BUY | STABILIZE | 30.0 | 7 | 105 | 5 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0010298173874616623 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 6 | 4-7 | 162 | BUY | STABILIZE | 30.0 | 7 | 115 | 5 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37002524733543396 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 6 | 4-7 | 163 | SELL | STABILIZE | 30.0 | 7 | 112 | 5 | 32.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -565ff610-fe51-470b-8452-a7eec5e31653 |
| Jogador 6 | 4-7 | 164 | BUY | STABILIZE | 30.0 | 7 | 114 | 5 | 32.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8070043921470642 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930,9204a42c-6310-4b08-9bc7-8a2e786b077a |
| Jogador 6 | 4-7 | 165 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 112 | 5 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1777159422636032 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 166 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 112 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32934609055519104 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 168 | BUY | STABILIZE | 30.0 | 7 | 123 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.018113613128662 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -53bbd605-d60b-4555-b5e8-29f1cfbb83b4,badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 6 | 5-1 | 169 | BUY | STABILIZE | 30.0 | 7 | 121 | 5 | 30.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.057614609599113464 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 6 | 5-1 | 170 | CRAFT_AND_EQUIP | STABILIZE | 30.0 | 7 | 117 | 5 | 30.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12673558294773102 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 172 | BUY | ALL_IN | 13.0 | 7 | 127 | 5 | 38.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15099084377288818 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 6 | 5-2 | 173 | CRAFT_AND_EQUIP | ALL_IN | 13.0 | 7 | 126 | 5 | 38.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12954644858837128 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 174 | SELL | ALL_IN | 13.0 | 7 | 126 | 5 | 38.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7074999809265137 | 0.0 | 0.0 | +— / -61362365-2cf7-40e4-95f9-98e28728fd39 |
| Jogador 6 | 5-2 | 175 | BUY | ALL_IN | 13.0 | 7 | 129 | 5 | 38.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.01514297816902399 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 12 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40457043051719666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.048290491104126 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23154349625110626 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368651151657104 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24602721631526947 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 38 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8270328044891357 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.199772447347641 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 46 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24544134736061096 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 47 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30101802945137024 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475703477859497 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1544678807258606 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 55 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1789994239807129 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 56 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 58 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-2 | 59 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11028651148080826 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 60 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.153961181640625 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 62 | BUY | STABILIZE | 94.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047542691230774 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 63 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6460407972335815 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17267242074012756 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 65 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09771763533353806 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 66 | SELL | STABILIZE | 94.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6187133193016052 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-3 | 67 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14203839004039764 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 68 | BUY_XP | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 69 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17471009492874146 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 71 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31527775526046753 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 72 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25737327337265015 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 73 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 78 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42251119017601013 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 80 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2896921634674072 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 81 | BUY | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3140585422515869 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 82 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 2 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005171899683773518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 84 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9130241274833679 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 85 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8853545188903809 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 86 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 87 | SELL | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00286666676402092 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-6 | 88 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001097780535928905 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 89 | SELL | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47992879152297974 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-6 | 90 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 92 | BUY | STABILIZE | 94.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2672014832496643 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 93 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03353499993681908 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 94 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0023797324392944574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 95 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4827854335308075 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 96 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014133737422525883 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 97 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014736984856426716 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 99 | BUY | STABILIZE | 94.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28452590107917786 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 100 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18571749329566956 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 102 | BUY | STABILIZE | 94.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20169596374034882 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 103 | BUY_XP | STABILIZE | 94.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 104 | BUY_XP | STABILIZE | 94.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 105 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 110 | SELL | STABILIZE | 94.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013369838707149029 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 3-4 | 112 | BUY | STABILIZE | 94.0 | 6 | 19 | 1 | 30.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379950523376465 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -4e206e09-40e3-4699-81cb-8aaf01109dea,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 3-4 | 113 | BUY | STABILIZE | 94.0 | 6 | 18 | 1 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8312209844589233 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 114 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09939657151699066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 115 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 15 | 1 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13822166621685028 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 116 | BUY | STABILIZE | 94.0 | 6 | 15 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10843814164400101 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 117 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 12 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5241961479187012 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 119 | BUY | STABILIZE | 94.0 | 6 | 21 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.800171434879303 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 120 | BUY | STABILIZE | 94.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5199185013771057 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-6 | 122 | SELL | STABILIZE | 94.0 | 6 | 27 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -1ff50c59-5133-459e-8bf1-d449c26efabf |
| Jogador 7 | 3-6 | 123 | BUY | STABILIZE | 94.0 | 6 | 30 | 3 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.6534507870674133 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 124 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 6 | 27 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15643392503261566 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 125 | EQUIP_FROM_INVENTORY | STABILIZE | 94.0 | 6 | 27 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11614015698432922 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 126 | BUY_XP | STABILIZE | 94.0 | 6 | 27 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011656000278890133 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 128 | SELL | STABILIZE | 94.0 | 6 | 34 | 3 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 3-7 | 129 | BUY | STABILIZE | 94.0 | 6 | 42 | 4 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18604610860347748 | 0.0 | 0.0 | +06fb62e5-6766-4156-bf7d-0da443a9b20c / -— |
| Jogador 7 | 3-7 | 130 | SELL | STABILIZE | 94.0 | 6 | 39 | 3 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3086666762828827 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 4-1 | 132 | BUY | STABILIZE | 94.0 | 6 | 54 | 5 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.34805217385292053 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -— |
| Jogador 7 | 4-1 | 133 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 52 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.03951982781291008 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 134 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 6 | 52 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12444260716438293 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 135 | SELL | STABILIZE | 94.0 | 6 | 52 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -06fb62e5-6766-4156-bf7d-0da443a9b20c |
| Jogador 7 | 4-1 | 136 | BUY | STABILIZE | 94.0 | 6 | 55 | 5 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011696554720401764 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-2 | 138 | SELL | STABILIZE | 94.0 | 6 | 67 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00821271538734436 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-2 | 139 | BUY | STABILIZE | 94.0 | 6 | 69 | 5 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8675439953804016 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 7 | 4-2 | 140 | SELL | STABILIZE | 94.0 | 6 | 67 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47438767552375793 | 0.0 | 0.0 | +— / -86c1ac55-598e-426a-86ea-64249f82b085 |
| Jogador 7 | 4-3 | 142 | BUY | STABILIZE | 94.0 | 6 | 84 | 5 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10611292719841003 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 143 | SELL | STABILIZE | 94.0 | 6 | 80 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029130633920431137 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-3 | 144 | BUY | STABILIZE | 94.0 | 6 | 83 | 5 | 32.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11945445090532303 | 0.0 | 0.0 | +f5cca112-4fa0-4ee6-a863-20a5d49ab7ef / -— |
| Jogador 7 | 4-3 | 145 | BUY_XP | STABILIZE | 94.0 | 6 | 81 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37285876274108887 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 146 | MOVE_BENCH | STABILIZE | 94.0 | 7 | 77 | 5 | 32.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4870568811893463 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 148 | BUY | STABILIZE | 94.0 | 7 | 91 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8798080086708069 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 7 | 4-4 | 149 | MOVE_BOARD | STABILIZE | 94.0 | 7 | 88 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004597194492816925 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 150 | SELL | STABILIZE | 94.0 | 7 | 88 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050200000405311584 | 0.0 | 0.0 | +— / -f5cca112-4fa0-4ee6-a863-20a5d49ab7ef |
| Jogador 7 | 4-5 | 152 | BUY | STABILIZE | 94.0 | 7 | 103 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12237916141748428 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 7 | 4-5 | 153 | SELL | STABILIZE | 94.0 | 7 | 99 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 7 | 4-5 | 154 | BUY | STABILIZE | 94.0 | 7 | 103 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1934901624917984 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -— |
| Jogador 7 | 4-5 | 155 | SELL | STABILIZE | 94.0 | 7 | 101 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05264115333557129 | 0.0 | 0.0 | +— / -31ea6d79-501d-4f2a-821d-7058334be82f |
| Jogador 7 | 4-5 | 156 | BUY | STABILIZE | 94.0 | 7 | 103 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19982387125492096 | 0.0 | 0.0 | +b82f90f3-6914-4db5-bc7c-74543cf91aef / -— |
| Jogador 7 | 4-6 | 158 | SELL | STABILIZE | 94.0 | 7 | 115 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05305790901184082 | 0.0 | 0.0 | +— / -b82f90f3-6914-4db5-bc7c-74543cf91aef |
| Jogador 7 | 4-6 | 159 | BUY | STABILIZE | 94.0 | 7 | 117 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9471094608306885 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,d69fa0dc-74b6-4ee7-90f7-aaca5405c59c |
| Jogador 7 | 4-6 | 160 | BUY | STABILIZE | 94.0 | 7 | 114 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37960416078567505 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 7 | 4-7 | 162 | BUY | STABILIZE | 94.0 | 7 | 127 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8937587738037109 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 7 | 4-7 | 163 | SELL | STABILIZE | 94.0 | 7 | 125 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5256115794181824 | 0.0 | 0.0 | +— / -4aa5d560-d9d3-45f9-802a-bdbe95788762 |
| Jogador 7 | 4-7 | 164 | BUY | STABILIZE | 94.0 | 7 | 133 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1842947155237198 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 7 | 4-7 | 165 | MOVE_BOARD | STABILIZE | 94.0 | 7 | 130 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017794016748666763 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 166 | SELL | STABILIZE | 94.0 | 7 | 130 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00024938586284406483 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 7 | 5-1 | 168 | BUY | STABILIZE | 94.0 | 7 | 147 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08548746258020401 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 7 | 5-1 | 169 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 7 | 145 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14273039996623993 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 170 | CRAFT_AND_EQUIP | STABILIZE | 94.0 | 7 | 145 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13477888703346252 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 172 | SELL | STABILIZE | 94.0 | 7 | 159 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03160950168967247 | 0.0 | 0.0 | +— / -ff181737-4995-4a67-add2-4f55cebabbee |
| Jogador 7 | 5-2 | 173 | BUY | STABILIZE | 94.0 | 7 | 161 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08558154851198196 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 7 | 5-2 | 174 | SELL | STABILIZE | 94.0 | 7 | 159 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03157418593764305 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 7 | 5-2 | 175 | BUY | STABILIZE | 94.0 | 7 | 161 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019029226154088974 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 7 | 5-3 | 177 | SELL | STABILIZE | 94.0 | 7 | 172 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 7 | 5-3 | 178 | BUY | STABILIZE | 94.0 | 7 | 175 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23110584914684296 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 7 | 5-3 | 179 | SELL | STABILIZE | 94.0 | 7 | 172 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -af404167-469a-447e-b415-dcb52033ef9b |
| Jogador 7 | 5-3 | 180 | BUY | STABILIZE | 94.0 | 7 | 175 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003632904961705208 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -— |
| Jogador 7 | 5-4 | 182 | SELL | STABILIZE | 94.0 | 7 | 187 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -a899fe97-90e4-4ae3-941c-af3dee48fed3 |
| Jogador 7 | 5-4 | 183 | BUY | STABILIZE | 94.0 | 7 | 188 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3755458891391754 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 7 | 5-4 | 184 | SELL | STABILIZE | 94.0 | 7 | 185 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -80130f72-2d7c-49db-8d6f-4c0a962260e8 |
| Jogador 7 | 5-4 | 185 | BUY | STABILIZE | 94.0 | 7 | 188 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1098136380314827 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 7 | 5-5 | 187 | SELL | STABILIZE | 94.0 | 7 | 197 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037237681448459625 | 0.0 | 0.0 | +— / -d8392323-28e4-4e98-a466-5958bf400729 |
| Jogador 7 | 5-5 | 188 | BUY | STABILIZE | 94.0 | 7 | 201 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017726607620716095 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 7 | 5-5 | 189 | SELL | STABILIZE | 94.0 | 7 | 198 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019433332607150078 | 0.0 | 0.0 | +— / -95eba9e8-10f5-48d5-86de-3d9a446b2e65 |
| Jogador 7 | 5-5 | 190 | BUY | STABILIZE | 94.0 | 7 | 201 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004372118040919304 | 0.0 | 0.0 | +eb418af1-c963-4da2-b052-86a153fc5ba1 / -— |
| Jogador 7 | 5-6 | 192 | SELL | STABILIZE | 80.0 | 7 | 209 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012379610911011696 | 0.0 | 0.0 | +— / -eb418af1-c963-4da2-b052-86a153fc5ba1 |
| Jogador 7 | 5-6 | 193 | BUY | STABILIZE | 80.0 | 7 | 211 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0938064232468605 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 7 | 5-6 | 194 | SELL | STABILIZE | 80.0 | 7 | 208 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031132960692048073 | 0.0 | 0.0 | +— / -f6000a82-1241-4220-9362-c8d788472db0 |
| Jogador 7 | 5-6 | 195 | BUY | STABILIZE | 80.0 | 7 | 211 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015130198560655117 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -— |
| Jogador 7 | 5-7 | 197 | SELL | STABILIZE | 66.0 | 7 | 219 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016833333298563957 | 0.0 | 0.0 | +— / -3329c812-11fa-4335-a982-f03e6ab28ee0 |
| Jogador 7 | 5-7 | 198 | BUY | STABILIZE | 66.0 | 7 | 222 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0199377536773682 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4,599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 5-7 | 199 | MOVE_BENCH | STABILIZE | 66.0 | 7 | 219 | 5 | 22.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3494036793708801 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 200 | BUY | STABILIZE | 66.0 | 7 | 219 | 5 | 34.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1627810299396515 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 7 | 6-1 | 202 | BUY | FAST8 | 66.0 | 7 | 227 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.0733860656619072 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 7 | 6-1 | 203 | EQUIP_FROM_INVENTORY | FAST8 | 66.0 | 7 | 224 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.147104874253273 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 204 | MOVE_BOARD | FAST8 | 66.0 | 7 | 224 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006097951554693282 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 205 | MOVE_BOARD | FAST8 | 66.0 | 7 | 224 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 207 | SELL | FAST8 | 50.0 | 7 | 235 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016833333298563957 | 0.0 | 0.0 | +— / -efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 7 | 6-2 | 208 | BUY | FAST8 | 50.0 | 7 | 238 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0098822116851807 | 0.0 | 0.0 | +83a3ef65-b342-4ec8-b2d1-be99c3602f81 / -033a84d9-70f6-46a8-a6eb-a2f03be70400,bcd06176-e1d7-43fb-abd4-b6faea8c7927 |
| Jogador 7 | 6-2 | 209 | SELL | STABILIZE | 50.0 | 7 | 236 | 5 | 30.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5899999737739563 | 0.0 | 0.0 | +— / -83a3ef65-b342-4ec8-b2d1-be99c3602f81 |
| Jogador 7 | 6-2 | 210 | BUY | STABILIZE | 50.0 | 7 | 241 | 5 | 30.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.079024076461792 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -42f739bb-e676-4a27-a96f-c09d09d592bb,caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 6-3 | 212 | BUY | STABILIZE | 33.0 | 7 | 251 | 5 | 32.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5299915671348572 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 7 | 6-3 | 213 | BUY | STABILIZE | 33.0 | 7 | 248 | 5 | 32.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15623611211776733 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 7 | 6-3 | 214 | MOVE_BENCH | STABILIZE | 33.0 | 7 | 245 | 5 | 32.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14956694841384888 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 215 | MOVE_BENCH | STABILIZE | 33.0 | 7 | 245 | 5 | 38.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5746575593948364 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 217 | BUY | ALL_IN | 17.0 | 7 | 257 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9527343511581421 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 7 | 6-4 | 218 | BUY | ALL_IN | 17.0 | 7 | 254 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029200630262494087 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 7 | 6-4 | 219 | MOVE_BOARD | ALL_IN | 17.0 | 7 | 252 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003946380224078894 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 220 | SELL | ALL_IN | 17.0 | 7 | 252 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01119999960064888 | 0.0 | 0.0 | +— / -1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 7 | 6-5 | 222 | BUY | ALL_IN | 17.0 | 7 | 266 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1087453365325928 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -cc56fedc-f555-4075-af15-6b5fb93a156f,f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 7 | 6-5 | 223 | BUY | ALL_IN | 17.0 | 7 | 264 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1163177415728569 | 0.0 | 0.0 | +b58c0c0e-9c6f-4977-91d1-177b7113c439 / -— |
| Jogador 7 | 6-5 | 224 | BUY | ALL_IN | 17.0 | 7 | 263 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22167454659938812 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 7 | 6-5 | 225 | SELL | ALL_IN | 17.0 | 7 | 260 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6923999786376953 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 7 | 6-6 | 227 | BUY | ALL_IN | 17.0 | 7 | 276 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0382235050201416 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 7 | 6-6 | 228 | SELL | ALL_IN | 17.0 | 7 | 273 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003100000089034438 | 0.0 | 0.0 | +— / -7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 |
| Jogador 7 | 6-6 | 229 | BUY | ALL_IN | 17.0 | 7 | 276 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9689984917640686 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 7 | 6-6 | 230 | SELL | ALL_IN | 17.0 | 7 | 273 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051500000059604645 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 7 | 6-7 | 232 | BUY | ALL_IN | 17.0 | 7 | 288 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10613705962896347 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 7 | 6-7 | 233 | SELL | ALL_IN | 17.0 | 7 | 285 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02983333356678486 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 7 | 6-7 | 234 | BUY | ALL_IN | 17.0 | 7 | 288 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029443737119436264 | 0.0 | 0.0 | +e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 / -— |
| Jogador 7 | 6-7 | 235 | SELL | ALL_IN | 17.0 | 7 | 286 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014104699715971947 | 0.0 | 0.0 | +— / -e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 |
| Jogador 7 | 7-1 | 237 | BUY | ALL_IN | 17.0 | 7 | 299 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7364252805709839 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -— |
| Jogador 7 | 7-1 | 238 | EQUIP_FROM_INVENTORY | ALL_IN | 17.0 | 7 | 296 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07383698970079422 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 239 | SELL | ALL_IN | 17.0 | 7 | 296 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09666985273361206 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 7-1 | 240 | BUY | ALL_IN | 17.0 | 7 | 299 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028759321197867393 | 0.0 | 0.0 | +9af00d66-f862-45b7-98d4-93fbd69fedba / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.50416499376297 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0143887996673584 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3602963089942932 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 34 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2829146087169647 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9772524833679199 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 36 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17354188859462738 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 37 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2519603669643402 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 38 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11602501571178436 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 39 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1140997409820557 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 45 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2013683319091797 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 46 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17967553436756134 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05705181881785393 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1034897565841675 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 49 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12450948357582092 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 50 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03433627262711525 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-2 | 52 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2576543688774109 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 53 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21270792186260223 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 54 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18157482147216797 | 0.0 | 0.0 | +ebe77c97-f249-4265-ae03-bc8115a4795f / -— |
| Jogador 8 | 2-2 | 55 | SELL | STABILIZE | 94.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045099999755620956 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 56 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05884593725204468 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1110355481505394 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 58 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5152862071990967 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04943377897143364 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 60 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15070758759975433 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 62 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9806419014930725 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 63 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9497092962265015 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-3 | 64 | BUY | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33042365312576294 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 65 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17664414644241333 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 66 | BUY | STABILIZE | 90.0 | 4 | 3 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2651914060115814 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4303278923034668 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 0 | 0 | 16.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2268577367067337 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 69 | SELL | STABILIZE | 90.0 | 4 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2180197387933731 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-4 | 71 | BUY | STABILIZE | 90.0 | 4 | 9 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.862350344657898 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 72 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1591462343931198 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 73 | SELL | STABILIZE | 90.0 | 4 | 5 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-4 | 74 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1740427166223526 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 75 | BUY_XP | STABILIZE | 90.0 | 4 | 6 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 76 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07779882103204727 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 77 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01148142945021391 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 78 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044288020581007004 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 80 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.898149847984314 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 81 | SELL | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010300000198185444 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-5 | 82 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.539276659488678 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-6 | 84 | SELL | STABILIZE | 84.0 | 5 | 9 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058064814656972885 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-6 | 85 | BUY | STABILIZE | 84.0 | 5 | 10 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.817219614982605 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 86 | SELL | STABILIZE | 84.0 | 5 | 9 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0684666633605957 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-6 | 87 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047675758600234985 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 88 | SELL | STABILIZE | 84.0 | 5 | 8 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03741229325532913 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 2-6 | 89 | BUY | STABILIZE | 84.0 | 5 | 10 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042827535420656204 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 90 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 7 | 0 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033600810915231705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 92 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008233333006501198 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-7 | 93 | BUY | STABILIZE | 84.0 | 5 | 16 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8696848154067993 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 94 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006910842843353748 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 2-7 | 95 | BUY | STABILIZE | 84.0 | 5 | 16 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04865706339478493 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 96 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024700000882148743 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 97 | BUY | STABILIZE | 84.0 | 5 | 16 | 1 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0933389887213707 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 3-1 | 99 | CRAFT_AND_EQUIP | STABILIZE | 84.0 | 5 | 21 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1437370330095291 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 100 | SELL | STABILIZE | 84.0 | 5 | 21 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003431178629398346 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-2 | 102 | BUY | STABILIZE | 84.0 | 5 | 31 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1849699169397354 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 103 | SELL | STABILIZE | 84.0 | 5 | 27 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05491926521062851 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 3-2 | 104 | BUY | STABILIZE | 84.0 | 5 | 30 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10731791704893112 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 105 | SELL | STABILIZE | 84.0 | 5 | 29 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0769248828291893 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 106 | BUY | STABILIZE | 84.0 | 5 | 30 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15724463760852814 | 0.0 | 0.0 | +655deca9-2d3f-4e88-827a-5f49da8f3451 / -— |
| Jogador 8 | 3-2 | 107 | SELL | STABILIZE | 84.0 | 5 | 28 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09220756590366364 | 0.0 | 0.0 | +— / -655deca9-2d3f-4e88-827a-5f49da8f3451 |
| Jogador 8 | 3-2 | 108 | BUY | STABILIZE | 84.0 | 5 | 30 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33260321617126465 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 8 | 3-3 | 110 | SELL | STABILIZE | 84.0 | 5 | 37 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 8 | 3-4 | 112 | BUY | STABILIZE | 75.0 | 5 | 47 | 4 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8829067349433899 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -5de56114-806a-4f58-8241-b3b8434a2154,b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 3-4 | 113 | BUY | STABILIZE | 75.0 | 5 | 46 | 4 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8785639405250549 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -3644801e-2247-403d-8b81-d2d3f15c2f55,ebe77c97-f249-4265-ae03-bc8115a4795f |
| Jogador 8 | 3-4 | 114 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 45 | 4 | 12.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3124929368495941 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 115 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 45 | 4 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5358185768127441 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 116 | BUY | STABILIZE | 75.0 | 5 | 45 | 4 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26041164994239807 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 117 | BUY | STABILIZE | 75.0 | 5 | 42 | 4 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08024337142705917 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-5 | 119 | BUY | STABILIZE | 75.0 | 5 | 49 | 4 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8388872742652893 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 120 | SELL | STABILIZE | 75.0 | 5 | 46 | 4 | 20.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5449901223182678 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-6 | 122 | BUY | STABILIZE | 66.0 | 5 | 59 | 5 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8989151120185852 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 3-6 | 123 | BUY | STABILIZE | 66.0 | 5 | 58 | 5 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07683561742305756 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 124 | SELL | STABILIZE | 66.0 | 5 | 54 | 5 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4900984764099121 | 0.0 | 0.0 | +— / -b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 8 | 3-6 | 125 | EQUIP_FROM_INVENTORY | STABILIZE | 66.0 | 5 | 57 | 5 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14714272320270538 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 126 | MOVE_BENCH | STABILIZE | 66.0 | 5 | 57 | 5 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.467672735452652 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 128 | BUY | STABILIZE | 54.0 | 6 | 68 | 5 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3350197374820709 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 129 | BUY | STABILIZE | 54.0 | 6 | 67 | 5 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.06208323314785957 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 130 | EQUIP_FROM_INVENTORY | STABILIZE | 54.0 | 6 | 64 | 5 | 22.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13774259388446808 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 132 | BUY | STABILIZE | 54.0 | 6 | 75 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | True | 0.9045203328132629 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 8 | 4-1 | 133 | EQUIP_FROM_INVENTORY | STABILIZE | 54.0 | 6 | 74 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.08077894896268845 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 134 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 6 | 74 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2456791251897812 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 135 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 6 | 74 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08933335542678833 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 136 | SELL | STABILIZE | 54.0 | 6 | 74 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 4-2 | 138 | BUY | STABILIZE | 43.0 | 6 | 87 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2370089739561081 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 139 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 83 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 140 | MOVE_BOARD | STABILIZE | 43.0 | 6 | 83 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08802211284637451 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 142 | SELL | STABILIZE | 32.0 | 6 | 95 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 4-3 | 143 | BUY | STABILIZE | 32.0 | 6 | 98 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3459297716617584 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -— |
| Jogador 8 | 4-3 | 144 | SELL | STABILIZE | 32.0 | 6 | 96 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -08a36d54-bb5c-48a6-afb1-e0f9943bf069 |
| Jogador 8 | 4-3 | 145 | BUY | STABILIZE | 32.0 | 6 | 100 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17913085222244263 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 146 | MOVE_BOARD | STABILIZE | 32.0 | 6 | 97 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1522292196750641 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 148 | SELL | ALL_IN | 18.0 | 6 | 110 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02864641696214676 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 8 | 4-4 | 149 | BUY | ALL_IN | 18.0 | 6 | 113 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9142774343490601 | 0.0 | 0.0 | +7b49fb38-6e0e-4a72-a2ce-0527827d36a6 / -— |
| Jogador 8 | 4-4 | 150 | SELL | ALL_IN | 18.0 | 6 | 111 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05045539513230324 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 4-5 | 152 | BUY | ALL_IN | 18.0 | 6 | 127 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0296012163162231 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -579b987a-fedf-45d8-92fc-634a041d3d4f,7b49fb38-6e0e-4a72-a2ce-0527827d36a6 |
| Jogador 8 | 4-5 | 153 | BUY | ALL_IN | 18.0 | 6 | 125 | 5 | 24.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8826691508293152 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -87600495-fe90-4832-ab42-9a5cb0ebe3f4,d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-5 | 154 | REROLL | ALL_IN | 18.0 | 6 | 122 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 155 | BUY | ALL_IN | 18.0 | 6 | 120 | 5 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0995323657989502 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -9af097e2-729d-474a-9a7e-b266c665c606,b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 4-5 | 156 | MOVE_BENCH | ALL_IN | 18.0 | 6 | 117 | 5 | 18.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5827474594116211 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 158 | BUY | ALL_IN | 6.0 | 6 | 130 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03394065052270889 | 0.0 | 0.0 | +06332ba7-fc4e-431e-ab25-2fb284c08c33 / -— |
| Jogador 8 | 4-6 | 159 | BUY | ALL_IN | 6.0 | 6 | 127 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.277102530002594 | 0.0 | 0.0 | +590d07db-5e90-4705-a7ae-96f84fd06382 / -— |
| Jogador 8 | 4-6 | 160 | BUY | ALL_IN | 6.0 | 6 | 124 | 5 | 20.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2818545699119568 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 111 | 49 | 3 | 3 | 0 | 1 | 0 | 126 | 28.0 |
- Jogador 1 — gasto por ação: BUY: 89g, BUY_XP: 20g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 47g, stage 3: 21g, stage 4: 32g, stage 5: 5g
| Jogador 2 | 124 | 135 | 47 | 5 | 7 | 1 | 1 | 0 | 81 | 36.0 |
- Jogador 2 — gasto por ação: BUY: 97g, BUY_XP: 36g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 53g, stage 3: 42g, stage 4: 21g, stage 5: 12g
| Jogador 3 | 169 | 165 | 104 | 2 | 4 | 1 | 0 | 0 | 339 | 42.0 |
- Jogador 3 — gasto por ação: BUY: 145g, BUY_XP: 20g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 16g, stage 4: 19g, stage 5: 38g, stage 6: 38g, stage 7: 1g
| Jogador 4 | 108 | 107 | 53 | 2 | 3 | 1 | 0 | 0 | 122 | 18.0 |
- Jogador 4 — gasto por ação: BUY: 87g, BUY_XP: 20g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 28g, stage 4: 25g
| Jogador 5 | 122 | 129 | 65 | 7 | 5 | 0 | 0 | 0 | 141 | 28.0 |
- Jogador 5 — gasto por ação: BUY: 105g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 43g, stage 3: 40g, stage 4: 25g, stage 5: 14g
| Jogador 6 | 117 | 122 | 45 | 7 | 6 | 0 | 0 | 0 | 126 | 38.0 |
- Jogador 6 — gasto por ação: BUY: 94g, BUY_XP: 28g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 47g, stage 3: 30g, stage 4: 30g, stage 5: 10g
| Jogador 7 | 174 | 202 | 115 | 4 | 6 | 0 | 0 | 0 | 295 | 44.0 |
- Jogador 7 — gasto por ação: BUY: 166g, BUY_XP: 36g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 50g, stage 3: 34g, stage 4: 36g, stage 5: 35g, stage 6: 34g, stage 7: 7g
| Jogador 8 | 117 | 111 | 54 | 7 | 0 | 0 | 1 | 0 | 122 | 20.0 |
- Jogador 8 — gasto por ação: BUY: 105g, BUY_XP: 4g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 28g, stage 4: 30g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 5 | 4 |
- Jogador 1 · 2-7 · step 96: PASS com 4g, HP 93, nível 6/8 (STABILIZE).
- Jogador 1 · 3-4 · step 116: PASS com 15g, HP 62, nível 6/8 (STABILIZE).
- Jogador 1 · 3-6 · step 126: PASS com 24g, HP 62, nível 6/8 (STABILIZE).
- Jogador 1 · 4-7 · step 165: REROLL com 102g, HP 17, nível 6/8 (ALL_IN).
| Jogador 2 | 9 | 2 |
- Jogador 2 · 4-5 · step 155: PASS com 39g, HP 28, nível 7/8 (STABILIZE).
- Jogador 2 · 5-2 · step 175: REROLL com 83g, HP 13, nível 7/8 (ALL_IN).
| Jogador 3 | 5 | 4 |
- Jogador 3 · 3-2 · step 107: PASS com 16g, HP 100, nível 6/8 (STABILIZE).
- Jogador 3 · 3-4 · step 116: PASS com 30g, HP 100, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 130: PASS com 62g, HP 91, nível 6/8 (STABILIZE).
- Jogador 3 · 4-3 · step 144: PASS com 97g, HP 91, nível 6/8 (STABILIZE).
| Jogador 4 | 5 | 0 |
| Jogador 5 | 6 | 0 |
| Jogador 6 | 7 | 1 |
- Jogador 6 · 3-6 · step 126: PASS com 40g, HP 62, nível 6/8 (STABILIZE).
| Jogador 7 | 9 | 0 |
| Jogador 8 | 1 | 1 |
- Jogador 8 · 4-5 · step 154: REROLL com 122g, HP 18, nível 6/8 (ALL_IN).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 3 | 3 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 3 | 3 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 122 | 26 | 23 | 73 | 0.0056 | 0.1077 | 0.0027 | 0.2778 | 0.0029 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0144 (45 ações), BUY_XP: Δ 0.0142 (5 ações), CRAFT_AND_EQUIP: Δ 0.0063 (7 ações), MOVE_BENCH: Δ -0.0035 (15 ações), MOVE_BOARD: Δ 0.0598 (18 ações), PASS: Δ 0.0000 (12 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0100 (19 ações)
| Jogador 2 | 124 | 29 | 26 | 69 | 0.0080 | 0.3024 | 0.0054 | 0.3606 | 0.0026 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0014 (50 ações), BUY_XP: Δ 0.0108 (9 ações), CRAFT_AND_EQUIP: Δ 0.0003 (7 ações), MOVE_BENCH: Δ 0.0351 (14 ações), MOVE_BOARD: Δ -0.0284 (18 ações), PASS: Δ 0.0000 (6 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0443 (19 ações)
| Jogador 3 | 169 | 39 | 40 | 90 | 0.0038 | 0.2664 | 0.0024 | 0.2241 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0239 (64 ações), BUY_XP: Δ 0.0097 (5 ações), CRAFT_AND_EQUIP: Δ 0.0106 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0310 (31 ações), MOVE_BOARD: Δ 0.0244 (15 ações), PASS: Δ 0.0000 (11 ações), SELL: Δ 0.0224 (32 ações)
| Jogador 4 | 108 | 30 | 23 | 55 | 0.0041 | 0.1458 | 0.0022 | 0.3014 | 0.0019 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0281 (46 ações), BUY_XP: Δ 0.0195 (5 ações), CRAFT_AND_EQUIP: Δ 0.0125 (5 ações), MOVE_BENCH: Δ 0.0581 (12 ações), MOVE_BOARD: Δ 0.0359 (16 ações), PASS: Δ 0.0000 (7 ações), SELL: Δ 0.0180 (17 ações)
| Jogador 5 | 122 | 20 | 20 | 82 | -0.0004 | -0.2039 | -0.0035 | 0.3164 | 0.0032 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0153 (58 ações), BUY_XP: Δ 0.0081 (6 ações), CRAFT_AND_EQUIP: Δ 0.0604 (7 ações), MOVE_BENCH: Δ -0.0412 (10 ações), MOVE_BOARD: Δ 0.0607 (5 ações), PASS: Δ 0.0000 (6 ações), SELL: Δ 0.0160 (30 ações)
| Jogador 6 | 117 | 28 | 23 | 66 | 0.0062 | -0.8941 | 0.0025 | 0.5076 | 0.0037 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0066 (47 ações), BUY_XP: Δ 0.0041 (7 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0246 (18 ações), MOVE_BOARD: Δ -0.0805 (6 ações), PASS: Δ 0.0000 (8 ações), SELL: Δ 0.0201 (21 ações)
| Jogador 7 | 174 | 31 | 28 | 115 | 0.0041 | 0.1235 | 0.0012 | 0.3941 | 0.0030 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0077 (71 ações), BUY_XP: Δ 0.0161 (9 ações), CRAFT_AND_EQUIP: Δ -0.0556 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0333 (7 ações), MOVE_BENCH: Δ -0.0042 (15 ações), MOVE_BOARD: Δ 0.0456 (20 ações), PASS: Δ 0.0000 (7 ações), SELL: Δ 0.0111 (38 ações)
| Jogador 8 | 117 | 23 | 26 | 68 | -0.0039 | -0.3408 | -0.0064 | 0.3673 | 0.0026 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0118 (55 ações), BUY_XP: Δ 0.0488 (1 ações), CRAFT_AND_EQUIP: Δ 0.0042 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0700 (3 ações), MOVE_BENCH: Δ 0.0087 (15 ações), MOVE_BOARD: Δ -0.0508 (9 ações), PASS: Δ 0.0000 (4 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0102 (24 ações)
- Jogador 1 — rounds avaliados: 27; correlação estrutural/combate: -0.442; posicional/combate: -0.367.
- Jogador 1 — combate positive: score estrutural prévio -0.027
  score posicional prévio 0.263
- Jogador 1 — combate negative: score estrutural prévio 0.292
  score posicional prévio 0.348
- Jogador 2 — rounds avaliados: 27; correlação estrutural/combate: -0.103; posicional/combate: 0.132.
- Jogador 2 — combate positive: score estrutural prévio 0.452
  score posicional prévio 0.368
- Jogador 2 — combate negative: score estrutural prévio 0.492
  score posicional prévio 0.351
- Jogador 3 — rounds avaliados: 39; correlação estrutural/combate: -0.156; posicional/combate: -0.064.
- Jogador 3 — combate positive: score estrutural prévio 0.250
  score posicional prévio 0.229
- Jogador 3 — combate negative: score estrutural prévio 0.386
  score posicional prévio 0.268
- Jogador 4 — rounds avaliados: 24; correlação estrutural/combate: 0.017; posicional/combate: -0.159.
- Jogador 4 — combate positive: score estrutural prévio 0.228
  score posicional prévio 0.329
- Jogador 4 — combate negative: score estrutural prévio 0.189
  score posicional prévio 0.325
- Jogador 5 — rounds avaliados: 28; correlação estrutural/combate: 0.266; posicional/combate: -0.095.
- Jogador 5 — combate positive: score estrutural prévio -0.131
  score posicional prévio 0.318
- Jogador 5 — combate negative: score estrutural prévio -0.270
  score posicional prévio 0.327
- Jogador 6 — rounds avaliados: 27; correlação estrutural/combate: 0.049; posicional/combate: -0.136.
- Jogador 6 — combate positive: score estrutural prévio -0.748
  score posicional prévio 0.482
- Jogador 6 — combate negative: score estrutural prévio -0.846
  score posicional prévio 0.519
- Jogador 7 — rounds avaliados: 39; correlação estrutural/combate: 0.231; posicional/combate: 0.038.
- Jogador 7 — combate positive: score estrutural prévio 0.196
  score posicional prévio 0.409
- Jogador 7 — combate negative: score estrutural prévio 0.089
  score posicional prévio 0.400
- Jogador 8 — rounds avaliados: 24; correlação estrutural/combate: 0.544; posicional/combate: -0.575.
- Jogador 8 — combate positive: score estrutural prévio -0.056
  score posicional prévio 0.310
- Jogador 8 — combate negative: score estrutural prévio -0.441
  score posicional prévio 0.400

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 148 | OK (148) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_Crownguard, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 150 | OK (150) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 208 | OK (208) | 9 | 0 | 0 | 0 | 9 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Deathblade, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_RedBuff, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 131 | OK (131) | 5 | 0 | 0 | 1 | 5 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 149 | OK (149) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_IonicSpark, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 143 | OK (143) | 4 | 0 | 3 | 0 | 7 | 3 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 213 | OK (213) | 9 | 0 | 0 | 0 | 9 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_RunaansHurricane, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 140 | OK (140) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_GuinsoosRageblade, TFT_Item_HextechGunblade, TFT_Item_SteraksGage, TFT_Item_ThiefsGloves; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 1); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.014 | 0.427 |
| Jogador 1 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 8 | 9 | 4 → 5 | -0.027 | 0.264 |
| Jogador 1 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 5 | 11 | 5 → 5 | 0.000 | -0.323 |
| Jogador 1 | 2-4 | 7 | 2.000 | 4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 5 → 6 | 4 | 5 → 5 | -0.002 | 0.000 |
| Jogador 1 | 2-5 | 4 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 6 → 11 | 4 | 5 → 5 | 0.016 | 0.684 |
| Jogador 1 | 2-6 | 8 | 6.000 | 6.000 | 0 → 1 | 3 → 2 | 18% → 21% | 11 → 7 | 11 | 5 → 6 | 0.065 | 0.364 |
| Jogador 1 | 2-7 | 7 | 0.000 | 4.000 | 1 → 2 | 2 → 1 | 21% → 18% | 7 → 10 | 3 | 6 → 6 | -0.086 | 0.000 |
| Jogador 1 | 3-1 | 3 | 4.000 | 0.000 | 2 → 2 | 1 → 2 | 18% → 21% | 10 → 13 | 2 | 6 → 6 | 0.025 | -0.958 |
| Jogador 1 | 3-2 | 8 | 4.000 | 2.000 | 2 → 3 | 2 → 1 | 21% → 21% | 13 → 14 | 5 | 6 → 6 | 0.122 | -0.353 |
| Jogador 1 | 3-3 | 2 | 0.000 | 6.000 | 3 → 3 | 1 → 1 | 21% → 21% | 14 → 18 | 3 | 6 → 6 | 0.000 | -1.294 |
| Jogador 1 | 3-4 | 6 | 0.000 | 6.000 | 3 → 3 | 1 → 1 | 21% → 21% | 18 → 22 | 3 | 6 → 6 | -0.085 | 0.000 |
| Jogador 1 | 3-5 | 3 | 2.000 | -2.000 | 3 → 3 | 1 → 0 | 21% → 21% | 22 → 28 | 2 | 6 → 6 | -0.109 | 0.905 |
| Jogador 1 | 3-6 | 6 | 0.000 | 8.000 | 3 → 3 | 0 → 1 | 21% → 21% | 28 → 33 | 4 | 6 → 6 | -0.023 | 0.469 |
| Jogador 1 | 3-7 | 4 | 0.000 | -4.000 | 3 → 3 | 1 → 2 | 21% → 21% | 33 → 45 | 2 | 6 → 6 | 0.052 | 0.000 |
| Jogador 1 | 4-1 | 6 | 0.000 | -2.000 | 3 → 3 | 2 → 2 | 21% → 21% | 45 → 55 | 3 | 6 → 6 | 0.000 | -0.439 |
| Jogador 1 | 4-2 | 4 | 0.000 | 4.000 | 3 → 3 | 2 → 2 | 21% → 21% | 55 → 64 | 5 | 6 → 6 | 0.000 | 0.725 |
| Jogador 1 | 4-3 | 6 | 0.000 | 4.000 | 3 → 3 | 2 → 1 | 21% → 21% | 64 → 70 | 6 | 6 → 6 | -0.010 | -0.446 |
| Jogador 1 | 4-4 | 4 | 0.000 | -6.000 | 3 → 3 | 1 → 1 | 21% → 21% | 70 → 84 | 2 | 6 → 6 | 0.015 | 0.000 |
| Jogador 1 | 4-5 | 6 | 0.000 | 10.000 | 3 → 3 | 1 → 1 | 21% → 21% | 84 → 90 | 7 | 6 → 6 | 0.045 | -0.469 |
| Jogador 1 | 4-6 | 4 | 0.000 | -8.000 | 3 → 3 | 1 → 2 | 21% → 21% | 90 → 105 | 2 | 6 → 6 | 0.095 | -0.716 |
| Jogador 1 | 4-7 | 6 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 21% → 21% | 105 → 114 | 7 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 4 | 0.000 | 6.000 | 3 → 3 | 2 → 3 | 21% → 21% | 114 → 122 | 3 | 6 → 6 | 0.008 | -0.725 |
| Jogador 1 | 5-2 | 5 | -28.000 | -50.000 | 3 → 0 | 3 → 0 | 21% → 0% | 122 → 126 | 2 | 6 → 6 | -0.200 | -0.600 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 14, COMPOSITION_COMPATIBILITY: 16, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 9; mudanças de composição: 3; posicionamento melhorou em 31 ações e piorou em 25.
- Jogador 1 — estado final: ouro 126, nível 6, vida 2.0, colocação 6.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 8 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.020 | -0.289 |
| Jogador 2 | 2-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.024 | -0.248 |
| Jogador 2 | 2-3 | 5 | 2.000 | 0.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 7 | 5 | 4 → 5 | 0.015 | 0.551 |
| Jogador 2 | 2-4 | 9 | 4.000 | 8.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 6 | 8 | 5 → 5 | 0.017 | 0.000 |
| Jogador 2 | 2-5 | 4 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 7 | 6 | 5 → 5 | -0.001 | -0.593 |
| Jogador 2 | 2-6 | 8 | 0.000 | -8.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 9 | 13 | 5 → 5 | 0.000 | -0.296 |
| Jogador 2 | 2-7 | 7 | 2.000 | 6.000 | 1 → 1 | 2 → 3 | 18% → 21% | 9 → 7 | 8 | 5 → 6 | 0.064 | 0.000 |
| Jogador 2 | 3-1 | 3 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 7 → 10 | 3 | 6 → 6 | 0.001 | -0.829 |
| Jogador 2 | 3-2 | 8 | 0.000 | -4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 10 → 6 | 13 | 6 → 6 | -0.002 | -0.329 |
| Jogador 2 | 3-3 | 2 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 21% → 21% | 6 → 9 | 3 | 6 → 6 | -0.001 | 1.358 |
| Jogador 2 | 3-4 | 7 | 0.000 | -4.000 | 1 → 1 | 3 → 3 | 21% → 21% | 9 → 12 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 3 | 0.000 | 8.000 | 1 → 1 | 3 → 5 | 21% → 21% | 12 → 15 | 4 | 6 → 6 | 0.000 | 0.922 |
| Jogador 2 | 3-6 | 6 | 0.000 | -6.000 | 1 → 1 | 5 → 4 | 21% → 21% | 15 → 24 | 4 | 6 → 6 | 0.000 | -0.486 |
| Jogador 2 | 3-7 | 4 | 0.000 | 6.000 | 1 → 1 | 4 → 3 | 21% → 21% | 24 → 23 | 7 | 6 → 6 | -0.030 | 0.000 |
| Jogador 2 | 4-1 | 6 | 6.000 | 0.000 | 1 → 2 | 3 → 4 | 21% → 21% | 23 → 28 | 3 | 6 → 7 | -0.006 | -0.452 |
| Jogador 2 | 4-2 | 4 | 6.000 | -6.000 | 2 → 3 | 4 → 3 | 21% → 21% | 28 → 35 | 1 | 7 → 7 | -0.009 | -0.646 |
| Jogador 2 | 4-3 | 6 | 6.000 | 6.000 | 3 → 3 | 3 → 3 | 21% → 25% | 35 → 38 | 6 | 7 → 7 | 0.018 | 0.475 |
| Jogador 2 | 4-4 | 4 | 0.000 | 2.000 | 3 → 3 | 3 → 2 | 25% → 25% | 38 → 42 | 4 | 7 → 7 | -0.031 | 0.000 |
| Jogador 2 | 4-5 | 5 | 0.000 | 6.000 | 3 → 3 | 2 → 3 | 25% → 25% | 42 → 50 | 3 | 7 → 7 | -0.132 | 0.597 |
| Jogador 2 | 4-6 | 4 | 0.000 | -14.000 | 3 → 3 | 3 → 3 | 25% → 25% | 50 → 72 | 1 | 7 → 7 | 0.180 | 0.746 |
| Jogador 2 | 4-7 | 6 | 0.000 | 4.000 | 3 → 3 | 3 → 4 | 25% → 25% | 72 → 81 | 3 | 7 → 7 | 0.021 | 0.000 |
| Jogador 2 | 5-1 | 4 | 0.000 | -4.000 | 3 → 3 | 4 → 4 | 25% → 25% | 81 → 93 | 0 | 7 → 7 | 0.000 | -0.712 |
| Jogador 2 | 5-2 | 5 | -36.000 | -34.000 | 3 → 0 | 4 → 0 | 25% → 0% | 93 → 81 | 12 | 7 → 7 | -0.215 | -0.550 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 32 ações e piorou em 29.
- Jogador 2 — estado final: ouro 81, nível 7, vida 13.0, colocação 5.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 8 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.003 | 0.327 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.684 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 8 | 7 | 4 → 5 | 0.006 | 0.502 |
| Jogador 3 | 2-4 | 9 | 6.000 | 2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 8 → 6 | 8 | 5 → 5 | 0.019 | 0.000 |
| Jogador 3 | 2-5 | 4 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 18% → 18% | 6 → 8 | 5 | 5 → 5 | 0.006 | 0.659 |
| Jogador 3 | 2-6 | 8 | 0.000 | -4.000 | 1 → 1 | 3 → 1 | 18% → 18% | 8 → 15 | 3 | 5 → 5 | -0.039 | 0.314 |
| Jogador 3 | 2-7 | 7 | 0.000 | 12.000 | 1 → 1 | 1 → 2 | 18% → 18% | 15 → 8 | 14 | 5 → 6 | -0.003 | 0.000 |
| Jogador 3 | 3-1 | 3 | 4.000 | -4.000 | 1 → 2 | 2 → 2 | 18% → 21% | 8 → 17 | 0 | 6 → 6 | 0.051 | 0.939 |
| Jogador 3 | 3-2 | 7 | 4.000 | -4.000 | 2 → 2 | 2 → 1 | 21% → 21% | 17 → 26 | 1 | 6 → 6 | -0.019 | 0.429 |
| Jogador 3 | 3-3 | 2 | 0.000 | 8.000 | 2 → 2 | 1 → 1 | 21% → 21% | 26 → 33 | 4 | 6 → 6 | 0.000 | 1.406 |
| Jogador 3 | 3-4 | 6 | 0.000 | 6.000 | 2 → 2 | 1 → 1 | 21% → 21% | 33 → 41 | 3 | 6 → 6 | -0.003 | 0.000 |
| Jogador 3 | 3-5 | 3 | 0.000 | 2.000 | 2 → 2 | 1 → 2 | 21% → 21% | 41 → 50 | 3 | 6 → 6 | 0.020 | -0.846 |
| Jogador 3 | 3-6 | 6 | 4.000 | -4.000 | 2 → 2 | 2 → 4 | 21% → 21% | 50 → 62 | 5 | 6 → 6 | 0.017 | 0.469 |
| Jogador 3 | 3-7 | 4 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 21% → 21% | 62 → 72 | 0 | 6 → 6 | -0.005 | 0.000 |
| Jogador 3 | 4-1 | 6 | 2.000 | -6.000 | 2 → 1 | 4 → 4 | 21% → 21% | 72 → 87 | 0 | 6 → 6 | 0.000 | 0.481 |
| Jogador 3 | 4-2 | 4 | 0.000 | 4.000 | 1 → 1 | 4 → 5 | 21% → 21% | 87 → 97 | 2 | 6 → 6 | 0.000 | 0.738 |
| Jogador 3 | 4-3 | 4 | -2.000 | 2.000 | 1 → 1 | 5 → 5 | 21% → 21% | 97 → 109 | 0 | 6 → 6 | -0.121 | 0.700 |
| Jogador 3 | 4-4 | 4 | 2.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 109 → 119 | 3 | 6 → 6 | 0.121 | 0.000 |
| Jogador 3 | 4-5 | 6 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 119 → 132 | 3 | 6 → 6 | 0.000 | 0.489 |
| Jogador 3 | 4-6 | 4 | 0.000 | -4.000 | 1 → 1 | 5 → 4 | 21% → 21% | 132 → 146 | 4 | 6 → 6 | -0.015 | 0.700 |
| Jogador 3 | 4-7 | 6 | 4.000 | 0.000 | 1 → 2 | 4 → 2 | 21% → 21% | 146 → 152 | 7 | 6 → 6 | 0.027 | 0.000 |
| Jogador 3 | 5-1 | 4 | 0.000 | 6.000 | 2 → 2 | 2 → 3 | 21% → 21% | 152 → 163 | 3 | 6 → 6 | -0.015 | 0.764 |
| Jogador 3 | 5-2 | 5 | 0.000 | -8.000 | 2 → 2 | 3 → 4 | 21% → 21% | 163 → 182 | 1 | 6 → 7 | 0.026 | 0.581 |
| Jogador 3 | 5-3 | 5 | 4.000 | -8.000 | 2 → 2 | 4 → 4 | 21% → 25% | 182 → 200 | 6 | 7 → 7 | 0.003 | 0.607 |
| Jogador 3 | 5-4 | 5 | 0.000 | 8.000 | 2 → 2 | 4 → 5 | 25% → 25% | 200 → 209 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 5 | 0.000 | 12.000 | 2 → 2 | 5 → 4 | 25% → 25% | 209 → 214 | 11 | 7 → 7 | 0.000 | 0.587 |
| Jogador 3 | 5-6 | 5 | 0.000 | -6.000 | 2 → 2 | 4 → 4 | 25% → 25% | 214 → 233 | 6 | 7 → 7 | 0.000 | 0.587 |
| Jogador 3 | 5-7 | 5 | 0.000 | -8.000 | 2 → 2 | 4 → 6 | 25% → 25% | 233 → 250 | 4 | 7 → 7 | -0.012 | 0.000 |
| Jogador 3 | 6-1 | 5 | 0.000 | -4.000 | 2 → 2 | 6 → 6 | 25% → 25% | 250 → 266 | 3 | 7 → 7 | 0.000 | 0.584 |
| Jogador 3 | 6-2 | 5 | 0.000 | -2.000 | 2 → 2 | 6 → 5 | 25% → 25% | 266 → 281 | 5 | 7 → 7 | 0.000 | 0.627 |
| Jogador 3 | 6-3 | 5 | 2.000 | -6.000 | 2 → 2 | 5 → 4 | 25% → 25% | 281 → 296 | 4 | 7 → 7 | 0.044 | 0.604 |
| Jogador 3 | 6-4 | 5 | 0.000 | 14.000 | 2 → 2 | 4 → 5 | 25% → 25% | 296 → 302 | 9 | 7 → 7 | -0.000 | 0.000 |
| Jogador 3 | 6-5 | 5 | 0.000 | -2.000 | 2 → 2 | 5 → 5 | 25% → 25% | 302 → 313 | 5 | 7 → 7 | 0.000 | -0.550 |
| Jogador 3 | 6-6 | 5 | 0.000 | 0.000 | 2 → 2 | 5 → 5 | 25% → 25% | 313 → 324 | 5 | 7 → 7 | 0.000 | -0.550 |
| Jogador 3 | 6-7 | 5 | 0.000 | 4.000 | 2 → 2 | 5 → 5 | 25% → 25% | 324 → 333 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 7-1 | 4 | 0.000 | -12.000 | 2 → 2 | 5 → 5 | 25% → 25% | 333 → 339 | 1 | 7 → 7 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 46 ações e piorou em 40.
- Jogador 3 — estado final: ouro 339, nível 7, vida 59.0, colocação None.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.021 | -0.404 |
| Jogador 4 | 2-2 | 4 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.034 | 0.684 |
| Jogador 4 | 2-3 | 9 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 18% → 18% | 6 → 6 | 9 | 5 → 5 | -0.004 | -0.264 |
| Jogador 4 | 2-4 | 9 | 0.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 18% | 6 → 8 | 10 | 5 → 5 | -0.003 | 0.000 |
| Jogador 4 | 2-5 | 4 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 8 → 11 | 5 | 5 → 5 | 0.001 | -0.645 |
| Jogador 4 | 2-6 | 8 | 0.000 | -10.000 | 0 → 0 | 2 → 2 | 18% → 18% | 11 → 23 | 5 | 5 → 5 | 0.000 | -0.342 |
| Jogador 4 | 2-7 | 7 | 2.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 21% | 23 → 21 | 9 | 5 → 6 | 0.011 | 0.000 |
| Jogador 4 | 3-1 | 3 | 6.000 | -6.000 | 0 → 1 | 2 → 1 | 21% → 21% | 21 → 28 | 1 | 6 → 6 | 0.023 | -0.879 |
| Jogador 4 | 3-2 | 8 | 4.000 | 4.000 | 1 → 3 | 1 → 0 | 21% → 21% | 28 → 32 | 5 | 6 → 6 | 0.035 | -0.335 |
| Jogador 4 | 3-3 | 2 | 0.000 | 2.000 | 3 → 3 | 0 → 0 | 21% → 21% | 32 → 42 | 1 | 6 → 6 | 0.000 | -1.269 |
| Jogador 4 | 3-4 | 7 | 0.000 | 12.000 | 3 → 3 | 0 → 2 | 21% → 21% | 42 → 47 | 6 | 6 → 6 | -0.040 | 0.000 |
| Jogador 4 | 3-5 | 3 | 0.000 | 10.000 | 3 → 3 | 2 → 3 | 21% → 21% | 47 → 54 | 5 | 6 → 6 | 0.000 | -0.846 |
| Jogador 4 | 3-6 | 6 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 54 → 63 | 5 | 6 → 6 | 0.011 | 0.514 |
| Jogador 4 | 3-7 | 4 | -4.000 | 8.000 | 3 → 3 | 3 → 2 | 21% → 21% | 63 → 68 | 5 | 6 → 6 | -0.103 | 0.000 |
| Jogador 4 | 4-1 | 6 | 0.000 | 6.000 | 3 → 3 | 2 → 3 | 21% → 21% | 68 → 75 | 3 | 6 → 6 | 0.009 | -0.492 |
| Jogador 4 | 4-2 | 4 | 0.000 | -4.000 | 3 → 3 | 3 → 3 | 21% → 21% | 75 → 89 | 2 | 6 → 6 | 0.037 | -0.694 |
| Jogador 4 | 4-3 | 6 | 0.000 | -4.000 | 3 → 3 | 3 → 4 | 21% → 21% | 89 → 104 | 5 | 6 → 6 | 0.043 | 0.475 |
| Jogador 4 | 4-4 | 4 | 0.000 | -6.000 | 3 → 3 | 4 → 1 | 21% → 21% | 104 → 113 | 4 | 6 → 6 | -0.030 | 0.000 |
| Jogador 4 | 4-5 | 6 | 0.000 | 16.000 | 3 → 3 | 1 → 1 | 21% → 21% | 113 → 115 | 8 | 6 → 6 | -0.002 | -0.461 |
| Jogador 4 | 4-6 | 4 | -18.000 | -48.000 | 3 → 0 | 1 → 0 | 21% → 0% | 115 → 122 | 3 | 6 → 6 | -0.135 | -0.737 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 35 ações e piorou em 25.
- Jogador 4 — estado final: ouro 122, nível 6, vida 3.0, colocação 8.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.347 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.607 |
| Jogador 5 | 2-3 | 9 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 9 | 7 | 4 → 5 | -0.007 | -0.264 |
| Jogador 5 | 2-4 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 10 | 11 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 4 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 8 | 8 | 5 → 5 | -0.015 | 0.628 |
| Jogador 5 | 2-6 | 8 | 0.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 16 | 4 | 5 → 5 | 0.008 | -0.322 |
| Jogador 5 | 2-7 | 7 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 16 → 22 | 4 | 5 → 6 | -0.042 | 0.000 |
| Jogador 5 | 3-1 | 3 | 6.000 | 2.000 | 0 → 0 | 1 → 2 | 18% → 21% | 22 → 25 | 4 | 6 → 6 | 0.054 | -0.862 |
| Jogador 5 | 3-2 | 8 | 0.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 25 → 22 | 15 | 6 → 6 | 0.001 | 0.358 |
| Jogador 5 | 3-3 | 2 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 22 → 25 | 3 | 6 → 6 | 0.000 | -1.316 |
| Jogador 5 | 3-4 | 7 | 0.000 | -2.000 | 0 → 0 | 2 → 3 | 21% → 21% | 25 → 33 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 3 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 21% → 21% | 33 → 37 | 4 | 6 → 6 | 0.000 | -0.862 |
| Jogador 5 | 3-6 | 6 | 0.000 | -4.000 | 0 → 0 | 3 → 4 | 21% → 21% | 37 → 48 | 3 | 6 → 6 | 0.000 | -0.439 |
| Jogador 5 | 3-7 | 4 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 21% → 21% | 48 → 55 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 6 | -2.000 | 10.000 | 0 → 0 | 4 → 4 | 21% → 21% | 55 → 62 | 4 | 6 → 6 | -0.003 | 0.475 |
| Jogador 5 | 4-2 | 4 | 0.000 | -6.000 | 0 → 0 | 4 → 4 | 21% → 21% | 62 → 77 | 1 | 6 → 6 | 0.000 | 0.690 |
| Jogador 5 | 4-3 | 6 | 0.000 | -2.000 | 0 → 0 | 4 → 5 | 21% → 21% | 77 → 88 | 4 | 6 → 6 | 0.000 | -0.438 |
| Jogador 5 | 4-4 | 4 | 2.000 | 0.000 | 0 → 0 | 5 → 4 | 21% → 21% | 88 → 95 | 3 | 6 → 6 | -0.072 | 0.000 |
| Jogador 5 | 4-5 | 6 | 4.000 | -6.000 | 0 → 0 | 4 → 3 | 21% → 21% | 95 → 107 | 2 | 6 → 6 | -0.015 | -0.497 |
| Jogador 5 | 4-6 | 4 | 0.000 | 10.000 | 0 → 0 | 3 → 4 | 21% → 21% | 107 → 113 | 5 | 6 → 6 | 0.000 | -0.656 |
| Jogador 5 | 4-7 | 6 | 0.000 | 0.000 | 0 → 0 | 4 → 3 | 21% → 21% | 113 → 124 | 6 | 6 → 7 | 0.006 | 0.000 |
| Jogador 5 | 5-1 | 4 | 6.000 | 0.000 | 0 → 0 | 3 → 4 | 21% → 25% | 124 → 132 | 3 | 7 → 7 | 0.129 | 0.751 |
| Jogador 5 | 5-2 | 5 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 132 → 145 | 3 | 7 → 7 | 0.012 | 0.577 |
| Jogador 5 | 5-3 | 5 | -34.000 | -36.000 | 0 → 0 | 4 → 0 | 25% → 0% | 145 → 141 | 8 | 7 → 7 | -0.064 | -0.570 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 20, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 12; mudanças de composição: 2; posicionamento melhorou em 27 ações e piorou em 21.
- Jogador 5 — estado final: ouro 141, nível 7, vida 15.0, colocação 3.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 6 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.021 | -0.412 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 9 | 6.000 | -4.000 | 0 → 0 | 2 → 3 | 14% → 18% | 9 → 6 | 13 | 5 → 5 | -0.002 | 0.000 |
| Jogador 6 | 2-5 | 4 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 18% → 18% | 6 → 11 | 3 | 5 → 5 | 0.002 | -0.645 |
| Jogador 6 | 2-6 | 8 | 0.000 | -10.000 | 0 → 0 | 4 → 4 | 18% → 18% | 11 → 24 | 3 | 5 → 5 | 0.015 | -0.303 |
| Jogador 6 | 2-7 | 7 | 4.000 | -8.000 | 0 → 0 | 4 → 3 | 18% → 21% | 24 → 26 | 11 | 5 → 6 | -0.031 | 0.000 |
| Jogador 6 | 3-1 | 3 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 26 → 31 | 3 | 6 → 6 | -0.020 | 0.888 |
| Jogador 6 | 3-2 | 8 | 4.000 | 0.000 | 0 → 1 | 3 → 1 | 21% → 21% | 31 → 34 | 4 | 6 → 6 | 0.057 | -0.335 |
| Jogador 6 | 3-3 | 2 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 21% → 21% | 34 → 40 | 3 | 6 → 6 | 0.002 | 1.383 |
| Jogador 6 | 3-4 | 7 | 0.000 | 14.000 | 1 → 1 | 2 → 2 | 21% → 21% | 40 → 32 | 15 | 6 → 6 | 0.038 | 0.000 |
| Jogador 6 | 3-5 | 3 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 21% → 21% | 32 → 42 | 3 | 6 → 6 | 0.020 | 0.922 |
| Jogador 6 | 3-6 | 6 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 21% → 21% | 42 → 49 | 2 | 6 → 6 | -0.037 | -0.439 |
| Jogador 6 | 3-7 | 4 | 0.000 | -4.000 | 1 → 0 | 4 → 4 | 21% → 21% | 49 → 62 | 0 | 6 → 6 | 0.070 | 0.000 |
| Jogador 6 | 4-1 | 6 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 62 → 72 | 1 | 6 → 6 | 0.000 | 0.469 |
| Jogador 6 | 4-2 | 4 | -4.000 | 8.000 | 0 → 0 | 4 → 3 | 21% → 21% | 72 → 77 | 5 | 6 → 6 | -0.047 | -0.681 |
| Jogador 6 | 4-3 | 6 | 0.000 | 0.000 | 0 → 0 | 3 → 4 | 21% → 21% | 77 → 90 | 7 | 6 → 6 | 0.010 | -0.446 |
| Jogador 6 | 4-4 | 4 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 90 → 99 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 6 | 6.000 | -4.000 | 0 → 1 | 4 → 3 | 21% → 21% | 99 → 108 | 2 | 6 → 7 | 0.053 | 0.506 |
| Jogador 6 | 4-6 | 4 | 8.000 | 2.000 | 1 → 1 | 3 → 4 | 21% → 25% | 108 → 115 | 6 | 7 → 7 | 0.010 | 0.758 |
| Jogador 6 | 4-7 | 6 | 2.000 | 0.000 | 1 → 1 | 4 → 3 | 25% → 21% | 115 → 123 | 5 | 7 → 7 | 0.085 | 0.000 |
| Jogador 6 | 5-1 | 4 | 4.000 | 4.000 | 1 → 2 | 3 → 2 | 21% → 21% | 123 → 127 | 6 | 7 → 7 | 0.007 | -0.738 |
| Jogador 6 | 5-2 | 5 | -38.000 | -48.000 | 2 → 0 | 2 → 0 | 21% → 0% | 127 → 126 | 4 | 7 → 7 | -0.131 | -0.546 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 33 ações e piorou em 26.
- Jogador 6 — estado final: ouro 126, nível 7, vida 13.0, colocação 4.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 6 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.016 | 0.456 |
| Jogador 7 | 2-2 | 10 | -2.000 | 4.000 | 0 → 0 | 3 → 2 | 14% → 11% | 8 → 8 | 8 | 4 → 4 | 0.015 | -0.258 |
| Jogador 7 | 2-3 | 9 | 10.000 | -6.000 | 0 → 0 | 2 → 2 | 11% → 14% | 8 → 8 | 9 | 4 → 5 | 0.056 | 0.304 |
| Jogador 7 | 2-4 | 5 | 6.000 | 8.000 | 0 → 0 | 2 → 2 | 14% → 18% | 8 → 6 | 7 | 5 → 5 | -0.010 | 0.000 |
| Jogador 7 | 2-5 | 4 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 9 | 4 | 5 → 5 | -0.007 | 0.684 |
| Jogador 7 | 2-6 | 8 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 18% → 18% | 9 → 7 | 12 | 5 → 5 | -0.005 | 0.342 |
| Jogador 7 | 2-7 | 7 | 8.000 | -2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 7 → 6 | 7 | 5 → 6 | 0.044 | 0.000 |
| Jogador 7 | 3-1 | 3 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 11 | 2 | 6 → 6 | 0.000 | 1.017 |
| Jogador 7 | 3-2 | 5 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 11 → 8 | 11 | 6 → 6 | 0.000 | 0.572 |
| Jogador 7 | 3-3 | 2 | 0.000 | -2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 19 | 0 | 6 → 6 | 0.000 | 1.433 |
| Jogador 7 | 3-4 | 7 | 2.000 | 4.000 | 0 → 0 | 3 → 1 | 21% → 21% | 19 → 21 | 7 | 6 → 6 | -0.029 | 0.000 |
| Jogador 7 | 3-5 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 3 | 21% → 21% | 21 → 27 | 4 | 6 → 6 | 0.000 | 0.905 |
| Jogador 7 | 3-6 | 6 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 27 → 34 | 7 | 6 → 6 | 0.019 | 0.514 |
| Jogador 7 | 3-7 | 4 | 0.000 | -12.000 | 0 → 0 | 4 → 4 | 21% → 21% | 34 → 54 | 3 | 6 → 6 | 0.015 | 0.000 |
| Jogador 7 | 4-1 | 6 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 54 → 67 | 4 | 6 → 6 | -0.012 | 0.519 |
| Jogador 7 | 4-2 | 4 | 0.000 | -6.000 | 0 → 0 | 4 → 4 | 21% → 21% | 67 → 84 | 2 | 6 → 6 | 0.000 | 0.725 |
| Jogador 7 | 4-3 | 6 | 2.000 | 4.000 | 0 → 0 | 4 → 4 | 21% → 25% | 84 → 91 | 10 | 6 → 7 | 0.018 | 0.523 |
| Jogador 7 | 4-4 | 4 | 0.000 | 2.000 | 0 → 0 | 4 → 5 | 25% → 25% | 91 → 103 | 3 | 7 → 7 | -0.037 | 0.000 |
| Jogador 7 | 4-5 | 6 | 0.000 | 4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 103 → 115 | 8 | 7 → 7 | 0.000 | 0.523 |
| Jogador 7 | 4-6 | 4 | 0.000 | -2.000 | 0 → 0 | 5 → 4 | 25% → 25% | 115 → 127 | 4 | 7 → 7 | -0.043 | 0.778 |
| Jogador 7 | 4-7 | 6 | 0.000 | -10.000 | 0 → 0 | 4 → 5 | 25% → 25% | 127 → 147 | 5 | 7 → 7 | 0.088 | 0.000 |
| Jogador 7 | 5-1 | 4 | 0.000 | 4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 147 → 159 | 2 | 7 → 7 | -0.095 | 0.784 |
| Jogador 7 | 5-2 | 5 | 0.000 | 2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 159 → 172 | 5 | 7 → 7 | 0.000 | 0.631 |
| Jogador 7 | 5-3 | 5 | 0.000 | -4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 172 → 187 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-4 | 5 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 187 → 197 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 5 | 0.000 | -4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 197 → 209 | 5 | 7 → 7 | 0.000 | -0.556 |
| Jogador 7 | 5-6 | 5 | 0.000 | 2.000 | 0 → 0 | 5 → 5 | 25% → 25% | 209 → 219 | 6 | 7 → 7 | 0.000 | -0.556 |
| Jogador 7 | 5-7 | 5 | 4.000 | -4.000 | 0 → 1 | 5 → 4 | 25% → 25% | 219 → 227 | 6 | 7 → 7 | 0.031 | 0.000 |
| Jogador 7 | 6-1 | 5 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 227 → 235 | 3 | 7 → 7 | -0.032 | -0.550 |
| Jogador 7 | 6-2 | 5 | -6.000 | -8.000 | 1 → 2 | 4 → 2 | 25% → 18% | 235 → 251 | 3 | 7 → 7 | 0.004 | -0.590 |
| Jogador 7 | 6-3 | 5 | 12.000 | 0.000 | 2 → 2 | 2 → 2 | 18% → 25% | 251 → 257 | 6 | 7 → 7 | -0.047 | -0.570 |
| Jogador 7 | 6-4 | 5 | 0.000 | 6.000 | 2 → 2 | 2 → 3 | 25% → 25% | 257 → 266 | 5 | 7 → 7 | 0.018 | 0.000 |
| Jogador 7 | 6-5 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 2 | 25% → 25% | 266 → 276 | 6 | 7 → 7 | 0.000 | 0.584 |
| Jogador 7 | 6-6 | 5 | 0.000 | 0.000 | 2 → 2 | 2 → 4 | 25% → 25% | 276 → 288 | 6 | 7 → 7 | 0.000 | 0.584 |
| Jogador 7 | 6-7 | 5 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 25% → 25% | 288 → 299 | 5 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 7-1 | 4 | 0.000 | 8.000 | 2 → 2 | 4 → 5 | 25% → 25% | 299 → 295 | 7 | 7 → 7 | 0.000 | 0.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 20, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 17; mudanças de composição: 0; posicionamento melhorou em 34 ações e piorou em 31.
- Jogador 7 — estado final: ouro 295, nível 7, vida 17.0, colocação None.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 8 | 6.000 | 0.000 | 0 → 2 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.003 | -0.322 |
| Jogador 8 | 2-2 | 10 | 0.000 | 12.000 | 2 → 2 | 0 → 0 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | 0.013 | -0.231 |
| Jogador 8 | 2-3 | 9 | 2.000 | 4.000 | 2 → 1 | 0 → 0 | 14% → 14% | 6 → 9 | 6 | 4 → 4 | 0.028 | 0.279 |
| Jogador 8 | 2-4 | 9 | 2.000 | 8.000 | 1 → 1 | 0 → 1 | 14% → 18% | 9 → 6 | 11 | 4 → 5 | -0.012 | 0.000 |
| Jogador 8 | 2-5 | 4 | 0.000 | 4.000 | 1 → 1 | 1 → 3 | 18% → 18% | 6 → 9 | 3 | 5 → 5 | -0.001 | -0.620 |
| Jogador 8 | 2-6 | 8 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 18% → 18% | 9 → 13 | 7 | 5 → 5 | 0.011 | 0.320 |
| Jogador 8 | 2-7 | 7 | 0.000 | -4.000 | 1 → 1 | 4 → 5 | 18% → 18% | 13 → 21 | 7 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 3 | 0.000 | -2.000 | 1 → 1 | 5 → 5 | 18% → 18% | 21 → 31 | 0 | 5 → 5 | 0.000 | 0.922 |
| Jogador 8 | 3-2 | 8 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 18% → 18% | 31 → 37 | 9 | 5 → 5 | 0.000 | 0.351 |
| Jogador 8 | 3-3 | 2 | 0.000 | -4.000 | 1 → 1 | 5 → 5 | 18% → 18% | 37 → 47 | 0 | 5 → 5 | 0.000 | -1.344 |
| Jogador 8 | 3-4 | 7 | 4.000 | 6.000 | 1 → 2 | 5 → 3 | 18% → 18% | 47 → 49 | 7 | 5 → 5 | -0.030 | 0.000 |
| Jogador 8 | 3-5 | 3 | 0.000 | 2.000 | 2 → 2 | 3 → 4 | 18% → 18% | 49 → 59 | 3 | 5 → 5 | 0.020 | -0.862 |
| Jogador 8 | 3-6 | 6 | 2.000 | 2.000 | 2 → 2 | 4 → 3 | 18% → 18% | 59 → 68 | 5 | 5 → 6 | -0.020 | -0.486 |
| Jogador 8 | 3-7 | 4 | 2.000 | 6.000 | 2 → 2 | 3 → 3 | 18% → 21% | 68 → 75 | 4 | 6 → 6 | -0.013 | 0.000 |
| Jogador 8 | 4-1 | 6 | 0.000 | -2.000 | 2 → 2 | 3 → 4 | 21% → 21% | 75 → 87 | 1 | 6 → 6 | 0.035 | -0.446 |
| Jogador 8 | 4-2 | 4 | 0.000 | 8.000 | 2 → 2 | 4 → 4 | 21% → 21% | 87 → 95 | 4 | 6 → 6 | -0.024 | -0.681 |
| Jogador 8 | 4-3 | 6 | 0.000 | -4.000 | 2 → 2 | 4 → 4 | 21% → 21% | 95 → 110 | 5 | 6 → 6 | -0.033 | -0.497 |
| Jogador 8 | 4-4 | 4 | 0.000 | -8.000 | 2 → 2 | 4 → 5 | 21% → 21% | 110 → 127 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 6 | -4.000 | 4.000 | 2 → 2 | 5 → 2 | 21% → 21% | 127 → 130 | 10 | 6 → 6 | -0.043 | -0.477 |
| Jogador 8 | 4-6 | 4 | -20.000 | -48.000 | 2 → 0 | 2 → 0 | 21% → 0% | 130 → 122 | 8 | 6 → 6 | 0.105 | -0.704 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 16, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 28 ações e piorou em 29.
- Jogador 8 — estado final: ouro 122, nível 6, vida 6.0, colocação 7.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 45 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 1 | 0 |
| Jogador 2 | 50 | 19 | 2 | 3 | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Jogador 3 | 64 | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 |
| Jogador 4 | 46 | 17 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 2 | 2 | 0 |
| Jogador 5 | 58 | 30 | 6 | 6 | 7 | 2 | 1 | 1 | 2 | 0 | 0 | 0 |
| Jogador 6 | 47 | 21 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |
| Jogador 7 | 71 | 38 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 1 | 0 | 0 |
| Jogador 8 | 55 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 1 | 0 |
- Jogador 1 — venda DA_18_Ornn (2-5, step 82): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Caitlyn (5-2, step 174): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_KhaZix (3-6, step 124): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-6, step 160): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=True, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-5, step 119): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_KogMaw18_AD (6-2, step 208): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_KogMaw18_AD (2-6, step 86): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-6, step 89): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Fiddlesticks18 (4-4, step 148): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_RekSai (2-7, step 94): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_Akali_AD (4-7, step 164): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_Yorick (2-6, step 87): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-6, step 88): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Kayle (2-7, step 92): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Sentry (3-7, step 129): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Tristana (4-3, step 144): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Xayah (5-2, step 174): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Camille (2-6, step 89): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (3-6, step 122): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (3-7, step 128): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rammus (3-7, step 130): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Diana (4-2, step 140): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (4-7, step 163): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (3-6, step 124): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.

Vendas de core/pares ignoradas antes da decisão da composição: **6**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 65 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 1 | 2-5 | 82 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 5-2 | 174 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Caitlyn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 55 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-6 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 3-7 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-1 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-2 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-3 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-4 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-5 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| MEDIUM | Jogador 1 | 4-7 | 162 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| LOW | Jogador 1 | 4-7 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 732 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-5 | 795 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-5 | 796 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 902 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1002 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-7 | 1003 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1053 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1054 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1165 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1201 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1285 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1334 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1335 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1420 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1421 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1482 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 1483 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 1570 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 1571 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 1634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 1635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 1726 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 1727 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 1789 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 1790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 2168 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-2 | 2169 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 3-3 | 1262 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 3-5 | 1397 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-6 | 88 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-4 | 114 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-4 | 117 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-6 | 124 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 3-6 | 126 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_CrimsonRaptor18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 3-7 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-6 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-6 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-1 | 1628 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 1690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 1780 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 1781 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 1843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 1844 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 1918 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 1919 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 1984 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-6 | 1985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 2072 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 2073 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 2136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 2137 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 2212 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 5-2 | 2213 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 4-4 | 1895 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 3-5 | 119 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 6-2 | 208 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 5-5 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 5-5 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-4 | 701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 760 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 868 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 963 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1012 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1107 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1143 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1276 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 1360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 1419 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1509 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 1572 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 1632 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-3 | 1633 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 1694 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 1783 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 1847 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 1935 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 1998 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 2075 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-3 | 2153 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-4 | 2231 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-5 | 2307 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-6 | 2385 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-7 | 2462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-1 | 2542 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-2 | 2620 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-3 | 2696 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-4 | 2772 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-5 | 2848 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-6 | 2924 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-7 | 3002 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| MEDIUM | Jogador 3 | 3-1 | 1084 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1204 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-6 | 1396 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-2 | 1609 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-4 | 77 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 2-5 | 82 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yunara foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 4 | 2-6 | 86 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 2-6 | 88 | PURCHASE_SALE_REVIEW | Compra de DA_CrimsonRaptor18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 2-6 | 89 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 2-6 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-7 | 1463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-1 | 1551 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-2 | 1614 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-6 | 1916 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-6 | 1917 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 2-4 | 77 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 85 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 88 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-4 | 116 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Warwick) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-4 | 117 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Alistar) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-6 | 126 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Xayah) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 129 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 2-1 | 48 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 49 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 2-4 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| MEDIUM | Jogador 5 | 3-2 | 104 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| LOW | Jogador 5 | 3-2 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| MEDIUM | Jogador 5 | 4-6 | 161 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 547 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 668 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 728 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 838 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 937 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 986 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-2 | 1094 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1095 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-3 | 1133 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1134 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-4 | 1233 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1234 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-5 | 1284 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1285 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-6 | 1372 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1373 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-7 | 1435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 1436 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-1 | 1525 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 1526 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-2 | 1589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 1590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 1680 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 1681 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 1743 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 1744 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 1832 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 1833 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 1896 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 1897 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 1985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 1986 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2050 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 2051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 2128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 2129 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 2205 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-3 | 2206 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 2-3 | 66 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 2-6 | 87 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 2-6 | 88 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 2-6 | 90 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 2-7 | 92 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kayle' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-7 | 95 | PURCHASE_SALE_REVIEW | Compra de DA_KogMaw18_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 6 | 3-7 | 129 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-3 | 144 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-3 | 146 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 5-2 | 174 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 6 | 2-3 | 70 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 537 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 659 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 720 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 834 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 930 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 979 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1094 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1130 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1229 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1230 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1280 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1281 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1368 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1369 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1436 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 1526 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 1527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 1589 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 1590 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 1676 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 1677 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 1738 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 1739 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 1830 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 1831 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 1894 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 1895 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 1987 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2049 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 2126 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-2 | 2127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 3-5 | 1345 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-6 | 89 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-6 | 122 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-7 | 128 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-7 | 130 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-2 | 140 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-7 | 163 | SOLD_CORE_UNIT | Venda de 'DA_18_Hecarim' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-5 | 829 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 940 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-7 | 1037 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-1 | 1087 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-2 | 1158 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-3 | 1195 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-4 | 1297 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1349 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1438 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1498 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 1584 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 1646 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 1730 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 1791 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 1879 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 2554 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 2555 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 2634 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 1-4 | 38 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 8 | 4-5 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-5 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 4-6 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 433 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 811 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 873 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 987 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1086 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1246 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1282 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 1521 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 1583 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 1672 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 1738 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 1826 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 1888 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 1973 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2036 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 4-6 | 2037 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
