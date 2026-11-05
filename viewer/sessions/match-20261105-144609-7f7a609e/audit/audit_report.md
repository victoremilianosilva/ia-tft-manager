# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4328**
- Achados: **348**
- CRITICAL: 0 | HIGH: 23 | MEDIUM: 67 | LOW: 258

## Metadados da sessão

- Match ID: 7f7a609e-ff0b-4171-a858-de5ba388e52a
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 2cb097f284849b572c30178c174caacd646479212e770abf10a51f5f11eb30a4
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **3886**
- Entradas posteriores à eliminação ignoradas: **442**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 158 | 6 | 0 | 13 | 44 | 3 | 2 | não/inconclusivo | 0 |
| Jogador 6 | 113 | 7 | 16 | 21 | 56 | 7 | 3 | não/inconclusivo | 0 |
| Jogador 7 | 133 | 7 | 7 | 13 | 62 | 4 | 4 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 199 | 58 | 29 | 8 | 0 | 17 | 76 | 0.1008 | 13 | 37 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 3, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 2, ALL_IN::SELL: 3, FAST8::BUY: 17, FAST8::BUY_XP: 2, FAST8::ITEM: 4, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 19, FAST8::PASS: 7, FAST8::SELL: 12, STABILIZE::BUY: 38, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 18, STABILIZE::MOVE_BOARD: 31, STABILIZE::PASS: 10, STABILIZE::SELL: 14
- Jogador 1 — recompensas por ação: BUY: média 0.3614 (n=58), BUY_XP: média 0.0575 (n=8), ITEM: média 0.1691 (n=11), MOVE_BENCH: média 0.1237 (n=24), MOVE_BOARD: média -0.0035 (n=52), PASS: média -0.0576 (n=17), SELL: média -0.1738 (n=29)
| Jogador 2 | 159 | 39 | 15 | 4 | 0 | 19 | 70 | 0.0765 | 8 | 17 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 5, ALL_IN::MOVE_BENCH: 9, ALL_IN::PASS: 1, ALL_IN::SELL: 6, STABILIZE::BUY: 33, STABILIZE::BUY_XP: 4, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 27, STABILIZE::MOVE_BOARD: 34, STABILIZE::PASS: 18, STABILIZE::SELL: 9
- Jogador 2 — recompensas por ação: BUY: média 0.4251 (n=39), BUY_XP: média -0.0150 (n=4), ITEM: média 0.1567 (n=12), MOVE_BENCH: média -0.0269 (n=36), MOVE_BOARD: média -0.0027 (n=34), PASS: média -0.0668 (n=19), SELL: média -0.2600 (n=15)
| Jogador 3 | 129 | 33 | 10 | 1 | 1 | 22 | 57 | 0.1056 | 5 | 19 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::MOVE_BENCH: 7, ALL_IN::MOVE_BOARD: 6, ALL_IN::PASS: 3, ALL_IN::REROLL: 1, ALL_IN::SELL: 6, FAST8::BUY: 2, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 4, FAST8::PASS: 2, FAST8::SELL: 1, STABILIZE::BUY: 24, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 25, STABILIZE::PASS: 17, STABILIZE::SELL: 3
- Jogador 3 — recompensas por ação: BUY: média 0.5309 (n=33), BUY_XP: média 0.0200 (n=1), ITEM: média 0.1640 (n=5), MOVE_BENCH: média 0.0682 (n=22), MOVE_BOARD: média -0.0077 (n=35), PASS: média -0.1227 (n=22), REROLL: média -0.0700 (n=1), SELL: média -0.3200 (n=10)
| Jogador 4 | 160 | 44 | 16 | 0 | 0 | 17 | 76 | 0.0917 | 17 | 12 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::MOVE_BENCH: 8, ALL_IN::MOVE_BOARD: 6, ALL_IN::PASS: 5, ALL_IN::SELL: 6, STABILIZE::BUY: 37, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 22, STABILIZE::MOVE_BOARD: 40, STABILIZE::PASS: 12, STABILIZE::SELL: 10
- Jogador 4 — recompensas por ação: BUY: média 0.5200 (n=44), ITEM: média 0.1829 (n=7), MOVE_BENCH: média -0.0420 (n=30), MOVE_BOARD: média -0.0083 (n=46), PASS: média -0.1835 (n=17), SELL: média -0.2956 (n=16)
| Jogador 5 | 220 | 63 | 27 | 19 | 0 | 22 | 78 | 0.1137 | 18 | 49 |
- Jogador 5 — ações por estratégia: ECON::BUY: 3, ECON::MOVE_BENCH: 2, ECON::MOVE_BOARD: 5, ECON::PASS: 2, ECON::SELL: 1, FAST8::BUY: 27, FAST8::BUY_XP: 10, FAST8::ITEM: 7, FAST8::MOVE_BENCH: 5, FAST8::MOVE_BOARD: 37, FAST8::PASS: 12, FAST8::SELL: 11, STABILIZE::BUY: 28, STABILIZE::BUY_XP: 9, STABILIZE::ITEM: 3, STABILIZE::MOVE_BENCH: 6, STABILIZE::MOVE_BOARD: 14, STABILIZE::PASS: 5, STABILIZE::SELL: 14, WINSTREAK::BUY: 5, WINSTREAK::ITEM: 1, WINSTREAK::MOVE_BENCH: 2, WINSTREAK::MOVE_BOARD: 7, WINSTREAK::PASS: 3, WINSTREAK::SELL: 1
- Jogador 5 — recompensas por ação: BUY: média 0.4127 (n=63), BUY_XP: média 0.0153 (n=19), ITEM: média 0.1518 (n=11), MOVE_BENCH: média 0.3867 (n=15), MOVE_BOARD: média -0.0097 (n=63), PASS: média -0.0800 (n=22), SELL: média -0.2363 (n=27)
| Jogador 6 | 208 | 56 | 21 | 16 | 4 | 22 | 76 | 0.1064 | 14 | 34 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::ITEM: 4, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, ALL_IN::REROLL: 3, ALL_IN::SELL: 6, FAST8::BUY: 18, FAST8::BUY_XP: 4, FAST8::ITEM: 3, FAST8::MOVE_BENCH: 21, FAST8::MOVE_BOARD: 17, FAST8::PASS: 11, FAST8::SELL: 7, STABILIZE::BUY: 30, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 17, STABILIZE::MOVE_BOARD: 18, STABILIZE::PASS: 10, STABILIZE::REROLL: 1, STABILIZE::SELL: 8
- Jogador 6 — recompensas por ação: BUY: média 0.5707 (n=56), BUY_XP: média 0.0506 (n=16), ITEM: média 0.1331 (n=13), MOVE_BENCH: média -0.0072 (n=39), MOVE_BOARD: média -0.0176 (n=37), PASS: média -0.0823 (n=22), REROLL: média -0.0925 (n=4), SELL: média -0.4410 (n=21)
| Jogador 7 | 215 | 62 | 21 | 7 | 1 | 21 | 87 | 0.1303 | 11 | 44 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 11, ALL_IN::MOVE_BENCH: 9, ALL_IN::MOVE_BOARD: 4, ALL_IN::PASS: 1, ALL_IN::REROLL: 1, ALL_IN::SELL: 6, FAST8::BUY: 24, FAST8::BUY_XP: 4, FAST8::ITEM: 12, FAST8::MOVE_BENCH: 7, FAST8::MOVE_BOARD: 31, FAST8::PASS: 10, FAST8::SELL: 11, STABILIZE::BUY: 27, STABILIZE::BUY_XP: 3, STABILIZE::ITEM: 4, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 27, STABILIZE::PASS: 10, STABILIZE::SELL: 4
- Jogador 7 — recompensas por ação: BUY: média 0.5079 (n=62), BUY_XP: média -0.0486 (n=7), ITEM: média 0.1000 (n=16), MOVE_BENCH: média 0.1928 (n=25), MOVE_BOARD: média -0.0082 (n=62), PASS: média -0.0776 (n=21), REROLL: média -0.0700 (n=1), SELL: média -0.3500 (n=21)
| Jogador 8 | 234 | 67 | 36 | 21 | 4 | 20 | 73 | 0.0954 | 22 | 43 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 10, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 3, ALL_IN::OTHER: 1, ALL_IN::REROLL: 3, ALL_IN::SELL: 7, FAST8::BUY: 10, FAST8::BUY_XP: 5, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 21, FAST8::PASS: 7, FAST8::SELL: 6, LOSS_STREAK::BUY: 4, LOSS_STREAK::MOVE_BOARD: 1, LOSS_STREAK::SELL: 5, STABILIZE::BUY: 43, STABILIZE::BUY_XP: 16, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 11, STABILIZE::MOVE_BOARD: 35, STABILIZE::PASS: 13, STABILIZE::REROLL: 1, STABILIZE::SELL: 18
- Jogador 8 — recompensas por ação: BUY: média 0.4190 (n=67), BUY_XP: média 0.0590 (n=21), ITEM: média 0.1350 (n=12), MOVE_BENCH: média 0.1944 (n=16), MOVE_BOARD: média -0.0042 (n=57), OTHER: média -0.0200 (n=1), PASS: média -0.0775 (n=20), REROLL: média -0.0925 (n=4), SELL: média -0.2647 (n=36)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 14:46:14 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.5100 |  |
| Jogador 1 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 14:46:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 14:46:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-1 | 14:46:25 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 1 | 1-2 | 14:46:28 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 1 | 1-2 | 14:46:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-2 | 14:46:33 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.5300 |  |
| Jogador 1 | 1-3 | 14:46:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 14:46:37 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 14:46:37 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 1-3 | 14:46:39 | MOVE Board -> Board: Akali (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 1-3 | 14:46:40 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 1 | 1-3 | 14:46:40 | MOVE Board -> Board: Ornn (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 1-3 | 14:46:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 14:46:45 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 1.1100 |  |
| Jogador 1 | 1-4 | 14:46:46 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | 1-4 | 14:46:49 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.1800 |  |
| Jogador 1 | 1-4 | 14:46:50 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | -0.0400 |  |
| Jogador 1 | 1-4 | 14:46:51 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Ornn | 0.4900 |  |
| Jogador 1 | 2-1 | 14:46:54 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Diana | 0.3100 |  |
| Jogador 1 | 2-1 | 14:46:55 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.2600 |  |
| Jogador 1 | 2-1 | 14:46:55 | MOVE Board -> Board: Akali (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.0300 |  |
| Jogador 1 | 2-1 | 14:46:56 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.2200 |  |
| Jogador 1 | 2-1 | 14:46:59 | MOVE Board -> Board: Akali (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 14:47:00 | MOVE Board -> Board: Akali (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-2 | 14:47:04 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Diana | 0.8500 |  |
| Jogador 1 | 2-2 | 14:47:04 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Diana | -0.5200 |  |
| Jogador 1 | 2-2 | 14:47:05 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | — | DA_18_Diana | -0.1400 |  |
| Jogador 1 | 2-2 | 14:47:05 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | 0.3000 |  |
| Jogador 1 | 2-2 | 14:47:06 | MOVE Bench -> Board: Shen (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Diana | -0.3600 |  |
| Jogador 1 | 2-2 | 14:47:07 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Diana | -0.1200 |  |
| Jogador 1 | 2-2 | 14:47:08 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 14:47:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-3 | 14:47:16 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Diana | 0.1900 |  |
| Jogador 1 | 2-3 | 14:47:16 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Diana | 0.4200 |  |
| Jogador 1 | 2-3 | 14:47:17 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Diana | 0.2100 |  |
| Jogador 1 | 2-3 | 14:47:18 | MOVE Board -> Board: Warwick (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-3 | 14:47:18 | MOVE Board -> Board: Akali (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-3 | 14:47:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 14:47:29 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Inferno | DA_18_Diana | 0.9000 |  |
| Jogador 1 | 2-4 | 14:47:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-4 | 14:47:30 | MOVE Board -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-4 | 14:47:31 | MOVE Board -> Board: Xayah (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Diana | -0.0800 |  |
| Jogador 1 | 2-4 | 14:47:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Diana | 0.0000 |  |
| Jogador 1 | 2-5 | 14:47:42 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Akali_AD | 0.9500 |  |
| Jogador 1 | 2-5 | 14:47:43 | MOVE Bench -> Board: Kayle (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Akali_AD | -0.1200 |  |
| Jogador 1 | 2-5 | 14:47:44 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Akali_AD | 0.4300 |  |
| Jogador 1 | 2-5 | 14:47:44 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Inferno | DA_18_Akali_AD | -0.2200 |  |
| Jogador 1 | 2-5 | 14:47:45 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | -0.3000 |  |
| Jogador 1 | 2-5 | 14:47:45 | MOVE Board -> Board: Varus (i:2.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 2-5 | 14:47:45 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | 0.0900 |  |
| Jogador 1 | 2-5 | 14:47:46 | MOVE Board -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | -0.0200 |  |
| Jogador 1 | 2-5 | 14:47:46 | MOVE Bench -> Board: Grompe (i:4.0) <-> Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Inferno | DA_18_Akali_AD | -0.3900 |  |
| Jogador 1 | 2-6 | 14:47:58 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Inferno | DA_18_Diana | -0.5800 |  |
| Jogador 1 | 2-6 | 14:47:58 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Diana | 0.7200 |  |
| Jogador 1 | 2-6 | 14:47:59 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Varus (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Diana | 0.1400 |  |
| Jogador 1 | 2-6 | 14:47:59 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Varus (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Diana | 0.1500 |  |
| Jogador 1 | 2-6 | 14:48:00 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_18_Diana | -0.0300 |  |
| Jogador 1 | 2-6 | 14:48:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Diana | 0.1400 |  |
| Jogador 1 | 2-6 | 14:48:01 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Inferno | DA_18_Diana | -0.0900 |  |
| Jogador 1 | 2-6 | 14:48:01 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Inferno | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-6 | 14:48:02 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Inferno | DA_18_Diana | -0.0200 |  |
| Jogador 1 | 2-7 | 14:48:14 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Inferno | DA_18_Diana | 0.2400 |  |
| Jogador 1 | 2-7 | 14:48:14 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Inferno | DA_18_Diana | -0.0300 |  |
| Jogador 1 | 2-7 | 14:48:15 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Diana | 0.0400 |  |
| Jogador 1 | 2-7 | 14:48:15 | MOVE Bench -> Board: Grompe (i:4.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Diana | -0.7000 |  |
| Jogador 1 | 2-7 | 14:48:16 | MOVE Bench -> Board: Warwick (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Diana | -0.0800 |  |
| Jogador 1 | 2-7 | 14:48:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Diana | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-1 | 14:48:31 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Inferno | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 3-1 | 14:48:32 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Inferno | DA_Gromp18_AP | 0.7800 |  |
| Jogador 1 | 3-1 | 14:48:32 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Inferno | DA_Gromp18_AP | 0.4000 |  |
| Jogador 1 | 3-1 | 14:48:33 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Inferno | DA_Gromp18_AP | 0.1700 |  |
| Jogador 1 | 3-1 | 14:48:33 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Inferno | DA_Gromp18_AP | -0.0400 |  |
| Jogador 1 | 3-1 | 14:48:34 | MOVE Board -> Board: Master Yi (i:6.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Inferno | DA_Gromp18_AP | -0.1700 |  |
| Jogador 1 | 3-1 | 14:48:34 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Inferno | DA_Gromp18_AP | 0.1600 |  |
| Jogador 1 | 3-1 | 14:48:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 2 | Inferno | DA_Gromp18_AP | -0.0900 |  |
| Jogador 1 | 3-1 | 14:48:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 2 | Inferno | DA_Gromp18_AP | -0.0100 |  |
| Jogador 1 | 3-2 | 14:48:50 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_Gromp18_AP | 0.3900 |  |
| Jogador 1 | 3-2 | 14:48:51 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_Gromp18_AP | 0.0800 |  |
| Jogador 1 | 3-2 | 14:48:51 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_Gromp18_AP | 0.0100 |  |
| Jogador 1 | 3-2 | 14:48:52 | MOVE Board -> Board: Shen (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_Gromp18_AP | -0.0300 |  |
| Jogador 1 | 3-2 | 14:48:52 | MOVE Board -> Board: Varus (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_Gromp18_AP | 0.0000 |  |
| Jogador 1 | 3-2 | 14:48:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Inferno | DA_Gromp18_AP | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-3 | 14:49:10 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Inferno | DA_18_Ezreal | -0.5000 |  |
| Jogador 1 | 3-3 | 14:49:11 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Inferno | DA_18_Ezreal | 0.6400 |  |
| Jogador 1 | 3-3 | 14:49:11 | MOVE Board -> Board: Master Yi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Inferno | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-3 | 14:49:12 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Inferno | DA_18_Ezreal | -0.0200 |  |
| Jogador 1 | 3-3 | 14:49:12 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Inferno | DA_18_Ezreal | 0.0300 |  |
| Jogador 1 | 3-3 | 14:49:13 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Inferno | DA_18_Ezreal | 0.0000 |  |
| Jogador 1 | 3-3 | 14:49:13 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Inferno | DA_18_Ezreal | 0.0100 |  |
| Jogador 1 | 3-3 | 14:49:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Inferno | DA_18_Ezreal | 0.0100 |  |
| Jogador 1 | 3-3 | 14:49:14 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Inferno | DA_18_Ezreal | -0.0900 |  |
| Jogador 1 | 3-4 | 14:49:32 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Inferno | DA_18_Ezreal | -0.0400 |  |
| Jogador 1 | 3-4 | 14:49:32 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Inferno | DA_18_Shen | 0.8500 |  |
| Jogador 1 | 3-4 | 14:49:33 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Inferno | DA_18_Shen | 0.7200 |  |
| Jogador 1 | 3-4 | 14:49:33 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Inferno | DA_18_Shen | 0.0500 |  |
| Jogador 1 | 3-4 | 14:49:34 | MOVE Board -> Board: Shen (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-4 | 14:49:34 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-4 | 14:49:35 | MOVE Board -> Board: Varus (i:2.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-4 | 14:49:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 23 | 1 | Inferno | DA_18_Shen | -0.0600 |  |
| Jogador 1 | 3-5 | 14:49:55 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Inferno | DA_18_Shen | 0.2500 |  |
| Jogador 1 | 3-5 | 14:49:56 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 2 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-5 | 14:49:56 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Inferno | DA_18_Shen | 0.6900 |  |
| Jogador 1 | 3-5 | 14:49:56 | MOVE Bench -> Board: Shen (i:4.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Inferno | DA_18_Shen | 0.1100 |  |
| Jogador 1 | 3-5 | 14:49:57 | MOVE Board -> Board: Shen (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-5 | 14:49:57 | MOVE Board -> Board: Master Yi (i:6.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-5 | 14:49:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-6 | 14:50:19 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 2 | Inferno | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 3-6 | 14:50:20 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Inferno | DA_18_Shen | 0.0400 |  |
| Jogador 1 | 3-6 | 14:50:20 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-6 | 14:50:21 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 3-6 | 14:50:22 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-6 | 14:50:22 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-6 | 14:50:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 2 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Inferno | DA_18_Shen | 0.1800 |  |
| Jogador 1 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Inferno | DA_18_Shen | 0.1800 |  |
| Jogador 1 | 3-7 | 14:50:51 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-7 | 14:50:51 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 3-7 | 14:50:52 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Xayah (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Inferno | DA_18_Shen | -0.3800 |  |
| Jogador 1 | 3-7 | 14:50:52 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 3-7 | 14:50:53 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Inferno | DA_18_Shen | -0.1500 |  |
| Jogador 1 | 3-7 | 14:50:53 | MOVE Board -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-7 | 14:50:54 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-1 | 14:51:19 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-1 | 14:51:19 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 4 | Inferno | DA_18_Shen | 0.5600 |  |
| Jogador 1 | 4-1 | 14:51:20 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-1 | 14:51:21 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Inferno | DA_18_Shen | 0.3100 |  |
| Jogador 1 | 4-1 | 14:51:21 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-1 | 14:51:22 | MOVE Board -> Board: Varus (i:2.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-1 | 14:51:22 | MOVE Board -> Board: Shen (i:4.0) <-> Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-1 | 14:51:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Inferno | DA_18_Shen | -0.0800 |  |
| Jogador 1 | 4-2 | 14:51:52 | VENDEU: Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Inferno | DA_18_Shen | -0.2700 |  |
| Jogador 1 | 4-2 | 14:51:52 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Inferno | DA_18_Shen | 0.8900 |  |
| Jogador 1 | 4-2 | 14:51:53 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Inferno | DA_18_Shen | 0.4400 |  |
| Jogador 1 | 4-2 | 14:51:53 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 4-2 | 14:51:54 | MOVE Board -> Board: Xayah (i:2.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-2 | 14:51:54 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-2 | 14:51:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Inferno | DA_18_Shen | -0.2300 |  |
| Jogador 1 | 4-3 | 14:52:26 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Inferno | DA_18_Shen | -0.2200 |  |
| Jogador 1 | 4-3 | 14:52:26 | VENDEU: Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Inferno | DA_18_Shen | -0.8500 |  |
| Jogador 1 | 4-3 | 14:52:27 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Shen (i:8.0) (tabuleiro slot 25) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Inferno | DA_18_Shen | 0.1400 |  |
| Jogador 1 | 4-3 | 14:52:27 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Shen (i:8.0) (tabuleiro slot 25) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Inferno | DA_18_Shen | 0.1400 |  |
| Jogador 1 | 4-3 | 14:52:28 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Inferno | DA_18_Shen | -0.2200 |  |
| Jogador 1 | 4-3 | 14:52:29 | MOVE Board -> Board: Cassiopeia (i:6.0) <-> Shen (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-3 | 14:52:29 | MOVE Board -> Board: Shen (i:8.0) <-> Nidalee (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-3 | 14:52:30 | MOVE Board -> Board: Nidalee (i:8.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Inferno | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 4-3 | 14:52:30 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Inferno | DA_18_Shen | -0.1000 |  |
| Jogador 1 | 4-4 | 14:53:01 | VENDEU: Yunara (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 4-4 | 14:53:01 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Inferno | DA_18_Shen | 0.4500 |  |
| Jogador 1 | 4-4 | 14:53:02 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Inferno | DA_18_Shen | 0.0100 |  |
| Jogador 1 | 4-4 | 14:53:02 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 80 | 5 | Inferno | DA_18_Shen | -0.1100 |  |
| Jogador 1 | 4-4 | 14:53:03 | VENDEU: Ezreal (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-4 | 14:53:04 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-4 | 14:53:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Inferno | DA_18_Shen | 0.0600 |  |
| Jogador 1 | 4-4 | 14:53:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Inferno | DA_18_Shen | 0.6900 |  |
| Jogador 1 | 4-4 | 14:53:05 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Inferno | DA_18_Shen | 0.4000 |  |
| Jogador 1 | 4-5 | 14:53:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | 0.8000 |  |
| Jogador 1 | 4-5 | 14:53:38 | MOVE Board -> Board: Cascalho (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 4-5 | 14:53:39 | MOVE Board -> Board: Master Yi (i:6.0) <-> Varus (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-5 | 14:53:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Inferno | DA_18_Shen | -0.1100 |  |
| Jogador 1 | 4-6 | 14:54:15 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-6 | 14:54:15 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Inferno | DA_18_Shen | 0.8900 |  |
| Jogador 1 | 4-6 | 14:54:16 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 95 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 4-6 | 14:54:16 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Inferno | DA_18_Cassiopeia | 0.8200 |  |
| Jogador 1 | 4-6 | 14:54:17 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Inferno | DA_18_Cassiopeia | -0.3900 |  |
| Jogador 1 | 4-6 | 14:54:17 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Inferno | DA_18_Cassiopeia | 0.5400 |  |
| Jogador 1 | 4-6 | 14:54:18 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Inferno | DA_18_Cassiopeia | -0.2100 |  |
| Jogador 1 | 4-6 | 14:54:19 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Inferno | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 1 | 4-6 | 14:54:20 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 89 | 5 | Inferno | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 1 | 4-7 | 14:54:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Inferno | DA_KogMaw18_AD | 1.0200 |  |
| Jogador 1 | 4-7 | 14:54:56 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Inferno | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 1 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Inferno | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 4-7 | 14:54:57 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Inferno | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 1 | 4-7 | 14:54:58 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 1 | 4-7 | 14:54:58 | MOVE Bench -> Board: Rengar (i:6.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 1 | 4-7 | 14:54:59 | MOVE Board -> Board: Rengar (i:6.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-7 | 14:54:59 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Inferno | DA_KogMaw18_AD | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 5-1 | 14:55:34 | VENDEU: Cassiopeia (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Inferno | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 1 | 5-1 | 14:55:35 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Inferno | DA_KogMaw18_AD | 0.9100 |  |
| Jogador 1 | 5-1 | 14:55:36 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Inferno | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 5-1 | 14:55:36 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 116 | 5 | Inferno | DA_18_Shen | -0.6000 |  |
| Jogador 1 | 5-1 | 14:55:37 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Inferno | DA_18_Shen | 0.2200 |  |
| Jogador 1 | 5-1 | 14:55:37 | MOVE Board -> Board: Cascalho (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-1 | 14:55:38 | MOVE Board -> Board: Master Yi (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 5-1 | 14:55:38 | MOVE Board -> Board: Xayah (i:2.0) <-> Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 5-1 | 14:55:39 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Inferno | DA_18_Shen | -0.1900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 5-2 | 14:56:17 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Inferno | DA_18_Shen | -0.0600 |  |
| Jogador 1 | 5-2 | 14:56:18 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Inferno | DA_18_Shen | 0.9800 |  |
| Jogador 1 | 5-2 | 14:56:18 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Inferno | DA_18_Shen | -0.5600 |  |
| Jogador 1 | 5-2 | 14:56:19 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Inferno | DA_18_Shen | 0.4900 |  |
| Jogador 1 | 5-2 | 14:56:19 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Inferno | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 5-2 | 14:56:19 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Inferno | DA_18_Shen | 0.4400 |  |
| Jogador 1 | 5-2 | 14:56:20 | MOVE Board -> Board: Shen (i:8.0) <-> Nidalee (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Inferno | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 5-2 | 14:56:20 | MOVE Board -> Board: Nidalee (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Inferno | DA_18_Shen | -0.0300 |  |
| Jogador 1 | 5-2 | 14:56:21 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Inferno | DA_18_Shen | 0.0700 |  |
| Jogador 2 | ? | 14:46:14 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 14:46:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 14:46:21 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 14:46:21 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 14:46:25 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5700 |  |
| Jogador 2 | 1-2 | 14:46:28 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 14:46:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 14:46:33 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.4700 |  |
| Jogador 2 | 1-3 | 14:46:36 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 14:46:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 14:46:37 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 1-3 | 14:46:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-3 | 14:46:41 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.5500 |  |
| Jogador 2 | 1-4 | 14:46:45 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 14:46:46 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 1-4 | 14:46:49 | MOVE Bench -> Board: Vi (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.3900 |  |
| Jogador 2 | 1-4 | 14:46:50 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-4 | 14:46:51 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 14:46:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 2-1 | 14:46:55 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-1 | 14:46:55 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 14:46:56 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 14:46:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 14:47:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Veigar | 0.2400 |  |
| Jogador 2 | 2-2 | 14:47:04 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-2 | 14:47:05 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-2 | 14:47:05 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-2 | 14:47:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-2 | 14:47:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 14:47:08 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-3 | 14:47:16 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 2-3 | 14:47:16 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 2-3 | 14:47:16 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-3 | 14:47:17 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 14:47:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 2-3 | 14:47:18 | MOVE Board -> Board: Sejuani (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 2-3 | 14:47:19 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 2-3 | 14:47:19 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 14:47:20 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-4 | 14:47:29 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-4 | 14:47:29 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-4 | 14:47:30 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 2-4 | 14:47:31 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.4100 |  |
| Jogador 2 | 2-4 | 14:47:31 | MOVE Bench -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | -0.3300 |  |
| Jogador 2 | 2-4 | 14:47:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-5 | 14:47:42 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Veigar | -0.8400 |  |
| Jogador 2 | 2-5 | 14:47:43 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | 0.9000 |  |
| Jogador 2 | 2-5 | 14:47:44 | MOVE Bench -> Board: Veigar (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 14:47:44 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-5 | 14:47:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 14:47:58 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-6 | 14:47:58 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | 0.7600 |  |
| Jogador 2 | 2-6 | 14:47:59 | MOVE Bench -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | -0.2400 |  |
| Jogador 2 | 2-6 | 14:47:59 | MOVE Bench -> Board: Veigar (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | 0.0400 |  |
| Jogador 2 | 2-6 | 14:48:00 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | -0.4200 |  |
| Jogador 2 | 2-6 | 14:48:00 | MOVE Bench -> Board: Vi (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | -0.3500 |  |
| Jogador 2 | 2-6 | 14:48:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 2-7 | 14:48:14 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 2-7 | 14:48:14 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_Fiddlesticks18 | -0.5800 |  |
| Jogador 2 | 2-7 | 14:48:15 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | 0.2900 |  |
| Jogador 2 | 2-7 | 14:48:15 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Rek'Sai (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 2 | 2-7 | 14:48:16 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Rek'Sai (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 2 | 2-7 | 14:48:16 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 2 | 2-7 | 14:48:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 2-7 | 14:48:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Colosso | DA_Fiddlesticks18 | 0.0800 |  |
| Jogador 2 | 2-7 | 14:48:17 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Colosso | DA_Fiddlesticks18 | 0.4500 |  |
| Jogador 2 | 3-1 | 14:48:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Fiddlesticks18 | 0.8100 |  |
| Jogador 2 | 3-1 | 14:48:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-1 | 14:48:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 2 | 3-1 | 14:48:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Fiddlesticks18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-2 | 14:48:50 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-2 | 14:48:51 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-2 | 14:48:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_Fiddlesticks18 | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-3 | 14:49:10 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-3 | 14:49:11 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 2 | 3-3 | 14:49:11 | MOVE Board -> Board: Rakan (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-3 | 14:49:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-4 | 14:49:32 | MOVE Bench -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 2 | 3-4 | 14:49:32 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | -0.3900 |  |
| Jogador 2 | 3-4 | 14:49:33 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-4 | 14:49:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_Fiddlesticks18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-5 | 14:49:55 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-5 | 14:49:56 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_Fiddlesticks18 | 0.8700 |  |
| Jogador 2 | 3-5 | 14:49:56 | MOVE Board -> Board: Yorick (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-5 | 14:49:56 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-5 | 14:49:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 2 | 3-5 | 14:49:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Colosso | DA_Fiddlesticks18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-6 | 14:50:19 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-6 | 14:50:20 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Colosso | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 2 | 3-6 | 14:50:20 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 2 | 3-6 | 14:50:21 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 2 | 3-6 | 14:50:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Colosso | DA_Fiddlesticks18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 2 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.2200 |  |
| Jogador 2 | 3-7 | 14:50:51 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | -0.2900 |  |
| Jogador 2 | 3-7 | 14:50:51 | MOVE Bench -> Board: Vi (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 2 | 3-7 | 14:50:52 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 2 | 3-7 | 14:50:52 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 3-7 | 14:50:53 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 2 | 3-7 | 14:50:53 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-1 | 14:51:19 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 85 | 5 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 2 | 4-1 | 14:51:19 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Colosso | DA_18_Rakan | 0.9600 |  |
| Jogador 2 | 4-1 | 14:51:20 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Colosso | DA_18_Rakan | 0.5100 |  |
| Jogador 2 | 4-1 | 14:51:21 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Colosso | DA_18_Rakan | 0.4700 |  |
| Jogador 2 | 4-1 | 14:51:21 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 2 | 4-1 | 14:51:22 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 2 | 4-1 | 14:51:22 | MOVE Board -> Board: Yorick (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 2 | 4-1 | 14:51:23 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 80 | 5 | Colosso | DA_18_Rakan | -0.1000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-2 | 14:51:52 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 2 | 4-2 | 14:51:52 | MOVE Board -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 2 | 4-2 | 14:51:53 | PASSOU TURNO | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 90 | 5 | Colosso | DA_18_Rakan | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-3 | 14:52:26 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Colosso | DA_Fiddlesticks18 | -0.5900 |  |
| Jogador 2 | 4-3 | 14:52:26 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Colosso | DA_18_Sejuani | 0.9600 |  |
| Jogador 2 | 4-3 | 14:52:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Colosso | DA_18_Sejuani | 0.3000 |  |
| Jogador 2 | 4-3 | 14:52:27 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Colosso | DA_18_Sejuani | 0.4100 |  |
| Jogador 2 | 4-3 | 14:52:28 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Sejuani | 0.0200 |  |
| Jogador 2 | 4-3 | 14:52:29 | MOVE Board -> Board: Krugue (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Sejuani | 0.0000 |  |
| Jogador 2 | 4-3 | 14:52:29 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Sejuani | -0.0100 |  |
| Jogador 2 | 4-3 | 14:52:30 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Colosso | DA_18_Sejuani | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-4 | 14:53:01 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 115 | 5 | Colosso | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 2 | 4-4 | 14:53:01 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Colosso | DA_18_Azir | 0.9000 |  |
| Jogador 2 | 4-4 | 14:53:02 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Colosso | DA_18_Azir | 0.0100 |  |
| Jogador 2 | 4-4 | 14:53:02 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Colosso | DA_18_Azir | 0.8900 |  |
| Jogador 2 | 4-4 | 14:53:03 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Colosso | DA_18_Azir | 0.2800 |  |
| Jogador 2 | 4-4 | 14:53:04 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Colosso | DA_18_Azir | -0.1400 |  |
| Jogador 2 | 4-4 | 14:53:05 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Colosso | DA_18_Azir | -0.2700 |  |
| Jogador 2 | 4-4 | 14:53:05 | MOVE Board -> Board: Karma (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Colosso | DA_18_Azir | 0.1500 |  |
| Jogador 2 | 4-4 | 14:53:05 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 108 | 5 | Colosso | DA_18_Azir | -0.0100 |  |
| Jogador 2 | 4-5 | 14:53:38 | VENDEU: Rek'Sai (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Colosso | DA_18_Azir | -0.6000 |  |
| Jogador 2 | 4-5 | 14:53:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Colosso | DA_18_Azir | 0.4200 |  |
| Jogador 2 | 4-5 | 14:53:39 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Yorick (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Colosso | DA_18_Azir | 0.1600 |  |
| Jogador 2 | 4-5 | 14:53:40 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Yorick (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Colosso | DA_18_Azir | 0.1400 |  |
| Jogador 2 | 4-5 | 14:53:40 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Yorick (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Colosso | DA_18_Azir | 0.1600 |  |
| Jogador 2 | 4-5 | 14:53:41 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 122 | 5 | Colosso | DA_18_Azir | 0.0200 |  |
| Jogador 2 | 4-5 | 14:53:41 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Colosso | DA_18_Azir | 0.5300 |  |
| Jogador 2 | 4-5 | 14:53:42 | MOVE Bench -> Board: Rakan (i:2.0) <-> Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Colosso | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 4-5 | 14:53:42 | MOVE Bench -> Board: Krugue (i:6.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Colosso | DA_18_Azir | -0.4100 |  |
| Jogador 2 | 4-6 | 14:54:15 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Colosso | DA_18_Azir | 0.0700 |  |
| Jogador 2 | 4-6 | 14:54:15 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Colosso | DA_18_Azir | -0.1000 |  |
| Jogador 2 | 4-6 | 14:54:16 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Colosso | DA_18_Azir | 0.0600 |  |
| Jogador 2 | 4-6 | 14:54:16 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Colosso | DA_18_Azir | -0.0100 |  |
| Jogador 2 | 4-6 | 14:54:17 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Colosso | DA_18_Azir | -0.2300 |  |
| Jogador 2 | 4-6 | 14:54:17 | MOVE Bench -> Board: Rakan (i:2.0) <-> Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Colosso | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 4-6 | 14:54:18 | MOVE Bench -> Board: Krugue (i:6.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Colosso | DA_18_Azir | -0.4100 |  |
| Jogador 2 | 4-6 | 14:54:19 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Colosso | DA_18_Azir | 0.0500 |  |
| Jogador 2 | 4-6 | 14:54:20 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Colosso | DA_18_Azir | 0.0100 |  |
| Jogador 2 | 4-7 | 14:54:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Colosso | DA_18_Azir | 0.9800 |  |
| Jogador 2 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Colosso | DA_18_Azir | 0.0600 |  |
| Jogador 2 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Colosso | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 4-7 | 14:54:57 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 145 | 5 | Colosso | DA_18_Azir | -0.6100 |  |
| Jogador 2 | 4-7 | 14:54:58 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Azir | -0.2000 |  |
| Jogador 2 | 4-7 | 14:54:58 | MOVE Bench -> Board: Rakan (i:2.0) <-> Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Azir | 0.1000 |  |
| Jogador 2 | 4-7 | 14:54:59 | MOVE Bench -> Board: Krugue (i:6.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Azir | -0.4100 |  |
| Jogador 2 | 4-7 | 14:54:59 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Azir | -0.3100 |  |
| Jogador 2 | 4-7 | 14:55:00 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Colosso | DA_18_Azir | -0.6100 |  |
| Jogador 3 | ? | 14:46:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 14:46:20 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 14:46:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 14:46:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 1-2 | 14:46:28 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 14:46:28 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 14:46:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 14:46:33 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 1-3 | 14:46:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 14:46:41 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.7100 |  |
| Jogador 3 | 1-4 | 14:46:45 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 3 | 1-4 | 14:46:46 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 14:46:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 14:46:51 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 2-1 | 14:46:54 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 2-1 | 14:46:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 14:47:04 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 3 | 2-2 | 14:47:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-3 | 14:47:16 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Akali_AD | 1.0800 |  |
| Jogador 3 | 2-3 | 14:47:16 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | — | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 2-3 | 14:47:16 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | — | DA_18_Akali_AD | 0.3700 |  |
| Jogador 3 | 2-3 | 14:47:17 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 2-3 | 14:47:18 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 2-3 | 14:47:18 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 14:47:19 | MOVE Board -> Board: Shen (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-3 | 14:47:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 2-3 | 14:47:20 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 2-4 | 14:47:29 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Devastador | DA_18_Akali_AD | 1.0200 |  |
| Jogador 3 | 2-4 | 14:47:29 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-4 | 14:47:30 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 14:47:31 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-4 | 14:47:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Devastador | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-5 | 14:47:42 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 2-5 | 14:47:43 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | 0.4400 |  |
| Jogador 3 | 2-5 | 14:47:44 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-5 | 14:47:44 | MOVE Board -> Board: Shen (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-5 | 14:47:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Devastador | DA_18_Akali_AD | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-6 | 14:47:58 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | 1.0600 |  |
| Jogador 3 | 2-6 | 14:47:58 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 14:47:59 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Devastador | DA_18_Yorick | 0.3200 |  |
| Jogador 3 | 2-6 | 14:47:59 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Devastador | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-6 | 14:48:00 | MOVE Board -> Board: Shen (i:4.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Devastador | DA_18_Yorick | -0.0100 |  |
| Jogador 3 | 2-6 | 14:48:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Devastador | DA_18_Yorick | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 2-7 | 14:48:14 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Devastador | DA_18_Yorick | 0.2600 |  |
| Jogador 3 | 2-7 | 14:48:14 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Devastador | DA_18_Yorick | 0.8400 |  |
| Jogador 3 | 2-7 | 14:48:15 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Devastador | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-7 | 14:48:15 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Devastador | DA_18_Yorick | -0.0100 |  |
| Jogador 3 | 2-7 | 14:48:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Devastador | DA_18_Yorick | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-1 | 14:48:31 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Devastador | DA_18_RekSai | 0.8900 |  |
| Jogador 3 | 3-1 | 14:48:32 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Devastador | DA_18_RekSai | 0.0000 |  |
| Jogador 3 | 3-1 | 14:48:32 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Devastador | DA_18_RekSai | -0.0100 |  |
| Jogador 3 | 3-1 | 14:48:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Devastador | DA_18_RekSai | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 14:48:50 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Devastador | DA_18_RekSai | 0.3100 |  |
| Jogador 3 | 3-2 | 14:48:51 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Devastador | DA_18_RekSai | -0.0800 |  |
| Jogador 3 | 3-2 | 14:48:51 | MOVE Board -> Board: Shen (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Devastador | DA_18_RekSai | 0.0000 |  |
| Jogador 3 | 3-2 | 14:48:52 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Devastador | DA_18_RekSai | 0.0000 |  |
| Jogador 3 | 3-2 | 14:48:52 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Devastador | DA_18_RekSai | -0.0200 |  |
| Jogador 3 | 3-2 | 14:48:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Devastador | DA_18_RekSai | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-3 | 14:49:10 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_RekSai | 0.6000 |  |
| Jogador 3 | 3-3 | 14:49:11 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_RekSai | -0.0400 |  |
| Jogador 3 | 3-3 | 14:49:11 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_RekSai | -0.0200 |  |
| Jogador 3 | 3-3 | 14:49:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Devastador | DA_18_RekSai | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-4 | 14:49:32 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_RekSai | 0.3100 |  |
| Jogador 3 | 3-4 | 14:49:32 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_RekSai | 0.0800 |  |
| Jogador 3 | 3-4 | 14:49:33 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_RekSai | -0.0200 |  |
| Jogador 3 | 3-4 | 14:49:33 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_RekSai | -0.0800 |  |
| Jogador 3 | 3-4 | 14:49:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Devastador | DA_18_RekSai | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-5 | 14:49:55 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 76 | 5 | Devastador | DA_18_RekSai | -0.4400 |  |
| Jogador 3 | 3-5 | 14:49:56 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 75 | 5 | Devastador | DA_18_RekSai | 0.3200 |  |
| Jogador 3 | 3-5 | 14:49:56 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 78 | 5 | Devastador | DA_18_Akali_AD | -0.8500 |  |
| Jogador 3 | 3-5 | 14:49:56 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Devastador | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 3-5 | 14:49:57 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 14:49:57 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-5 | 14:49:58 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 14:49:58 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-5 | 14:49:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 77 | 5 | Devastador | DA_18_Akali_AD | -0.0700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-6 | 14:50:19 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Devastador | DA_18_Akali_AD | 0.4800 |  |
| Jogador 3 | 3-6 | 14:50:20 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Devastador | DA_18_Akali_AD | -0.2200 |  |
| Jogador 3 | 3-6 | 14:50:20 | MOVE Board -> Board: Warwick (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 14:50:21 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 14:50:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Devastador | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Akali_AD | 0.1100 |  |
| Jogador 3 | 3-7 | 14:50:51 | VENDEU: Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 97 | 5 | Devastador | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-7 | 14:50:51 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Akali_AD | 0.3000 |  |
| Jogador 3 | 3-7 | 14:50:52 | MOVE Bench -> Board: Diana (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-7 | 14:50:52 | MOVE Board -> Board: Diana (i:6.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 14:50:53 | MOVE Board -> Board: Warwick (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 14:50:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Akali_AD | -0.1100 |  |
| Jogador 3 | 4-1 | 14:51:19 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 109 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-1 | 14:51:19 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | 0.8700 |  |
| Jogador 3 | 4-1 | 14:51:20 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 4-1 | 14:51:21 | MOVE Bench -> Board: Diana (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 4-1 | 14:51:21 | MOVE Bench -> Board: Warwick (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 4-1 | 14:51:22 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 4-1 | 14:51:22 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 4-1 | 14:51:23 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 107 | 5 | Devastador | DA_18_Akali_AD | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-2 | 14:51:52 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Devastador | DA_18_Akali_AD | -0.5100 |  |
| Jogador 3 | 4-2 | 14:51:52 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | 0.1900 |  |
| Jogador 3 | 4-2 | 14:51:53 | MOVE Board -> Board: Shen (i:4.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 14:51:53 | MOVE Bench -> Board: Diana (i:6.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 4-2 | 14:51:54 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 4-2 | 14:51:54 | MOVE Board -> Board: Diana (i:6.0) <-> Rek'Sai (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 14:51:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Devastador | DA_18_Akali_AD | -0.5100 |  |
| Jogador 3 | 4-3 | 14:52:26 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-3 | 14:52:26 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Devastador | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 4-3 | 14:52:27 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Devastador | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 4-3 | 14:52:27 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 14:52:28 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Devastador | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 4-3 | 14:52:29 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Devastador | DA_18_Akali_AD | -0.7000 |  |
| Jogador 3 | 4-3 | 14:52:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Devastador | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 4-3 | 14:52:30 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 14:52:30 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 14:53:01 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 148 | 5 | Devastador | DA_18_Akali_AD | -0.6500 |  |
| Jogador 3 | 4-4 | 14:53:01 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Devastador | DA_18_Akali_AD | 0.5200 |  |
| Jogador 3 | 4-4 | 14:53:02 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 4-4 | 14:53:02 | MOVE Bench -> Board: Warwick (i:4.0) <-> Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Devastador | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 4-4 | 14:53:03 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Rek'Sai (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Devastador | DA_18_Akali_AD | -0.6300 |  |
| Jogador 3 | 4-4 | 14:53:04 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Devastador | DA_18_Akali_AD | -0.3500 |  |
| Jogador 3 | 4-4 | 14:53:05 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Devastador | DA_18_Akali_AD | -0.5700 |  |
| Jogador 3 | 4-5 | 14:53:38 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 161 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 14:53:38 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Devastador | DA_18_Akali_AD | 1.0700 |  |
| Jogador 3 | 4-5 | 14:53:39 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Devastador | DA_18_Akali_AD | 0.5100 |  |
| Jogador 3 | 4-5 | 14:53:40 | COMPROU: Elise (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Devastador | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 4-5 | 14:53:40 | MOVE Board -> Board: Warwick (i:4.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 14:53:41 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-5 | 14:53:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 157 | 5 | Devastador | DA_18_Akali_AD | -0.5800 |  |
| Jogador 4 | ? | 14:46:14 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5900 |  |
| Jogador 4 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:46:20 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 14:46:21 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 14:46:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 4 | 1-2 | 14:46:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 14:46:33 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4000 |  |
| Jogador 4 | 1-3 | 14:46:36 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 14:46:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 14:46:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 4 | 1-3 | 14:46:39 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-3 | 14:46:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 1-3 | 14:46:40 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 1-3 | 14:46:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-4 | 14:46:45 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 4 | 1-4 | 14:46:46 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 4 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 4 | 1-4 | 14:46:48 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 1-4 | 14:46:49 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 4 | 1-4 | 14:46:50 | MOVE Board -> Board: Yorick (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 1-4 | 14:46:51 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | -0.1100 |  |
| Jogador 4 | 2-1 | 14:46:54 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Yorick | 0.2400 |  |
| Jogador 4 | 2-1 | 14:46:55 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Yorick | -0.0300 |  |
| Jogador 4 | 2-1 | 14:46:55 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 2-1 | 14:46:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 2-2 | 14:47:04 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 4 | 2-2 | 14:47:04 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 4 | 2-2 | 14:47:05 | MOVE Bench -> Board: Camille (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 4 | 2-2 | 14:47:05 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.1200 |  |
| Jogador 4 | 2-2 | 14:47:06 | MOVE Board -> Board: Camille (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-2 | 14:47:07 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 4 | 2-2 | 14:47:08 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 14:47:16 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 4 | 2-3 | 14:47:16 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 4 | 2-3 | 14:47:16 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 14:47:17 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_18_Akali_AD | -0.1400 |  |
| Jogador 4 | 2-3 | 14:47:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | — | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-4 | 14:47:29 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | 0.8000 |  |
| Jogador 4 | 2-4 | 14:47:29 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | 0.8400 |  |
| Jogador 4 | 2-4 | 14:47:30 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Akali_AD | 0.1500 |  |
| Jogador 4 | 2-4 | 14:47:31 | MOVE Board -> Board: Veigar (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Akali_AD | -0.2900 |  |
| Jogador 4 | 2-4 | 14:47:31 | MOVE Board -> Board: Camille (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 2-4 | 14:47:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-5 | 14:47:42 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Camille | -0.5800 |  |
| Jogador 4 | 2-5 | 14:47:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Camille | 0.9100 |  |
| Jogador 4 | 2-5 | 14:47:44 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Camille | -0.0400 |  |
| Jogador 4 | 2-5 | 14:47:44 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Camille | 0.8400 |  |
| Jogador 4 | 2-5 | 14:47:45 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Camille | -0.5200 |  |
| Jogador 4 | 2-5 | 14:47:45 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Camille | 0.1500 |  |
| Jogador 4 | 2-5 | 14:47:45 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Camille | 0.3600 |  |
| Jogador 4 | 2-5 | 14:47:46 | MOVE Board -> Board: Varus (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-5 | 14:47:46 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Camille | -0.0100 |  |
| Jogador 4 | 2-6 | 14:47:58 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_18_Rakan | 0.8700 |  |
| Jogador 4 | 2-6 | 14:47:58 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Colosso | DA_18_Xayah | 0.9500 |  |
| Jogador 4 | 2-6 | 14:47:59 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_18_Xayah | 0.3200 |  |
| Jogador 4 | 2-6 | 14:47:59 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_18_Rakan | 0.9000 |  |
| Jogador 4 | 2-6 | 14:48:00 | MOVE Board -> Board: Rakan (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-6 | 14:48:00 | MOVE Board -> Board: Veigar (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 2-6 | 14:48:01 | MOVE Board -> Board: Camille (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 2-6 | 14:48:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_18_Rakan | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-7 | 14:48:14 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | 0.3100 |  |
| Jogador 4 | 2-7 | 14:48:14 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | 0.1800 |  |
| Jogador 4 | 2-7 | 14:48:15 | MOVE Bench -> Board: Yorick (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | 0.0900 |  |
| Jogador 4 | 2-7 | 14:48:15 | MOVE Bench -> Board: Camille (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | -0.7800 |  |
| Jogador 4 | 2-7 | 14:48:16 | MOVE Bench -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | 0.0400 |  |
| Jogador 4 | 2-7 | 14:48:16 | MOVE Bench -> Board: Yorick (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | 0.0800 |  |
| Jogador 4 | 2-7 | 14:48:17 | MOVE Bench -> Board: Camille (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | -0.7800 |  |
| Jogador 4 | 2-7 | 14:48:17 | MOVE Bench -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | 0.0500 |  |
| Jogador 4 | 2-7 | 14:48:17 | MOVE Bench -> Board: Yorick (i:2.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Xayah | 0.0900 |  |
| Jogador 4 | 3-1 | 14:48:31 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Xayah | 0.8800 |  |
| Jogador 4 | 3-1 | 14:48:32 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Xayah | 0.2500 |  |
| Jogador 4 | 3-1 | 14:48:32 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Xayah | 0.5900 |  |
| Jogador 4 | 3-1 | 14:48:33 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Xayah | 0.5800 |  |
| Jogador 4 | 3-1 | 14:48:33 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_18_Yorick | 0.3200 |  |
| Jogador 4 | 3-1 | 14:48:34 | MOVE Board -> Board: Yorick (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-1 | 14:48:34 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 3-1 | 14:48:34 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Colosso | DA_18_Yorick | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-2 | 14:48:50 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-2 | 14:48:51 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Colosso | DA_18_Yorick | 0.0200 |  |
| Jogador 4 | 3-2 | 14:48:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 3-2 | 14:48:52 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 3-2 | 14:48:52 | MOVE Board -> Board: Yorick (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 3-2 | 14:48:53 | MOVE Board -> Board: Varus (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Rakan | 0.0200 |  |
| Jogador 4 | 3-2 | 14:48:53 | MOVE Board -> Board: Rakan (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Rakan | -0.3100 |  |
| Jogador 4 | 3-2 | 14:48:54 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 3-2 | 14:48:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Rakan | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-3 | 14:49:10 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 4 | Colosso | DA_18_Rakan | -0.5900 |  |
| Jogador 4 | 3-3 | 14:49:11 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Rakan | 0.8300 |  |
| Jogador 4 | 3-3 | 14:49:11 | MOVE Bench -> Board: Yorick (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Yorick | 0.2100 |  |
| Jogador 4 | 3-3 | 14:49:12 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 4 | 3-3 | 14:49:12 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Yorick | 0.0800 |  |
| Jogador 4 | 3-3 | 14:49:13 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 3-3 | 14:49:13 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Rakan | 0.1300 |  |
| Jogador 4 | 3-3 | 14:49:14 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 3-3 | 14:49:14 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 4 | Colosso | DA_18_Rakan | -0.1000 |  |
| Jogador 4 | 3-4 | 14:49:32 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Colosso | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 3-4 | 14:49:32 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Colosso | DA_18_Rakan | 0.9000 |  |
| Jogador 4 | 3-4 | 14:49:33 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Colosso | DA_18_Rakan | 0.3200 |  |
| Jogador 4 | 3-4 | 14:49:33 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Colosso | DA_18_Rakan | 0.0100 |  |
| Jogador 4 | 3-4 | 14:49:34 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Colosso | DA_18_Rakan | 0.1200 |  |
| Jogador 4 | 3-4 | 14:49:34 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 4 | 3-4 | 14:49:35 | MOVE Board -> Board: Yorick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Colosso | DA_18_Rakan | -0.0200 |  |
| Jogador 4 | 3-4 | 14:49:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Colosso | DA_18_Rakan | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-5 | 14:49:55 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 80 | 5 | Colosso | DA_18_Yorick | 0.8700 |  |
| Jogador 4 | 3-5 | 14:49:56 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 85 | 5 | Colosso | DA_18_Yorick | -0.6000 |  |
| Jogador 4 | 3-5 | 14:49:56 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 83 | 5 | Colosso | DA_18_Yorick | 0.8400 |  |
| Jogador 4 | 3-5 | 14:49:56 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 83 | 5 | Colosso | DA_18_Yorick | -0.0800 |  |
| Jogador 4 | 3-5 | 14:49:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 83 | 5 | Colosso | DA_18_Yorick | -0.0500 |  |
| Jogador 4 | 3-5 | 14:49:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 83 | 5 | Colosso | DA_18_Yorick | -0.1700 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-6 | 14:50:19 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Colosso | DA_18_Yorick | -0.4200 |  |
| Jogador 4 | 3-6 | 14:50:20 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Colosso | DA_18_Yorick | 0.9400 |  |
| Jogador 4 | 3-6 | 14:50:20 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Colosso | DA_18_Yorick | 0.3400 |  |
| Jogador 4 | 3-6 | 14:50:21 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Colosso | DA_18_Yorick | -0.7700 |  |
| Jogador 4 | 3-6 | 14:50:22 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Colosso | DA_18_Yorick | 0.3200 |  |
| Jogador 4 | 3-6 | 14:50:22 | MOVE Bench -> Board: Varus (i:2.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Colosso | DA_18_Yorick | -0.5400 |  |
| Jogador 4 | 3-6 | 14:50:23 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Colosso | DA_18_Yorick | 0.2200 |  |
| Jogador 4 | 3-6 | 14:50:23 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Colosso | DA_18_Yorick | 0.0800 |  |
| Jogador 4 | 3-6 | 14:50:24 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 4 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Colosso | DA_18_Yorick | 0.2100 |  |
| Jogador 4 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Colosso | DA_18_Yorick | 0.2500 |  |
| Jogador 4 | 3-7 | 14:50:51 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Colosso | DA_18_Yorick | -0.5900 |  |
| Jogador 4 | 3-7 | 14:50:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Yorick | 0.9000 |  |
| Jogador 4 | 3-7 | 14:50:52 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Yorick (i:4.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Yorick | 0.1300 |  |
| Jogador 4 | 3-7 | 14:50:52 | EQUIP_FROM_INVENTORY: TFT_Item_Leviathan -> Diana (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Yorick | 0.1300 |  |
| Jogador 4 | 3-7 | 14:50:53 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 106 | 5 | Colosso | DA_18_Yorick | 0.0100 |  |
| Jogador 4 | 3-7 | 14:50:53 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Yorick | 0.3300 |  |
| Jogador 4 | 3-7 | 14:50:54 | MOVE Bench -> Board: Akali (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Colosso | DA_18_Yorick | -0.1900 |  |
| Jogador 4 | 4-1 | 14:51:19 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Colosso | DA_18_Yorick | -0.1000 |  |
| Jogador 4 | 4-1 | 14:51:19 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Colosso | DA_18_Yorick | 0.7600 |  |
| Jogador 4 | 4-1 | 14:51:20 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Colosso | DA_18_Yorick | -0.5600 |  |
| Jogador 4 | 4-1 | 14:51:21 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Colosso | DA_18_Yorick | 0.3900 |  |
| Jogador 4 | 4-1 | 14:51:21 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-1 | 14:51:22 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 4-1 | 14:51:22 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Colosso | DA_18_Yorick | -0.5100 |  |
| Jogador 4 | 4-2 | 14:51:52 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Colosso | DA_18_Yorick | -0.6800 |  |
| Jogador 4 | 4-2 | 14:51:52 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Colosso | DA_18_Yorick | 0.1700 |  |
| Jogador 4 | 4-2 | 14:51:53 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-2 | 14:51:53 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Colosso | DA_18_Yorick | -0.6100 |  |
| Jogador 4 | 4-2 | 14:51:54 | MOVE Bench -> Board: Xayah (i:2.0) <-> Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Colosso | DA_18_Yorick | -0.3500 |  |
| Jogador 4 | 4-2 | 14:51:54 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Colosso | DA_18_Yorick | -0.5300 |  |
| Jogador 4 | 4-3 | 14:52:26 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Colosso | DA_18_Yorick | -0.0500 |  |
| Jogador 4 | 4-3 | 14:52:26 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Yorick | 0.0100 |  |
| Jogador 4 | 4-3 | 14:52:27 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 4-3 | 14:52:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Yorick | 0.0100 |  |
| Jogador 4 | 4-3 | 14:52:28 | MOVE Board -> Board: Yorick (i:2.0) <-> Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 4-3 | 14:52:29 | MOVE Board -> Board: Camille (i:2.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 4 | 4-3 | 14:52:29 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Colosso | DA_18_Yorick | -0.5400 |  |
| Jogador 4 | 4-4 | 14:53:01 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 4-4 | 14:53:01 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Colosso | DA_18_Yorick | 0.0100 |  |
| Jogador 4 | 4-4 | 14:53:02 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-4 | 14:53:02 | MOVE Bench -> Board: Akali (i:2.0) <-> Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Colosso | DA_18_Yorick | -0.3600 |  |
| Jogador 4 | 4-4 | 14:53:03 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Colosso | DA_18_Yorick | -0.5500 |  |
| Jogador 4 | 4-5 | 14:53:38 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Colosso | DA_18_Yorick | -0.6100 |  |
| Jogador 4 | 4-5 | 14:53:38 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 161 | 5 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 4 | 4-5 | 14:53:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Colosso | DA_18_Yorick | -0.1100 |  |
| Jogador 4 | 4-5 | 14:53:40 | MOVE Bench -> Board: Akali (i:2.0) <-> Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Colosso | DA_18_Yorick | 0.1100 |  |
| Jogador 4 | 4-5 | 14:53:40 | MOVE Bench -> Board: Camille (i:2.0) <-> Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Colosso | DA_18_Yorick | -0.3700 |  |
| Jogador 4 | 4-5 | 14:53:41 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Colosso | DA_18_Yorick | -0.3700 |  |
| Jogador 4 | 4-5 | 14:53:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Colosso | DA_18_Yorick | -0.5800 |  |
| Jogador 5 | ? | 14:46:14 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.5700 |  |
| Jogador 5 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 14:46:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 14:46:21 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 14:46:25 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1800 |  |
| Jogador 5 | 1-2 | 14:46:28 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.1900 |  |
| Jogador 5 | 1-2 | 14:46:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 1-2 | 14:46:33 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.4100 |  |
| Jogador 5 | 1-3 | 14:46:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yunara | 0.3200 |  |
| Jogador 5 | 1-3 | 14:46:37 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yunara | -0.0600 |  |
| Jogador 5 | 1-3 | 14:46:37 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.2700 |  |
| Jogador 5 | 1-3 | 14:46:39 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 1-3 | 14:46:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.1900 |  |
| Jogador 5 | 1-3 | 14:46:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 1-4 | 14:46:45 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yunara | 0.9700 |  |
| Jogador 5 | 1-4 | 14:46:46 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yunara | 0.4500 |  |
| Jogador 5 | 1-4 | 14:46:48 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2400 |  |
| Jogador 5 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2000 |  |
| Jogador 5 | 1-4 | 14:46:49 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.1700 |  |
| Jogador 5 | 1-4 | 14:46:50 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.1700 |  |
| Jogador 5 | 1-4 | 14:46:51 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0500 |  |
| Jogador 5 | 2-1 | 14:46:54 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_MasterYi_AD | 0.3400 |  |
| Jogador 5 | 2-1 | 14:46:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_MasterYi_AD | 0.3100 |  |
| Jogador 5 | 2-1 | 14:46:55 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_MasterYi_AD | -0.1400 |  |
| Jogador 5 | 2-1 | 14:46:56 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_MasterYi_AD | -0.5700 |  |
| Jogador 5 | 2-1 | 14:46:59 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2700 |  |
| Jogador 5 | 2-1 | 14:47:00 | MOVE Board -> Board: Sejuani (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | -0.3300 |  |
| Jogador 5 | 2-2 | 14:47:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 5 | 2-2 | 14:47:04 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.1700 |  |
| Jogador 5 | 2-2 | 14:47:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | -0.0400 |  |
| Jogador 5 | 2-2 | 14:47:05 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 2-2 | 14:47:06 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.4500 |  |
| Jogador 5 | 2-2 | 14:47:07 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 5 | 2-2 | 14:47:08 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 2-3 | 14:47:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.3700 |  |
| Jogador 5 | 2-3 | 14:47:16 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 5 | 2-3 | 14:47:16 | MOVE Board -> Board: Master Yi (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-3 | 14:47:17 | MOVE Board -> Board: Sejuani (i:4.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 5 | 2-3 | 14:47:18 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 5 | 2-3 | 14:47:18 | MOVE Board -> Board: Veigar (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 5 | 2-3 | 14:47:19 | MOVE Board -> Board: Sejuani (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 5 | 2-3 | 14:47:19 | MOVE Board -> Board: Master Yi (i:6.0) <-> Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 5 | 2-3 | 14:47:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 5 | 2-4 | 14:47:29 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 5 | 2-4 | 14:47:29 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 5 | 2-4 | 14:47:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 5 | 2-4 | 14:47:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 2-4 | 14:47:31 | MOVE Board -> Board: Yunara (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 5 | 2-4 | 14:47:31 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 5 | 2-4 | 14:47:32 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 5 | 2-4 | 14:47:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 5 | 2-4 | 14:47:33 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 5 | 2-5 | 14:47:42 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 5 | 2-5 | 14:47:43 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 5 | 2-5 | 14:47:44 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 5 | 2-5 | 14:47:44 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.3700 |  |
| Jogador 5 | 2-5 | 14:47:45 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 5 | 2-5 | 14:47:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 5 | 2-5 | 14:47:45 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_Tristana | 0.4000 |  |
| Jogador 5 | 2-5 | 14:47:46 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 2-5 | 14:47:46 | MOVE Board -> Board: Tristana (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 2-6 | 14:47:58 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_18_Tristana | 0.9800 |  |
| Jogador 5 | 2-6 | 14:47:58 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Yunara | 1.0500 |  |
| Jogador 5 | 2-6 | 14:47:59 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Yunara | 0.2500 |  |
| Jogador 5 | 2-6 | 14:47:59 | MOVE Board -> Board: Sejuani (i:4.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 2-6 | 14:48:00 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 2-6 | 14:48:00 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Yunara | -0.0200 |  |
| Jogador 5 | 2-6 | 14:48:01 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_18_Tristana | -0.6200 |  |
| Jogador 5 | 2-6 | 14:48:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_18_Tristana | -0.0600 |  |
| Jogador 5 | 2-6 | 14:48:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Tristana | -0.0600 |  |
| Jogador 5 | 2-7 | 14:48:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_18_Tristana | 0.8000 |  |
| Jogador 5 | 2-7 | 14:48:14 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_Tristana | 0.2900 |  |
| Jogador 5 | 2-7 | 14:48:15 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_Tristana | 0.2100 |  |
| Jogador 5 | 2-7 | 14:48:15 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_18_Tristana | 0.2400 |  |
| Jogador 5 | 2-7 | 14:48:16 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Florescer | DA_18_Tristana | -0.1400 |  |
| Jogador 5 | 2-7 | 14:48:16 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | 0.5200 |  |
| Jogador 5 | 2-7 | 14:48:17 | MOVE Board -> Board: Tristana (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 2-7 | 14:48:17 | MOVE Board -> Board: Master Yi (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 2-7 | 14:48:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-1 | 14:48:31 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_18_Tristana | 0.7400 |  |
| Jogador 5 | 3-1 | 14:48:32 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Tristana | -0.2000 |  |
| Jogador 5 | 3-1 | 14:48:32 | MOVE Board -> Board: Veigar (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-1 | 14:48:33 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 3-1 | 14:48:33 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-2 | 14:48:50 | COMPROU: Yunara (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_Yunara | 0.7700 |  |
| Jogador 5 | 3-2 | 14:48:51 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_18_Yunara | 0.1300 |  |
| Jogador 5 | 3-2 | 14:48:51 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Yunara | 0.2100 |  |
| Jogador 5 | 3-2 | 14:48:52 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Yunara | -0.0100 |  |
| Jogador 5 | 3-2 | 14:48:52 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 3-2 | 14:48:53 | MOVE Board -> Board: Veigar (i:2.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Yunara | -0.1600 |  |
| Jogador 5 | 3-2 | 14:48:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 3-3 | 14:49:10 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Yunara | 0.7400 |  |
| Jogador 5 | 3-3 | 14:49:11 | VENDEU: Yunara (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 0 | Florescer | DA_18_Tristana | -0.5000 |  |
| Jogador 5 | 3-3 | 14:49:11 | COMPROU: Karma (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Florescer | DA_18_Tristana | 0.7700 |  |
| Jogador 5 | 3-3 | 14:49:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Tristana | -0.0900 |  |
| Jogador 5 | 3-3 | 14:49:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 4 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-3 | 14:49:13 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Tristana | 0.0800 |  |
| Jogador 5 | 3-3 | 14:49:13 | MOVE Bench -> Board: Rengar (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Tristana | 0.4100 |  |
| Jogador 5 | 3-3 | 14:49:14 | MOVE Board -> Board: Rengar (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Tristana | 0.0400 |  |
| Jogador 5 | 3-3 | 14:49:14 | MOVE Board -> Board: Veigar (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-4 | 14:49:32 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Florescer | DA_18_Tristana | 0.0800 |  |
| Jogador 5 | 3-4 | 14:49:32 | COMPROU: Morgana (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 3-4 | 14:49:33 | MOVE Board -> Board: Tristana (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | 0.0500 |  |
| Jogador 5 | 3-4 | 14:49:33 | MOVE Board -> Board: Sejuani (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-4 | 14:49:34 | MOVE Board -> Board: Master Yi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-4 | 14:49:34 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-4 | 14:49:35 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 3-4 | 14:49:35 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 1 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-5 | 14:49:55 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Tristana | 0.6400 |  |
| Jogador 5 | 3-5 | 14:49:56 | MOVE Board -> Board: Veigar (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-5 | 14:49:56 | MOVE Board -> Board: Tristana (i:6.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-5 | 14:49:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 3-6 | 14:50:19 | VENDEU: Karma (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 0 | Florescer | DA_18_Tristana | -0.5000 |  |
| Jogador 5 | 3-6 | 14:50:20 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 0 | Florescer | DA_18_LeBlanc | 0.6900 |  |
| Jogador 5 | 3-6 | 14:50:20 | COMPROU: Rengar (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Florescer | DA_18_LeBlanc | 0.3500 |  |
| Jogador 5 | 3-6 | 14:50:21 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Florescer | DA_18_LeBlanc | -0.0100 |  |
| Jogador 5 | 3-6 | 14:50:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Florescer | DA_18_LeBlanc | -0.0900 |  |
| Jogador 5 | 3-6 | 14:50:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Florescer | DA_18_LeBlanc | -0.0100 |  |
| Jogador 5 | 3-6 | 14:50:23 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_LeBlanc | -0.0500 |  |
| Jogador 5 | 3-6 | 14:50:23 | MOVE Board -> Board: Rengar (i:6.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_LeBlanc | 0.0000 |  |
| Jogador 5 | 3-6 | 14:50:24 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 0 | 0 | Florescer | DA_18_LeBlanc | -0.0100 |  |
| Jogador 5 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_LeBlanc | 0.1300 |  |
| Jogador 5 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_LeBlanc | 0.1400 |  |
| Jogador 5 | 3-7 | 14:50:51 | MOVE Board -> Board: Veigar (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_LeBlanc | 0.0000 |  |
| Jogador 5 | 3-7 | 14:50:51 | MOVE Board -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_LeBlanc | -0.0200 |  |
| Jogador 5 | 3-7 | 14:50:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 8 | 0 | Florescer | DA_18_LeBlanc | 0.0000 |  |
| Jogador 5 | 4-1 | 14:51:19 | VENDEU: LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 0 | Florescer | DA_18_Tristana | -0.5000 |  |
| Jogador 5 | 4-1 | 14:51:19 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Florescer | DA_18_Tristana | 0.6700 |  |
| Jogador 5 | 4-1 | 14:51:20 | MOVE Board -> Board: Tristana (i:6.0) <-> Rengar (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 4-1 | 14:51:21 | MOVE Board -> Board: Rengar (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 4-1 | 14:51:21 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 4-1 | 14:51:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 0 | Florescer | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 4-2 | 14:51:52 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Florescer | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 4-2 | 14:51:52 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Florescer | DA_18_Tristana | 0.7600 |  |
| Jogador 5 | 4-2 | 14:51:53 | VENDEU: Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 33 | 2 | Florescer | DA_18_Tristana | -0.0300 |  |
| Jogador 5 | 4-2 | 14:51:53 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Florescer | DA_18_MasterYi_AD | 0.8200 |  |
| Jogador 5 | 4-2 | 14:51:54 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Florescer | DA_18_MasterYi_AD | 0.6300 |  |
| Jogador 5 | 4-2 | 14:51:54 | MOVE Bench -> Board: Master Yi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Florescer | DA_18_MasterYi_AD | 0.6000 |  |
| Jogador 5 | 4-2 | 14:51:55 | MOVE Board -> Board: Master Yi (i:12.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 4-2 | 14:51:55 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 4-2 | 14:51:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 2 | Florescer | DA_18_MasterYi_AD | -0.1100 |  |
| Jogador 5 | 4-3 | 14:52:26 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Florescer | DA_18_MasterYi_AD | 0.2600 |  |
| Jogador 5 | 4-3 | 14:52:26 | MOVE Board -> Board: Veigar (i:2.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 4-3 | 14:52:27 | MOVE Board -> Board: Master Yi (i:12.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 4-3 | 14:52:27 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 2 | Florescer | DA_18_MasterYi_AD | -0.1800 |  |
| Jogador 5 | 4-4 | 14:53:01 | VENDEU: Morgana (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Florescer | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 5 | 4-4 | 14:53:01 | COMPROU: Leona (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Florescer | DA_18_MasterYi_AD | 0.7000 |  |
| Jogador 5 | 4-4 | 14:53:02 | MOVE Board -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 4-4 | 14:53:02 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 4-4 | 14:53:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Florescer | DA_18_MasterYi_AD | -0.0800 |  |
| Jogador 5 | 4-5 | 14:53:38 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 4-5 | 14:53:38 | MOVE Board -> Board: Veigar (i:2.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Florescer | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 5 | 4-5 | 14:53:39 | MOVE Board -> Board: Master Yi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Florescer | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 5 | 4-5 | 14:53:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 5 | Florescer | DA_18_MasterYi_AD | -0.0900 |  |
| Jogador 5 | 4-6 | 14:54:15 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Florescer | DA_18_MasterYi_AD | -0.0600 |  |
| Jogador 5 | 4-6 | 14:54:15 | COMPROU: Sejuani (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Florescer | DA_18_MasterYi_AD | 0.8900 |  |
| Jogador 5 | 4-6 | 14:54:16 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Florescer | DA_18_MasterYi_AD | 0.6000 |  |
| Jogador 5 | 4-6 | 14:54:16 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Florescer | DA_18_MasterYi_AD | 0.0400 |  |
| Jogador 5 | 4-6 | 14:54:17 | MOVE Board -> Board: Master Yi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 4-6 | 14:54:17 | MOVE Board -> Board: Tristana (i:6.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 4-6 | 14:54:18 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Florescer | DA_18_MasterYi_AD | -0.2400 |  |
| Jogador 5 | 4-7 | 14:54:55 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Florescer | DA_18_MasterYi_AD | 0.6900 |  |
| Jogador 5 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Florescer | DA_18_MasterYi_AD | 0.1800 |  |
| Jogador 5 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 90 | 5 | Florescer | DA_18_MasterYi_AD | 0.1900 |  |
| Jogador 5 | 4-7 | 14:54:57 | VENDEU: Sejuani (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Florescer | DA_18_MasterYi_AD | -0.6000 |  |
| Jogador 5 | 4-7 | 14:54:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Florescer | DA_18_Tristana | 0.9500 |  |
| Jogador 5 | 4-7 | 14:54:58 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 92 | 5 | Florescer | DA_18_Tristana | 0.1500 |  |
| Jogador 5 | 4-7 | 14:54:59 | COMPROU: Nidalee (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Florescer | DA_18_Tristana | 0.0100 |  |
| Jogador 5 | 4-7 | 14:54:59 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Florescer | DA_18_Tristana | 0.0000 |  |
| Jogador 5 | 4-7 | 14:55:00 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 88 | 5 | Florescer | DA_18_Tristana | -0.0100 |  |
| Jogador 5 | 5-1 | 14:55:34 | VENDEU: Tristana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 106 | 5 | Florescer | DA_18_MasterYi_AD | -0.5100 |  |
| Jogador 5 | 5-1 | 14:55:35 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Florescer | DA_18_MasterYi_AD | -0.1400 |  |
| Jogador 5 | 5-1 | 14:55:36 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Master Yi (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Florescer | DA_18_MasterYi_AD | 0.0900 |  |
| Jogador 5 | 5-1 | 14:55:36 | EQUIP_FROM_INVENTORY: TFT_Item_Leviathan -> Master Yi (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Florescer | DA_18_MasterYi_AD | 0.1300 |  |
| Jogador 5 | 5-1 | 14:55:37 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Rek'Sai (i:2.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 103 | 5 | Florescer | DA_18_MasterYi_AD | 0.1000 |  |
| Jogador 5 | 5-1 | 14:55:37 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Florescer | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 5 | 5-1 | 14:55:38 | MOVE Board -> Board: Master Yi (i:6.0) <-> Master Yi (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 5-1 | 14:55:38 | MOVE Board -> Board: Master Yi (i:12.0) <-> Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 99 | 5 | Florescer | DA_18_MasterYi_AD | -0.0300 |  |
| Jogador 5 | 5-1 | 14:55:39 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Florescer | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 5 | 5-2 | 14:56:17 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 5-2 | 14:56:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 106 | 5 | Florescer | DA_18_MasterYi_AD | 0.3200 |  |
| Jogador 5 | 5-2 | 14:56:18 | VENDEU: Leona (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Florescer | DA_18_MasterYi_AD | -0.3900 |  |
| Jogador 5 | 5-2 | 14:56:19 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 104 | 5 | Florescer | DA_18_MasterYi_AD | 0.2800 |  |
| Jogador 5 | 5-2 | 14:56:19 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 100 | 5 | Florescer | DA_18_MasterYi_AD | 0.0600 |  |
| Jogador 5 | 5-2 | 14:56:19 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Florescer | DA_18_MasterYi_AD | 0.4700 |  |
| Jogador 5 | 5-2 | 14:56:20 | MOVE Bench -> Board: Nidalee (i:8.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 96 | 5 | Florescer | DA_18_MasterYi_AD | 0.2400 |  |
| Jogador 5 | 5-2 | 14:56:20 | COMPROU: Diana (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 93 | 5 | Florescer | DA_18_MasterYi_AD | -0.1700 |  |
| Jogador 5 | 5-2 | 14:56:21 | MOVE Board -> Board: Nidalee (i:8.0) <-> Rek'Sai (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 93 | 5 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 5-3 | 14:57:01 | VENDEU: Leona (i:2.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 106 | 5 | Florescer | DA_18_MasterYi_AD | 0.0200 |  |
| Jogador 5 | 5-3 | 14:57:01 | COMPROU: Vi (Custo 3 \| i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 103 | 5 | Florescer | DA_18_MasterYi_AD | 0.8700 |  |
| Jogador 5 | 5-3 | 14:57:02 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Master Yi (i:6.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 103 | 5 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 5-3 | 14:57:02 | MOVE Board -> Board: Master Yi (i:6.0) <-> Master Yi (i:12.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 103 | 5 | Florescer | DA_18_MasterYi_AD | -0.0200 |  |
| Jogador 5 | 5-3 | 14:57:03 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 103 | 5 | Florescer | DA_18_MasterYi_AD | -0.1300 |  |
| Jogador 5 | 5-3 | 14:57:06 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 103 | 5 | Florescer | DA_18_MasterYi_AD | 0.4700 |  |
| Jogador 5 | 5-4 | 14:57:54 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 110 | 5 | Florescer | DA_18_MasterYi_AD | 0.8900 |  |
| Jogador 5 | 5-4 | 14:57:55 | MOVE Board -> Board: Master Yi (i:12.0) <-> Vazio | ECON | ECON: manter reserva de 50 e gastar excedente útil | 110 | 5 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 5-4 | 14:57:56 | MOVE Board -> Board: Veigar (i:2.0) <-> Nidalee (i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 110 | 5 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 5-4 | 14:57:56 | PASSOU TURNO | ECON | ECON: manter reserva de 50 e gastar excedente útil | 110 | 5 | Florescer | DA_18_MasterYi_AD | -0.1400 |  |
| Jogador 5 | 5-5 | 14:58:38 | VENDEU: Diana (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 125 | 5 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 5-5 | 14:58:38 | COMPROU: Vi (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 122 | 5 | Florescer | DA_18_MasterYi_AD | 1.0000 |  |
| Jogador 5 | 5-5 | 14:58:39 | COMPROU: Rakan (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 121 | 5 | Florescer | DA_18_MasterYi_AD | 0.1500 |  |
| Jogador 5 | 5-5 | 14:58:40 | MOVE Board -> Board: Nidalee (i:8.0) <-> Master Yi (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 121 | 5 | Florescer | DA_18_MasterYi_AD | 0.0000 |  |
| Jogador 5 | 5-5 | 14:58:40 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rek'Sai (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 121 | 5 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 5-5 | 14:58:41 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Master Yi (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 121 | 5 | Florescer | DA_18_MasterYi_AD | -0.0100 |  |
| Jogador 5 | 5-5 | 14:58:41 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 121 | 5 | Florescer | DA_18_MasterYi_AD | -0.3000 |  |
| Jogador 5 | 5-6 | 14:59:22 | COMPROU: Nidalee (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 129 | 5 | Florescer | DA_Nidalee18_AP | 1.0000 |  |
| Jogador 5 | 5-6 | 14:59:22 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 126 | 5 | Florescer | DA_Nidalee18_AP | 0.9800 |  |
| Jogador 5 | 5-6 | 14:59:24 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Florescer | DA_Nidalee18_AP | 0.2400 |  |
| Jogador 5 | 5-6 | 14:59:24 | MOVE Bench -> Board: Vi (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 123 | 5 | Florescer | DA_Nidalee18_AP | 0.3200 |  |
| Jogador 5 | 5-6 | 14:59:25 | MOVE Board -> Board: Vi (i:12.0) <-> Veigar (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 123 | 5 | Florescer | DA_Nidalee18_AP | -0.0200 |  |
| Jogador 5 | 5-6 | 14:59:25 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 123 | 5 | Florescer | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 5 | 5-6 | 14:59:26 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 123 | 5 | Florescer | DA_Nidalee18_AP | -0.3000 |  |
| Jogador 5 | 5-6 | 14:59:27 | MOVE Bench -> Board: Rengar (i:12.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 123 | 5 | Florescer | DA_Nidalee18_AP | 0.4300 |  |
| Jogador 5 | 5-7 | 15:00:12 | COMPROU: Ashe (Custo 5 \| i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 129 | 5 | Florescer | DA_Nidalee18_AP | 0.3700 |  |
| Jogador 5 | 5-7 | 15:00:12 | EQUIP_FROM_INVENTORY: TFT_Item_MadredsBloodrazor -> Master Yi (i:12.0) (tabuleiro slot 8) | WINSTREAK | WINSTREAK: preservar vantagem atual | 129 | 5 | Florescer | DA_Nidalee18_AP | 0.1300 |  |
| Jogador 5 | 5-7 | 15:00:13 | COMPROU: Karma (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 128 | 5 | Florescer | DA_Nidalee18_AP | 0.3800 |  |
| Jogador 5 | 5-7 | 15:00:13 | MOVE Board -> Board: Rengar (i:12.0) <-> Veigar (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 128 | 5 | Florescer | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 5 | 5-7 | 15:00:14 | MOVE Board -> Board: Veigar (i:2.0) <-> Vi (i:12.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 128 | 5 | Florescer | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 5 | 5-7 | 15:00:14 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 128 | 5 | Florescer | DA_Nidalee18_AP | -0.1600 |  |
| Jogador 6 | ? | 14:46:14 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 14:46:20 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 6 | 1-1 | 14:46:21 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.9900 |  |
| Jogador 6 | 1-1 | 14:46:21 | MOVE Bench -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.3200 |  |
| Jogador 6 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-1 | 14:46:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 1-2 | 14:46:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-2 | 14:46:33 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.5400 |  |
| Jogador 6 | 1-3 | 14:46:36 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 1.0200 |  |
| Jogador 6 | 1-3 | 14:46:37 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 1-3 | 14:46:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.1500 |  |
| Jogador 6 | 1-3 | 14:46:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-4 | 14:46:45 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 1.0200 |  |
| Jogador 6 | 1-4 | 14:46:46 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 1-4 | 14:46:48 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.9700 |  |
| Jogador 6 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 6 | 1-4 | 14:46:49 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 6 | 1-4 | 14:46:50 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.4000 |  |
| Jogador 6 | 1-4 | 14:46:51 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 2-1 | 14:46:54 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1400 |  |
| Jogador 6 | 2-1 | 14:46:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0400 |  |
| Jogador 6 | 2-1 | 14:46:55 | MOVE Board -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-1 | 14:46:56 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.2100 |  |
| Jogador 6 | 2-1 | 14:46:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 14:47:04 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 2-2 | 14:47:04 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 14:47:05 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Tristana | -0.5400 |  |
| Jogador 6 | 2-2 | 14:47:05 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Tristana | -0.4900 |  |
| Jogador 6 | 2-2 | 14:47:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | -0.0500 |  |
| Jogador 6 | 2-2 | 14:47:07 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.6300 |  |
| Jogador 6 | 2-2 | 14:47:08 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.2800 |  |
| Jogador 6 | 2-3 | 14:47:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Rakan | 1.1100 |  |
| Jogador 6 | 2-3 | 14:47:16 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Rakan | 0.9100 |  |
| Jogador 6 | 2-3 | 14:47:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.4000 |  |
| Jogador 6 | 2-3 | 14:47:17 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | -0.1000 |  |
| Jogador 6 | 2-3 | 14:47:18 | MOVE Board -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.3000 |  |
| Jogador 6 | 2-3 | 14:47:18 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 2-3 | 14:47:19 | MOVE Board -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 2-3 | 14:47:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 2-4 | 14:47:29 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Rakan | 1.0500 |  |
| Jogador 6 | 2-4 | 14:47:29 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Rakan | 0.5700 |  |
| Jogador 6 | 2-4 | 14:47:30 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | 0.2800 |  |
| Jogador 6 | 2-4 | 14:47:31 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | -0.1400 |  |
| Jogador 6 | 2-4 | 14:47:31 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 2-4 | 14:47:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 2-5 | 14:47:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Rakan | 0.3100 |  |
| Jogador 6 | 2-5 | 14:47:43 | MOVE Board -> Board: Rakan (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 6 | 2-5 | 14:47:44 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_18_Rakan | 0.3200 |  |
| Jogador 6 | 2-5 | 14:47:44 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_18_Rakan | -0.4000 |  |
| Jogador 6 | 2-5 | 14:47:45 | MOVE Bench -> Board: Tristana (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_18_Rakan | 0.3300 |  |
| Jogador 6 | 2-5 | 14:47:45 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Feérico | DA_18_Rakan | 0.0300 |  |
| Jogador 6 | 2-5 | 14:47:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 1 | Feérico | DA_18_Rakan | -0.1200 |  |
| Jogador 6 | 2-5 | 14:47:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 1 | Feérico | DA_18_Rakan | -0.0400 |  |
| Jogador 6 | 2-5 | 14:47:46 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 1 | Feérico | DA_18_Rakan | -0.3000 |  |
| Jogador 6 | 2-6 | 14:47:58 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Rakan | 0.9000 |  |
| Jogador 6 | 2-6 | 14:47:58 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Rakan | 0.9400 |  |
| Jogador 6 | 2-6 | 14:47:59 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Rakan | 0.6300 |  |
| Jogador 6 | 2-6 | 14:47:59 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Rakan | 0.0600 |  |
| Jogador 6 | 2-6 | 14:48:00 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Rakan | -0.5000 |  |
| Jogador 6 | 2-6 | 14:48:00 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Rakan | -0.5500 |  |
| Jogador 6 | 2-6 | 14:48:01 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Shen (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Rakan | 0.0300 |  |
| Jogador 6 | 2-6 | 14:48:01 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Shen (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Rakan | 0.0900 |  |
| Jogador 6 | 2-6 | 14:48:02 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Rakan | 0.2500 |  |
| Jogador 6 | 2-7 | 14:48:14 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Rakan | 0.2800 |  |
| Jogador 6 | 2-7 | 14:48:14 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Rakan | 0.4000 |  |
| Jogador 6 | 2-7 | 14:48:15 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Rakan | 0.1800 |  |
| Jogador 6 | 2-7 | 14:48:15 | MOVE Board -> Board: Vi (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 2-7 | 14:48:16 | MOVE Board -> Board: Shen (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 2-7 | 14:48:16 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-1 | 14:48:31 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Feérico | DA_18_Rakan | 0.7400 |  |
| Jogador 6 | 3-1 | 14:48:32 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Feérico | DA_18_Rakan | -0.0600 |  |
| Jogador 6 | 3-1 | 14:48:32 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 3-1 | 14:48:33 | MOVE Board -> Board: Rakan (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 6 | 3-1 | 14:48:33 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Feérico | DA_18_Rakan | 0.7200 |  |
| Jogador 6 | 3-1 | 14:48:34 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-1 | 14:48:34 | MOVE Board -> Board: Vi (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 3-1 | 14:48:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 16 | 1 | Feérico | DA_18_Rakan | -0.0600 |  |
| Jogador 6 | 3-2 | 14:48:50 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Rakan | 0.7300 |  |
| Jogador 6 | 3-2 | 14:48:51 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Feérico | DA_18_Rakan | 0.6400 |  |
| Jogador 6 | 3-2 | 14:48:51 | MOVE Board -> Board: Shen (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 3-2 | 14:48:52 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Feérico | DA_18_Rakan | -0.1300 |  |
| Jogador 6 | 3-2 | 14:48:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-3 | 14:49:10 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 28 | 1 | Feérico | DA_18_Rakan | -0.5200 |  |
| Jogador 6 | 3-3 | 14:49:11 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Feérico | DA_18_Rakan | 0.7100 |  |
| Jogador 6 | 3-3 | 14:49:11 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Feérico | DA_18_Rakan | -0.9800 |  |
| Jogador 6 | 3-3 | 14:49:12 | COMPROU: Lillia (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Rakan | 0.2100 |  |
| Jogador 6 | 3-3 | 14:49:12 | MOVE Bench -> Board: Vi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Rakan | -0.2700 |  |
| Jogador 6 | 3-3 | 14:49:13 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Rakan | 0.0700 |  |
| Jogador 6 | 3-3 | 14:49:13 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Rakan | -0.4100 |  |
| Jogador 6 | 3-3 | 14:49:14 | MOVE Bench -> Board: Vi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Rakan | -0.4100 |  |
| Jogador 6 | 3-3 | 14:49:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 3-4 | 14:49:32 | VENDEU: Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Feérico | DA_18_Rakan | -0.5100 |  |
| Jogador 6 | 3-4 | 14:49:32 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Feérico | DA_18_Rammus | 0.7100 |  |
| Jogador 6 | 3-4 | 14:49:33 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Feérico | DA_18_Rammus | 0.0800 |  |
| Jogador 6 | 3-4 | 14:49:33 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Feérico | DA_18_Rammus | -0.4100 |  |
| Jogador 6 | 3-4 | 14:49:34 | MOVE Bench -> Board: Vi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Feérico | DA_18_Rammus | -0.2300 |  |
| Jogador 6 | 3-4 | 14:49:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 27 | 2 | Feérico | DA_18_Rammus | -0.0800 |  |
| Jogador 6 | 3-5 | 14:49:55 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Feérico | DA_18_Rammus | 0.0300 |  |
| Jogador 6 | 3-5 | 14:49:56 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Feérico | DA_18_Rammus | 0.0800 |  |
| Jogador 6 | 3-5 | 14:49:56 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Feérico | DA_18_Rammus | -0.4100 |  |
| Jogador 6 | 3-5 | 14:49:56 | MOVE Bench -> Board: Vi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Feérico | DA_18_Rammus | -0.4100 |  |
| Jogador 6 | 3-5 | 14:49:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Feérico | DA_18_Rammus | -0.1200 |  |
| Jogador 6 | 3-6 | 14:50:19 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Feérico | DA_18_Rammus | 0.6800 |  |
| Jogador 6 | 3-6 | 14:50:20 | VENDEU: Rammus (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Feérico | DA_18_Rakan | -0.4900 |  |
| Jogador 6 | 3-6 | 14:50:20 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Feérico | DA_18_Teemo | 0.8100 |  |
| Jogador 6 | 3-6 | 14:50:21 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Feérico | DA_18_Teemo | -0.0900 |  |
| Jogador 6 | 3-6 | 14:50:22 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Feérico | DA_18_Teemo | -0.4100 |  |
| Jogador 6 | 3-6 | 14:50:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Feérico | DA_18_Teemo | -0.1300 |  |
| Jogador 6 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Feérico | DA_18_Teemo | 0.1800 |  |
| Jogador 6 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Feérico | DA_18_Teemo | 0.2000 |  |
| Jogador 6 | 3-7 | 14:50:51 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Feérico | DA_18_Teemo | 0.2600 |  |
| Jogador 6 | 3-7 | 14:50:51 | MOVE Bench -> Board: Vi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Feérico | DA_18_Teemo | -0.2200 |  |
| Jogador 6 | 3-7 | 14:50:52 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Feérico | DA_18_Teemo | 0.0800 |  |
| Jogador 6 | 3-7 | 14:50:52 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Feérico | DA_18_Teemo | -0.4100 |  |
| Jogador 6 | 3-7 | 14:50:53 | MOVE Bench -> Board: Vi (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Feérico | DA_18_Teemo | -0.4100 |  |
| Jogador 6 | 3-7 | 14:50:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Feérico | DA_18_Teemo | -0.2200 |  |
| Jogador 6 | 4-1 | 14:51:19 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Feérico | DA_18_Tristana | 0.8900 |  |
| Jogador 6 | 4-1 | 14:51:19 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Feérico | DA_18_Tristana | 0.0900 |  |
| Jogador 6 | 4-1 | 14:51:20 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Feérico | DA_18_Tristana | -0.0800 |  |
| Jogador 6 | 4-1 | 14:51:21 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Feérico | DA_18_Tristana | -0.7000 |  |
| Jogador 6 | 4-1 | 14:51:21 | MOVE Bench -> Board: Lillia (i:8.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Feérico | DA_18_Tristana | 0.0700 |  |
| Jogador 6 | 4-1 | 14:51:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 5 | Feérico | DA_18_Tristana | 0.5700 |  |
| Jogador 6 | 4-1 | 14:51:22 | MOVE Board -> Board: Rakan (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 5 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 4-1 | 14:51:23 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Lillia (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 5 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 6 | 4-1 | 14:51:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 5 | Feérico | DA_18_Tristana | -0.0800 |  |
| Jogador 6 | 4-2 | 14:51:52 | VENDEU: Teemo (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Feérico | DA_18_Tristana | -0.6000 |  |
| Jogador 6 | 4-2 | 14:51:52 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Feérico | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 4-2 | 14:51:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 6 | 4-2 | 14:51:53 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 6 | 4-2 | 14:51:54 | MOVE Board -> Board: Lillia (i:8.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 4-2 | 14:51:54 | MOVE Board -> Board: Shen (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 4-2 | 14:51:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Feérico | DA_18_Tristana | -0.0900 |  |
| Jogador 6 | 4-3 | 14:52:26 | VENDEU: Tristana (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Feérico | DA_18_Rakan | -0.6000 |  |
| Jogador 6 | 4-3 | 14:52:26 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Feérico | DA_18_Rakan | 0.7100 |  |
| Jogador 6 | 4-3 | 14:52:27 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Feérico | DA_18_Rakan | -0.0300 |  |
| Jogador 6 | 4-3 | 14:52:27 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Feérico | DA_18_Rakan | 0.3400 |  |
| Jogador 6 | 4-3 | 14:52:28 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-3 | 14:52:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Feérico | DA_18_Rakan | 0.0600 |  |
| Jogador 6 | 4-3 | 14:52:29 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Feérico | DA_18_Rakan | 0.5500 |  |
| Jogador 6 | 4-3 | 14:52:30 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Feérico | DA_18_Rakan | 0.4000 |  |
| Jogador 6 | 4-3 | 14:52:30 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 69 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 14:53:01 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Feérico | DA_18_Rakan | 0.2600 |  |
| Jogador 6 | 4-4 | 14:53:01 | MOVE Board -> Board: Rakan (i:4.0) <-> Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Feérico | DA_18_Rakan | 0.0000 |  |
| Jogador 6 | 4-4 | 14:53:02 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 4-4 | 14:53:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 77 | 5 | Feérico | DA_18_Rakan | -0.1000 |  |
| Jogador 6 | 4-5 | 14:53:38 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Feérico | DA_18_Rakan | -0.4700 |  |
| Jogador 6 | 4-5 | 14:53:38 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Feérico | DA_18_Rakan | 0.9100 |  |
| Jogador 6 | 4-5 | 14:53:39 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 80 | 5 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-5 | 14:53:40 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-5 | 14:53:40 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-5 | 14:53:41 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-5 | 14:53:41 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-5 | 14:53:42 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-5 | 14:53:42 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 56 | 5 | Feérico | DA_18_Rakan | 0.0400 |  |
| Jogador 6 | 4-6 | 14:54:15 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 6 | 4-6 | 14:54:15 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 6 | 4-6 | 14:54:16 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Feérico | DA_KogMaw18_AD | 0.9500 |  |
| Jogador 6 | 4-6 | 14:54:16 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Feérico | DA_KogMaw18_AD | 0.5200 |  |
| Jogador 6 | 4-6 | 14:54:17 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Feérico | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 6 | 4-6 | 14:54:17 | MOVE Board -> Board: Vi (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-6 | 14:54:18 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-6 | 14:54:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 59 | 5 | Feérico | DA_KogMaw18_AD | -0.1000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-7 | 14:54:55 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 6 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Master Yi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 4-7 | 14:54:57 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 4-7 | 14:54:58 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 4-7 | 14:54:58 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_KogMaw18_AD | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 5-1 | 14:55:34 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Feérico | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 6 | 5-1 | 14:55:35 | MOVE Bench -> Board: Diana (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-1 | 14:55:36 | MOVE Bench -> Board: Shen (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Feérico | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 6 | 5-1 | 14:55:36 | MOVE Bench -> Board: Vi (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Feérico | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 6 | 5-1 | 14:55:37 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 5-1 | 14:55:37 | REROLL | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Feérico | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 6 | 5-1 | 14:55:38 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 78 | 5 | Feérico | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 6 | 5-1 | 14:55:38 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Feérico | DA_KogMaw18_AD | 0.8800 |  |
| Jogador 6 | 5-1 | 14:55:39 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Feérico | DA_KogMaw18_AD | 0.3900 |  |
| Jogador 6 | 5-2 | 14:56:17 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Feérico | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 6 | 5-2 | 14:56:18 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Feérico | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 6 | 5-2 | 14:56:18 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 5-2 | 14:56:19 | MOVE Bench -> Board: Zyra (i:8.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Feérico | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 6 | 5-2 | 14:56:19 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Feérico | DA_KogMaw18_AD | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 5-3 | 14:57:01 | VENDEU: Master Yi (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 99 | 5 | Feérico | DA_KogMaw18_AD | -0.4900 |  |
| Jogador 6 | 5-3 | 14:57:01 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 6 | 5-3 | 14:57:02 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Vi (i:6.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 6 | 5-3 | 14:57:02 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Vi (i:6.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Feérico | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 6 | 5-3 | 14:57:03 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Feérico | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 6 | 5-3 | 14:57:04 | VENDEU: Kog'Maw (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Feérico | DA_18_Rakan | -0.6900 |  |
| Jogador 6 | 5-3 | 14:57:05 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Feérico | DA_18_Rakan | 0.9400 |  |
| Jogador 6 | 5-3 | 14:57:06 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Lillia (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Feérico | DA_18_Rakan | 0.1300 |  |
| Jogador 6 | 5-3 | 14:57:06 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Lillia (i:8.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Feérico | DA_18_Rakan | 0.1200 |  |
| Jogador 6 | 5-4 | 14:57:54 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 5-4 | 14:57:55 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_18_Rakan | 1.0100 |  |
| Jogador 6 | 5-4 | 14:57:56 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Feérico | DA_18_Rakan | -0.0100 |  |
| Jogador 6 | 5-4 | 14:57:56 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Rakan | 0.9500 |  |
| Jogador 6 | 5-4 | 14:57:57 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 6 | 5-4 | 14:57:57 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Rakan | -0.4800 |  |
| Jogador 6 | 5-4 | 14:57:58 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Rakan | 0.8100 |  |
| Jogador 6 | 5-4 | 14:57:58 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 6 | 5-4 | 14:57:58 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Rakan | -0.6200 |  |
| Jogador 6 | 5-5 | 14:58:38 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Feérico | DA_Vi18 | 1.0900 |  |
| Jogador 6 | 5-5 | 14:58:38 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Feérico | DA_Vi18 | 0.4700 |  |
| Jogador 6 | 5-5 | 14:58:39 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Feérico | DA_Vi18 | 0.5900 |  |
| Jogador 6 | 5-5 | 14:58:40 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_Vi18 | 0.5700 |  |
| Jogador 6 | 5-5 | 14:58:40 | MOVE Board -> Board: Vi (i:6.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_Vi18 | 0.0000 |  |
| Jogador 6 | 5-5 | 14:58:41 | MOVE Board -> Board: Diana (i:6.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_Vi18 | -0.0100 |  |
| Jogador 6 | 5-5 | 14:58:41 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_Vi18 | -0.5800 |  |
| Jogador 7 | ? | 14:46:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 14:46:20 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 14:46:25 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 7 | 1-2 | 14:46:28 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 14:46:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 14:46:33 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.5200 |  |
| Jogador 7 | 1-3 | 14:46:36 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 7 | 1-3 | 14:46:37 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-3 | 14:46:37 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1500 |  |
| Jogador 7 | 1-3 | 14:46:39 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-3 | 14:46:40 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 7 | 1-3 | 14:46:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 14:46:45 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-4 | 14:46:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1100 |  |
| Jogador 7 | 1-4 | 14:46:48 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 7 | 1-4 | 14:46:48 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0700 |  |
| Jogador 7 | 1-4 | 14:46:49 | MOVE Board -> Board: Camille (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 14:46:50 | MOVE Board -> Board: Akali (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-4 | 14:46:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 14:46:54 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 14:46:55 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 14:46:55 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 7 | 2-1 | 14:46:56 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.4800 |  |
| Jogador 7 | 2-1 | 14:46:59 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 7 | 2-1 | 14:47:00 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 7 | 2-2 | 14:47:04 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-2 | 14:47:04 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Akali_AD | 0.8700 |  |
| Jogador 7 | 2-2 | 14:47:05 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 2-2 | 14:47:05 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 2-2 | 14:47:06 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-2 | 14:47:07 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | -0.6300 |  |
| Jogador 7 | 2-2 | 14:47:08 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> LeBlanc (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.0700 |  |
| Jogador 7 | 2-3 | 14:47:16 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 7 | 2-3 | 14:47:16 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | 0.2800 |  |
| Jogador 7 | 2-3 | 14:47:16 | MOVE Bench -> Board: Azuporã (i:8.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | 0.3700 |  |
| Jogador 7 | 2-3 | 14:47:17 | MOVE Board -> Board: Camille (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-3 | 14:47:18 | MOVE Board -> Board: Camille (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-3 | 14:47:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 14:47:29 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_Sentinel18 | 0.2700 |  |
| Jogador 7 | 2-4 | 14:47:29 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 14:47:30 | MOVE Board -> Board: Camille (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-4 | 14:47:31 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-4 | 14:47:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 14:47:42 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_Sentinel18 | 0.8200 |  |
| Jogador 7 | 2-5 | 14:47:43 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | 0.8100 |  |
| Jogador 7 | 2-5 | 14:47:44 | MOVE Board -> Board: Azuporã (i:8.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | -0.1900 |  |
| Jogador 7 | 2-5 | 14:47:44 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | 0.1000 |  |
| Jogador 7 | 2-5 | 14:47:45 | MOVE Board -> Board: Camille (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 14:47:45 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | -0.2100 |  |
| Jogador 7 | 2-5 | 14:47:45 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 14:47:46 | MOVE Board -> Board: Hecarim (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 14:47:46 | MOVE Board -> Board: Camille (i:2.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-6 | 14:47:58 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 2-6 | 14:47:58 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_Sentinel18 | -0.5800 |  |
| Jogador 7 | 2-6 | 14:47:59 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | 0.1600 |  |
| Jogador 7 | 2-6 | 14:47:59 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-6 | 14:48:00 | MOVE Board -> Board: Azuporã (i:8.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | 0.2400 |  |
| Jogador 7 | 2-6 | 14:48:00 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-6 | 14:48:01 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-6 | 14:48:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-7 | 14:48:14 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_Sentinel18 | 0.1800 |  |
| Jogador 7 | 2-7 | 14:48:14 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 2-7 | 14:48:15 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_Sentinel18 | 0.8400 |  |
| Jogador 7 | 2-7 | 14:48:15 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 2-7 | 14:48:16 | MOVE Bench -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_Sentinel18 | 0.3800 |  |
| Jogador 7 | 2-7 | 14:48:16 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | 0.1700 |  |
| Jogador 7 | 2-7 | 14:48:17 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | 0.0200 |  |
| Jogador 7 | 2-7 | 14:48:17 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 2-7 | 14:48:17 | MOVE Board -> Board: Shen (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-1 | 14:48:31 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_Sentinel18 | 0.8000 |  |
| Jogador 7 | 3-1 | 14:48:32 | MOVE Board -> Board: Hecarim (i:6.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-1 | 14:48:32 | MOVE Board -> Board: Azuporã (i:8.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_Sentinel18 | -0.1500 |  |
| Jogador 7 | 3-1 | 14:48:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_Sentinel18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-2 | 14:48:50 | VENDEU: Camille (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_Sentinel18 | -0.5800 |  |
| Jogador 7 | 3-2 | 14:48:51 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Devastador | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 3-2 | 14:48:51 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Kog'Maw (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Devastador | DA_Sentinel18 | 0.1400 |  |
| Jogador 7 | 3-2 | 14:48:52 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Kog'Maw (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 1 | Devastador | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 3-2 | 14:48:52 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 13 | 1 | Devastador | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 3-2 | 14:48:53 | VENDEU: Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Devastador | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 3-2 | 14:48:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 1 | Devastador | DA_Sentinel18 | 0.1900 |  |
| Jogador 7 | 3-2 | 14:48:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 1 | Devastador | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 3-2 | 14:48:54 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 1 | Devastador | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 3-3 | 14:49:10 | VENDEU: Cassiopeia (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 12 | 0 | Devastador | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 3-3 | 14:49:11 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_KogMaw18_AD | 0.6800 |  |
| Jogador 7 | 3-3 | 14:49:11 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 9 | 0 | Devastador | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 7 | 3-3 | 14:49:12 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 6 | 0 | Devastador | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 7 | 3-3 | 14:49:12 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-3 | 14:49:13 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 7 | 3-3 | 14:49:13 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 3-3 | 14:49:14 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 7 | 3-3 | 14:49:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 2 | 0 | Devastador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 14:49:32 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 5 | 0 | Devastador | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 7 | 3-4 | 14:49:32 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_KogMaw18_AD | 0.4700 |  |
| Jogador 7 | 3-4 | 14:49:33 | MOVE Board -> Board: Hecarim (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-4 | 14:49:33 | MOVE Board -> Board: Shen (i:4.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 7 | 3-4 | 14:49:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 3 | 0 | Devastador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-5 | 14:49:55 | VENDEU: Kog'Maw (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 17 | 0 | Devastador | DA_Sentinel18 | -0.4900 |  |
| Jogador 7 | 3-5 | 14:49:56 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_Sentinel18 | 0.7300 |  |
| Jogador 7 | 3-5 | 14:49:56 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Fiddlesticks (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 3-5 | 14:49:56 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Fiddlesticks (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 3-5 | 14:49:57 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 3-5 | 14:49:57 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 3-5 | 14:49:58 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 3-5 | 14:49:58 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 0 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-6 | 14:50:19 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 25 | 1 | Devastador | DA_Sentinel18 | -0.4500 |  |
| Jogador 7 | 3-6 | 14:50:20 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Devastador | DA_Fiddlesticks18 | 0.7800 |  |
| Jogador 7 | 3-6 | 14:50:20 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Devastador | DA_Fiddlesticks18 | 0.7400 |  |
| Jogador 7 | 3-6 | 14:50:21 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Devastador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-6 | 14:50:22 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 20 | 1 | Devastador | DA_Fiddlesticks18 | 0.5300 |  |
| Jogador 7 | 3-6 | 14:50:22 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 7 | 3-6 | 14:50:23 | MOVE Board -> Board: Grompe (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-6 | 14:50:23 | MOVE Board -> Board: Hecarim (i:6.0) <-> LeBlanc (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-6 | 14:50:24 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 19 | 1 | Devastador | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Devastador | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 26 | 1 | Devastador | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 3-7 | 14:50:51 | VENDEU: Fiddlesticks (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 1 | Devastador | DA_Sentinel18 | -0.4900 |  |
| Jogador 7 | 3-7 | 14:50:51 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 1 | Devastador | DA_Sentinel18 | 0.8300 |  |
| Jogador 7 | 3-7 | 14:50:52 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Shen (i:4.0) (tabuleiro slot 25) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 1 | Devastador | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 3-7 | 14:50:52 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Grompe (i:4.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 1 | Devastador | DA_Sentinel18 | 0.0600 |  |
| Jogador 7 | 3-7 | 14:50:53 | MOVE Board -> Board: Azuporã (i:8.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 1 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 3-7 | 14:50:53 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 1 | Devastador | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 3-7 | 14:50:54 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 31 | 1 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-1 | 14:51:19 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 39 | 3 | Devastador | DA_Sentinel18 | 0.7800 |  |
| Jogador 7 | 4-1 | 14:51:19 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Devastador | DA_Murkwolf18 | 0.2700 |  |
| Jogador 7 | 4-1 | 14:51:20 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Devastador | DA_Murkwolf18 | 0.0000 |  |
| Jogador 7 | 4-1 | 14:51:21 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Devastador | DA_Murkwolf18 | 0.5400 |  |
| Jogador 7 | 4-1 | 14:51:21 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Devastador | DA_Murkwolf18 | 0.0100 |  |
| Jogador 7 | 4-1 | 14:51:22 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Devastador | DA_Murkwolf18 | 0.0000 |  |
| Jogador 7 | 4-1 | 14:51:22 | MOVE Board -> Board: Azuporã (i:8.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Devastador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 7 | 4-1 | 14:51:23 | MOVE Board -> Board: Grompe (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Devastador | DA_Murkwolf18 | -0.0600 |  |
| Jogador 7 | 4-1 | 14:51:23 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 36 | 3 | Devastador | DA_Murkwolf18 | -0.0400 |  |
| Jogador 7 | 4-2 | 14:51:52 | VENDEU: Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Devastador | DA_Sentinel18 | -0.5000 |  |
| Jogador 7 | 4-2 | 14:51:52 | COMPROU: Camille (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 3 | Devastador | DA_Sentinel18 | 0.8100 |  |
| Jogador 7 | 4-2 | 14:51:53 | VENDEU: Warwick (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 3 | Devastador | DA_Sentinel18 | -0.6000 |  |
| Jogador 7 | 4-2 | 14:51:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 3 | Devastador | DA_Sentinel18 | 0.8900 |  |
| Jogador 7 | 4-2 | 14:51:54 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Devastador | DA_Sentinel18 | 0.9300 |  |
| Jogador 7 | 4-2 | 14:51:54 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Devastador | DA_Sentinel18 | 0.3600 |  |
| Jogador 7 | 4-2 | 14:51:55 | MOVE Board -> Board: Diana (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 14:51:55 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-2 | 14:51:56 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 3 | Devastador | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 4-3 | 14:52:26 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Devastador | DA_Sentinel18 | 0.8700 |  |
| Jogador 7 | 4-3 | 14:52:26 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Devastador | DA_Sentinel18 | 0.1500 |  |
| Jogador 7 | 4-3 | 14:52:27 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-3 | 14:52:27 | MOVE Board -> Board: Diana (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-3 | 14:52:28 | MOVE Board -> Board: Azuporã (i:8.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-3 | 14:52:29 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 56 | 5 | Devastador | DA_Sentinel18 | -0.2200 |  |
| Jogador 7 | 4-4 | 14:53:01 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Devastador | DA_Sentinel18 | 0.5600 |  |
| Jogador 7 | 4-4 | 14:53:01 | VENDEU: LeBlanc (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 68 | 5 | Devastador | DA_Sentinel18 | -0.4400 |  |
| Jogador 7 | 4-4 | 14:53:02 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Devastador | DA_Sentinel18 | 0.4100 |  |
| Jogador 7 | 4-4 | 14:53:02 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Mamãe Bicuda (i:6.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Devastador | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 4-4 | 14:53:03 | MOVE Board -> Board: Hecarim (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Devastador | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-4 | 14:53:04 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Devastador | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 4-4 | 14:53:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 67 | 5 | Devastador | DA_Sentinel18 | -0.0900 |  |
| Jogador 7 | 4-5 | 14:53:38 | VENDEU: Veigar (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Devastador | DA_Sentinel18 | 0.0100 |  |
| Jogador 7 | 4-5 | 14:53:38 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Devastador | DA_18_Hecarim | 0.7400 |  |
| Jogador 7 | 4-5 | 14:53:39 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Devastador | DA_18_Hecarim | 0.1600 |  |
| Jogador 7 | 4-5 | 14:53:40 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 76 | 5 | Devastador | DA_18_Hecarim | 0.4100 |  |
| Jogador 7 | 4-5 | 14:53:40 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Hecarim | 0.0500 |  |
| Jogador 7 | 4-5 | 14:53:41 | MOVE Board -> Board: Hecarim (i:12.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-5 | 14:53:41 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-5 | 14:53:42 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Hecarim | -0.1000 |  |
| Jogador 7 | 4-6 | 14:54:15 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 83 | 5 | Devastador | DA_18_Hecarim | 0.8100 |  |
| Jogador 7 | 4-6 | 14:54:15 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Devastador | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 4-6 | 14:54:16 | MOVE Board -> Board: Diana (i:6.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Devastador | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-6 | 14:54:16 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Devastador | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-6 | 14:54:17 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 81 | 5 | Devastador | DA_18_Hecarim | -0.1000 |  |
| Jogador 7 | 4-7 | 14:54:55 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Devastador | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_GiantsBelt + TFT_Item_NegatronCloak -> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Devastador | DA_18_Hecarim | 0.1300 |  |
| Jogador 7 | 4-7 | 14:54:56 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 91 | 5 | Devastador | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-7 | 14:54:57 | VENDEU: Grompe (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Hecarim | -0.6000 |  |
| Jogador 7 | 4-7 | 14:54:58 | COMPROU: Grompe (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Hecarim | 0.8200 |  |
| Jogador 7 | 4-7 | 14:54:58 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Diana (i:6.0) (tabuleiro slot 8) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 4-7 | 14:54:59 | MOVE Board -> Board: Diana (i:6.0) <-> Hecarim (i:12.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-7 | 14:54:59 | MOVE Board -> Board: Hecarim (i:12.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 4-7 | 14:55:00 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 94 | 5 | Devastador | DA_18_Hecarim | -0.1200 |  |
| Jogador 7 | 5-1 | 14:55:34 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 105 | 5 | Devastador | DA_18_Hecarim | -0.0300 |  |
| Jogador 7 | 5-1 | 14:55:35 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Devastador | DA_18_Hecarim | 1.0200 |  |
| Jogador 7 | 5-1 | 14:55:36 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Devastador | DA_18_Hecarim | 1.0200 |  |
| Jogador 7 | 5-1 | 14:55:36 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Azuporã (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Devastador | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 5-1 | 14:55:37 | MOVE Board -> Board: Azuporã (i:8.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Devastador | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 5-1 | 14:55:37 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Devastador | DA_18_Hecarim | -0.1800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 5-2 | 14:56:17 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Devastador | DA_18_Hecarim | 0.7200 |  |
| Jogador 7 | 5-2 | 14:56:18 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Devastador | DA_18_Hecarim | -0.2000 |  |
| Jogador 7 | 5-2 | 14:56:18 | MOVE Board -> Board: Camille (i:2.0) <-> Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Devastador | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 5-2 | 14:56:19 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Devastador | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 5-2 | 14:56:19 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Devastador | DA_18_Hecarim | -0.7000 |  |
| Jogador 7 | 5-3 | 14:57:01 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Devastador | DA_18_Hecarim | 0.4600 |  |
| Jogador 7 | 5-3 | 14:57:01 | VENDEU: Grompe (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Devastador | DA_18_Hecarim | -0.7100 |  |
| Jogador 7 | 5-3 | 14:57:02 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Devastador | DA_18_Hecarim | 0.4200 |  |
| Jogador 7 | 5-3 | 14:57:02 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Devastador | DA_18_Hecarim | 0.0900 |  |
| Jogador 7 | 5-3 | 14:57:03 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Hecarim (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Devastador | DA_18_Hecarim | 0.0800 |  |
| Jogador 7 | 5-3 | 14:57:04 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Lobo Trevoguari (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Devastador | DA_18_Hecarim | -0.4100 |  |
| Jogador 7 | 5-3 | 14:57:05 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Devastador | DA_18_Hecarim | 0.0800 |  |
| Jogador 7 | 5-3 | 14:57:06 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Hecarim (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Devastador | DA_18_Hecarim | 0.0800 |  |
| Jogador 7 | 5-3 | 14:57:06 | MOVE Bench -> Board: Hecarim (i:12.0) <-> Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 117 | 5 | Devastador | DA_18_Hecarim | -0.4000 |  |
| Jogador 7 | 5-4 | 14:57:54 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Devastador | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 5-4 | 14:57:55 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 130 | 5 | Devastador | DA_18_Hecarim | 0.4500 |  |
| Jogador 7 | 5-4 | 14:57:56 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Devastador | DA_18_Hecarim | -0.5600 |  |
| Jogador 7 | 5-4 | 14:57:56 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 128 | 5 | Devastador | DA_18_Hecarim | 0.4200 |  |
| Jogador 7 | 5-4 | 14:57:57 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Devastador | DA_18_Hecarim | -0.0700 |  |
| Jogador 7 | 5-4 | 14:57:57 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Devastador | DA_18_Hecarim | -0.0100 |  |
| Jogador 7 | 5-4 | 14:57:58 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Devastador | DA_18_Hecarim | 0.0600 |  |
| Jogador 7 | 5-4 | 14:57:58 | MOVE Bench -> Board: Camille (i:2.0) <-> Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Devastador | DA_18_Hecarim | -0.7100 |  |
| Jogador 7 | 5-4 | 14:57:58 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Lobo Trevoguari (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Devastador | DA_18_Hecarim | -0.4100 |  |
| Jogador 7 | 5-5 | 14:58:38 | VENDEU: Lobo Trevoguari (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Devastador | DA_18_Hecarim | -0.7100 |  |
| Jogador 7 | 5-5 | 14:58:38 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Devastador | DA_18_Hecarim | 0.9000 |  |
| Jogador 7 | 5-5 | 14:58:39 | VENDEU: Krugue (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Devastador | DA_18_Hecarim | -0.0300 |  |
| Jogador 7 | 5-5 | 14:58:40 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Devastador | DA_CrimsonRaptor18 | 1.0600 |  |
| Jogador 7 | 5-5 | 14:58:40 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Devastador | DA_CrimsonRaptor18 | 0.5300 |  |
| Jogador 7 | 5-5 | 14:58:41 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Devastador | DA_CrimsonRaptor18 | -0.1500 |  |
| Jogador 7 | 5-5 | 14:58:41 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Devastador | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 7 | 5-5 | 14:58:42 | COMPROU: Cascalho (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Devastador | DA_CrimsonRaptor18 | 0.1300 |  |
| Jogador 7 | 5-5 | 14:58:42 | MOVE Board -> Board: Diana (i:6.0) <-> Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Devastador | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | ? | 14:46:14 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5900 |  |
| Jogador 8 | ? | 14:46:15 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 14:46:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 14:46:21 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 8 | 1-1 | 14:46:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 14:46:25 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-2 | 14:46:28 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-2 | 14:46:28 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-2 | 14:46:33 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.4200 |  |
| Jogador 8 | 1-3 | 14:46:36 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.6500 |  |
| Jogador 8 | 1-3 | 14:46:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 14:46:37 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-3 | 14:46:39 | MOVE Board -> Board: Veigar (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.2400 |  |
| Jogador 8 | 1-3 | 14:46:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 8 | 1-3 | 14:46:40 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.9800 |  |
| Jogador 8 | 1-3 | 14:46:41 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 1-3 | 14:46:41 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.1000 |  |
| Jogador 8 | 1-3 | 14:46:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 1-4 | 14:46:45 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 8 | 1-4 | 14:46:46 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.9800 |  |
| Jogador 8 | 1-4 | 14:46:48 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.3700 |  |
| Jogador 8 | 1-4 | 14:46:48 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.1400 |  |
| Jogador 8 | 1-4 | 14:46:49 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 8 | 1-4 | 14:46:50 | MOVE Bench -> Board: Leona (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.5500 |  |
| Jogador 8 | 1-4 | 14:46:51 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.2700 |  |
| Jogador 8 | 2-1 | 14:46:54 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Xayah | 0.2800 |  |
| Jogador 8 | 2-1 | 14:46:55 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.2300 |  |
| Jogador 8 | 2-1 | 14:46:55 | MOVE Board -> Board: Leona (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-1 | 14:46:56 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 2-1 | 14:46:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-2 | 14:47:04 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Xayah | 0.9800 |  |
| Jogador 8 | 2-2 | 14:47:04 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Xayah | 0.8400 |  |
| Jogador 8 | 2-2 | 14:47:05 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.3300 |  |
| Jogador 8 | 2-2 | 14:47:05 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.0700 |  |
| Jogador 8 | 2-2 | 14:47:06 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.3300 |  |
| Jogador 8 | 2-2 | 14:47:07 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 2-2 | 14:47:08 | MOVE Board -> Board: Leona (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 2-3 | 14:47:16 | VENDEU: Xayah (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 12 | 0 | — | DA_18_Leona | -0.5000 |  |
| Jogador 8 | 2-3 | 14:47:16 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 9 | 0 | — | DA_18_Leona | -0.1500 |  |
| Jogador 8 | 2-3 | 14:47:16 | VENDEU: Akali (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 10 | 0 | — | DA_18_Leona | 0.0500 |  |
| Jogador 8 | 2-3 | 14:47:17 | COMPROU: Sejuani (Custo 2 \| i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 8 | 0 | — | DA_18_Leona | -0.1000 |  |
| Jogador 8 | 2-3 | 14:47:18 | VENDEU: Xayah (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 9 | 0 | — | DA_18_Leona | -0.0500 |  |
| Jogador 8 | 2-3 | 14:47:18 | COMPROU: Ornn (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 8 | 0 | — | DA_18_Leona | -0.0600 |  |
| Jogador 8 | 2-3 | 14:47:19 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 8 | 0 | — | DA_18_Leona | 0.0000 |  |
| Jogador 8 | 2-3 | 14:47:19 | VENDEU: Ornn (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 9 | 0 | — | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-3 | 14:47:20 | VENDEU: Warwick (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 11 | 0 | — | DA_18_Leona | -0.0400 |  |
| Jogador 8 | 2-4 | 14:47:29 | COMPROU: Karma (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 17 | 1 | Enfeitiçador | DA_18_Leona | 0.8600 |  |
| Jogador 8 | 2-4 | 14:47:29 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Leona | 0.0700 |  |
| Jogador 8 | 2-4 | 14:47:30 | MOVE Bench -> Board: Rammus (i:6.0) <-> Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Leona | -0.4000 |  |
| Jogador 8 | 2-4 | 14:47:31 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_Karma18 | -0.6300 |  |
| Jogador 8 | 2-4 | 14:47:31 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Rammus | -0.5500 |  |
| Jogador 8 | 2-4 | 14:47:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_18_Rammus | 0.1700 |  |
| Jogador 8 | 2-4 | 14:47:32 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Rammus | -0.3400 |  |
| Jogador 8 | 2-4 | 14:47:32 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Rammus | 0.1100 |  |
| Jogador 8 | 2-4 | 14:47:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Rammus | 0.0500 |  |
| Jogador 8 | 2-5 | 14:47:42 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_18_Tristana | 0.2300 |  |
| Jogador 8 | 2-5 | 14:47:43 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | 0.2300 |  |
| Jogador 8 | 2-5 | 14:47:44 | MOVE Bench -> Board: Warwick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | 0.4000 |  |
| Jogador 8 | 2-5 | 14:47:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Espinhos Negros | DA_18_Tristana | 0.1500 |  |
| Jogador 8 | 2-5 | 14:47:45 | MOVE Board -> Board: Warwick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 2-5 | 14:47:45 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 2-5 | 14:47:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Espinhos Negros | DA_18_Tristana | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 2-6 | 14:47:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Tristana | 0.8200 |  |
| Jogador 8 | 2-6 | 14:47:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Tristana | -0.1300 |  |
| Jogador 8 | 2-6 | 14:47:59 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 2-6 | 14:47:59 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Espinhos Negros | DA_18_Tristana | -0.0500 |  |
| Jogador 8 | 2-6 | 14:48:00 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Espinhos Negros | DA_18_Tristana | -0.0500 |  |
| Jogador 8 | 2-6 | 14:48:00 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 2-6 | 14:48:01 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Espinhos Negros | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 2-6 | 14:48:01 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Tristana | 0.2000 |  |
| Jogador 8 | 2-6 | 14:48:02 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 2-7 | 14:48:14 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Espinhos Negros | DA_18_Tristana | 0.2100 |  |
| Jogador 8 | 2-7 | 14:48:14 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 2 | Espinhos Negros | DA_18_Tristana | 0.2100 |  |
| Jogador 8 | 2-7 | 14:48:15 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Espinhos Negros | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 2-7 | 14:48:15 | MOVE Bench -> Board: Tristana (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Espinhos Negros | DA_18_Tristana | -0.3200 |  |
| Jogador 8 | 2-7 | 14:48:16 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Espinhos Negros | DA_18_Tristana | -0.4200 |  |
| Jogador 8 | 2-7 | 14:48:16 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Espinhos Negros | DA_18_Tristana | 0.0400 |  |
| Jogador 8 | 2-7 | 14:48:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 2 | Espinhos Negros | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 2-7 | 14:48:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 2 | Feérico | DA_18_Tristana | -0.0900 |  |
| Jogador 8 | 2-7 | 14:48:17 | MOVE Board -> Board: Yorick (i:2.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 2 | Feérico | DA_18_Tristana | -0.0700 |  |
| Jogador 8 | 3-1 | 14:48:31 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Tristana | -0.1100 |  |
| Jogador 8 | 3-1 | 14:48:32 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 3-1 | 14:48:32 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 15 | 1 | Feérico | DA_18_Tristana | 0.5300 |  |
| Jogador 8 | 3-1 | 14:48:33 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-1 | 14:48:33 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Tristana | 0.1000 |  |
| Jogador 8 | 3-1 | 14:48:34 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-1 | 14:48:34 | MOVE Board -> Board: Yorick (i:2.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-1 | 14:48:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 1 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-2 | 14:48:50 | VENDEU: Rek'Sai (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 3-2 | 14:48:51 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Tristana | 0.5600 |  |
| Jogador 8 | 3-2 | 14:48:51 | MOVE Board -> Board: Rammus (i:6.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-2 | 14:48:52 | MOVE Board -> Board: Warwick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Tristana | 0.0900 |  |
| Jogador 8 | 3-2 | 14:48:52 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Tristana | 0.0100 |  |
| Jogador 8 | 3-2 | 14:48:53 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Tristana | -0.1300 |  |
| Jogador 8 | 3-2 | 14:48:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 3-2 | 14:48:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-3 | 14:49:10 | MOVE Board -> Board: Rammus (i:6.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Feérico | DA_18_Tristana | 0.0700 |  |
| Jogador 8 | 3-3 | 14:49:11 | MOVE Board -> Board: Warwick (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Feérico | DA_18_Tristana | 0.0700 |  |
| Jogador 8 | 3-3 | 14:49:11 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 3-3 | 14:49:12 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 3-3 | 14:49:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 30 | 2 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-4 | 14:49:32 | VENDEU: Elise (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 41 | 3 | Feérico | DA_18_Tristana | 0.0900 |  |
| Jogador 8 | 3-4 | 14:49:32 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Feérico | DA_18_Tristana | 0.1800 |  |
| Jogador 8 | 3-4 | 14:49:33 | MOVE Board -> Board: Yorick (i:2.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-4 | 14:49:33 | MOVE Board -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 3-4 | 14:49:34 | MOVE Board -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-4 | 14:49:34 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 3 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-5 | 14:49:55 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 3 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 3-5 | 14:49:56 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Feérico | DA_18_Tristana | 0.2300 |  |
| Jogador 8 | 3-5 | 14:49:56 | MOVE Board -> Board: Tristana (i:6.0) <-> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 3-5 | 14:49:56 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 3-5 | 14:49:57 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 3 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-6 | 14:50:19 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 57 | 4 | Feérico | DA_18_Tristana | -0.4900 |  |
| Jogador 8 | 3-6 | 14:50:20 | COMPROU: Rammus (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Feérico | DA_18_Tristana | 0.7600 |  |
| Jogador 8 | 3-6 | 14:50:20 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 4 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 3-6 | 14:50:21 | COMPROU: Xayah (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Feérico | DA_18_Tristana | 0.2600 |  |
| Jogador 8 | 3-6 | 14:50:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 50 | 4 | Feérico | DA_18_Tristana | 0.0400 |  |
| Jogador 8 | 3-6 | 14:50:22 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 46 | 4 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 3-6 | 14:50:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 4 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 8 | 3-6 | 14:50:23 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 38 | 4 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 3-6 | 14:50:24 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 34 | 4 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 8 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 8 | 3-7 | 14:50:50 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Feérico | DA_18_Tristana | 0.1800 |  |
| Jogador 8 | 3-7 | 14:50:51 | VENDEU: Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Feérico | DA_18_Tristana | -0.4100 |  |
| Jogador 8 | 3-7 | 14:50:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 3 | Feérico | DA_18_Veigar | 0.8500 |  |
| Jogador 8 | 3-7 | 14:50:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Feérico | DA_18_Veigar | 0.5300 |  |
| Jogador 8 | 3-7 | 14:50:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 3-7 | 14:50:53 | MOVE Board -> Board: Warwick (i:4.0) <-> Rammus (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 8 | 3-7 | 14:50:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Feérico | DA_18_Veigar | -0.1800 |  |
| Jogador 8 | 4-1 | 14:51:19 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Feérico | DA_18_Veigar | 0.1800 |  |
| Jogador 8 | 4-1 | 14:51:19 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 48 | 4 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 8 | 4-1 | 14:51:20 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Feérico | DA_18_Veigar | -0.0700 |  |
| Jogador 8 | 4-1 | 14:51:21 | MOVE Board -> Board: Rammus (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 4-1 | 14:51:21 | MOVE Board -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 8 | 4-1 | 14:51:22 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 44 | 4 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 8 | 4-2 | 14:51:52 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Tristana | -0.5900 |  |
| Jogador 8 | 4-2 | 14:51:52 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Tristana | 0.1800 |  |
| Jogador 8 | 4-2 | 14:51:53 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Yorick (i:2.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Tristana | 0.0800 |  |
| Jogador 8 | 4-2 | 14:51:53 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Rammus (i:6.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Tristana | 0.1100 |  |
| Jogador 8 | 4-2 | 14:51:54 | MOVE Board -> Board: Tristana (i:6.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-2 | 14:51:54 | MOVE Board -> Board: Rammus (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-2 | 14:51:55 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-2 | 14:51:55 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 54 | 4 | Feérico | DA_18_Tristana | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-3 | 14:52:26 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Feérico | DA_18_Tristana | -0.0200 |  |
| Jogador 8 | 4-3 | 14:52:26 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_18_Tristana | 0.8800 |  |
| Jogador 8 | 4-3 | 14:52:27 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 8 | 4-3 | 14:52:27 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 8 | 4-3 | 14:52:28 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-3 | 14:52:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 4-3 | 14:52:29 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 4-3 | 14:52:30 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 56 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 4-3 | 14:52:30 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 52 | 5 | Feérico | DA_18_Tristana | 0.0400 |  |
| Jogador 8 | 4-4 | 14:53:01 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Feérico | DA_18_Tristana | -0.4800 |  |
| Jogador 8 | 4-4 | 14:53:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Feérico | DA_18_Tristana | 0.9100 |  |
| Jogador 8 | 4-4 | 14:53:02 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_18_Tristana | -0.4400 |  |
| Jogador 8 | 4-4 | 14:53:02 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Feérico | DA_18_Tristana | 0.9600 |  |
| Jogador 8 | 4-4 | 14:53:03 | MOVE Bench -> Board: Sivir (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Feérico | DA_18_Tristana | 0.1600 |  |
| Jogador 8 | 4-4 | 14:53:04 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Feérico | DA_18_Tristana | 0.5700 |  |
| Jogador 8 | 4-4 | 14:53:05 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 8 | 4-4 | 14:53:05 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-4 | 14:53:05 | MOVE Board -> Board: Sivir (i:8.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 8 | 4-5 | 14:53:38 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Feérico | DA_18_Tristana | 0.2200 |  |
| Jogador 8 | 4-5 | 14:53:38 | MOVE Board -> Board: Rammus (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Feérico | DA_18_Tristana | 0.0000 |  |
| Jogador 8 | 4-5 | 14:53:39 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 4-5 | 14:53:40 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 61 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 4-5 | 14:53:40 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 57 | 5 | Feérico | DA_18_Tristana | 0.0600 |  |
| Jogador 8 | 4-5 | 14:53:41 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 53 | 5 | Feérico | DA_18_Tristana | 0.0400 |  |
| Jogador 8 | 4-5 | 14:53:41 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 49 | 5 | Feérico | DA_18_Tristana | -0.0400 |  |
| Jogador 8 | 4-5 | 14:53:42 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 45 | 5 | Feérico | DA_18_Tristana | 0.0300 |  |
| Jogador 8 | 4-5 | 14:53:42 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 41 | 5 | Feérico | DA_18_Tristana | 0.0300 |  |
| Jogador 8 | 4-6 | 14:54:15 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Feérico | DA_18_Sivir | -0.6000 |  |
| Jogador 8 | 4-6 | 14:54:15 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Sivir | 0.1800 |  |
| Jogador 8 | 4-6 | 14:54:16 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Feérico | DA_18_Sivir | -0.0300 |  |
| Jogador 8 | 4-6 | 14:54:16 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Feérico | DA_18_Sivir | 0.6800 |  |
| Jogador 8 | 4-6 | 14:54:17 | BUY XP | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Sivir | 0.8000 |  |
| Jogador 8 | 4-6 | 14:54:17 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Sivir | 0.4500 |  |
| Jogador 8 | 4-6 | 14:54:18 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 4-6 | 14:54:19 | MOVE Board -> Board: Sivir (i:8.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Sivir | -0.0100 |  |
| Jogador 8 | 4-6 | 14:54:20 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 53 | 4 | Feérico | DA_18_Sivir | -0.2000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-7 | 14:54:55 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Sivir | 0.1800 |  |
| Jogador 8 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Sivir | 0.1600 |  |
| Jogador 8 | 4-7 | 14:54:56 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Sivir | 0.1700 |  |
| Jogador 8 | 4-7 | 14:54:57 | MOVE Bench -> Board: Zyra (i:8.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Sivir | -0.4000 |  |
| Jogador 8 | 4-7 | 14:54:58 | MOVE Board -> Board: Zyra (i:8.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Sivir | -0.0100 |  |
| Jogador 8 | 4-7 | 14:54:58 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 60 | 5 | Feérico | DA_18_Sivir | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 5-1 | 14:55:34 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Feérico | DA_18_Sivir | -0.0400 |  |
| Jogador 8 | 5-1 | 14:55:35 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_18_Sivir | 0.7500 |  |
| Jogador 8 | 5-1 | 14:55:36 | MOVE Board -> Board: Rammus (i:6.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 5-1 | 14:55:36 | MOVE Board -> Board: Warwick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_18_Sivir | -0.0100 |  |
| Jogador 8 | 5-1 | 14:55:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_18_Sivir | -0.0200 |  |
| Jogador 8 | 5-1 | 14:55:37 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Feérico | DA_18_Sivir | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 5-2 | 14:56:17 | MOVE Board -> Board: Rammus (i:6.0) <-> Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Feérico | DA_18_Sivir | 0.0000 |  |
| Jogador 8 | 5-2 | 14:56:18 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Feérico | DA_CrimsonRaptor18 | -0.0100 |  |
| Jogador 8 | 5-2 | 14:56:18 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 85 | 5 | Feérico | DA_CrimsonRaptor18 | -0.3100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 5-3 | 14:57:01 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 102 | 5 | Feérico | DA_CrimsonRaptor18 | -0.5100 |  |
| Jogador 8 | 5-3 | 14:57:01 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 99 | 5 | Feérico | DA_Fiddlesticks18 | 1.0200 |  |
| Jogador 8 | 5-3 | 14:57:02 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Feérico | DA_Fiddlesticks18 | 0.7500 |  |
| Jogador 8 | 5-3 | 14:57:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 94 | 5 | Feérico | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 8 | 5-3 | 14:57:03 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Feérico | DA_Fiddlesticks18 | 0.6800 |  |
| Jogador 8 | 5-3 | 14:57:04 | MOVE Board -> Board: Rakan (i:2.0) <-> Rammus (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 8 | 5-3 | 14:57:05 | MOVE Board -> Board: Rammus (i:6.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 8 | 5-3 | 14:57:06 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Feérico | DA_Fiddlesticks18 | -0.1600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 5-4 | 14:57:54 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 113 | 5 | Feérico | DA_CrimsonRaptor18 | -0.6000 |  |
| Jogador 8 | 5-4 | 14:57:55 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_CrimsonRaptor18 | 0.3800 |  |
| Jogador 8 | 5-4 | 14:57:56 | MOVE Board -> Board: Sivir (i:8.0) <-> Zyra (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_CrimsonRaptor18 | 0.0000 |  |
| Jogador 8 | 5-4 | 14:57:56 | MOVE Board -> Board: Zyra (i:8.0) <-> Warwick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_18_Zyra | -0.0100 |  |
| Jogador 8 | 5-4 | 14:57:57 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 112 | 5 | Feérico | DA_18_Zyra | -0.1800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 5-5 | 14:58:38 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Zyra | -0.5900 |  |
| Jogador 8 | 5-5 | 14:58:38 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Feérico | DA_18_Rammus | 1.0500 |  |
| Jogador 8 | 5-5 | 14:58:39 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Feérico | DA_18_Rammus | 0.3500 |  |
| Jogador 8 | 5-5 | 14:58:40 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Feérico | DA_18_Rammus | 0.4300 |  |
| Jogador 8 | 5-5 | 14:58:40 | MOVE Bench -> Board: Rammus (i:6.0) <-> Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 118 | 5 | Feérico | DA_18_Rammus | -0.3800 |  |
| Jogador 8 | 5-5 | 14:58:41 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Feérico | DA_18_Rammus | -0.0700 |  |
| Jogador 8 | 5-5 | 14:58:41 | VENDEU: Rammus (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Feérico | DA_18_Zyra | -0.7100 |  |
| Jogador 8 | 5-5 | 14:58:42 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Feérico | DA_18_Zyra | 0.4600 |  |
| Jogador 8 | 5-5 | 14:58:42 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Mamãe Bicuda (i:6.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 121 | 5 | Feérico | DA_18_Zyra | 0.0900 |  |
| Jogador 8 | 5-6 | 14:59:22 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Feérico | DA_18_Zyra | -0.6200 |  |
| Jogador 8 | 5-6 | 14:59:22 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Feérico | DA_18_Zyra | 0.8900 |  |
| Jogador 8 | 5-6 | 14:59:24 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Feérico | DA_18_Zyra | -0.0600 |  |
| Jogador 8 | 5-6 | 14:59:24 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Feérico | DA_18_Zyra | -0.1600 |  |
| Jogador 8 | 5-6 | 14:59:25 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Feérico | DA_18_Zyra | -0.0700 |  |
| Jogador 8 | 5-6 | 14:59:25 | VENDEU: Rengar (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Feérico | DA_18_Zyra | 0.0000 |  |
| Jogador 8 | 5-6 | 14:59:26 | COMPROU: Amumu (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Feérico | DA_18_Zyra | 0.0400 |  |
| Jogador 8 | 5-6 | 14:59:26 | VENDEU: Amumu (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Feérico | DA_18_Zyra | -0.0200 |  |
| Jogador 8 | 5-6 | 14:59:27 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Feérico | DA_18_Zyra | 0.5100 |  |
| Jogador 8 | 5-7 | 15:00:12 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Rakan | 1.1100 |  |
| Jogador 8 | 5-7 | 15:00:12 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 141 | 5 | Feérico | DA_18_Rakan | 0.9400 |  |
| Jogador 8 | 5-7 | 15:00:13 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Rakan | 0.4500 |  |
| Jogador 8 | 5-7 | 15:00:13 | EQUIP_FROM_INVENTORY: DA_18_EmblemHunter -> Mamãe Bicuda (i:6.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Rakan | -0.0200 |  |
| Jogador 8 | 5-7 | 15:00:14 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Feérico | DA_18_Rakan | -0.0700 |  |
| Jogador 8 | 5-7 | 15:00:14 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Feérico | DA_18_Zyra | -0.7000 |  |
| Jogador 8 | 5-7 | 15:00:14 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Zyra | 0.4600 |  |
| Jogador 8 | 5-7 | 15:00:15 | EQUIP_FROM_INVENTORY: TFT_Item_RabadonsDeathcap -> Mamãe Bicuda (i:6.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Zyra | 0.0900 |  |
| Jogador 8 | 5-7 | 15:00:15 | EQUIP_FROM_INVENTORY: TFT_Item_DragonsClaw -> Warwick (i:4.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 138 | 5 | Feérico | DA_18_Zyra | 0.0800 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 28 | 28 | 140 | 28 | 16 | 199 | 13 | 37 |
| Jogador 2 | 26 | 26 | 130 | 26 | 16 | 159 | 8 | 17 |
| Jogador 3 | 24 | 25 | 125 | 24 | 18 | 129 | 5 | 19 |
| Jogador 4 | 24 | 24 | 120 | 24 | 15 | 160 | 17 | 12 |
| Jogador 5 | 33 | 33 | 165 | 33 | 17 | 220 | 18 | 49 |
| Jogador 6 | 31 | 35 | 175 | 31 | 16 | 208 | 14 | 34 |
| Jogador 7 | 31 | 32 | 160 | 31 | 18 | 215 | 11 | 44 |
| Jogador 8 | 33 | 37 | 185 | 33 | 18 | 234 | 22 | 43 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 199 | 199 | 199 | 0 | 188 | 0 | 199 | 199 | 199 | 58/43 |
| Jogador 2 | 159 | 159 | 159 | 0 | 147 | 0 | 159 | 159 | 159 | 39/25 |
| Jogador 3 | 129 | 129 | 129 | 0 | 124 | 0 | 129 | 129 | 129 | 33/20 |
| Jogador 4 | 160 | 160 | 160 | 0 | 153 | 0 | 160 | 160 | 160 | 44/30 |
| Jogador 5 | 220 | 220 | 220 | 0 | 209 | 0 | 220 | 220 | 220 | 63/47 |
| Jogador 6 | 208 | 208 | 208 | 0 | 195 | 0 | 208 | 208 | 208 | 56/41 |
| Jogador 7 | 215 | 215 | 215 | 0 | 199 | 0 | 215 | 215 | 215 | 62/47 |
| Jogador 8 | 234 | 234 | 234 | 0 | 221 | 0 | 234 | 234 | 234 | 67/52 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.511091411113739 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24879175424575806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.287935346364975 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 36 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5254529118537903 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0389666557312012 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 49 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.026097297668457 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03983444347977638 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 51 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016042277216911316 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1456615924835205 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 53 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 54 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1106451749801636 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.34806638956069946 | 0.0 | 0.0 | +57652644-f861-47bc-addd-90760a272b22 / -— |
| Jogador 1 | 2-1 | 61 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22100159525871277 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20685763657093048 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17597316205501556 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043152593076229095 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4940270781517029 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31481704115867615 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 68 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2633734345436096 | 0.0 | 0.0 | +56a8c7e1-c6a6-47e0-9a00-6416cf6f068f / -— |
| Jogador 1 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030097467824816704 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22418080270290375 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 71 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 72 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06366962939500809 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 74 | BUY | STABILIZE | 91.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8502488136291504 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 91.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5161296725273132 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-3 | 76 | SELL | STABILIZE | 91.0 | 4 | 12 | 1 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13566666841506958 | 0.0 | 0.0 | +— / -cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-3 | 77 | BUY | STABILIZE | 91.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29645639657974243 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 91.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3563465178012848 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 79 | BUY_XP | STABILIZE | 91.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 91.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004089487716555595 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 91.0 | 5 | 13 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34183844923973083 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 83 | BUY | STABILIZE | 91.0 | 5 | 10 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1926679015159607 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -— |
| Jogador 1 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 9 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4168728291988373 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 85 | BUY | STABILIZE | 91.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.210529625415802 | 0.0 | 0.0 | +7d8f4f6b-4eba-4c31-9834-bd81a3765520 / -— |
| Jogador 1 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999479055404663 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 88 | PASS | STABILIZE | 91.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 91.0 | 5 | 12 | 1 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8953906893730164 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 91.0 | 5 | 10 | 1 | 14.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060126081109046936 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 94 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 8 | 0 | 14.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004121595702599734 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 8 | 0 | 14.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07700207084417343 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | PASS | STABILIZE | 91.0 | 5 | 8 | 0 | 14.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 91.0 | 5 | 15 | 1 | 14.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499450325965881 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 14 | 1 | 12.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11950798332691193 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 14 | 1 | 14.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4303700625896454 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 105 | BUY | STABILIZE | 91.0 | 5 | 14 | 1 | 16.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21759864687919617 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 106 | BUY | STABILIZE | 91.0 | 5 | 11 | 1 | 16.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29829972982406616 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 8 | 0 | 16.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0595732107758522 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 8 | 0 | 16.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08659566938877106 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 8 | 0 | 16.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01614641584455967 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 110 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 8 | 0 | 16.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39151883125305176 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | SELL | STABILIZE | 86.0 | 5 | 13 | 1 | 16.0 | Inferno/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 86.0 | 5 | 16 | 1 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7188008427619934 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 114 | EQUIP_FROM_INVENTORY | STABILIZE | 86.0 | 5 | 14 | 1 | 16.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14296779036521912 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 115 | EQUIP_FROM_INVENTORY | STABILIZE | 86.0 | 5 | 14 | 1 | 16.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1531871110200882 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 116 | SELL | STABILIZE | 86.0 | 5 | 14 | 1 | 16.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025888638570904732 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-7 | 117 | BUY | STABILIZE | 86.0 | 5 | 15 | 1 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14415182173252106 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -— |
| Jogador 1 | 2-7 | 118 | MOVE_BENCH | STABILIZE | 86.0 | 5 | 14 | 1 | 16.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09198493510484695 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 119 | SELL | STABILIZE | 86.0 | 5 | 14 | 1 | 18.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00759226456284523 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 2-7 | 120 | BUY | STABILIZE | 86.0 | 5 | 17 | 1 | 18.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019701693207025528 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 86.0 | 5 | 21 | 2 | 18.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24145632982254028 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 123 | SELL | STABILIZE | 86.0 | 5 | 21 | 2 | 18.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026436544954776764 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 1 | 3-1 | 124 | BUY | STABILIZE | 86.0 | 5 | 23 | 2 | 18.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035634346306324005 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 86.0 | 5 | 20 | 2 | 18.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6975858211517334 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 86.0 | 5 | 20 | 2 | 18.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07904387265443802 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 127 | PASS | STABILIZE | 86.0 | 5 | 20 | 2 | 16.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | SELL | STABILIZE | 77.0 | 5 | 28 | 2 | 16.0 | Inferno/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048486605286598206 | 0.0 | 0.0 | +— / -7d8f4f6b-4eba-4c31-9834-bd81a3765520 |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 77.0 | 5 | 30 | 3 | 16.0 | Inferno/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7805690169334412 | 0.0 | 0.0 | +5204a655-be8f-4607-8fa3-28c981ac1397 / -760d5bee-7d64-4f03-abf0-6357c914a1ed,b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 77.0 | 5 | 28 | 2 | 12.0 | Inferno/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40436506271362305 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | BUY | STABILIZE | 77.0 | 5 | 28 | 2 | 18.0 | Inferno/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17072902619838715 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 136 | BUY | STABILIZE | 77.0 | 5 | 25 | 2 | 18.0 | Inferno/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03703295812010765 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 21 | 2 | 18.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17245782911777496 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 21 | 2 | 18.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15727870166301727 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 139 | BUY_XP | STABILIZE | 77.0 | 5 | 21 | 2 | 18.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 140 | BUY_XP | STABILIZE | 77.0 | 5 | 17 | 1 | 18.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 20 | 2 | 18.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39402520656585693 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 143 | BUY | STABILIZE | 77.0 | 6 | 20 | 2 | 24.0 | Inferno/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07630308717489243 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 17 | 1 | 24.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007119307294487953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 17 | 1 | 24.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025627942755818367 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 17 | 1 | 24.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004325360059738159 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 147 | PASS | STABILIZE | 77.0 | 6 | 17 | 1 | 24.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | SELL | STABILIZE | 77.0 | 6 | 25 | 2 | 24.0 | Inferno/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -5204a655-be8f-4607-8fa3-28c981ac1397 |
| Jogador 1 | 3-4 | 153 | BUY | STABILIZE | 77.0 | 6 | 30 | 3 | 24.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6434089541435242 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 28 | 2 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.3642969861393794e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 155 | SELL | STABILIZE | 77.0 | 6 | 28 | 2 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023499999195337296 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 3-4 | 156 | BUY | STABILIZE | 77.0 | 6 | 29 | 2 | 24.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027684472501277924 | 0.0 | 0.0 | +c07fa6e1-195e-4a06-ba8f-b75213704c8a / -— |
| Jogador 1 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 28 | 2 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.195224265567958e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 158 | BUY_XP | STABILIZE | 77.0 | 6 | 28 | 2 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011656000278890133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 159 | BUY_XP | STABILIZE | 77.0 | 6 | 24 | 2 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011656000278890133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 160 | BUY_XP | STABILIZE | 77.0 | 6 | 20 | 2 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | SELL | STABILIZE | 77.0 | 6 | 23 | 2 | 24.0 | Inferno/DA_18_Ezreal | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03856666758656502 | 0.0 | 0.0 | +— / -45450b46-63b4-488f-9469-3348c6da8f4b |
| Jogador 1 | 3-5 | 163 | BUY | STABILIZE | 77.0 | 6 | 26 | 2 | 24.0 | Inferno/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8509039878845215 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 24 | 2 | 20.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7185630202293396 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 165 | BUY | FAST8 | 77.0 | 6 | 24 | 2 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04706862196326256 | 0.0 | 0.0 | +a9184317-58b7-4804-9aef-3e2c08c20935 / -— |
| Jogador 1 | 3-5 | 166 | MOVE_BOARD | FAST8 | 77.0 | 6 | 23 | 2 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0021435068920254707 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 167 | MOVE_BOARD | FAST8 | 77.0 | 6 | 23 | 2 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015832193195819855 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | MOVE_BOARD | FAST8 | 77.0 | 6 | 23 | 2 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022116059437394142 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 169 | PASS | FAST8 | 77.0 | 6 | 23 | 2 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05999999865889549 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | BUY | FAST8 | 77.0 | 6 | 32 | 3 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2451619952917099 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 173 | SELL | FAST8 | 77.0 | 6 | 30 | 3 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024389585480093956 | 0.0 | 0.0 | +— / -a9184317-58b7-4804-9aef-3e2c08c20935 |
| Jogador 1 | 3-6 | 174 | BUY | FAST8 | 77.0 | 6 | 31 | 3 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6851609349250793 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 175 | MOVE_BENCH | FAST8 | 77.0 | 6 | 29 | 2 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10572323948144913 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 176 | MOVE_BOARD | FAST8 | 77.0 | 6 | 29 | 2 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 177 | MOVE_BOARD | FAST8 | 77.0 | 6 | 29 | 2 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01291792280972004 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 178 | PASS | FAST8 | 77.0 | 6 | 29 | 2 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02449999935925007 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | FAST8 | 64.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4073333442211151 | 0.0 | 0.0 | +— / -56a8c7e1-c6a6-47e0-9a00-6416cf6f068f |
| Jogador 1 | 3-7 | 183 | BUY | FAST8 | 64.0 | 6 | 38 | 3 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04144442081451416 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 184 | SELL | FAST8 | 64.0 | 6 | 34 | 3 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-7 | 185 | BUY | FAST8 | 64.0 | 6 | 36 | 3 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029579542577266693 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 186 | MOVE_BOARD | FAST8 | 64.0 | 6 | 34 | 3 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015304397093132138 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 187 | MOVE_BOARD | FAST8 | 64.0 | 6 | 34 | 3 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01555583719164133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 188 | PASS | FAST8 | 64.0 | 6 | 34 | 3 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 64.0 | 6 | 42 | 4 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17704851925373077 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 64.0 | 6 | 42 | 4 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.177094504237175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | SELL | FAST8 | 64.0 | 6 | 42 | 4 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011448423378169537 | 0.0 | 0.0 | +— / -227dbcdb-af5c-4318-94d1-f01a7847d100 |
| Jogador 1 | 4-1 | 195 | BUY | FAST8 | 64.0 | 6 | 44 | 4 | 28.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015189792960882187 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 196 | MOVE_BENCH | FAST8 | 64.0 | 6 | 41 | 4 | 28.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3844096064567566 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 197 | SELL | FAST8 | 64.0 | 6 | 41 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010833333246409893 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 4-1 | 198 | BUY | FAST8 | 64.0 | 6 | 44 | 4 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15095505118370056 | 0.0 | 0.0 | +e7c8751e-5d30-4953-9508-35488b6c45db / -— |
| Jogador 1 | 4-1 | 199 | MOVE_BOARD | FAST8 | 64.0 | 6 | 41 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.817853444663342e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 200 | MOVE_BOARD | FAST8 | 64.0 | 6 | 41 | 4 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01508138794451952 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | FAST8 | 53.0 | 6 | 51 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013068512082099915 | 0.0 | 0.0 | +— / -e7c8751e-5d30-4953-9508-35488b6c45db |
| Jogador 1 | 4-2 | 203 | BUY | FAST8 | 53.0 | 6 | 54 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5572705864906311 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 204 | SELL | FAST8 | 53.0 | 6 | 51 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 4-2 | 205 | BUY | FAST8 | 53.0 | 6 | 54 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30842894315719604 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | FAST8 | 53.0 | 6 | 53 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.849208436207846e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 207 | MOVE_BOARD | FAST8 | 53.0 | 6 | 53 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015136988833546638 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 208 | MOVE_BOARD | FAST8 | 53.0 | 6 | 53 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01486220397055149 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 209 | PASS | FAST8 | 53.0 | 6 | 53 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08158450573682785 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | SELL | FAST8 | 53.0 | 6 | 64 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2652333378791809 | 0.0 | 0.0 | +— / -c07fa6e1-195e-4a06-ba8f-b75213704c8a |
| Jogador 1 | 4-3 | 213 | BUY | FAST8 | 53.0 | 6 | 65 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8925443291664124 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 4-3 | 214 | MOVE_BENCH | FAST8 | 53.0 | 6 | 63 | 5 | 30.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43502843379974365 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 215 | BUY | FAST8 | 53.0 | 6 | 63 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010555047541856766 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 1 | 4-3 | 216 | MOVE_BOARD | FAST8 | 53.0 | 6 | 62 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 217 | MOVE_BOARD | FAST8 | 53.0 | 6 | 62 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014666058123111725 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 218 | PASS | FAST8 | 53.0 | 6 | 62 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22728049755096436 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | BUY | FAST8 | 42.0 | 6 | 72 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22331015765666962 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 1 | 4-4 | 223 | SELL | FAST8 | 42.0 | 6 | 70 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8500000238418579 | 0.0 | 0.0 | +— / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 |
| Jogador 1 | 4-4 | 224 | EQUIP_FROM_INVENTORY | FAST8 | 42.0 | 6 | 75 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14107893407344818 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 225 | EQUIP_FROM_INVENTORY | FAST8 | 42.0 | 6 | 75 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14107893407344818 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 226 | BUY | FAST8 | 42.0 | 6 | 75 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21908918023109436 | 0.0 | 0.0 | +2357a4df-3c61-4957-83c3-572bbb99ac5a / -— |
| Jogador 1 | 4-4 | 227 | MOVE_BOARD | FAST8 | 42.0 | 6 | 73 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.322964966580912e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 228 | MOVE_BOARD | FAST8 | 42.0 | 6 | 73 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015007455833256245 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 229 | MOVE_BOARD | FAST8 | 42.0 | 6 | 73 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014992287382483482 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 230 | PASS | FAST8 | 42.0 | 6 | 73 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10267896950244904 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | FAST8 | 42.0 | 6 | 83 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006634758319705725 | 0.0 | 0.0 | +— / -2357a4df-3c61-4957-83c3-572bbb99ac5a |
| Jogador 1 | 4-5 | 233 | BUY | FAST8 | 42.0 | 6 | 85 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4452705383300781 | 0.0 | 0.0 | +1022f12a-84e9-4eeb-81dc-706092de3728 / -— |
| Jogador 1 | 4-5 | 234 | SELL | FAST8 | 42.0 | 6 | 82 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -a7893c5d-2faa-4292-9240-f3cc5813151e |
| Jogador 1 | 4-5 | 235 | BUY | FAST8 | 42.0 | 6 | 84 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1096598356962204 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 1 | 4-5 | 236 | SELL | FAST8 | 42.0 | 6 | 80 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00026424313546158373 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 1 | 4-5 | 237 | BUY | FAST8 | 42.0 | 6 | 84 | 5 | 32.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004404266364872456 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 1 | 4-5 | 238 | BUY_XP | FAST8 | 42.0 | 6 | 81 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055743999779224396 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 239 | BUY_XP | FAST8 | 42.0 | 6 | 77 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6859250068664551 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 240 | MOVE_BENCH | FAST8 | 42.0 | 7 | 73 | 5 | 32.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40284812450408936 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | BUY | FAST8 | 42.0 | 7 | 84 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7969333529472351 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 1 | 4-6 | 243 | MOVE_BOARD | FAST8 | 42.0 | 7 | 81 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00033778444048948586 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 244 | MOVE_BOARD | FAST8 | 42.0 | 7 | 81 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015520214103162289 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 245 | PASS | FAST8 | 42.0 | 7 | 81 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10932040959596634 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 252 | SELL | STABILIZE | 30.0 | 7 | 91 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -5b96c8f7-bacb-47df-8666-30d30d49549d |
| Jogador 1 | 4-7 | 253 | BUY | STABILIZE | 30.0 | 7 | 94 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8897391557693481 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 1 | 4-7 | 254 | SELL | STABILIZE | 30.0 | 7 | 91 | 5 | 34.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 |
| Jogador 1 | 4-7 | 255 | BUY | STABILIZE | 30.0 | 7 | 95 | 5 | 34.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8195281624794006 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -1022f12a-84e9-4eeb-81dc-706092de3728,15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 4-7 | 256 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 92 | 5 | 28.0 | Inferno/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39396947622299194 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 257 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 92 | 5 | 32.0 | Inferno/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5360813140869141 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 258 | BUY | STABILIZE | 30.0 | 7 | 92 | 5 | 34.0 | Inferno/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2120673954486847 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 1 | 4-7 | 259 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 89 | 5 | 34.0 | Inferno/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 260 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 89 | 5 | 34.0 | Inferno/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018353064078837633 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 262 | BUY | STABILIZE | 30.0 | 7 | 99 | 5 | 34.0 | Inferno/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.023539423942566 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -d01cae02-d8ba-491e-841f-bf3120953933,d1bc6c5b-74a5-46db-b00f-e91265546f5d |
| Jogador 1 | 5-1 | 263 | BUY | STABILIZE | 30.0 | 7 | 96 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04311913624405861 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 1 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 30.0 | 7 | 93 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08426593989133835 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 265 | CRAFT_AND_EQUIP | STABILIZE | 30.0 | 7 | 93 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18285152316093445 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 266 | BUY | STABILIZE | 30.0 | 7 | 93 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5161677598953247 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 1 | 5-1 | 267 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 90 | 5 | 34.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3976583480834961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 268 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 90 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 269 | PASS | STABILIZE | 30.0 | 7 | 90 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15917730331420898 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 272 | SELL | STABILIZE | 30.0 | 7 | 101 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40237778425216675 | 0.0 | 0.0 | +— / -68301141-c9f1-4303-9775-753520772836 |
| Jogador 1 | 5-2 | 273 | BUY | STABILIZE | 30.0 | 7 | 109 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9092234969139099 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 1 | 5-2 | 274 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 108 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.779924438480521e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 275 | SELL | STABILIZE | 30.0 | 7 | 108 | 5 | 38.0 | Inferno/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -02d3d068-e592-4f9c-a574-914955401575 |
| Jogador 1 | 5-2 | 276 | BUY | STABILIZE | 30.0 | 7 | 116 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21673330664634705 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 1 | 5-2 | 277 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 113 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.3037353003019234e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 278 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 113 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018787411972880363 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 279 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 113 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02197224460542202 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 280 | PASS | STABILIZE | 30.0 | 7 | 113 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1854415386915207 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 282 | SELL | ALL_IN | 16.0 | 7 | 123 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -2949d735-3c16-4a45-835b-e11a9c12b16a |
| Jogador 1 | 5-3 | 283 | BUY | ALL_IN | 16.0 | 7 | 126 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9844774007797241 | 0.0 | 0.0 | +c7762d7d-bcfa-4694-a3fc-038d7242207f / -— |
| Jogador 1 | 5-3 | 284 | SELL | ALL_IN | 16.0 | 7 | 125 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619239211082458 | 0.0 | 0.0 | +— / -2f5d8cb8-8ba3-45e9-a345-00e931d34490 |
| Jogador 1 | 5-3 | 285 | BUY | ALL_IN | 16.0 | 7 | 128 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49430936574935913 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 1 | 5-3 | 286 | SELL | ALL_IN | 16.0 | 7 | 126 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020236147567629814 | 0.0 | 0.0 | +— / -ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 1 | 5-3 | 287 | BUY | ALL_IN | 16.0 | 7 | 129 | 5 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43553426861763 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 1 | 5-3 | 288 | MOVE_BOARD | ALL_IN | 16.0 | 7 | 126 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004546658135950565 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 289 | MOVE_BOARD | ALL_IN | 16.0 | 7 | 126 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034518763422966 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 290 | MOVE_BENCH | ALL_IN | 16.0 | 7 | 126 | 5 | 38.0 | Inferno/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07336433976888657 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.21754200756549835 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17793168127536774 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5746603608131409 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1177988052368164 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 36 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4684927761554718 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4051581621170044 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 49 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0718024969100952 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0884234756231308 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 51 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5537455677986145 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0373989343643188 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20083950459957123 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 61 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2349543273448944 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24891069531440735 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38717809319496155 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017356421798467636 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036084774881601334 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 67 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179227828979492 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 68 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25828829407691956 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01148625835776329 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 71 | PASS | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24424611032009125 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 75 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03604252636432648 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032969266176223755 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027697956189513206 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 78 | BUY_XP | STABILIZE | 100.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 79 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015038283541798592 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33718425035476685 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 83 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40374237298965454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 84 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18907630443572998 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.946086558746174e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 86 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20904910564422607 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23229855298995972 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10633579641580582 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007004937157034874 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3025020956993103 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025499338284134865 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 2 | 2-5 | 94 | BUY | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2581334114074707 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 18.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40501534938812256 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 96 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32991352677345276 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 97 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 102 | SELL | STABILIZE | 89.0 | 5 | 6 | 0 | 16.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8374999761581421 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-6 | 103 | BUY | STABILIZE | 89.0 | 5 | 9 | 0 | 16.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8959678411483765 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 7 | 0 | 16.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04196741059422493 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 7 | 0 | 18.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4197697639465332 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 106 | PASS | STABILIZE | 89.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 112 | SELL | STABILIZE | 83.0 | 5 | 13 | 1 | 14.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010300000198185444 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-7 | 113 | BUY | STABILIZE | 83.0 | 5 | 14 | 1 | 14.0 | Colosso/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7571927905082703 | 0.0 | 0.0 | +0067f61f-504d-440a-b071-de7f18886e3d / -— |
| Jogador 2 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 14.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2378861904144287 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 16.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039227209985256195 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 116 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 18.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41685786843299866 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 117 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 14.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35338452458381653 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 118 | PASS | STABILIZE | 83.0 | 5 | 13 | 1 | 16.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 83.0 | 5 | 20 | 2 | 16.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17066438496112823 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 123 | SELL | STABILIZE | 83.0 | 5 | 20 | 2 | 16.0 | Colosso/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -11a1c814-5357-4f19-944f-aa11d6bf8384 |
| Jogador 2 | 3-1 | 124 | BUY | STABILIZE | 83.0 | 5 | 23 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.2934451997280121 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 125 | EQUIP_FROM_INVENTORY | STABILIZE | 83.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11271893233060837 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 126 | EQUIP_FROM_INVENTORY | STABILIZE | 83.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10338388383388519 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 127 | BUY_XP | STABILIZE | 83.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 128 | BUY_XP | STABILIZE | 83.0 | 5 | 18 | 1 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 129 | BUY_XP | STABILIZE | 83.0 | 5 | 14 | 1 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07806999981403351 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 130 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 10 | 1 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45284682512283325 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 132 | BUY | STABILIZE | 74.0 | 6 | 17 | 1 | 18.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.807843804359436 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 133 | MOVE_BOARD | STABILIZE | 74.0 | 6 | 16 | 1 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 134 | MOVE_BOARD | STABILIZE | 74.0 | 6 | 16 | 1 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015284447930753231 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 135 | PASS | STABILIZE | 74.0 | 6 | 16 | 1 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 142 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 24 | 2 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 143 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 24 | 2 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014949839562177658 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 144 | PASS | STABILIZE | 63.0 | 6 | 24 | 2 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02199999988079071 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 32 | 3 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0010193496709689498 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 153 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 32 | 3 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01517533976584673 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 32 | 3 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014969072304666042 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 155 | PASS | STABILIZE | 63.0 | 6 | 32 | 3 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026000000536441803 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 40 | 4 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06720535457134247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 40 | 4 | 16.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3921010196208954 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 40 | 4 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 165 | PASS | STABILIZE | 63.0 | 6 | 40 | 4 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 172 | SELL | STABILIZE | 63.0 | 6 | 51 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 63.0 | 6 | 54 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8652287721633911 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 51 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00030618731398135424 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 51 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014672606252133846 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 51 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015108885243535042 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 177 | PASS | STABILIZE | 63.0 | 6 | 51 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05633125081658363 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | SELL | STABILIZE | 53.0 | 6 | 61 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -6a071ec5-c3f4-41b3-a0d8-c1aee62cffee |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 53.0 | 6 | 64 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07487833499908447 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 184 | MOVE_BOARD | STABILIZE | 53.0 | 6 | 61 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 53.0 | 6 | 61 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014980791136622429 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 186 | PASS | STABILIZE | 53.0 | 6 | 61 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060631174594163895 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 53.0 | 6 | 71 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17521235346794128 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 53.0 | 6 | 71 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21991966664791107 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 194 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 71 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28713053464889526 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 195 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 71 | 5 | 14.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08574209362268448 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 71 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05266069620847702 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 197 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 71 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4147387742996216 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 198 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 71 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 199 | PASS | STABILIZE | 53.0 | 6 | 71 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09347418695688248 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 202 | SELL | STABILIZE | 53.0 | 6 | 82 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018525153398513794 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 4-2 | 203 | BUY | STABILIZE | 53.0 | 6 | 85 | 5 | 18.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9612693190574646 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-2 | 204 | MOVE_BENCH | STABILIZE | 53.0 | 6 | 84 | 5 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.512231171131134 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 205 | BUY | STABILIZE | 53.0 | 6 | 84 | 5 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4665522277355194 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 2 | 4-2 | 206 | BUY | STABILIZE | 53.0 | 6 | 81 | 5 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017688177525997162 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 2 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 53.0 | 6 | 80 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 53.0 | 6 | 80 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 209 | PASS | STABILIZE | 53.0 | 6 | 80 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09994778037071228 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 90 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004207201418466866 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 213 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 90 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014610083773732185 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 214 | PASS | STABILIZE | 41.0 | 6 | 90 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11928441375494003 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | SELL | STABILIZE | 30.0 | 6 | 101 | 5 | 22.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-4 | 223 | BUY | STABILIZE | 30.0 | 6 | 104 | 5 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9618309140205383 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -561fb9a8-e987-4935-b11c-6c6104ced65d,6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 4-4 | 224 | BUY | STABILIZE | 30.0 | 6 | 102 | 5 | 18.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30171823501586914 | 0.0 | 0.0 | +fcd8f4bf-7e1f-42b3-a989-5b3683394c89 / -— |
| Jogador 2 | 4-4 | 225 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 100 | 5 | 18.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4057310223579407 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 226 | BUY | STABILIZE | 30.0 | 6 | 100 | 5 | 24.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017537126317620277 | 0.0 | 0.0 | +7dfeef88-7e1d-43b8-b012-017278ec61dc / -— |
| Jogador 2 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 99 | 5 | 24.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 99 | 5 | 24.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01298407930880785 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 229 | PASS | STABILIZE | 30.0 | 6 | 99 | 5 | 24.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15395309031009674 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | SELL | STABILIZE | 30.0 | 6 | 110 | 5 | 24.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -696f53ae-1413-47cc-b491-9870b7bcba51 |
| Jogador 2 | 4-5 | 233 | BUY | STABILIZE | 30.0 | 6 | 115 | 5 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8977088332176208 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 2 | 4-5 | 234 | SELL | STABILIZE | 30.0 | 6 | 112 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00787427555769682 | 0.0 | 0.0 | +— / -9cb61b5c-2c8a-43a2-a854-517f4377f6db |
| Jogador 2 | 4-5 | 235 | BUY | STABILIZE | 30.0 | 6 | 113 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8944119215011597 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -0067f61f-504d-440a-b071-de7f18886e3d,adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 4-5 | 236 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 112 | 5 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2774202525615692 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 237 | BUY | STABILIZE | 30.0 | 6 | 112 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14125773310661316 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 2 | 4-5 | 238 | BUY | STABILIZE | 30.0 | 6 | 109 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26510244607925415 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 2 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 108 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14920057356357574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 108 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498735137283802 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | SELL | ALL_IN | 18.0 | 6 | 119 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6037573218345642 | 0.0 | 0.0 | +— / -45da6d00-829e-4e2e-a1a5-318498fd007b |
| Jogador 2 | 4-6 | 243 | BUY | ALL_IN | 18.0 | 6 | 122 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4229302406311035 | 0.0 | 0.0 | +738fea60-6b44-40f1-9936-43accf852bd7 / -— |
| Jogador 2 | 4-6 | 244 | EQUIP_FROM_INVENTORY | ALL_IN | 18.0 | 6 | 121 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15978717803955078 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 245 | EQUIP_FROM_INVENTORY | ALL_IN | 18.0 | 6 | 121 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14486584067344666 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 246 | EQUIP_FROM_INVENTORY | ALL_IN | 18.0 | 6 | 121 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1627712845802307 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 247 | SELL | ALL_IN | 18.0 | 6 | 121 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 2 | 4-6 | 248 | BUY | ALL_IN | 18.0 | 6 | 122 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5260446071624756 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 2 | 4-6 | 249 | MOVE_BENCH | ALL_IN | 18.0 | 6 | 121 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09958526492118835 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 250 | MOVE_BENCH | ALL_IN | 18.0 | 6 | 121 | 5 | 20.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4149538576602936 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 252 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 132 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06821778416633606 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 253 | SELL | ALL_IN | 5.0 | 6 | 132 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09613333642482758 | 0.0 | 0.0 | +— / -fcd8f4bf-7e1f-42b3-a989-5b3683394c89 |
| Jogador 2 | 4-7 | 254 | BUY | ALL_IN | 5.0 | 6 | 134 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05545251816511154 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 2 | 4-7 | 255 | SELL | ALL_IN | 5.0 | 6 | 133 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011503411456942558 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 2 | 4-7 | 256 | BUY | ALL_IN | 5.0 | 6 | 134 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22968700528144836 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 2 | 4-7 | 257 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 132 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09957472234964371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 258 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 132 | 5 | 20.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4149528443813324 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 259 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 132 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05385972559452057 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 260 | SELL | ALL_IN | 5.0 | 6 | 132 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 |
| Jogador 2 | 5-1 | 262 | BUY | ALL_IN | 5.0 | 6 | 145 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9790099263191223 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | ALL_IN | 5.0 | 6 | 144 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06480929255485535 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | CRAFT_AND_EQUIP | ALL_IN | 5.0 | 6 | 144 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10383372008800507 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 265 | SELL | ALL_IN | 5.0 | 6 | 144 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6057551503181458 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 2 | 5-1 | 266 | BUY | ALL_IN | 5.0 | 6 | 145 | 5 | 24.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19748948514461517 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 2 | 5-1 | 267 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 141 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09991313517093658 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 268 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 141 | 5 | 20.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41495174169540405 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 269 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 141 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3089171051979065 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 270 | PASS | ALL_IN | 5.0 | 6 | 141 | 5 | 24.0 | Colosso/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6100925207138062 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15822835266590118 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0395530462265015 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179661750793457 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26999422907829285 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 48 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.707682728767395 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 1.027385950088501 | 0.0 | 0.0 | +584812e9-d314-4de0-97e2-604c5c69466c / -— |
| Jogador 3 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26494914293289185 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 61 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09426847100257874 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 67 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2633116841316223 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 68 | PASS | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3156124949455261 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 95.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 89.0 | 4 | 17 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0757607221603394 | 0.0 | 0.0 | +92450a29-eacd-4b5f-b3b5-cc8125e4918e / -584812e9-d314-4de0-97e2-604c5c69466c,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 2-4 | 83 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 16 | 1 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4220220446586609 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | BUY | STABILIZE | 89.0 | 4 | 16 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.37356147170066833 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 85 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 4 | 15 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1413296014070511 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 86 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 4 | 15 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12785394489765167 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 15 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0028414286207407713 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 15 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016107534989714622 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 89 | BUY_XP | STABILIZE | 89.0 | 4 | 15 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 90 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 11 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1446933150291443 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 89.0 | 5 | 18 | 1 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0209800004959106 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY | STABILIZE | 89.0 | 5 | 17 | 1 | 14.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27268925309181213 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 94 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 14 | 1 | 14.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0010663479333743453 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 14 | 1 | 14.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009813188575208187 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 96 | PASS | STABILIZE | 89.0 | 5 | 14 | 1 | 14.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | BUY | STABILIZE | 89.0 | 5 | 21 | 2 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368744134902954 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 103 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 20 | 2 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4401330053806305 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017116360366344452 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013769068755209446 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 106 | PASS | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020892856642603874 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 89.0 | 5 | 29 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0580337047576904 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 26 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 114 | BUY | STABILIZE | 89.0 | 5 | 26 | 2 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3219270706176758 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01305869035422802 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 117 | PASS | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021785713732242584 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 5 | 33 | 3 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2631056606769562 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 123 | BUY | STABILIZE | 89.0 | 5 | 33 | 3 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.84172523021698 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 124 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 32 | 3 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 125 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 32 | 3 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014240908436477184 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 126 | PASS | STABILIZE | 89.0 | 5 | 32 | 3 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12399999797344208 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | BUY | STABILIZE | 89.0 | 5 | 42 | 4 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8928239941596985 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -2fa86b11-4e28-4652-890e-f00a79068223,3e2ae0fa-f6ff-467f-99d8-331b49a6db63 |
| Jogador 3 | 3-2 | 133 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 41 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013275319943204522 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 134 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 41 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | PASS | STABILIZE | 89.0 | 5 | 41 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12849999964237213 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | BUY | STABILIZE | 79.0 | 5 | 50 | 5 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3108588457107544 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 3 | 3-3 | 143 | BUY | STABILIZE | 79.0 | 5 | 48 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07675463706254959 | 0.0 | 0.0 | +ffdee27e-2d30-40b5-9937-92be68ab1390 / -— |
| Jogador 3 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 46 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004136953502893448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 46 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017278834711760283 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 46 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015309040434658527 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | PASS | STABILIZE | 79.0 | 5 | 46 | 4 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13099999725818634 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | BUY | STABILIZE | 67.0 | 5 | 56 | 5 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6034716963768005 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 153 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 54 | 5 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041919462382793427 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 54 | 5 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022157246246933937 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | PASS | STABILIZE | 67.0 | 5 | 54 | 5 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15552203357219696 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | BUY | STABILIZE | 67.0 | 5 | 65 | 5 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31315261125564575 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 163 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 62 | 5 | 22.0 | Devastador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07990408688783646 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 62 | 5 | 22.0 | Devastador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016017302870750427 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 62 | 5 | 22.0 | Devastador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08337801694869995 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 166 | PASS | STABILIZE | 67.0 | 5 | 62 | 5 | 22.0 | Devastador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06109634414315224 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | SELL | STABILIZE | 57.0 | 5 | 73 | 5 | 22.0 | Devastador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44131389260292053 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-6 | 173 | BUY | STABILIZE | 57.0 | 5 | 76 | 5 | 22.0 | Devastador/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3215242922306061 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 174 | SELL | STABILIZE | 57.0 | 5 | 75 | 5 | 22.0 | Devastador/DA_18_RekSai | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8474000096321106 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-6 | 175 | BUY | STABILIZE | 57.0 | 5 | 78 | 5 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8466697335243225 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 57.0 | 5 | 77 | 5 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0043919687159359455 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | MOVE_BOARD | STABILIZE | 57.0 | 5 | 77 | 5 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01379296276718378 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 178 | MOVE_BOARD | STABILIZE | 57.0 | 5 | 77 | 5 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015309040434658527 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 57.0 | 5 | 77 | 5 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014421558938920498 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 180 | PASS | STABILIZE | 57.0 | 5 | 77 | 5 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06843539327383041 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | MOVE_BENCH | STABILIZE | 46.0 | 6 | 88 | 5 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48125696182250977 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 183 | BUY | FAST8 | 46.0 | 6 | 88 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22348538041114807 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 184 | MOVE_BOARD | FAST8 | 46.0 | 6 | 85 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00024582567857578397 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 185 | MOVE_BOARD | FAST8 | 46.0 | 6 | 85 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 186 | PASS | FAST8 | 46.0 | 6 | 85 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07385042309761047 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 46.0 | 6 | 96 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 46.0 | 6 | 96 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11018446087837219 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | SELL | FAST8 | 46.0 | 6 | 96 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 4-1 | 195 | BUY | FAST8 | 46.0 | 6 | 97 | 5 | 26.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29584744572639465 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 3 | 4-1 | 196 | MOVE_BENCH | FAST8 | 46.0 | 6 | 94 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09977252036333084 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 197 | MOVE_BOARD | FAST8 | 46.0 | 6 | 94 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 198 | MOVE_BOARD | FAST8 | 46.0 | 6 | 94 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 199 | PASS | FAST8 | 46.0 | 6 | 94 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11274565756320953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | SELL | STABILIZE | 34.0 | 6 | 106 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -cdb48eea-209d-4833-9a68-79df61990332 |
| Jogador 3 | 4-2 | 203 | BUY | STABILIZE | 34.0 | 6 | 109 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.874353289604187 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 3 | 4-2 | 204 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 107 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3993476331233978 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 205 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 107 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08178649097681046 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 206 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 107 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07097333669662476 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 207 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 107 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41420209407806396 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 208 | MOVE_BENCH | STABILIZE | 34.0 | 6 | 107 | 5 | 26.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41477617621421814 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 209 | PASS | STABILIZE | 34.0 | 6 | 107 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15212878584861755 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 212 | SELL | ALL_IN | 23.0 | 6 | 120 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5148981809616089 | 0.0 | 0.0 | +— / -f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 3 | 4-3 | 213 | BUY | ALL_IN | 23.0 | 6 | 123 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19192969799041748 | 0.0 | 0.0 | +2001a193-3868-4a3f-8a71-3a9f95c04a02 / -— |
| Jogador 3 | 4-3 | 214 | MOVE_BOARD | ALL_IN | 23.0 | 6 | 120 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 215 | MOVE_BENCH | ALL_IN | 23.0 | 6 | 120 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08439406007528305 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 216 | MOVE_BENCH | ALL_IN | 23.0 | 6 | 120 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41384801268577576 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 217 | MOVE_BOARD | ALL_IN | 23.0 | 6 | 120 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014974595978856087 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 218 | PASS | ALL_IN | 23.0 | 6 | 120 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5149715542793274 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | SELL | ALL_IN | 10.0 | 6 | 133 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04846666753292084 | 0.0 | 0.0 | +— / -2001a193-3868-4a3f-8a71-3a9f95c04a02 |
| Jogador 3 | 4-4 | 223 | BUY | ALL_IN | 10.0 | 6 | 136 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2508896291255951 | 0.0 | 0.0 | +f4173576-aa2e-4a93-94ec-ecd49d90d2b7 / -— |
| Jogador 3 | 4-4 | 224 | REROLL | ALL_IN | 10.0 | 6 | 133 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 225 | SELL | ALL_IN | 10.0 | 6 | 131 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026666666381061077 | 0.0 | 0.0 | +— / -f4173576-aa2e-4a93-94ec-ecd49d90d2b7 |
| Jogador 3 | 4-4 | 226 | BUY | ALL_IN | 10.0 | 6 | 134 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9504727721214294 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 3 | 4-4 | 227 | SELL | ALL_IN | 10.0 | 6 | 132 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6995221972465515 | 0.0 | 0.0 | +— / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9 |
| Jogador 3 | 4-4 | 228 | BUY | ALL_IN | 10.0 | 6 | 135 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4226466119289398 | 0.0 | 0.0 | +d53646ff-bb49-4f82-b761-faa4657f01cc / -— |
| Jogador 3 | 4-4 | 229 | MOVE_BOARD | ALL_IN | 10.0 | 6 | 132 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00017304120410699397 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 230 | MOVE_BOARD | ALL_IN | 10.0 | 6 | 132 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 232 | SELL | ALL_IN | 10.0 | 6 | 145 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6548555493354797 | 0.0 | 0.0 | +— / -d53646ff-bb49-4f82-b761-faa4657f01cc |
| Jogador 3 | 4-5 | 233 | BUY | ALL_IN | 10.0 | 6 | 148 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5168160200119019 | 0.0 | 0.0 | +226f36b1-cb9a-464a-a10a-3f21ebd41f24 / -— |
| Jogador 3 | 4-5 | 234 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 147 | 5 | 30.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0994444265961647 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 235 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 147 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05398311838507652 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 236 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 147 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6287981867790222 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 237 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 147 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3533794581890106 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 238 | PASS | ALL_IN | 10.0 | 6 | 147 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5747509598731995 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | SELL | ALL_IN | 10.0 | 6 | 158 | 5 | 28.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 4-6 | 243 | BUY | ALL_IN | 10.0 | 6 | 161 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0651419162750244 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce,d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 3 | 4-6 | 244 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 159 | 5 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5055716633796692 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 245 | BUY | ALL_IN | 10.0 | 6 | 159 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26110318303108215 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -— |
| Jogador 3 | 4-6 | 246 | MOVE_BOARD | ALL_IN | 10.0 | 6 | 157 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 247 | MOVE_BOARD | ALL_IN | 10.0 | 6 | 157 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014012545347213745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 248 | PASS | ALL_IN | 10.0 | 6 | 157 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5830170512199402 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16588649153709412 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 35 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4014376997947693 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0139472484588623 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 49 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3389796018600464 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 50 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0335134267807007 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 51 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017469621961936355 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 53 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012796590104699135 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 54 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0383573770523071 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 60 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21472883224487305 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 61 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17384754121303558 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.75303303473629e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 63 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11304869502782822 | 0.0 | 0.0 | +b166276e-305e-4945-8398-7c8b4b86ca9e / -— |
| Jogador 4 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10580834746360779 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 67 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24129793047904968 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03276757895946503 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 70 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0423076152801514 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793,eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-3 | 75 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0316535234451294 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 11 | 1 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.408825546503067 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | BUY | STABILIZE | 95.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11516374349594116 | 0.0 | 0.0 | +89740fc1-ac0c-4a0b-9e85-1832d5c3acc4 / -— |
| Jogador 4 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008870731107890606 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12836088240146637 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24935382604599 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 4 | 17 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3512265980243683 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 4 | 14 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2657948136329651 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 13 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009961973410099745 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 13 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1375267505645752 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | PASS | STABILIZE | 95.0 | 4 | 13 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 4 | 19 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7995291352272034 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -— |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 4 | 18 | 1 | 10.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8432802557945251 | 0.0 | 0.0 | +a72d427f-f2f7-46dd-97bf-d28999772db0 / -— |
| Jogador 4 | 2-5 | 94 | BUY | STABILIZE | 95.0 | 4 | 17 | 1 | 10.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15073619782924652 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 14 | 1 | 10.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2904774248600006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 14 | 1 | 10.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010059856809675694 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 97 | PASS | STABILIZE | 95.0 | 4 | 14 | 1 | 10.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | SELL | STABILIZE | 88.0 | 5 | 20 | 2 | 10.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-6 | 103 | BUY | STABILIZE | 88.0 | 5 | 23 | 2 | 10.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9073364734649658 | 0.0 | 0.0 | +814d07bd-0296-44af-9626-26a8a224d86f / -— |
| Jogador 4 | 2-6 | 104 | SELL | STABILIZE | 88.0 | 5 | 22 | 2 | 10.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04229411482810974 | 0.0 | 0.0 | +— / -e989a0cc-848a-4c45-b153-315877aee8f7 |
| Jogador 4 | 2-6 | 105 | BUY | STABILIZE | 88.0 | 5 | 24 | 2 | 10.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8365809321403503 | 0.0 | 0.0 | +f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 / -— |
| Jogador 4 | 2-6 | 106 | SELL | STABILIZE | 88.0 | 5 | 23 | 2 | 10.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5246666669845581 | 0.0 | 0.0 | +— / -f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 |
| Jogador 4 | 2-6 | 107 | BUY | STABILIZE | 88.0 | 5 | 24 | 2 | 10.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15315231680870056 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
| Jogador 4 | 2-6 | 108 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 22 | 2 | 10.0 | Colosso/DA_18_Camille | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3614361882209778 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 22 | 2 | 12.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3025088906288147 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 22 | 2 | 12.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009648153558373451 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 112 | BUY | STABILIZE | 88.0 | 5 | 30 | 3 | 12.0 | Colosso/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8699662089347839 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -814d07bd-0296-44af-9626-26a8a224d86f,9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-7 | 113 | BUY | STABILIZE | 88.0 | 5 | 29 | 2 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9478963017463684 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -4b07138d-44fd-4515-8b65-d7db84f4639c,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-7 | 114 | BUY | STABILIZE | 88.0 | 5 | 28 | 2 | 10.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3213120102882385 | 0.0 | 0.0 | +3d4fca52-8f58-4464-8cec-752fa99dbb3c / -— |
| Jogador 4 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 27 | 2 | 10.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9022376537322998 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 27 | 2 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003740887390449643 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 27 | 2 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014484764076769352 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 27 | 2 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499698031693697 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 119 | PASS | STABILIZE | 88.0 | 5 | 27 | 2 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022142857313156128 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 122 | BUY | STABILIZE | 88.0 | 5 | 34 | 3 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3127534091472626 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 5 | 33 | 3 | 14.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17837002873420715 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 33 | 3 | 14.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0884517952799797 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 33 | 3 | 12.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7836005091667175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 33 | 3 | 12.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038394566625356674 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 127 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 33 | 3 | 14.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08189984411001205 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 128 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 33 | 3 | 12.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.779012143611908 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 129 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 33 | 3 | 12.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0533025898039341 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 130 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 33 | 3 | 14.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0940399169921875 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 79.0 | 5 | 41 | 4 | 12.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8829719424247742 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 40 | 4 | 8.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24866269528865814 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 134 | BUY | STABILIZE | 79.0 | 5 | 40 | 4 | 14.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5884281396865845 | 0.0 | 0.0 | +3f253868-2de5-4189-95a0-705f62682958 / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 39 | 3 | 14.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5835187435150146 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | BUY | STABILIZE | 79.0 | 5 | 39 | 3 | 18.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.316490113735199 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 38 | 3 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0023461177479475737 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 38 | 3 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010446745902299881 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 139 | PASS | STABILIZE | 79.0 | 5 | 38 | 3 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 47 | 4 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.297487637610175e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 143 | SELL | STABILIZE | 67.0 | 5 | 47 | 4 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01889999955892563 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 3-3 | 144 | BUY | STABILIZE | 67.0 | 5 | 50 | 5 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26799100637435913 | 0.0 | 0.0 | +e2ed7625-f3aa-43f0-936b-7322cb9d16f1 / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.3927019608672708e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05769147723913193 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01651141047477722 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 148 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31195560097694397 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 67.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05708947032690048 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 150 | PASS | STABILIZE | 67.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03449999913573265 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | SELL | STABILIZE | 56.0 | 5 | 59 | 5 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 56.0 | 5 | 62 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8344757556915283 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 56.0 | 5 | 60 | 5 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20849807560443878 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 155 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 60 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02835085801780224 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 156 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 60 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07642927020788193 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 60 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017454562708735466 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 60 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12718768417835236 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 60 | 5 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0021400414407253265 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 60 | 5 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10459372401237488 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | SELL | STABILIZE | 56.0 | 5 | 71 | 5 | 18.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 3-5 | 163 | BUY | STABILIZE | 56.0 | 5 | 74 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9005183577537537 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,f71a7192-663d-46a0-93ef-b900c59c3bde |
| Jogador 4 | 3-5 | 164 | BUY | STABILIZE | 56.0 | 5 | 72 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32275691628456116 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 70 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010869874618947506 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 70 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1212167888879776 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 70 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01862688735127449 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 168 | MOVE_BOARD | STABILIZE | 56.0 | 5 | 70 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023981856182217598 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 169 | PASS | STABILIZE | 56.0 | 5 | 70 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16293907165527344 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | BUY | STABILIZE | 45.0 | 5 | 81 | 5 | 18.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8712957501411438 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 173 | SELL | STABILIZE | 45.0 | 5 | 80 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -40f2a32f-1ace-4700-8a79-e6b5d3212036 |
| Jogador 4 | 3-6 | 174 | BUY | STABILIZE | 45.0 | 5 | 85 | 5 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.842115581035614 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 4 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 45.0 | 5 | 83 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07645992189645767 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 45.0 | 5 | 83 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050631552934646606 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 177 | PASS | STABILIZE | 45.0 | 5 | 83 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1710468828678131 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | SELL | STABILIZE | 33.0 | 5 | 95 | 5 | 18.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4226333200931549 | 0.0 | 0.0 | +— / -3f253868-2de5-4189-95a0-705f62682958 |
| Jogador 4 | 3-7 | 183 | BUY | STABILIZE | 33.0 | 5 | 96 | 5 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9365045428276062 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2,f722cd46-0c4e-42e7-80ff-4b910c28d572 |
| Jogador 4 | 3-7 | 184 | BUY | STABILIZE | 33.0 | 5 | 94 | 5 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3433302938938141 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 4 | 3-7 | 185 | MOVE_BENCH | STABILIZE | 33.0 | 5 | 92 | 5 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7713568210601807 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 186 | BUY | STABILIZE | 33.0 | 5 | 92 | 5 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3180156648159027 | 0.0 | 0.0 | +e9d5f645-4afc-44f4-ae53-bc832c49f451 / -— |
| Jogador 4 | 3-7 | 187 | MOVE_BENCH | STABILIZE | 33.0 | 5 | 91 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5398682951927185 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 188 | MOVE_BENCH | STABILIZE | 33.0 | 5 | 91 | 5 | 16.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22372876107692719 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 33.0 | 5 | 91 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08447735756635666 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 33.0 | 5 | 91 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026353945955634117 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 33.0 | 5 | 103 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21380899846553802 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 33.0 | 5 | 103 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2474905103445053 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | SELL | STABILIZE | 33.0 | 5 | 103 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 4 | 4-1 | 195 | BUY | STABILIZE | 33.0 | 5 | 106 | 5 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9014078974723816 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 196 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 5 | 105 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1299111694097519 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 197 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 5 | 105 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12999369204044342 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 198 | SELL | STABILIZE | 33.0 | 5 | 105 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -89740fc1-ac0c-4a0b-9e85-1832d5c3acc4 |
| Jogador 4 | 4-1 | 199 | BUY | STABILIZE | 33.0 | 5 | 106 | 5 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.332084059715271 | 0.0 | 0.0 | +5637ca02-9946-4d1a-9679-e5c316ef566b / -— |
| Jogador 4 | 4-1 | 200 | MOVE_BENCH | STABILIZE | 33.0 | 5 | 105 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18696235120296478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 118 | 5 | 22.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1002761647105217 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 203 | BUY | ALL_IN | 21.0 | 6 | 118 | 5 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7604575753211975 | 0.0 | 0.0 | +cb216a0d-8bff-41f9-99bd-231ca5186fb5 / -— |
| Jogador 4 | 4-2 | 204 | SELL | ALL_IN | 21.0 | 6 | 117 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5600029826164246 | 0.0 | 0.0 | +— / -e9d5f645-4afc-44f4-ae53-bc832c49f451 |
| Jogador 4 | 4-2 | 205 | BUY | ALL_IN | 21.0 | 6 | 118 | 5 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3924703299999237 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 4 | 4-2 | 206 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 115 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00040879807784222066 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 207 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 115 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014290738850831985 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 208 | PASS | ALL_IN | 21.0 | 6 | 115 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5144945383071899 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 212 | SELL | ALL_IN | 21.0 | 6 | 126 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6837999820709229 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 4-3 | 213 | BUY | ALL_IN | 21.0 | 6 | 128 | 5 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16736716032028198 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 4 | 4-3 | 214 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 125 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001108399941585958 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 215 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 125 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6102193593978882 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 216 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 125 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35341358184814453 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 217 | PASS | ALL_IN | 21.0 | 6 | 125 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.526321530342102 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 222 | SELL | ALL_IN | 21.0 | 6 | 137 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05346880480647087 | 0.0 | 0.0 | +— / -7b3e8122-3b51-46b5-94a8-68fb77156e0e |
| Jogador 4 | 4-4 | 223 | BUY | ALL_IN | 21.0 | 6 | 140 | 5 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006440436467528343 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 4 | 4-4 | 224 | SELL | ALL_IN | 21.0 | 6 | 138 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015231537632644176 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 4 | 4-4 | 225 | BUY | ALL_IN | 21.0 | 6 | 140 | 5 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006795457098633051 | 0.0 | 0.0 | +b5b3098f-d48c-42b8-8022-639a25225980 / -— |
| Jogador 4 | 4-4 | 226 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 138 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010010786354541779 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 227 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 138 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025857746601104736 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 228 | PASS | ALL_IN | 21.0 | 6 | 138 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.536828339099884 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | SELL | ALL_IN | 21.0 | 6 | 149 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015154046006500721 | 0.0 | 0.0 | +— / -b5b3098f-d48c-42b8-8022-639a25225980 |
| Jogador 4 | 4-5 | 233 | BUY | ALL_IN | 21.0 | 6 | 151 | 5 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007080922834575176 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 4 | 4-5 | 234 | MOVE_BOARD | ALL_IN | 21.0 | 6 | 149 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 235 | MOVE_BENCH | ALL_IN | 21.0 | 6 | 149 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36229392886161804 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 236 | PASS | ALL_IN | 21.0 | 6 | 149 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5458420515060425 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 242 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 159 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.614956259727478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 243 | SELL | ALL_IN | 10.0 | 6 | 159 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029887616634368896 | 0.0 | 0.0 | +— / -f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 4 | 4-6 | 244 | BUY | ALL_IN | 10.0 | 6 | 161 | 5 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10567150264978409 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 4 | 4-6 | 245 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 158 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10573136061429977 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 246 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 158 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3699217140674591 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 247 | MOVE_BENCH | ALL_IN | 10.0 | 6 | 158 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36873748898506165 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 248 | PASS | ALL_IN | 10.0 | 6 | 158 | 5 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5838479995727539 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5658670663833618 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17659981548786163 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18749907612800598 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4052088260650635 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32031217217445374 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06292524188756943 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 50 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2745124399662018 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 51 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007072990760207176 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18646866083145142 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 53 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9747360348701477 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.44816330075263977 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 61 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24081367254257202 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20127682387828827 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 63 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17037545144557953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 64 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17408205568790436 | 0.0 | 0.0 | +— / -634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-1 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04545314982533455 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 67 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3420252203941345 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 68 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3140122592449188 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 69 | SELL | STABILIZE | 95.0 | 4 | 2 | 0 | 12.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14293475449085236 | 0.0 | 0.0 | +— / -341df1a1-a619-420a-926a-0fe048aa1456 |
| Jogador 5 | 2-2 | 70 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5674451589584351 | 0.0 | 0.0 | +— / -02c39b42-90d5-4e01-9380-460b6c1cb993 |
| Jogador 5 | 2-2 | 71 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27071189880371094 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 5 | 2-2 | 72 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3324045240879059 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2903759181499481 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16964305937290192 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09966666996479034 | 0.0 | 0.0 | +— / -5627d898-cff3-4664-87d1-40a8f3656ab3 |
| Jogador 5 | 2-3 | 78 | SELL | STABILIZE | 95.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4462481439113617 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14779317378997803 | 0.0 | 0.0 | +— / -eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36793532967567444 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32251158356666565 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07496564090251923 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11321808397769928 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019212180748581886 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 89 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24370475113391876 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 90 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3518907427787781 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3173177242279053 | 0.0 | 0.0 | +28f66ef1-93d6-4cc8-a0c9-e84e844dee28 / -— |
| Jogador 5 | 2-5 | 94 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21346282958984375 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 95 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11723997443914413 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 97 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1467452496290207 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10363718867301941 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4004324674606323 | 0.0 | 0.0 | +— / -28f66ef1-93d6-4cc8-a0c9-e84e844dee28 |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08464623242616653 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04862471669912338 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 104 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36766666173934937 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 6 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 107 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 108 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4025860130786896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 109 | BUY | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0349222756922245 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 24.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002196110785007477 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 24.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.979061484336853 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.045611023902893 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -7098795b-11bf-4b73-837a-87f5d8aece4c,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24953116476535797 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00040914598503150046 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497098058462143 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 117 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 20.0 | Florescer/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 2-7 | 118 | SELL | STABILIZE | 95.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -46838f8d-8037-485c-8c34-9639f14ada19 |
| Jogador 5 | 2-7 | 119 | BUY_XP | STABILIZE | 95.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 120 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7987250089645386 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 123 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2850777804851532 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -— |
| Jogador 5 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2086942493915558 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 125 | BUY | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24185478687286377 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-1 | 126 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 20.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14305421710014343 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 3-1 | 127 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 20.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5173949003219604 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 128 | MOVE_BOARD | FAST8 | 95.0 | 6 | 1 | 0 | 26.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015019714832305908 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 129 | MOVE_BOARD | FAST8 | 95.0 | 6 | 1 | 0 | 26.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014980848878622055 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 130 | PASS | FAST8 | 95.0 | 6 | 1 | 0 | 26.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 132 | BUY | FAST8 | 95.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7351174354553223 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 133 | BUY | FAST8 | 95.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20200715959072113 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 134 | MOVE_BOARD | FAST8 | 95.0 | 6 | 4 | 0 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005438548978418112 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 135 | MOVE_BOARD | FAST8 | 95.0 | 6 | 4 | 0 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026052886620163918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 136 | PASS | FAST8 | 95.0 | 6 | 4 | 0 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 142 | BUY | FAST8 | 95.0 | 6 | 13 | 1 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7656329870223999 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0,ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-3 | 143 | BUY | FAST8 | 95.0 | 6 | 11 | 1 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13133801519870758 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 144 | BUY | FAST8 | 95.0 | 6 | 7 | 0 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21191616356372833 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 145 | BUY_XP | FAST8 | 95.0 | 6 | 4 | 0 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 146 | MOVE_BOARD | FAST8 | 95.0 | 6 | 0 | 0 | 26.0 | Florescer/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 147 | MOVE_BOARD | FAST8 | 95.0 | 6 | 0 | 0 | 26.0 | Florescer/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16032955050468445 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 148 | PASS | FAST8 | 95.0 | 6 | 0 | 0 | 26.0 | Florescer/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | BUY | FAST8 | 95.0 | 6 | 9 | 0 | 26.0 | Florescer/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7378309369087219 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 153 | SELL | FAST8 | 95.0 | 6 | 8 | 0 | 26.0 | Florescer/DA_18_Yunara | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 3-4 | 154 | BUY | FAST8 | 95.0 | 6 | 13 | 1 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7679336071014404 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -2e4ab22c-62d7-425c-9528-2e1315655c24,6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 3-4 | 155 | BUY_XP | FAST8 | 95.0 | 6 | 12 | 1 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 156 | BUY_XP | FAST8 | 95.0 | 6 | 8 | 0 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 157 | BUY_XP | FAST8 | 95.0 | 6 | 4 | 0 | 26.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08229999989271164 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 158 | MOVE_BENCH | FAST8 | 95.0 | 7 | 0 | 0 | 26.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4061250388622284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 159 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04341353848576546 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 160 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 162 | BUY | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0848502516746521 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 163 | BUY | FAST8 | 95.0 | 7 | 5 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2392103224992752 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 164 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050754282623529434 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 165 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 166 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004934643511660397 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 167 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014695233665406704 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 168 | MOVE_BOARD | FAST8 | 95.0 | 7 | 1 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014931519515812397 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 169 | PASS | FAST8 | 95.0 | 7 | 1 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 172 | BUY | FAST8 | 95.0 | 7 | 10 | 1 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6383078098297119 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 173 | MOVE_BOARD | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 174 | MOVE_BOARD | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015033705160021782 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 175 | PASS | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 182 | SELL | FAST8 | 95.0 | 7 | 17 | 1 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-7 | 183 | BUY | FAST8 | 95.0 | 7 | 20 | 2 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6942521929740906 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -b0190388-bc3b-43af-b782-94490de9d8b1,bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-7 | 184 | BUY | FAST8 | 95.0 | 7 | 18 | 1 | 32.0 | Florescer/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3472984731197357 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 185 | BUY_XP | FAST8 | 95.0 | 7 | 15 | 1 | 32.0 | Florescer/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 186 | BUY_XP | FAST8 | 95.0 | 7 | 11 | 1 | 32.0 | Florescer/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 187 | BUY_XP | FAST8 | 95.0 | 7 | 7 | 0 | 32.0 | Florescer/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 188 | BUY | FAST8 | 95.0 | 7 | 3 | 0 | 32.0 | Florescer/DA_18_LeBlanc | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04509267210960388 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 189 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Florescer/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 190 | MOVE_BOARD | FAST8 | 95.0 | 7 | 0 | 0 | 32.0 | Florescer/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0149806784465909 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1315789371728897 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1366077959537506 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 194 | MOVE_BOARD | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0416378245281521e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 195 | MOVE_BOARD | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015019568614661694 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 196 | PASS | FAST8 | 95.0 | 7 | 8 | 0 | 32.0 | Florescer/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 202 | SELL | FAST8 | 95.0 | 7 | 17 | 1 | 32.0 | Florescer/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 5 | 4-2 | 203 | BUY | FAST8 | 95.0 | 7 | 22 | 2 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6695456504821777 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 5 | 4-2 | 204 | MOVE_BOARD | FAST8 | 95.0 | 7 | 19 | 1 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.946682328314637e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 205 | MOVE_BOARD | FAST8 | 95.0 | 7 | 19 | 1 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 206 | MOVE_BOARD | FAST8 | 95.0 | 7 | 19 | 1 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499695610255003 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 207 | PASS | FAST8 | 95.0 | 7 | 19 | 1 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027857143431901932 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 212 | SELL | FAST8 | 95.0 | 7 | 30 | 3 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 4-3 | 213 | BUY | FAST8 | 95.0 | 7 | 33 | 3 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.764691948890686 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 5 | 4-3 | 214 | SELL | FAST8 | 95.0 | 7 | 30 | 3 | 32.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025566667318344116 | 0.0 | 0.0 | +— / -4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 5 | 4-3 | 215 | BUY | FAST8 | 95.0 | 7 | 33 | 3 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8233722448348999 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -68cd8ae3-399f-461f-89a8-189d7b0a6b59,dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 4-3 | 216 | BUY | FAST8 | 95.0 | 7 | 30 | 3 | 26.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6285563707351685 | 0.0 | 0.0 | +16acc555-c819-4f7c-b406-2f48f11ffc87 / -— |
| Jogador 5 | 4-3 | 217 | MOVE_BENCH | FAST8 | 95.0 | 7 | 28 | 2 | 26.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5977042317390442 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 218 | MOVE_BOARD | FAST8 | 95.0 | 7 | 28 | 2 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01494823582470417 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 219 | MOVE_BOARD | FAST8 | 95.0 | 7 | 28 | 2 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999369159340858 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 220 | PASS | FAST8 | 95.0 | 7 | 28 | 2 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11428571492433548 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 222 | BUY | FAST8 | 95.0 | 7 | 39 | 3 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2637603282928467 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 5 | 4-4 | 223 | MOVE_BOARD | FAST8 | 95.0 | 7 | 36 | 3 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.2319896086410154e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 224 | MOVE_BOARD | FAST8 | 95.0 | 7 | 36 | 3 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 225 | PASS | FAST8 | 95.0 | 7 | 36 | 3 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | SELL | FAST8 | 95.0 | 7 | 47 | 4 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10383333265781403 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 4-5 | 233 | BUY | FAST8 | 95.0 | 7 | 51 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7027495503425598 | 0.0 | 0.0 | +652568b9-7093-4e77-8b9c-7ed286cf7f4c / -— |
| Jogador 5 | 4-5 | 234 | MOVE_BOARD | FAST8 | 95.0 | 7 | 50 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.037555297349172e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 235 | MOVE_BOARD | FAST8 | 95.0 | 7 | 50 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014998959377408028 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 236 | PASS | FAST8 | 95.0 | 7 | 50 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 242 | MOVE_BOARD | FAST8 | 95.0 | 7 | 64 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.16412848001346e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 243 | MOVE_BOARD | FAST8 | 95.0 | 7 | 64 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000398270785809 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 244 | MOVE_BOARD | FAST8 | 95.0 | 7 | 64 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500011421740055 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 245 | PASS | FAST8 | 95.0 | 7 | 64 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08862585574388504 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 252 | SELL | FAST8 | 95.0 | 7 | 78 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 4-7 | 253 | BUY | FAST8 | 95.0 | 7 | 81 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8861191272735596 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -16acc555-c819-4f7c-b406-2f48f11ffc87,1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 4-7 | 254 | MOVE_BENCH | FAST8 | 95.0 | 7 | 79 | 5 | 34.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5973241925239563 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 255 | BUY | FAST8 | 95.0 | 7 | 79 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03520768880844116 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 5 | 4-7 | 256 | MOVE_BOARD | FAST8 | 95.0 | 7 | 78 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012342140544205904 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 257 | MOVE_BOARD | FAST8 | 95.0 | 7 | 78 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014008989557623863 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 258 | PASS | FAST8 | 95.0 | 7 | 78 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23848992586135864 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 262 | BUY | FAST8 | 95.0 | 7 | 91 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6944865584373474 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -— |
| Jogador 5 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 95.0 | 7 | 90 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17766302824020386 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 264 | CRAFT_AND_EQUIP | FAST8 | 95.0 | 7 | 90 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18822503089904785 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 265 | SELL | FAST8 | 95.0 | 7 | 90 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -755060be-13bb-4686-9ee9-e53fef2d75b2 |
| Jogador 5 | 5-1 | 266 | BUY | FAST8 | 95.0 | 7 | 95 | 5 | 40.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9479475617408752 | 0.0 | 0.0 | +811fcf1f-2023-4c36-a961-d61cb0dd68d0 / -0debca82-3a2a-44ba-af48-83211d5e5243,e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 5-1 | 267 | MOVE_BENCH | FAST8 | 95.0 | 7 | 92 | 5 | 28.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15118205547332764 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 268 | BUY | FAST8 | 95.0 | 7 | 92 | 5 | 30.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014751329086720943 | 0.0 | 0.0 | +0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c / -— |
| Jogador 5 | 5-1 | 269 | MOVE_BOARD | FAST8 | 95.0 | 7 | 88 | 5 | 30.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0024706441909074783 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 270 | MOVE_BOARD | FAST8 | 95.0 | 7 | 88 | 5 | 30.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497559528797865 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 272 | SELL | FAST8 | 82.0 | 7 | 98 | 5 | 30.0 | Florescer/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.507822573184967 | 0.0 | 0.0 | +— / -811fcf1f-2023-4c36-a961-d61cb0dd68d0 |
| Jogador 5 | 5-2 | 273 | BUY | FAST8 | 82.0 | 7 | 106 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.13830821216106415 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 5 | 5-2 | 274 | EQUIP_FROM_INVENTORY | FAST8 | 82.0 | 7 | 103 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09079229086637497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 275 | EQUIP_FROM_INVENTORY | FAST8 | 82.0 | 7 | 103 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12822942435741425 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 276 | EQUIP_FROM_INVENTORY | FAST8 | 82.0 | 7 | 103 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10375242680311203 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 277 | BUY_XP | FAST8 | 82.0 | 7 | 103 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 278 | MOVE_BOARD | FAST8 | 82.0 | 7 | 99 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.9140799849992618e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 279 | MOVE_BOARD | FAST8 | 82.0 | 7 | 99 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029750347137451172 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 280 | BUY_XP | FAST8 | 82.0 | 7 | 99 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 282 | SELL | FAST8 | 82.0 | 7 | 106 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -9af900db-c181-448a-9736-30f08f062a00 |
| Jogador 5 | 5-3 | 283 | BUY | FAST8 | 82.0 | 7 | 109 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3190940320491791 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 5 | 5-3 | 284 | SELL | FAST8 | 82.0 | 7 | 106 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38929998874664307 | 0.0 | 0.0 | +— / -652568b9-7093-4e77-8b9c-7ed286cf7f4c |
| Jogador 5 | 5-3 | 285 | BUY | FAST8 | 82.0 | 7 | 107 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2798883020877838 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -— |
| Jogador 5 | 5-3 | 286 | BUY_XP | FAST8 | 82.0 | 7 | 104 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05511999875307083 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 287 | BUY_XP | FAST8 | 82.0 | 7 | 100 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47494998574256897 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 288 | MOVE_BENCH | STABILIZE | 82.0 | 8 | 96 | 5 | 30.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23579716682434082 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 289 | BUY | ECON | 82.0 | 8 | 96 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16895799338817596 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 5 | 5-3 | 290 | MOVE_BOARD | ECON | 82.0 | 8 | 93 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.000290299067273736 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 292 | SELL | ECON | 82.0 | 8 | 105 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 5-4 | 293 | BUY | ECON | 82.0 | 8 | 106 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8730146288871765 | 0.0 | 0.0 | +33e9808b-2f92-49e7-ac35-1f6f9388edef / -— |
| Jogador 5 | 5-4 | 294 | MOVE_BOARD | ECON | 82.0 | 8 | 103 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 295 | MOVE_BOARD | ECON | 82.0 | 8 | 103 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015860499814152718 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 296 | PASS | ECON | 82.0 | 8 | 103 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12903527915477753 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 300 | MOVE_BENCH | ECON | 82.0 | 8 | 103 | 5 | 38.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4686644971370697 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 302 | BUY | ECON | 82.0 | 8 | 114 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8903125524520874 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 5 | 5-5 | 303 | MOVE_BOARD | ECON | 82.0 | 8 | 110 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009279471705667675 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 304 | MOVE_BOARD | ECON | 82.0 | 8 | 110 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013891145586967468 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 305 | PASS | ECON | 82.0 | 8 | 110 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13503490388393402 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 312 | SELL | WINSTREAK | 82.0 | 8 | 122 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 5 | 5-6 | 313 | BUY | WINSTREAK | 82.0 | 8 | 125 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0027282238006592 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -33e9808b-2f92-49e7-ac35-1f6f9388edef,e9bb05f6-3838-423a-bfd2-3791379b479e |
| Jogador 5 | 5-6 | 314 | BUY | WINSTREAK | 82.0 | 8 | 122 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14811468124389648 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 5 | 5-6 | 315 | MOVE_BOARD | WINSTREAK | 82.0 | 8 | 121 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.263458777131746e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 316 | MOVE_BOARD | WINSTREAK | 82.0 | 8 | 121 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01493906881660223 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 317 | MOVE_BOARD | WINSTREAK | 82.0 | 8 | 121 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 318 | PASS | WINSTREAK | 82.0 | 8 | 121 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.298602819442749 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 322 | BUY | WINSTREAK | 82.0 | 8 | 133 | 5 | 44.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.004231572151184 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c,f2dbe099-e518-4261-b120-9f327b112dcb |
| Jogador 5 | 5-7 | 323 | BUY | WINSTREAK | 82.0 | 8 | 129 | 5 | 36.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9790751934051514 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -0d693604-37ed-4f64-9a87-ded68f8a2dea,68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 5-7 | 324 | BUY | STABILIZE | 82.0 | 8 | 126 | 5 | 30.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24012012779712677 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 5 | 5-7 | 325 | MOVE_BENCH | STABILIZE | 82.0 | 8 | 123 | 5 | 30.0 | Florescer/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31881725788116455 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 326 | MOVE_BOARD | WINSTREAK | 82.0 | 8 | 123 | 5 | 42.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016424894332885742 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 327 | MOVE_BOARD | WINSTREAK | 82.0 | 8 | 123 | 5 | 42.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014096391387283802 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 328 | PASS | WINSTREAK | 82.0 | 8 | 123 | 5 | 42.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30035915970802307 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 330 | MOVE_BENCH | WINSTREAK | 82.0 | 8 | 123 | 5 | 42.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4280913472175598 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 332 | BUY | WINSTREAK | 82.0 | 8 | 134 | 5 | 54.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3662039041519165 | 0.0 | 0.0 | +e4cdd5ad-44bd-4dc3-875d-4606ef0ad140 / -— |
| Jogador 5 | 6-1 | 333 | EQUIP_FROM_INVENTORY | WINSTREAK | 82.0 | 8 | 129 | 5 | 54.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13206958770751953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 334 | BUY | WINSTREAK | 82.0 | 8 | 129 | 5 | 54.0 | Florescer/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37768328189849854 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 5 | 6-1 | 335 | MOVE_BOARD | WINSTREAK | 82.0 | 8 | 128 | 5 | 54.0 | Florescer/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004263987357262522 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 336 | MOVE_BOARD | WINSTREAK | 82.0 | 8 | 128 | 5 | 54.0 | Florescer/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014542464166879654 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 337 | PASS | WINSTREAK | 82.0 | 8 | 128 | 5 | 54.0 | Florescer/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16447728872299194 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9946255087852478 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3207568824291229 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011186919175088406 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 35 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5352335572242737 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0199745893478394 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 49 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2857540547847748 | 0.0 | 0.0 | +72aa8420-8dc2-4e9b-a10a-bd2a36f26656 / -— |
| Jogador 6 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14690238237380981 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 51 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0236717462539673 | 0.0 | 0.0 | +97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 / -— |
| Jogador 6 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.290481299161911 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 61 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.965688169002533 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22131632268428802 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 63 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20946940779685974 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4026159346103668 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011628403328359127 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 67 | BUY | STABILIZE | 94.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14317545294761658 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 68 | BUY_XP | STABILIZE | 94.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1532365381717682 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21210390329360962 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 71 | PASS | STABILIZE | 94.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 74 | BUY | STABILIZE | 94.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.278158038854599 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 75 | SELL | STABILIZE | 94.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15042588114738464 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-3 | 76 | SELL | STABILIZE | 94.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5428675413131714 | 0.0 | 0.0 | +— / -3ad41699-a484-4178-be10-d8f72dfd1f35 |
| Jogador 6 | 2-3 | 77 | SELL | STABILIZE | 94.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48762133717536926 | 0.0 | 0.0 | +— / -72aa8420-8dc2-4e9b-a10a-bd2a36f26656 |
| Jogador 6 | 2-3 | 78 | BUY_XP | STABILIZE | 94.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0533050000667572 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 79 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6254048347473145 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 80 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28403496742248535 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 94.0 | 5 | 11 | 1 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1132804155349731 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -185ee377-0917-4209-905b-9486d5be0193,646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 94.0 | 5 | 10 | 1 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9090096354484558 | 0.0 | 0.0 | +77d51a33-bfc7-4b8b-b460-8a4a45391474 / -— |
| Jogador 6 | 2-4 | 84 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3996424674987793 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10269740968942642 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3030000329017639 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017231842502951622 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01567441038787365 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | PASS | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 94.0 | 5 | 14 | 1 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.04776132106781 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -425b1e77-5887-40b3-875e-c1f60dc6c513,908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-5 | 93 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 13 | 1 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5668300986289978 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 94 | BUY | STABILIZE | 94.0 | 5 | 13 | 1 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27976763248443604 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -— |
| Jogador 6 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 11 | 1 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14075548946857452 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 96 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03420725092291832 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 97 | PASS | STABILIZE | 94.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 89.0 | 5 | 17 | 1 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31193894147872925 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 14 | 1 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06683725118637085 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 104 | BUY | STABILIZE | 89.0 | 5 | 14 | 1 | 16.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32057616114616394 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 11 | 1 | 16.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39888978004455566 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 11 | 1 | 16.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3333064019680023 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 11 | 1 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03452460095286369 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 108 | BUY_XP | STABILIZE | 89.0 | 5 | 11 | 1 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 109 | BUY_XP | STABILIZE | 89.0 | 5 | 7 | 0 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 3 | 0 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3031439185142517 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 84.0 | 5 | 9 | 0 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8959567546844482 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 84.0 | 5 | 6 | 0 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.941533625125885 | 0.0 | 0.0 | +a2f987f8-01d6-4463-9ab4-f96c9b6f067b / -77d51a33-bfc7-4b8b-b460-8a4a45391474,97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 |
| Jogador 6 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 5 | 0 | 18.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.625024676322937 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 5 | 0 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06100841984152794 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 116 | SELL | STABILIZE | 84.0 | 5 | 5 | 0 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.501815915107727 | 0.0 | 0.0 | +— / -a2f987f8-01d6-4463-9ab4-f96c9b6f067b |
| Jogador 6 | 2-7 | 117 | SELL | STABILIZE | 84.0 | 5 | 8 | 0 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490000247955322 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-7 | 118 | EQUIP_FROM_INVENTORY | STABILIZE | 84.0 | 5 | 11 | 1 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.03076396882534027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 119 | EQUIP_FROM_INVENTORY | STABILIZE | 84.0 | 5 | 11 | 1 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09039448946714401 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 120 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24799838662147522 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 84.0 | 6 | 14 | 1 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.27718058228492737 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 11 | 1 | 22.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4031924307346344 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | CRAFT_AND_EQUIP | FAST8 | 84.0 | 6 | 11 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17516982555389404 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 125 | MOVE_BOARD | FAST8 | 84.0 | 6 | 11 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 126 | MOVE_BOARD | FAST8 | 84.0 | 6 | 11 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015133615583181381 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 127 | PASS | FAST8 | 84.0 | 6 | 11 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 132 | BUY | FAST8 | 84.0 | 6 | 18 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7379919290542603 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -— |
| Jogador 6 | 3-2 | 133 | MOVE_BOARD | FAST8 | 84.0 | 6 | 17 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05897911265492439 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 134 | MOVE_BOARD | FAST8 | 84.0 | 6 | 17 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04414128512144089 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 135 | MOVE_BOARD | FAST8 | 84.0 | 6 | 17 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015068897046148777 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 136 | BUY | FAST8 | 84.0 | 6 | 17 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7196966409683228 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -— |
| Jogador 6 | 3-2 | 137 | MOVE_BOARD | FAST8 | 84.0 | 6 | 16 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002262821653857827 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | MOVE_BOARD | FAST8 | 84.0 | 6 | 16 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 139 | PASS | FAST8 | 84.0 | 6 | 16 | 1 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05649999901652336 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | FAST8 | 84.0 | 6 | 24 | 2 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7346630692481995 | 0.0 | 0.0 | +952adeb2-fe24-47af-9748-5131b91dcc06 / -— |
| Jogador 6 | 3-3 | 143 | BUY | FAST8 | 84.0 | 6 | 22 | 2 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6418890953063965 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 144 | MOVE_BOARD | FAST8 | 84.0 | 6 | 19 | 1 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0051932488568127155 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 145 | MOVE_BOARD | FAST8 | 84.0 | 6 | 19 | 1 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13420619070529938 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | PASS | FAST8 | 84.0 | 6 | 19 | 1 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | SELL | FAST8 | 74.0 | 6 | 25 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5229555368423462 | 0.0 | 0.0 | +— / -a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 3-4 | 153 | BUY | FAST8 | 74.0 | 6 | 28 | 2 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7127523422241211 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 154 | SELL | FAST8 | 74.0 | 6 | 25 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9779999852180481 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-4 | 155 | BUY | FAST8 | 74.0 | 6 | 26 | 2 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21272841095924377 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 156 | MOVE_BENCH | FAST8 | 74.0 | 6 | 22 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.270010769367218 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 157 | MOVE_BENCH | FAST8 | 74.0 | 6 | 22 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0669073611497879 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 158 | MOVE_BENCH | FAST8 | 74.0 | 6 | 22 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 159 | MOVE_BENCH | FAST8 | 74.0 | 6 | 22 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4068278968334198 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 160 | PASS | FAST8 | 74.0 | 6 | 22 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | SELL | FAST8 | 74.0 | 6 | 29 | 2 | 28.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5080000162124634 | 0.0 | 0.0 | +— / -53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-5 | 163 | BUY | FAST8 | 74.0 | 6 | 30 | 3 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7085610628128052 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -2938180d-94e5-4bb7-832e-baa51f820ba2,50f9a30c-27db-4ed0-804e-548f87950b17 |
| Jogador 6 | 3-5 | 164 | MOVE_BENCH | FAST8 | 74.0 | 6 | 27 | 2 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07946896553039551 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BENCH | FAST8 | 74.0 | 6 | 27 | 2 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | MOVE_BENCH | FAST8 | 74.0 | 6 | 27 | 2 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23205377161502838 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 167 | PASS | FAST8 | 74.0 | 6 | 27 | 2 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0794999971985817 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | BUY | FAST8 | 62.0 | 6 | 35 | 3 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03297757729887962 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 173 | MOVE_BENCH | FAST8 | 62.0 | 6 | 32 | 3 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08001130819320679 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 174 | MOVE_BENCH | FAST8 | 62.0 | 6 | 32 | 3 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 175 | MOVE_BENCH | FAST8 | 62.0 | 6 | 32 | 3 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4065457582473755 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 176 | PASS | FAST8 | 62.0 | 6 | 32 | 3 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12399999797344208 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | BUY | FAST8 | 62.0 | 6 | 41 | 4 | 28.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.683567464351654 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 183 | SELL | FAST8 | 62.0 | 6 | 38 | 3 | 28.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -06db3a99-d008-406a-ac86-30884335d7c2 |
| Jogador 6 | 3-7 | 184 | BUY | FAST8 | 62.0 | 6 | 46 | 4 | 28.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8071324229240417 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -2ef60eed-d073-41a6-adec-4466c673b313,952adeb2-fe24-47af-9748-5131b91dcc06 |
| Jogador 6 | 3-7 | 185 | MOVE_BENCH | FAST8 | 62.0 | 6 | 44 | 4 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08534371852874756 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 186 | MOVE_BENCH | FAST8 | 62.0 | 6 | 44 | 4 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 187 | PASS | FAST8 | 62.0 | 6 | 44 | 4 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12999999523162842 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 62.0 | 6 | 53 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17554940283298492 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 62.0 | 6 | 53 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19950823485851288 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | BUY | FAST8 | 62.0 | 6 | 53 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25904780626296997 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 195 | MOVE_BENCH | FAST8 | 62.0 | 6 | 50 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22071298956871033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 196 | MOVE_BENCH | FAST8 | 62.0 | 6 | 50 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0814606249332428 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 197 | MOVE_BENCH | FAST8 | 62.0 | 6 | 50 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 198 | MOVE_BENCH | FAST8 | 62.0 | 6 | 50 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41423025727272034 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 199 | PASS | FAST8 | 62.0 | 6 | 50 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2199999988079071 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 202 | BUY | FAST8 | 62.0 | 6 | 62 | 5 | 28.0 | Feérico/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8936879634857178 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -43da0d73-facd-488b-b856-94e9496a97f9,665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 6 | 4-2 | 203 | MOVE_BENCH | FAST8 | 62.0 | 6 | 59 | 5 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0934564620256424 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 204 | BUY | FAST8 | 62.0 | 6 | 59 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08323746174573898 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 6 | 4-2 | 205 | MOVE_BENCH | FAST8 | 62.0 | 6 | 56 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.704785943031311 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 206 | MOVE_BENCH | FAST8 | 62.0 | 6 | 56 | 5 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07106216251850128 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 207 | BUY | FAST8 | 62.0 | 6 | 56 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5722282528877258 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -— |
| Jogador 6 | 4-2 | 208 | MOVE_BOARD | FAST8 | 62.0 | 6 | 53 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.848071057494963e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 209 | MOVE_BOARD | FAST8 | 62.0 | 6 | 53 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016441980376839638 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 210 | PASS | FAST8 | 62.0 | 6 | 53 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08158450573682785 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | SELL | FAST8 | 50.0 | 6 | 63 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -89cec488-9a0e-4838-b486-2504a0742476 |
| Jogador 6 | 4-3 | 213 | BUY | FAST8 | 50.0 | 6 | 68 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18110458552837372 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 6 | 4-3 | 214 | BUY_XP | FAST8 | 50.0 | 6 | 67 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055743999779224396 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 215 | BUY_XP | FAST8 | 50.0 | 6 | 63 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055743999779224396 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 216 | MOVE_BOARD | FAST8 | 50.0 | 6 | 59 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 217 | MOVE_BOARD | FAST8 | 50.0 | 6 | 59 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 218 | PASS | FAST8 | 50.0 | 6 | 59 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08530551940202713 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | SELL | FAST8 | 50.0 | 6 | 70 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 6 | 4-4 | 223 | BUY | FAST8 | 50.0 | 6 | 78 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7100703120231628 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 6 | 4-4 | 224 | SELL | FAST8 | 50.0 | 6 | 75 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-4 | 225 | BUY | FAST8 | 50.0 | 6 | 78 | 5 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3412952721118927 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 6 | 4-4 | 226 | MOVE_BOARD | FAST8 | 50.0 | 6 | 77 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00029302327311597764 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 227 | BUY_XP | FAST8 | 50.0 | 6 | 77 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055743999779224396 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 228 | BUY_XP | FAST8 | 50.0 | 6 | 73 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5476250052452087 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | MOVE_BENCH | FAST8 | 50.0 | 7 | 69 | 5 | 30.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4010137617588043 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 230 | MOVE_BOARD | FAST8 | 50.0 | 7 | 69 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995588921010494 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | BUY | FAST8 | 50.0 | 7 | 79 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2607194185256958 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 6 | 4-5 | 233 | MOVE_BOARD | FAST8 | 50.0 | 7 | 77 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.998927660286427e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 234 | MOVE_BOARD | FAST8 | 50.0 | 7 | 77 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014875741675496101 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 235 | PASS | FAST8 | 50.0 | 7 | 77 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09776484221220016 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | STABILIZE | 38.0 | 7 | 87 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47228413820266724 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 4-6 | 243 | BUY | STABILIZE | 38.0 | 7 | 88 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9067420959472656 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 6 | 4-6 | 244 | BUY_XP | STABILIZE | 38.0 | 7 | 84 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 245 | BUY_XP | STABILIZE | 38.0 | 7 | 80 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 246 | BUY_XP | STABILIZE | 38.0 | 7 | 76 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 247 | BUY_XP | STABILIZE | 38.0 | 7 | 72 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 248 | BUY_XP | STABILIZE | 38.0 | 7 | 68 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 249 | BUY_XP | STABILIZE | 38.0 | 7 | 64 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 250 | BUY_XP | STABILIZE | 38.0 | 7 | 60 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 252 | SELL | STABILIZE | 38.0 | 7 | 67 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06617556512355804 | 0.0 | 0.0 | +— / -a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 6 | 4-7 | 253 | BUY | STABILIZE | 38.0 | 7 | 68 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9636999368667603 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede,fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 4-7 | 254 | BUY | STABILIZE | 38.0 | 7 | 65 | 5 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9526414275169373 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -b755a0c5-f515-4f95-8f58-1e05f40ad302,f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-7 | 255 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 62 | 5 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5193724632263184 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 256 | BUY | STABILIZE | 38.0 | 7 | 62 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3994404375553131 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 6 | 4-7 | 257 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 59 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 59 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003579668700695 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 259 | PASS | STABILIZE | 38.0 | 7 | 59 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09918996691703796 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | BUY | STABILIZE | 38.0 | 7 | 69 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15455348789691925 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -— |
| Jogador 6 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 66 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1151728481054306 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 66 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.060658060014247894 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 265 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 66 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.873261685948819e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 266 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 66 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 267 | PASS | STABILIZE | 38.0 | 7 | 66 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11549459397792816 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 272 | BUY | STABILIZE | 38.0 | 7 | 78 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15154017508029938 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 6 | 5-2 | 273 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 76 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004056256264448166 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 274 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 76 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4119027853012085 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 275 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 76 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07571882754564285 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 276 | BUY_XP | STABILIZE | 38.0 | 7 | 76 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04732000082731247 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 277 | REROLL | STABILIZE | 38.0 | 7 | 72 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 278 | SELL | STABILIZE | 38.0 | 7 | 70 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4598543643951416 | 0.0 | 0.0 | +— / -57d86f23-f167-472f-9878-21dcddc0a5f7 |
| Jogador 6 | 5-2 | 279 | BUY | STABILIZE | 38.0 | 7 | 78 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8814905285835266 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -7fd8b302-97aa-4373-94f4-adfcad477ed2,93f7279f-b03b-407b-b623-c0a2bd88f877 |
| Jogador 6 | 5-2 | 280 | BUY | STABILIZE | 38.0 | 7 | 75 | 5 | 30.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3876757323741913 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 6 | 5-3 | 282 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 85 | 5 | 30.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4024730622768402 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 283 | BUY | STABILIZE | 38.0 | 7 | 85 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08650308102369308 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 6 | 5-3 | 284 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 81 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -7.368267688434571e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 285 | MOVE_BENCH | STABILIZE | 38.0 | 7 | 81 | 5 | 36.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4131736159324646 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 286 | PASS | STABILIZE | 38.0 | 7 | 81 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12989333271980286 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 292 | SELL | ALL_IN | 22.0 | 7 | 91 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49077779054641724 | 0.0 | 0.0 | +— / -b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 6 | 5-4 | 293 | BUY | ALL_IN | 22.0 | 7 | 99 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.108741894364357 | 0.0 | 0.0 | +438ec27b-d901-437b-82b5-64e6d46fccb1 / -— |
| Jogador 6 | 5-4 | 294 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 97 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09064480662345886 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 295 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 97 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1020413264632225 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 296 | REROLL | ALL_IN | 22.0 | 7 | 97 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 297 | SELL | ALL_IN | 22.0 | 7 | 95 | 5 | 38.0 | Feérico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6887999773025513 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 6 | 5-4 | 298 | BUY | ALL_IN | 22.0 | 7 | 103 | 5 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9369827508926392 | 0.0 | 0.0 | +3329c812-11fa-4335-a982-f03e6ab28ee0 / -— |
| Jogador 6 | 5-4 | 299 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 102 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12995660305023193 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 300 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 7 | 102 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12481391429901123 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 302 | SELL | ALL_IN | 22.0 | 7 | 112 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011823879554867744 | 0.0 | 0.0 | +— / -a492f78e-91f0-48cb-891a-6518551da328 |
| Jogador 6 | 5-5 | 303 | BUY | ALL_IN | 22.0 | 7 | 114 | 5 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0094878673553467 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 6 | 5-5 | 304 | SELL | ALL_IN | 22.0 | 7 | 113 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -438ec27b-d901-437b-82b5-64e6d46fccb1 |
| Jogador 6 | 5-5 | 305 | BUY | ALL_IN | 22.0 | 7 | 115 | 5 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.949950635433197 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 6 | 5-5 | 306 | REROLL | ALL_IN | 22.0 | 7 | 112 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 307 | SELL | ALL_IN | 22.0 | 7 | 110 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4814888834953308 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 6 | 5-5 | 308 | BUY | ALL_IN | 22.0 | 7 | 112 | 5 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8069534301757812 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 6 | 5-5 | 309 | REROLL | ALL_IN | 22.0 | 7 | 109 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 310 | SELL | ALL_IN | 22.0 | 7 | 107 | 5 | 38.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6249951124191284 | 0.0 | 0.0 | +— / -7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 6 | 5-6 | 312 | BUY | ALL_IN | 5.0 | 7 | 121 | 5 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0858181715011597 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -2ed895f2-1e83-426c-88fc-b9fb6403835d,9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 5-6 | 313 | BUY | ALL_IN | 5.0 | 7 | 118 | 5 | 32.0 | Feérico/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47179779410362244 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 6 | 5-6 | 314 | MOVE_BENCH | ALL_IN | 5.0 | 7 | 115 | 5 | 32.0 | Feérico/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5947930216789246 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 315 | BUY | ALL_IN | 5.0 | 7 | 115 | 5 | 38.0 | Feérico/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.573042631149292 | 0.0 | 0.0 | +3eccad10-cc50-4695-852e-0809356dd33b / -— |
| Jogador 6 | 5-6 | 316 | MOVE_BOARD | ALL_IN | 5.0 | 7 | 113 | 5 | 38.0 | Feérico/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 317 | MOVE_BOARD | ALL_IN | 5.0 | 7 | 113 | 5 | 38.0 | Feérico/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 318 | PASS | ALL_IN | 5.0 | 7 | 113 | 5 | 38.0 | Feérico/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5774304270744324 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3524000942707062 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 35 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.048647403717041 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 36 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5160974860191345 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0325764417648315 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13629421591758728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1526176929473877 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 51 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1510968655347824 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0888063907623291 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 53 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2632134258747101 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11174893379211426 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3338145315647125 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 62 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0713411495089531 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 65 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0478954315185547 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 68 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17527446150779724 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 69 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.18764565885066986 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 70 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4766789674758911 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 71 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09254232048988342 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 72 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1344592422246933 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 74 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0459800958633423 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8669515252113342 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 76 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2831466794013977 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 77 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1378285437822342 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 78 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 2-3 | 80 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07392439246177673 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2444029301404953 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28364497423171997 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37168264389038086 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 85 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018389733508229256 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | PASS | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2652222812175751 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 5 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005583607708103955 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 94 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 5 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015035429038107395 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 95 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 5 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 96 | PASS | STABILIZE | 95.0 | 5 | 5 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 5 | 11 | 1 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.816093385219574 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8123023509979248 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1882021278142929 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09705138951539993 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0031147634144872427 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20756664872169495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002126317238435149 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058574602007865906 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 88.0 | 5 | 7 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1582103669643402 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 113 | SELL | STABILIZE | 88.0 | 5 | 5 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-7 | 114 | BUY | STABILIZE | 88.0 | 5 | 8 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15631571412086487 | 0.0 | 0.0 | +1e0a3ead-540d-4169-a1fc-3e79592564a0 / -— |
| Jogador 7 | 2-7 | 115 | BUY_XP | STABILIZE | 88.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 2 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24445347487926483 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 2 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006635901518166065 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 2 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014950793236494064 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 119 | PASS | STABILIZE | 88.0 | 5 | 2 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 5 | 7 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18349425494670868 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 123 | SELL | STABILIZE | 88.0 | 5 | 7 | 0 | 24.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006166666746139526 | 0.0 | 0.0 | +— / -242805ca-f275-4e04-a2f5-81e0b6680dd1 |
| Jogador 7 | 3-1 | 124 | BUY | STABILIZE | 88.0 | 5 | 8 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8377689719200134 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -bb7ed7a4-035a-4798-a9b2-44893057ab84,dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14006343483924866 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3766744136810303 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 127 | BUY | STABILIZE | 88.0 | 5 | 7 | 0 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1703425496816635 | 0.0 | 0.0 | +c114a849-aa3b-4b7f-bc26-b5b699914f0b / -— |
| Jogador 7 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 6 | 0 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021352507174015045 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 129 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 6 | 0 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015043162740767002 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 6 | 0 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 88.0 | 5 | 12 | 1 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8049371838569641 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -— |
| Jogador 7 | 3-2 | 133 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 10 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 134 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 10 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15336190164089203 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 135 | PASS | STABILIZE | 88.0 | 5 | 10 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | SELL | FAST8 | 78.0 | 6 | 16 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -033a84d9-70f6-46a8-a6eb-a2f03be70400 |
| Jogador 7 | 3-3 | 143 | BUY | FAST8 | 78.0 | 6 | 19 | 1 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.21114927530288696 | 0.0 | 0.0 | +4d03897d-0113-4a29-a864-75305c142d97 / -— |
| Jogador 7 | 3-3 | 144 | EQUIP_FROM_INVENTORY | FAST8 | 78.0 | 6 | 17 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.139963299036026 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 145 | EQUIP_FROM_INVENTORY | FAST8 | 78.0 | 6 | 17 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0867229625582695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 146 | BUY_XP | FAST8 | 78.0 | 6 | 17 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 147 | SELL | FAST8 | 78.0 | 6 | 13 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028699999675154686 | 0.0 | 0.0 | +— / -c114a849-aa3b-4b7f-bc26-b5b699914f0b |
| Jogador 7 | 3-3 | 148 | BUY | FAST8 | 78.0 | 6 | 14 | 1 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.188423752784729 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 149 | BUY_XP | FAST8 | 78.0 | 6 | 11 | 1 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 150 | BUY_XP | FAST8 | 78.0 | 6 | 7 | 0 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 152 | SELL | FAST8 | 69.0 | 6 | 9 | 0 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08563333004713058 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 3-4 | 153 | BUY | FAST8 | 69.0 | 6 | 12 | 1 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6839414238929749 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 9 | 0 | 22.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25301268696784973 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 155 | BUY | FAST8 | 69.0 | 6 | 9 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21350452303886414 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 156 | BUY_XP | FAST8 | 69.0 | 6 | 6 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | MOVE_BENCH | FAST8 | 69.0 | 6 | 2 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5968294143676758 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 158 | MOVE_BOARD | FAST8 | 69.0 | 6 | 2 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016321837902069092 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 159 | MOVE_BOARD | FAST8 | 69.0 | 6 | 2 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06559587270021439 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 160 | PASS | FAST8 | 69.0 | 6 | 2 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | FAST8 | 69.0 | 6 | 8 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7224477529525757 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 163 | BUY | FAST8 | 69.0 | 6 | 5 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4684355854988098 | 0.0 | 0.0 | +2074e6ec-81e7-41c9-be7e-a0d9310fbafa / -— |
| Jogador 7 | 3-5 | 164 | MOVE_BOARD | FAST8 | 69.0 | 6 | 3 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 165 | MOVE_BOARD | FAST8 | 69.0 | 6 | 3 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 166 | PASS | FAST8 | 69.0 | 6 | 3 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | SELL | FAST8 | 69.0 | 6 | 9 | 0 | 32.0 | Devastador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 3-6 | 173 | BUY | FAST8 | 69.0 | 6 | 17 | 1 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7347519993782043 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 7 | 3-6 | 174 | EQUIP_FROM_INVENTORY | FAST8 | 69.0 | 6 | 15 | 1 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12303614616394043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | EQUIP_FROM_INVENTORY | FAST8 | 69.0 | 6 | 15 | 1 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08951142430305481 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 176 | MOVE_BOARD | FAST8 | 69.0 | 6 | 15 | 1 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030445897951722145 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 177 | MOVE_BOARD | FAST8 | 69.0 | 6 | 15 | 1 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015005300752818584 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 178 | MOVE_BOARD | FAST8 | 69.0 | 6 | 15 | 1 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014990084804594517 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 179 | PASS | FAST8 | 69.0 | 6 | 15 | 1 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | SELL | FAST8 | 69.0 | 6 | 23 | 2 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.451824426651001 | 0.0 | 0.0 | +— / -a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 3-7 | 183 | BUY | FAST8 | 69.0 | 6 | 25 | 2 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7788244485855103 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -f116ca4e-dbe8-457e-83a5-958525aa384a,f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 3-7 | 184 | BUY | FAST8 | 69.0 | 6 | 22 | 2 | 26.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7373292446136475 | 0.0 | 0.0 | +1cba4955-961e-4efd-a291-e0a70bf72841 / -— |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | FAST8 | 69.0 | 6 | 20 | 2 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017436762573197484 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 186 | MOVE_BENCH | FAST8 | 69.0 | 6 | 20 | 2 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5262610912322998 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | BUY | FAST8 | 69.0 | 6 | 20 | 2 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13745568692684174 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 188 | MOVE_BOARD | FAST8 | 69.0 | 6 | 19 | 1 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004105461295694113 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 189 | MOVE_BOARD | FAST8 | 69.0 | 6 | 19 | 1 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013002878986299038 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 190 | MOVE_BOARD | FAST8 | 69.0 | 6 | 19 | 1 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015590151771903038 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 69.0 | 6 | 26 | 2 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.05461885780096054 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 69.0 | 6 | 26 | 2 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06879061460494995 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | SELL | FAST8 | 69.0 | 6 | 26 | 2 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -8a52858d-da47-4de9-8e91-8612788cb8fd |
| Jogador 7 | 4-1 | 195 | BUY | FAST8 | 69.0 | 6 | 34 | 3 | 30.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.825689435005188 | 0.0 | 0.0 | +6a30a366-c631-429d-9523-af769cdf48a4 / -1e0a3ead-540d-4169-a1fc-3e79592564a0,69ccc61a-403b-4025-8359-b2061dc6ad10 |
| Jogador 7 | 4-1 | 196 | EQUIP_FROM_INVENTORY | FAST8 | 69.0 | 6 | 32 | 3 | 30.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04174584895372391 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 197 | EQUIP_FROM_INVENTORY | FAST8 | 69.0 | 6 | 32 | 3 | 30.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06165093928575516 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 198 | MOVE_BOARD | FAST8 | 69.0 | 6 | 32 | 3 | 30.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 199 | BUY | FAST8 | 69.0 | 6 | 32 | 3 | 30.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14726027846336365 | 0.0 | 0.0 | +626c50be-ec88-444f-84bb-9b8d41100085 / -— |
| Jogador 7 | 4-1 | 200 | MOVE_BOARD | FAST8 | 69.0 | 6 | 31 | 3 | 30.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.5319015801651403e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | BUY | FAST8 | 69.0 | 6 | 41 | 4 | 30.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7758994102478027 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -96bf8f0a-9fe1-4182-95dc-903c1e623983,ac02c0c4-a10d-497d-b6c1-d458ad7ae58c |
| Jogador 7 | 4-2 | 203 | BUY | FAST8 | 69.0 | 6 | 39 | 3 | 26.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2741664946079254 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 7 | 4-2 | 204 | MOVE_BOARD | FAST8 | 69.0 | 6 | 37 | 3 | 26.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005373157327994704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 205 | MOVE_BENCH | FAST8 | 69.0 | 6 | 37 | 3 | 26.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.537998616695404 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 206 | BUY | FAST8 | 69.0 | 6 | 37 | 3 | 28.0 | Devastador/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013446195051074028 | 0.0 | 0.0 | +bf0751f0-8094-4441-adb3-e5f8b4158426 / -— |
| Jogador 7 | 4-2 | 207 | MOVE_BOARD | FAST8 | 69.0 | 6 | 36 | 3 | 28.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015691241715103388 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 208 | MOVE_BOARD | FAST8 | 69.0 | 6 | 36 | 3 | 28.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014907476492226124 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 209 | MOVE_BOARD | FAST8 | 69.0 | 6 | 36 | 3 | 28.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05758947506546974 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 210 | PASS | FAST8 | 69.0 | 6 | 36 | 3 | 28.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03999999910593033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | SELL | FAST8 | 69.0 | 6 | 46 | 4 | 28.0 | Devastador/DA_Murkwolf18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5033000111579895 | 0.0 | 0.0 | +— / -0803068a-0141-4e75-ab81-12bb13986025 |
| Jogador 7 | 4-3 | 213 | BUY | FAST8 | 69.0 | 6 | 51 | 5 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8138272762298584 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -— |
| Jogador 7 | 4-3 | 214 | SELL | FAST8 | 69.0 | 6 | 50 | 5 | 28.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -6a30a366-c631-429d-9523-af769cdf48a4 |
| Jogador 7 | 4-3 | 215 | BUY | FAST8 | 69.0 | 6 | 55 | 5 | 28.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8917253613471985 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -1cba4955-961e-4efd-a291-e0a70bf72841,4d03897d-0113-4a29-a864-75305c142d97 |
| Jogador 7 | 4-3 | 216 | BUY | STABILIZE | 69.0 | 6 | 53 | 5 | 24.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9323958158493042 | 0.0 | 0.0 | +f5cca112-4fa0-4ee6-a863-20a5d49ab7ef / -2074e6ec-81e7-41c9-be7e-a0d9310fbafa,42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 4-3 | 217 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 51 | 5 | 20.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3642820417881012 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 218 | MOVE_BOARD | FAST8 | 69.0 | 6 | 51 | 5 | 26.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 219 | MOVE_BOARD | FAST8 | 69.0 | 6 | 51 | 5 | 26.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012729139067232609 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 220 | PASS | FAST8 | 69.0 | 6 | 51 | 5 | 26.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08047321438789368 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | BUY | FAST8 | 57.0 | 6 | 61 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.866106390953064 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 7 | 4-4 | 223 | BUY | FAST8 | 57.0 | 6 | 59 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14899873733520508 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 7 | 4-4 | 224 | MOVE_BOARD | FAST8 | 57.0 | 6 | 56 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026431381702423096 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 225 | MOVE_BOARD | FAST8 | 57.0 | 6 | 56 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | FAST8 | 57.0 | 6 | 56 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | PASS | FAST8 | 57.0 | 6 | 56 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22339646518230438 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | BUY | FAST8 | 57.0 | 6 | 66 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5608271360397339 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 7 | 4-5 | 233 | SELL | FAST8 | 57.0 | 6 | 63 | 5 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44434911012649536 | 0.0 | 0.0 | +— / -f5cca112-4fa0-4ee6-a863-20a5d49ab7ef |
| Jogador 7 | 4-5 | 234 | BUY | FAST8 | 57.0 | 6 | 68 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.40539130568504333 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 7 | 4-5 | 235 | EQUIP_FROM_INVENTORY | FAST8 | 57.0 | 6 | 67 | 5 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09198057651519775 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 236 | MOVE_BOARD | FAST8 | 57.0 | 6 | 67 | 5 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 237 | MOVE_BOARD | FAST8 | 57.0 | 6 | 67 | 5 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01449790969491005 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 238 | PASS | FAST8 | 57.0 | 6 | 67 | 5 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0906796008348465 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | FAST8 | 45.0 | 7 | 78 | 5 | 32.0 | Devastador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -bf0751f0-8094-4441-adb3-e5f8b4158426 |
| Jogador 7 | 4-6 | 243 | BUY | FAST8 | 45.0 | 7 | 79 | 5 | 32.0 | Devastador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7448098063468933 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,715d5bfc-c8c3-4dec-a247-9e07ee2755e8 |
| Jogador 7 | 4-6 | 244 | MOVE_BENCH | FAST8 | 45.0 | 7 | 76 | 5 | 26.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1561177372932434 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 245 | MOVE_BENCH | FAST8 | 45.0 | 7 | 76 | 5 | 32.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40637800097465515 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | BUY | FAST8 | 45.0 | 7 | 76 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05016808956861496 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 7 | 4-6 | 247 | MOVE_BOARD | FAST8 | 45.0 | 7 | 75 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 248 | MOVE_BOARD | FAST8 | 45.0 | 7 | 75 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 249 | PASS | FAST8 | 45.0 | 7 | 75 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09798949211835861 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | BUY | FAST8 | 45.0 | 7 | 86 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8085561394691467 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 7 | 4-7 | 253 | BUY | FAST8 | 45.0 | 7 | 83 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31037637591362 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 7 | 4-7 | 254 | MOVE_BOARD | FAST8 | 45.0 | 7 | 81 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 255 | MOVE_BOARD | FAST8 | 45.0 | 7 | 81 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499201636761427 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | PASS | FAST8 | 45.0 | 7 | 81 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10274707525968552 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | CRAFT_AND_EQUIP | FAST8 | 45.0 | 7 | 91 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.09780782461166382 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | FAST8 | 45.0 | 7 | 91 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1319594383239746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | MOVE_BOARD | FAST8 | 45.0 | 7 | 91 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 265 | SELL | FAST8 | 45.0 | 7 | 91 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 7 | 5-1 | 266 | BUY | FAST8 | 45.0 | 7 | 96 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8164289593696594 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 7 | 5-1 | 267 | EQUIP_FROM_INVENTORY | FAST8 | 45.0 | 7 | 94 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10411722213029861 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 268 | MOVE_BOARD | FAST8 | 45.0 | 7 | 94 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 269 | MOVE_BOARD | FAST8 | 45.0 | 7 | 94 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 270 | PASS | FAST8 | 45.0 | 7 | 94 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12466555833816528 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | SELL | STABILIZE | 28.0 | 7 | 104 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02990354411303997 | 0.0 | 0.0 | +— / -6ea982ab-292d-42fc-99e6-d67c89f9f4fe |
| Jogador 7 | 5-2 | 273 | BUY | STABILIZE | 28.0 | 7 | 105 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0224190950393677 | 0.0 | 0.0 | +9414ca8e-930e-4a0e-8cbd-42d8997d8705 / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4,f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 7 | 5-2 | 274 | BUY | STABILIZE | 28.0 | 7 | 103 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0194008350372314 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -24b29fe6-466c-42d5-9f92-5d6114f0f98f,98b600a1-736b-437d-a69e-8a7f7235d9c3 |
| Jogador 7 | 5-2 | 275 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 101 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 276 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 101 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014989150688052177 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 277 | PASS | STABILIZE | 28.0 | 7 | 101 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1770356297492981 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | BUY | ALL_IN | 12.0 | 7 | 112 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7177391052246094 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 7 | 5-3 | 283 | BUY | ALL_IN | 12.0 | 7 | 110 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20239965617656708 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 7 | 5-3 | 284 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 107 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.950117262429558e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 285 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 107 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015057790093123913 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 286 | PASS | ALL_IN | 12.0 | 7 | 107 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.702755868434906 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | BUY | ALL_IN | 12.0 | 7 | 118 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45765724778175354 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 7 | 5-4 | 293 | SELL | ALL_IN | 12.0 | 7 | 116 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7128999829292297 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 7 | 5-4 | 294 | BUY | ALL_IN | 12.0 | 7 | 121 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4239270091056824 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -— |
| Jogador 7 | 5-4 | 295 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 117 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09114836156368256 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 296 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 117 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0763232558965683 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 297 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 117 | 5 | 40.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4148872494697571 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 298 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 117 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07620717585086823 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 299 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 117 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07676953822374344 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 300 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 117 | 5 | 40.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3966253995895386 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 302 | SELL | ALL_IN | 12.0 | 7 | 128 | 5 | 50.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 7 | 5-5 | 303 | BUY | ALL_IN | 12.0 | 7 | 131 | 5 | 50.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45444509387016296 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 7 | 5-5 | 304 | SELL | ALL_IN | 12.0 | 7 | 130 | 5 | 50.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5556989312171936 | 0.0 | 0.0 | +— / -262702a6-b710-4129-9dc6-0c1a04514ff9 |
| Jogador 7 | 5-5 | 305 | BUY | ALL_IN | 12.0 | 7 | 131 | 5 | 50.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.419661283493042 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 7 | 5-5 | 306 | REROLL | ALL_IN | 12.0 | 7 | 128 | 5 | 50.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 307 | SELL | ALL_IN | 12.0 | 7 | 126 | 5 | 50.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005558657459914684 | 0.0 | 0.0 | +— / -626c50be-ec88-444f-84bb-9b8d41100085 |
| Jogador 7 | 5-5 | 308 | BUY | ALL_IN | 12.0 | 7 | 127 | 5 | 50.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0642656460404396 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 7 | 5-5 | 309 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 124 | 5 | 50.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7057697772979736 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 310 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 124 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4146520793437958 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 312 | SELL | ALL_IN | 12.0 | 7 | 135 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7128999829292297 | 0.0 | 0.0 | +— / -9414ca8e-930e-4a0e-8cbd-42d8997d8705 |
| Jogador 7 | 5-6 | 313 | BUY | ALL_IN | 12.0 | 7 | 140 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8970016837120056 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 7 | 5-6 | 314 | SELL | ALL_IN | 12.0 | 7 | 137 | 5 | 44.0 | Devastador/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03405597060918808 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 7 | 5-6 | 315 | BUY | ALL_IN | 12.0 | 7 | 140 | 5 | 44.0 | Devastador/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0579332113265991 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -599caeca-96ef-4308-b6cd-f65b005879e2,864f332a-0446-4995-b7fb-76d48d293501 |
| Jogador 7 | 5-6 | 316 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 137 | 5 | 38.0 | Devastador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5312920808792114 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 317 | BUY | ALL_IN | 12.0 | 7 | 137 | 5 | 44.0 | Devastador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15068022906780243 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 7 | 5-6 | 318 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 134 | 5 | 44.0 | Devastador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 319 | BUY | ALL_IN | 12.0 | 7 | 134 | 5 | 44.0 | Devastador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12613360583782196 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 7 | 5-6 | 320 | MOVE_BOARD | ALL_IN | 12.0 | 7 | 133 | 5 | 44.0 | Devastador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5923603177070618 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01241401955485344 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15749381482601166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 35 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29005196690559387 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 36 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4232161343097687 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.649158239364624 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -— |
| Jogador 8 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0014695916324853897 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 50 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29146304726600647 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 51 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24316278100013733 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1201409101486206 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 53 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9806308746337891 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 54 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.7755575615628914e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 55 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09524503350257874 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 56 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0449798107147217 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9771193861961365 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -64f24363-3325-4538-972e-a6d8260b3787,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-1 | 61 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3664688467979431 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 62 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13641192018985748 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 63 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1504042148590088 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5469688773155212 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 65 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2734346091747284 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -— |
| Jogador 8 | 2-2 | 67 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2791939377784729 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 68 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2254001945257187 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 71 | PASS | STABILIZE | 94.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9777241349220276 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 75 | BUY | STABILIZE | 89.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8352176547050476 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 76 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32807624340057373 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 77 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07242975383996964 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33034923672676086 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 79 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 82 | SELL | LOSS_STREAK | 83.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-4 | 83 | BUY | LOSS_STREAK | 83.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14944733679294586 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 84 | SELL | LOSS_STREAK | 83.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050433333963155746 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-4 | 85 | BUY | LOSS_STREAK | 83.0 | 4 | 10 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09622309356927872 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 86 | SELL | LOSS_STREAK | 83.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0466945618391037 | 0.0 | 0.0 | +— / -01f4a73c-7202-4ee3-964e-d32370c3c547 |
| Jogador 8 | 2-4 | 87 | BUY | LOSS_STREAK | 83.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06105498597025871 | 0.0 | 0.0 | +fb186a97-59a4-4b3a-be2f-dadd2670dc95 / -— |
| Jogador 8 | 2-4 | 88 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018928564386442304 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 89 | SELL | LOSS_STREAK | 83.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Leona | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0364999994635582 | 0.0 | 0.0 | +— / -fb186a97-59a4-4b3a-be2f-dadd2670dc95 |
| Jogador 8 | 2-4 | 90 | SELL | LOSS_STREAK | 83.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04296672344207764 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-5 | 92 | BUY | LOSS_STREAK | 83.0 | 4 | 18 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.857100248336792 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -5de56114-806a-4f58-8241-b3b8434a2154,76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 2-5 | 93 | BUY | LOSS_STREAK | 83.0 | 4 | 17 | 1 | 10.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0720248818397522 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 94 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 14 | 1 | 10.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3957766890525818 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 83.0 | 4 | 14 | 1 | 12.0 | Enfeitiçador/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-5 | 96 | SELL | STABILIZE | 83.0 | 4 | 17 | 1 | 12.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5490000247955322 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-5 | 97 | BUY | STABILIZE | 83.0 | 4 | 20 | 2 | 12.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16763073205947876 | 0.0 | 0.0 | +cf4575c2-3622-4493-91f1-c5efbe1fbd8b / -— |
| Jogador 8 | 2-5 | 98 | SELL | STABILIZE | 83.0 | 4 | 19 | 1 | 12.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34030094742774963 | 0.0 | 0.0 | +— / -cf4575c2-3622-4493-91f1-c5efbe1fbd8b |
| Jogador 8 | 2-5 | 99 | BUY | STABILIZE | 83.0 | 4 | 20 | 2 | 12.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11194249242544174 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 100 | BUY_XP | STABILIZE | 83.0 | 4 | 18 | 1 | 12.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 77.0 | 5 | 21 | 2 | 12.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22507792711257935 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 103 | BUY | STABILIZE | 77.0 | 5 | 18 | 1 | 12.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2251078486442566 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 77.0 | 5 | 15 | 1 | 12.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40299370884895325 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 105 | BUY | STABILIZE | 77.0 | 5 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1459069401025772 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 8 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 108 | PASS | STABILIZE | 77.0 | 5 | 14 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 112 | BUY | STABILIZE | 77.0 | 5 | 21 | 2 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8168473839759827 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 113 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 18 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13479630649089813 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 114 | SELL | STABILIZE | 77.0 | 5 | 18 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012715594843029976 | 0.0 | 0.0 | +— / -630d9254-3856-4d88-b981-43a8270b4b3d |
| Jogador 8 | 2-7 | 115 | BUY | STABILIZE | 77.0 | 5 | 19 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04621228948235512 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 16 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04852622002363205 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 117 | SELL | STABILIZE | 77.0 | 5 | 16 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010170581750571728 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-7 | 118 | SELL | STABILIZE | 77.0 | 5 | 18 | 1 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008333333767950535 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-7 | 119 | BUY | STABILIZE | 77.0 | 5 | 21 | 2 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20040564239025116 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 20 | 2 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 77.0 | 5 | 27 | 2 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20898807048797607 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 77.0 | 5 | 23 | 2 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20726647973060608 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 124 | SELL | STABILIZE | 77.0 | 5 | 23 | 2 | 16.0 | Espinhos Negros/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013095568865537643 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 77.0 | 5 | 26 | 2 | 16.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31970149278640747 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 126 | SELL | STABILIZE | 77.0 | 5 | 26 | 2 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41966667771339417 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-1 | 127 | BUY | STABILIZE | 77.0 | 5 | 27 | 2 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042583610862493515 | 0.0 | 0.0 | +88420167-3841-43dd-b1d0-3e5ab2294c78 / -— |
| Jogador 8 | 3-1 | 128 | BUY_XP | STABILIZE | 77.0 | 5 | 25 | 2 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015681249788030982 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 129 | BUY_XP | STABILIZE | 77.0 | 5 | 21 | 2 | 20.0 | Espinhos Negros/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 130 | MOVE_BOARD | STABILIZE | 77.0 | 5 | 17 | 1 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06649219244718552 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 132 | BUY | STABILIZE | 66.0 | 5 | 23 | 2 | 20.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1094350516796112 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 133 | BUY_XP | STABILIZE | 66.0 | 5 | 19 | 1 | 20.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06353499740362167 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 66.0 | 6 | 15 | 1 | 20.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5264443755149841 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 135 | BUY | FAST8 | 66.0 | 6 | 15 | 1 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010946119204163551 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 136 | MOVE_BOARD | FAST8 | 66.0 | 6 | 14 | 1 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10244913399219513 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 137 | MOVE_BOARD | FAST8 | 66.0 | 6 | 14 | 1 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 138 | MOVE_BOARD | FAST8 | 66.0 | 6 | 14 | 1 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 139 | PASS | FAST8 | 66.0 | 6 | 14 | 1 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | SELL | FAST8 | 66.0 | 6 | 21 | 2 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02306441031396389 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 8 | 3-3 | 143 | BUY | FAST8 | 66.0 | 6 | 22 | 2 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5642684698104858 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 144 | MOVE_BOARD | FAST8 | 66.0 | 6 | 21 | 2 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002071708207949996 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 145 | MOVE_BOARD | FAST8 | 66.0 | 6 | 21 | 2 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09050800651311874 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 146 | MOVE_BOARD | FAST8 | 66.0 | 6 | 21 | 2 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007950125262141228 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 147 | MOVE_BOARD | FAST8 | 66.0 | 6 | 21 | 2 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12612825632095337 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 148 | MOVE_BOARD | FAST8 | 66.0 | 6 | 21 | 2 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01702236197888851 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 149 | PASS | FAST8 | 66.0 | 6 | 21 | 2 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 152 | MOVE_BOARD | FAST8 | 66.0 | 6 | 30 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0662694200873375 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 153 | MOVE_BOARD | FAST8 | 66.0 | 6 | 30 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06893192231655121 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 154 | MOVE_BOARD | FAST8 | 66.0 | 6 | 30 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015016594901680946 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 155 | MOVE_BOARD | FAST8 | 66.0 | 6 | 30 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015028283931314945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 156 | PASS | FAST8 | 66.0 | 6 | 30 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 162 | SELL | FAST8 | 66.0 | 6 | 39 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08579999953508377 | 0.0 | 0.0 | +— / -88420167-3841-43dd-b1d0-3e5ab2294c78 |
| Jogador 8 | 3-5 | 163 | BUY | FAST8 | 66.0 | 6 | 41 | 4 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1819978654384613 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 164 | MOVE_BOARD | FAST8 | 66.0 | 6 | 38 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.104768544901162e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 165 | MOVE_BOARD | FAST8 | 66.0 | 6 | 38 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000700019299984 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 166 | MOVE_BOARD | FAST8 | 66.0 | 6 | 38 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 167 | PASS | FAST8 | 66.0 | 6 | 38 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 172 | SELL | FAST8 | 56.0 | 6 | 46 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060233332216739655 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 3-6 | 173 | BUY | FAST8 | 56.0 | 6 | 49 | 4 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23491604626178741 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 174 | MOVE_BOARD | FAST8 | 56.0 | 6 | 46 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.305915743112564e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 175 | MOVE_BOARD | FAST8 | 56.0 | 6 | 46 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 176 | PASS | FAST8 | 56.0 | 6 | 46 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 182 | SELL | FAST8 | 56.0 | 6 | 56 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4906333386898041 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-7 | 183 | BUY | FAST8 | 56.0 | 6 | 57 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7621328234672546 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 184 | SELL | FAST8 | 56.0 | 6 | 54 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-7 | 185 | BUY | FAST8 | 56.0 | 6 | 55 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2575351893901825 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 186 | BUY_XP | FAST8 | 56.0 | 6 | 54 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04451199993491173 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 187 | BUY_XP | FAST8 | 56.0 | 6 | 50 | 5 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0585159994661808 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 188 | BUY_XP | FAST8 | 56.0 | 6 | 46 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021484000608325005 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 189 | BUY_XP | FAST8 | 56.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0585159994661808 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 190 | BUY_XP | FAST8 | 56.0 | 6 | 38 | 3 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021484000608325005 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | CRAFT_AND_EQUIP | FAST8 | 56.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15738986432552338 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 193 | CRAFT_AND_EQUIP | FAST8 | 56.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1805189847946167 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 194 | SELL | FAST8 | 56.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4116729199886322 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 4-1 | 195 | BUY | FAST8 | 56.0 | 6 | 45 | 4 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8544070720672607 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce,f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 4-1 | 196 | BUY | FAST8 | 56.0 | 6 | 44 | 4 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.528706967830658 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 197 | MOVE_BOARD | FAST8 | 56.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 198 | MOVE_BOARD | FAST8 | 56.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015167036093771458 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 199 | PASS | FAST8 | 56.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1842857152223587 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 202 | BUY | FAST8 | 42.0 | 7 | 51 | 5 | 26.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1824970692396164 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 4-2 | 203 | MOVE_BENCH | FAST8 | 42.0 | 7 | 48 | 4 | 26.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07852869480848312 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 204 | BUY | FAST8 | 42.0 | 7 | 48 | 4 | 32.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06502850353717804 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 205 | MOVE_BOARD | FAST8 | 42.0 | 7 | 44 | 4 | 32.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0004860933404415846 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 206 | MOVE_BOARD | FAST8 | 42.0 | 7 | 44 | 4 | 32.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 207 | PASS | FAST8 | 42.0 | 7 | 44 | 4 | 32.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05104761943221092 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 212 | SELL | STABILIZE | 30.0 | 7 | 54 | 5 | 32.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 8 | 4-3 | 213 | BUY | STABILIZE | 30.0 | 7 | 57 | 5 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.17951446771621704 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 214 | EQUIP_FROM_INVENTORY | STABILIZE | 30.0 | 7 | 54 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08473169058561325 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 215 | EQUIP_FROM_INVENTORY | STABILIZE | 30.0 | 7 | 54 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1138608381152153 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 216 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 54 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0003117983287665993 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 217 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 54 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499878615140915 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 218 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 54 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 219 | PASS | STABILIZE | 30.0 | 7 | 54 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10990767180919647 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 222 | SELL | STABILIZE | 30.0 | 7 | 65 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022466666996479034 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 4-4 | 223 | BUY | STABILIZE | 30.0 | 7 | 69 | 5 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8847211599349976 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 8 | 4-4 | 224 | SELL | STABILIZE | 30.0 | 7 | 68 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 8 | 4-4 | 225 | BUY | STABILIZE | 30.0 | 7 | 71 | 5 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8598210215568542 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -— |
| Jogador 8 | 4-4 | 226 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 68 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.944273081899155e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 227 | BUY_XP | STABILIZE | 30.0 | 7 | 68 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061765000224113464 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 228 | BUY_XP | STABILIZE | 30.0 | 7 | 64 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061195001006126404 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 229 | BUY_XP | STABILIZE | 30.0 | 7 | 60 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06062500178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 230 | BUY_XP | STABILIZE | 30.0 | 7 | 56 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04019999876618385 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 232 | SELL | STABILIZE | 30.0 | 7 | 62 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4805999994277954 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 8 | 4-5 | 233 | BUY | STABILIZE | 30.0 | 7 | 64 | 5 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9078636765480042 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -— |
| Jogador 8 | 4-5 | 234 | SELL | STABILIZE | 30.0 | 7 | 63 | 5 | 32.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44419702887535095 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 4-5 | 235 | BUY | STABILIZE | 30.0 | 7 | 66 | 5 | 32.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9638979434967041 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -87600495-fe90-4832-ab42-9a5cb0ebe3f4,d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-5 | 236 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 63 | 5 | 20.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15893830358982086 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 237 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 63 | 5 | 28.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5703369975090027 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 238 | BUY | STABILIZE | 30.0 | 7 | 63 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02858847565948963 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 8 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 60 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006144068902358413 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 60 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 242 | BUY | STABILIZE | 30.0 | 7 | 72 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22207748889923096 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -— |
| Jogador 8 | 4-6 | 243 | MOVE_BOARD | STABILIZE | 30.0 | 7 | 69 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -8.935274672694504e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 244 | BUY_XP | STABILIZE | 30.0 | 7 | 69 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06190750002861023 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 245 | BUY_XP | STABILIZE | 30.0 | 7 | 65 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06133750081062317 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 246 | BUY_XP | STABILIZE | 30.0 | 7 | 61 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06076750159263611 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 247 | BUY_XP | STABILIZE | 30.0 | 7 | 57 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04019999876618385 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 248 | BUY_XP | STABILIZE | 30.0 | 7 | 53 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04309999942779541 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 249 | BUY_XP | STABILIZE | 30.0 | 7 | 49 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 250 | BUY_XP | STABILIZE | 30.0 | 7 | 45 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 252 | SELL | STABILIZE | 30.0 | 7 | 52 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -9717d30c-f073-470c-a6ce-7db8257de559 |
| Jogador 8 | 4-7 | 253 | BUY | STABILIZE | 30.0 | 7 | 60 | 5 | 30.0 | Feérico/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17791108787059784 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 8 | 4-7 | 254 | SELL | STABILIZE | 30.0 | 7 | 57 | 5 | 30.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -0f5471bd-1451-4979-adc9-aced6bb63610 |
| Jogador 8 | 4-7 | 255 | BUY | STABILIZE | 30.0 | 7 | 60 | 5 | 30.0 | Feérico/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.677655816078186 | 0.0 | 0.0 | +0fd34229-b814-4580-8651-59e712d5657f / -— |
| Jogador 8 | 4-7 | 256 | BUY_XP | STABILIZE | 30.0 | 7 | 57 | 5 | 30.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7998600006103516 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 257 | MOVE_BENCH | STABILIZE | 30.0 | 8 | 53 | 5 | 30.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44606807827949524 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 258 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 53 | 5 | 36.0 | Feérico/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014698708429932594 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 259 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 53 | 5 | 36.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01488923653960228 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 260 | PASS | STABILIZE | 30.0 | 8 | 53 | 5 | 36.0 | Feérico/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2040511816740036 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 262 | BUY | STABILIZE | 30.0 | 8 | 64 | 5 | 36.0 | Feérico/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1826643943786621 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 8 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 30.0 | 8 | 60 | 5 | 36.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16322071850299835 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 30.0 | 8 | 60 | 5 | 36.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16969427466392517 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 265 | MOVE_BENCH | STABILIZE | 30.0 | 8 | 60 | 5 | 36.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3997878134250641 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 266 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 60 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 267 | PASS | STABILIZE | 30.0 | 8 | 60 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12681987881660461 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 272 | SELL | STABILIZE | 30.0 | 8 | 72 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03537178784608841 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 5-2 | 273 | BUY | STABILIZE | 30.0 | 8 | 75 | 5 | 42.0 | Feérico/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7469236254692078 | 0.0 | 0.0 | +c8706680-2712-4914-b6c0-59bf92a2796d / -— |
| Jogador 8 | 5-2 | 274 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 72 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.156085253725905e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 275 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 72 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 276 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 72 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500002108514309 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 277 | PASS | STABILIZE | 30.0 | 8 | 72 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13938646018505096 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 282 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 85 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00019653482013382018 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 283 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 85 | 5 | 42.0 | Feérico/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014812970533967018 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 284 | PASS | STABILIZE | 30.0 | 8 | 85 | 5 | 42.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3075973391532898 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 292 | SELL | STABILIZE | 30.0 | 8 | 99 | 5 | 42.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5105666518211365 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 8 | 5-4 | 293 | BUY | STABILIZE | 30.0 | 8 | 102 | 5 | 42.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0225639343261719 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -167110eb-b0d0-4873-9ffe-38286dcc5ca2,23366968-ed3f-43d0-9f24-bb7691bf5d45 |
| Jogador 8 | 5-4 | 294 | BUY | STABILIZE | 30.0 | 8 | 99 | 5 | 42.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.750285267829895 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -— |
| Jogador 8 | 5-4 | 295 | REROLL | STABILIZE | 30.0 | 8 | 96 | 5 | 42.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 296 | BUY | STABILIZE | 30.0 | 8 | 94 | 5 | 42.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6807069182395935 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 8 | 5-4 | 297 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 92 | 5 | 42.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.4068182281334884e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 298 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 92 | 5 | 42.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 299 | PASS | STABILIZE | 30.0 | 8 | 92 | 5 | 42.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16142413020133972 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 302 | SELL | STABILIZE | 30.0 | 8 | 105 | 5 | 42.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -7f9f3188-2482-4518-9fd2-34f0ea1527a9 |
| Jogador 8 | 5-5 | 303 | BUY | STABILIZE | 30.0 | 8 | 113 | 5 | 42.0 | Feérico/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.383160799741745 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 8 | 5-5 | 304 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 112 | 5 | 42.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 305 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 112 | 5 | 42.0 | Feérico/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499720849096775 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 306 | PASS | STABILIZE | 30.0 | 8 | 112 | 5 | 42.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18428237736225128 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 312 | SELL | ALL_IN | 15.0 | 8 | 122 | 5 | 42.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5885999798774719 | 0.0 | 0.0 | +— / -a267d973-f857-4dda-89e1-209bff42ab6f |
| Jogador 8 | 5-6 | 313 | BUY | ALL_IN | 15.0 | 8 | 124 | 5 | 42.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0494896173477173 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -112206a4-c285-4f76-878a-056248cba468,2e656a3d-eed0-40bb-a831-443d972d6588 |
| Jogador 8 | 5-6 | 314 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 121 | 5 | 30.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34905296564102173 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 315 | BUY | ALL_IN | 15.0 | 8 | 121 | 5 | 32.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4300806224346161 | 0.0 | 0.0 | +3365b4aa-125c-4f72-bcc5-01c5a205b9b0 / -— |
| Jogador 8 | 5-6 | 316 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 118 | 5 | 32.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38340339064598083 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 317 | REROLL | ALL_IN | 15.0 | 8 | 118 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 318 | SELL | ALL_IN | 15.0 | 8 | 116 | 5 | 36.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7084000110626221 | 0.0 | 0.0 | +— / -27079fe2-8808-47b7-8b10-9fb2834bb6ed |
| Jogador 8 | 5-6 | 319 | BUY | ALL_IN | 15.0 | 8 | 124 | 5 | 36.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4622464179992676 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 8 | 5-6 | 320 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 8 | 121 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09094616025686264 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 322 | SELL | ALL_IN | 15.0 | 8 | 132 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6185666918754578 | 0.0 | 0.0 | +— / -57ba484a-6228-4263-8171-00a8a5893bea |
| Jogador 8 | 5-7 | 323 | BUY | ALL_IN | 15.0 | 8 | 135 | 5 | 36.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8861811757087708 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 8 | 5-7 | 324 | SELL | ALL_IN | 15.0 | 8 | 134 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -c8706680-2712-4914-b6c0-59bf92a2796d |
| Jogador 8 | 5-7 | 325 | BUY | ALL_IN | 15.0 | 8 | 137 | 5 | 36.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1576693058013916 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 8 | 5-7 | 326 | REROLL | ALL_IN | 15.0 | 8 | 134 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 327 | SELL | ALL_IN | 15.0 | 8 | 132 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -5de51369-647a-45bd-95b7-c8efe44c5484 |
| Jogador 8 | 5-7 | 328 | BUY | ALL_IN | 15.0 | 8 | 135 | 5 | 36.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03823055326938629 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -— |
| Jogador 8 | 5-7 | 329 | SELL | ALL_IN | 15.0 | 8 | 131 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016119003295898438 | 0.0 | 0.0 | +— / -1ad1f705-7e6b-4c1f-811c-2863dbf2db9e |
| Jogador 8 | 5-7 | 330 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 135 | 5 | 36.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5107617974281311 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 332 | BUY | ALL_IN | 15.0 | 8 | 145 | 5 | 38.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.11043381690979 | 0.0 | 0.0 | +e89905aa-6564-4e15-bc3a-c281646446bc / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,fe12befc-b473-4f91-9e51-558a03efa3ad |
| Jogador 8 | 6-1 | 333 | BUY | ALL_IN | 15.0 | 8 | 144 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.9436689019203186 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 8 | 6-1 | 334 | BUY | ALL_IN | 15.0 | 8 | 141 | 5 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4488886594772339 | 0.0 | 0.0 | +56332309-e8e8-464a-904f-e9253912cd2f / -— |
| Jogador 8 | 6-1 | 335 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 8 | 138 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.018593600019812584 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 336 | REROLL | ALL_IN | 15.0 | 8 | 138 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 337 | SELL | ALL_IN | 15.0 | 8 | 136 | 5 | 36.0 | Feérico/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7019000053405762 | 0.0 | 0.0 | +— / -e89905aa-6564-4e15-bc3a-c281646446bc |
| Jogador 8 | 6-1 | 338 | BUY | ALL_IN | 15.0 | 8 | 139 | 5 | 36.0 | Feérico/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.45746034383773804 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 8 | 6-1 | 339 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 8 | 138 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09156456589698792 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 340 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 8 | 138 | 5 | 36.0 | Feérico/DA_18_Zyra | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08299268782138824 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 199 | 158 | 86 | 11 | 7 | 0 | 0 | 0 | 126 | 42.0 |
- Jogador 1 — gasto por ação: BUY: 126g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 5g, stage 2: 36g, stage 3: 51g, stage 4: 47g, stage 5: 19g
| Jogador 2 | 159 | 85 | 35 | 2 | 3 | 0 | 0 | 0 | 141 | 24.0 |
- Jogador 2 — gasto por ação: BUY: 69g, BUY_XP: 16g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 5g, stage 2: 32g, stage 3: 20g, stage 4: 23g, stage 5: 5g
| Jogador 3 | 129 | 66 | 28 | 2 | 0 | 0 | 1 | 0 | 157 | 28.0 |
- Jogador 3 — gasto por ação: BUY: 60g, BUY_XP: 4g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 4g, stage 2: 23g, stage 3: 16g, stage 4: 23g
| Jogador 4 | 160 | 65 | 37 | 4 | 0 | 0 | 0 | 0 | 158 | 24.0 |
- Jogador 4 — gasto por ação: BUY: 65g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 5g, stage 2: 23g, stage 3: 19g, stage 4: 18g
| Jogador 5 | 220 | 217 | 68 | 7 | 15 | 1 | 0 | 0 | 128 | 54.0 |
- Jogador 5 — gasto por ação: BUY: 141g, BUY_XP: 76g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 62g, stage 3: 67g, stage 4: 18g, stage 5: 57g, stage 6: 6g
| Jogador 6 | 208 | 196 | 74 | 7 | 14 | 0 | 4 | 0 | 113 | 38.0 |
- Jogador 6 — gasto por ação: BUY: 124g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 4g, stage 2: 45g, stage 3: 28g, stage 4: 76g, stage 5: 43g
| Jogador 7 | 215 | 160 | 72 | 7 | 7 | 0 | 1 | 0 | 133 | 44.0 |
- Jogador 7 — gasto por ação: BUY: 130g, BUY_XP: 28g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 4g, stage 2: 45g, stage 3: 44g, stage 4: 31g, stage 5: 36g
| Jogador 8 | 234 | 234 | 102 | 13 | 18 | 1 | 4 | 0 | 138 | 36.0 |
- Jogador 8 — gasto por ação: BUY: 142g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 6g, stage 2: 44g, stage 3: 54g, stage 4: 81g, stage 5: 39g, stage 6: 10g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 8 | 13 |
- Jogador 1 · 2-4 · step 88: PASS com 7g, HP 91, nível 5/8 (STABILIZE).
- Jogador 1 · 2-5 · step 96: PASS com 8g, HP 91, nível 5/8 (STABILIZE).
- Jogador 1 · 3-1 · step 127: PASS com 20g, HP 86, nível 5/8 (STABILIZE).
- Jogador 1 · 3-3 · step 147: PASS com 17g, HP 77, nível 6/8 (STABILIZE).
- Jogador 1 · 3-5 · step 169: PASS com 23g, HP 77, nível 6/8 (FAST8).
- Jogador 1 · 3-6 · step 178: PASS com 29g, HP 77, nível 6/8 (FAST8).
- Jogador 1 · 3-7 · step 188: PASS com 34g, HP 64, nível 6/8 (FAST8).
- Jogador 1 · 4-2 · step 209: PASS com 53g, HP 53, nível 6/8 (FAST8).
- Jogador 1 · 4-3 · step 218: PASS com 62g, HP 53, nível 6/8 (FAST8).
- Jogador 1 · 4-4 · step 230: PASS com 73g, HP 42, nível 6/8 (FAST8).
- Jogador 1 · 4-6 · step 245: PASS com 81g, HP 42, nível 7/8 (FAST8).
- Jogador 1 · 5-1 · step 269: PASS com 90g, HP 30, nível 7/8 (STABILIZE).
- Jogador 1 · 5-2 · step 280: PASS com 113g, HP 30, nível 7/8 (STABILIZE).
| Jogador 2 | 4 | 14 |
- Jogador 2 · 2-2 · step 71: PASS com 5g, HP 100, nível 4/8 (STABILIZE).
- Jogador 2 · 2-6 · step 106: PASS com 7g, HP 89, nível 5/8 (STABILIZE).
- Jogador 2 · 2-7 · step 118: PASS com 13g, HP 83, nível 5/8 (STABILIZE).
- Jogador 2 · 3-2 · step 135: PASS com 16g, HP 74, nível 6/8 (STABILIZE).
- Jogador 2 · 3-3 · step 144: PASS com 24g, HP 63, nível 6/8 (STABILIZE).
- Jogador 2 · 3-4 · step 155: PASS com 32g, HP 63, nível 6/8 (STABILIZE).
- Jogador 2 · 3-5 · step 165: PASS com 40g, HP 63, nível 6/8 (STABILIZE).
- Jogador 2 · 3-6 · step 177: PASS com 51g, HP 63, nível 6/8 (STABILIZE).
- Jogador 2 · 3-7 · step 186: PASS com 61g, HP 53, nível 6/8 (STABILIZE).
- Jogador 2 · 4-1 · step 199: PASS com 71g, HP 53, nível 6/8 (STABILIZE).
- Jogador 2 · 4-2 · step 209: PASS com 80g, HP 53, nível 6/8 (STABILIZE).
- Jogador 2 · 4-3 · step 214: PASS com 90g, HP 41, nível 6/8 (STABILIZE).
- Jogador 2 · 4-4 · step 229: PASS com 99g, HP 30, nível 6/8 (STABILIZE).
- Jogador 2 · 5-1 · step 270: PASS com 141g, HP 5, nível 6/8 (ALL_IN).
| Jogador 3 | 1 | 19 |
- Jogador 3 · 2-1 · step 61: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 3 · 2-2 · step 68: PASS com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 3 · 2-3 · step 75: PASS com 10g, HP 95, nível 4/8 (STABILIZE).
- Jogador 3 · 2-5 · step 96: PASS com 14g, HP 89, nível 5/8 (STABILIZE).
- Jogador 3 · 2-6 · step 106: PASS com 20g, HP 89, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 117: PASS com 25g, HP 89, nível 5/8 (STABILIZE).
- Jogador 3 · 3-1 · step 126: PASS com 32g, HP 89, nível 5/8 (STABILIZE).
- Jogador 3 · 3-2 · step 135: PASS com 41g, HP 89, nível 5/8 (STABILIZE).
- Jogador 3 · 3-3 · step 147: PASS com 46g, HP 79, nível 5/8 (STABILIZE).
- Jogador 3 · 3-4 · step 155: PASS com 54g, HP 67, nível 5/8 (STABILIZE).
- Jogador 3 · 3-5 · step 166: PASS com 62g, HP 67, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 180: PASS com 77g, HP 57, nível 5/8 (STABILIZE).
- Jogador 3 · 3-7 · step 186: PASS com 85g, HP 46, nível 6/8 (FAST8).
- Jogador 3 · 4-1 · step 199: PASS com 94g, HP 46, nível 6/8 (FAST8).
- Jogador 3 · 4-2 · step 209: PASS com 107g, HP 34, nível 6/8 (STABILIZE).
- Jogador 3 · 4-3 · step 218: PASS com 120g, HP 23, nível 6/8 (ALL_IN).
- Jogador 3 · 4-4 · step 224: REROLL com 133g, HP 10, nível 6/8 (ALL_IN).
- Jogador 3 · 4-5 · step 238: PASS com 147g, HP 10, nível 6/8 (ALL_IN).
- Jogador 3 · 4-6 · step 248: PASS com 157g, HP 10, nível 6/8 (ALL_IN).
| Jogador 4 | 0 | 13 |
- Jogador 4 · 2-2 · step 70: PASS com 8g, HP 100, nível 4/8 (STABILIZE).
- Jogador 4 · 2-4 · step 86: PASS com 13g, HP 95, nível 4/8 (STABILIZE).
- Jogador 4 · 2-5 · step 97: PASS com 14g, HP 95, nível 4/8 (STABILIZE).
- Jogador 4 · 2-7 · step 119: PASS com 27g, HP 88, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 139: PASS com 38g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-3 · step 150: PASS com 49g, HP 67, nível 5/8 (STABILIZE).
- Jogador 4 · 3-5 · step 169: PASS com 70g, HP 56, nível 5/8 (STABILIZE).
- Jogador 4 · 3-6 · step 177: PASS com 83g, HP 45, nível 5/8 (STABILIZE).
- Jogador 4 · 4-2 · step 208: PASS com 115g, HP 21, nível 6/8 (ALL_IN).
- Jogador 4 · 4-3 · step 217: PASS com 125g, HP 21, nível 6/8 (ALL_IN).
- Jogador 4 · 4-4 · step 228: PASS com 138g, HP 21, nível 6/8 (ALL_IN).
- Jogador 4 · 4-5 · step 236: PASS com 149g, HP 21, nível 6/8 (ALL_IN).
- Jogador 4 · 4-6 · step 248: PASS com 158g, HP 10, nível 6/8 (ALL_IN).
| Jogador 5 | 19 | 9 |
- Jogador 5 · 3-2 · step 136: PASS com 4g, HP 95, nível 6/8 (FAST8).
- Jogador 5 · 3-6 · step 175: PASS com 8g, HP 95, nível 7/8 (FAST8).
- Jogador 5 · 4-1 · step 196: PASS com 8g, HP 95, nível 7/8 (FAST8).
- Jogador 5 · 4-2 · step 207: PASS com 19g, HP 95, nível 7/8 (FAST8).
- Jogador 5 · 4-3 · step 220: PASS com 28g, HP 95, nível 7/8 (FAST8).
- Jogador 5 · 4-4 · step 225: PASS com 36g, HP 95, nível 7/8 (FAST8).
- Jogador 5 · 4-5 · step 236: PASS com 50g, HP 95, nível 7/8 (FAST8).
- Jogador 5 · 4-6 · step 245: PASS com 64g, HP 95, nível 7/8 (FAST8).
- Jogador 5 · 4-7 · step 258: PASS com 78g, HP 95, nível 7/8 (FAST8).
| Jogador 6 | 16 | 21 |
- Jogador 6 · 2-4 · step 89: PASS com 8g, HP 94, nível 5/8 (STABILIZE).
- Jogador 6 · 2-5 · step 97: PASS com 11g, HP 94, nível 5/8 (STABILIZE).
- Jogador 6 · 3-1 · step 127: PASS com 11g, HP 84, nível 6/8 (FAST8).
- Jogador 6 · 3-2 · step 139: PASS com 16g, HP 84, nível 6/8 (FAST8).
- Jogador 6 · 3-3 · step 146: PASS com 19g, HP 84, nível 6/8 (FAST8).
- Jogador 6 · 3-4 · step 160: PASS com 22g, HP 74, nível 6/8 (FAST8).
- Jogador 6 · 3-5 · step 167: PASS com 27g, HP 74, nível 6/8 (FAST8).
- Jogador 6 · 3-6 · step 176: PASS com 32g, HP 62, nível 6/8 (FAST8).
- Jogador 6 · 3-7 · step 187: PASS com 44g, HP 62, nível 6/8 (FAST8).
- Jogador 6 · 4-1 · step 199: PASS com 50g, HP 62, nível 6/8 (FAST8).
- Jogador 6 · 4-2 · step 210: PASS com 53g, HP 62, nível 6/8 (FAST8).
- Jogador 6 · 4-3 · step 218: PASS com 59g, HP 50, nível 6/8 (FAST8).
- Jogador 6 · 4-5 · step 235: PASS com 77g, HP 50, nível 7/8 (FAST8).
- Jogador 6 · 4-7 · step 259: PASS com 59g, HP 38, nível 7/8 (STABILIZE).
- Jogador 6 · 5-1 · step 267: PASS com 66g, HP 38, nível 7/8 (STABILIZE).
- Jogador 6 · 5-2 · step 277: REROLL com 72g, HP 38, nível 7/8 (STABILIZE).
- Jogador 6 · 5-3 · step 286: PASS com 81g, HP 38, nível 7/8 (STABILIZE).
- Jogador 6 · 5-4 · step 296: REROLL com 97g, HP 22, nível 7/8 (ALL_IN).
- Jogador 6 · 5-5 · step 306: REROLL com 112g, HP 22, nível 7/8 (ALL_IN).
- Jogador 6 · 5-5 · step 309: REROLL com 109g, HP 22, nível 7/8 (ALL_IN).
- Jogador 6 · 5-6 · step 318: PASS com 113g, HP 5, nível 7/8 (ALL_IN).
| Jogador 7 | 7 | 13 |
- Jogador 7 · 2-5 · step 96: PASS com 5g, HP 95, nível 5/8 (STABILIZE).
- Jogador 7 · 3-2 · step 135: PASS com 10g, HP 88, nível 5/8 (STABILIZE).
- Jogador 7 · 3-6 · step 179: PASS com 15g, HP 69, nível 6/8 (FAST8).
- Jogador 7 · 4-2 · step 210: PASS com 36g, HP 69, nível 6/8 (FAST8).
- Jogador 7 · 4-3 · step 220: PASS com 51g, HP 69, nível 6/8 (FAST8).
- Jogador 7 · 4-4 · step 227: PASS com 56g, HP 57, nível 6/8 (FAST8).
- Jogador 7 · 4-5 · step 238: PASS com 67g, HP 57, nível 6/8 (FAST8).
- Jogador 7 · 4-6 · step 249: PASS com 75g, HP 45, nível 7/8 (FAST8).
- Jogador 7 · 4-7 · step 256: PASS com 81g, HP 45, nível 7/8 (FAST8).
- Jogador 7 · 5-1 · step 270: PASS com 94g, HP 45, nível 7/8 (FAST8).
- Jogador 7 · 5-2 · step 277: PASS com 101g, HP 28, nível 7/8 (STABILIZE).
- Jogador 7 · 5-3 · step 286: PASS com 107g, HP 12, nível 7/8 (ALL_IN).
- Jogador 7 · 5-5 · step 306: REROLL com 128g, HP 12, nível 7/8 (ALL_IN).
| Jogador 8 | 21 | 9 |
- Jogador 8 · 2-6 · step 108: PASS com 14g, HP 77, nível 5/8 (STABILIZE).
- Jogador 8 · 3-2 · step 139: PASS com 14g, HP 66, nível 6/8 (FAST8).
- Jogador 8 · 3-3 · step 149: PASS com 21g, HP 66, nível 6/8 (FAST8).
- Jogador 8 · 3-4 · step 156: PASS com 30g, HP 66, nível 6/8 (FAST8).
- Jogador 8 · 3-5 · step 167: PASS com 38g, HP 66, nível 6/8 (FAST8).
- Jogador 8 · 3-6 · step 176: PASS com 46g, HP 56, nível 6/8 (FAST8).
- Jogador 8 · 4-1 · step 199: PASS com 42g, HP 56, nível 6/8 (FAST8).
- Jogador 8 · 4-2 · step 207: PASS com 44g, HP 42, nível 7/8 (FAST8).
- Jogador 8 · 4-3 · step 219: PASS com 54g, HP 30, nível 7/8 (STABILIZE).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 2 | 2 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 3 | 3 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 199 | 51 | 48 | 100 | 0.0001 | 0.2141 | -0.0010 | 0.3887 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0433 (58 ações), BUY_XP: Δ 0.0054 (8 ações), CRAFT_AND_EQUIP: Δ 0.0428 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0768 (24 ações), MOVE_BOARD: Δ -0.0001 (52 ações), PASS: Δ 0.0001 (17 ações), SELL: Δ 0.0124 (29 ações)
| Jogador 2 | 159 | 50 | 34 | 75 | 0.0055 | 0.1737 | 0.0029 | 0.3061 | 0.0026 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0178 (39 ações), BUY_XP: Δ 0.0039 (4 ações), CRAFT_AND_EQUIP: Δ 0.0023 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0072 (5 ações), MOVE_BENCH: Δ 0.0051 (36 ações), MOVE_BOARD: Δ 0.0224 (34 ações), PASS: Δ 0.0001 (19 ações), SELL: Δ 0.0368 (15 ações)
| Jogador 3 | 129 | 36 | 39 | 54 | 0.0044 | 0.2171 | 0.0022 | 0.2034 | 0.0022 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0503 (33 ações), BUY_XP: Δ 0.0238 (1 ações), CRAFT_AND_EQUIP: Δ 0.0032 (5 ações), MOVE_BENCH: Δ 0.0577 (22 ações), MOVE_BOARD: Δ 0.0143 (35 ações), PASS: Δ 0.0000 (22 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0420 (10 ações)
| Jogador 4 | 160 | 48 | 54 | 58 | 0.0046 | 0.0469 | 0.0029 | 0.2656 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0487 (44 ações), CRAFT_AND_EQUIP: Δ 0.0131 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0696 (30 ações), MOVE_BOARD: Δ 0.0093 (46 ações), PASS: Δ 0.0000 (17 ações), SELL: Δ 0.0191 (16 ações)
| Jogador 5 | 220 | 60 | 48 | 112 | 0.0024 | 0.2642 | 0.0006 | 0.3799 | 0.0018 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0198 (63 ações), BUY_XP: Δ 0.0074 (19 ações), CRAFT_AND_EQUIP: Δ 0.0080 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0041 (4 ações), MOVE_BENCH: Δ 0.0437 (15 ações), MOVE_BOARD: Δ 0.0087 (63 ações), PASS: Δ 0.0000 (22 ações), SELL: Δ 0.0132 (27 ações)
| Jogador 6 | 208 | 44 | 47 | 117 | 0.0030 | 0.1517 | 0.0011 | 0.3859 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0413 (56 ações), BUY_XP: Δ 0.0045 (16 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0776 (39 ações), MOVE_BOARD: Δ -0.0206 (37 ações), PASS: Δ -0.0009 (22 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0298 (21 ações)
| Jogador 7 | 215 | 59 | 57 | 99 | 0.0012 | 0.2338 | -0.0003 | 0.2800 | 0.0015 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0465 (62 ações), BUY_XP: Δ -0.0095 (7 ações), CRAFT_AND_EQUIP: Δ 0.0046 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0576 (9 ações), MOVE_BENCH: Δ 0.0468 (25 ações), MOVE_BOARD: Δ 0.0109 (62 ações), PASS: Δ 0.0006 (21 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0384 (21 ações)
| Jogador 8 | 234 | 48 | 42 | 144 | 0.0029 | 0.3390 | 0.0021 | 0.2785 | 0.0008 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0250 (67 ações), BUY_XP: Δ 0.0062 (21 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0006 (6 ações), MOVE_BENCH: Δ 0.0511 (16 ações), MOVE_BOARD: Δ 0.0123 (57 ações), PASS: Δ 0.0054 (20 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0167 (36 ações)
- Jogador 1 — rounds avaliados: 28; correlação estrutural/combate: 0.299; posicional/combate: 0.153.
- Jogador 1 — combate positive: score estrutural prévio 0.381
  score posicional prévio 0.428
- Jogador 1 — combate negative: score estrutural prévio 0.146
  score posicional prévio 0.379
- Jogador 2 — rounds avaliados: 26; correlação estrutural/combate: -0.215; posicional/combate: -0.049.
- Jogador 2 — combate positive: score estrutural prévio 0.197
  score posicional prévio 0.281
- Jogador 2 — combate negative: score estrutural prévio 0.298
  score posicional prévio 0.297
- Jogador 3 — rounds avaliados: 24; correlação estrutural/combate: 0.134; posicional/combate: -0.203.
- Jogador 3 — combate positive: score estrutural prévio 0.258
  score posicional prévio 0.170
- Jogador 3 — combate negative: score estrutural prévio 0.175
  score posicional prévio 0.205
- Jogador 4 — rounds avaliados: 24; correlação estrutural/combate: 0.116; posicional/combate: -0.007.
- Jogador 4 — combate positive: score estrutural prévio 0.196
  score posicional prévio 0.272
- Jogador 4 — combate negative: score estrutural prévio 0.091
  score posicional prévio 0.267
- Jogador 5 — rounds avaliados: 33; correlação estrutural/combate: 0.194; posicional/combate: 0.122.
- Jogador 5 — combate positive: score estrutural prévio 0.328
  score posicional prévio 0.398
- Jogador 5 — combate negative: score estrutural prévio 0.186
  score posicional prévio 0.366
- Jogador 6 — rounds avaliados: 31; correlação estrutural/combate: 0.084; posicional/combate: -0.056.
- Jogador 6 — combate positive: score estrutural prévio 0.238
  score posicional prévio 0.382
- Jogador 6 — combate negative: score estrutural prévio 0.132
  score posicional prévio 0.399
- Jogador 7 — rounds avaliados: 31; correlação estrutural/combate: 0.044; posicional/combate: -0.145.
- Jogador 7 — combate positive: score estrutural prévio 0.225
  score posicional prévio 0.273
- Jogador 7 — combate negative: score estrutural prévio 0.185
  score posicional prévio 0.304
- Jogador 8 — rounds avaliados: 33; correlação estrutural/combate: 0.279; posicional/combate: -0.061.
- Jogador 8 — combate positive: score estrutural prévio 0.531
  score posicional prévio 0.267
- Jogador 8 — combate negative: score estrutural prévio 0.261
  score posicional prévio 0.277

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 226 | OK (226) | 4 | 3 | 0 | 0 | 7 | 2 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_IonicSpark, TFT_Item_JeweledGauntlet, TFT_Item_MadredsBloodrazor, TFT_Item_Morellonomicon, TFT_Item_RedBuff; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 184 | OK (184) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 152 | OK (152) | 5 | 0 | 0 | 1 | 5 | 0 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 183 | OK (183) | 5 | 0 | 0 | 1 | 5 | 2 |
- Jogador 4 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_Leviathan, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 253 | OK (253) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 5 — IDs equipados observados: TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_Leviathan, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 238 | OK (238) | 4 | 3 | 0 | 0 | 7 | 2 |
- Jogador 6 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 245 | OK (245) | 6 | 1 | 0 | 0 | 7 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_NightHarvester, TFT_Item_RabadonsDeathcap, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 5); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 266 | OK (266) | 7 | 0 | 1 | 0 | 8 | 3 |
- Jogador 8 — IDs equipados observados: DA_18_EmblemHunter, TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_HextechGunblade, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.147 | 0.000 |
| Jogador 1 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.006 | 0.000 |
| Jogador 1 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 4 | 1 | 3 → 3 | -0.017 | 0.000 |
| Jogador 1 | 1-4 | 8 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 4 → 6 | 2 | 3 → 4 | -0.033 | 0.000 |
| Jogador 1 | 2-1 | 8 | 2.000 | 0.000 | 0 → 0 | 2 → 1 | 11% → 14% | 6 → 9 | 2 | 4 → 4 | -0.040 | -0.289 |
| Jogador 1 | 2-2 | 7 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 10 | 5 | 4 → 4 | 0.104 | -0.339 |
| Jogador 1 | 2-3 | 8 | 2.000 | -2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 10 → 13 | 7 | 4 → 5 | 0.065 | 0.314 |
| Jogador 1 | 2-4 | 8 | 4.000 | 8.000 | 0 → 0 | 2 → 2 | 14% → 18% | 13 → 12 | 6 | 5 → 5 | -0.003 | 0.000 |
| Jogador 1 | 2-5 | 6 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 18% → 18% | 12 → 15 | 4 | 5 → 5 | -0.139 | 0.419 |
| Jogador 1 | 2-6 | 10 | 2.000 | 10.000 | 0 → 0 | 3 → 2 | 18% → 18% | 15 → 13 | 7 | 5 → 5 | 0.033 | -0.237 |
| Jogador 1 | 2-7 | 10 | 2.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 13 → 21 | 5 | 5 → 5 | 0.012 | 0.000 |
| Jogador 1 | 3-1 | 7 | -2.000 | 4.000 | 0 → 0 | 3 → 3 | 18% → 18% | 21 → 28 | 3 | 5 → 5 | -0.001 | -0.370 |
| Jogador 1 | 3-2 | 10 | 2.000 | 8.000 | 0 → 0 | 3 → 2 | 18% → 18% | 28 → 20 | 17 | 5 → 6 | -0.000 | 0.286 |
| Jogador 1 | 3-3 | 7 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 21% | 20 → 25 | 3 | 6 → 6 | 0.043 | 0.402 |
| Jogador 1 | 3-4 | 10 | 0.000 | -4.000 | 0 → 0 | 2 → 3 | 21% → 21% | 25 → 23 | 15 | 6 → 6 | -0.000 | 0.000 |
| Jogador 1 | 3-5 | 9 | 4.000 | -8.000 | 0 → 1 | 3 → 2 | 21% → 21% | 23 → 32 | 3 | 6 → 6 | -0.057 | 0.339 |
| Jogador 1 | 3-6 | 8 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 21% → 21% | 32 → 36 | 4 | 6 → 6 | 0.078 | -0.369 |
| Jogador 1 | 3-7 | 8 | 0.000 | 4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 36 → 42 | 6 | 6 → 6 | -0.061 | 0.000 |
| Jogador 1 | 4-1 | 10 | 6.000 | -4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 42 → 51 | 6 | 6 → 6 | 0.030 | -0.268 |
| Jogador 1 | 4-2 | 9 | 0.000 | -4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 51 → 64 | 4 | 6 → 6 | 0.049 | 0.332 |
| Jogador 1 | 4-3 | 8 | -2.000 | 2.000 | 1 → 1 | 3 → 2 | 21% → 21% | 64 → 72 | 3 | 6 → 6 | -0.035 | -0.328 |
| Jogador 1 | 4-4 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 72 → 83 | 4 | 6 → 6 | 0.007 | 0.000 |
| Jogador 1 | 4-5 | 10 | 2.000 | 2.000 | 1 → 1 | 2 → 3 | 21% → 25% | 83 → 84 | 18 | 6 → 7 | -0.013 | 0.293 |
| Jogador 1 | 4-6 | 5 | 0.000 | 6.000 | 1 → 1 | 3 → 4 | 25% → 25% | 84 → 91 | 3 | 7 → 7 | -0.063 | -0.553 |
| Jogador 1 | 4-7 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 91 → 99 | 9 | 7 → 7 | -0.034 | 0.000 |
| Jogador 1 | 5-1 | 9 | 4.000 | 8.000 | 1 → 1 | 4 → 4 | 25% → 25% | 99 → 101 | 9 | 7 → 7 | 0.121 | 0.329 |
| Jogador 1 | 5-2 | 10 | 0.000 | -16.000 | 1 → 1 | 4 → 5 | 25% → 25% | 101 → 123 | 4 | 7 → 7 | -0.101 | -0.278 |
| Jogador 1 | 5-3 | 10 | -38.000 | -38.000 | 1 → 0 | 5 → 0 | 25% → 0% | 123 → 126 | 6 | 7 → 7 | -0.035 | -0.290 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 12, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 56 ações e piorou em 49.
- Jogador 1 — estado final: ouro 126, nível 7, vida 16.0, colocação 5.
| Jogador 2 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.214 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.050 | 0.000 |
| Jogador 2 | 1-3 | 4 | 0.000 | 0.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 4 | 1 | 3 → 3 | 0.111 | 0.000 |
| Jogador 2 | 1-4 | 6 | 2.000 | 2.000 | 1 → 1 | 0 → 1 | 7% → 11% | 4 → 6 | 2 | 3 → 4 | 0.041 | 0.000 |
| Jogador 2 | 2-1 | 8 | 6.000 | 2.000 | 1 → 1 | 1 → 2 | 11% → 14% | 6 → 8 | 4 | 4 → 4 | 0.003 | 0.314 |
| Jogador 2 | 2-2 | 6 | 0.000 | 4.000 | 1 → 1 | 2 → 1 | 14% → 14% | 8 → 12 | 3 | 4 → 4 | -0.005 | 0.419 |
| Jogador 2 | 2-3 | 8 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 14% → 14% | 12 → 9 | 8 | 4 → 5 | 0.037 | -0.296 |
| Jogador 2 | 2-4 | 10 | 4.000 | 10.000 | 1 → 1 | 1 → 1 | 14% → 18% | 9 → 7 | 7 | 5 → 5 | -0.051 | 0.000 |
| Jogador 2 | 2-5 | 7 | -2.000 | 16.000 | 1 → 0 | 1 → 1 | 18% → 18% | 7 → 6 | 7 | 5 → 5 | 0.031 | -0.354 |
| Jogador 2 | 2-6 | 6 | -2.000 | 2.000 | 0 → 1 | 1 → 2 | 18% → 18% | 6 → 13 | 2 | 5 → 5 | -0.051 | -0.397 |
| Jogador 2 | 2-7 | 8 | 2.000 | -2.000 | 1 → 0 | 2 → 3 | 18% → 18% | 13 → 20 | 1 | 5 → 5 | 0.045 | 0.000 |
| Jogador 2 | 3-1 | 10 | 2.000 | -4.000 | 0 → 0 | 3 → 3 | 18% → 21% | 20 → 17 | 13 | 5 → 6 | 0.013 | -0.254 |
| Jogador 2 | 3-2 | 5 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 17 → 24 | 1 | 6 → 6 | -0.003 | -0.545 |
| Jogador 2 | 3-3 | 4 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 24 → 32 | 0 | 6 → 6 | 0.000 | 0.725 |
| Jogador 2 | 3-4 | 5 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 32 → 40 | 0 | 6 → 6 | 0.010 | 0.000 |
| Jogador 2 | 3-5 | 5 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 40 → 51 | 0 | 6 → 6 | -0.000 | 0.572 |
| Jogador 2 | 3-6 | 7 | 0.000 | 0.000 | 0 → 0 | 4 → 5 | 21% → 21% | 51 → 61 | 3 | 6 → 6 | 0.007 | -0.376 |
| Jogador 2 | 3-7 | 6 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 21% → 21% | 61 → 71 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 9 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 21% → 21% | 71 → 82 | 0 | 6 → 6 | 0.002 | 0.332 |
| Jogador 2 | 4-2 | 9 | 4.000 | -2.000 | 0 → 0 | 5 → 5 | 21% → 21% | 82 → 90 | 5 | 6 → 6 | -0.008 | -0.313 |
| Jogador 2 | 4-3 | 4 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 21% → 21% | 90 → 101 | 0 | 6 → 6 | -0.001 | -0.656 |
| Jogador 2 | 4-4 | 9 | 2.000 | 0.000 | 0 → 0 | 5 → 4 | 21% → 21% | 101 → 110 | 5 | 6 → 6 | -0.013 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 110 → 119 | 8 | 6 → 6 | 0.051 | -0.276 |
| Jogador 2 | 4-6 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 5 | 21% → 21% | 119 → 132 | 2 | 6 → 6 | 0.014 | -0.275 |
| Jogador 2 | 4-7 | 10 | 0.000 | -4.000 | 0 → 0 | 5 → 5 | 21% → 21% | 132 → 145 | 3 | 6 → 6 | -0.009 | 0.000 |
| Jogador 2 | 5-1 | 10 | -24.000 | -36.000 | 0 → 0 | 5 → 0 | 21% → 0% | 145 → 141 | 5 | 6 → 6 | -0.097 | -0.275 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 55 ações e piorou em 36.
- Jogador 2 — estado final: ouro 141, nível 6, vida 5.0, colocação 6.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 3 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.007 | 0.000 |
| Jogador 3 | 1-3 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 7% | 2 → 3 | 2 | 3 → 3 | -0.092 | 0.000 |
| Jogador 3 | 1-4 | 3 | 4.000 | -4.000 | 0 → 1 | 0 → 0 | 7% → 11% | 3 → 7 | 0 | 3 → 4 | 0.065 | 0.000 |
| Jogador 3 | 2-1 | 5 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 11% → 14% | 7 → 10 | 3 | 4 → 4 | -0.015 | 0.537 |
| Jogador 3 | 2-2 | 3 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 10 → 12 | 3 | 4 → 4 | -0.042 | -0.791 |
| Jogador 3 | 2-3 | 3 | 0.000 | 4.000 | 1 → 1 | 1 → 1 | 14% → 14% | 12 → 17 | 2 | 4 → 4 | 0.000 | -0.860 |
| Jogador 3 | 2-4 | 10 | 4.000 | -2.000 | 1 → 1 | 1 → 0 | 14% → 14% | 17 → 18 | 6 | 4 → 5 | 0.039 | 0.000 |
| Jogador 3 | 2-5 | 6 | 6.000 | 2.000 | 1 → 1 | 0 → 1 | 14% → 18% | 18 → 21 | 4 | 5 → 5 | 0.037 | 0.440 |
| Jogador 3 | 2-6 | 6 | 2.000 | -2.000 | 1 → 2 | 1 → 0 | 18% → 18% | 21 → 29 | 1 | 5 → 5 | -0.027 | 0.423 |
| Jogador 3 | 2-7 | 7 | 0.000 | 8.000 | 2 → 2 | 0 → 1 | 18% → 18% | 29 → 33 | 4 | 5 → 5 | 0.005 | 0.000 |
| Jogador 3 | 3-1 | 6 | 0.000 | 2.000 | 2 → 2 | 1 → 2 | 18% → 18% | 33 → 42 | 1 | 5 → 5 | 0.002 | 0.461 |
| Jogador 3 | 3-2 | 5 | 0.000 | 0.000 | 2 → 2 | 2 → 1 | 18% → 18% | 42 → 50 | 1 | 5 → 5 | -0.014 | -0.537 |
| Jogador 3 | 3-3 | 7 | 0.000 | 8.000 | 2 → 2 | 1 → 1 | 18% → 18% | 50 → 56 | 4 | 5 → 5 | 0.018 | -0.416 |
| Jogador 3 | 3-4 | 5 | 0.000 | 4.000 | 2 → 2 | 1 → 2 | 18% → 18% | 56 → 65 | 2 | 5 → 5 | -0.065 | 0.000 |
| Jogador 3 | 3-5 | 6 | 0.000 | 6.000 | 2 → 2 | 2 → 2 | 18% → 18% | 65 → 73 | 3 | 5 → 5 | -0.007 | -0.455 |
| Jogador 3 | 3-6 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 3 | 18% → 18% | 73 → 88 | 2 | 5 → 6 | 0.041 | -0.283 |
| Jogador 3 | 3-7 | 6 | 4.000 | 2.000 | 2 → 2 | 3 → 3 | 18% → 21% | 88 → 96 | 3 | 6 → 6 | -0.003 | 0.000 |
| Jogador 3 | 4-1 | 9 | 2.000 | 2.000 | 2 → 2 | 3 → 4 | 21% → 21% | 96 → 106 | 3 | 6 → 6 | 0.005 | -0.313 |
| Jogador 3 | 4-2 | 9 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 21% → 21% | 106 → 120 | 2 | 6 → 6 | 0.006 | -0.297 |
| Jogador 3 | 4-3 | 8 | 2.000 | -2.000 | 2 → 2 | 5 → 4 | 21% → 21% | 120 → 133 | 3 | 6 → 6 | -0.005 | -0.356 |
| Jogador 3 | 4-4 | 10 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 21% → 21% | 133 → 145 | 10 | 6 → 6 | 0.003 | 0.000 |
| Jogador 3 | 4-5 | 8 | -2.000 | -2.000 | 2 → 2 | 5 → 5 | 21% → 21% | 145 → 158 | 1 | 6 → 6 | -0.001 | 0.356 |
| Jogador 3 | 4-6 | 8 | -28.000 | -32.000 | 2 → 0 | 5 → 0 | 21% → 0% | 158 → 157 | 4 | 6 → 6 | -0.076 | -0.367 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 11, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 40 ações e piorou em 41.
- Jogador 3 — estado final: ouro 157, nível 6, vida 10.0, colocação 8.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 4 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 4 | 1-3 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 5 | 0 | 3 → 3 | -0.006 | 0.000 |
| Jogador 4 | 1-4 | 8 | 0.000 | 6.000 | 0 → 0 | 0 → 2 | 11% → 11% | 5 → 6 | 3 | 3 → 4 | 0.028 | 0.000 |
| Jogador 4 | 2-1 | 8 | 2.000 | 2.000 | 0 → 0 | 2 → 3 | 11% → 14% | 6 → 10 | 2 | 4 → 4 | -0.017 | 0.304 |
| Jogador 4 | 2-2 | 5 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 14% → 14% | 10 → 13 | 2 | 4 → 4 | -0.063 | -0.464 |
| Jogador 4 | 2-3 | 8 | 2.000 | 0.000 | 0 → 1 | 3 → 1 | 14% → 14% | 13 → 17 | 3 | 4 → 4 | 0.071 | 0.330 |
| Jogador 4 | 2-4 | 6 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 14% → 14% | 17 → 19 | 4 | 4 → 4 | -0.119 | 0.000 |
| Jogador 4 | 2-5 | 7 | 0.000 | 10.000 | 1 → 1 | 1 → 3 | 14% → 14% | 19 → 20 | 5 | 4 → 5 | -0.038 | -0.384 |
| Jogador 4 | 2-6 | 10 | 2.000 | -4.000 | 1 → 1 | 3 → 4 | 14% → 18% | 20 → 30 | 4 | 5 → 5 | 0.052 | 0.251 |
| Jogador 4 | 2-7 | 9 | 2.000 | 0.000 | 1 → 2 | 4 → 2 | 18% → 18% | 30 → 34 | 3 | 5 → 5 | 0.082 | 0.000 |
| Jogador 4 | 3-1 | 10 | -2.000 | 4.000 | 2 → 1 | 2 → 2 | 18% → 18% | 34 → 41 | 1 | 5 → 5 | -0.017 | -0.259 |
| Jogador 4 | 3-2 | 9 | 6.000 | -2.000 | 1 → 2 | 2 → 2 | 18% → 18% | 41 → 47 | 3 | 5 → 5 | 0.003 | -0.324 |
| Jogador 4 | 3-3 | 10 | 0.000 | -2.000 | 2 → 2 | 2 → 2 | 18% → 18% | 47 → 59 | 1 | 5 → 5 | -0.127 | -0.273 |
| Jogador 4 | 3-4 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 3 | 18% → 18% | 59 → 71 | 2 | 5 → 5 | 0.042 | 0.000 |
| Jogador 4 | 3-5 | 9 | 0.000 | -2.000 | 2 → 2 | 3 → 2 | 18% → 18% | 71 → 81 | 4 | 5 → 5 | 0.016 | -0.319 |
| Jogador 4 | 3-6 | 7 | 0.000 | -2.000 | 2 → 2 | 2 → 4 | 18% → 18% | 81 → 95 | 3 | 5 → 5 | -0.023 | -0.409 |
| Jogador 4 | 3-7 | 10 | 4.000 | 0.000 | 2 → 2 | 4 → 3 | 18% → 18% | 95 → 103 | 5 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 10 | 0.000 | -2.000 | 2 → 2 | 3 → 4 | 18% → 18% | 103 → 118 | 2 | 5 → 6 | 0.060 | -0.276 |
| Jogador 4 | 4-2 | 8 | 2.000 | 4.000 | 2 → 2 | 4 → 4 | 18% → 21% | 118 → 126 | 4 | 6 → 6 | -0.019 | 0.356 |
| Jogador 4 | 4-3 | 7 | 0.000 | 2.000 | 2 → 2 | 4 → 4 | 21% → 21% | 126 → 137 | 3 | 6 → 6 | -0.039 | 0.400 |
| Jogador 4 | 4-4 | 8 | 0.000 | -2.000 | 2 → 2 | 4 → 4 | 21% → 21% | 137 → 149 | 4 | 6 → 6 | -0.007 | 0.000 |
| Jogador 4 | 4-5 | 6 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 21% → 21% | 149 → 159 | 2 | 6 → 6 | 0.040 | -0.446 |
| Jogador 4 | 4-6 | 8 | -24.000 | -24.000 | 2 → 0 | 4 → 0 | 21% → 0% | 159 → 158 | 3 | 6 → 6 | -0.052 | -0.352 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 52 ações e piorou em 55.
- Jogador 4 — estado final: ouro 158, nível 6, vida 10.0, colocação 7.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.149 | 0.000 |
| Jogador 5 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.013 | 0.000 |
| Jogador 5 | 1-4 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.024 | 0.000 |
| Jogador 5 | 2-1 | 8 | 4.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | 0.025 | -0.296 |
| Jogador 5 | 2-2 | 7 | 0.000 | 10.000 | 0 → 0 | 1 → 0 | 14% → 14% | 6 → 7 | 7 | 4 → 4 | -0.084 | 0.366 |
| Jogador 5 | 2-3 | 8 | 6.000 | -8.000 | 0 → 0 | 0 → 0 | 14% → 18% | 7 → 7 | 10 | 4 → 5 | 0.019 | 0.342 |
| Jogador 5 | 2-4 | 10 | 0.000 | 10.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 8 | 5 | 5 → 5 | 0.001 | 0.000 |
| Jogador 5 | 2-5 | 10 | 0.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 9 | 11 | 5 → 5 | 0.103 | 0.264 |
| Jogador 5 | 2-6 | 10 | 6.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 21% | 9 → 7 | 12 | 5 → 6 | -0.012 | 0.270 |
| Jogador 5 | 2-7 | 10 | -4.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 18% | 7 → 6 | 13 | 6 → 6 | 0.033 | 0.000 |
| Jogador 5 | 3-1 | 10 | 6.000 | 4.000 | 0 → 0 | 0 → 1 | 18% → 21% | 6 → 9 | 6 | 6 → 6 | -0.013 | 0.305 |
| Jogador 5 | 3-2 | 6 | 0.000 | 10.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 13 | 5 | 6 → 6 | -0.114 | 0.514 |
| Jogador 5 | 3-3 | 8 | 0.000 | 14.000 | 0 → 0 | 2 → 1 | 21% → 21% | 13 → 9 | 13 | 6 → 6 | -0.041 | 0.385 |
| Jogador 5 | 3-4 | 10 | 6.000 | -12.000 | 0 → 0 | 1 → 1 | 21% → 25% | 9 → 8 | 14 | 6 → 7 | 0.013 | 0.000 |
| Jogador 5 | 3-5 | 9 | 0.000 | 14.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 10 | 7 | 7 → 7 | 0.121 | 0.332 |
| Jogador 5 | 3-6 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 25% → 25% | 10 → 17 | 2 | 7 → 7 | -0.062 | 0.622 |
| Jogador 5 | 3-7 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 17 → 8 | 20 | 7 → 7 | 0.008 | 0.000 |
| Jogador 5 | 4-1 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 8 → 17 | 0 | 7 → 7 | -0.016 | 0.523 |
| Jogador 5 | 4-2 | 7 | 0.000 | -2.000 | 0 → 0 | 2 → 3 | 25% → 25% | 17 → 30 | 3 | 7 → 7 | 0.013 | 0.426 |
| Jogador 5 | 4-3 | 10 | 6.000 | -8.000 | 0 → 1 | 3 → 4 | 25% → 25% | 30 → 39 | 8 | 7 → 7 | 0.050 | 0.301 |
| Jogador 5 | 4-4 | 5 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 39 → 47 | 3 | 7 → 7 | -0.092 | 0.000 |
| Jogador 5 | 4-5 | 6 | 0.000 | -6.000 | 1 → 1 | 4 → 5 | 25% → 25% | 47 → 64 | 1 | 7 → 7 | 0.001 | 0.489 |
| Jogador 5 | 4-6 | 5 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 25% → 25% | 64 → 78 | 0 | 7 → 7 | 0.055 | 0.617 |
| Jogador 5 | 4-7 | 8 | 2.000 | -6.000 | 1 → 1 | 5 → 4 | 25% → 25% | 78 → 91 | 3 | 7 → 7 | -0.072 | 0.000 |
| Jogador 5 | 5-1 | 10 | -10.000 | 12.000 | 1 → 1 | 4 → 4 | 25% → 21% | 91 → 98 | 8 | 7 → 7 | 0.004 | -0.280 |
| Jogador 5 | 5-2 | 10 | 0.000 | -6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 98 → 106 | 11 | 7 → 7 | -0.031 | 0.294 |
| Jogador 5 | 5-3 | 10 | 8.000 | 2.000 | 1 → 1 | 4 → 3 | 21% → 25% | 106 → 105 | 17 | 7 → 8 | 0.003 | 0.297 |
| Jogador 5 | 5-4 | 7 | 6.000 | -2.000 | 1 → 1 | 3 → 4 | 25% → 29% | 105 → 114 | 3 | 8 → 8 | 0.030 | 0.000 |
| Jogador 5 | 5-5 | 5 | 0.000 | 8.000 | 1 → 1 | 4 → 5 | 29% → 29% | 114 → 122 | 4 | 8 → 8 | 0.017 | 0.591 |
| Jogador 5 | 5-6 | 8 | 0.000 | -4.000 | 1 → 1 | 5 → 4 | 29% → 29% | 122 → 133 | 4 | 8 → 8 | -0.004 | 0.371 |
| Jogador 5 | 5-7 | 9 | 10.000 | -4.000 | 1 → 3 | 4 → 2 | 29% → 29% | 133 → 134 | 10 | 8 → 8 | 0.010 | 0.000 |
| Jogador 5 | 6-1 | 7 | 0.000 | 12.000 | 3 → 3 | 2 → 2 | 29% → 29% | 134 → 129 | 6 | 8 → 8 | 0.007 | 0.435 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 17, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 65 ações e piorou em 48.
- Jogador 5 — estado final: ouro 129, nível 8, vida 82.0, colocação 1.
| Jogador 6 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.014 | 0.000 |
| Jogador 6 | 1-2 | 6 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.020 | 0.000 |
| Jogador 6 | 1-3 | 3 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 7% → 11% | 2 → 5 | 0 | 3 → 3 | 0.054 | 0.000 |
| Jogador 6 | 1-4 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 5 → 7 | 2 | 3 → 4 | 0.056 | 0.000 |
| Jogador 6 | 2-1 | 8 | 2.000 | 4.000 | 0 → 0 | 2 → 4 | 11% → 14% | 7 → 9 | 3 | 4 → 4 | 0.034 | -0.316 |
| Jogador 6 | 2-2 | 6 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 14% → 14% | 9 → 8 | 7 | 4 → 4 | -0.164 | 0.410 |
| Jogador 6 | 2-3 | 8 | 6.000 | -6.000 | 0 → 0 | 4 → 2 | 14% → 18% | 8 → 11 | 8 | 4 → 5 | 0.057 | 0.314 |
| Jogador 6 | 2-4 | 9 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 11 → 14 | 3 | 5 → 5 | 0.048 | 0.000 |
| Jogador 6 | 2-5 | 7 | 2.000 | 2.000 | 0 → 1 | 2 → 1 | 18% → 18% | 14 → 17 | 3 | 5 → 5 | -0.084 | -0.339 |
| Jogador 6 | 2-6 | 10 | 4.000 | 8.000 | 1 → 1 | 1 → 1 | 18% → 18% | 17 → 9 | 14 | 5 → 5 | -0.026 | -0.237 |
| Jogador 6 | 2-7 | 10 | 2.000 | 2.000 | 1 → 1 | 1 → 1 | 18% → 18% | 9 → 14 | 7 | 5 → 6 | 0.112 | 0.000 |
| Jogador 6 | 3-1 | 7 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 14 → 18 | 3 | 6 → 6 | 0.006 | 0.388 |
| Jogador 6 | 3-2 | 9 | 0.000 | 4.000 | 1 → 1 | 1 → 3 | 21% → 21% | 18 → 24 | 2 | 6 → 6 | -0.029 | 0.307 |
| Jogador 6 | 3-3 | 6 | 0.000 | 10.000 | 1 → 1 | 3 → 5 | 21% → 21% | 24 → 25 | 5 | 6 → 6 | -0.074 | -0.439 |
| Jogador 6 | 3-4 | 10 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 21% → 21% | 25 → 29 | 7 | 6 → 6 | 0.103 | 0.000 |
| Jogador 6 | 3-5 | 7 | 0.000 | -2.000 | 1 → 1 | 5 → 4 | 21% → 21% | 29 → 35 | 3 | 6 → 6 | -0.009 | -0.402 |
| Jogador 6 | 3-6 | 6 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 35 → 41 | 3 | 6 → 6 | 0.000 | 0.500 |
| Jogador 6 | 3-7 | 7 | 0.000 | -6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 41 → 53 | 5 | 6 → 6 | -0.147 | 0.000 |
| Jogador 6 | 4-1 | 9 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 53 → 62 | 3 | 6 → 6 | 0.114 | 0.317 |
| Jogador 6 | 4-2 | 10 | 2.000 | 10.000 | 1 → 1 | 4 → 4 | 21% → 21% | 62 → 63 | 9 | 6 → 6 | -0.048 | -0.276 |
| Jogador 6 | 4-3 | 8 | 0.000 | -6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 63 → 70 | 9 | 6 → 6 | 0.010 | 0.350 |
| Jogador 6 | 4-4 | 10 | 6.000 | -16.000 | 1 → 1 | 4 → 5 | 21% → 25% | 70 → 79 | 12 | 6 → 7 | 0.029 | 0.000 |
| Jogador 6 | 4-5 | 5 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 25% → 25% | 79 → 87 | 2 | 7 → 7 | 0.080 | -0.543 |
| Jogador 6 | 4-6 | 10 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 25% → 25% | 87 → 67 | 32 | 7 → 7 | 0.000 | 0.293 |
| Jogador 6 | 4-7 | 9 | 0.000 | 4.000 | 1 → 1 | 5 → 3 | 25% → 25% | 67 → 69 | 9 | 7 → 7 | -0.063 | 0.000 |
| Jogador 6 | 5-1 | 7 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 69 → 78 | 3 | 7 → 7 | -0.006 | 0.417 |
| Jogador 6 | 5-2 | 10 | -6.000 | 0.000 | 1 → 1 | 3 → 2 | 25% → 21% | 78 → 85 | 12 | 7 → 7 | 0.002 | 0.000 |
| Jogador 6 | 5-3 | 6 | 8.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 25% | 85 → 91 | 4 | 7 → 7 | -0.002 | -0.467 |
| Jogador 6 | 5-4 | 10 | 0.000 | -18.000 | 1 → 1 | 2 → 3 | 25% → 25% | 91 → 112 | 5 | 7 → 7 | 0.016 | 0.000 |
| Jogador 6 | 5-5 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 5 | 25% → 25% | 112 → 121 | 11 | 7 → 7 | 0.000 | -0.275 |
| Jogador 6 | 5-6 | 8 | -38.000 | -34.000 | 1 → 0 | 5 → 0 | 25% → 0% | 121 → 113 | 8 | 7 → 7 | -0.111 | -0.350 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 20; mudanças de composição: 1; posicionamento melhorou em 47 ações e piorou em 48.
- Jogador 6 — estado final: ouro 113, nível 7, vida 5.0, colocação 4.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.044 | 0.000 |
| Jogador 7 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | -0.020 | 0.000 |
| Jogador 7 | 1-4 | 7 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 5 → 7 | 2 | 3 → 4 | 0.023 | 0.000 |
| Jogador 7 | 2-1 | 8 | 2.000 | 8.000 | 0 → 0 | 2 → 2 | 11% → 14% | 7 → 8 | 5 | 4 → 4 | -0.033 | 0.330 |
| Jogador 7 | 2-2 | 7 | 6.000 | 0.000 | 0 → 0 | 2 → 1 | 14% → 14% | 8 → 11 | 4 | 4 → 4 | 0.001 | 0.359 |
| Jogador 7 | 2-3 | 8 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 14% | 11 → 10 | 9 | 4 → 5 | -0.021 | -0.296 |
| Jogador 7 | 2-4 | 7 | 10.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 18% | 10 → 8 | 7 | 5 → 5 | 0.126 | 0.000 |
| Jogador 7 | 2-5 | 6 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 11 | 3 | 5 → 5 | 0.043 | 0.476 |
| Jogador 7 | 2-6 | 10 | 0.000 | 10.000 | 0 → 0 | 1 → 3 | 18% → 18% | 11 → 7 | 9 | 5 → 5 | -0.104 | -0.254 |
| Jogador 7 | 2-7 | 9 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 18% → 18% | 7 → 7 | 8 | 5 → 5 | 0.126 | 0.000 |
| Jogador 7 | 3-1 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 18% | 7 → 12 | 2 | 5 → 5 | -0.027 | 0.277 |
| Jogador 7 | 3-2 | 5 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 12 → 16 | 2 | 5 → 6 | -0.126 | -0.517 |
| Jogador 7 | 3-3 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 18% → 18% | 16 → 9 | 17 | 6 → 6 | 0.107 | -0.254 |
| Jogador 7 | 3-4 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 2 | 18% → 21% | 9 → 8 | 10 | 6 → 6 | -0.098 | 0.000 |
| Jogador 7 | 3-5 | 6 | 0.000 | 10.000 | 0 → 0 | 2 → 4 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | 0.000 | 0.485 |
| Jogador 7 | 3-6 | 9 | 0.000 | -8.000 | 0 → 0 | 4 → 5 | 21% → 21% | 9 → 23 | 2 | 6 → 6 | 0.084 | 0.312 |
| Jogador 7 | 3-7 | 10 | -2.000 | 4.000 | 0 → 0 | 5 → 4 | 21% → 21% | 23 → 26 | 6 | 6 → 6 | -0.030 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | -10.000 | 0 → 0 | 4 → 3 | 21% → 21% | 26 → 41 | 3 | 6 → 6 | -0.000 | 0.293 |
| Jogador 7 | 4-2 | 10 | -2.000 | 8.000 | 0 → 0 | 3 → 2 | 21% → 21% | 41 → 46 | 5 | 6 → 6 | -0.043 | 0.293 |
| Jogador 7 | 4-3 | 10 | 4.000 | -18.000 | 0 → 0 | 2 → 1 | 21% → 21% | 46 → 61 | 5 | 6 → 6 | 0.029 | -0.276 |
| Jogador 7 | 4-4 | 7 | 0.000 | 10.000 | 0 → 0 | 1 → 2 | 21% → 21% | 61 → 66 | 5 | 6 → 6 | 0.070 | 0.000 |
| Jogador 7 | 4-5 | 8 | 0.000 | 0.000 | 0 → 0 | 2 → 4 | 21% → 21% | 66 → 78 | 4 | 6 → 7 | -0.030 | -0.346 |
| Jogador 7 | 4-6 | 9 | 12.000 | -12.000 | 0 → 1 | 4 → 3 | 21% → 25% | 78 → 86 | 4 | 7 → 7 | 0.014 | 0.332 |
| Jogador 7 | 4-7 | 6 | 0.000 | 10.000 | 1 → 1 | 3 → 4 | 25% → 25% | 86 → 91 | 5 | 7 → 7 | -0.009 | 0.000 |
| Jogador 7 | 5-1 | 10 | 0.000 | -4.000 | 1 → 1 | 4 → 5 | 25% → 25% | 91 → 104 | 2 | 7 → 7 | 0.000 | -0.280 |
| Jogador 7 | 5-2 | 7 | 0.000 | -2.000 | 1 → 1 | 5 → 3 | 25% → 25% | 104 → 112 | 4 | 7 → 7 | 0.002 | -0.400 |
| Jogador 7 | 5-3 | 6 | 0.000 | 10.000 | 1 → 1 | 3 → 4 | 25% → 25% | 112 → 118 | 5 | 7 → 7 | -0.010 | 0.000 |
| Jogador 7 | 5-4 | 10 | 6.000 | -2.000 | 1 → 2 | 4 → 4 | 25% → 25% | 118 → 128 | 6 | 7 → 7 | 0.011 | 0.000 |
| Jogador 7 | 5-5 | 10 | -6.000 | 10.000 | 2 → 1 | 4 → 3 | 25% → 25% | 128 → 135 | 9 | 7 → 7 | -0.017 | 0.294 |
| Jogador 7 | 5-6 | 10 | -44.000 | -46.000 | 1 → 0 | 3 → 0 | 25% → 0% | 135 → 133 | 10 | 7 → 7 | -0.071 | -0.280 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 13, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 65 ações e piorou em 60.
- Jogador 7 — estado final: ouro 133, nível 7, vida 12.0, colocação 3.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.150 | 0.000 |
| Jogador 8 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 8 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 4 | 1 | 3 → 3 | 0.004 | 0.000 |
| Jogador 8 | 1-4 | 10 | 0.000 | 6.000 | 0 → 0 | 0 → 2 | 11% → 11% | 4 → 5 | 3 | 3 → 4 | -0.035 | 0.000 |
| Jogador 8 | 2-1 | 8 | 4.000 | 0.000 | 0 → 1 | 2 → 0 | 11% → 14% | 5 → 6 | 4 | 4 → 4 | -0.018 | -0.310 |
| Jogador 8 | 2-2 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 9 | 3 | 4 → 4 | -0.021 | -0.404 |
| Jogador 8 | 2-3 | 8 | 0.000 | 12.000 | 1 → 1 | 0 → 2 | 14% → 14% | 9 → 9 | 6 | 4 → 4 | 0.123 | -0.310 |
| Jogador 8 | 2-4 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 14% → 14% | 9 → 18 | 6 | 4 → 4 | -0.024 | 0.000 |
| Jogador 8 | 2-5 | 10 | 2.000 | 0.000 | 1 → 0 | 2 → 1 | 14% → 14% | 18 → 21 | 11 | 4 → 5 | 0.023 | -0.248 |
| Jogador 8 | 2-6 | 8 | 4.000 | 10.000 | 0 → 0 | 1 → 1 | 14% → 18% | 21 → 21 | 7 | 5 → 5 | 0.033 | 0.314 |
| Jogador 8 | 2-7 | 10 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 18% → 18% | 21 → 27 | 7 | 5 → 5 | -0.101 | 0.000 |
| Jogador 8 | 3-1 | 10 | 4.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 27 → 23 | 14 | 5 → 5 | -0.007 | -0.288 |
| Jogador 8 | 3-2 | 9 | 6.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 21% | 23 → 21 | 9 | 5 → 6 | 0.009 | 0.322 |
| Jogador 8 | 3-3 | 9 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 21 → 30 | 1 | 6 → 6 | 0.002 | 0.302 |
| Jogador 8 | 3-4 | 6 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 30 → 39 | 0 | 6 → 6 | 0.137 | 0.000 |
| Jogador 8 | 3-5 | 7 | 0.000 | 2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 39 → 46 | 3 | 6 → 6 | 0.035 | -0.383 |
| Jogador 8 | 3-6 | 6 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 46 → 56 | 3 | 6 → 6 | -0.031 | 0.506 |
| Jogador 8 | 3-7 | 10 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 56 → 42 | 24 | 6 → 6 | -0.000 | 0.000 |
| Jogador 8 | 4-1 | 9 | 0.000 | -2.000 | 0 → 0 | 4 → 3 | 21% → 21% | 42 → 51 | 3 | 6 → 7 | -0.015 | -0.331 |
| Jogador 8 | 4-2 | 7 | 6.000 | 8.000 | 0 → 0 | 3 → 4 | 21% → 25% | 51 → 54 | 7 | 7 → 7 | -0.022 | -0.402 |
| Jogador 8 | 4-3 | 9 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 54 → 65 | 3 | 7 → 7 | 0.027 | 0.326 |
| Jogador 8 | 4-4 | 10 | 0.000 | -6.000 | 0 → 0 | 4 → 6 | 25% → 25% | 65 → 62 | 20 | 7 → 7 | 0.001 | 0.000 |
| Jogador 8 | 4-5 | 10 | -2.000 | 0.000 | 0 → 0 | 6 → 4 | 25% → 25% | 62 → 72 | 7 | 7 → 7 | -0.006 | 0.288 |
| Jogador 8 | 4-6 | 10 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 72 → 52 | 31 | 7 → 7 | -0.006 | 0.291 |
| Jogador 8 | 4-7 | 10 | 6.000 | -12.000 | 0 → 0 | 4 → 5 | 25% → 29% | 52 → 64 | 10 | 7 → 8 | 0.035 | 0.000 |
| Jogador 8 | 5-1 | 7 | 6.000 | 2.000 | 0 → 0 | 5 → 5 | 29% → 29% | 64 → 72 | 4 | 8 → 8 | 0.018 | 0.426 |
| Jogador 8 | 5-2 | 7 | 0.000 | 0.000 | 0 → 0 | 5 → 6 | 29% → 29% | 72 → 85 | 3 | 8 → 8 | 0.004 | 0.425 |
| Jogador 8 | 5-3 | 4 | 0.000 | 0.000 | 0 → 0 | 6 → 6 | 29% → 29% | 85 → 99 | 0 | 8 → 8 | -0.054 | 0.768 |
| Jogador 8 | 5-4 | 9 | 0.000 | 4.000 | 0 → 0 | 6 → 6 | 29% → 29% | 99 → 105 | 10 | 8 → 8 | -0.007 | 0.000 |
| Jogador 8 | 5-5 | 6 | 0.000 | -10.000 | 0 → 0 | 6 → 6 | 29% → 29% | 105 → 122 | 1 | 8 → 8 | 0.015 | -0.467 |
| Jogador 8 | 5-6 | 10 | -6.000 | 2.000 | 0 → 0 | 6 → 4 | 29% → 25% | 122 → 132 | 11 | 8 → 8 | -0.023 | 0.296 |
| Jogador 8 | 5-7 | 10 | 2.000 | -12.000 | 0 → 0 | 4 → 4 | 25% → 29% | 132 → 145 | 10 | 8 → 8 | -0.003 | 0.000 |
| Jogador 8 | 6-1 | 10 | -38.000 | -28.000 | 0 → 0 | 4 → 0 | 29% → 0% | 145 → 138 | 10 | 8 → 8 | -0.081 | -0.285 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 19; mudanças de composição: 2; posicionamento melhorou em 51 ações e piorou em 43.
- Jogador 8 — estado final: ouro 138, nível 8, vida 15.0, colocação 2.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 58 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| Jogador 2 | 39 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Jogador 3 | 33 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Jogador 4 | 44 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Jogador 5 | 63 | 27 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 2 | 1 | 0 |
| Jogador 6 | 56 | 21 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| Jogador 7 | 62 | 21 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 8 | 67 | 36 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 1 | 0 |
- Jogador 1 — venda DA_18_Akali_AD (2-7, step 112): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Gromp18_AP (3-4, step 152): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Warwick (3-7, step 182): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Shen (4-4, step 223): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Cassiopeia (5-2, step 272): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_KogMaw18_AD (5-2, step 275): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_Krug18 (5-3, step 284): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Veigar (2-6, step 102): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Veigar (3-1, step 123): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-4, step 222): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Sejuani (4-5, step 232): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 2 — venda DA_18_RekSai (4-6, step 242): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Karma18 (5-1, step 265): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 3 — venda DA_18_RekSai (3-6, step 174): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_KhaZix (4-3, step 212): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Akali_AD (2-6, step 102): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Veigar (2-6, step 106): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Sejuani (3-6, step 173): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Camille (3-7, step 182): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 4 — venda DA_18_Camille (4-2, step 204): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (2-7, step 118): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Yunara (3-4, step 153): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_LeBlanc (4-2, step 202): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Sejuani (5-1, step 265): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Tristana (5-2, step 272): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Leona (5-3, step 284): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-7, step 117): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=True, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rakan (3-4, step 154): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rammus (3-7, step 183): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_Teemo (4-3, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Tristana (4-4, step 222): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Sentry (4-6, step 242): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rammus (5-2, step 278): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_18_MasterYi_AD (5-4, step 292): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (5-4, step 297): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Diana (5-5, step 310): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Akali_AD (2-7, step 113): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (3-6, step 172): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Shen (3-7, step 182): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_Fiddlesticks18 (4-1, step 194): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Warwick (4-3, step 214): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_LeBlanc (4-5, step 233): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Ornn (5-5, step 304): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Murkwolf18 (5-6, step 312): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_Karma18 (2-5, step 96): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Akali_AD (3-7, step 182): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Vi18 (4-1, step 194): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Veigar (4-3, step 212): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Warwick (4-5, step 232): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_Vi18 (4-5, step 234): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Tristana (4-7, step 252): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Diana (5-4, step 292): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Fiddlesticks18 (5-5, step 302): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Warwick (5-6, step 312): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Diana (5-7, step 322): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (6-1, step 337): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **6**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-7 | 112 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 3-4 | 152 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-7 | 182 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-4 | 223 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-2 | 272 | SOLD_CORE_UNIT | Venda de 'DA_18_Cassiopeia' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 5-2 | 275 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 5-3 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 1-4 | 282 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-1 | 394 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-5 | 802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-5 | 803 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 938 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 939 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1081 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-7 | 1082 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1178 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1179 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1313 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1314 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1545 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1546 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1670 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1671 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1779 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1780 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1889 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 1890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2028 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 2029 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2272 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2273 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2414 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2415 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2547 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2548 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2762 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-1 | 2890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-1 | 2891 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 3029 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-2 | 3030 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 3169 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-3 | 3170 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 2-7 | 1155 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 3-2 | 1390 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-7 | 2867 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-1 | 3006 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 2 | 3-1 | 123 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-6 | 242 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 45 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-3 | 187 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 2-4 | 718 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-4 | 719 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-5 | 816 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-6 | 902 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-6 | 903 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 2-7 | 1016 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-1 | 1151 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-2 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 1610 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 1735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 1861 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 2619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 5-1 | 2620 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-6 | 993 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-1 | 1201 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-2 | 1260 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-3 | 1333 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-4 | 1404 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-5 | 1501 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-6 | 1587 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-7 | 1712 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-1 | 1838 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-2 | 1898 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-3 | 2026 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-6 | 174 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 4-3 | 212 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 3 | 1-3 | 186 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 1-4 | 233 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-1 | 304 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-2 | 351 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-3 | 399 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-4 | 534 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 708 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 971 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1072 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1147 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1235 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 1722 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 1836 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-4 | 1972 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2087 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2205 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 4-6 | 2206 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 2-2 | 376 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-4 | 598 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-5 | 685 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-6 | 784 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 2-7 | 870 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-1 | 948 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-2 | 1049 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1124 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-4 | 1212 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-5 | 1355 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-1 | 1699 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 4 | 2-6 | 102 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 3-6 | 173 | SOLD_CORE_UNIT | Venda de 'DA_18_Sejuani' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 4-2 | 204 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 4 | 2-5 | 754 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1429 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-4 | 1569 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1692 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-6 | 1790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 1929 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2289 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2400 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-6 | 2603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-6 | 2604 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-3 | 633 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-4 | 731 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-6 | 997 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-1 | 1264 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-2 | 1406 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-4 | 1669 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-5 | 1767 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-3 | 77 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Kobuko) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 2-3 | 78 | PURCHASE_SALE_REVIEW | Compra de DA_18_Rakan foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 2-5 | 97 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 105 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 5 | 2-7 | 118 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 4-2 | 202 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-2 | 272 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-3 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Leona' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-1 | 382 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-2 | 482 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-2 | 483 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-3 | 593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-3 | 594 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-4 | 726 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 727 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-5 | 859 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 860 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-6 | 990 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 2-7 | 1122 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-1 | 1258 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-2 | 1341 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1342 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-3 | 1448 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1449 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-4 | 1580 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1581 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-5 | 1701 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-6 | 1772 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1773 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 3-7 | 1902 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 1903 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-1 | 1992 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 1993 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-2 | 2090 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2091 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-3 | 2228 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2229 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 2462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 2573 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-7 | 2574 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2716 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-1 | 2717 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 2858 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 2859 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 2993 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-3 | 2994 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 3098 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-4 | 3099 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 3172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 3289 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 3411 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-7 | 3412 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 3511 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 2-3 | 75 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-4 | 154 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-3 | 212 | SOLD_CORE_UNIT | Venda de 'DA_18_Teemo' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-4 | 222 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-6 | 242 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sentry' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-4 | 292 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 5-4 | 297 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 5-5 | 310 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-2 | 127 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-3 | 174 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 2-2 | 442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 551 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 905 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1044 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1045 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-1 | 1146 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-3 | 1358 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1359 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1496 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1596 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-6 | 1684 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-7 | 1786 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1787 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-1 | 1914 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-2 | 2054 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2055 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-3 | 2167 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2168 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-4 | 2302 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2303 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-5 | 2381 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-6 | 2508 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 2637 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 2739 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 2882 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 2968 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-4 | 3112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-5 | 3249 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-6 | 3363 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-6 | 3364 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 2-4 | 750 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-6 | 2614 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-7 | 2716 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 5-2 | 2945 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 7 | 2-7 | 113 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 3-6 | 172 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 4-5 | 233 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-5 | 304 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ornn' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-2 | 103 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-3 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 259 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 366 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 464 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-3 | 580 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-4 | 682 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 770 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 909 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-6 | 910 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 1036 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1179 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1251 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-2 | 1252 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1391 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-3 | 1392 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1533 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-4 | 1534 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1620 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-5 | 1621 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1747 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-6 | 1748 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1890 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 1891 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2034 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 2035 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2177 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 2178 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2317 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2416 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2533 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2658 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 2659 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2745 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2746 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2893 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 2994 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 3085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 3220 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 3361 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 3508 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-6 | 3509 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 3-1 | 1228 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 5-1 | 2971 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 8 | 2-5 | 96 | SOLD_CORE_UNIT | Venda de 'DA_Karma18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 2-5 | 98 | PURCHASE_SALE_REVIEW | Compra de DA_18_Kobuko foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-7 | 182 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-3 | 212 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-7 | 252 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 5-5 | 302 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-7 | 322 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 6-1 | 337 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-1 | 129 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 8 | 4-1 | 195 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 8 | 4-2 | 211 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 8 | 4-7 | 252 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-4 | 306 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 417 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-2 | 500 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1134 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1395 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1396 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1520 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1521 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1605 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 1790 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 1920 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2151 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2152 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2282 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2283 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2417 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2418 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2556 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 2557 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2687 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-6 | 2688 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 2824 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-7 | 2825 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 2926 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-1 | 2927 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 3031 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-2 | 3032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 3093 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-3 | 3094 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-4 | 3219 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-4 | 3220 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-5 | 3307 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-6 | 3455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-6 | 3456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-7 | 3592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 5-7 | 3593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-1 | 3739 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-1 | 3740 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-5 | 973 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-2 | 2259 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-6 | 2801 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 4-7 | 2903 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-1 | 3008 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-2 | 3070 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-3 | 3196 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-4 | 3284 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
