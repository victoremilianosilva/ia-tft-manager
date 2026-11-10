# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5124**
- Achados: **966**
- CRITICAL: 0 | HIGH: 11 | MEDIUM: 95 | LOW: 860

## Metadados da sessão

- Match ID: 383ce91e-3636-47f4-846f-8c05763884d2
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: 3d63262fb93d7504bfc05b4e6efd43b7d3bf9e722c0407b8e8b1bd7903bc856d
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4372**
- Entradas posteriores à eliminação ignoradas: **752**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 67 | 7 | 8 | 9 | 49 | 0 | 2 | não/inconclusivo | 0 |
| Jogador 6 | 74 | 7 | 14 | 4 | 71 | 3 | 2 | não/inconclusivo | 0 |
| Jogador 7 | 102 | 7 | 12 | 6 | 78 | 5 | 1 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 264 | 65 | 26 | 49 | 0 | 24 | 84 | 0.1074 | 13 | 56 |
- Jogador 1 — ações por estratégia: ECON::BUY: 11, ECON::BUY_XP: 14, ECON::ITEM: 7, ECON::MOVE_BENCH: 5, ECON::MOVE_BOARD: 6, ECON::PASS: 2, ECON::SELL: 4, FAST8::BUY: 4, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 7, FAST8::PASS: 2, FAST8::SELL: 3, STABILIZE::BUY: 44, STABILIZE::BUY_XP: 20, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 13, STABILIZE::MOVE_BOARD: 38, STABILIZE::PASS: 14, STABILIZE::SELL: 18, WINSTREAK::BUY: 6, WINSTREAK::BUY_XP: 15, WINSTREAK::ITEM: 2, WINSTREAK::MOVE_BENCH: 1, WINSTREAK::MOVE_BOARD: 13, WINSTREAK::PASS: 6, WINSTREAK::SELL: 1
- Jogador 1 — recompensas por ação: BUY: média 0.4375 (n=65), BUY_XP: média -0.0214 (n=49), ITEM: média 0.1313 (n=16), MOVE_BENCH: média 0.3060 (n=20), MOVE_BOARD: média -0.0028 (n=64), PASS: média -0.0292 (n=24), SELL: média -0.2450 (n=26)
| Jogador 2 | 305 | 117 | 81 | 21 | 0 | 12 | 60 | 0.0664 | 6 | 32 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 28, ALL_IN::BUY_XP: 3, ALL_IN::ITEM: 5, ALL_IN::MOVE_BENCH: 2, ALL_IN::MOVE_BOARD: 8, ALL_IN::PASS: 1, ALL_IN::SELL: 24, FAST8::BUY: 1, FAST8::BUY_XP: 1, FAST8::MOVE_BENCH: 2, FAST8::MOVE_BOARD: 1, STABILIZE::BUY: 88, STABILIZE::BUY_XP: 17, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 14, STABILIZE::MOVE_BOARD: 33, STABILIZE::PASS: 11, STABILIZE::SELL: 57
- Jogador 2 — recompensas por ação: BUY: média 0.2149 (n=117), BUY_XP: média 0.0229 (n=21), ITEM: média 0.1386 (n=14), MOVE_BENCH: média 0.2178 (n=18), MOVE_BOARD: média -0.0095 (n=42), PASS: média -0.0625 (n=12), SELL: média -0.1244 (n=81)
| Jogador 3 | 269 | 106 | 68 | 8 | 2 | 16 | 61 | 0.0850 | 6 | 20 |
- Jogador 3 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::REROLL: 2, ALL_IN::SELL: 7, FAST8::BUY: 16, FAST8::ITEM: 1, FAST8::MOVE_BENCH: 3, FAST8::MOVE_BOARD: 9, FAST8::SELL: 16, STABILIZE::BUY: 81, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 25, STABILIZE::MOVE_BOARD: 24, STABILIZE::PASS: 16, STABILIZE::SELL: 45
- Jogador 3 — recompensas por ação: BUY: média 0.2716 (n=106), BUY_XP: média -0.0125 (n=8), ITEM: média 0.1975 (n=8), MOVE_BENCH: média 0.0421 (n=28), MOVE_BOARD: média -0.0018 (n=33), PASS: média -0.0075 (n=16), REROLL: média -0.0700 (n=2), SELL: média -0.1216 (n=68)
| Jogador 4 | 162 | 49 | 23 | 8 | 1 | 18 | 55 | 0.0836 | 4 | 21 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 6, ALL_IN::ITEM: 3, ALL_IN::MOVE_BENCH: 5, ALL_IN::MOVE_BOARD: 3, ALL_IN::PASS: 2, ALL_IN::REROLL: 1, ALL_IN::SELL: 4, STABILIZE::BUY: 43, STABILIZE::BUY_XP: 8, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 31, STABILIZE::MOVE_BOARD: 16, STABILIZE::PASS: 16, STABILIZE::SELL: 19
- Jogador 4 — recompensas por ação: BUY: média 0.4508 (n=49), BUY_XP: média -0.0225 (n=8), ITEM: média 0.1837 (n=8), MOVE_BENCH: média -0.0533 (n=36), MOVE_BOARD: média -0.0158 (n=19), PASS: média -0.0728 (n=18), REROLL: média -0.0700 (n=1), SELL: média -0.2713 (n=23)
| Jogador 5 | 186 | 84 | 60 | 6 | 3 | 8 | 18 | 0.0504 | 12 | 20 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 13, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::MOVE_BOARD: 1, ALL_IN::REROLL: 2, ALL_IN::SELL: 8, STABILIZE::BUY: 71, STABILIZE::BUY_XP: 6, STABILIZE::ITEM: 5, STABILIZE::MOVE_BENCH: 10, STABILIZE::MOVE_BOARD: 6, STABILIZE::PASS: 8, STABILIZE::REROLL: 1, STABILIZE::SELL: 52
- Jogador 5 — recompensas por ação: BUY: média 0.2094 (n=84), BUY_XP: média -0.0183 (n=6), ITEM: média 0.1643 (n=7), MOVE_BENCH: média 0.2609 (n=11), MOVE_BOARD: média 0.0214 (n=7), PASS: média -0.0075 (n=8), REROLL: média -0.1133 (n=3), SELL: média -0.1978 (n=60)
| Jogador 6 | 206 | 71 | 42 | 14 | 2 | 16 | 49 | 0.0698 | 13 | 33 |
- Jogador 6 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::ITEM: 2, ALL_IN::REROLL: 1, ALL_IN::SELL: 2, STABILIZE::BUY: 67, STABILIZE::BUY_XP: 14, STABILIZE::ITEM: 10, STABILIZE::MOVE_BENCH: 15, STABILIZE::MOVE_BOARD: 34, STABILIZE::PASS: 16, STABILIZE::REROLL: 1, STABILIZE::SELL: 40
- Jogador 6 — recompensas por ação: BUY: média 0.2677 (n=71), BUY_XP: média -0.0379 (n=14), ITEM: média 0.1508 (n=12), MOVE_BENCH: média 0.1400 (n=15), MOVE_BOARD: média -0.0021 (n=34), PASS: média -0.0019 (n=16), REROLL: média -0.1150 (n=2), SELL: média -0.1826 (n=42)
| Jogador 7 | 227 | 78 | 51 | 12 | 0 | 16 | 61 | 0.0630 | 8 | 34 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 9, ALL_IN::MOVE_BOARD: 2, ALL_IN::SELL: 7, STABILIZE::BUY: 69, STABILIZE::BUY_XP: 12, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 9, STABILIZE::MOVE_BOARD: 50, STABILIZE::PASS: 16, STABILIZE::SELL: 44
- Jogador 7 — recompensas por ação: BUY: média 0.2731 (n=78), BUY_XP: média -0.0425 (n=12), ITEM: média 0.1533 (n=9), MOVE_BENCH: média 0.2867 (n=9), MOVE_BOARD: média -0.0050 (n=52), PASS: média -0.0100 (n=16), SELL: média -0.1965 (n=51)
| Jogador 8 | 184 | 80 | 56 | 1 | 0 | 6 | 33 | 0.0649 | 4 | 34 |
- Jogador 8 — ações por estratégia: ALL_IN::BUY: 13, ALL_IN::ITEM: 2, ALL_IN::MOVE_BENCH: 1, ALL_IN::SELL: 11, STABILIZE::BUY: 67, STABILIZE::BUY_XP: 1, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 23, STABILIZE::MOVE_BOARD: 9, STABILIZE::PASS: 6, STABILIZE::SELL: 45
- Jogador 8 — recompensas por ação: BUY: média 0.3330 (n=80), BUY_XP: média -0.0400 (n=1), ITEM: média 0.1800 (n=8), MOVE_BENCH: média 0.0229 (n=24), MOVE_BOARD: média -0.0256 (n=9), PASS: média -0.0333 (n=6), SELL: média -0.2896 (n=56)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 09:15:30 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2100 |  |
| Jogador 1 | ? | 09:15:31 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | ? | 09:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 09:15:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 09:15:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2400 |  |
| Jogador 1 | 1-1 | 09:15:37 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2200 |  |
| Jogador 1 | 1-1 | 09:15:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 09:15:39 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-1 | 09:15:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 09:15:41 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.4300 |  |
| Jogador 1 | 1-2 | 09:15:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.3500 |  |
| Jogador 1 | 1-2 | 09:15:44 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2500 |  |
| Jogador 1 | 1-2 | 09:15:44 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-2 | 09:15:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 1-2 | 09:15:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-3 | 09:15:52 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 09:15:52 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0300 |  |
| Jogador 1 | 1-3 | 09:15:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 09:16:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 1 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 09:16:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-4 | 09:16:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 09:16:05 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 1 | 2-1 | 09:16:09 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Diana | 0.3400 |  |
| Jogador 1 | 2-1 | 09:16:10 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Diana | -0.1300 |  |
| Jogador 1 | 2-1 | 09:16:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0500 |  |
| Jogador 1 | 2-1 | 09:16:11 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.0600 |  |
| Jogador 1 | 2-1 | 09:16:12 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | 0.2800 |  |
| Jogador 1 | 2-1 | 09:16:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Diana | -0.0100 |  |
| Jogador 1 | 2-1 | 09:16:13 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1700 |  |
| Jogador 1 | 2-2 | 09:16:20 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 1 | 2-2 | 09:16:20 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.3600 |  |
| Jogador 1 | 2-2 | 09:16:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 09:16:22 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1800 |  |
| Jogador 1 | 2-2 | 09:16:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 1 | 2-2 | 09:16:22 | MOVE Board -> Board: Ornn (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-2 | 09:16:23 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-2 | 09:16:23 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 09:16:32 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Ornn | 1.1200 |  |
| Jogador 1 | 2-3 | 09:16:33 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Ornn | -0.0600 |  |
| Jogador 1 | 2-3 | 09:16:33 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | -0.6300 |  |
| Jogador 1 | 2-3 | 09:16:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 1 | 2-3 | 09:16:35 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 1 | 2-3 | 09:16:35 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 2-3 | 09:16:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 09:16:46 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 1.0300 |  |
| Jogador 1 | 2-4 | 09:16:46 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-4 | 09:16:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 2-4 | 09:16:47 | MOVE Bench -> Board: Shen (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 2-4 | 09:16:48 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 2-4 | 09:16:48 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-4 | 09:16:49 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-4 | 09:16:49 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-5 | 09:17:01 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Adaptador | DA_KogMaw18_AD | 1.1200 |  |
| Jogador 1 | 2-5 | 09:17:01 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 2-5 | 09:17:02 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 1 | 2-5 | 09:17:02 | MOVE Bench -> Board: Krugue (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 2-5 | 09:17:03 | MOVE Board -> Board: Krugue (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 09:17:04 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 2-5 | 09:17:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 2-6 | 09:17:18 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Adaptador | DA_KogMaw18_AD | 1.0400 |  |
| Jogador 1 | 2-6 | 09:17:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 1.0200 |  |
| Jogador 1 | 2-6 | 09:17:19 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 1 | 2-6 | 09:17:19 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 1 | 2-6 | 09:17:20 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 1 | 2-6 | 09:17:20 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | -0.5200 |  |
| Jogador 1 | 2-6 | 09:17:21 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Kog'Maw (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 1 | 2-6 | 09:17:21 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Kog'Maw (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 2-6 | 09:17:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 2-7 | 09:17:37 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 2-7 | 09:17:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 2-7 | 09:17:38 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 2-7 | 09:17:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 2-7 | 09:17:40 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 1 | 2-7 | 09:17:40 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 2-7 | 09:17:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-1 | 09:18:00 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Adaptador | DA_KogMaw18_AD | 0.7200 |  |
| Jogador 1 | 3-1 | 09:18:01 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 1 | 3-1 | 09:18:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 09:18:03 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.2200 |  |
| Jogador 1 | 3-1 | 09:18:03 | MOVE Board -> Board: Shen (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-1 | 09:18:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 09:18:27 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Adaptador | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 1 | 3-2 | 09:18:27 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 09:18:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 09:18:28 | MOVE Board -> Board: Krugue (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 1 | 3-2 | 09:18:29 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-2 | 09:18:30 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-2 | 09:18:30 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.1700 |  |
| Jogador 1 | 3-2 | 09:18:31 | MOVE Board -> Board: Alistar (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-2 | 09:18:31 | MOVE Board -> Board: Shen (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-3 | 09:18:54 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Adaptador | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 1 | 3-3 | 09:18:55 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Adaptador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-3 | 09:18:55 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Adaptador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 3-3 | 09:18:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-3 | 09:18:57 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 3-3 | 09:18:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.2400 |  |
| Jogador 1 | 3-3 | 09:18:58 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Adaptador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-3 | 09:18:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-3 | 09:18:59 | MOVE Board -> Board: Shen (i:4.0) <-> Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-4 | 09:19:22 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 1 | 3-4 | 09:19:23 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 3-4 | 09:19:23 | MOVE Bench -> Board: Alistar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 3-4 | 09:19:24 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 3-4 | 09:19:24 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 1 | 3-4 | 09:19:25 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-4 | 09:19:26 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 1 | 3-4 | 09:19:26 | MOVE Board -> Board: Alistar (i:4.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-4 | 09:19:27 | MOVE Board -> Board: Master Yi (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Adaptador | DA_KogMaw18_AD | -0.3400 |  |
| Jogador 1 | 3-5 | 09:19:51 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Adaptador | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 3-5 | 09:19:52 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 1 | 3-5 | 09:19:52 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 1 | 3-5 | 09:19:52 | MOVE Board -> Board: Cascalho (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 3-5 | 09:19:53 | MOVE Board -> Board: Master Yi (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-5 | 09:19:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 3-6 | 09:20:22 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Adaptador | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 1 | 3-6 | 09:20:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Adaptador | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 1 | 3-6 | 09:20:23 | MOVE Board -> Board: Alistar (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Adaptador | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 1 | 3-6 | 09:20:24 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Adaptador | DA_KogMaw18_AD | -0.1900 |  |
| Jogador 1 | 3-6 | 09:20:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Adaptador | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Adaptador | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 1 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_BFSword -> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Adaptador | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 1 | 3-7 | 09:20:58 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Adaptador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 3-7 | 09:20:58 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Adaptador | DA_KogMaw18_AD | 0.4500 |  |
| Jogador 1 | 3-7 | 09:20:59 | MOVE Board -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 09:21:00 | MOVE Board -> Board: Alistar (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Adaptador | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 1 | 3-7 | 09:21:01 | MOVE Board -> Board: Cascalho (i:2.0) <-> Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 3-7 | 09:21:01 | MOVE Board -> Board: Master Yi (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Adaptador | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 1 | 3-7 | 09:21:02 | MOVE Board -> Board: Grompe (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-1 | 09:21:34 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Adaptador | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 1 | 4-1 | 09:21:35 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Adaptador | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 1 | 4-1 | 09:21:35 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Adaptador | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 1 | 4-1 | 09:21:36 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Adaptador | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 1 | 4-1 | 09:21:36 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-1 | 09:21:37 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Adaptador | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 1 | 4-1 | 09:21:37 | MOVE Board -> Board: Alistar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-1 | 09:21:38 | MOVE Board -> Board: Alistar (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-1 | 09:21:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Adaptador | DA_KogMaw18_AD | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 4-2 | 09:22:13 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 4-2 | 09:22:14 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Adaptador | DA_KogMaw18_AD | 0.9300 |  |
| Jogador 1 | 4-2 | 09:22:14 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Adaptador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 4-2 | 09:22:15 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Adaptador | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 1 | 4-2 | 09:22:15 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Adaptador | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 1 | 4-2 | 09:22:16 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Adaptador | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 1 | 4-2 | 09:22:17 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-2 | 09:22:18 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Adaptador | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-2 | 09:22:18 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 42 | 3 | Adaptador | DA_KogMaw18_AD | 0.5500 |  |
| Jogador 1 | 4-3 | 09:22:52 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Adaptador | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 1 | 4-3 | 09:22:53 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Adaptador | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 1 | 4-3 | 09:22:53 | MOVE Board -> Board: Master Yi (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Adaptador | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 1 | 4-3 | 09:22:54 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-3 | 09:22:54 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Adaptador | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 4-3 | 09:22:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 49 | 4 | Adaptador | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 4-4 | 09:23:32 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-4 | 09:23:33 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 4 | Adaptador | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 1 | 4-4 | 09:23:34 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 64 | 4 | Adaptador | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 1 | 4-4 | 09:23:34 | COMPROU: Malphite (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Adaptador | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-4 | 09:23:35 | MOVE Board -> Board: Krugue (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Adaptador | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 1 | 4-4 | 09:23:35 | MOVE Board -> Board: Grompe (i:4.0) <-> Krugue (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Adaptador | DA_KogMaw18_AD | 0.0400 |  |
| Jogador 1 | 4-4 | 09:23:36 | MOVE Board -> Board: Krugue (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-4 | 09:23:36 | MOVE Board -> Board: Master Yi (i:6.0) <-> Alistar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 4-4 | 09:23:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 4 | Adaptador | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 1 | 4-5 | 09:24:15 | VENDEU: Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 73 | 5 | Adaptador | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 4-5 | 09:24:16 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Adaptador | DA_KogMaw18_AD | 0.8900 |  |
| Jogador 1 | 4-5 | 09:24:17 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Adaptador | DA_CrimsonRaptor18 | 0.9600 |  |
| Jogador 1 | 4-5 | 09:24:17 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Adaptador | DA_CrimsonRaptor18 | 0.0900 |  |
| Jogador 1 | 4-5 | 09:24:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Adaptador | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 1 | 4-5 | 09:24:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Adaptador | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 1 | 4-5 | 09:24:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Adaptador | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 1 | 4-5 | 09:24:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 5 | Adaptador | DA_CrimsonRaptor18 | 0.0200 |  |
| Jogador 1 | 4-5 | 09:24:20 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 47 | 5 | Adaptador | DA_CrimsonRaptor18 | 0.0400 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:24:59 | COMPROU: Malphite (Custo 4 \| i:8.0) | ECON | ECON: manter reserva de 50 e gastar excedente útil | 53 | 4 | Adaptador | DA_CrimsonRaptor18 | 0.5000 |  |
| Jogador 1 | 4-6 | 09:25:00 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 49 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.0500 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:25:00 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 45 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:25:01 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 41 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:25:01 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 37 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.1100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:25:02 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 33 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:25:02 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 29 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.1100 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:25:02 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 25 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-6 | 09:25:03 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 21 | 4 | Adaptador | DA_CrimsonRaptor18 | -0.0300 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 4-7 | 09:25:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Lobo Trevoguari (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 28 | 2 | Adaptador | DA_CrimsonRaptor18 | 0.1000 |  |
| Jogador 1 | 4-7 | 09:25:50 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Lobo Trevoguari (i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 28 | 2 | Adaptador | DA_CrimsonRaptor18 | 0.1600 |  |
| Jogador 1 | 4-7 | 09:25:51 | VENDEU: Grompe (i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 33 | 2 | Adaptador | DA_CrimsonRaptor18 | -0.5000 |  |
| Jogador 1 | 4-7 | 09:25:51 | COMPROU: Nidalee (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 29 | 2 | Adaptador | DA_CrimsonRaptor18 | 0.7200 |  |
| Jogador 1 | 4-7 | 09:25:52 | VENDEU: Mamãe Bicuda (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 37 | 2 | Adaptador | DA_18_Malphite | -0.4900 |  |
| Jogador 1 | 4-7 | 09:25:52 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 34 | 2 | Adaptador | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 1 | 4-7 | 09:25:53 | COMPROU: Krugue (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Adaptador | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 1 | 4-7 | 09:25:53 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Adaptador | DA_KogMaw18_AD | 0.3400 |  |
| Jogador 1 | 4-7 | 09:25:54 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Adaptador | DA_KogMaw18_AD | -0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 5-1 | 09:26:39 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Adaptador | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 1 | 5-1 | 09:26:39 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Adaptador | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 1 | 5-1 | 09:26:40 | COMPROU: Ahri (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Adaptador | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 1 | 5-1 | 09:26:41 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Master Yi (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Adaptador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 1 | 5-1 | 09:26:42 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Adaptador | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 1 | 5-1 | 09:26:42 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Adaptador | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 1 | 5-1 | 09:26:45 | MOVE Bench -> Board: Malphite (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 27 | 2 | Adaptador | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 1 | 5-2 | 09:27:36 | COMPROU: Akali (Custo 1 \| i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 34 | 2 | Adaptador | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 1 | 5-2 | 09:27:37 | VENDEU: Kog'Maw (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 42 | 2 | Adaptador | DA_18_Malphite | -0.4900 |  |
| Jogador 1 | 5-2 | 09:27:37 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 2 | Adaptador | DA_18_Malphite | 0.8200 |  |
| Jogador 1 | 5-2 | 09:27:38 | MOVE Bench -> Board: Ahri (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 39 | 2 | Adaptador | DA_18_Malphite | 0.1500 |  |
| Jogador 1 | 5-2 | 09:27:39 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Lobo Trevoguari (i:4.0) (tabuleiro slot 23) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 2 | Adaptador | DA_18_Malphite | 0.0700 |  |
| Jogador 1 | 5-2 | 09:27:39 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Akali (i:2.0) (tabuleiro slot 11) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 2 | Adaptador | DA_18_Malphite | 0.1600 |  |
| Jogador 1 | 5-2 | 09:27:39 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Akali (i:2.0) (tabuleiro slot 11) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 2 | Adaptador | DA_18_Malphite | 0.1200 |  |
| Jogador 1 | 5-2 | 09:27:40 | COMPROU: Amumu (Custo 4 \| i:8.0) | ECON | ECON: acumular até o limite de juros de 50 | 35 | 2 | Adaptador | DA_18_Malphite | 0.0500 |  |
| Jogador 1 | 5-2 | 09:27:40 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 31 | 2 | Adaptador | DA_18_Malphite | 0.0000 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 5-3 | 09:28:26 | VENDEU: Master Yi (i:12.0) | ECON | ECON: acumular até o limite de juros de 50 | 49 | 3 | Adaptador | DA_18_Malphite | -0.5700 |  |
| Jogador 1 | 5-3 | 09:28:27 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | ECON | ECON: acumular até o limite de juros de 50 | 47 | 3 | Adaptador | DA_18_Malphite | 0.7800 |  |
| Jogador 1 | 5-3 | 09:28:27 | EQUIP_FROM_INVENTORY: TFT_Item_Deathblade -> Akali (i:2.0) (tabuleiro slot 11) | ECON | ECON: acumular até o limite de juros de 50 | 47 | 3 | Adaptador | DA_18_Malphite | 0.0800 |  |
| Jogador 1 | 5-3 | 09:28:28 | EQUIP_FROM_INVENTORY: TFT_Item_RapidFireCannon -> Fiddlesticks (i:6.0) (tabuleiro slot 25) | ECON | ECON: acumular até o limite de juros de 50 | 47 | 3 | Adaptador | DA_18_Malphite | 0.0900 |  |
| Jogador 1 | 5-3 | 09:28:28 | MOVE Board -> Board: Ahri (i:8.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 47 | 3 | Adaptador | DA_18_Malphite | 0.0000 |  |
| Jogador 1 | 5-3 | 09:28:29 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 43 | 3 | Adaptador | DA_18_Malphite | 0.0000 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 5-3 | 09:28:31 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Adaptador | DA_18_Malphite | -0.0800 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 5-3 | 09:28:31 | BUY XP | ECON | ECON: acumular até o limite de juros de 50 | 35 | 3 | Adaptador | DA_18_Malphite | 0.0000 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW |
| Jogador 1 | 5-3 | 09:28:32 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 35 | 3 | Adaptador | DA_18_Malphite | 0.6000 |  |
| Jogador 1 | 5-4 | 09:29:18 | COMPROU: Lux (Custo 5 \| i:10.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Adaptador | DA_18_Malphite | -0.2400 |  |
| Jogador 1 | 5-4 | 09:29:19 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Adaptador | DA_18_Malphite | 0.0000 |  |
| Jogador 1 | 5-4 | 09:29:19 | MOVE Board -> Board: Malphite (i:8.0) <-> Fiddlesticks (i:6.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Adaptador | DA_18_Malphite | -0.0100 |  |
| Jogador 1 | 5-4 | 09:29:20 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Akali (i:2.0) | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Adaptador | DA_18_Malphite | -0.0100 |  |
| Jogador 1 | 5-4 | 09:29:20 | PASSOU TURNO | ECON | ECON: acumular até o limite de juros de 50 | 39 | 3 | Adaptador | DA_18_Malphite | -0.0500 |  |
| Jogador 1 | 5-5 | 09:30:10 | MOVE Board -> Board: Akali (i:2.0) <-> Ahri (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 50 | 4 | Adaptador | DA_18_Malphite | 0.0000 |  |
| Jogador 1 | 5-5 | 09:30:10 | MOVE Board -> Board: Ahri (i:8.0) <-> Krugue (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 50 | 4 | Adaptador | DA_18_Malphite | -0.0100 |  |
| Jogador 1 | 5-5 | 09:30:11 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 50 | 4 | Adaptador | DA_18_Malphite | -0.0900 |  |
| Jogador 1 | 5-6 | 09:31:05 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Akali (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 61 | 5 | Adaptador | DA_18_Malphite | 0.0000 |  |
| Jogador 1 | 5-6 | 09:31:05 | MOVE Board -> Board: Akali (i:2.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 61 | 5 | Adaptador | DA_18_Malphite | -0.0200 |  |
| Jogador 1 | 5-6 | 09:31:06 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Malphite (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 61 | 5 | Adaptador | DA_18_Malphite | -0.0100 |  |
| Jogador 1 | 5-6 | 09:31:06 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 61 | 5 | Adaptador | DA_18_Malphite | -0.0500 |  |
| Jogador 1 | 5-7 | 09:31:58 | COMPROU: Nidalee (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 68 | 5 | Adaptador | DA_Nidalee18_AP | 1.0700 |  |
| Jogador 1 | 5-7 | 09:31:59 | COMPROU: Alistar (Custo 2 \| i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 66 | 5 | Adaptador | DA_Nidalee18_AP | 0.5100 |  |
| Jogador 1 | 5-7 | 09:31:59 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Akali (i:2.0) (tabuleiro slot 9) | WINSTREAK | WINSTREAK: preservar vantagem atual | 66 | 5 | Adaptador | DA_Nidalee18_AP | 0.0900 |  |
| Jogador 1 | 5-7 | 09:32:00 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 62 | 5 | Adaptador | DA_Nidalee18_AP | 0.2600 |  |
| Jogador 1 | 5-7 | 09:32:00 | MOVE Board -> Board: Lux (i:10.0) <-> Akali (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 62 | 5 | Adaptador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 1 | 5-7 | 09:32:01 | MOVE Board -> Board: Akali (i:2.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 62 | 5 | Adaptador | DA_Nidalee18_AP | -0.0200 |  |
| Jogador 1 | 5-7 | 09:32:01 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Lobo Trevoguari (i:4.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 62 | 5 | Adaptador | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 1 | 5-7 | 09:32:01 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 62 | 5 | Adaptador | DA_Nidalee18_AP | -0.0500 |  |
| Jogador 1 | 6-1 | 09:32:52 | VENDEU: Rubrivirim (i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 75 | 5 | Adaptador | DA_Nidalee18_AP | -0.0300 |  |
| Jogador 1 | 6-1 | 09:32:53 | COMPROU: Akali (Custo 1 \| i:2.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 74 | 5 | Adaptador | DA_Nidalee18_AP | 1.0600 |  |
| Jogador 1 | 6-1 | 09:32:54 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Lux (i:10.0) (tabuleiro slot 9) | WINSTREAK | WINSTREAK: preservar vantagem atual | 74 | 5 | Adaptador | DA_Nidalee18_AP | 0.0500 |  |
| Jogador 1 | 6-1 | 09:32:54 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 70 | 5 | Adaptador | DA_Nidalee18_AP | 0.0300 |  |
| Jogador 1 | 6-1 | 09:32:54 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 66 | 5 | Adaptador | DA_Nidalee18_AP | 0.0300 |  |
| Jogador 1 | 6-1 | 09:32:55 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 62 | 5 | Adaptador | DA_Nidalee18_AP | 0.0300 |  |
| Jogador 1 | 6-1 | 09:32:55 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 58 | 5 | Adaptador | DA_Nidalee18_AP | 0.0300 |  |
| Jogador 1 | 6-1 | 09:32:56 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 54 | 5 | Adaptador | DA_Nidalee18_AP | 0.0100 |  |
| Jogador 1 | 6-1 | 09:32:56 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 50 | 5 | Adaptador | DA_Nidalee18_AP | 0.0100 |  |
| Jogador 1 | 6-2 | 09:33:50 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 59 | 5 | Adaptador | DA_Nidalee18_AP | 0.0300 |  |
| Jogador 1 | 6-2 | 09:33:50 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 55 | 5 | Adaptador | DA_Nidalee18_AP | 0.0100 |  |
| Jogador 1 | 6-2 | 09:33:51 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 51 | 5 | Adaptador | DA_Nidalee18_AP | 0.0100 |  |
| Jogador 1 | 6-2 | 09:33:51 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 47 | 5 | Adaptador | DA_Nidalee18_AP | -0.0800 |  |
| Jogador 1 | 6-2 | 09:33:52 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 43 | 5 | Adaptador | DA_Nidalee18_AP | -0.0300 |  |
| Jogador 1 | 6-2 | 09:33:52 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 39 | 5 | Adaptador | DA_Nidalee18_AP | -0.1100 |  |
| Jogador 1 | 6-2 | 09:33:53 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 35 | 5 | Adaptador | DA_Nidalee18_AP | -0.0300 |  |
| Jogador 1 | 6-2 | 09:33:53 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 31 | 5 | Adaptador | DA_Nidalee18_AP | -0.0300 |  |
| Jogador 1 | 6-2 | 09:33:53 | BUY XP | WINSTREAK | WINSTREAK: preservar vantagem atual | 27 | 5 | Adaptador | DA_Nidalee18_AP | -0.1100 |  |
| Jogador 1 | 6-3 | 09:34:50 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 38 | 2 | Adaptador | DA_Nidalee18_AP | -0.1900 |  |
| Jogador 1 | 6-4 | 09:35:49 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Adaptador | DA_Nidalee18_AP | 0.7600 |  |
| Jogador 1 | 6-4 | 09:35:49 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Adaptador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 1 | 6-4 | 09:35:50 | MOVE Board -> Board: Malphite (i:8.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Adaptador | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 1 | 6-4 | 09:35:50 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Lux (i:10.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Adaptador | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 1 | 6-4 | 09:35:51 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Adaptador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 1 | 6-4 | 09:35:55 | MOVE Bench -> Board: Rubrivira (i:8.0) <-> Vazio | WINSTREAK | WINSTREAK: preservar vantagem atual | 45 | 3 | Adaptador | DA_Nidalee18_AP | 0.2700 |  |
| Jogador 1 | 6-5 | 09:36:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 55 | 4 | Adaptador | DA_Nidalee18_AP | 0.4600 |  |
| Jogador 1 | 6-5 | 09:36:55 | MOVE Board -> Board: Rubrivira (i:8.0) <-> Fiddlesticks (i:6.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 55 | 4 | Adaptador | DA_Nidalee18_AP | 0.0000 |  |
| Jogador 1 | 6-5 | 09:36:56 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Malphite (i:8.0) | WINSTREAK | WINSTREAK: preservar vantagem atual | 55 | 4 | Adaptador | DA_Nidalee18_AP | -0.0100 |  |
| Jogador 1 | 6-5 | 09:36:56 | PASSOU TURNO | WINSTREAK | WINSTREAK: preservar vantagem atual | 55 | 4 | Adaptador | DA_Nidalee18_AP | -0.0500 |  |
| Jogador 2 | ? | 09:15:30 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | ? | 09:15:31 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | ? | 09:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 09:15:36 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 09:15:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 1-1 | 09:15:37 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 1-1 | 09:15:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 09:15:41 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.5000 |  |
| Jogador 2 | 1-2 | 09:15:43 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 09:15:44 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1200 |  |
| Jogador 2 | 1-2 | 09:15:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 09:15:48 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 1-3 | 09:15:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 09:15:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0700 |  |
| Jogador 2 | 1-3 | 09:15:53 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-3 | 09:15:53 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.4000 |  |
| Jogador 2 | 1-3 | 09:15:54 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-3 | 09:15:54 | MOVE Board -> Board: Veigar (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 1-3 | 09:15:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 09:16:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 09:16:02 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 09:16:02 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 1-4 | 09:16:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 1-4 | 09:16:05 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2000 |  |
| Jogador 2 | 1-4 | 09:16:06 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-1 | 09:16:09 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 09:16:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | 2-1 | 09:16:10 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-1 | 09:16:11 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 2-1 | 09:16:12 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.8800 |  |
| Jogador 2 | 2-1 | 09:16:12 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-1 | 09:16:13 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-2 | 09:16:20 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 2-2 | 09:16:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0500 |  |
| Jogador 2 | 2-2 | 09:16:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 09:16:32 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.9700 |  |
| Jogador 2 | 2-3 | 09:16:33 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 2-3 | 09:16:33 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 09:16:34 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-3 | 09:16:35 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1300 |  |
| Jogador 2 | 2-3 | 09:16:35 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1500 |  |
| Jogador 2 | 2-3 | 09:16:36 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1900 |  |
| Jogador 2 | 2-3 | 09:16:36 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 2-3 | 09:16:36 | MOVE Board -> Board: Veigar (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-4 | 09:16:46 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.3100 |  |
| Jogador 2 | 2-4 | 09:16:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 09:16:47 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 2-4 | 09:16:47 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-4 | 09:16:48 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 09:16:48 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-4 | 09:16:49 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-4 | 09:16:49 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-4 | 09:16:50 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-5 | 09:17:01 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 2-5 | 09:17:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0300 |  |
| Jogador 2 | 2-5 | 09:17:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.5900 |  |
| Jogador 2 | 2-5 | 09:17:02 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-5 | 09:17:03 | MOVE Board -> Board: Veigar (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-5 | 09:17:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 09:17:18 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | 0.3600 |  |
| Jogador 2 | 2-6 | 09:17:18 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 2-6 | 09:17:19 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-6 | 09:17:19 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 2-6 | 09:17:20 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-6 | 09:17:20 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 2-6 | 09:17:21 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 2-6 | 09:17:21 | MOVE Bench -> Board: Lillia (i:8.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.6200 |  |
| Jogador 2 | 2-6 | 09:17:22 | MOVE Board -> Board: Lillia (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 09:17:37 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-7 | 09:17:37 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.1500 |  |
| Jogador 2 | 2-7 | 09:17:38 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 09:17:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-7 | 09:17:40 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-7 | 09:17:40 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0800 |  |
| Jogador 2 | 2-7 | 09:17:40 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-7 | 09:17:41 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-7 | 09:17:41 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 09:18:00 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Veigar | 0.7600 |  |
| Jogador 2 | 3-1 | 09:18:01 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | 0.7600 |  |
| Jogador 2 | 3-1 | 09:18:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 09:18:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-1 | 09:18:03 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-1 | 09:18:04 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.2100 |  |
| Jogador 2 | 3-1 | 09:18:04 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.3600 |  |
| Jogador 2 | 3-1 | 09:18:05 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Veigar | -0.2900 |  |
| Jogador 2 | 3-1 | 09:18:05 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-2 | 09:18:27 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | 0.8000 |  |
| Jogador 2 | 3-2 | 09:18:27 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.2500 |  |
| Jogador 2 | 3-2 | 09:18:28 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-2 | 09:18:28 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Veigar | -0.0600 |  |
| Jogador 2 | 3-2 | 09:18:29 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_Veigar | -0.0500 |  |
| Jogador 2 | 3-2 | 09:18:30 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-2 | 09:18:30 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_Veigar | -0.6200 |  |
| Jogador 2 | 3-2 | 09:18:31 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | -0.6300 |  |
| Jogador 2 | 3-2 | 09:18:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 09:18:54 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-3 | 09:18:55 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-3 | 09:18:55 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 09:18:56 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Feérico | DA_18_Veigar | -0.3700 |  |
| Jogador 2 | 3-3 | 09:18:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | 0.4300 |  |
| Jogador 2 | 3-3 | 09:18:57 | MOVE Board -> Board: Lillia (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-3 | 09:18:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 09:18:58 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-3 | 09:18:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-4 | 09:19:22 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Feérico | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 3-4 | 09:19:23 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Feérico | DA_18_Veigar | 0.0700 |  |
| Jogador 2 | 3-4 | 09:19:23 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_18_Veigar | -0.2600 |  |
| Jogador 2 | 3-4 | 09:19:24 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-4 | 09:19:24 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 3-4 | 09:19:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Feérico | DA_18_Veigar | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-5 | 09:19:51 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-5 | 09:19:52 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | 0.3000 |  |
| Jogador 2 | 3-5 | 09:19:52 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-5 | 09:19:52 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Veigar | -0.0400 |  |
| Jogador 2 | 3-5 | 09:19:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 09:19:53 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Veigar | -0.5100 |  |
| Jogador 2 | 3-5 | 09:19:54 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 3-5 | 09:19:55 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-5 | 09:19:55 | MOVE Board -> Board: Lillia (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Feérico | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 3-6 | 09:20:22 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 3-6 | 09:20:23 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_Veigar | 0.8100 |  |
| Jogador 2 | 3-6 | 09:20:23 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Feérico | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 3-6 | 09:20:24 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_Tristana | 0.8500 |  |
| Jogador 2 | 3-6 | 09:20:24 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Tristana | 0.2700 |  |
| Jogador 2 | 3-6 | 09:20:25 | VENDEU: Tristana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Feérico | DA_18_Lillia | -0.6200 |  |
| Jogador 2 | 3-6 | 09:20:25 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 1 | Feérico | DA_18_Lillia | -0.4300 |  |
| Jogador 2 | 3-6 | 09:20:26 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_18_Lillia | -0.1400 |  |
| Jogador 2 | 3-6 | 09:20:26 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 3-7 | 09:20:57 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Feérico | DA_18_Lillia | 0.2900 |  |
| Jogador 2 | 3-7 | 09:20:57 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Feérico | DA_18_Lillia | -0.0700 |  |
| Jogador 2 | 3-7 | 09:20:58 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Feérico | DA_18_Lillia | 0.1800 |  |
| Jogador 2 | 3-7 | 09:20:58 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Feérico | DA_18_Lillia | 0.2200 |  |
| Jogador 2 | 3-7 | 09:20:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-7 | 09:21:00 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 2 | Feérico | DA_18_Lillia | -0.2800 |  |
| Jogador 2 | 3-7 | 09:21:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 2 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 3-7 | 09:21:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 2 | Feérico | DA_18_Lillia | -0.0900 |  |
| Jogador 2 | 3-7 | 09:21:02 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 2 | Feérico | DA_18_Lillia | 0.4000 |  |
| Jogador 2 | 4-1 | 09:21:34 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Feérico | DA_18_Lillia | 0.5900 |  |
| Jogador 2 | 4-1 | 09:21:35 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 4-1 | 09:21:35 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 4-1 | 09:21:36 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-1 | 09:21:36 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 4-1 | 09:21:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_Lillia | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-2 | 09:22:13 | VENDEU: Krugue (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Feérico | DA_18_Lillia | -0.0400 |  |
| Jogador 2 | 4-2 | 09:22:14 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Feérico | DA_18_Lillia | 0.3300 |  |
| Jogador 2 | 4-2 | 09:22:14 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-2 | 09:22:15 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-2 | 09:22:15 | MOVE Board -> Board: Veigar (i:4.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-2 | 09:22:16 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-2 | 09:22:17 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_18_Lillia | 0.0800 |  |
| Jogador 2 | 4-2 | 09:22:18 | MOVE Board -> Board: Lillia (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-2 | 09:22:18 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-3 | 09:22:52 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 4-3 | 09:22:53 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Lillia | 0.3600 |  |
| Jogador 2 | 4-3 | 09:22:53 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-3 | 09:22:54 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Lillia | -0.0600 |  |
| Jogador 2 | 4-3 | 09:22:54 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_18_Lillia | 0.0100 |  |
| Jogador 2 | 4-3 | 09:22:55 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Feérico | DA_18_Lillia | -0.2600 |  |
| Jogador 2 | 4-3 | 09:22:55 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Feérico | DA_18_Lillia | 0.0100 |  |
| Jogador 2 | 4-3 | 09:22:56 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_18_Lillia | -0.2200 |  |
| Jogador 2 | 4-3 | 09:22:56 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-4 | 09:23:32 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-4 | 09:23:33 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Feérico | DA_18_Lillia | 0.8300 |  |
| Jogador 2 | 4-4 | 09:23:34 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Feérico | DA_18_Lillia | 0.1000 |  |
| Jogador 2 | 4-4 | 09:23:34 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Feérico | DA_18_Lillia | 0.8700 |  |
| Jogador 2 | 4-4 | 09:23:35 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Feérico | DA_18_Lillia | -0.4300 |  |
| Jogador 2 | 4-4 | 09:23:35 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Lillia | 0.0100 |  |
| Jogador 2 | 4-4 | 09:23:36 | MOVE Board -> Board: Yorick (i:2.0) <-> Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-4 | 09:23:36 | MOVE Board -> Board: Lillia (i:8.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-4 | 09:23:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Feérico | DA_18_Lillia | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-5 | 09:24:15 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 4-5 | 09:24:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Feérico | DA_18_Lillia | 0.9600 |  |
| Jogador 2 | 4-5 | 09:24:17 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 66 | 5 | Feérico | DA_18_Lillia | -0.5900 |  |
| Jogador 2 | 4-5 | 09:24:17 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Feérico | DA_18_Lillia | 0.4000 |  |
| Jogador 2 | 4-5 | 09:24:18 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Feérico | DA_18_Lillia | 0.2500 |  |
| Jogador 2 | 4-5 | 09:24:18 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Kobuko (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Feérico | DA_18_Lillia | 0.1100 |  |
| Jogador 2 | 4-5 | 09:24:19 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Kobuko (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Feérico | DA_18_Lillia | 0.0800 |  |
| Jogador 2 | 4-5 | 09:24:19 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Feérico | DA_18_Lillia | -0.0400 |  |
| Jogador 2 | 4-5 | 09:24:20 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-6 | 09:24:59 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_18_Lillia | 0.0000 |  |
| Jogador 2 | 4-6 | 09:25:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Feérico | DA_18_Lillia | 0.1200 |  |
| Jogador 2 | 4-6 | 09:25:00 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 4-6 | 09:25:01 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Feérico | DA_18_Lillia | 0.0200 |  |
| Jogador 2 | 4-6 | 09:25:01 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-6 | 09:25:02 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Feérico | DA_18_Lillia | 0.0100 |  |
| Jogador 2 | 4-6 | 09:25:02 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 4-6 | 09:25:02 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Feérico | DA_18_Lillia | -0.2700 |  |
| Jogador 2 | 4-6 | 09:25:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 69 | 5 | Feérico | DA_18_Lillia | 0.0400 |  |
| Jogador 2 | 4-7 | 09:25:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Lillia | 0.1300 |  |
| Jogador 2 | 4-7 | 09:25:50 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 79 | 5 | Feérico | DA_18_Lillia | 0.1300 |  |
| Jogador 2 | 4-7 | 09:25:51 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 81 | 5 | Feérico | DA_18_Lillia | 0.0200 |  |
| Jogador 2 | 4-7 | 09:25:51 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Feérico | DA_18_Lillia | 0.3900 |  |
| Jogador 2 | 4-7 | 09:25:52 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 78 | 5 | Feérico | DA_18_Lillia | -0.1000 |  |
| Jogador 2 | 4-7 | 09:25:52 | COMPROU: Lux (Solar) (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Feérico | DA_18_Lillia | -0.1500 |  |
| Jogador 2 | 4-7 | 09:25:53 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Feérico | DA_18_Lillia | 0.0200 |  |
| Jogador 2 | 4-7 | 09:25:53 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Feérico | DA_18_Lillia | -0.1300 |  |
| Jogador 2 | 4-7 | 09:25:54 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Feérico | DA_18_Lillia | -0.0100 |  |
| Jogador 2 | 5-1 | 09:26:39 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 5-1 | 09:26:39 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_18_Lillia | -0.0300 |  |
| Jogador 2 | 5-1 | 09:26:40 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 82 | 5 | Feérico | DA_18_Lillia | 0.0800 |  |
| Jogador 2 | 5-1 | 09:26:41 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_18_Lillia | -0.0200 |  |
| Jogador 2 | 5-1 | 09:26:42 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Feérico | DA_18_Lillia | -0.2800 |  |
| Jogador 2 | 5-1 | 09:26:42 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_18_Lillia | 0.0200 |  |
| Jogador 2 | 5-1 | 09:26:43 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Feérico | DA_18_Lillia | -0.2500 |  |
| Jogador 2 | 5-1 | 09:26:44 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Feérico | DA_18_Lillia | 0.0200 |  |
| Jogador 2 | 5-1 | 09:26:45 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Feérico | DA_18_Lillia | -0.2500 |  |
| Jogador 2 | 5-2 | 09:27:36 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Feérico | DA_18_Lillia | 0.0200 |  |
| Jogador 2 | 5-2 | 09:27:37 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 94 | 5 | Feérico | DA_18_Azir | 1.0200 |  |
| Jogador 2 | 5-2 | 09:27:37 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Feérico | DA_18_Azir | -0.1300 |  |
| Jogador 2 | 5-2 | 09:27:38 | MOVE Bench -> Board: Lux (Solar) (i:10.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 91 | 5 | Feérico | DA_18_Azir | 0.0500 |  |
| Jogador 2 | 5-2 | 09:27:39 | VENDEU: Azir (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.6000 |  |
| Jogador 2 | 5-2 | 09:27:39 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-2 | 09:27:39 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 92 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0500 |  |
| Jogador 2 | 5-2 | 09:27:40 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0500 |  |
| Jogador 2 | 5-2 | 09:27:40 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0500 |  |
| Jogador 2 | 5-3 | 09:28:26 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 97 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-3 | 09:28:27 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 96 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.9700 |  |
| Jogador 2 | 5-3 | 09:28:27 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-3 | 09:28:28 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | 1.0200 |  |
| Jogador 2 | 5-3 | 09:28:28 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1500 |  |
| Jogador 2 | 5-3 | 09:28:29 | COMPROU: Alune (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1800 |  |
| Jogador 2 | 5-3 | 09:28:31 | MOVE Board -> Board: Lux (Solar) (i:10.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 93 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-3 | 09:28:31 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0300 |  |
| Jogador 2 | 5-3 | 09:28:32 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 89 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.6000 |  |
| Jogador 2 | 5-4 | 09:29:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 96 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-4 | 09:29:19 | COMPROU: Zyra (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 92 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0700 |  |
| Jogador 2 | 5-4 | 09:29:19 | MOVE Bench -> Board: Alune (i:10.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 92 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.4400 |  |
| Jogador 2 | 5-4 | 09:29:20 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 89 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.1600 |  |
| Jogador 2 | 5-4 | 09:29:20 | MOVE Board -> Board: Alune (i:10.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 89 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-4 | 09:29:21 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Alune (i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 89 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-4 | 09:29:21 | MOVE Board -> Board: Alune (i:10.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 89 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0200 |  |
| Jogador 2 | 5-4 | 09:29:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 89 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.1400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-5 | 09:30:10 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.6000 |  |
| Jogador 2 | 5-5 | 09:30:10 | COMPROU: Malphite (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.2300 |  |
| Jogador 2 | 5-5 | 09:30:11 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Veigar (i:4.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1200 |  |
| Jogador 2 | 5-5 | 09:30:11 | EQUIP_FROM_INVENTORY: TFT_Item_BrambleVest -> Kha'Zix (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0600 |  |
| Jogador 2 | 5-5 | 09:30:11 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-5 | 09:30:12 | MOVE Board -> Board: Tristana (i:6.0) <-> Alune (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-5 | 09:30:12 | MOVE Board -> Board: Alune (i:10.0) <-> Veigar (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-5 | 09:30:13 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.5000 |  |
| Jogador 2 | 5-6 | 09:31:05 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-6 | 09:31:05 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.9200 |  |
| Jogador 2 | 5-6 | 09:31:06 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0300 |  |
| Jogador 2 | 5-6 | 09:31:06 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.3900 |  |
| Jogador 2 | 5-6 | 09:31:07 | MOVE Board -> Board: Veigar (i:4.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-6 | 09:31:07 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0200 |  |
| Jogador 2 | 5-6 | 09:31:08 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0100 |  |
| Jogador 2 | 5-6 | 09:31:08 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Kobuko (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-6 | 09:31:09 | MOVE Board -> Board: Kobuko (i:2.0) <-> Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 5-7 | 09:31:58 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Kha'Zix (i:6.0) (tabuleiro slot 12) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0700 |  |
| Jogador 2 | 5-7 | 09:31:59 | VENDEU: Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0300 |  |
| Jogador 2 | 5-7 | 09:31:59 | COMPROU: Sivir (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1400 |  |
| Jogador 2 | 5-7 | 09:32:00 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0200 |  |
| Jogador 2 | 5-7 | 09:32:00 | COMPROU: Morgana (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 119 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.2200 |  |
| Jogador 2 | 5-7 | 09:32:01 | VENDEU: Morgana (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 123 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0100 |  |
| Jogador 2 | 5-7 | 09:32:01 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.2300 |  |
| Jogador 2 | 5-7 | 09:32:01 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Lux (Solar) (i:10.0) | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 5-7 | 09:32:02 | MOVE Board -> Board: Lux (Solar) (i:10.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 120 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 6-1 | 09:32:52 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0200 |  |
| Jogador 2 | 6-1 | 09:32:53 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.2000 |  |
| Jogador 2 | 6-1 | 09:32:54 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0300 |  |
| Jogador 2 | 6-1 | 09:32:54 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 129 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0800 |  |
| Jogador 2 | 6-1 | 09:32:54 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 6-1 | 09:32:55 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1800 |  |
| Jogador 2 | 6-1 | 09:32:55 | VENDEU: Shen (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0300 |  |
| Jogador 2 | 6-1 | 09:32:56 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0400 |  |
| Jogador 2 | 6-1 | 09:32:56 | VENDEU: LeBlanc (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 6-2 | 09:33:50 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.9500 |  |
| Jogador 2 | 6-2 | 09:33:50 | VENDEU: Malphite (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0600 |  |
| Jogador 2 | 6-2 | 09:33:51 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0600 |  |
| Jogador 2 | 6-2 | 09:33:51 | VENDEU: Zyra (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0200 |  |
| Jogador 2 | 6-2 | 09:33:52 | COMPROU: Ahri (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 140 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0600 |  |
| Jogador 2 | 6-2 | 09:33:52 | VENDEU: Ahri (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0100 |  |
| Jogador 2 | 6-2 | 09:33:53 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 142 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.2300 |  |
| Jogador 2 | 6-2 | 09:33:53 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0200 |  |
| Jogador 2 | 6-2 | 09:33:53 | COMPROU: Camille (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.2400 |  |
| Jogador 2 | 6-3 | 09:34:50 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 154 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0200 |  |
| Jogador 2 | 6-3 | 09:34:50 | COMPROU: Azir (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Feérico | DA_18_Lux_Sunbeam | 1.1100 |  |
| Jogador 2 | 6-3 | 09:34:51 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0600 |  |
| Jogador 2 | 6-3 | 09:34:51 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.6100 |  |
| Jogador 2 | 6-3 | 09:34:52 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 151 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.6800 |  |
| Jogador 2 | 6-3 | 09:34:52 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1400 |  |
| Jogador 2 | 6-3 | 09:34:52 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 143 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1600 |  |
| Jogador 2 | 6-3 | 09:34:53 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 139 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1600 |  |
| Jogador 2 | 6-3 | 09:34:53 | BUY XP | ALL_IN | HP crítico: gastar para sobreviver | 135 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1600 |  |
| Jogador 2 | 6-4 | 09:35:49 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 149 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0200 |  |
| Jogador 2 | 6-4 | 09:35:49 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 146 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.4700 |  |
| Jogador 2 | 6-4 | 09:35:50 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.5400 |  |
| Jogador 2 | 6-4 | 09:35:50 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.7600 |  |
| Jogador 2 | 6-4 | 09:35:51 | MOVE Bench -> Board: Rammus (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 147 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.2700 |  |
| Jogador 2 | 6-4 | 09:35:51 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 144 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 6-4 | 09:35:52 | VENDEU: Kha'Zix (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 152 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0600 |  |
| Jogador 2 | 6-4 | 09:35:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.2600 |  |
| Jogador 2 | 6-4 | 09:35:55 | MOVE Bench -> Board: Yunara (i:4.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 150 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.4000 |  |
| Jogador 2 | 6-5 | 09:36:55 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.7100 |  |
| Jogador 2 | 6-5 | 09:36:55 | EQUIP_FROM_INVENTORY: TFT_Item_GargoyleStoneplate -> Lux (Solar) (i:10.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0700 |  |
| Jogador 2 | 6-5 | 09:36:56 | EQUIP_FROM_INVENTORY: TFT_Item_BrambleVest -> Lux (Solar) (i:10.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0600 |  |
| Jogador 2 | 6-5 | 09:36:56 | VENDEU: Cassiopeia (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0000 |  |
| Jogador 2 | 6-5 | 09:36:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 158 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.1800 |  |
| Jogador 2 | 6-5 | 09:36:57 | VENDEU: Rek'Sai (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.0300 |  |
| Jogador 2 | 6-5 | 09:36:57 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 155 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.2400 |  |
| Jogador 2 | 6-5 | 09:36:58 | VENDEU: Rubrivira (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 159 | 5 | Feérico | DA_18_Lux_Sunbeam | 0.0100 |  |
| Jogador 2 | 6-5 | 09:36:58 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 156 | 5 | Feérico | DA_18_Lux_Sunbeam | -0.2100 |  |
| Jogador 3 | ? | 09:15:30 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | ? | 09:15:31 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | ? | 09:15:32 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | ? | 09:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 09:15:36 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 09:15:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 1-1 | 09:15:37 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-1 | 09:15:38 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 1-1 | 09:15:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 09:15:41 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-2 | 09:15:43 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 09:15:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 09:15:44 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 09:15:46 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-2 | 09:15:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 09:15:48 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 1-3 | 09:15:52 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-3 | 09:15:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 09:15:53 | MOVE Board -> Board: Akali (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-3 | 09:15:53 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 09:15:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 09:16:00 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 3 | 1-4 | 09:16:02 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-4 | 09:16:02 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-4 | 09:16:02 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 1-4 | 09:16:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-1 | 09:16:09 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 2-1 | 09:16:10 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 3 | 2-1 | 09:16:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 09:16:20 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 2-2 | 09:16:20 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 2-2 | 09:16:21 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-2 | 09:16:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 09:16:32 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-3 | 09:16:33 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 2-3 | 09:16:33 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 2-3 | 09:16:34 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 2-3 | 09:16:35 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-3 | 09:16:35 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 2-3 | 09:16:36 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-3 | 09:16:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-4 | 09:16:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.9000 |  |
| Jogador 3 | 2-4 | 09:16:46 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-4 | 09:16:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 09:17:01 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-5 | 09:17:01 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 09:17:02 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.6000 |  |
| Jogador 3 | 2-5 | 09:17:02 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-5 | 09:17:03 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | 0.6000 |  |
| Jogador 3 | 2-5 | 09:17:04 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 2-5 | 09:17:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 2-5 | 09:17:05 | MOVE Board -> Board: Yorick (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-5 | 09:17:05 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 09:17:18 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 2-6 | 09:17:18 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | 0.1600 |  |
| Jogador 3 | 2-6 | 09:17:19 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 2-6 | 09:17:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 2-6 | 09:17:20 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-6 | 09:17:20 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 2-6 | 09:17:21 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Akali_AD | -0.6300 |  |
| Jogador 3 | 2-6 | 09:17:21 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-6 | 09:17:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 2-7 | 09:17:37 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.2000 |  |
| Jogador 3 | 2-7 | 09:17:37 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 2-7 | 09:17:38 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-7 | 09:17:39 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.6900 |  |
| Jogador 3 | 2-7 | 09:17:40 | MOVE Board -> Board: Cascalho (i:2.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 09:17:40 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 2-7 | 09:17:40 | MOVE Board -> Board: Akali (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-7 | 09:17:41 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 09:18:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Colosso | DA_18_Akali_AD | 0.8200 |  |
| Jogador 3 | 3-1 | 09:18:01 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Akali_AD | 0.7800 |  |
| Jogador 3 | 3-1 | 09:18:02 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 3-1 | 09:18:03 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 3-1 | 09:18:03 | MOVE Board -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 09:18:04 | MOVE Board -> Board: Akali (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-1 | 09:18:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-2 | 09:18:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 3-2 | 09:18:27 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Colosso | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 3-2 | 09:18:28 | MOVE Board -> Board: Yorick (i:4.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 09:18:28 | MOVE Board -> Board: Kha'Zix (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-2 | 09:18:29 | MOVE Board -> Board: Grompe (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-2 | 09:18:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-3 | 09:18:54 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 09:18:55 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | 0.7300 |  |
| Jogador 3 | 3-3 | 09:18:55 | MOVE Bench -> Board: Rengar (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | -0.6500 |  |
| Jogador 3 | 3-3 | 09:18:56 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 3-3 | 09:18:57 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | -0.1200 |  |
| Jogador 3 | 3-3 | 09:18:57 | MOVE Bench -> Board: Rengar (i:6.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 3-3 | 09:18:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-4 | 09:19:22 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Colosso | DA_18_Akali_AD | -0.4200 |  |
| Jogador 3 | 3-4 | 09:19:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 3-4 | 09:19:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 3-4 | 09:19:24 | COMPROU: Nidalee (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 3-4 | 09:19:24 | MOVE Bench -> Board: Aronguejo (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 3-4 | 09:19:25 | MOVE Bench -> Board: Sivir (i:8.0) <-> Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 3-4 | 09:19:26 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | -0.6500 |  |
| Jogador 3 | 3-4 | 09:19:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-5 | 09:19:51 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Colosso | DA_18_Akali_AD | -0.5000 |  |
| Jogador 3 | 3-5 | 09:19:52 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Colosso | DA_18_Akali_AD | 0.7900 |  |
| Jogador 3 | 3-5 | 09:19:52 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_18_Akali_AD | 0.7700 |  |
| Jogador 3 | 3-5 | 09:19:52 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 3-5 | 09:19:53 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-5 | 09:19:53 | VENDEU: Aronguejo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_18_Akali_AD | -0.5000 |  |
| Jogador 3 | 3-5 | 09:19:54 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 3-5 | 09:19:55 | MOVE Board -> Board: Diana (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 09:19:55 | MOVE Board -> Board: Grompe (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 09:20:22 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Colosso | DA_18_Akali_AD | -0.5700 |  |
| Jogador 3 | 3-6 | 09:20:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Colosso | DA_18_Akali_AD | 0.3000 |  |
| Jogador 3 | 3-6 | 09:20:23 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 3-6 | 09:20:24 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 3-6 | 09:20:24 | MOVE Board -> Board: Yorick (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-6 | 09:20:25 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-6 | 09:20:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Akali_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Akali_AD | 0.1700 |  |
| Jogador 3 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_TearOfTheGoddess -> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 3-7 | 09:20:58 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-7 | 09:20:58 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Colosso | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 3-7 | 09:20:59 | VENDEU: Nidalee (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 3-7 | 09:21:00 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Colosso | DA_KogMaw18_AD | 0.9100 |  |
| Jogador 3 | 3-7 | 09:21:01 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 3 | Colosso | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 3 | 3-7 | 09:21:01 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Colosso | DA_KogMaw18_AD | -0.2700 |  |
| Jogador 3 | 3-7 | 09:21:02 | MOVE Bench -> Board: Sivir (i:8.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 3 | 4-1 | 09:21:34 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 4-1 | 09:21:35 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Colosso | DA_18_Akali_AD | 0.8400 |  |
| Jogador 3 | 4-1 | 09:21:35 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-1 | 09:21:36 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-1 | 09:21:36 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Colosso | DA_18_Akali_AD | 0.0600 |  |
| Jogador 3 | 4-1 | 09:21:37 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-1 | 09:21:37 | MOVE Board -> Board: Grompe (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-1 | 09:21:38 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 3 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-1 | 09:21:38 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-2 | 09:22:13 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-2 | 09:22:14 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Colosso | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 4-2 | 09:22:14 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 4-2 | 09:22:15 | COMPROU: Sett (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Colosso | DA_18_Akali_AD | -0.2300 |  |
| Jogador 3 | 4-2 | 09:22:15 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Colosso | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 4-2 | 09:22:16 | MOVE Bench -> Board: Sivir (i:8.0) <-> Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Colosso | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 4-2 | 09:22:17 | MOVE Bench -> Board: Rengar (i:6.0) <-> Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Colosso | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | 4-2 | 09:22:18 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Sivir (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Colosso | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 4-2 | 09:22:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Colosso | DA_18_Akali_AD | -0.0900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 3 | 4-3 | 09:22:52 | VENDEU: Sett (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 09:22:53 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 72 | 5 | Colosso | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 4-3 | 09:22:53 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-3 | 09:22:54 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Colosso | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 4-3 | 09:22:54 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-3 | 09:22:55 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Colosso | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 4-3 | 09:22:55 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-3 | 09:22:56 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Colosso | DA_18_Akali_AD | -0.2800 |  |
| Jogador 3 | 4-3 | 09:22:56 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 75 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-4 | 09:23:32 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 83 | 5 | Colosso | DA_18_Akali_AD | 0.3600 |  |
| Jogador 3 | 4-4 | 09:23:33 | VENDEU: Sivir (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 87 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-4 | 09:23:34 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 84 | 5 | Colosso | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 4-4 | 09:23:34 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-4 | 09:23:35 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 4-4 | 09:23:35 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-4 | 09:23:36 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 86 | 5 | Colosso | DA_18_Akali_AD | -0.2300 |  |
| Jogador 3 | 4-4 | 09:23:36 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 3 | 4-4 | 09:23:38 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 88 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 09:24:15 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Colosso | DA_18_Akali_AD | 0.3900 |  |
| Jogador 3 | 4-5 | 09:24:16 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 102 | 5 | Colosso | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 4-5 | 09:24:17 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 100 | 5 | Colosso | DA_18_Akali_AD | 0.3700 |  |
| Jogador 3 | 4-5 | 09:24:17 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Colosso | DA_18_Akali_AD | -0.5900 |  |
| Jogador 3 | 4-5 | 09:24:18 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 98 | 5 | Colosso | DA_18_Akali_AD | 0.3000 |  |
| Jogador 3 | 4-5 | 09:24:18 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Colosso | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 4-5 | 09:24:19 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 98 | 5 | Colosso | DA_18_Akali_AD | 0.3000 |  |
| Jogador 3 | 4-5 | 09:24:19 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 101 | 5 | Colosso | DA_18_Akali_AD | -0.4000 |  |
| Jogador 3 | 4-5 | 09:24:20 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 99 | 5 | Colosso | DA_18_Akali_AD | 0.3300 |  |
| Jogador 3 | 4-6 | 09:24:59 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Colosso | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 4-6 | 09:25:00 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 108 | 5 | Colosso | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 4-6 | 09:25:00 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 106 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 4-6 | 09:25:01 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 103 | 5 | Colosso | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | 4-6 | 09:25:01 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Colosso | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 4-6 | 09:25:02 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 109 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-6 | 09:25:02 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-6 | 09:25:02 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 110 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-6 | 09:25:03 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 111 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-7 | 09:25:50 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Colosso | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | 4-7 | 09:25:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Yorick (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Colosso | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 4-7 | 09:25:51 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 119 | 5 | Colosso | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 4-7 | 09:25:51 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 121 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 4-7 | 09:25:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 120 | 5 | Colosso | DA_18_Akali_AD | 0.0600 |  |
| Jogador 3 | 4-7 | 09:25:52 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 123 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-7 | 09:25:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 122 | 5 | Colosso | DA_18_Akali_AD | 0.7400 |  |
| Jogador 3 | 4-7 | 09:25:53 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Colosso | DA_18_Akali_AD | 0.4700 |  |
| Jogador 3 | 4-7 | 09:25:54 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 5-1 | 09:26:39 | VENDEU: Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 5-1 | 09:26:39 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Colosso | DA_18_Akali_AD | 0.8700 |  |
| Jogador 3 | 5-1 | 09:26:40 | VENDEU: Kha'Zix (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 135 | 5 | Colosso | DA_18_Akali_AD | -0.3800 |  |
| Jogador 3 | 5-1 | 09:26:41 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 5-1 | 09:26:42 | VENDEU: Warwick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 135 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-1 | 09:26:42 | COMPROU: Tristana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Colosso | DA_18_Akali_AD | -0.2100 |  |
| Jogador 3 | 5-1 | 09:26:43 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Grompe (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 5-1 | 09:26:44 | MOVE Board -> Board: Grompe (i:4.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-1 | 09:26:45 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-2 | 09:27:36 | VENDEU: Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 145 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-2 | 09:27:37 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 142 | 5 | Colosso | DA_18_Akali_AD | 0.8600 |  |
| Jogador 3 | 5-2 | 09:27:37 | VENDEU: Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 144 | 5 | Colosso | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 5-2 | 09:27:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 142 | 5 | Colosso | DA_18_Akali_AD | 0.9200 |  |
| Jogador 3 | 5-2 | 09:27:39 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 139 | 5 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 5-2 | 09:27:39 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 144 | 5 | Colosso | DA_18_Akali_AD | -0.6000 |  |
| Jogador 3 | 5-2 | 09:27:39 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 141 | 5 | Colosso | DA_18_Akali_AD | -0.2500 |  |
| Jogador 3 | 5-2 | 09:27:40 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 137 | 5 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 5-2 | 09:27:40 | BUY XP | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 133 | 5 | Colosso | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 5-3 | 09:28:26 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 148 | 5 | Colosso | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 5-3 | 09:28:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 146 | 5 | Colosso | DA_18_Akali_AD | 0.9300 |  |
| Jogador 3 | 5-3 | 09:28:27 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 5-3 | 09:28:28 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 146 | 5 | Colosso | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 5-3 | 09:28:28 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Colosso | DA_18_Akali_AD | -0.3800 |  |
| Jogador 3 | 5-3 | 09:28:29 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 146 | 5 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 3 | 5-3 | 09:28:31 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 149 | 5 | Colosso | DA_18_Akali_AD | -0.0700 |  |
| Jogador 3 | 5-3 | 09:28:31 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 147 | 5 | Colosso | DA_18_Akali_AD | 0.0400 |  |
| Jogador 3 | 5-3 | 09:28:32 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Colosso | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 5-4 | 09:29:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Colosso | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 5-4 | 09:29:19 | VENDEU: Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 5-4 | 09:29:19 | COMPROU: Azir (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Colosso | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 5-4 | 09:29:20 | VENDEU: Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 5-4 | 09:29:20 | COMPROU: Lux (Espinhos Negros) (Custo 5 \| i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_18_Akali_AD | -0.1100 |  |
| Jogador 3 | 5-4 | 09:29:21 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 5-4 | 09:29:21 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 5-4 | 09:29:21 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 5-4 | 09:29:22 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Mamãe Bicuda (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 152 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 5-5 | 09:30:10 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 5-5 | 09:30:10 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 164 | 5 | Colosso | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 5-5 | 09:30:11 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 5-5 | 09:30:11 | COMPROU: Ahri (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 163 | 5 | Colosso | DA_18_Akali_AD | -0.2200 |  |
| Jogador 3 | 5-5 | 09:30:11 | VENDEU: Ahri (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 5-5 | 09:30:12 | COMPROU: Kayle (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 165 | 5 | Colosso | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 5-5 | 09:30:12 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 165 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 5-5 | 09:30:13 | MOVE Board -> Board: Diana (i:6.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 165 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-5 | 09:30:13 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 165 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-6 | 09:31:05 | VENDEU: Kayle (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 177 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 5-6 | 09:31:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 176 | 5 | Colosso | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 5-6 | 09:31:06 | VENDEU: Lux (Espinhos Negros) (i:10.0) | FAST8 | FAST8: composição planejada exige nível 8 | 181 | 5 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 5-6 | 09:31:06 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Colosso | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 5-6 | 09:31:07 | VENDEU: Kog'Maw (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 181 | 5 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 5-6 | 09:31:07 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 5-6 | 09:31:08 | VENDEU: Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 181 | 5 | Colosso | DA_18_Akali_AD | -0.0300 |  |
| Jogador 3 | 5-6 | 09:31:08 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Colosso | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 5-6 | 09:31:09 | MOVE Board -> Board: Mamãe Bicuda (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 179 | 5 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 5-7 | 09:31:58 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Diana (i:6.0) (tabuleiro slot 25) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Colosso | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 5-7 | 09:31:59 | VENDEU: Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 191 | 5 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 5-7 | 09:31:59 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 188 | 5 | Colosso | DA_CrimsonRaptor18 | 1.0100 |  |
| Jogador 3 | 5-7 | 09:32:00 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 185 | 5 | Colosso | DA_CrimsonRaptor18 | 0.2400 |  |
| Jogador 3 | 5-7 | 09:32:00 | VENDEU: Mamãe Bicuda (i:12.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 193 | 5 | Colosso | DA_18_Yorick | -0.6000 |  |
| Jogador 3 | 5-7 | 09:32:01 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 190 | 5 | Colosso | DA_18_Yorick | 0.2400 |  |
| Jogador 3 | 5-7 | 09:32:01 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 191 | 5 | Colosso | DA_18_Yorick | -0.5900 |  |
| Jogador 3 | 5-7 | 09:32:01 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 188 | 5 | Colosso | DA_18_Yorick | 0.1300 |  |
| Jogador 3 | 5-7 | 09:32:02 | MOVE Bench -> Board: Kha'Zix (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 188 | 5 | Colosso | DA_18_Yorick | -0.1000 |  |
| Jogador 3 | 6-1 | 09:32:52 | COMPROU: Rengar (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 196 | 5 | Colosso | DA_18_Yorick | 0.8100 |  |
| Jogador 3 | 6-1 | 09:32:53 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 193 | 5 | Colosso | DA_18_Yorick | 0.0600 |  |
| Jogador 3 | 6-1 | 09:32:54 | VENDEU: Rengar (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 201 | 5 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 3 | 6-1 | 09:32:54 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 199 | 5 | Colosso | DA_18_Yorick | 0.0600 |  |
| Jogador 3 | 6-1 | 09:32:54 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 201 | 5 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 3 | 6-1 | 09:32:55 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 200 | 5 | Colosso | DA_18_Yorick | -0.0400 |  |
| Jogador 3 | 6-1 | 09:32:55 | VENDEU: Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 201 | 5 | Colosso | DA_18_Yorick | 0.0100 |  |
| Jogador 3 | 6-1 | 09:32:56 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 200 | 5 | Colosso | DA_18_Yorick | -0.2700 |  |
| Jogador 3 | 6-1 | 09:32:56 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 198 | 5 | Colosso | DA_18_Yorick | -0.0700 |  |
| Jogador 3 | 6-2 | 09:33:50 | VENDEU: Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 210 | 5 | Colosso | DA_18_Yorick | 0.0200 |  |
| Jogador 3 | 6-2 | 09:33:50 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Colosso | DA_18_Yorick | 0.5300 |  |
| Jogador 3 | 6-2 | 09:33:51 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 210 | 5 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 3 | 6-2 | 09:33:51 | COMPROU: Azuporã (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 206 | 5 | Colosso | DA_18_Yorick | 0.2300 |  |
| Jogador 3 | 6-2 | 09:33:52 | VENDEU: Azuporã (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 210 | 5 | Colosso | DA_18_Yorick | -0.0500 |  |
| Jogador 3 | 6-2 | 09:33:52 | COMPROU: Hecarim (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 207 | 5 | Colosso | DA_18_Yorick | 0.0900 |  |
| Jogador 3 | 6-2 | 09:33:53 | VENDEU: Hecarim (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 210 | 5 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 3 | 6-2 | 09:33:53 | COMPROU: Shen (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 208 | 5 | Colosso | DA_18_Yorick | 0.0600 |  |
| Jogador 3 | 6-2 | 09:33:53 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 206 | 5 | Colosso | DA_18_Yorick | -0.0700 |  |
| Jogador 4 | ? | 09:15:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 4 | ? | 09:15:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 4 | ? | 09:15:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | ? | 09:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 09:15:36 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 09:15:36 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 09:15:37 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-1 | 09:15:38 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0900 |  |
| Jogador 4 | 1-1 | 09:15:39 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 09:15:41 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4600 |  |
| Jogador 4 | 1-2 | 09:15:43 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 1-2 | 09:15:44 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 09:15:44 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 09:15:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 4 | 1-2 | 09:15:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 09:15:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 09:15:52 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 09:15:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 09:16:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 4 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.1800 |  |
| Jogador 4 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2200 |  |
| Jogador 4 | 1-4 | 09:16:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 4 | 1-4 | 09:16:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-4 | 09:16:05 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3900 |  |
| Jogador 4 | 2-1 | 09:16:09 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9600 |  |
| Jogador 4 | 2-1 | 09:16:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 2-1 | 09:16:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 2-2 | 09:16:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9400 |  |
| Jogador 4 | 2-2 | 09:16:20 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Camille | 1.0400 |  |
| Jogador 4 | 2-2 | 09:16:21 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Camille | 0.3000 |  |
| Jogador 4 | 2-2 | 09:16:22 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.5600 |  |
| Jogador 4 | 2-2 | 09:16:22 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 09:16:22 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 4 | 2-2 | 09:16:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 09:16:23 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.5400 |  |
| Jogador 4 | 2-2 | 09:16:23 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 09:16:32 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 4 | 2-3 | 09:16:33 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-3 | 09:16:33 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 4 | 2-3 | 09:16:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-3 | 09:16:35 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-3 | 09:16:35 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 2-3 | 09:16:36 | VENDEU: Aphelios (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_KogMaw18_AD | -0.0800 |  |
| Jogador 4 | 2-3 | 09:16:36 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_KogMaw18_AD | 0.2500 |  |
| Jogador 4 | 2-3 | 09:16:36 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_KogMaw18_AD | 0.9600 |  |
| Jogador 4 | 2-4 | 09:16:46 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Florescer | DA_KogMaw18_AD | 1.0000 |  |
| Jogador 4 | 2-4 | 09:16:46 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 4 | 2-4 | 09:16:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-4 | 09:16:47 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 2-4 | 09:16:48 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 2-4 | 09:16:48 | MOVE Bench -> Board: Diana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-4 | 09:16:49 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 2-4 | 09:16:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 2-4 | 09:16:50 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 09:17:01 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 2-5 | 09:17:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 2-5 | 09:17:02 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 2-5 | 09:17:02 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-5 | 09:17:03 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 2-5 | 09:17:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 2-6 | 09:17:18 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 4 | 2-6 | 09:17:18 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.3600 |  |
| Jogador 4 | 2-6 | 09:17:19 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 2-6 | 09:17:19 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 4 | 2-6 | 09:17:20 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.5900 |  |
| Jogador 4 | 2-6 | 09:17:20 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1300 |  |
| Jogador 4 | 2-6 | 09:17:21 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1500 |  |
| Jogador 4 | 2-6 | 09:17:21 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 2-6 | 09:17:22 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 09:17:37 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 2-7 | 09:17:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 2-7 | 09:17:38 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2400 |  |
| Jogador 4 | 2-7 | 09:17:39 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 2-7 | 09:17:40 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 4 | 2-7 | 09:17:40 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 4 | 2-7 | 09:17:40 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 2-7 | 09:17:41 | MOVE Bench -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | 0.1000 |  |
| Jogador 4 | 2-7 | 09:17:41 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Florescer | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 4 | 3-1 | 09:18:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 4 | 3-1 | 09:18:01 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.2300 |  |
| Jogador 4 | 3-1 | 09:18:02 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 09:18:03 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Florescer | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 4 | 3-1 | 09:18:03 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 3-1 | 09:18:04 | MOVE Bench -> Board: Yorick (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 4 | 3-1 | 09:18:04 | MOVE Board -> Board: Yorick (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-1 | 09:18:05 | MOVE Board -> Board: Sejuani (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 4 | 3-1 | 09:18:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-2 | 09:18:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Florescer | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 4 | 3-2 | 09:18:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.7700 |  |
| Jogador 4 | 3-2 | 09:18:28 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 3-2 | 09:18:28 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 4 | 3-2 | 09:18:29 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 4 | 3-2 | 09:18:30 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | -0.5000 |  |
| Jogador 4 | 3-2 | 09:18:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-3 | 09:18:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Florescer | DA_KogMaw18_AD | 0.2100 |  |
| Jogador 4 | 3-3 | 09:18:55 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 4 | 3-3 | 09:18:55 | MOVE Bench -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Florescer | DA_KogMaw18_AD | -0.3700 |  |
| Jogador 4 | 3-3 | 09:18:56 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 4 | 3-3 | 09:18:57 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 3-3 | 09:18:57 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.3000 |  |
| Jogador 4 | 3-3 | 09:18:58 | MOVE Bench -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 4 | 3-3 | 09:18:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 09:19:22 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Florescer | DA_KogMaw18_AD | -0.5800 |  |
| Jogador 4 | 3-4 | 09:19:23 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | 0.8000 |  |
| Jogador 4 | 3-4 | 09:19:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 4 | 3-4 | 09:19:24 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | -0.4600 |  |
| Jogador 4 | 3-4 | 09:19:24 | MOVE Bench -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | -0.3900 |  |
| Jogador 4 | 3-4 | 09:19:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Florescer | DA_KogMaw18_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-5 | 09:19:51 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-5 | 09:19:52 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Florescer | DA_KogMaw18_AD | 0.8500 |  |
| Jogador 4 | 3-5 | 09:19:52 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_KogMaw18_AD | 0.6000 |  |
| Jogador 4 | 3-5 | 09:19:52 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 3-5 | 09:19:53 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Florescer | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 4 | 3-5 | 09:19:53 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 4 | 3-5 | 09:19:54 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | -0.3000 |  |
| Jogador 4 | 3-5 | 09:19:55 | MOVE Bench -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | -0.4100 |  |
| Jogador 4 | 3-5 | 09:19:55 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Florescer | DA_KogMaw18_AD | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-6 | 09:20:22 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Florescer | DA_KogMaw18_AD | 0.7400 |  |
| Jogador 4 | 3-6 | 09:20:23 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Florescer | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 4 | 3-6 | 09:20:23 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Florescer | DA_KogMaw18_AD | -0.4400 |  |
| Jogador 4 | 3-6 | 09:20:24 | MOVE Bench -> Board: Diana (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Florescer | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 4 | 3-6 | 09:20:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Florescer | DA_KogMaw18_AD | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Florescer | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 4 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Florescer | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 4 | 3-7 | 09:20:58 | MOVE Bench -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Florescer | DA_KogMaw18_AD | 0.3300 |  |
| Jogador 4 | 3-7 | 09:20:58 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Florescer | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 4 | 3-7 | 09:20:59 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Florescer | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 4 | 3-7 | 09:21:00 | MOVE Board -> Board: Karma (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Florescer | DA_KogMaw18_AD | 0.0300 |  |
| Jogador 4 | 3-7 | 09:21:01 | MOVE Board -> Board: Yorick (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 09:21:01 | MOVE Board -> Board: Diana (i:6.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Florescer | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 4 | 3-7 | 09:21:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Florescer | DA_KogMaw18_AD | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-1 | 09:21:34 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Florescer | DA_KogMaw18_AD | -0.5700 |  |
| Jogador 4 | 4-1 | 09:21:35 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 44 | 3 | Florescer | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 4 | 4-1 | 09:21:35 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 46 | 3 | Florescer | DA_KogMaw18_AD | -0.1100 |  |
| Jogador 4 | 4-1 | 09:21:36 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 4-1 | 09:21:36 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Florescer | DA_KogMaw18_AD | -0.5100 |  |
| Jogador 4 | 4-1 | 09:21:37 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Florescer | DA_KogMaw18_AD | -0.5700 |  |
| Jogador 4 | 4-1 | 09:21:37 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Florescer | DA_KogMaw18_AD | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-2 | 09:22:13 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 56 | 4 | Florescer | DA_KogMaw18_AD | -0.7000 |  |
| Jogador 4 | 4-2 | 09:22:14 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Florescer | DA_KogMaw18_AD | 0.5400 |  |
| Jogador 4 | 4-2 | 09:22:14 | EQUIP_FROM_INVENTORY: TFT_Item_StatikkShiv -> Yorick (i:2.0) (tabuleiro slot 26) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Florescer | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 4 | 4-2 | 09:22:15 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Yorick (i:2.0) (tabuleiro slot 26) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Florescer | DA_KogMaw18_AD | 0.1500 |  |
| Jogador 4 | 4-2 | 09:22:15 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Yorick (i:2.0) (tabuleiro slot 26) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 4-2 | 09:22:16 | MOVE Bench -> Board: Mamãe Bicuda (i:6.0) <-> Kog'Maw (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Florescer | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 4 | 4-2 | 09:22:17 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Florescer | DA_KogMaw18_AD | -0.3800 |  |
| Jogador 4 | 4-2 | 09:22:18 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 53 | 4 | Florescer | DA_KogMaw18_AD | -0.4500 |  |
| Jogador 4 | 4-3 | 09:22:52 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Florescer | DA_KogMaw18_AD | 0.5600 |  |
| Jogador 4 | 4-3 | 09:22:53 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_KogMaw18_AD | 0.4300 |  |
| Jogador 4 | 4-3 | 09:22:53 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 4 | 4-3 | 09:22:54 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 64 | 5 | Florescer | DA_KogMaw18_AD | -0.1200 |  |
| Jogador 4 | 4-3 | 09:22:54 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 61 | 5 | Florescer | DA_KogMaw18_AD | 0.1200 |  |
| Jogador 4 | 4-3 | 09:22:55 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 59 | 5 | Florescer | DA_KogMaw18_AD | -0.0700 |  |
| Jogador 4 | 4-3 | 09:22:55 | VENDEU: Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 62 | 5 | Florescer | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 4 | 4-3 | 09:22:56 | COMPROU: Soraka (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Florescer | DA_KogMaw18_AD | 0.0800 |  |
| Jogador 4 | 4-3 | 09:22:56 | MOVE Bench -> Board: Yorick (i:2.0) <-> Karma (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 58 | 5 | Florescer | DA_KogMaw18_AD | 0.3500 |  |
| Jogador 4 | 4-4 | 09:23:32 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Florescer | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 4 | 4-4 | 09:23:33 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Florescer | DA_KogMaw18_AD | 1.1000 |  |
| Jogador 4 | 4-4 | 09:23:34 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Florescer | DA_KogMaw18_AD | 0.5800 |  |
| Jogador 4 | 4-4 | 09:23:34 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_KogMaw18_AD | -0.2100 |  |
| Jogador 4 | 4-4 | 09:23:35 | MOVE Board -> Board: Karma (i:2.0) <-> Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 4 | 4-4 | 09:23:35 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 4 | 4-4 | 09:23:36 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 67 | 5 | Florescer | DA_KogMaw18_AD | -0.6400 |  |
| Jogador 5 | ? | 09:15:30 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | ? | 09:15:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 5 | ? | 09:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 09:15:36 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 5 | 1-1 | 09:15:36 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 09:15:37 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 5 | 1-1 | 09:15:38 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 09:15:39 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 5 | 1-1 | 09:15:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 09:15:41 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4300 |  |
| Jogador 5 | 1-2 | 09:15:43 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2200 |  |
| Jogador 5 | 1-2 | 09:15:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-3 | 09:15:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3300 |  |
| Jogador 5 | 1-3 | 09:15:52 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 5 | 1-3 | 09:15:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-4 | 09:16:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 1.0300 |  |
| Jogador 5 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 5 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_RecurveBow -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.2100 |  |
| Jogador 5 | 1-4 | 09:16:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.4100 |  |
| Jogador 5 | 1-4 | 09:16:02 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2300 |  |
| Jogador 5 | 1-4 | 09:16:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-1 | 09:16:09 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | 0.9700 |  |
| Jogador 5 | 2-1 | 09:16:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-1 | 09:16:10 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-2 | 09:16:20 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 1.0400 |  |
| Jogador 5 | 2-2 | 09:16:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 5 | 2-2 | 09:16:21 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 5 | 2-2 | 09:16:22 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 5 | 2-2 | 09:16:22 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 5 | 2-2 | 09:16:22 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 5 | 2-2 | 09:16:23 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0300 |  |
| Jogador 5 | 2-2 | 09:16:23 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Cassiopeia | -0.2600 |  |
| Jogador 5 | 2-2 | 09:16:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 09:16:32 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Cassiopeia | 0.3100 |  |
| Jogador 5 | 2-3 | 09:16:33 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Cassiopeia | 0.2200 |  |
| Jogador 5 | 2-3 | 09:16:33 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0600 |  |
| Jogador 5 | 2-3 | 09:16:34 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-3 | 09:16:35 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.1700 |  |
| Jogador 5 | 2-3 | 09:16:35 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Cassiopeia | -0.0800 |  |
| Jogador 5 | 2-3 | 09:16:36 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Cassiopeia | -0.1000 |  |
| Jogador 5 | 2-3 | 09:16:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-3 | 09:16:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Cassiopeia | 0.0000 |  |
| Jogador 5 | 2-4 | 09:16:46 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.2900 |  |
| Jogador 5 | 2-4 | 09:16:46 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3400 |  |
| Jogador 5 | 2-4 | 09:16:47 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-4 | 09:16:47 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.1200 |  |
| Jogador 5 | 2-4 | 09:16:48 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3200 |  |
| Jogador 5 | 2-4 | 09:16:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-4 | 09:16:49 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | -0.3500 |  |
| Jogador 5 | 2-4 | 09:16:49 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.0300 |  |
| Jogador 5 | 2-4 | 09:16:50 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.4000 |  |
| Jogador 5 | 2-5 | 09:17:01 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Espinhos Negros | DA_18_Cassiopeia | 0.3600 |  |
| Jogador 5 | 2-5 | 09:17:01 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0900 |  |
| Jogador 5 | 2-5 | 09:17:02 | MOVE Board -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 09:17:02 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0600 |  |
| Jogador 5 | 2-5 | 09:17:03 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0900 |  |
| Jogador 5 | 2-5 | 09:17:04 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0700 |  |
| Jogador 5 | 2-5 | 09:17:04 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4300 |  |
| Jogador 5 | 2-5 | 09:17:05 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-5 | 09:17:05 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.0100 |  |
| Jogador 5 | 2-6 | 09:17:18 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.3500 |  |
| Jogador 5 | 2-6 | 09:17:18 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.9600 |  |
| Jogador 5 | 2-6 | 09:17:19 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.2100 |  |
| Jogador 5 | 2-6 | 09:17:19 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0300 |  |
| Jogador 5 | 2-6 | 09:17:20 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0400 |  |
| Jogador 5 | 2-6 | 09:17:20 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Cassiopeia | 0.1100 |  |
| Jogador 5 | 2-6 | 09:17:21 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.4200 |  |
| Jogador 5 | 2-6 | 09:17:21 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.3800 |  |
| Jogador 5 | 2-6 | 09:17:22 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Cassiopeia | -0.0100 |  |
| Jogador 5 | 2-7 | 09:17:37 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.7500 |  |
| Jogador 5 | 2-7 | 09:17:37 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Yunara | 0.1900 |  |
| Jogador 5 | 2-7 | 09:17:38 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_18_Yunara | 0.1100 |  |
| Jogador 5 | 2-7 | 09:17:39 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Enfeitiçador | DA_18_Yunara | 0.0300 |  |
| Jogador 5 | 2-7 | 09:17:40 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.6200 |  |
| Jogador 5 | 2-7 | 09:17:40 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Enfeitiçador | DA_18_Tristana | -0.2700 |  |
| Jogador 5 | 2-7 | 09:17:40 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 2-7 | 09:17:41 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Enfeitiçador | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 2-7 | 09:17:41 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_18_Tristana | -0.3500 |  |
| Jogador 5 | 3-1 | 09:18:00 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_18_Tristana | 0.6900 |  |
| Jogador 5 | 3-1 | 09:18:01 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Enfeitiçador | DA_18_Tristana | 0.2700 |  |
| Jogador 5 | 3-1 | 09:18:02 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_18_Tristana | -0.0200 |  |
| Jogador 5 | 3-1 | 09:18:03 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Enfeitiçador | DA_18_Tristana | -0.1000 |  |
| Jogador 5 | 3-1 | 09:18:03 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.5400 |  |
| Jogador 5 | 3-1 | 09:18:04 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | -0.2400 |  |
| Jogador 5 | 3-1 | 09:18:04 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.3400 |  |
| Jogador 5 | 3-1 | 09:18:05 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_18_Tristana | -0.2700 |  |
| Jogador 5 | 3-1 | 09:18:05 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Enfeitiçador | DA_18_Tristana | -0.3200 |  |
| Jogador 5 | 3-2 | 09:18:27 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_18_Tristana | 0.8100 |  |
| Jogador 5 | 3-2 | 09:18:27 | COMPROU: Ahri (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_18_Tristana | 0.2100 |  |
| Jogador 5 | 3-2 | 09:18:28 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_18_Tristana | 0.2800 |  |
| Jogador 5 | 3-2 | 09:18:28 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_18_Ahri | -0.1000 |  |
| Jogador 5 | 3-2 | 09:18:29 | VENDEU: Ahri (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Enfeitiçador | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 3-2 | 09:18:30 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Azir | 0.0400 |  |
| Jogador 5 | 3-2 | 09:18:30 | MOVE Bench -> Board: Yunara (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 3-2 | 09:18:31 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Azir | -0.4000 |  |
| Jogador 5 | 3-2 | 09:18:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Enfeitiçador | DA_18_Azir | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-3 | 09:18:54 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Azir | 0.8300 |  |
| Jogador 5 | 3-3 | 09:18:55 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 2 | Enfeitiçador | DA_18_Azir | 0.5200 |  |
| Jogador 5 | 3-3 | 09:18:55 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Azir | -0.0500 |  |
| Jogador 5 | 3-3 | 09:18:56 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Azir | 0.0500 |  |
| Jogador 5 | 3-3 | 09:18:57 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Azir | -0.3700 |  |
| Jogador 5 | 3-3 | 09:18:57 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Enfeitiçador | DA_18_Azir | -0.2500 |  |
| Jogador 5 | 3-3 | 09:18:58 | VENDEU: Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Enfeitiçador | DA_18_Azir | -0.3400 |  |
| Jogador 5 | 3-3 | 09:18:58 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_18_Azir | -0.4900 |  |
| Jogador 5 | 3-3 | 09:18:59 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_18_Azir | -0.4900 |  |
| Jogador 5 | 3-4 | 09:19:22 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Enfeitiçador | DA_18_Azir | 0.8500 |  |
| Jogador 5 | 3-4 | 09:19:23 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 3-4 | 09:19:23 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Enfeitiçador | DA_18_Azir | 0.4700 |  |
| Jogador 5 | 3-4 | 09:19:24 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 3 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 3-4 | 09:19:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 3 | Enfeitiçador | DA_18_Azir | -0.1900 |  |
| Jogador 5 | 3-4 | 09:19:25 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 3 | Enfeitiçador | DA_18_Azir | -0.3500 |  |
| Jogador 5 | 3-4 | 09:19:26 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 3 | Enfeitiçador | DA_18_Azir | -0.5400 |  |
| Jogador 5 | 3-4 | 09:19:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 3 | Enfeitiçador | DA_18_Azir | -0.3600 |  |
| Jogador 5 | 3-4 | 09:19:27 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 3 | Enfeitiçador | DA_18_Azir | -0.3200 |  |
| Jogador 5 | 3-5 | 09:19:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Enfeitiçador | DA_18_Azir | 0.0900 |  |
| Jogador 5 | 3-5 | 09:19:52 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_18_Azir | 0.0200 |  |
| Jogador 5 | 3-5 | 09:19:52 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_18_Azir | -0.3500 |  |
| Jogador 5 | 3-5 | 09:19:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 3 | Enfeitiçador | DA_18_Azir | -0.2400 |  |
| Jogador 5 | 3-5 | 09:19:53 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 3-5 | 09:19:53 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Enfeitiçador | DA_18_Azir | -0.3100 |  |
| Jogador 5 | 3-5 | 09:19:54 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Azir | -0.3200 |  |
| Jogador 5 | 3-5 | 09:19:55 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 3 | Enfeitiçador | DA_18_Azir | -0.3700 |  |
| Jogador 5 | 3-5 | 09:19:55 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Enfeitiçador | DA_18_Azir | -0.0500 |  |
| Jogador 5 | 3-6 | 09:20:22 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Enfeitiçador | DA_18_Azir | 0.3800 |  |
| Jogador 5 | 3-6 | 09:20:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Azir | 0.0300 |  |
| Jogador 5 | 3-6 | 09:20:23 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Enfeitiçador | DA_18_Azir | -0.2900 |  |
| Jogador 5 | 3-6 | 09:20:24 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 4 | Enfeitiçador | DA_18_Azir | -0.0400 |  |
| Jogador 5 | 3-6 | 09:20:24 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Enfeitiçador | DA_18_Azir | -0.3500 |  |
| Jogador 5 | 3-6 | 09:20:25 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Enfeitiçador | DA_18_Azir | -0.2800 |  |
| Jogador 5 | 3-6 | 09:20:25 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Enfeitiçador | DA_18_Azir | -0.3200 |  |
| Jogador 5 | 3-6 | 09:20:26 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 4 | Enfeitiçador | DA_18_Azir | -0.2000 |  |
| Jogador 5 | 3-6 | 09:20:26 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Enfeitiçador | DA_18_Azir | 0.8300 |  |
| Jogador 5 | 3-7 | 09:20:57 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Azir | 0.2100 |  |
| Jogador 5 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Azir | 0.1700 |  |
| Jogador 5 | 3-7 | 09:20:58 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Enfeitiçador | DA_18_Azir | 0.2000 |  |
| Jogador 5 | 3-7 | 09:20:58 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 3-7 | 09:20:59 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 3-7 | 09:21:00 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 3-7 | 09:21:01 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Azir | -0.2400 |  |
| Jogador 5 | 3-7 | 09:21:01 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 54 | 4 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 3-7 | 09:21:02 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Enfeitiçador | DA_18_Azir | -0.2400 |  |
| Jogador 5 | 4-1 | 09:21:34 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 4-1 | 09:21:35 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_18_Azir | 0.8900 |  |
| Jogador 5 | 4-1 | 09:21:35 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Azir | -0.0200 |  |
| Jogador 5 | 4-1 | 09:21:36 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_18_Azir | -0.0500 |  |
| Jogador 5 | 4-1 | 09:21:36 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-1 | 09:21:37 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 4-1 | 09:21:37 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-1 | 09:21:38 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Azir | 0.0900 |  |
| Jogador 5 | 4-1 | 09:21:38 | MOVE Board -> Board: Karma (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Azir | -0.1400 |  |
| Jogador 5 | 4-2 | 09:22:13 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-2 | 09:22:14 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 76 | 5 | Enfeitiçador | DA_18_Azir | 0.1200 |  |
| Jogador 5 | 4-2 | 09:22:14 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Enfeitiçador | DA_18_Azir | -0.0300 |  |
| Jogador 5 | 4-2 | 09:22:15 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Enfeitiçador | DA_18_Azir | 0.0300 |  |
| Jogador 5 | 4-2 | 09:22:15 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Enfeitiçador | DA_18_Azir | -0.0200 |  |
| Jogador 5 | 4-2 | 09:22:16 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Enfeitiçador | DA_18_Azir | -0.2400 |  |
| Jogador 5 | 4-2 | 09:22:17 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 4-2 | 09:22:18 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 75 | 5 | Enfeitiçador | DA_18_Azir | -0.2700 |  |
| Jogador 5 | 4-2 | 09:22:18 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 77 | 5 | Enfeitiçador | DA_18_Azir | 0.0200 |  |
| Jogador 5 | 4-3 | 09:22:52 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Enfeitiçador | DA_18_Azir | 1.0100 |  |
| Jogador 5 | 4-3 | 09:22:53 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Enfeitiçador | DA_18_Azir | 0.2900 |  |
| Jogador 5 | 4-3 | 09:22:53 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 87 | 5 | Enfeitiçador | DA_18_Azir | 0.5700 |  |
| Jogador 5 | 4-3 | 09:22:54 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 86 | 5 | Enfeitiçador | DA_18_Azir | 0.0500 |  |
| Jogador 5 | 4-3 | 09:22:54 | VENDEU: Karma (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Enfeitiçador | DA_18_Azir | -0.6800 |  |
| Jogador 5 | 4-3 | 09:22:55 | EQUIP_FROM_INVENTORY: TFT_Item_IonicSpark -> Kobuko (i:2.0) (tabuleiro slot 25) | ALL_IN | HP crítico: gastar para sobreviver | 89 | 5 | Enfeitiçador | DA_18_Azir | 0.0900 |  |
| Jogador 5 | 4-3 | 09:22:55 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_18_Azir | 0.7500 |  |
| Jogador 5 | 4-3 | 09:22:56 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Cassiopeia (i:6.0) (tabuleiro slot 8) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_18_Azir | 0.0900 |  |
| Jogador 5 | 4-3 | 09:22:56 | MOVE Board -> Board: Azir (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Enfeitiçador | DA_18_Azir | 0.0300 |  |
| Jogador 5 | 4-4 | 09:23:32 | VENDEU: Soraka (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Enfeitiçador | DA_18_Azir | -0.0600 |  |
| Jogador 5 | 4-4 | 09:23:33 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Enfeitiçador | DA_18_Azir | 0.8600 |  |
| Jogador 5 | 4-4 | 09:23:34 | VENDEU: Sejuani (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Enfeitiçador | DA_18_Azir | -0.4800 |  |
| Jogador 5 | 4-4 | 09:23:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Enfeitiçador | DA_18_Azir | 0.4000 |  |
| Jogador 5 | 4-4 | 09:23:35 | VENDEU: Fiddlesticks (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Enfeitiçador | DA_18_Azir | -0.1400 |  |
| Jogador 5 | 4-4 | 09:23:35 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 103 | 5 | Enfeitiçador | DA_18_Azir | -0.1800 |  |
| Jogador 5 | 4-4 | 09:23:36 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Enfeitiçador | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 4-4 | 09:23:36 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Enfeitiçador | DA_18_Azir | -0.0100 |  |
| Jogador 5 | 4-4 | 09:23:38 | COMPROU: Aphelios (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 98 | 5 | Enfeitiçador | DA_18_Azir | -0.2200 |  |
| Jogador 5 | 4-5 | 09:24:15 | VENDEU: Aphelios (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-5 | 09:24:16 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Enfeitiçador | DA_CrimsonRaptor18 | 1.0600 |  |
| Jogador 5 | 4-5 | 09:24:17 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 110 | 5 | Enfeitiçador | DA_CrimsonRaptor18 | 0.0500 |  |
| Jogador 5 | 4-5 | 09:24:17 | COMPROU: Master Yi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Enfeitiçador | DA_CrimsonRaptor18 | 0.1400 |  |
| Jogador 5 | 4-5 | 09:24:18 | VENDEU: Mamãe Bicuda (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_18_Azir | -0.7200 |  |
| Jogador 5 | 4-5 | 09:24:18 | COMPROU: Warwick (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_18_Azir | -0.2300 |  |
| Jogador 5 | 4-5 | 09:24:19 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Enfeitiçador | DA_18_Azir | -0.0700 |  |
| Jogador 5 | 4-5 | 09:24:19 | VENDEU: Warwick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_18_Azir | 0.0100 |  |
| Jogador 5 | 4-5 | 09:24:20 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Enfeitiçador | DA_18_Azir | 0.7600 |  |
| Jogador 6 | ? | 09:15:30 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2400 |  |
| Jogador 6 | ? | 09:15:31 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | -0.1500 |  |
| Jogador 6 | ? | 09:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 09:15:36 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 09:15:36 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | 1-1 | 09:15:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 09:15:41 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.2200 |  |
| Jogador 6 | 1-2 | 09:15:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.0400 |  |
| Jogador 6 | 1-2 | 09:15:44 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0400 |  |
| Jogador 6 | 1-2 | 09:15:44 | MOVE Board -> Board: Xayah (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 09:15:46 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 6 | 1-2 | 09:15:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-2 | 09:15:48 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.5800 |  |
| Jogador 6 | 1-3 | 09:15:52 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 1.0200 |  |
| Jogador 6 | 1-3 | 09:15:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 09:16:00 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1300 |  |
| Jogador 6 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 6 | 1-4 | 09:16:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.2900 |  |
| Jogador 6 | 1-4 | 09:16:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 6 | 1-4 | 09:16:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 6 | 1-4 | 09:16:05 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0900 |  |
| Jogador 6 | 2-1 | 09:16:09 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.2600 |  |
| Jogador 6 | 2-1 | 09:16:10 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2500 |  |
| Jogador 6 | 2-1 | 09:16:10 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-1 | 09:16:11 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0800 |  |
| Jogador 6 | 2-1 | 09:16:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-2 | 09:16:20 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2900 |  |
| Jogador 6 | 2-2 | 09:16:20 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-2 | 09:16:21 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-2 | 09:16:22 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 09:16:22 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | -0.1500 |  |
| Jogador 6 | 2-2 | 09:16:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Tristana | 0.0000 |  |
| Jogador 6 | 2-3 | 09:16:32 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Tristana | 0.1800 |  |
| Jogador 6 | 2-3 | 09:16:33 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Tristana | 0.2400 |  |
| Jogador 6 | 2-3 | 09:16:33 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | 0.8100 |  |
| Jogador 6 | 2-3 | 09:16:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 09:16:35 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 2-3 | 09:16:35 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1100 |  |
| Jogador 6 | 2-3 | 09:16:36 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-3 | 09:16:36 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-3 | 09:16:36 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 09:16:46 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_Tristana | 0.8600 |  |
| Jogador 6 | 2-4 | 09:16:46 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Feérico | DA_18_Tristana | -0.4200 |  |
| Jogador 6 | 2-4 | 09:16:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_Tristana | -0.1400 |  |
| Jogador 6 | 2-4 | 09:16:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Tristana | -0.0600 |  |
| Jogador 6 | 2-4 | 09:16:48 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 2-4 | 09:16:48 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Tristana | 0.2000 |  |
| Jogador 6 | 2-4 | 09:16:49 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.6300 |  |
| Jogador 6 | 2-4 | 09:16:49 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | 0.3500 |  |
| Jogador 6 | 2-4 | 09:16:50 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_Yorick | -0.4800 |  |
| Jogador 6 | 2-5 | 09:17:01 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 6 | 2-5 | 09:17:01 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.3200 |  |
| Jogador 6 | 2-5 | 09:17:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-5 | 09:17:02 | VENDEU: Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_Yorick | -0.1600 |  |
| Jogador 6 | 2-5 | 09:17:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | -0.0600 |  |
| Jogador 6 | 2-5 | 09:17:04 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_Yorick | -0.4800 |  |
| Jogador 6 | 2-5 | 09:17:04 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_Yorick | -1.0200 |  |
| Jogador 6 | 2-5 | 09:17:05 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.3300 |  |
| Jogador 6 | 2-5 | 09:17:05 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_Yorick | 0.0100 |  |
| Jogador 6 | 2-6 | 09:17:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | 0.3000 |  |
| Jogador 6 | 2-6 | 09:17:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 6 | 2-6 | 09:17:19 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.3800 |  |
| Jogador 6 | 2-6 | 09:17:19 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-6 | 09:17:20 | MOVE Board -> Board: Cascalho (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.0200 |  |
| Jogador 6 | 2-6 | 09:17:20 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 2-6 | 09:17:21 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-6 | 09:17:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 2-7 | 09:17:37 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 6 | 2-7 | 09:17:37 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 6 | 2-7 | 09:17:38 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.1100 |  |
| Jogador 6 | 2-7 | 09:17:39 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.4000 |  |
| Jogador 6 | 2-7 | 09:17:40 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 2-7 | 09:17:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-1 | 09:18:00 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 6 | 3-1 | 09:18:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_KogMaw18_AD | 0.8400 |  |
| Jogador 6 | 3-1 | 09:18:02 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 6 | 3-1 | 09:18:03 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 6 | 3-1 | 09:18:03 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 3-1 | 09:18:04 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 3-1 | 09:18:04 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 6 | 3-1 | 09:18:05 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Xayah (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.1600 |  |
| Jogador 6 | 3-1 | 09:18:05 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Xayah (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 6 | 3-2 | 09:18:27 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | 0.2000 |  |
| Jogador 6 | 3-2 | 09:18:27 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Xayah (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_KogMaw18_AD | 0.1400 |  |
| Jogador 6 | 3-2 | 09:18:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 3-2 | 09:18:28 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 6 | 3-2 | 09:18:29 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-2 | 09:18:30 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.0500 |  |
| Jogador 6 | 3-2 | 09:18:30 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 6 | 3-2 | 09:18:31 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 6 | 3-2 | 09:18:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-3 | 09:18:54 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_KogMaw18_AD | 0.7600 |  |
| Jogador 6 | 3-3 | 09:18:55 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.4700 |  |
| Jogador 6 | 3-3 | 09:18:55 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 3-3 | 09:18:56 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 6 | 3-3 | 09:18:57 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 3-3 | 09:18:57 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 3-3 | 09:18:58 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 3-3 | 09:18:58 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.4000 |  |
| Jogador 6 | 3-3 | 09:18:59 | MOVE Board -> Board: Tristana (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-4 | 09:19:22 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-4 | 09:19:23 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-4 | 09:19:23 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.0600 |  |
| Jogador 6 | 3-4 | 09:19:24 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-4 | 09:19:24 | MOVE Board -> Board: Xayah (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-4 | 09:19:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-5 | 09:19:51 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_KogMaw18_AD | 0.0700 |  |
| Jogador 6 | 3-5 | 09:19:52 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 6 | 3-5 | 09:19:52 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 6 | 3-5 | 09:19:52 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 6 | 3-5 | 09:19:53 | MOVE Board -> Board: Kayle (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | -0.0100 |  |
| Jogador 6 | 3-5 | 09:19:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-6 | 09:20:22 | COMPROU: Gnar (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_GnarSmall | 0.0900 |  |
| Jogador 6 | 3-6 | 09:20:23 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Feérico | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 3-6 | 09:20:23 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-6 | 09:20:24 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 3-6 | 09:20:24 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-6 | 09:20:25 | MOVE Board -> Board: Xayah (i:2.0) <-> Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-6 | 09:20:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_GnarSmall | 0.1300 |  |
| Jogador 6 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_GnarSmall | 0.1300 |  |
| Jogador 6 | 3-7 | 09:20:58 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 3-7 | 09:20:58 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Feérico | DA_18_GnarSmall | 0.4500 |  |
| Jogador 6 | 3-7 | 09:20:59 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 3-7 | 09:21:00 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_GnarSmall | 0.2400 |  |
| Jogador 6 | 3-7 | 09:21:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-7 | 09:21:01 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 3-7 | 09:21:02 | MOVE Board -> Board: Kayle (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Feérico | DA_18_GnarSmall | 0.0500 |  |
| Jogador 6 | 4-1 | 09:21:34 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-1 | 09:21:35 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_GnarSmall | 0.7600 |  |
| Jogador 6 | 4-1 | 09:21:35 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-1 | 09:21:36 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Feérico | DA_18_GnarSmall | 0.7500 |  |
| Jogador 6 | 4-1 | 09:21:36 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_GnarSmall | 0.1500 |  |
| Jogador 6 | 4-1 | 09:21:37 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-1 | 09:21:37 | MOVE Board -> Board: Tristana (i:6.0) <-> Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-1 | 09:21:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 09:22:13 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_GnarSmall | 0.7900 |  |
| Jogador 6 | 4-2 | 09:22:14 | MOVE Board -> Board: Kayle (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 09:22:14 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Feérico | DA_18_GnarSmall | 0.1300 |  |
| Jogador 6 | 4-2 | 09:22:15 | VENDEU: Rammus (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Feérico | DA_18_GnarSmall | 0.0300 |  |
| Jogador 6 | 4-2 | 09:22:15 | COMPROU: Amumu (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 09:22:16 | MOVE Board -> Board: Tristana (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-2 | 09:22:17 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-2 | 09:22:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Feérico | DA_18_GnarSmall | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-3 | 09:22:52 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_GnarSmall | 0.0400 |  |
| Jogador 6 | 4-3 | 09:22:53 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Feérico | DA_18_GnarSmall | 0.3100 |  |
| Jogador 6 | 4-3 | 09:22:53 | VENDEU: Amumu (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-3 | 09:22:54 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Feérico | DA_18_GnarSmall | 0.7300 |  |
| Jogador 6 | 4-3 | 09:22:54 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_GnarSmall | -0.3300 |  |
| Jogador 6 | 4-3 | 09:22:55 | MOVE Board -> Board: Kayle (i:4.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-3 | 09:22:55 | MOVE Board -> Board: Xayah (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-3 | 09:22:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Feérico | DA_18_GnarSmall | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-4 | 09:23:32 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Feérico | DA_18_GnarSmall | 0.0600 |  |
| Jogador 6 | 4-4 | 09:23:33 | VENDEU: Vi (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 1 | Feérico | DA_18_GnarSmall | 0.0300 |  |
| Jogador 6 | 4-4 | 09:23:34 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Feérico | DA_18_GnarSmall | -0.0200 |  |
| Jogador 6 | 4-4 | 09:23:34 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 1 | Feérico | DA_18_GnarSmall | -0.0300 |  |
| Jogador 6 | 4-4 | 09:23:35 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_18_GnarSmall | -0.1500 |  |
| Jogador 6 | 4-4 | 09:23:35 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-4 | 09:23:36 | VENDEU: Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 1 | Feérico | DA_18_GnarSmall | 0.0700 |  |
| Jogador 6 | 4-4 | 09:23:36 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_18_GnarSmall | -0.1100 |  |
| Jogador 6 | 4-4 | 09:23:38 | MOVE Board -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Feérico | DA_18_GnarSmall | 0.0000 |  |
| Jogador 6 | 4-5 | 09:24:15 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Feérico | DA_18_GnarSmall | -0.0100 |  |
| Jogador 6 | 4-5 | 09:24:16 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Feérico | DA_18_GnarSmall | 0.3100 |  |
| Jogador 6 | 4-5 | 09:24:17 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Feérico | DA_18_GnarSmall | 0.0100 |  |
| Jogador 6 | 4-5 | 09:24:17 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Feérico | DA_18_GnarSmall | 0.2400 |  |
| Jogador 6 | 4-5 | 09:24:18 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 2 | Feérico | DA_18_GnarSmall | 0.0900 |  |
| Jogador 6 | 4-5 | 09:24:18 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Feérico | DA_18_GnarSmall | -0.1000 |  |
| Jogador 6 | 4-5 | 09:24:19 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 2 | Feérico | DA_18_GnarSmall | 0.0700 |  |
| Jogador 6 | 4-5 | 09:24:19 | VENDEU: Gnar (i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 2 | Feérico | DA_Fiddlesticks18 | -0.1200 |  |
| Jogador 6 | 4-5 | 09:24:20 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 2 | Feérico | DA_Fiddlesticks18 | -0.1700 |  |
| Jogador 6 | 4-6 | 09:24:59 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 5 | Feérico | DA_Fiddlesticks18 | 0.9500 |  |
| Jogador 6 | 4-6 | 09:25:00 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 5 | Feérico | DA_KogMaw18_AD | 0.9400 |  |
| Jogador 6 | 4-6 | 09:25:00 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 5 | Feérico | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 6 | 4-6 | 09:25:01 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Feérico | DA_Fiddlesticks18 | -0.6300 |  |
| Jogador 6 | 4-6 | 09:25:01 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Feérico | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 6 | 4-6 | 09:25:02 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Feérico | DA_Fiddlesticks18 | -0.3500 |  |
| Jogador 6 | 4-6 | 09:25:02 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Feérico | DA_Fiddlesticks18 | -0.0400 |  |
| Jogador 6 | 4-6 | 09:25:02 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Feérico | DA_Fiddlesticks18 | 0.4200 |  |
| Jogador 6 | 4-6 | 09:25:03 | MOVE Board -> Board: Tristana (i:6.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Feérico | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 6 | 4-7 | 09:25:50 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 70 | 5 | Feérico | DA_Fiddlesticks18 | 1.1100 |  |
| Jogador 6 | 4-7 | 09:25:50 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Feérico | DA_Fiddlesticks18 | 1.1000 |  |
| Jogador 6 | 4-7 | 09:25:51 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Feérico | DA_Fiddlesticks18 | 0.1300 |  |
| Jogador 6 | 4-7 | 09:25:51 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Feérico | DA_Fiddlesticks18 | 0.1400 |  |
| Jogador 6 | 4-7 | 09:25:52 | MOVE Bench -> Board: Rakan (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Feérico | DA_Fiddlesticks18 | -0.3600 |  |
| Jogador 6 | 4-7 | 09:25:52 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Feérico | DA_Fiddlesticks18 | 0.2700 |  |
| Jogador 6 | 4-7 | 09:25:53 | COMPROU: Aphelios (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Feérico | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 6 | 4-7 | 09:25:53 | MOVE Bench -> Board: Aphelios (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Feérico | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 6 | 4-7 | 09:25:54 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 5 | Feérico | DA_Fiddlesticks18 | -0.2500 |  |
| Jogador 6 | 5-1 | 09:26:39 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_Fiddlesticks18 | 0.0600 |  |
| Jogador 6 | 5-1 | 09:26:39 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 67 | 5 | Feérico | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 6 | 5-1 | 09:26:40 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Feérico | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 6 | 5-1 | 09:26:41 | VENDEU: Kayle (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Feérico | DA_Fiddlesticks18 | -0.6000 |  |
| Jogador 6 | 5-1 | 09:26:42 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 6 | 5-1 | 09:26:42 | MOVE Board -> Board: Aphelios (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Feérico | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 6 | 5-1 | 09:26:43 | REROLL | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Feérico | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 6 | 5-1 | 09:26:44 | VENDEU: Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Feérico | DA_18_Tristana | -0.5800 |  |
| Jogador 6 | 5-1 | 09:26:45 | MOVE Bench -> Board: Caitlyn (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 74 | 5 | Feérico | DA_18_Tristana | 0.3700 |  |
| Jogador 6 | 5-2 | 09:27:36 | COMPROU: Alistar (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 83 | 5 | Feérico | DA_18_Tristana | 0.5700 |  |
| Jogador 6 | 5-2 | 09:27:37 | COMPROU: Zyra (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Tristana | 0.1400 |  |
| Jogador 6 | 5-2 | 09:27:37 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Tristana (i:6.0) (tabuleiro slot 24) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Tristana | 0.1200 |  |
| Jogador 6 | 5-2 | 09:27:38 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Tristana (i:6.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Feérico | DA_18_Tristana | 0.1700 |  |
| Jogador 6 | 5-2 | 09:27:39 | VENDEU: Varus (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Feérico | DA_18_Tristana | -0.0300 |  |
| Jogador 6 | 5-2 | 09:27:39 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Feérico | DA_18_Tristana | 0.0200 |  |
| Jogador 6 | 5-2 | 09:27:39 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Feérico | DA_18_Tristana | -0.0700 |  |
| Jogador 6 | 5-2 | 09:27:40 | VENDEU: Aronguejo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Feérico | DA_18_Tristana | -0.0100 |  |
| Jogador 6 | 5-2 | 09:27:40 | COMPROU: Krugue (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Feérico | DA_18_Tristana | -0.2600 |  |
| Jogador 7 | ? | 09:15:30 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2900 |  |
| Jogador 7 | ? | 09:15:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 09:15:36 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 09:15:36 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 1-1 | 09:15:37 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-1 | 09:15:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 1-1 | 09:15:39 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 09:15:40 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-1 | 09:15:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 09:15:41 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 7 | 1-2 | 09:15:43 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 09:15:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 09:15:44 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-2 | 09:15:46 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 09:15:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 09:15:47 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 09:15:52 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 7 | 1-3 | 09:15:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-3 | 09:15:53 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 09:15:53 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2000 |  |
| Jogador 7 | 1-3 | 09:15:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 09:16:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8300 |  |
| Jogador 7 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 7 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2500 |  |
| Jogador 7 | 1-4 | 09:16:02 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 7 | 1-4 | 09:16:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 09:16:05 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.4400 |  |
| Jogador 7 | 2-1 | 09:16:09 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 2-1 | 09:16:10 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 7 | 2-1 | 09:16:10 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 7 | 2-1 | 09:16:11 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 2-1 | 09:16:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 09:16:12 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 2-1 | 09:16:13 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | -0.6300 |  |
| Jogador 7 | 2-2 | 09:16:20 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Hecarim | 1.0500 |  |
| Jogador 7 | 2-2 | 09:16:20 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.6800 |  |
| Jogador 7 | 2-2 | 09:16:21 | EQUIP_FROM_INVENTORY: TFT_Item_Quicksilver -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 2-2 | 09:16:22 | EQUIP_FROM_INVENTORY: TFT_Item_RedBuff -> Rakan (i:2.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 2-2 | 09:16:22 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.1000 |  |
| Jogador 7 | 2-2 | 09:16:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 2-3 | 09:16:32 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Hecarim | 0.3100 |  |
| Jogador 7 | 2-3 | 09:16:33 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Sentinel18 | 0.2100 |  |
| Jogador 7 | 2-3 | 09:16:33 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Sentinel18 | -0.1300 |  |
| Jogador 7 | 2-3 | 09:16:34 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-3 | 09:16:35 | MOVE Board -> Board: Varus (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Sentinel18 | -0.3200 |  |
| Jogador 7 | 2-3 | 09:16:35 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.0800 |  |
| Jogador 7 | 2-3 | 09:16:36 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Sentinel18 | 0.2300 |  |
| Jogador 7 | 2-3 | 09:16:36 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | -0.1100 |  |
| Jogador 7 | 2-3 | 09:16:36 | MOVE Board -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-4 | 09:16:46 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.3200 |  |
| Jogador 7 | 2-4 | 09:16:46 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Sentinel18 | 0.3300 |  |
| Jogador 7 | 2-4 | 09:16:47 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_Sentinel18 | -0.0600 |  |
| Jogador 7 | 2-4 | 09:16:47 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.4600 |  |
| Jogador 7 | 2-4 | 09:16:48 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-4 | 09:16:48 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 2-5 | 09:17:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_Sentinel18 | 1.0100 |  |
| Jogador 7 | 2-5 | 09:17:01 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | 0.9600 |  |
| Jogador 7 | 2-5 | 09:17:02 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 2-5 | 09:17:02 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_Sentinel18 | -0.6200 |  |
| Jogador 7 | 2-5 | 09:17:03 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_Sentinel18 | -0.6300 |  |
| Jogador 7 | 2-5 | 09:17:04 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 2-5 | 09:17:04 | VENDEU: Azuporã (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.6300 |  |
| Jogador 7 | 2-5 | 09:17:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-5 | 09:17:05 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0100 |  |
| Jogador 7 | 2-6 | 09:17:18 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.2800 |  |
| Jogador 7 | 2-6 | 09:17:18 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-6 | 09:17:19 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 2-6 | 09:17:19 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0200 |  |
| Jogador 7 | 2-6 | 09:17:20 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.0400 |  |
| Jogador 7 | 2-6 | 09:17:20 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0600 |  |
| Jogador 7 | 2-6 | 09:17:21 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -1.0200 |  |
| Jogador 7 | 2-6 | 09:17:21 | MOVE Board -> Board: Hecarim (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 2-6 | 09:17:22 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.2200 |  |
| Jogador 7 | 2-7 | 09:17:37 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.2800 |  |
| Jogador 7 | 2-7 | 09:17:37 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | 0.1900 |  |
| Jogador 7 | 2-7 | 09:17:38 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 2-7 | 09:17:39 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.6200 |  |
| Jogador 7 | 2-7 | 09:17:40 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 2-7 | 09:17:40 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 2-7 | 09:17:40 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 7 | 2-7 | 09:17:41 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 7 | 2-7 | 09:17:41 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 3-1 | 09:18:00 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.2700 |  |
| Jogador 7 | 3-1 | 09:18:01 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.2500 |  |
| Jogador 7 | 3-1 | 09:18:02 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0500 |  |
| Jogador 7 | 3-1 | 09:18:03 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0900 |  |
| Jogador 7 | 3-1 | 09:18:03 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.3300 |  |
| Jogador 7 | 3-1 | 09:18:04 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-1 | 09:18:04 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | 0.3100 |  |
| Jogador 7 | 3-1 | 09:18:05 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_KogMaw18_AD | -0.2000 |  |
| Jogador 7 | 3-1 | 09:18:05 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 09:18:27 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.0900 |  |
| Jogador 7 | 3-2 | 09:18:27 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | 0.1700 |  |
| Jogador 7 | 3-2 | 09:18:28 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 7 | 3-2 | 09:18:28 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.4300 |  |
| Jogador 7 | 3-2 | 09:18:29 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 7 | 3-2 | 09:18:30 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | -0.1000 |  |
| Jogador 7 | 3-2 | 09:18:30 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_KogMaw18_AD | -0.2600 |  |
| Jogador 7 | 3-2 | 09:18:31 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-2 | 09:18:31 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_KogMaw18_AD | -0.0300 |  |
| Jogador 7 | 3-3 | 09:18:54 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_KogMaw18_AD | 0.8100 |  |
| Jogador 7 | 3-3 | 09:18:55 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_KogMaw18_AD | 0.8300 |  |
| Jogador 7 | 3-3 | 09:18:55 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Varus | -0.5400 |  |
| Jogador 7 | 3-3 | 09:18:56 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | -0.0700 |  |
| Jogador 7 | 3-3 | 09:18:57 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.2800 |  |
| Jogador 7 | 3-3 | 09:18:57 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 3-3 | 09:18:58 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.1500 |  |
| Jogador 7 | 3-3 | 09:18:58 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.2900 |  |
| Jogador 7 | 3-3 | 09:18:59 | MOVE Board -> Board: Diana (i:6.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-4 | 09:19:22 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.0500 |  |
| Jogador 7 | 3-4 | 09:19:23 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.1500 |  |
| Jogador 7 | 3-4 | 09:19:23 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0800 |  |
| Jogador 7 | 3-4 | 09:19:24 | MOVE Board -> Board: Varus (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-4 | 09:19:24 | MOVE Board -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-4 | 09:19:25 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-4 | 09:19:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-5 | 09:19:51 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Varus | 0.2800 |  |
| Jogador 7 | 3-5 | 09:19:52 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.2300 |  |
| Jogador 7 | 3-5 | 09:19:52 | MOVE Board -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-5 | 09:19:52 | MOVE Board -> Board: Hecarim (i:6.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 3-5 | 09:19:53 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-6 | 09:20:22 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.8000 |  |
| Jogador 7 | 3-6 | 09:20:23 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Varus | 0.0200 |  |
| Jogador 7 | 3-6 | 09:20:23 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.2900 |  |
| Jogador 7 | 3-6 | 09:20:24 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-6 | 09:20:24 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-6 | 09:20:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Varus | 0.1800 |  |
| Jogador 7 | 3-7 | 09:20:57 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Varus | 0.0600 |  |
| Jogador 7 | 3-7 | 09:20:58 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Varus | 0.0700 |  |
| Jogador 7 | 3-7 | 09:20:58 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.2800 |  |
| Jogador 7 | 3-7 | 09:20:59 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Varus | 0.0600 |  |
| Jogador 7 | 3-7 | 09:21:00 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 3-7 | 09:21:01 | MOVE Board -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 3-7 | 09:21:01 | MOVE Board -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 3-7 | 09:21:02 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-1 | 09:21:34 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Varus | -0.0300 |  |
| Jogador 7 | 4-1 | 09:21:35 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Varus | 0.2800 |  |
| Jogador 7 | 4-1 | 09:21:35 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Varus | -0.4300 |  |
| Jogador 7 | 4-1 | 09:21:36 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Varus | 0.8000 |  |
| Jogador 7 | 4-1 | 09:21:36 | MOVE Board -> Board: Hecarim (i:6.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-1 | 09:21:37 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-1 | 09:21:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-1 | 09:21:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Varus | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-2 | 09:22:13 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_18_Varus | -0.4200 |  |
| Jogador 7 | 4-2 | 09:22:14 | COMPROU: Soraka (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_18_Varus | -0.2400 |  |
| Jogador 7 | 4-2 | 09:22:14 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_18_Varus | 0.0900 |  |
| Jogador 7 | 4-2 | 09:22:15 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-2 | 09:22:15 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-2 | 09:22:16 | MOVE Board -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-2 | 09:22:17 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_18_Varus | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-3 | 09:22:52 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Colosso | DA_18_Varus | 0.0700 |  |
| Jogador 7 | 4-3 | 09:22:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 2 | Colosso | DA_18_Varus | 0.6800 |  |
| Jogador 7 | 4-3 | 09:22:53 | VENDEU: Soraka (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Colosso | DA_18_Varus | 0.0700 |  |
| Jogador 7 | 4-3 | 09:22:54 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Colosso | DA_18_Varus | 0.2400 |  |
| Jogador 7 | 4-3 | 09:22:54 | MOVE Board -> Board: Diana (i:6.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 4-3 | 09:22:55 | MOVE Board -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-3 | 09:22:55 | MOVE Board -> Board: Varus (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-3 | 09:22:56 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Colosso | DA_18_Varus | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-4 | 09:23:32 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_18_Varus | -0.5600 |  |
| Jogador 7 | 4-4 | 09:23:33 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 33 | 2 | Colosso | DA_18_Varus | 0.7600 |  |
| Jogador 7 | 4-4 | 09:23:34 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_18_Varus | -0.5300 |  |
| Jogador 7 | 4-4 | 09:23:34 | COMPROU: Ezreal (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Colosso | DA_18_Varus | -0.2400 |  |
| Jogador 7 | 4-4 | 09:23:35 | VENDEU: Ezreal (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Colosso | DA_18_Varus | 0.0100 |  |
| Jogador 7 | 4-4 | 09:23:35 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-4 | 09:23:36 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Varus | 0.0000 |  |
| Jogador 7 | 4-4 | 09:23:36 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Varus | -0.0200 |  |
| Jogador 7 | 4-4 | 09:23:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Colosso | DA_18_Varus | -0.0400 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-5 | 09:24:15 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 3 | Colosso | DA_18_Varus | -0.0100 |  |
| Jogador 7 | 4-5 | 09:24:16 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Colosso | DA_18_Varus | 0.9300 |  |
| Jogador 7 | 4-5 | 09:24:17 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_18_Hecarim | 0.8900 |  |
| Jogador 7 | 4-5 | 09:24:17 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Colosso | DA_18_Hecarim | 0.3500 |  |
| Jogador 7 | 4-5 | 09:24:18 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Hecarim | 0.2200 |  |
| Jogador 7 | 4-5 | 09:24:18 | MOVE Board -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-5 | 09:24:19 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 4-5 | 09:24:19 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Hecarim | 0.3800 |  |
| Jogador 7 | 4-5 | 09:24:20 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-6 | 09:24:59 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Colosso | DA_18_Hecarim | 0.8100 |  |
| Jogador 7 | 4-6 | 09:25:00 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Hecarim | -0.0800 |  |
| Jogador 7 | 4-6 | 09:25:00 | MOVE Board -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Hecarim | 0.0000 |  |
| Jogador 7 | 4-6 | 09:25:01 | MOVE Board -> Board: Yorick (i:2.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Hecarim | -0.0200 |  |
| Jogador 7 | 4-6 | 09:25:01 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Colosso | DA_18_Hecarim | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-7 | 09:25:50 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_18_Hecarim | 0.1400 |  |
| Jogador 7 | 4-7 | 09:25:50 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Varus (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Colosso | DA_18_Hecarim | 0.1100 |  |
| Jogador 7 | 4-7 | 09:25:51 | VENDEU: Hecarim (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 4 | Colosso | DA_Sentinel18 | -0.4700 |  |
| Jogador 7 | 4-7 | 09:25:51 | COMPROU: Ashe (Custo 5 \| i:10.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Colosso | DA_Sentinel18 | 0.0400 |  |
| Jogador 7 | 4-7 | 09:25:52 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 58 | 4 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-7 | 09:25:52 | VENDEU: Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 61 | 4 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 4-7 | 09:25:53 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 4-7 | 09:25:53 | MOVE Board -> Board: Varus (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 4-7 | 09:25:54 | MOVE Board -> Board: Yorick (i:2.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 4 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-1 | 09:26:39 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-1 | 09:26:39 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 71 | 5 | Colosso | DA_Sentinel18 | 0.4500 |  |
| Jogador 7 | 5-1 | 09:26:40 | VENDEU: Ashe (i:10.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-1 | 09:26:41 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 73 | 5 | Colosso | DA_Sentinel18 | 0.1200 |  |
| Jogador 7 | 5-1 | 09:26:42 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 76 | 5 | Colosso | DA_Sentinel18 | -0.0400 |  |
| Jogador 7 | 5-1 | 09:26:42 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Colosso | DA_Sentinel18 | 0.0900 |  |
| Jogador 7 | 5-1 | 09:26:43 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-1 | 09:26:44 | MOVE Board -> Board: Rakan (i:4.0) <-> Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-1 | 09:26:45 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 74 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-2 | 09:27:36 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-2 | 09:27:37 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 09:27:37 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-2 | 09:27:38 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 09:27:39 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 84 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 09:27:39 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 86 | 5 | Colosso | DA_Sentinel18 | -0.0100 |  |
| Jogador 7 | 5-2 | 09:27:39 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Colosso | DA_Sentinel18 | -0.2200 |  |
| Jogador 7 | 5-2 | 09:27:40 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-2 | 09:27:40 | MOVE Board -> Board: Yorick (i:2.0) <-> Varus (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-3 | 09:28:26 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 97 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-3 | 09:28:27 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 95 | 5 | Colosso | DA_Sentinel18 | 1.0500 |  |
| Jogador 7 | 5-3 | 09:28:27 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 92 | 5 | Colosso | DA_Sentinel18 | 0.9000 |  |
| Jogador 7 | 5-3 | 09:28:28 | COMPROU: Sett (Custo 4 \| i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 88 | 5 | Colosso | DA_Sentinel18 | 0.0500 |  |
| Jogador 7 | 5-3 | 09:28:28 | VENDEU: Aronguejo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Colosso | DA_Sentinel18 | -0.7000 |  |
| Jogador 7 | 5-3 | 09:28:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Colosso | DA_Sentinel18 | 0.1100 |  |
| Jogador 7 | 5-3 | 09:28:31 | MOVE Board -> Board: Varus (i:4.0) <-> Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-3 | 09:28:31 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 93 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-3 | 09:28:32 | COMPROU: Yunara (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 91 | 5 | Colosso | DA_Sentinel18 | 0.0300 |  |
| Jogador 7 | 5-4 | 09:29:18 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Colosso | DA_Sentinel18 | -0.0300 |  |
| Jogador 7 | 5-4 | 09:29:19 | COMPROU: Vi (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 101 | 5 | Colosso | DA_Sentinel18 | 0.4300 |  |
| Jogador 7 | 5-4 | 09:29:19 | VENDEU: Sett (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Colosso | DA_Sentinel18 | -0.0200 |  |
| Jogador 7 | 5-4 | 09:29:20 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Colosso | DA_Sentinel18 | 0.2000 |  |
| Jogador 7 | 5-4 | 09:29:20 | VENDEU: Akali (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Colosso | DA_Sentinel18 | -0.0700 |  |
| Jogador 7 | 5-4 | 09:29:21 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Colosso | DA_Sentinel18 | -0.2300 |  |
| Jogador 7 | 5-4 | 09:29:21 | VENDEU: Kha'Zix (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 105 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 7 | 5-4 | 09:29:21 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Colosso | DA_Sentinel18 | -0.2800 |  |
| Jogador 7 | 5-4 | 09:29:22 | MOVE Board -> Board: Rakan (i:4.0) <-> Lobo Trevoguari (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 102 | 5 | Colosso | DA_Sentinel18 | 0.0000 |  |
| Jogador 8 | ? | 09:15:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | ? | 09:15:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 8 | ? | 09:15:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 09:15:36 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 09:15:36 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 8 | 1-1 | 09:15:37 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 8 | 1-1 | 09:15:38 | MOVE Board -> Board: Karma (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3600 |  |
| Jogador 8 | 1-1 | 09:15:39 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 8 | 1-1 | 09:15:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 09:15:41 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.5000 |  |
| Jogador 8 | 1-2 | 09:15:43 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 8 | 1-2 | 09:15:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3600 |  |
| Jogador 8 | 1-2 | 09:15:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-3 | 09:15:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.2800 |  |
| Jogador 8 | 1-3 | 09:15:52 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 8 | 1-3 | 09:15:53 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1700 |  |
| Jogador 8 | 1-3 | 09:15:53 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 8 | 1-3 | 09:15:54 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1200 |  |
| Jogador 8 | 1-3 | 09:15:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-4 | 09:16:00 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.1100 |  |
| Jogador 8 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 1-4 | 09:16:01 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 1-4 | 09:16:02 | MOVE Bench -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 1-4 | 09:16:02 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 1.1000 |  |
| Jogador 8 | 1-4 | 09:16:02 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 1-4 | 09:16:05 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Karma18 | 0.4100 |  |
| Jogador 8 | 1-4 | 09:16:06 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-1 | 09:16:09 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-1 | 09:16:10 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2100 |  |
| Jogador 8 | 2-1 | 09:16:10 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 2-1 | 09:16:11 | MOVE Board -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-1 | 09:16:12 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.0500 |  |
| Jogador 8 | 2-1 | 09:16:12 | MOVE Bench -> Board: Teemo (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.5000 |  |
| Jogador 8 | 2-1 | 09:16:13 | MOVE Bench -> Board: Karma (i:4.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-2 | 09:16:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_Karma18 | 0.9900 |  |
| Jogador 8 | 2-2 | 09:16:20 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_Karma18 | 1.0500 |  |
| Jogador 8 | 2-2 | 09:16:21 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.3700 |  |
| Jogador 8 | 2-2 | 09:16:22 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | 0.4100 |  |
| Jogador 8 | 2-2 | 09:16:22 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | 0.3000 |  |
| Jogador 8 | 2-2 | 09:16:22 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_Karma18 | -0.6300 |  |
| Jogador 8 | 2-2 | 09:16:23 | BUY XP | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.0400 |  |
| Jogador 8 | 2-2 | 09:16:23 | MOVE Board -> Board: Xayah (i:4.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0000 |  |
| Jogador 8 | 2-2 | 09:16:23 | MOVE Board -> Board: Karma (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.1800 |  |
| Jogador 8 | 2-3 | 09:16:32 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-3 | 09:16:33 | COMPROU: Kha'Zix (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 2-3 | 09:16:33 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.3500 |  |
| Jogador 8 | 2-3 | 09:16:34 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-3 | 09:16:35 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1800 |  |
| Jogador 8 | 2-3 | 09:16:35 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_Karma18 | -0.4100 |  |
| Jogador 8 | 2-3 | 09:16:36 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.1400 |  |
| Jogador 8 | 2-3 | 09:16:36 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-3 | 09:16:36 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_Karma18 | -0.0300 |  |
| Jogador 8 | 2-4 | 09:16:46 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Enfeitiçador | DA_Karma18 | 0.9000 |  |
| Jogador 8 | 2-4 | 09:16:46 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | 0.8600 |  |
| Jogador 8 | 2-4 | 09:16:47 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Enfeitiçador | DA_Karma18 | 0.1200 |  |
| Jogador 8 | 2-4 | 09:16:47 | VENDEU: Kha'Zix (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 2-4 | 09:16:48 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 2-4 | 09:16:48 | VENDEU: Master Yi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 2-4 | 09:16:49 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Enfeitiçador | DA_Karma18 | -0.3400 |  |
| Jogador 8 | 2-4 | 09:16:49 | VENDEU: Rammus (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Enfeitiçador | DA_Karma18 | -0.4200 |  |
| Jogador 8 | 2-4 | 09:16:50 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Enfeitiçador | DA_Karma18 | 0.0800 |  |
| Jogador 8 | 2-5 | 09:17:01 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Enfeitiçador | DA_Karma18 | 0.2800 |  |
| Jogador 8 | 2-5 | 09:17:01 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | 0.2000 |  |
| Jogador 8 | 2-5 | 09:17:02 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_Karma18 | 0.1700 |  |
| Jogador 8 | 2-5 | 09:17:02 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Enfeitiçador | DA_Karma18 | -0.6100 |  |
| Jogador 8 | 2-5 | 09:17:03 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | -0.3800 |  |
| Jogador 8 | 2-5 | 09:17:04 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | -0.1000 |  |
| Jogador 8 | 2-5 | 09:17:04 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Enfeitiçador | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 2-5 | 09:17:05 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 2-5 | 09:17:05 | VENDEU: Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | -0.4300 |  |
| Jogador 8 | 2-6 | 09:17:18 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_Karma18 | 0.8900 |  |
| Jogador 8 | 2-6 | 09:17:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_Karma18 | 0.0500 |  |
| Jogador 8 | 2-6 | 09:17:19 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Enfeitiçador | DA_Karma18 | 0.1100 |  |
| Jogador 8 | 2-6 | 09:17:19 | VENDEU: Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-6 | 09:17:20 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_Karma18 | -0.3200 |  |
| Jogador 8 | 2-6 | 09:17:20 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-6 | 09:17:21 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-6 | 09:17:21 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Enfeitiçador | DA_Karma18 | -0.5600 |  |
| Jogador 8 | 2-6 | 09:17:22 | VENDEU: Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Enfeitiçador | DA_Karma18 | -0.1400 |  |
| Jogador 8 | 2-7 | 09:17:37 | COMPROU: Lillia (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.0900 |  |
| Jogador 8 | 2-7 | 09:17:37 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_SparringGloves -> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.2600 |  |
| Jogador 8 | 2-7 | 09:17:38 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.0800 |  |
| Jogador 8 | 2-7 | 09:17:39 | MOVE Bench -> Board: Elise (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.3900 |  |
| Jogador 8 | 2-7 | 09:17:40 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.1800 |  |
| Jogador 8 | 2-7 | 09:17:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Enfeitiçador | DA_Karma18 | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-1 | 09:18:00 | COMPROU: Rubrivira (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Enfeitiçador | DA_Karma18 | -0.0900 |  |
| Jogador 8 | 3-1 | 09:18:01 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | -0.0100 |  |
| Jogador 8 | 3-1 | 09:18:02 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.0600 |  |
| Jogador 8 | 3-1 | 09:18:03 | MOVE Bench -> Board: Elise (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | -0.1300 |  |
| Jogador 8 | 3-1 | 09:18:03 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.0700 |  |
| Jogador 8 | 3-1 | 09:18:04 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | 0.0300 |  |
| Jogador 8 | 3-1 | 09:18:04 | MOVE Bench -> Board: Elise (i:4.0) <-> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | -0.4000 |  |
| Jogador 8 | 3-1 | 09:18:05 | MOVE Bench -> Board: Cassiopeia (i:6.0) <-> Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | -0.3800 |  |
| Jogador 8 | 3-1 | 09:18:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Enfeitiçador | DA_Karma18 | -0.1200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-2 | 09:18:27 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Enfeitiçador | DA_Karma18 | 0.2400 |  |
| Jogador 8 | 3-2 | 09:18:27 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Enfeitiçador | DA_18_Xayah | -0.5000 |  |
| Jogador 8 | 3-2 | 09:18:28 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_18_Xayah | 0.5700 |  |
| Jogador 8 | 3-2 | 09:18:28 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Cassiopeia (i:6.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Enfeitiçador | DA_18_Xayah | 0.1600 |  |
| Jogador 8 | 3-2 | 09:18:29 | VENDEU: Rubrivira (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Enfeitiçador | DA_18_Xayah | 0.0100 |  |
| Jogador 8 | 3-2 | 09:18:30 | VENDEU: Lillia (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Xayah | -0.0700 |  |
| Jogador 8 | 3-2 | 09:18:30 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Enfeitiçador | DA_18_Xayah | 0.3000 |  |
| Jogador 8 | 3-2 | 09:18:31 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Enfeitiçador | DA_18_Xayah | -0.2300 |  |
| Jogador 8 | 3-2 | 09:18:31 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Enfeitiçador | DA_18_Xayah | -0.4200 |  |
| Jogador 8 | 3-3 | 09:18:54 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_18_Xayah | 0.9400 |  |
| Jogador 8 | 3-3 | 09:18:55 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Xayah | 0.9000 |  |
| Jogador 8 | 3-3 | 09:18:55 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 62 | 5 | Enfeitiçador | DA_18_Xayah | -0.6400 |  |
| Jogador 8 | 3-3 | 09:18:56 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 59 | 5 | Enfeitiçador | DA_18_Xayah | 0.0800 |  |
| Jogador 8 | 3-3 | 09:18:57 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 60 | 5 | Enfeitiçador | DA_18_Xayah | -0.0900 |  |
| Jogador 8 | 3-3 | 09:18:57 | VENDEU: Mamãe Bicuda (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 63 | 5 | Enfeitiçador | DA_18_Xayah | -0.4100 |  |
| Jogador 8 | 3-3 | 09:18:58 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 64 | 5 | Enfeitiçador | DA_18_Xayah | -0.6400 |  |
| Jogador 8 | 3-3 | 09:18:58 | VENDEU: Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 65 | 5 | Enfeitiçador | DA_18_Xayah | -0.9800 |  |
| Jogador 8 | 3-3 | 09:18:59 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 67 | 5 | Enfeitiçador | DA_18_Xayah | -0.8600 |  |
| Jogador 8 | 3-4 | 09:19:22 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Enfeitiçador | DA_18_Xayah | 0.9900 |  |
| Jogador 8 | 3-4 | 09:19:23 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_18_Xayah | 0.4000 |  |
| Jogador 8 | 3-4 | 09:19:23 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Enfeitiçador | DA_18_Xayah | 0.9500 |  |
| Jogador 8 | 3-4 | 09:19:24 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 68 | 5 | Enfeitiçador | DA_18_Xayah | -0.2600 |  |
| Jogador 8 | 3-4 | 09:19:24 | VENDEU: Yunara (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 70 | 5 | Enfeitiçador | DA_18_Xayah | -0.3300 |  |
| Jogador 8 | 3-4 | 09:19:25 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 72 | 5 | Enfeitiçador | DA_18_Xayah | -0.4100 |  |
| Jogador 8 | 3-4 | 09:19:26 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 74 | 5 | Enfeitiçador | DA_18_Xayah | -0.6600 |  |
| Jogador 8 | 3-4 | 09:19:26 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 76 | 5 | Enfeitiçador | DA_18_Xayah | -0.2400 |  |
| Jogador 8 | 3-4 | 09:19:27 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 75 | 5 | Enfeitiçador | DA_18_Xayah | -0.2700 |  |
| Jogador 8 | 3-5 | 09:19:51 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 84 | 5 | Enfeitiçador | DA_18_Xayah | 0.9500 |  |
| Jogador 8 | 3-5 | 09:19:52 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 82 | 5 | Enfeitiçador | DA_18_Xayah | 0.8300 |  |
| Jogador 8 | 3-5 | 09:19:52 | COMPROU: Malphite (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 78 | 5 | Enfeitiçador | DA_18_Xayah | 0.1100 |  |
| Jogador 8 | 3-5 | 09:19:52 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 79 | 5 | Enfeitiçador | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 3-5 | 09:19:53 | VENDEU: Malphite (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 83 | 5 | Enfeitiçador | DA_18_Xayah | -0.4000 |  |
| Jogador 8 | 3-5 | 09:19:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 80 | 5 | Enfeitiçador | DA_18_Xayah | 0.0300 |  |
| Jogador 8 | 3-5 | 09:19:54 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 83 | 5 | Enfeitiçador | DA_18_Xayah | -0.3800 |  |
| Jogador 8 | 3-5 | 09:19:55 | VENDEU: Elise (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 85 | 5 | Enfeitiçador | DA_18_Xayah | -0.5500 |  |
| Jogador 8 | 3-5 | 09:19:55 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 86 | 5 | Enfeitiçador | DA_18_Xayah | -1.0000 |  |
| Jogador 8 | 3-6 | 09:20:22 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 96 | 5 | Enfeitiçador | DA_18_Xayah | 0.4800 |  |
| Jogador 8 | 3-6 | 09:20:23 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 93 | 5 | Enfeitiçador | DA_18_Xayah | 0.0900 |  |
| Jogador 8 | 3-6 | 09:20:23 | COMPROU: Rengar (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Enfeitiçador | DA_18_Xayah | -0.0200 |  |
| Jogador 8 | 3-6 | 09:20:24 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Enfeitiçador | DA_18_Xayah | -0.2600 |  |
| Jogador 8 | 3-6 | 09:20:24 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 88 | 5 | Enfeitiçador | DA_18_Xayah | 0.4100 |  |
| Jogador 8 | 3-6 | 09:20:25 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Enfeitiçador | DA_18_Xayah | -0.0400 |  |
| Jogador 8 | 3-6 | 09:20:25 | MOVE Board -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Enfeitiçador | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 3-6 | 09:20:26 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Elise (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Enfeitiçador | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 3-6 | 09:20:26 | MOVE Board -> Board: Elise (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 87 | 5 | Enfeitiçador | DA_18_Xayah | -0.0200 |  |
| Jogador 8 | 3-7 | 09:20:57 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 97 | 5 | Enfeitiçador | DA_18_Xayah | 1.0100 |  |
| Jogador 8 | 3-7 | 09:20:57 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 95 | 5 | Enfeitiçador | DA_18_Xayah | 0.3700 |  |
| Jogador 8 | 3-7 | 09:20:58 | COMPROU: Mamãe Bicuda (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Enfeitiçador | DA_18_Xayah | 0.1600 |  |
| Jogador 8 | 3-7 | 09:20:58 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Enfeitiçador | DA_18_Xayah | 0.0800 |  |
| Jogador 8 | 3-7 | 09:20:59 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Enfeitiçador | DA_18_Xayah | 0.2500 |  |
| Jogador 8 | 3-7 | 09:21:00 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Cassiopeia (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Enfeitiçador | DA_18_Xayah | 0.2500 |  |
| Jogador 8 | 3-7 | 09:21:01 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Enfeitiçador | DA_18_Xayah | 0.0100 |  |
| Jogador 8 | 3-7 | 09:21:01 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 90 | 5 | Enfeitiçador | DA_18_Xayah | 0.1300 |  |
| Jogador 8 | 3-7 | 09:21:02 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 91 | 5 | Enfeitiçador | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 4-1 | 09:21:34 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Enfeitiçador | DA_18_Xayah | 0.7800 |  |
| Jogador 8 | 4-1 | 09:21:35 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Enfeitiçador | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 4-1 | 09:21:35 | COMPROU: Elise (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Enfeitiçador | DA_18_Xayah | 0.5600 |  |
| Jogador 8 | 4-1 | 09:21:36 | VENDEU: Rengar (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Enfeitiçador | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 4-1 | 09:21:36 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Enfeitiçador | DA_18_Xayah | 0.0700 |  |
| Jogador 8 | 4-1 | 09:21:37 | VENDEU: Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 104 | 5 | Enfeitiçador | DA_18_Xayah | -0.0200 |  |
| Jogador 8 | 4-1 | 09:21:37 | COMPROU: Sivir (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: pressão de vida | 100 | 5 | Enfeitiçador | DA_18_Xayah | -0.1900 |  |
| Jogador 8 | 4-1 | 09:21:38 | VENDEU: Azir (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 103 | 5 | Enfeitiçador | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 4-1 | 09:21:38 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 101 | 5 | Enfeitiçador | DA_18_Xayah | -0.2100 |  |
| Jogador 8 | 4-2 | 09:22:13 | VENDEU: Grompe (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_18_Xayah | 0.0100 |  |
| Jogador 8 | 4-2 | 09:22:14 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Enfeitiçador | DA_18_Xayah | 0.3800 |  |
| Jogador 8 | 4-2 | 09:22:14 | VENDEU: Mamãe Bicuda (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 114 | 5 | Enfeitiçador | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 4-2 | 09:22:15 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Enfeitiçador | DA_18_Xayah | 0.2400 |  |
| Jogador 8 | 4-2 | 09:22:15 | VENDEU: Sivir (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 4-2 | 09:22:16 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 112 | 5 | Enfeitiçador | DA_18_Xayah | 0.1500 |  |
| Jogador 8 | 4-2 | 09:22:17 | VENDEU: Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_18_Xayah | -0.0300 |  |
| Jogador 8 | 4-2 | 09:22:18 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Enfeitiçador | DA_18_Xayah | -0.1600 |  |
| Jogador 8 | 4-2 | 09:22:18 | VENDEU: Teemo (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Enfeitiçador | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 4-3 | 09:22:52 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Enfeitiçador | DA_18_Xayah | 0.9200 |  |
| Jogador 8 | 4-3 | 09:22:53 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_Xayah | -0.0500 |  |
| Jogador 8 | 4-3 | 09:22:53 | COMPROU: Xayah (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Enfeitiçador | DA_18_Xayah | 0.4500 |  |
| Jogador 8 | 4-3 | 09:22:54 | VENDEU: Xayah (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 127 | 5 | Enfeitiçador | DA_18_Xayah | -0.7100 |  |
| Jogador 8 | 4-3 | 09:22:54 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 124 | 5 | Enfeitiçador | DA_18_Xayah | 0.4600 |  |
| Jogador 8 | 4-3 | 09:22:55 | VENDEU: Elise (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Enfeitiçador | DA_18_Xayah | -0.6200 |  |
| Jogador 8 | 4-3 | 09:22:55 | COMPROU: Camille (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_18_Xayah | 0.2400 |  |
| Jogador 8 | 4-3 | 09:22:56 | VENDEU: Camille (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 126 | 5 | Enfeitiçador | DA_18_Xayah | -0.0500 |  |
| Jogador 8 | 4-3 | 09:22:56 | COMPROU: Ornn (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 125 | 5 | Enfeitiçador | DA_18_Xayah | -0.2200 |  |
| Jogador 8 | 4-4 | 09:23:32 | VENDEU: Ornn (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 137 | 5 | Enfeitiçador | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 4-4 | 09:23:33 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 136 | 5 | Enfeitiçador | DA_18_Xayah | 1.0500 |  |
| Jogador 8 | 4-4 | 09:23:34 | COMPROU: Tristana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Enfeitiçador | DA_18_Xayah | 0.2400 |  |
| Jogador 8 | 4-4 | 09:23:34 | MOVE Bench -> Board: Tristana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 133 | 5 | Enfeitiçador | DA_18_Xayah | 0.3900 |  |
| Jogador 8 | 4-4 | 09:23:35 | COMPROU: Teemo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 131 | 5 | Enfeitiçador | DA_18_Xayah | 0.1700 |  |
| Jogador 8 | 4-4 | 09:23:35 | VENDEU: Rakan (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Enfeitiçador | DA_18_Xayah | -0.6900 |  |
| Jogador 8 | 4-4 | 09:23:36 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Lobo Trevoguari (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Enfeitiçador | DA_18_Xayah | 0.0600 |  |
| Jogador 8 | 4-4 | 09:23:36 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Lobo Trevoguari (i:4.0) (tabuleiro slot 19) | ALL_IN | HP crítico: gastar para sobreviver | 134 | 5 | Enfeitiçador | DA_18_Xayah | 0.0800 |  |
| Jogador 8 | 4-4 | 09:23:38 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 132 | 5 | Enfeitiçador | DA_18_Xayah | 0.0200 |  |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 38 | 38 | 190 | 38 | 17 | 264 | 13 | 56 |
| Jogador 2 | 38 | 38 | 190 | 38 | 18 | 305 | 6 | 32 |
| Jogador 3 | 35 | 37 | 185 | 35 | 17 | 269 | 6 | 20 |
| Jogador 4 | 23 | 24 | 120 | 23 | 14 | 162 | 4 | 21 |
| Jogador 5 | 24 | 27 | 135 | 24 | 15 | 186 | 12 | 20 |
| Jogador 6 | 28 | 30 | 150 | 28 | 18 | 206 | 13 | 33 |
| Jogador 7 | 30 | 30 | 150 | 30 | 17 | 227 | 8 | 34 |
| Jogador 8 | 23 | 23 | 115 | 23 | 14 | 184 | 4 | 34 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 264 | 264 | 264 | 0 | 248 | 0 | 264 | 264 | 264 | 65/48 |
| Jogador 2 | 305 | 305 | 305 | 0 | 291 | 0 | 305 | 305 | 305 | 117/101 |
| Jogador 3 | 269 | 269 | 269 | 0 | 261 | 0 | 269 | 269 | 269 | 106/92 |
| Jogador 4 | 162 | 162 | 162 | 0 | 154 | 0 | 162 | 162 | 162 | 49/35 |
| Jogador 5 | 186 | 186 | 186 | 0 | 179 | 0 | 186 | 186 | 186 | 84/70 |
| Jogador 6 | 206 | 206 | 206 | 0 | 194 | 0 | 206 | 206 | 206 | 71/56 |
| Jogador 7 | 227 | 227 | 227 | 0 | 218 | 0 | 227 | 227 | 227 | 78/63 |
| Jogador 8 | 184 | 184 | 184 | 0 | 176 | 0 | 184 | 184 | 184 | 80/66 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.20922301709651947 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.25060486793518066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23841141164302826 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22248587012290955 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013312771916389465 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.425262987613678 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.34730032086372375 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25139033794403076 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Ornn | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0387686491012573 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0314959287643433 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9796043038368225 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19132192432880402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17696425318717957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 58 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 59 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3994101583957672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33583778142929077 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 65 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12954987585544586 | 0.0 | 0.0 | +— / -699bd379-c986-4107-9c35-eeb8b49cf182 |
| Jogador 1 | 2-2 | 66 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 67 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060369908809661865 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 68 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27565330266952515 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00807955488562584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 70 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17273180186748505 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2729833126068115 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35905736684799194 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 1 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 75 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17829318344593048 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 1 | 2-3 | 76 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 79 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.116982340812683 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-4 | 83 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 84 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 1 | 2-4 | 85 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3635474443435669 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 86 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5461429953575134 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 87 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011836444027721882 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 88 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.031973123550415 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 93 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39517438411712646 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 94 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 0 | 0 | 14.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09984113276004791 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 96 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06441924721002579 | 0.0 | 0.0 | +— / -cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 2-5 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001613457134226337 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 98 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014717580750584602 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 99 | PASS | STABILIZE | 100.0 | 6 | 1 | 0 | 16.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 102 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179955005645752 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 18.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05520254001021385 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 104 | BUY | STABILIZE | 100.0 | 6 | 4 | 0 | 18.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2649584710597992 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 1 | 0 | 18.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3997105062007904 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013506794348359108 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 107 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014716637320816517 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 108 | PASS | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 112 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0375759601593018 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 1 | 2-7 | 113 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.019982933998108 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-7 | 114 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3487469255924225 | 0.0 | 0.0 | +acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce / -— |
| Jogador 1 | 2-7 | 115 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 5 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4788491129875183 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 116 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3451012670993805 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 117 | SELL | STABILIZE | 100.0 | 6 | 3 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5217328071594238 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 2-7 | 118 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1577768474817276 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 119 | EQUIP_FROM_INVENTORY | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14761483669281006 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 120 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 122 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28213992714881897 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2469814270734787 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 124 | BUY | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08033330738544464 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 125 | BUY_XP | STABILIZE | 100.0 | 6 | 4 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 126 | SELL | STABILIZE | 100.0 | 6 | 0 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 3-1 | 127 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06215396523475647 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -— |
| Jogador 1 | 3-1 | 128 | PASS | STABILIZE | 100.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 132 | BUY | STABILIZE | 100.0 | 6 | 10 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7220772504806519 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -— |
| Jogador 1 | 3-2 | 133 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19170470535755157 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 134 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 135 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2202577441930771 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 137 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 142 | BUY | STABILIZE | 100.0 | 6 | 11 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24934250116348267 | 0.0 | 0.0 | +66b5ed5e-7fdf-4135-a334-e693715e302d / -— |
| Jogador 1 | 3-3 | 143 | BUY_XP | STABILIZE | 100.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 144 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22281408309936523 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007934259250760078 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 147 | SELL | STABILIZE | 100.0 | 6 | 1 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02425481006503105 | 0.0 | 0.0 | +— / -8e819ba6-a356-4d9b-a8c9-7493332900fb |
| Jogador 1 | 3-3 | 148 | BUY | STABILIZE | 100.0 | 6 | 3 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1678260862827301 | 0.0 | 0.0 | +45450b46-63b4-488f-9469-3348c6da8f4b / -— |
| Jogador 1 | 3-3 | 149 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 152 | SELL | STABILIZE | 100.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10599999874830246 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 1 | 3-4 | 153 | BUY | STABILIZE | 100.0 | 6 | 12 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10147438198328018 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 1 | 3-4 | 154 | BUY_XP | STABILIZE | 100.0 | 6 | 11 | 1 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04040500149130821 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 155 | BUY_XP | STABILIZE | 100.0 | 7 | 7 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 156 | SELL | STABILIZE | 100.0 | 7 | 3 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02407880686223507 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 1 | 3-4 | 157 | BUY | STABILIZE | 100.0 | 7 | 4 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23955516517162323 | 0.0 | 0.0 | +0450963e-c7e2-4ff5-a2f5-09e65fa63527 / -— |
| Jogador 1 | 3-4 | 158 | SELL | STABILIZE | 100.0 | 7 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -0450963e-c7e2-4ff5-a2f5-09e65fa63527 |
| Jogador 1 | 3-4 | 159 | BUY_XP | STABILIZE | 100.0 | 7 | 4 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 0 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 162 | BUY | STABILIZE | 100.0 | 7 | 8 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.835131824016571 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 163 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 6 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0913928747177124 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 6 | 0 | 20.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13731682300567627 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 165 | BUY_XP | STABILIZE | 100.0 | 7 | 6 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 2 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2955770790576935 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014960871078073978 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 168 | BUY | STABILIZE | 100.0 | 7 | 2 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05659729242324829 | 0.0 | 0.0 | +c5557e24-8174-4d79-9e22-c2cbbb8225a8 / -— |
| Jogador 1 | 3-5 | 169 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 0 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 170 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 0 | 0 | 30.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33541518449783325 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 172 | BUY | STABILIZE | 100.0 | 7 | 9 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8031268119812012 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -— |
| Jogador 1 | 3-6 | 173 | BUY | STABILIZE | 100.0 | 7 | 6 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2812636196613312 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3469521105289459 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05430258810520172 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 177 | PASS | STABILIZE | 100.0 | 7 | 2 | 0 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 182 | SELL | STABILIZE | 100.0 | 7 | 11 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 1 | 3-7 | 183 | BUY | STABILIZE | 100.0 | 7 | 16 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8039796352386475 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 184 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 13 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07089721411466599 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 13 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19497615098953247 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 186 | PASS | STABILIZE | 100.0 | 7 | 13 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 7 | 22 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1551578789949417 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 7 | 22 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08901868015527725 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 194 | SELL | STABILIZE | 100.0 | 7 | 22 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -c5557e24-8174-4d79-9e22-c2cbbb8225a8 |
| Jogador 1 | 4-1 | 195 | BUY | STABILIZE | 100.0 | 7 | 24 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4537273943424225 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -— |
| Jogador 1 | 4-1 | 196 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 21 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005855212919414043 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 21 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13936729729175568 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 21 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01175983902066946 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 21 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10474908351898193 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 21 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011187762022018433 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 202 | SELL | STABILIZE | 100.0 | 7 | 32 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4100181758403778 | 0.0 | 0.0 | +— / -66b5ed5e-7fdf-4135-a334-e693715e302d |
| Jogador 1 | 4-2 | 203 | BUY | STABILIZE | 100.0 | 7 | 34 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8263090252876282 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 1 | 4-2 | 204 | SELL | STABILIZE | 100.0 | 7 | 31 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4339999854564667 | 0.0 | 0.0 | +— / -a4188ec8-4188-4fdf-8d76-c559fc0c7daf |
| Jogador 1 | 4-2 | 205 | BUY | STABILIZE | 100.0 | 7 | 34 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3326004445552826 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -— |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 33 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03284844383597374 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 33 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017813952639698982 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 33 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01497726235538721 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 209 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 33 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000863000750542 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 210 | PASS | STABILIZE | 100.0 | 7 | 33 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037857141345739365 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 212 | SELL | STABILIZE | 100.0 | 7 | 45 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002166666556149721 | 0.0 | 0.0 | +— / -45450b46-63b4-488f-9469-3348c6da8f4b |
| Jogador 1 | 4-3 | 213 | BUY | STABILIZE | 100.0 | 7 | 48 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9269487857818604 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -1e504283-c5d1-4eb3-915e-20533ec3a756,acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce |
| Jogador 1 | 4-3 | 214 | BUY | STABILIZE | 100.0 | 7 | 47 | 4 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03785262629389763 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 1 | 4-3 | 215 | SELL | STABILIZE | 100.0 | 7 | 43 | 4 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5839999914169312 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 1 | 4-3 | 216 | BUY | STABILIZE | 100.0 | 7 | 46 | 4 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2621934413909912 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 1 | 4-3 | 217 | SELL | STABILIZE | 100.0 | 7 | 43 | 4 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026000000536441803 | 0.0 | 0.0 | +— / -caf1c554-2223-4090-9f96-b551e5c579ce |
| Jogador 1 | 4-3 | 218 | BUY_XP | STABILIZE | 100.0 | 7 | 46 | 4 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022065000608563423 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 219 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 42 | 4 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09467051923274994 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 220 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 42 | 4 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5512835383415222 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 222 | BUY | FAST8 | 100.0 | 7 | 55 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024516187608242035 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 1 | 4-4 | 223 | BUY | FAST8 | 100.0 | 7 | 52 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2146727591753006 | 0.0 | 0.0 | +7dfeef88-7e1d-43b8-b012-017278ec61dc / -— |
| Jogador 1 | 4-4 | 224 | MOVE_BOARD | FAST8 | 100.0 | 7 | 49 | 4 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04174874722957611 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 225 | MOVE_BOARD | FAST8 | 100.0 | 7 | 49 | 4 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011533873155713081 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 226 | MOVE_BOARD | FAST8 | 100.0 | 7 | 49 | 4 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.054048944264650345 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 227 | PASS | FAST8 | 100.0 | 7 | 49 | 4 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04928571358323097 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 232 | SELL | FAST8 | 100.0 | 7 | 61 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -7dfeef88-7e1d-43b8-b012-017278ec61dc |
| Jogador 1 | 4-5 | 233 | BUY | FAST8 | 100.0 | 7 | 64 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07547135651111603 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 1 | 4-5 | 234 | SELL | FAST8 | 100.0 | 7 | 61 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -696f53ae-1413-47cc-b491-9870b7bcba51 |
| Jogador 1 | 4-5 | 235 | BUY | FAST8 | 100.0 | 7 | 64 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09313017874956131 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 1 | 4-5 | 236 | MOVE_BOARD | FAST8 | 100.0 | 7 | 60 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0379071868956089 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 237 | MOVE_BOARD | FAST8 | 100.0 | 7 | 60 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04399996995925903 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 238 | MOVE_BOARD | FAST8 | 100.0 | 7 | 60 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 239 | MOVE_BOARD | FAST8 | 100.0 | 7 | 60 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 240 | PASS | FAST8 | 100.0 | 7 | 60 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08595746010541916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 242 | SELL | FAST8 | 88.0 | 7 | 70 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04673333466053009 | 0.0 | 0.0 | +— / -45da6d00-829e-4e2e-a1a5-318498fd007b |
| Jogador 1 | 4-6 | 243 | BUY | FAST8 | 88.0 | 7 | 73 | 5 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8916836380958557 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -760d5bee-7d64-4f03-abf0-6357c914a1ed,b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 1 | 4-6 | 244 | BUY | STABILIZE | 88.0 | 7 | 71 | 5 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9610971212387085 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -9fe58106-e0c4-4ecc-b152-13c8c0eb564e,c617e958-b482-40ce-ab24-acff4dc48bc0 |
| Jogador 1 | 4-6 | 245 | BUY | STABILIZE | 88.0 | 7 | 68 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09348893910646439 | 0.0 | 0.0 | +99182042-c4b9-4801-b66a-1f4432d301f3 / -— |
| Jogador 1 | 4-6 | 246 | BUY_XP | STABILIZE | 88.0 | 7 | 67 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019780000671744347 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 247 | BUY_XP | STABILIZE | 88.0 | 7 | 63 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019780000671744347 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 248 | BUY_XP | STABILIZE | 88.0 | 7 | 59 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019780000671744347 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 249 | BUY_XP | STABILIZE | 88.0 | 7 | 55 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019780000671744347 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 250 | BUY_XP | STABILIZE | 88.0 | 7 | 51 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04295625165104866 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 252 | BUY | ECON | 88.0 | 8 | 57 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4972134530544281 | 0.0 | 0.0 | +e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b / -— |
| Jogador 1 | 4-7 | 253 | BUY_XP | ECON | 88.0 | 8 | 53 | 5 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05310000106692314 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 254 | BUY_XP | ECON | 88.0 | 8 | 49 | 4 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 255 | BUY_XP | ECON | 88.0 | 8 | 45 | 4 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 256 | BUY_XP | ECON | 88.0 | 8 | 41 | 4 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 257 | BUY_XP | ECON | 88.0 | 8 | 37 | 3 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 258 | BUY_XP | ECON | 88.0 | 8 | 33 | 3 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 259 | BUY_XP | ECON | 88.0 | 8 | 29 | 2 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 260 | BUY_XP | ECON | 88.0 | 8 | 25 | 2 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | ECON | 88.0 | 8 | 28 | 2 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10163441300392151 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | ECON | 88.0 | 8 | 28 | 2 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16232222318649292 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 264 | SELL | ECON | 88.0 | 8 | 28 | 2 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -772bccc4-15f4-4de2-95f8-82d0ed9a72d2 |
| Jogador 1 | 5-1 | 265 | BUY | ECON | 88.0 | 8 | 33 | 3 | 32.0 | Adaptador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7227782011032104 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 1 | 5-1 | 266 | SELL | ECON | 88.0 | 8 | 29 | 2 | 32.0 | Adaptador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -4a885bc0-41b4-43f1-94d3-8e755a10645c |
| Jogador 1 | 5-1 | 267 | BUY | ECON | 88.0 | 8 | 37 | 3 | 32.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8539895415306091 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -227dbcdb-af5c-4318-94d1-f01a7847d100,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 5-1 | 268 | BUY | ECON | 88.0 | 8 | 34 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7505999803543091 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 1 | 5-1 | 269 | MOVE_BENCH | ECON | 88.0 | 8 | 31 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3448847830295563 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 270 | BUY_XP | ECON | 88.0 | 8 | 31 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08179999887943268 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 272 | BUY | ECON | 73.0 | 8 | 34 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04754123091697693 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 1 | 5-2 | 273 | MOVE_BENCH | ECON | 73.0 | 8 | 31 | 3 | 28.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15176013112068176 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 274 | BUY | ECON | 73.0 | 8 | 31 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012250808998942375 | 0.0 | 0.0 | +af98a89b-ee97-45ce-972a-3f41e280b6b2 / -— |
| Jogador 1 | 5-2 | 275 | MOVE_BOARD | ECON | 73.0 | 8 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 276 | MOVE_BOARD | ECON | 73.0 | 8 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014804462902247906 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 277 | PASS | ECON | 73.0 | 8 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03692857176065445 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 280 | MOVE_BENCH | ECON | 73.0 | 8 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4024941325187683 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 282 | BUY | ECON | 73.0 | 8 | 35 | 3 | 42.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8055588006973267 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 1 | 5-3 | 283 | SELL | ECON | 73.0 | 8 | 34 | 3 | 42.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49399998784065247 | 0.0 | 0.0 | +— / -02d3d068-e592-4f9c-a574-914955401575 |
| Jogador 1 | 5-3 | 284 | BUY | ECON | 73.0 | 8 | 42 | 4 | 42.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.8189454078674316 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -7c218f01-e884-46da-8a1a-2d2db27a5ff1,d8c38b21-fc25-4c11-87b5-b5747d71bbc7 |
| Jogador 1 | 5-3 | 285 | MOVE_BENCH | ECON | 73.0 | 8 | 39 | 3 | 30.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.15321141481399536 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 286 | EQUIP_FROM_INVENTORY | ECON | 73.0 | 8 | 39 | 3 | 38.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0740952268242836 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 287 | EQUIP_FROM_INVENTORY | ECON | 73.0 | 8 | 39 | 3 | 38.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16068315505981445 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 288 | EQUIP_FROM_INVENTORY | ECON | 73.0 | 8 | 39 | 3 | 38.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1182350143790245 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 289 | BUY | ECON | 73.0 | 8 | 39 | 3 | 38.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050069667398929596 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 1 | 5-3 | 290 | BUY_XP | ECON | 73.0 | 8 | 35 | 3 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017999999690800905 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 292 | SELL | ECON | 73.0 | 8 | 41 | 4 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 1 | 5-4 | 293 | BUY | ECON | 73.0 | 8 | 49 | 4 | 38.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7832635641098022 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 1 | 5-4 | 294 | EQUIP_FROM_INVENTORY | ECON | 73.0 | 8 | 47 | 4 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08436349034309387 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 295 | EQUIP_FROM_INVENTORY | ECON | 73.0 | 8 | 47 | 4 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08535827696323395 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 296 | MOVE_BOARD | ECON | 73.0 | 8 | 47 | 4 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008758041076362133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 297 | BUY_XP | ECON | 73.0 | 8 | 47 | 4 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017999999690800905 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 298 | BUY_XP | ECON | 73.0 | 8 | 43 | 4 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08179999887943268 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 299 | BUY_XP | ECON | 73.0 | 8 | 39 | 3 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017999999690800905 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 300 | MOVE_BENCH | ECON | 73.0 | 8 | 35 | 3 | 38.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5996316075325012 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 302 | BUY | ECON | 73.0 | 8 | 44 | 4 | 40.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24446147680282593 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 1 | 5-5 | 303 | MOVE_BOARD | ECON | 73.0 | 8 | 39 | 3 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.19355302862823e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 304 | MOVE_BOARD | ECON | 73.0 | 8 | 39 | 3 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 305 | MOVE_BOARD | ECON | 73.0 | 8 | 39 | 3 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014968364499509335 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 306 | PASS | ECON | 73.0 | 8 | 39 | 3 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04635714367032051 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 312 | MOVE_BOARD | WINSTREAK | 73.0 | 8 | 50 | 5 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.9111868570907973e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 313 | MOVE_BOARD | WINSTREAK | 73.0 | 8 | 50 | 5 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 314 | PASS | WINSTREAK | 73.0 | 8 | 50 | 5 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 322 | MOVE_BOARD | WINSTREAK | 73.0 | 9 | 61 | 5 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.504913391021546e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 323 | MOVE_BOARD | WINSTREAK | 73.0 | 9 | 61 | 5 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015027572400867939 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 324 | MOVE_BOARD | WINSTREAK | 73.0 | 9 | 61 | 5 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 325 | PASS | WINSTREAK | 73.0 | 9 | 61 | 5 | 40.0 | Adaptador/DA_18_Malphite | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045777563005685806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 332 | BUY | WINSTREAK | 73.0 | 9 | 72 | 5 | 50.0 | Adaptador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0651721954345703 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -4518ad1d-87e7-4110-830a-96183c533201,ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 1 | 6-1 | 333 | BUY | WINSTREAK | 73.0 | 9 | 68 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5093883872032166 | 0.0 | 0.0 | +caeaaabc-213a-4018-97f3-8797a0711863 / -— |
| Jogador 1 | 6-1 | 334 | EQUIP_FROM_INVENTORY | WINSTREAK | 73.0 | 9 | 66 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09292621165513992 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 335 | BUY | WINSTREAK | 73.0 | 9 | 66 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25500279664993286 | 0.0 | 0.0 | +3ae84928-bc2a-4c1e-8663-b7ad05da4501 / -— |
| Jogador 1 | 6-1 | 336 | MOVE_BOARD | WINSTREAK | 73.0 | 9 | 62 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.4991957111051306e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 337 | MOVE_BOARD | WINSTREAK | 73.0 | 9 | 62 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015003150328993797 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 338 | MOVE_BOARD | WINSTREAK | 73.0 | 9 | 62 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 339 | PASS | WINSTREAK | 73.0 | 9 | 62 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05073658749461174 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 342 | SELL | WINSTREAK | 73.0 | 9 | 74 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02801082469522953 | 0.0 | 0.0 | +— / -99182042-c4b9-4801-b66a-1f4432d301f3 |
| Jogador 1 | 6-2 | 343 | BUY | WINSTREAK | 73.0 | 9 | 75 | 5 | 50.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0612921714782715 | 0.0 | 0.0 | +d58ebcea-d18b-42f8-a6ca-984d15656662 / -b2566e66-ba8b-4ec9-9875-e08ce45cd7a1,b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 1 | 6-2 | 344 | EQUIP_FROM_INVENTORY | WINSTREAK | 73.0 | 9 | 74 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04830204322934151 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 345 | BUY_XP | WINSTREAK | 73.0 | 9 | 74 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02879999950528145 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 346 | BUY_XP | WINSTREAK | 73.0 | 9 | 70 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028200000524520874 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 347 | BUY_XP | WINSTREAK | 73.0 | 9 | 66 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02759999968111515 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 348 | BUY_XP | WINSTREAK | 73.0 | 9 | 62 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 349 | BUY_XP | WINSTREAK | 73.0 | 9 | 58 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005200000014156103 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 350 | BUY_XP | WINSTREAK | 73.0 | 9 | 54 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005200000014156103 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 352 | BUY_XP | WINSTREAK | 73.0 | 9 | 63 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027149999514222145 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 353 | BUY_XP | WINSTREAK | 73.0 | 9 | 59 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005200000014156103 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 354 | BUY_XP | WINSTREAK | 73.0 | 9 | 55 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005200000014156103 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 355 | BUY_XP | WINSTREAK | 73.0 | 9 | 51 | 5 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08470000326633453 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 356 | BUY_XP | WINSTREAK | 73.0 | 9 | 47 | 4 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 357 | BUY_XP | WINSTREAK | 73.0 | 9 | 43 | 4 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 358 | BUY_XP | WINSTREAK | 73.0 | 9 | 39 | 3 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 359 | BUY_XP | WINSTREAK | 73.0 | 9 | 35 | 3 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 360 | BUY_XP | WINSTREAK | 73.0 | 9 | 31 | 3 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 362 | PASS | WINSTREAK | 73.0 | 10 | 38 | 3 | 46.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18771427869796753 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 372 | BUY | WINSTREAK | 73.0 | 10 | 49 | 4 | 62.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7577409744262695 | 0.0 | 0.0 | +00497e43-57ef-4c25-a34b-0be0155bb92d / -— |
| Jogador 1 | 6-5 | 373 | MOVE_BOARD | WINSTREAK | 73.0 | 10 | 45 | 4 | 62.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 5.032421995565528e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 374 | MOVE_BOARD | WINSTREAK | 73.0 | 10 | 45 | 4 | 62.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 375 | MOVE_BOARD | WINSTREAK | 73.0 | 10 | 45 | 4 | 62.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 376 | PASS | WINSTREAK | 73.0 | 10 | 45 | 4 | 62.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 380 | MOVE_BENCH | WINSTREAK | 73.0 | 10 | 45 | 4 | 62.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2705710232257843 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-6 | 382 | BUY | WINSTREAK | 73.0 | 10 | 58 | 5 | 70.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.456819087266922 | 0.0 | 0.0 | +4321582a-0b45-4666-a119-7b49e92d012a / -— |
| Jogador 1 | 6-6 | 383 | MOVE_BOARD | WINSTREAK | 73.0 | 10 | 55 | 5 | 70.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-6 | 384 | MOVE_BOARD | WINSTREAK | 73.0 | 10 | 55 | 5 | 70.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-6 | 385 | PASS | WINSTREAK | 73.0 | 10 | 55 | 5 | 70.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045335106551647186 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29996994137763977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.16027452051639557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11422412097454071 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43195363879203796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 20 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5011208057403564 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1178061962127686 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1183956116437912 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3084782063961029 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40794336795806885 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0721389055252075 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 44 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2019224762916565 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.400314062833786 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024478765204548836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012103810906410217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 48 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0379807949066162 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1818237006664276 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2733021080493927 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2662481367588043 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 59 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1482027918100357 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047436825931072235 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 61 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19654007256031036 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 2 | 2-1 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028999745845794678 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 64 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.047969937324524 | 0.0 | 0.0 | +56b3bab3-f85f-4065-a392-f191e3b9a8a9 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 65 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2335163950920105 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 66 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15169912576675415 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2306191772222519 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 68 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8824999928474426 | 0.0 | 0.0 | +— / -56b3bab3-f85f-4065-a392-f191e3b9a8a9 |
| Jogador 2 | 2-2 | 69 | BUY_XP | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 70 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19457465410232544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 72 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29834944009780884 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 2 | 2-3 | 73 | BUY_XP | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 74 | PASS | STABILIZE | 90.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 82 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9691802263259888 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 2 | 2-4 | 83 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3295946419239044 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 84 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002934961346909404 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 85 | SELL | STABILIZE | 85.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 |
| Jogador 2 | 2-4 | 86 | BUY | STABILIZE | 85.0 | 5 | 4 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12603126466274261 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 2 | 2-4 | 87 | SELL | STABILIZE | 85.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1527567356824875 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 2 | 2-4 | 88 | BUY | STABILIZE | 85.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19187654554843903 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 2 | 2-4 | 89 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3988630771636963 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014861222356557846 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 92 | BUY | STABILIZE | 85.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3108147084712982 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 2 | 2-5 | 93 | BUY_XP | STABILIZE | 85.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 94 | SELL | STABILIZE | 85.0 | 5 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10753991454839706 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-5 | 95 | BUY | STABILIZE | 85.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05872822180390358 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 2 | 2-5 | 96 | SELL | STABILIZE | 85.0 | 5 | 1 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04100000113248825 | 0.0 | 0.0 | +— / -eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 2 | 2-5 | 97 | BUY | STABILIZE | 85.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05881332606077194 | 0.0 | 0.0 | +be53a299-cc3e-4af3-94f6-343f9de1e0a0 / -— |
| Jogador 2 | 2-5 | 98 | SELL | STABILIZE | 85.0 | 5 | 1 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04100000113248825 | 0.0 | 0.0 | +— / -be53a299-cc3e-4af3-94f6-343f9de1e0a0 |
| Jogador 2 | 2-5 | 99 | SELL | STABILIZE | 85.0 | 5 | 2 | 0 | 16.0 | Feérico/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10230299830436707 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-5 | 100 | BUY_XP | STABILIZE | 85.0 | 5 | 5 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 102 | BUY | STABILIZE | 79.0 | 5 | 7 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21974952518939972 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 103 | BUY_XP | STABILIZE | 79.0 | 5 | 4 | 0 | 16.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 79.0 | 6 | 0 | 0 | 16.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5937293767929077 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 105 | MOVE_BOARD | STABILIZE | 79.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014704774133861065 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 106 | MOVE_BOARD | STABILIZE | 79.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014742878265678883 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 107 | PASS | STABILIZE | 79.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 112 | BUY | STABILIZE | 72.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3648684024810791 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 113 | BUY | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11204952746629715 | 0.0 | 0.0 | +068d0768-4134-4a5f-a132-0642c23d91e1 / -— |
| Jogador 2 | 2-7 | 114 | SELL | STABILIZE | 72.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10188454389572144 | 0.0 | 0.0 | +— / -068d0768-4134-4a5f-a132-0642c23d91e1 |
| Jogador 2 | 2-7 | 115 | BUY | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08674605190753937 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 2-7 | 116 | SELL | STABILIZE | 72.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 2-7 | 117 | BUY | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06068631261587143 | 0.0 | 0.0 | +c96b6357-8134-4e68-af0b-f5695a815597 / -— |
| Jogador 2 | 2-7 | 118 | SELL | STABILIZE | 72.0 | 6 | 1 | 0 | 18.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04233333468437195 | 0.0 | 0.0 | +— / -c96b6357-8134-4e68-af0b-f5695a815597 |
| Jogador 2 | 2-7 | 119 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6196767687797546 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 122 | BUY | STABILIZE | 72.0 | 6 | 10 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1465374380350113 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 123 | BUY | STABILIZE | 72.0 | 6 | 7 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1504957675933838 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 2 | 3-1 | 124 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.26041343808174133 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 125 | BUY_XP | STABILIZE | 72.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 126 | SELL | STABILIZE | 72.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0944141075015068 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 2 | 3-1 | 127 | BUY | STABILIZE | 72.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07640314847230911 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 128 | SELL | STABILIZE | 72.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03433333337306976 | 0.0 | 0.0 | +— / -ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 2 | 3-1 | 129 | SELL | STABILIZE | 72.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -97fc5647-5995-4f21-aa03-13454546919a |
| Jogador 2 | 3-1 | 130 | BUY_XP | STABILIZE | 72.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 132 | BUY | STABILIZE | 62.0 | 6 | 10 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7574544548988342 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -7ca9b803-76eb-4283-9648-7f98bfd81149,d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 2 | 3-2 | 133 | BUY | STABILIZE | 62.0 | 6 | 9 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7580538988113403 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 134 | BUY_XP | STABILIZE | 62.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 135 | BUY_XP | STABILIZE | 62.0 | 6 | 4 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 136 | SELL | STABILIZE | 62.0 | 6 | 0 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 2 | 3-2 | 137 | BUY | STABILIZE | 62.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2130378633737564 | 0.0 | 0.0 | +e86a4466-cd1f-48a3-a825-cab2e361b72a / -— |
| Jogador 2 | 3-2 | 138 | SELL | STABILIZE | 62.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3596666753292084 | 0.0 | 0.0 | +— / -e86a4466-cd1f-48a3-a825-cab2e361b72a |
| Jogador 2 | 3-2 | 139 | BUY | STABILIZE | 62.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2864295542240143 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 2 | 3-2 | 140 | SELL | STABILIZE | 62.0 | 6 | 1 | 0 | 24.0 | Feérico/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020999999716877937 | 0.0 | 0.0 | +— / -f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 2 | 3-3 | 142 | BUY | STABILIZE | 62.0 | 6 | 9 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8038970828056335 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 143 | BUY | STABILIZE | 62.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2521574795246124 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 144 | SELL | STABILIZE | 62.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038333334028720856 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-3 | 145 | BUY | STABILIZE | 62.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05957783758640289 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 146 | SELL | STABILIZE | 62.0 | 6 | 3 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050333332270383835 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 2 | 3-3 | 147 | BUY_XP | STABILIZE | 62.0 | 6 | 6 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 148 | SELL | STABILIZE | 62.0 | 6 | 2 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6171776652336121 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-3 | 149 | SELL | STABILIZE | 62.0 | 6 | 5 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 3-3 | 150 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 8 | 0 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00088141905143857 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 152 | BUY | STABILIZE | 62.0 | 6 | 15 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02428523637354374 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 153 | BUY | STABILIZE | 62.0 | 6 | 13 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024493619799613953 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 154 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008797089685685933 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 155 | SELL | STABILIZE | 62.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36899998784065247 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-4 | 156 | BUY | STABILIZE | 62.0 | 6 | 13 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43442487716674805 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 157 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.295202191111457e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 158 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997422695159912 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 159 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997935853898525 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 160 | PASS | STABILIZE | 62.0 | 6 | 11 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 162 | BUY | STABILIZE | 62.0 | 6 | 18 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17424312233924866 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 163 | BUY | STABILIZE | 62.0 | 6 | 15 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06599706411361694 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 164 | BUY | STABILIZE | 62.0 | 6 | 13 | 1 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2622847557067871 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 2 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 12 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0026225934270769358 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 12 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012376728467643261 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 167 | PASS | STABILIZE | 62.0 | 6 | 12 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 172 | SELL | STABILIZE | 62.0 | 6 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014633333310484886 | 0.0 | 0.0 | +— / -c5a8f36d-74b1-4944-a3db-bfb601a89b59 |
| Jogador 2 | 3-6 | 173 | BUY | STABILIZE | 62.0 | 6 | 21 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3013589084148407 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 2 | 3-6 | 174 | SELL | STABILIZE | 62.0 | 6 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023996740579605103 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-6 | 175 | BUY | STABILIZE | 62.0 | 6 | 22 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04067199304699898 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -— |
| Jogador 2 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 19 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.5448289306950755e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 177 | SELL | STABILIZE | 62.0 | 6 | 19 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5080000162124634 | 0.0 | 0.0 | +— / -f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 2 | 3-6 | 178 | BUY | STABILIZE | 62.0 | 6 | 20 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10651624202728271 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 17 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.9802519091172144e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 180 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 17 | 1 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015000207349658012 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 182 | SELL | STABILIZE | 62.0 | 7 | 25 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010833333246409893 | 0.0 | 0.0 | +— / -33a860e2-992f-4355-ab24-85b4a2576f90 |
| Jogador 2 | 3-7 | 183 | BUY | STABILIZE | 62.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.812249481678009 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 184 | SELL | STABILIZE | 62.0 | 7 | 24 | 2 | 24.0 | Feérico/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002973910653963685 | 0.0 | 0.0 | +— / -23157bd6-5e8f-4416-bb7f-2e5d71a06543 |
| Jogador 2 | 3-7 | 185 | BUY | STABILIZE | 62.0 | 7 | 27 | 2 | 24.0 | Feérico/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8489577174186707 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -0c15e414-bc67-46de-a087-fb7708db0dfe,e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-7 | 186 | BUY | STABILIZE | 62.0 | 7 | 24 | 2 | 24.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2722925841808319 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 187 | SELL | STABILIZE | 62.0 | 7 | 21 | 2 | 24.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6190000176429749 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 188 | SELL | STABILIZE | 62.0 | 7 | 29 | 2 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4283333420753479 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-7 | 189 | BUY | STABILIZE | 62.0 | 7 | 31 | 3 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1400696188211441 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 2 | 3-7 | 190 | BUY_XP | STABILIZE | 62.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 192 | BUY | STABILIZE | 62.0 | 7 | 32 | 3 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2881837785243988 | 0.0 | 0.0 | +15d93457-0760-419e-87db-74223c1cb7f4 / -— |
| Jogador 2 | 4-1 | 193 | BUY | STABILIZE | 62.0 | 7 | 29 | 2 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06760670244693756 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 2 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 62.0 | 7 | 26 | 2 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1763247847557068 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 195 | CRAFT_AND_EQUIP | STABILIZE | 62.0 | 7 | 26 | 2 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22111867368221283 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 196 | SELL | STABILIZE | 62.0 | 7 | 26 | 2 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 4-1 | 197 | BUY | STABILIZE | 62.0 | 7 | 28 | 2 | 24.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2842969298362732 | 0.0 | 0.0 | +48be5cb2-e7b3-41f8-b212-79e21249fa6a / -— |
| Jogador 2 | 4-1 | 198 | BUY_XP | STABILIZE | 62.0 | 7 | 24 | 2 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007728000171482563 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 199 | BUY_XP | STABILIZE | 62.0 | 7 | 20 | 2 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08772800117731094 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 200 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 16 | 1 | 24.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4043061435222626 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 202 | BUY | STABILIZE | 62.0 | 7 | 25 | 2 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.586688756942749 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -15d93457-0760-419e-87db-74223c1cb7f4,ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 2 | 4-2 | 203 | BUY | STABILIZE | 62.0 | 7 | 22 | 2 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02758553996682167 | 0.0 | 0.0 | +974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 / -— |
| Jogador 2 | 4-2 | 204 | BUY | STABILIZE | 62.0 | 7 | 21 | 2 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027810316532850266 | 0.0 | 0.0 | +bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b / -— |
| Jogador 2 | 4-2 | 205 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 20 | 2 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.349955815996509e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 20 | 2 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01586223766207695 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 207 | PASS | STABILIZE | 62.0 | 7 | 20 | 2 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02857142873108387 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 212 | SELL | STABILIZE | 62.0 | 7 | 31 | 3 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040699999779462814 | 0.0 | 0.0 | +— / -0534477f-2ff8-47a7-b71b-1a1d5430589e |
| Jogador 2 | 4-3 | 213 | BUY | STABILIZE | 62.0 | 7 | 39 | 3 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3326553702354431 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 2 | 4-3 | 214 | SELL | STABILIZE | 62.0 | 7 | 36 | 3 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -974a1c04-fd6f-4b0c-9c56-6507bb8bbfa0 |
| Jogador 2 | 4-3 | 215 | BUY | STABILIZE | 62.0 | 7 | 37 | 3 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0026170772034674883 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -— |
| Jogador 2 | 4-3 | 216 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 34 | 3 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0018536491552367806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 217 | SELL | STABILIZE | 62.0 | 7 | 34 | 3 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0070333331823349 | 0.0 | 0.0 | +— / -bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b |
| Jogador 2 | 4-3 | 218 | BUY | STABILIZE | 62.0 | 7 | 35 | 3 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07561716437339783 | 0.0 | 0.0 | +506f421d-7a3c-46d7-9cac-6c107bc35e31 / -— |
| Jogador 2 | 4-3 | 219 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 34 | 3 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 220 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 34 | 3 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012688955292105675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 222 | SELL | STABILIZE | 49.0 | 7 | 42 | 4 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028699999675154686 | 0.0 | 0.0 | +— / -506f421d-7a3c-46d7-9cac-6c107bc35e31 |
| Jogador 2 | 4-4 | 223 | BUY | STABILIZE | 49.0 | 7 | 43 | 4 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.357108473777771 | 0.0 | 0.0 | +bb2e33e3-fe6f-4344-b113-aeba7ace7a2d / -— |
| Jogador 2 | 4-4 | 224 | SELL | STABILIZE | 49.0 | 7 | 40 | 4 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010833333246409893 | 0.0 | 0.0 | +— / -3f488391-7117-4e28-b6cc-7416722351d4 |
| Jogador 2 | 4-4 | 225 | BUY | STABILIZE | 49.0 | 7 | 43 | 4 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.062456704676151276 | 0.0 | 0.0 | +d974e68a-e978-4335-8827-a94a9219be58 / -— |
| Jogador 2 | 4-4 | 226 | SELL | STABILIZE | 49.0 | 7 | 40 | 4 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00563333323225379 | 0.0 | 0.0 | +— / -d974e68a-e978-4335-8827-a94a9219be58 |
| Jogador 2 | 4-4 | 227 | BUY | STABILIZE | 49.0 | 7 | 43 | 4 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25857022404670715 | 0.0 | 0.0 | +30d2995a-d9b8-4424-af46-8766734e440c / -— |
| Jogador 2 | 4-4 | 228 | SELL | STABILIZE | 49.0 | 7 | 40 | 4 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014299999922513962 | 0.0 | 0.0 | +— / -30d2995a-d9b8-4424-af46-8766734e440c |
| Jogador 2 | 4-4 | 229 | BUY | STABILIZE | 49.0 | 7 | 43 | 4 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21613174676895142 | 0.0 | 0.0 | +f4173576-aa2e-4a93-94ec-ecd49d90d2b7 / -— |
| Jogador 2 | 4-4 | 230 | MOVE_BOARD | STABILIZE | 49.0 | 7 | 42 | 4 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.2728272597305477e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 232 | SELL | STABILIZE | 49.0 | 7 | 51 | 5 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -f4173576-aa2e-4a93-94ec-ecd49d90d2b7 |
| Jogador 2 | 4-5 | 233 | BUY | STABILIZE | 49.0 | 7 | 52 | 5 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8287742733955383 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 2 | 4-5 | 234 | SELL | STABILIZE | 49.0 | 7 | 49 | 4 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09723333269357681 | 0.0 | 0.0 | +— / -48be5cb2-e7b3-41f8-b212-79e21249fa6a |
| Jogador 2 | 4-5 | 235 | BUY | STABILIZE | 49.0 | 7 | 53 | 5 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8652746081352234 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -— |
| Jogador 2 | 4-5 | 236 | SELL | STABILIZE | 49.0 | 7 | 50 | 5 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4293736517429352 | 0.0 | 0.0 | +— / -bb2e33e3-fe6f-4344-b113-aeba7ace7a2d |
| Jogador 2 | 4-5 | 237 | BUY | STABILIZE | 49.0 | 7 | 53 | 5 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005981876980513334 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -— |
| Jogador 2 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 49.0 | 7 | 51 | 5 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.6026810334988113e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 49.0 | 7 | 51 | 5 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01498227659612894 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 240 | PASS | STABILIZE | 49.0 | 7 | 51 | 5 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08048655092716217 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 242 | SELL | STABILIZE | 49.0 | 7 | 62 | 5 | 26.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017877060920000076 | 0.0 | 0.0 | +— / -fcc4f620-7b85-40ed-a42c-2eadd37a82fd |
| Jogador 2 | 4-6 | 243 | BUY | STABILIZE | 49.0 | 7 | 64 | 5 | 26.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9612933993339539 | 0.0 | 0.0 | +51a5a5d7-c5ea-43e2-a521-22fe0275c231 / -5a1572b3-8b27-4d87-b885-f342b91c0854,6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 4-6 | 244 | SELL | STABILIZE | 49.0 | 7 | 63 | 5 | 22.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5939000248908997 | 0.0 | 0.0 | +— / -51a5a5d7-c5ea-43e2-a521-22fe0275c231 |
| Jogador 2 | 4-6 | 245 | BUY | STABILIZE | 49.0 | 7 | 66 | 5 | 22.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3981398940086365 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 2 | 4-6 | 246 | MOVE_BENCH | STABILIZE | 49.0 | 7 | 65 | 5 | 22.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.2533503770828247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 247 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 7 | 65 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1116943508386612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 248 | EQUIP_FROM_INVENTORY | STABILIZE | 49.0 | 7 | 65 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08012865483760834 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 249 | BUY | STABILIZE | 49.0 | 7 | 65 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041491053998470306 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 2 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 49.0 | 7 | 63 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002677531447261572 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 252 | SELL | STABILIZE | 39.0 | 7 | 73 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |
| Jogador 2 | 4-7 | 253 | BUY | STABILIZE | 39.0 | 7 | 75 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11534559726715088 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -— |
| Jogador 2 | 4-7 | 254 | SELL | STABILIZE | 39.0 | 7 | 74 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030089378356933594 | 0.0 | 0.0 | +— / -6722b147-c2a7-4fd0-a943-5036adb3e3a1 |
| Jogador 2 | 4-7 | 255 | BUY | STABILIZE | 39.0 | 7 | 75 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019692791625857353 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 2 | 4-7 | 256 | SELL | STABILIZE | 39.0 | 7 | 73 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011934405192732811 | 0.0 | 0.0 | +— / -3b934078-806c-40f0-b102-e9131220f70e |
| Jogador 2 | 4-7 | 257 | BUY | STABILIZE | 39.0 | 7 | 75 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006146498955786228 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 2 | 4-7 | 258 | SELL | STABILIZE | 39.0 | 7 | 74 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -755060be-13bb-4686-9ee9-e53fef2d75b2 |
| Jogador 2 | 4-7 | 259 | BUY | STABILIZE | 39.0 | 7 | 75 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26984846591949463 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 2 | 4-7 | 260 | BUY_XP | STABILIZE | 39.0 | 7 | 73 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038895998150110245 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 39.0 | 7 | 79 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13472160696983337 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 39.0 | 7 | 79 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1337260603904724 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 264 | SELL | STABILIZE | 39.0 | 7 | 79 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 2 | 5-1 | 265 | BUY | STABILIZE | 39.0 | 7 | 81 | 5 | 28.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3937045931816101 | 0.0 | 0.0 | +91966802-adc2-46d2-9e7e-194283bca85c / -— |
| Jogador 2 | 5-1 | 266 | MOVE_BENCH | STABILIZE | 39.0 | 7 | 78 | 5 | 28.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09964252263307571 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 267 | BUY | STABILIZE | 39.0 | 7 | 78 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14570292830467224 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 2 | 5-1 | 268 | SELL | STABILIZE | 39.0 | 7 | 73 | 5 | 34.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 2 | 5-1 | 269 | BUY | STABILIZE | 39.0 | 7 | 76 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1314321756362915 | 0.0 | 0.0 | +a64cf09b-42bf-494e-9603-d387b6740200 / -— |
| Jogador 2 | 5-1 | 270 | SELL | STABILIZE | 39.0 | 7 | 73 | 5 | 34.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -a64cf09b-42bf-494e-9603-d387b6740200 |
| Jogador 2 | 5-2 | 272 | BUY | STABILIZE | 39.0 | 7 | 86 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024443458765745163 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 2 | 5-2 | 273 | SELL | STABILIZE | 39.0 | 7 | 83 | 5 | 34.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -2949d735-3c16-4a45-835b-e11a9c12b16a |
| Jogador 2 | 5-2 | 274 | BUY | STABILIZE | 39.0 | 7 | 86 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07696524262428284 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 2 | 5-2 | 275 | SELL | STABILIZE | 39.0 | 7 | 82 | 5 | 34.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -0d120db3-34e2-47e3-a57c-0d65dcc56342 |
| Jogador 2 | 5-2 | 276 | BUY | STABILIZE | 39.0 | 7 | 86 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28285279870033264 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 2 | 5-2 | 277 | SELL | STABILIZE | 39.0 | 7 | 83 | 5 | 34.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -c69a2be1-356a-4576-9887-6d1790221a5e |
| Jogador 2 | 5-2 | 278 | BUY | STABILIZE | 39.0 | 7 | 86 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2541247308254242 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 2 | 5-2 | 279 | SELL | STABILIZE | 39.0 | 7 | 84 | 5 | 34.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -ff181737-4995-4a67-add2-4f55cebabbee |
| Jogador 2 | 5-2 | 280 | BUY | STABILIZE | 39.0 | 7 | 86 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25412148237228394 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 2 | 5-3 | 282 | SELL | STABILIZE | 39.0 | 7 | 95 | 5 | 34.0 | Feérico/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 2 | 5-3 | 283 | BUY | STABILIZE | 39.0 | 7 | 97 | 5 | 34.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0233538150787354 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5,9d2d95f2-c079-43eb-a4cd-37b224a473a8 |
| Jogador 2 | 5-3 | 284 | BUY | STABILIZE | 39.0 | 7 | 94 | 5 | 28.0 | Feérico/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12537822127342224 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 2 | 5-3 | 285 | MOVE_BENCH | STABILIZE | 39.0 | 7 | 91 | 5 | 28.0 | Feérico/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0542524978518486 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 286 | SELL | STABILIZE | 39.0 | 7 | 91 | 5 | 32.0 | Feérico/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 2 | 5-3 | 287 | BUY | STABILIZE | 39.0 | 7 | 99 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.000175245018908754 | 0.0 | 0.0 | +c7762d7d-bcfa-4694-a3fc-038d7242207f / -— |
| Jogador 2 | 5-3 | 288 | BUY_XP | STABILIZE | 39.0 | 7 | 96 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04732000082731247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 289 | BUY_XP | STABILIZE | 39.0 | 7 | 92 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04732000082731247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 290 | BUY_XP | STABILIZE | 39.0 | 7 | 88 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04732000082731247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 292 | SELL | STABILIZE | 39.0 | 7 | 94 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00426666671410203 | 0.0 | 0.0 | +— / -c7762d7d-bcfa-4694-a3fc-038d7242207f |
| Jogador 2 | 5-4 | 293 | BUY | STABILIZE | 39.0 | 7 | 97 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9739224314689636 | 0.0 | 0.0 | +d5c73756-6784-44e9-b521-5c61db813319 / -— |
| Jogador 2 | 5-4 | 294 | SELL | STABILIZE | 39.0 | 7 | 96 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012066666968166828 | 0.0 | 0.0 | +— / -6c338d19-b3d3-49a7-b61e-4732249ee457 |
| Jogador 2 | 5-4 | 295 | BUY | STABILIZE | 39.0 | 7 | 99 | 5 | 32.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0191917419433594 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -584e7960-a541-4d45-8ea1-8a75e288c387,a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 5-4 | 296 | MOVE_BENCH | STABILIZE | 39.0 | 7 | 98 | 5 | 30.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15169893205165863 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 297 | BUY | FAST8 | 39.0 | 7 | 98 | 5 | 36.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18354743719100952 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 2 | 5-4 | 298 | MOVE_BOARD | FAST8 | 39.0 | 7 | 93 | 5 | 36.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001437683094991371 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 299 | BUY_XP | FAST8 | 39.0 | 7 | 93 | 5 | 36.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026799999177455902 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 300 | MOVE_BENCH | FAST8 | 39.0 | 7 | 89 | 5 | 36.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5995531678199768 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 302 | BUY | STABILIZE | 39.0 | 8 | 99 | 5 | 42.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0021896346006542444 | 0.0 | 0.0 | +98991369-e5f0-4725-928c-f2fa5362bf73 / -— |
| Jogador 2 | 5-5 | 303 | BUY | STABILIZE | 39.0 | 8 | 96 | 5 | 42.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06592642515897751 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 2 | 5-5 | 304 | MOVE_BENCH | STABILIZE | 39.0 | 8 | 92 | 5 | 42.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44054359197616577 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 305 | BUY | STABILIZE | 39.0 | 8 | 92 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1550757884979248 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -— |
| Jogador 2 | 5-5 | 306 | MOVE_BOARD | STABILIZE | 39.0 | 8 | 89 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.572909215814434e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 307 | MOVE_BOARD | STABILIZE | 39.0 | 8 | 89 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 308 | MOVE_BOARD | STABILIZE | 39.0 | 8 | 89 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024108797311782837 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 309 | PASS | STABILIZE | 39.0 | 8 | 89 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13530896604061127 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 312 | SELL | ALL_IN | 24.0 | 8 | 99 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.600766658782959 | 0.0 | 0.0 | +— / -d8392323-28e4-4e98-a466-5958bf400729 |
| Jogador 2 | 5-6 | 313 | BUY | ALL_IN | 24.0 | 8 | 102 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.23331382870674133 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 2 | 5-6 | 314 | EQUIP_FROM_INVENTORY | ALL_IN | 24.0 | 8 | 98 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12013948708772659 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 315 | EQUIP_FROM_INVENTORY | ALL_IN | 24.0 | 8 | 98 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05944760888814926 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 316 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 98 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004939705249853432 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 317 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 98 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01119624637067318 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 318 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 98 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014271148480474949 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 319 | PASS | ALL_IN | 24.0 | 8 | 98 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5041682720184326 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 322 | SELL | ALL_IN | 24.0 | 8 | 109 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -aea521ef-8511-4b98-9c6d-e83b814777df |
| Jogador 2 | 5-7 | 323 | BUY | ALL_IN | 24.0 | 8 | 112 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.920874834060669 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -— |
| Jogador 2 | 5-7 | 324 | SELL | ALL_IN | 24.0 | 8 | 109 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -98991369-e5f0-4725-928c-f2fa5362bf73 |
| Jogador 2 | 5-7 | 325 | BUY | ALL_IN | 24.0 | 8 | 112 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38887128233909607 | 0.0 | 0.0 | +551e9535-d584-4055-a544-ed78d65ecacb / -— |
| Jogador 2 | 5-7 | 326 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 109 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.068974911002442e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 327 | SELL | ALL_IN | 24.0 | 8 | 109 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -f6000a82-1241-4220-9362-c8d788472db0 |
| Jogador 2 | 5-7 | 328 | BUY | ALL_IN | 24.0 | 8 | 113 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005087587516754866 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 2 | 5-7 | 329 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 110 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 330 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 110 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 332 | EQUIP_FROM_INVENTORY | ALL_IN | 24.0 | 8 | 120 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07410232722759247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 333 | SELL | ALL_IN | 24.0 | 8 | 120 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -01c587bb-ca4f-4690-9e4b-d1e9c44fd33e |
| Jogador 2 | 6-1 | 334 | BUY | ALL_IN | 24.0 | 8 | 123 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1421155482530594 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 2 | 6-1 | 335 | SELL | ALL_IN | 24.0 | 8 | 119 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -85fb6db6-e1b0-4fa1-b99a-2f205305ef0b |
| Jogador 2 | 6-1 | 336 | BUY | ALL_IN | 24.0 | 8 | 123 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21862134337425232 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -— |
| Jogador 2 | 6-1 | 337 | SELL | ALL_IN | 24.0 | 8 | 119 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -9f1c634e-13c7-4b59-838c-4b676fa059be |
| Jogador 2 | 6-1 | 338 | BUY | ALL_IN | 24.0 | 8 | 123 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22656817734241486 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 2 | 6-1 | 339 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 120 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 340 | MOVE_BOARD | ALL_IN | 24.0 | 8 | 120 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999955892562866 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 342 | SELL | ALL_IN | 24.0 | 8 | 130 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -be1e11e4-dc58-4e75-a402-3a2d831ac7b3 |
| Jogador 2 | 6-2 | 343 | BUY | ALL_IN | 24.0 | 8 | 133 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19649775326251984 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 2 | 6-2 | 344 | SELL | ALL_IN | 24.0 | 8 | 131 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031110331416130066 | 0.0 | 0.0 | +— / -a37d8478-8a98-4099-bb18-3602d68764f5 |
| Jogador 2 | 6-2 | 345 | BUY | ALL_IN | 24.0 | 8 | 133 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07668177038431168 | 0.0 | 0.0 | +68a0405b-6231-471f-98a5-1661d32f4ac4 / -— |
| Jogador 2 | 6-2 | 346 | SELL | ALL_IN | 24.0 | 8 | 129 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0077333333902060986 | 0.0 | 0.0 | +— / -68a0405b-6231-471f-98a5-1661d32f4ac4 |
| Jogador 2 | 6-2 | 347 | BUY | ALL_IN | 24.0 | 8 | 133 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1817069947719574 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 2 | 6-2 | 348 | SELL | ALL_IN | 24.0 | 8 | 131 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -6eff87be-d18f-4f46-a9c6-9ae977c887e0 |
| Jogador 2 | 6-2 | 349 | BUY | ALL_IN | 24.0 | 8 | 133 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03539232909679413 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 2 | 6-2 | 350 | SELL | ALL_IN | 24.0 | 8 | 131 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015796800144016743 | 0.0 | 0.0 | +— / -b311d350-7bab-48ee-9833-0883606b4a2f |
| Jogador 2 | 6-3 | 352 | BUY | ALL_IN | 24.0 | 8 | 143 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.950688898563385 | 0.0 | 0.0 | +4261ad99-2607-4d90-978c-9e9abffd6d95 / -— |
| Jogador 2 | 6-3 | 353 | SELL | ALL_IN | 24.0 | 8 | 140 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059714753180742264 | 0.0 | 0.0 | +— / -f087511a-d834-4f41-9b99-00bf0f6dc061 |
| Jogador 2 | 6-3 | 354 | BUY | ALL_IN | 24.0 | 8 | 144 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05788857862353325 | 0.0 | 0.0 | +b1d58916-6d8b-4071-a37d-a478395e6a1e / -— |
| Jogador 2 | 6-3 | 355 | SELL | ALL_IN | 24.0 | 8 | 140 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -b1d58916-6d8b-4071-a37d-a478395e6a1e |
| Jogador 2 | 6-3 | 356 | BUY | ALL_IN | 24.0 | 8 | 144 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05689222738146782 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 2 | 6-3 | 357 | SELL | ALL_IN | 24.0 | 8 | 140 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005357139743864536 | 0.0 | 0.0 | +— / -920ec426-49cf-489f-aad8-3f5461b93be6 |
| Jogador 2 | 6-3 | 358 | BUY | ALL_IN | 24.0 | 8 | 144 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2340993881225586 | 0.0 | 0.0 | +56332309-e8e8-464a-904f-e9253912cd2f / -— |
| Jogador 2 | 6-3 | 359 | SELL | ALL_IN | 24.0 | 8 | 142 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -56332309-e8e8-464a-904f-e9253912cd2f |
| Jogador 2 | 6-3 | 360 | BUY | ALL_IN | 24.0 | 8 | 144 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24119620025157928 | 0.0 | 0.0 | +e89905aa-6564-4e15-bc3a-c281646446bc / -— |
| Jogador 2 | 6-4 | 362 | SELL | ALL_IN | 24.0 | 8 | 153 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -e89905aa-6564-4e15-bc3a-c281646446bc |
| Jogador 2 | 6-4 | 363 | BUY | ALL_IN | 24.0 | 8 | 154 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1098545789718628 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -4261ad99-2607-4d90-978c-9e9abffd6d95,551e9535-d584-4055-a544-ed78d65ecacb |
| Jogador 2 | 6-4 | 364 | BUY | ALL_IN | 24.0 | 8 | 151 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05686792731285095 | 0.0 | 0.0 | +3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 / -— |
| Jogador 2 | 6-4 | 365 | BUY | ALL_IN | 24.0 | 8 | 147 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6118570566177368 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 2 | 6-4 | 366 | SELL | ALL_IN | 24.0 | 8 | 143 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6832000017166138 | 0.0 | 0.0 | +— / -a810e10d-e7ef-4ece-8fb2-8b6471b557ec |
| Jogador 2 | 6-4 | 367 | BUY | ALL_IN | 24.0 | 8 | 151 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1438480168581009 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 2 | 6-4 | 368 | BUY_XP | ALL_IN | 24.0 | 8 | 147 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.160007506608963 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 369 | BUY_XP | ALL_IN | 24.0 | 8 | 143 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15925750136375427 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 370 | BUY_XP | ALL_IN | 24.0 | 8 | 139 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15850749611854553 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 372 | SELL | ALL_IN | 24.0 | 8 | 145 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -2ac6d717-87f1-4421-929e-1934a9317e72 |
| Jogador 2 | 6-5 | 373 | BUY | ALL_IN | 24.0 | 8 | 149 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46604669094085693 | 0.0 | 0.0 | +3a17cc98-2024-4ac0-b627-9a751d138cd9 / -— |
| Jogador 2 | 6-5 | 374 | SELL | ALL_IN | 24.0 | 8 | 146 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5393333435058594 | 0.0 | 0.0 | +— / -3e7b8e2e-528d-42bb-8c2a-bf9f833e7c77 |
| Jogador 2 | 6-5 | 375 | BUY | ALL_IN | 24.0 | 8 | 150 | 5 | 52.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7607836127281189 | 0.0 | 0.0 | +e29db20a-6b71-4518-ac7d-1e5d9eb67582 / -91966802-adc2-46d2-9e7e-194283bca85c,d1840f93-35b0-4e88-b58e-eea7267beedc |
| Jogador 2 | 6-5 | 376 | MOVE_BENCH | ALL_IN | 24.0 | 8 | 147 | 5 | 40.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2651597857475281 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 377 | BUY | ALL_IN | 24.0 | 8 | 147 | 5 | 46.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004214304964989424 | 0.0 | 0.0 | +5d95f8bc-0c01-4c67-8764-4410eb32ee93 / -— |
| Jogador 2 | 6-5 | 378 | SELL | ALL_IN | 24.0 | 8 | 144 | 5 | 46.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06363333016633987 | 0.0 | 0.0 | +— / -e29db20a-6b71-4518-ac7d-1e5d9eb67582 |
| Jogador 2 | 6-5 | 379 | BUY | ALL_IN | 24.0 | 8 | 152 | 5 | 46.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | -0.2636420428752899 | 0.0 | 0.0 | +46b04fe4-ef4d-4449-94d0-d8bc9660c4e0 / -— |
| Jogador 2 | 6-5 | 380 | MOVE_BENCH | ALL_IN | 24.0 | 8 | 150 | 5 | 46.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4001447856426239 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 382 | BUY | ALL_IN | 3.0 | 8 | 160 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7056468725204468 | 0.0 | 0.0 | +c55e9bf2-c9cf-4b76-a40c-6e8d73205402 / -— |
| Jogador 2 | 6-6 | 383 | EQUIP_FROM_INVENTORY | ALL_IN | 3.0 | 8 | 156 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07415493577718735 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 384 | EQUIP_FROM_INVENTORY | ALL_IN | 3.0 | 8 | 156 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06189693883061409 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 385 | SELL | ALL_IN | 3.0 | 8 | 156 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0003558626922313124 | 0.0 | 0.0 | +— / -5d95f8bc-0c01-4c67-8764-4410eb32ee93 |
| Jogador 2 | 6-6 | 386 | BUY | ALL_IN | 3.0 | 8 | 159 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17838382720947266 | 0.0 | 0.0 | +9f271ee0-c506-40b7-b3f3-bac209974ba2 / -— |
| Jogador 2 | 6-6 | 387 | SELL | ALL_IN | 3.0 | 8 | 158 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -9f271ee0-c506-40b7-b3f3-bac209974ba2 |
| Jogador 2 | 6-6 | 388 | BUY | ALL_IN | 3.0 | 8 | 159 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24174293875694275 | 0.0 | 0.0 | +8c4772c9-83f1-4021-b83f-a9ff1773bea0 / -— |
| Jogador 2 | 6-6 | 389 | SELL | ALL_IN | 3.0 | 8 | 155 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013933333568274975 | 0.0 | 0.0 | +— / -8c4772c9-83f1-4021-b83f-a9ff1773bea0 |
| Jogador 2 | 6-6 | 390 | BUY | ALL_IN | 3.0 | 8 | 159 | 5 | 50.0 | Feérico/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20537568628787994 | 0.0 | 0.0 | +87902519-e44a-4d4c-9956-ac5aedc9b0c6 / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08146253973245621 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22444601356983185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0904720276594162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4064550995826721 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0396647453308105 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179777383804321 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009961719624698162 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5897860527038574 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2272767424583435 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21242481470108032 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2642510235309601 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25187569856643677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23012398183345795 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39559081196784973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21812109649181366 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007085069082677364 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 61 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9590535163879395 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 65 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3374614119529724 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 66 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33307790756225586 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 73 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26547107100486755 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 74 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 75 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 82 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8901299834251404 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -— |
| Jogador 3 | 2-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40741997957229614 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 84 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.152047261595726 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08526350557804108 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07939225435256958 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01492172572761774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 89 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 92 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8983666300773621 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 3 | 2-5 | 93 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 94 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 102 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01022229716181755 | 0.0 | 0.0 | +— / -5ead8548-7453-4fa1-856e-674995576a48 |
| Jogador 3 | 2-6 | 103 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9474310278892517 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -c70251e8-af44-4466-808f-d49e9e5f57e9,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-6 | 104 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5998446941375732 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 105 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.949966311454773 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 3 | 2-6 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5991642475128174 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 107 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05727062746882439 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 3 | 2-6 | 108 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.7935384676093236e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014764945022761822 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 112 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8882485032081604 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 113 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16227300465106964 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 114 | SELL | STABILIZE | 100.0 | 5 | 3 | 0 | 24.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014466666616499424 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 3 | 2-7 | 115 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1689334362745285 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 3 | 2-7 | 116 | SELL | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008439739234745502 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 2-7 | 117 | SELL | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11879843473434448 | 0.0 | 0.0 | +— / -41db1132-4e1c-48eb-8a9b-1b2c74cb22ce |
| Jogador 3 | 2-7 | 118 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6330000162124634 | 0.0 | 0.0 | +— / -e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 3 | 2-7 | 119 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019639788661152124 | 0.0 | 0.0 | +432bc6b0-03a8-42f3-a147-d165f4172a8f / -— |
| Jogador 3 | 2-7 | 120 | BUY_XP | STABILIZE | 100.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04806999862194061 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 122 | BUY | STABILIZE | 100.0 | 6 | 11 | 1 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20113149285316467 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25847864151000977 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 124 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40004289150238037 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 125 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6883208751678467 | 0.0 | 0.0 | +19cf270e-27a1-4d3c-bef7-0b1af400d07c / -— |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004137182841077447 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 128 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015140024945139885 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 129 | PASS | STABILIZE | 100.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 132 | BUY | STABILIZE | 100.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8203579187393188 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-2 | 133 | BUY | STABILIZE | 100.0 | 6 | 15 | 1 | 24.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7751079797744751 | 0.0 | 0.0 | +f2020469-2f4e-4b95-96e4-1e7d091f1ab0 / -19cf270e-27a1-4d3c-bef7-0b1af400d07c,432bc6b0-03a8-42f3-a147-d165f4172a8f |
| Jogador 3 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 14 | 1 | 22.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16867457330226898 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 135 | BUY | STABILIZE | 100.0 | 6 | 14 | 1 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06455493718385696 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 136 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015138690359890461 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 138 | PASS | STABILIZE | 100.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 142 | BUY | STABILIZE | 90.0 | 6 | 17 | 1 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8058741688728333 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 143 | BUY | STABILIZE | 90.0 | 6 | 15 | 1 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24806863069534302 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 144 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0003344610158819705 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 145 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015101403929293156 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013858510181307793 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 147 | PASS | STABILIZE | 90.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 152 | SELL | STABILIZE | 90.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004487771540880203 | 0.0 | 0.0 | +— / -f2020469-2f4e-4b95-96e4-1e7d091f1ab0 |
| Jogador 3 | 3-4 | 153 | BUY | STABILIZE | 90.0 | 6 | 21 | 2 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7288667559623718 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6465780735015869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 155 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08500505238771439 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6615779399871826 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 158 | PASS | STABILIZE | 90.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 162 | SELL | STABILIZE | 90.0 | 6 | 24 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41575556993484497 | 0.0 | 0.0 | +— / -2d1296a3-9aa4-42ab-8b86-34661e32a63d |
| Jogador 3 | 3-5 | 163 | BUY | STABILIZE | 90.0 | 6 | 27 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8487100005149841 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-5 | 164 | BUY | STABILIZE | 90.0 | 6 | 24 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2472964972257614 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 165 | BUY | STABILIZE | 90.0 | 6 | 21 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06691092997789383 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10000584274530411 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 167 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 17 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6610590815544128 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 168 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 17 | 1 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6516704559326172 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 169 | PASS | STABILIZE | 90.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 172 | SELL | STABILIZE | 90.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 |
| Jogador 3 | 3-6 | 173 | BUY | STABILIZE | 90.0 | 6 | 30 | 3 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7859750390052795 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -bca8862c-5e5b-4a51-9173-79218fbfea3d,f0b6c16b-7610-454c-929d-7152f0a041d3 |
| Jogador 3 | 3-6 | 174 | BUY | STABILIZE | 90.0 | 6 | 28 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7697986960411072 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 175 | BUY | STABILIZE | 90.0 | 6 | 25 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015333395451307297 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -— |
| Jogador 3 | 3-6 | 176 | BUY_XP | STABILIZE | 90.0 | 6 | 23 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 177 | SELL | STABILIZE | 90.0 | 6 | 19 | 1 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5 | 0.0 | 0.0 | +— / -0e31b1ec-3ead-480e-8577-f59bb5486d00 |
| Jogador 3 | 3-6 | 178 | BUY | STABILIZE | 90.0 | 6 | 24 | 2 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03614902123808861 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 3 | 3-6 | 179 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 23 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007853240240365267 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 180 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 23 | 2 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01421168353408575 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 182 | SELL | STABILIZE | 81.0 | 6 | 30 | 3 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5740000009536743 | 0.0 | 0.0 | +— / -a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 3 | 3-7 | 183 | BUY | STABILIZE | 81.0 | 6 | 38 | 3 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30093032121658325 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 184 | SELL | STABILIZE | 81.0 | 6 | 35 | 3 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006481201853603125 | 0.0 | 0.0 | +— / -1489b596-9339-407a-b49f-d01ecfdd6f78 |
| Jogador 3 | 3-7 | 185 | BUY | STABILIZE | 81.0 | 6 | 36 | 3 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24098201096057892 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 33 | 3 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -7.415992087089762e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 33 | 3 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499907299876213 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 188 | PASS | STABILIZE | 81.0 | 6 | 33 | 3 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 81.0 | 6 | 41 | 4 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17436330020427704 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 81.0 | 6 | 41 | 4 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.236711323261261 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 194 | SELL | STABILIZE | 81.0 | 6 | 41 | 4 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010301060974597931 | 0.0 | 0.0 | +— / -27102740-ce4d-4bec-a9eb-ed936f6bc364 |
| Jogador 3 | 4-1 | 195 | BUY | STABILIZE | 81.0 | 6 | 43 | 4 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8545872569084167 | 0.0 | 0.0 | +9175d2a8-4736-402d-873b-cf4846b04d97 / -— |
| Jogador 3 | 4-1 | 196 | SELL | STABILIZE | 81.0 | 6 | 40 | 4 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04144737869501114 | 0.0 | 0.0 | +— / -ccdd8153-af58-4fe7-994c-d49f0a7a17f8 |
| Jogador 3 | 4-1 | 197 | BUY | STABILIZE | 81.0 | 6 | 44 | 4 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9079274535179138 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9,b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 3 | 4-1 | 198 | BUY | STABILIZE | 81.0 | 6 | 41 | 4 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20375066995620728 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 3 | 4-1 | 199 | BUY | STABILIZE | 81.0 | 6 | 37 | 3 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2693306803703308 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 3 | 4-1 | 200 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 35 | 3 | 30.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08924052119255066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 202 | SELL | STABILIZE | 69.0 | 6 | 44 | 4 | 32.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0380406454205513 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 3 | 4-2 | 203 | BUY | STABILIZE | 69.0 | 6 | 52 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8441148400306702 | 0.0 | 0.0 | +f394f34c-c68b-4213-9eb0-88f302976405 / -— |
| Jogador 3 | 4-2 | 204 | SELL | STABILIZE | 69.0 | 6 | 50 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -465ecc70-f5da-47f4-a7c0-2005a8ed24c1 |
| Jogador 3 | 4-2 | 205 | BUY | STABILIZE | 69.0 | 6 | 52 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05248638242483139 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 3 | 4-2 | 206 | SELL | STABILIZE | 69.0 | 6 | 49 | 4 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06256666779518127 | 0.0 | 0.0 | +— / -4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 3 | 4-2 | 207 | BUY | STABILIZE | 69.0 | 6 | 52 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005919229704886675 | 0.0 | 0.0 | +cb216a0d-8bff-41f9-99bd-231ca5186fb5 / -— |
| Jogador 3 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 50 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.706442832182802e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 209 | SELL | STABILIZE | 69.0 | 6 | 50 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012045854702591896 | 0.0 | 0.0 | +— / -cb216a0d-8bff-41f9-99bd-231ca5186fb5 |
| Jogador 3 | 4-2 | 210 | BUY | STABILIZE | 69.0 | 6 | 52 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045935265719890594 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 3 | 4-3 | 212 | SELL | STABILIZE | 69.0 | 6 | 61 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016963813453912735 | 0.0 | 0.0 | +— / -090f2ba6-5514-49ba-a80d-a0711cd06245 |
| Jogador 3 | 4-3 | 213 | BUY | STABILIZE | 69.0 | 6 | 63 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11556314677000046 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 3 | 4-3 | 214 | SELL | STABILIZE | 69.0 | 6 | 60 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03713417425751686 | 0.0 | 0.0 | +— / -3bbd7105-b508-437d-ac84-11e01a499779 |
| Jogador 3 | 4-3 | 215 | BUY | STABILIZE | 69.0 | 6 | 63 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2323852777481079 | 0.0 | 0.0 | +7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed / -— |
| Jogador 3 | 4-3 | 216 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 59 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6362341046333313 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 217 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 59 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08031607419252396 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 218 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 59 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20618775486946106 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 219 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 59 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6359944939613342 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 220 | PASS | STABILIZE | 69.0 | 6 | 59 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08530551940202713 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 222 | SELL | STABILIZE | 69.0 | 6 | 71 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed |
| Jogador 3 | 4-4 | 223 | BUY | STABILIZE | 69.0 | 6 | 75 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2638660669326782 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 3 | 4-4 | 224 | SELL | STABILIZE | 69.0 | 6 | 72 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 3 | 4-4 | 225 | BUY | STABILIZE | 69.0 | 6 | 75 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26960495114326477 | 0.0 | 0.0 | +b5b3098f-d48c-42b8-8022-639a25225980 / -— |
| Jogador 3 | 4-4 | 226 | SELL | STABILIZE | 69.0 | 6 | 73 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -b5b3098f-d48c-42b8-8022-639a25225980 |
| Jogador 3 | 4-4 | 227 | BUY | STABILIZE | 69.0 | 6 | 75 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2696070075035095 | 0.0 | 0.0 | +fb551efa-6ad5-4f97-aa05-bc5eb70943d4 / -— |
| Jogador 3 | 4-4 | 228 | SELL | STABILIZE | 69.0 | 6 | 73 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -fb551efa-6ad5-4f97-aa05-bc5eb70943d4 |
| Jogador 3 | 4-4 | 229 | BUY | STABILIZE | 69.0 | 6 | 75 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27500396966934204 | 0.0 | 0.0 | +b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 / -— |
| Jogador 3 | 4-4 | 230 | SELL | STABILIZE | 69.0 | 6 | 74 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018699999898672104 | 0.0 | 0.0 | +— / -b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 |
| Jogador 3 | 4-5 | 232 | BUY | STABILIZE | 69.0 | 6 | 86 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35804033279418945 | 0.0 | 0.0 | +8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e / -— |
| Jogador 3 | 4-5 | 233 | SELL | STABILIZE | 69.0 | 6 | 83 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -527f78df-1e51-4731-9175-1c4812aa82ad |
| Jogador 3 | 4-5 | 234 | BUY | STABILIZE | 69.0 | 6 | 87 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.126050665974617 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 3 | 4-5 | 235 | SELL | STABILIZE | 69.0 | 6 | 84 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -42733dbd-0bc3-461b-95ab-76daf5ad6296 |
| Jogador 3 | 4-5 | 236 | BUY | STABILIZE | 69.0 | 6 | 88 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1599745750427246 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 3 | 4-5 | 237 | SELL | STABILIZE | 69.0 | 6 | 86 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027621226385235786 | 0.0 | 0.0 | +— / -f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 3 | 4-5 | 238 | BUY | STABILIZE | 69.0 | 6 | 88 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22694693505764008 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 3 | 4-5 | 239 | SELL | STABILIZE | 69.0 | 6 | 86 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -b1efce8c-0cb0-47fc-a361-c50a76c0f9de |
| Jogador 3 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 88 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.2645139924625255e-08 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 242 | BUY | STABILIZE | 69.0 | 6 | 100 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3929285705089569 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 3 | 4-6 | 243 | SELL | STABILIZE | 69.0 | 6 | 99 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07444382458925247 | 0.0 | 0.0 | +— / -8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e |
| Jogador 3 | 4-6 | 244 | BUY | STABILIZE | 69.0 | 6 | 102 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36685195565223694 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 3 | 4-6 | 245 | SELL | STABILIZE | 69.0 | 6 | 100 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -ec9662c5-0734-41a3-9999-224d7716228b |
| Jogador 3 | 4-6 | 246 | BUY | STABILIZE | 69.0 | 6 | 101 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29570913314819336 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 3 | 4-6 | 247 | SELL | STABILIZE | 69.0 | 6 | 98 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4025450050830841 | 0.0 | 0.0 | +— / -20821a31-3317-4f82-bbb2-b70cdebdd893 |
| Jogador 3 | 4-6 | 248 | BUY | STABILIZE | 69.0 | 6 | 101 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2972559928894043 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 3 | 4-6 | 249 | SELL | STABILIZE | 69.0 | 6 | 98 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40274709463119507 | 0.0 | 0.0 | +— / -3bfc4626-3226-44b6-a401-ff9c18761448 |
| Jogador 3 | 4-6 | 250 | BUY | STABILIZE | 69.0 | 6 | 101 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3268640339374542 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 3 | 4-7 | 252 | SELL | STABILIZE | 57.0 | 6 | 109 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1001693606376648 | 0.0 | 0.0 | +— / -023f01af-91d0-4e07-8229-2b7cded83151 |
| Jogador 3 | 4-7 | 253 | BUY | STABILIZE | 57.0 | 6 | 111 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9633733630180359 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -9175d2a8-4736-402d-873b-cf4846b04d97,bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-7 | 254 | BUY | STABILIZE | 57.0 | 6 | 108 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018149379640817642 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 3 | 4-7 | 255 | BUY | STABILIZE | 57.0 | 6 | 106 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20553766191005707 | 0.0 | 0.0 | +57d86f23-f167-472f-9878-21dcddc0a5f7 / -— |
| Jogador 3 | 4-7 | 256 | SELL | STABILIZE | 57.0 | 6 | 103 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -362f7357-283e-4f88-bff3-ffa6314af821 |
| Jogador 3 | 4-7 | 257 | BUY | STABILIZE | 57.0 | 6 | 111 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02525750733911991 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 3 | 4-7 | 258 | SELL | STABILIZE | 57.0 | 6 | 109 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015533333644270897 | 0.0 | 0.0 | +— / -a3def045-2a10-4672-a6d6-255c40fd1c90 |
| Jogador 3 | 4-7 | 259 | BUY | STABILIZE | 57.0 | 6 | 111 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015542320907115936 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -— |
| Jogador 3 | 4-7 | 260 | SELL | STABILIZE | 57.0 | 6 | 110 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005455316044390202 | 0.0 | 0.0 | +— / -943437ce-e190-4790-986b-4e66e49637a7 |
| Jogador 3 | 5-1 | 262 | BUY | STABILIZE | 57.0 | 7 | 121 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.347528338432312 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -— |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 57.0 | 7 | 119 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22150222957134247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 57.0 | 7 | 119 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13777901232242584 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 265 | SELL | STABILIZE | 57.0 | 7 | 119 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02805255353450775 | 0.0 | 0.0 | +— / -d80c845d-24bc-4053-a60d-5d0122839b0c |
| Jogador 3 | 5-1 | 266 | BUY | STABILIZE | 57.0 | 7 | 121 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058034785091876984 | 0.0 | 0.0 | +685fc2a9-6a67-445e-ab34-59ec1f986f8e / -— |
| Jogador 3 | 5-1 | 267 | SELL | STABILIZE | 57.0 | 7 | 120 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -57d86f23-f167-472f-9878-21dcddc0a5f7 |
| Jogador 3 | 5-1 | 268 | BUY | STABILIZE | 57.0 | 7 | 123 | 5 | 30.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.739332914352417 | 0.0 | 0.0 | +952ea2b4-387d-455d-b1ad-fb0de8c46e47 / -— |
| Jogador 3 | 5-1 | 269 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 122 | 5 | 30.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4748045802116394 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 270 | BUY | FAST8 | 57.0 | 7 | 122 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018260307610034943 | 0.0 | 0.0 | +811fcf1f-2023-4c36-a961-d61cb0dd68d0 / -— |
| Jogador 3 | 5-2 | 272 | SELL | FAST8 | 57.0 | 7 | 132 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027041975408792496 | 0.0 | 0.0 | +— / -811fcf1f-2023-4c36-a961-d61cb0dd68d0 |
| Jogador 3 | 5-2 | 273 | BUY | FAST8 | 57.0 | 7 | 133 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8687798380851746 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 3 | 5-2 | 274 | SELL | FAST8 | 57.0 | 7 | 132 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37990882992744446 | 0.0 | 0.0 | +— / -9028d514-586b-4d0e-b042-07389323c8cf |
| Jogador 3 | 5-2 | 275 | BUY | FAST8 | 57.0 | 7 | 135 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15541525185108185 | 0.0 | 0.0 | +678a6f43-ca48-46c9-8c5b-6790493f4841 / -— |
| Jogador 3 | 5-2 | 276 | SELL | FAST8 | 57.0 | 7 | 133 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010522512719035149 | 0.0 | 0.0 | +— / -678a6f43-ca48-46c9-8c5b-6790493f4841 |
| Jogador 3 | 5-2 | 277 | BUY | FAST8 | 57.0 | 7 | 135 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2070605456829071 | 0.0 | 0.0 | +77489602-9456-4a97-aa7e-df7ef91d5e4a / -— |
| Jogador 3 | 5-2 | 278 | MOVE_BOARD | FAST8 | 57.0 | 7 | 132 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00011750214616768062 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 279 | MOVE_BOARD | FAST8 | 57.0 | 7 | 132 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014997856691479683 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 280 | MOVE_BOARD | FAST8 | 57.0 | 7 | 132 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 282 | SELL | FAST8 | 57.0 | 7 | 142 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -77489602-9456-4a97-aa7e-df7ef91d5e4a |
| Jogador 3 | 5-3 | 283 | BUY | FAST8 | 57.0 | 7 | 145 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8646572232246399 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 3 | 5-3 | 284 | SELL | FAST8 | 57.0 | 7 | 142 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09688464552164078 | 0.0 | 0.0 | +— / -02e125a0-3563-47ec-a82a-cba5178731dd |
| Jogador 3 | 5-3 | 285 | BUY | FAST8 | 57.0 | 7 | 144 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9171878099441528 | 0.0 | 0.0 | +1c5a9322-14c8-4df9-937b-842dcaa1f372 / -ab6084b0-65df-4a70-8591-687b320d98b6,f394f34c-c68b-4213-9eb0-88f302976405 |
| Jogador 3 | 5-3 | 286 | BUY | STABILIZE | 57.0 | 7 | 142 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05137717351317406 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 3 | 5-3 | 287 | SELL | STABILIZE | 57.0 | 7 | 139 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -1c5a9322-14c8-4df9-937b-842dcaa1f372 |
| Jogador 3 | 5-3 | 288 | BUY | STABILIZE | 57.0 | 7 | 144 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25022125244140625 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -— |
| Jogador 3 | 5-3 | 289 | BUY_XP | STABILIZE | 57.0 | 7 | 141 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04732000082731247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 290 | BUY_XP | STABILIZE | 57.0 | 7 | 137 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04732000082731247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 292 | SELL | STABILIZE | 57.0 | 7 | 145 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016100000590085983 | 0.0 | 0.0 | +— / -e9bb05f6-3838-423a-bfd2-3791379b479e |
| Jogador 3 | 5-4 | 293 | BUY | STABILIZE | 57.0 | 7 | 148 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9263085126876831 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -— |
| Jogador 3 | 5-4 | 294 | SELL | STABILIZE | 57.0 | 7 | 146 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02106310985982418 | 0.0 | 0.0 | +— / -aee0c45d-0178-4238-987f-5ee83dae7bce |
| Jogador 3 | 5-4 | 295 | BUY | STABILIZE | 57.0 | 7 | 149 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2572920620441437 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 3 | 5-4 | 296 | SELL | STABILIZE | 57.0 | 7 | 146 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3793957829475403 | 0.0 | 0.0 | +— / -b2517873-8317-401b-8461-1d86969edbd7 |
| Jogador 3 | 5-4 | 297 | BUY | STABILIZE | 57.0 | 7 | 149 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25173288583755493 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -— |
| Jogador 3 | 5-4 | 298 | SELL | STABILIZE | 57.0 | 7 | 146 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06840000301599503 | 0.0 | 0.0 | +— / -1512b230-15a6-405f-9b6b-4387a3091648 |
| Jogador 3 | 5-4 | 299 | BUY | STABILIZE | 57.0 | 7 | 149 | 5 | 32.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03816517814993858 | 0.0 | 0.0 | +f0264dc3-6749-4682-929e-fab42383532a / -— |
| Jogador 3 | 5-4 | 300 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 147 | 5 | 32.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5863366723060608 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 302 | BUY | FAST8 | 57.0 | 7 | 158 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17710569500923157 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 3 | 5-5 | 303 | SELL | FAST8 | 57.0 | 7 | 155 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04790688678622246 | 0.0 | 0.0 | +— / -f0264dc3-6749-4682-929e-fab42383532a |
| Jogador 3 | 5-5 | 304 | BUY | FAST8 | 57.0 | 7 | 157 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12168874591588974 | 0.0 | 0.0 | +dcb61be2-9a58-49bc-9f11-2f5fce42e7ea / -— |
| Jogador 3 | 5-5 | 305 | SELL | FAST8 | 57.0 | 7 | 154 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051418058574199677 | 0.0 | 0.0 | +— / -dcb61be2-9a58-49bc-9f11-2f5fce42e7ea |
| Jogador 3 | 5-5 | 306 | BUY | FAST8 | 57.0 | 7 | 157 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11298881471157074 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 3 | 5-5 | 307 | MOVE_BOARD | FAST8 | 57.0 | 7 | 152 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 308 | SELL | FAST8 | 57.0 | 7 | 152 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -3faf4ab2-44b3-4779-985b-658c64791c28 |
| Jogador 3 | 5-5 | 309 | BUY | FAST8 | 57.0 | 7 | 155 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053751349449157715 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 3 | 5-5 | 310 | MOVE_BOARD | FAST8 | 57.0 | 7 | 152 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0001712885859888047 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 312 | SELL | FAST8 | 57.0 | 7 | 164 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -f2dbe099-e518-4261-b120-9f327b112dcb |
| Jogador 3 | 5-6 | 313 | BUY | FAST8 | 57.0 | 7 | 167 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1356416493654251 | 0.0 | 0.0 | +bbfa514f-8d07-411b-aa19-4511ae5fb5cd / -— |
| Jogador 3 | 5-6 | 314 | SELL | FAST8 | 57.0 | 7 | 164 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -bbfa514f-8d07-411b-aa19-4511ae5fb5cd |
| Jogador 3 | 5-6 | 315 | BUY | FAST8 | 57.0 | 7 | 167 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21888087689876556 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 3 | 5-6 | 316 | SELL | FAST8 | 57.0 | 7 | 163 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -2b89bd83-8449-4c63-9da2-62a46c68bdf5 |
| Jogador 3 | 5-6 | 317 | BUY | FAST8 | 57.0 | 7 | 167 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04054460674524307 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -— |
| Jogador 3 | 5-6 | 318 | MOVE_BOARD | FAST8 | 57.0 | 7 | 165 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00017180549912154675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 319 | MOVE_BOARD | FAST8 | 57.0 | 7 | 165 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 320 | MOVE_BOARD | FAST8 | 57.0 | 7 | 165 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01499960944056511 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 322 | SELL | FAST8 | 42.0 | 7 | 175 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018140099942684174 | 0.0 | 0.0 | +— / -7de5aac5-85d7-4add-b5a7-1c89be9d7e40 |
| Jogador 3 | 5-7 | 323 | BUY | FAST8 | 42.0 | 7 | 177 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4012935161590576 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 3 | 5-7 | 324 | SELL | FAST8 | 42.0 | 7 | 176 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02419999986886978 | 0.0 | 0.0 | +— / -8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 |
| Jogador 3 | 5-7 | 325 | BUY | FAST8 | 42.0 | 7 | 181 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1376117467880249 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 3 | 5-7 | 326 | SELL | FAST8 | 42.0 | 7 | 178 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055399999022483826 | 0.0 | 0.0 | +— / -2d5214b0-3e0c-4e71-8664-2459bf616650 |
| Jogador 3 | 5-7 | 327 | BUY | FAST8 | 42.0 | 7 | 181 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051530659198760986 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -— |
| Jogador 3 | 5-7 | 328 | SELL | FAST8 | 42.0 | 7 | 178 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -d4c27edc-9b7e-4a31-a967-3aa80766b470 |
| Jogador 3 | 5-7 | 329 | BUY | FAST8 | 42.0 | 7 | 181 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045990511775016785 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 3 | 5-7 | 330 | MOVE_BOARD | FAST8 | 42.0 | 7 | 179 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.994338987287847e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 332 | EQUIP_FROM_INVENTORY | FAST8 | 42.0 | 7 | 189 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06929408013820648 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 333 | SELL | FAST8 | 42.0 | 7 | 189 | 5 | 36.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 3 | 6-1 | 334 | BUY | FAST8 | 42.0 | 7 | 191 | 5 | 36.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.013728141784668 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -7643f027-a90f-4f3a-8b4c-7be4cba17f95,9a96b07c-5b37-4be7-855e-dc2d942e7171 |
| Jogador 3 | 6-1 | 335 | BUY | STABILIZE | 42.0 | 7 | 188 | 5 | 30.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24298007786273956 | 0.0 | 0.0 | +8faad4f9-9f15-49e8-94af-b4d28879cc0d / -— |
| Jogador 3 | 6-1 | 336 | SELL | STABILIZE | 42.0 | 7 | 185 | 5 | 30.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6003999710083008 | 0.0 | 0.0 | +— / -27079fe2-8808-47b7-8b10-9fb2834bb6ed |
| Jogador 3 | 6-1 | 337 | BUY | STABILIZE | 42.0 | 7 | 193 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24232123792171478 | 0.0 | 0.0 | +3c46b699-2b56-48d0-820c-b523c5153b9f / -— |
| Jogador 3 | 6-1 | 338 | SELL | STABILIZE | 42.0 | 7 | 190 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5913000106811523 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 3 | 6-1 | 339 | BUY | STABILIZE | 42.0 | 7 | 191 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12633661925792694 | 0.0 | 0.0 | +3365b4aa-125c-4f72-bcc5-01c5a205b9b0 / -— |
| Jogador 3 | 6-1 | 340 | MOVE_BENCH | STABILIZE | 42.0 | 7 | 188 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09986098110675812 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 342 | BUY | ALL_IN | 23.0 | 7 | 199 | 5 | 36.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8107920289039612 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -3c46b699-2b56-48d0-820c-b523c5153b9f,6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 |
| Jogador 3 | 6-2 | 343 | BUY | ALL_IN | 23.0 | 7 | 196 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055429648607969284 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 3 | 6-2 | 344 | SELL | ALL_IN | 23.0 | 7 | 193 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030296536162495613 | 0.0 | 0.0 | +— / -bdee5671-864a-47c9-9576-9e0d8d2a7c6a |
| Jogador 3 | 6-2 | 345 | BUY | ALL_IN | 23.0 | 7 | 201 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06145133450627327 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 3 | 6-2 | 346 | SELL | ALL_IN | 23.0 | 7 | 199 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012500000186264515 | 0.0 | 0.0 | +— / -5de51369-647a-45bd-95b7-c8efe44c5484 |
| Jogador 3 | 6-2 | 347 | BUY | ALL_IN | 23.0 | 7 | 201 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036611855030059814 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -— |
| Jogador 3 | 6-2 | 348 | SELL | ALL_IN | 23.0 | 7 | 200 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01263333298265934 | 0.0 | 0.0 | +— / -0a0e7d41-96bf-404f-a3bf-98df0a182b63 |
| Jogador 3 | 6-2 | 349 | BUY | ALL_IN | 23.0 | 7 | 201 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26991790533065796 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -— |
| Jogador 3 | 6-2 | 350 | REROLL | ALL_IN | 23.0 | 7 | 200 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 352 | SELL | ALL_IN | 5.0 | 7 | 209 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019999999552965164 | 0.0 | 0.0 | +— / -1f349179-be2a-4738-bda1-072f7fae2147 |
| Jogador 3 | 6-3 | 353 | BUY | ALL_IN | 5.0 | 7 | 210 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5285213589668274 | 0.0 | 0.0 | +17279599-f3fc-4cf2-874f-da62a23ac238 / -— |
| Jogador 3 | 6-3 | 354 | SELL | ALL_IN | 5.0 | 7 | 207 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02983333356678486 | 0.0 | 0.0 | +— / -3365b4aa-125c-4f72-bcc5-01c5a205b9b0 |
| Jogador 3 | 6-3 | 355 | BUY | ALL_IN | 5.0 | 7 | 210 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22925367951393127 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 3 | 6-3 | 356 | SELL | ALL_IN | 5.0 | 7 | 206 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048020537942647934 | 0.0 | 0.0 | +— / -85d35881-ba70-4310-8d5f-bae796309eed |
| Jogador 3 | 6-3 | 357 | BUY | ALL_IN | 5.0 | 7 | 210 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08770526200532913 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 3 | 6-3 | 358 | SELL | ALL_IN | 5.0 | 7 | 207 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016390401870012283 | 0.0 | 0.0 | +— / -bfe7ca8a-6e89-4673-b142-262e012398a9 |
| Jogador 3 | 6-3 | 359 | BUY | ALL_IN | 5.0 | 7 | 210 | 5 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061455681920051575 | 0.0 | 0.0 | +b00644f3-3c3c-4ea2-a1fb-cc416e01e9e6 / -— |
| Jogador 3 | 6-3 | 360 | REROLL | ALL_IN | 5.0 | 7 | 208 | 5 | 30.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07000000029802322 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.20565874874591827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0004227982135489583 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2201479971408844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09193183481693268 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4628557562828064 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16226407885551453 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06005147472023964 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0128024816513062 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33920297026634216 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9802146553993225 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1839553564786911 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2163086235523224 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 58 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 59 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39172497391700745 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 64 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9556216597557068 | 0.0 | 0.0 | +8a006243-4508-4a6c-97ae-a0ce807cee54 / -— |
| Jogador 4 | 2-2 | 65 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 66 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9439022541046143 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 4 | 2-3 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.043451189994812 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-3 | 74 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30421218276023865 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 75 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_18_Camille | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5619999766349792 | 0.0 | 0.0 | +— / -095246b2-70a1-44ff-9f62-3752ad86693a |
| Jogador 4 | 2-3 | 76 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 77 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 8.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -34439867-85f7-4392-a985-337c6af81a1a |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10035542398691177 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 79 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5416666865348816 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 80 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1373712718486786 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23764429986476898 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15833333134651184 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-4 | 85 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005146525800228119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11433333158493042 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08100000023841858 | 0.0 | 0.0 | +— / -0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 2-4 | 89 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2500929534435272 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 4 | 2-4 | 90 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9550306797027588 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 4 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0011910200119019 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -86c535a4-a22b-4667-bc0f-46b4843d97cc,8aecef4c-747d-4f03-a858-85fe309988ab |
| Jogador 4 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.384468674659729 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 4 | 2-5 | 94 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2077520787715912 | 0.0 | 0.0 | +— / -4b07138d-44fd-4515-8b65-d7db84f4639c |
| Jogador 4 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21662946045398712 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3975072205066681 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5793939828872681 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013033942319452763 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 102 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32603171467781067 | 0.0 | 0.0 | +f71a7192-663d-46a0-93ef-b900c59c3bde / -— |
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
| Jogador 4 | 3-2 | 132 | BUY | STABILIZE | 73.0 | 6 | 8 | 0 | 18.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379985094070435 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 133 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 7 | 0 | 14.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2299346774816513 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 134 | BUY | STABILIZE | 73.0 | 6 | 7 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28799891471862793 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6034011244773865 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 136 | BUY | STABILIZE | 73.0 | 6 | 6 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11864210665225983 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 3 | 0 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04742184281349182 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 138 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 3 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 139 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 3 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.054462119936943054 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 140 | PASS | STABILIZE | 73.0 | 6 | 3 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 142 | BUY | STABILIZE | 62.0 | 6 | 9 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8347469568252563 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -8052731e-e34c-4de7-84b1-2b986cfeddaa,c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 4 | 3-3 | 143 | BUY | STABILIZE | 62.0 | 6 | 7 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7701987028121948 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 144 | BUY | STABILIZE | 62.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17683953046798706 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 145 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 3 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15690426528453827 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03811413422226906 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 147 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5030484199523926 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 148 | PASS | STABILIZE | 62.0 | 6 | 3 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 152 | BUY | STABILIZE | 52.0 | 6 | 10 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20561973750591278 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 153 | BUY | STABILIZE | 52.0 | 6 | 8 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28208017349243164 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 154 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 5 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36584150791168213 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 155 | BUY | STABILIZE | 52.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7380741834640503 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17853014171123505 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 157 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30157867074012756 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 4 | 0 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4041779935359955 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 159 | PASS | STABILIZE | 52.0 | 6 | 4 | 0 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 162 | SELL | STABILIZE | 52.0 | 6 | 11 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5799999833106995 | 0.0 | 0.0 | +— / -52018505-08c9-471f-83b9-fd5066efe55a |
| Jogador 4 | 3-5 | 163 | BUY | STABILIZE | 52.0 | 6 | 16 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8030096888542175 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 14 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08572697639465332 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 165 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 14 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4638077914714813 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 166 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 14 | 1 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3866232633590698 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 167 | PASS | STABILIZE | 52.0 | 6 | 14 | 1 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 172 | SELL | STABILIZE | 41.0 | 6 | 23 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 4 | 3-6 | 173 | BUY | STABILIZE | 41.0 | 6 | 26 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.850013256072998 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -7fd03119-ac82-49e1-b3bb-3a0caa31011f,fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 3-6 | 174 | BUY | STABILIZE | 41.0 | 6 | 24 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6010157465934753 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 175 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 21 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17843903601169586 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 176 | SELL | STABILIZE | 41.0 | 6 | 21 | 2 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -23f4d10f-2614-47b2-bfb2-4fb276764b5e |
| Jogador 4 | 3-6 | 177 | BUY | STABILIZE | 41.0 | 6 | 26 | 2 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09900225698947906 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 4 | 3-6 | 178 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 23 | 2 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3011972904205322 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 179 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 23 | 2 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4087209403514862 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 180 | PASS | STABILIZE | 41.0 | 6 | 23 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0621570385992527 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 182 | BUY | STABILIZE | 41.0 | 6 | 31 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7440882921218872 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 4 | 3-7 | 183 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 28 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07455876469612122 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 184 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 28 | 2 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44362470507621765 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 185 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 28 | 2 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38492611050605774 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 186 | PASS | STABILIZE | 41.0 | 6 | 28 | 2 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02698666602373123 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 41.0 | 6 | 35 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18133480846881866 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 41.0 | 6 | 35 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21501632034778595 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 194 | MOVE_BENCH | STABILIZE | 41.0 | 6 | 35 | 3 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32876989245414734 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 195 | SELL | STABILIZE | 41.0 | 6 | 35 | 3 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007851317524909973 | 0.0 | 0.0 | +— / -f722cd46-0c4e-42e7-80ff-4b910c28d572 |
| Jogador 4 | 4-1 | 196 | BUY | STABILIZE | 41.0 | 6 | 38 | 3 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3069785535335541 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 4 | 4-1 | 197 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 37 | 3 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03120526485145092 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 37 | 3 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 41.0 | 6 | 37 | 3 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 200 | PASS | STABILIZE | 41.0 | 6 | 37 | 3 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047114286571741104 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 202 | SELL | STABILIZE | 27.0 | 6 | 45 | 4 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5702270269393921 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 4 | 4-2 | 203 | BUY | STABILIZE | 27.0 | 6 | 46 | 4 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.319064199924469 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 4 | 4-2 | 204 | SELL | STABILIZE | 27.0 | 6 | 44 | 4 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1111999973654747 | 0.0 | 0.0 | +— / -fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 4 | 4-2 | 205 | BUY | STABILIZE | 27.0 | 6 | 46 | 4 | 20.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018630843609571457 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 4 | 4-2 | 206 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 43 | 4 | 20.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5079225301742554 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 207 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 43 | 4 | 24.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5728645920753479 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 208 | PASS | STABILIZE | 27.0 | 6 | 43 | 4 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07699999958276749 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 212 | SELL | ALL_IN | 16.0 | 6 | 53 | 5 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6991000175476074 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 4-3 | 213 | BUY | ALL_IN | 16.0 | 6 | 56 | 5 | 22.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5381826758384705 | 0.0 | 0.0 | +333b0a0b-8868-40b2-96e9-71e468c5dd1f / -— |
| Jogador 4 | 4-3 | 214 | EQUIP_FROM_INVENTORY | ALL_IN | 16.0 | 6 | 53 | 5 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15871483087539673 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 215 | EQUIP_FROM_INVENTORY | ALL_IN | 16.0 | 6 | 53 | 5 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15162456035614014 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 216 | EQUIP_FROM_INVENTORY | ALL_IN | 16.0 | 6 | 53 | 5 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12497087568044662 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 217 | MOVE_BENCH | ALL_IN | 16.0 | 6 | 53 | 5 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24508027732372284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 218 | MOVE_BENCH | ALL_IN | 16.0 | 6 | 53 | 5 | 22.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37536317110061646 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 219 | PASS | ALL_IN | 16.0 | 6 | 53 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45450007915496826 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 222 | MOVE_BENCH | ALL_IN | 2.0 | 7 | 64 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5563980937004089 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 223 | BUY | ALL_IN | 2.0 | 7 | 64 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42585518956184387 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 4 | 4-4 | 224 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 62 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2545369267463684 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 225 | SELL | ALL_IN | 2.0 | 7 | 62 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11779999732971191 | 0.0 | 0.0 | +— / -ad19ac66-9f86-4c29-8ae7-7222164aece1 |
| Jogador 4 | 4-4 | 226 | BUY | ALL_IN | 2.0 | 7 | 64 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11902373284101486 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 4 | 4-4 | 227 | REROLL | ALL_IN | 2.0 | 7 | 61 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 228 | SELL | ALL_IN | 2.0 | 7 | 59 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030266666784882545 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 4 | 4-4 | 229 | BUY | ALL_IN | 2.0 | 7 | 62 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07602832466363907 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 4 | 4-4 | 230 | MOVE_BENCH | ALL_IN | 2.0 | 7 | 58 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34572634100914 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 232 | SELL | ALL_IN | 2.0 | 7 | 69 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0229595098644495 | 0.0 | 0.0 | +— / -d1f19609-8b5f-489d-a2cf-d015fe7ed27e |
| Jogador 4 | 4-5 | 233 | BUY | ALL_IN | 2.0 | 7 | 73 | 5 | 32.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1023651361465454 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -409b32b9-5280-4d79-b5b2-871ed597ba56,9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 4-5 | 234 | MOVE_BENCH | ALL_IN | 2.0 | 7 | 70 | 5 | 26.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.580346941947937 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 235 | BUY | ALL_IN | 2.0 | 7 | 70 | 5 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21435965597629547 | 0.0 | 0.0 | +1ff42607-ccac-4d3f-8277-bccddf08862f / -— |
| Jogador 4 | 4-5 | 236 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0030400415416806936 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 237 | MOVE_BOARD | ALL_IN | 2.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030642833560705185 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 238 | PASS | ALL_IN | 2.0 | 7 | 67 | 5 | 28.0 | Florescer/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6380040645599365 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.26577791571617126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.24549612402915955 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12370830029249191 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11255644261837006 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17292346060276031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012102286331355572 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42841246724128723 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21666038036346436 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33030465245246887 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2888270318508148 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 44 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.032682180404663 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19873403012752533 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21273480355739594 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4088921844959259 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22606784105300903 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 60 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9719427227973938 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 5 | 2-2 | 65 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 66 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 72 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0441042184829712 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -341df1a1-a619-420a-926a-0fe048aa1456,634004e3-6a89-4cb3-929d-39ef6d3bce3c |
| Jogador 5 | 2-3 | 73 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12275191396474838 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 75 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24612858891487122 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43632957339286804 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 77 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16280943155288696 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03177344799041748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 79 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25767263770103455 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 80 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 82 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3106890916824341 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 83 | BUY | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21843014657497406 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 5 | 2-4 | 84 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05810000002384186 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-4 | 85 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08829675614833832 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-4 | 86 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16730917990207672 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 87 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07833333313465118 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-4 | 88 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09783884882926941 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 5 | 2-4 | 89 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 90 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 92 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2902473211288452 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 93 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33943894505500793 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 5 | 2-5 | 94 | SELL | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06970000267028809 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-5 | 95 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1223333328962326 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 2-5 | 96 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3170258402824402 | 0.0 | 0.0 | +28f66ef1-93d6-4cc8-a0c9-e84e844dee28 / -— |
| Jogador 5 | 2-5 | 97 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 98 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3515999913215637 | 0.0 | 0.0 | +— / -28f66ef1-93d6-4cc8-a0c9-e84e844dee28 |
| Jogador 5 | 2-5 | 99 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 0 | 0 | 14.0 | Espinhos Negros/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3971159756183624 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 102 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36481961607933044 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 5 | 2-6 | 103 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Espinhos Negros/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09186519682407379 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 104 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06104522570967674 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 105 | BUY | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05930067598819733 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 106 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08731768280267715 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 107 | SELL | STABILIZE | 95.0 | 6 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06522078812122345 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 108 | SELL | STABILIZE | 95.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43148890137672424 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-6 | 109 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005137316416949034 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 5 | 2-6 | 110 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0050762249156832695 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-7 | 112 | BUY | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34532737731933594 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 113 | BUY | STABILIZE | 90.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9630588889122009 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 114 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20998093485832214 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 5 | 2-7 | 115 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.034699998795986176 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 5 | 2-7 | 116 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03592974692583084 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 2-7 | 117 | BUY | STABILIZE | 90.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10740545392036438 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 118 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41966667771339417 | 0.0 | 0.0 | +— / -21abffda-a6c9-4987-8350-4f6d8f540441 |
| Jogador 5 | 2-7 | 119 | SELL | STABILIZE | 90.0 | 6 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37566667795181274 | 0.0 | 0.0 | +— / -6eee9a92-4235-46af-ae42-c38acd6847ef |
| Jogador 5 | 2-7 | 120 | BUY | STABILIZE | 90.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00808158703148365 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 5 | 3-1 | 122 | BUY | STABILIZE | 90.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7501031756401062 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -46838f8d-8037-485c-8c34-9639f14ada19,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.190902441740036 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 124 | BUY | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11416009068489075 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 125 | BUY | STABILIZE | 90.0 | 6 | 6 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028782688081264496 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 5 | 3-1 | 126 | SELL | STABILIZE | 90.0 | 6 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.625 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-1 | 127 | BUY | STABILIZE | 90.0 | 6 | 9 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2711927890777588 | 0.0 | 0.0 | +79ed9815-7667-4e50-86a3-420599ce8c79 / -— |
| Jogador 5 | 3-1 | 128 | SELL | STABILIZE | 90.0 | 6 | 7 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 5 | 3-1 | 129 | SELL | STABILIZE | 90.0 | 6 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2409999966621399 | 0.0 | 0.0 | +— / -79ed9815-7667-4e50-86a3-420599ce8c79 |
| Jogador 5 | 3-1 | 130 | BUY | STABILIZE | 90.0 | 6 | 10 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35375088453292847 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 5 | 3-2 | 132 | BUY | STABILIZE | 90.0 | 6 | 16 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6885117888450623 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 133 | BUY | STABILIZE | 90.0 | 6 | 13 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27089130878448486 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 134 | SELL | STABILIZE | 90.0 | 6 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023000000044703484 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 5 | 3-2 | 135 | SELL | STABILIZE | 90.0 | 6 | 12 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09637503325939178 | 0.0 | 0.0 | +— / -a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 |
| Jogador 5 | 3-2 | 136 | SELL | STABILIZE | 90.0 | 6 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5380130410194397 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 5 | 3-2 | 137 | BUY | STABILIZE | 90.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23666338622570038 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 138 | SELL | STABILIZE | 90.0 | 6 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3356666564941406 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-2 | 139 | BUY | STABILIZE | 90.0 | 6 | 17 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27131813764572144 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 5 | 3-2 | 140 | SELL | STABILIZE | 90.0 | 6 | 15 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32100000977516174 | 0.0 | 0.0 | +— / -d218597b-b641-4a4c-867a-41227b83fcff |
| Jogador 5 | 3-3 | 142 | BUY | STABILIZE | 90.0 | 6 | 25 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8105481266975403 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 143 | BUY | STABILIZE | 90.0 | 6 | 23 | 2 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2107120305299759 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 144 | BUY | STABILIZE | 90.0 | 6 | 19 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2809866666793823 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 145 | SELL | STABILIZE | 90.0 | 6 | 16 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09771686047315598 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-3 | 146 | SELL | STABILIZE | 90.0 | 6 | 19 | 1 | 16.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09300000220537186 | 0.0 | 0.0 | +— / -8a4d0946-b80f-4fbb-ab7c-d43c2697c34e |
| Jogador 5 | 3-3 | 147 | BUY | STABILIZE | 90.0 | 6 | 23 | 2 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04345705360174179 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 148 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 20 | 2 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014042627066373825 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 149 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 20 | 2 | 14.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40409326553344727 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 150 | PASS | STABILIZE | 90.0 | 6 | 20 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05849999934434891 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 152 | BUY | STABILIZE | 78.0 | 6 | 27 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8257275819778442 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 5 | 3-4 | 153 | BUY | STABILIZE | 78.0 | 6 | 26 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5212894082069397 | 0.0 | 0.0 | +ee087d59-c995-4032-b4d9-27220b469d71 / -— |
| Jogador 5 | 3-4 | 154 | SELL | STABILIZE | 78.0 | 6 | 25 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05374174192547798 | 0.0 | 0.0 | +— / -a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 3-4 | 155 | BUY | STABILIZE | 78.0 | 6 | 28 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05291061848402023 | 0.0 | 0.0 | +2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f / -— |
| Jogador 5 | 3-4 | 156 | SELL | STABILIZE | 78.0 | 6 | 26 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37111878395080566 | 0.0 | 0.0 | +— / -2a0cf69a-4791-44ac-ad8c-7f7bcf9a9b3f |
| Jogador 5 | 3-4 | 157 | BUY | STABILIZE | 78.0 | 6 | 28 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2549080550670624 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 5 | 3-4 | 158 | SELL | STABILIZE | 78.0 | 6 | 26 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34152576327323914 | 0.0 | 0.0 | +— / -46fc5f36-cf3e-422e-89f3-9501ec9d7d12 |
| Jogador 5 | 3-4 | 159 | SELL | STABILIZE | 78.0 | 6 | 28 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49013274908065796 | 0.0 | 0.0 | +— / -ee087d59-c995-4032-b4d9-27220b469d71 |
| Jogador 5 | 3-4 | 160 | SELL | STABILIZE | 78.0 | 6 | 29 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49442222714424133 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 5 | 3-5 | 162 | BUY | STABILIZE | 78.0 | 6 | 39 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8511416912078857 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -02c39b42-90d5-4e01-9380-460b6c1cb993,eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 3-5 | 163 | BUY | STABILIZE | 78.0 | 6 | 38 | 3 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11700698733329773 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 5 | 3-5 | 164 | MOVE_BENCH | STABILIZE | 78.0 | 6 | 35 | 3 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4744119644165039 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 165 | BUY | STABILIZE | 78.0 | 6 | 35 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02935066819190979 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 166 | BUY | STABILIZE | 78.0 | 6 | 32 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18753398954868317 | 0.0 | 0.0 | +6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 / -— |
| Jogador 5 | 3-5 | 167 | BUY | STABILIZE | 78.0 | 6 | 31 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3546450138092041 | 0.0 | 0.0 | +c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 / -— |
| Jogador 5 | 3-5 | 168 | SELL | STABILIZE | 78.0 | 6 | 29 | 2 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5384865999221802 | 0.0 | 0.0 | +— / -ba3c4e40-b686-40b3-bc40-004a8667f853 |
| Jogador 5 | 3-5 | 169 | SELL | STABILIZE | 78.0 | 6 | 32 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3596666753292084 | 0.0 | 0.0 | +— / -6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 |
| Jogador 5 | 3-5 | 170 | SELL | STABILIZE | 78.0 | 6 | 33 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32100000977516174 | 0.0 | 0.0 | +— / -c3a766c4-2db6-4b3f-88e9-a855fef1e6f6 |
| Jogador 5 | 3-6 | 172 | BUY | STABILIZE | 67.0 | 6 | 44 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08890439569950104 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 173 | BUY | STABILIZE | 67.0 | 6 | 43 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019693637266755104 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 174 | BUY | STABILIZE | 67.0 | 6 | 41 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3546883761882782 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 175 | BUY | STABILIZE | 67.0 | 6 | 39 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2365594208240509 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 176 | SELL | STABILIZE | 67.0 | 6 | 38 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011166666634380817 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 3-6 | 177 | SELL | STABILIZE | 67.0 | 6 | 39 | 3 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31299999356269836 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 5 | 3-6 | 178 | SELL | STABILIZE | 67.0 | 6 | 40 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32100000977516174 | 0.0 | 0.0 | +— / -1457cd1e-c240-4ce5-9217-a91bddfc8807 |
| Jogador 5 | 3-6 | 179 | SELL | STABILIZE | 67.0 | 6 | 42 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.371158242225647 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-6 | 180 | SELL | STABILIZE | 67.0 | 6 | 44 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.052173446863889694 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 3-7 | 182 | BUY | STABILIZE | 55.0 | 6 | 57 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3831670582294464 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 5 | 3-7 | 183 | BUY | STABILIZE | 55.0 | 6 | 55 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03373470529913902 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 184 | BUY | STABILIZE | 55.0 | 6 | 52 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2929551601409912 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 5 | 3-7 | 185 | BUY | STABILIZE | 55.0 | 6 | 49 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041549984365701675 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 186 | SELL | STABILIZE | 55.0 | 6 | 47 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3490000069141388 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 3-7 | 187 | BUY | STABILIZE | 55.0 | 6 | 49 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2768740653991699 | 0.0 | 0.0 | +9b509d0e-ae62-4bfa-a551-f46ea68c64f4 / -— |
| Jogador 5 | 3-7 | 188 | SELL | STABILIZE | 55.0 | 6 | 48 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3230000138282776 | 0.0 | 0.0 | +— / -9b509d0e-ae62-4bfa-a551-f46ea68c64f4 |
| Jogador 5 | 3-7 | 189 | REROLL | STABILIZE | 55.0 | 6 | 49 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20399999618530273 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 190 | BUY | STABILIZE | 55.0 | 6 | 47 | 4 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8298068046569824 | 0.0 | 0.0 | +e7c8751e-5d30-4953-9508-35488b6c45db / -— |
| Jogador 5 | 4-1 | 192 | BUY | STABILIZE | 55.0 | 6 | 55 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2127760946750641 | 0.0 | 0.0 | +45d53a67-4ed4-495d-8751-5ea0f72f91e9 / -— |
| Jogador 5 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 55.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1695060133934021 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 194 | CRAFT_AND_EQUIP | STABILIZE | 55.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19597120583057404 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 195 | SELL | STABILIZE | 55.0 | 6 | 51 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 4-1 | 196 | BUY | STABILIZE | 55.0 | 6 | 54 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1237071081995964 | 0.0 | 0.0 | +3d7ba32f-3349-479e-bb6f-9cd1f2006149 / -— |
| Jogador 5 | 4-1 | 197 | SELL | STABILIZE | 55.0 | 6 | 53 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03325121849775314 | 0.0 | 0.0 | +— / -3d7ba32f-3349-479e-bb6f-9cd1f2006149 |
| Jogador 5 | 4-1 | 198 | BUY | STABILIZE | 55.0 | 6 | 54 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23506700992584229 | 0.0 | 0.0 | +78525c90-c4d2-425d-ba90-a03664c60a28 / -— |
| Jogador 5 | 4-1 | 199 | SELL | STABILIZE | 55.0 | 6 | 52 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -78525c90-c4d2-425d-ba90-a03664c60a28 |
| Jogador 5 | 4-1 | 200 | BUY | STABILIZE | 55.0 | 6 | 54 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2350662648677826 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 5 | 4-2 | 202 | SELL | STABILIZE | 44.0 | 6 | 63 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -a8a8381a-f3a8-45ec-9106-293d73fca0c8 |
| Jogador 5 | 4-2 | 203 | BUY | STABILIZE | 44.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.894365131855011 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 5 | 4-2 | 204 | SELL | STABILIZE | 44.0 | 6 | 62 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 |
| Jogador 5 | 4-2 | 205 | BUY | STABILIZE | 44.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05361908674240112 | 0.0 | 0.0 | +6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb / -— |
| Jogador 5 | 4-2 | 206 | SELL | STABILIZE | 44.0 | 6 | 62 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -6f887b0c-3b11-42cb-8a9f-187b0ecd7dfb |
| Jogador 5 | 4-2 | 207 | BUY | STABILIZE | 44.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12384891510009766 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 5 | 4-2 | 208 | SELL | STABILIZE | 44.0 | 6 | 64 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03328762575984001 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 5 | 4-2 | 209 | BUY | STABILIZE | 44.0 | 6 | 65 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09225486218929291 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -— |
| Jogador 5 | 4-2 | 210 | MOVE_BOARD | STABILIZE | 44.0 | 6 | 64 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14460216462612152 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 212 | SELL | STABILIZE | 34.0 | 6 | 76 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026799999177455902 | 0.0 | 0.0 | +— / -93f7279f-b03b-407b-b623-c0a2bd88f877 |
| Jogador 5 | 4-3 | 213 | BUY | STABILIZE | 34.0 | 6 | 77 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12277501821517944 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 5 | 4-3 | 214 | SELL | STABILIZE | 34.0 | 6 | 76 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03323376923799515 | 0.0 | 0.0 | +— / -840740a6-45be-4107-a4b7-b10cefe1a667 |
| Jogador 5 | 4-3 | 215 | BUY | STABILIZE | 34.0 | 6 | 77 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02632240019738674 | 0.0 | 0.0 | +651884f1-8453-44cb-ac46-780eb9f7ac86 / -— |
| Jogador 5 | 4-3 | 216 | SELL | STABILIZE | 34.0 | 6 | 75 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015042885206639767 | 0.0 | 0.0 | +— / -651884f1-8453-44cb-ac46-780eb9f7ac86 |
| Jogador 5 | 4-3 | 217 | BUY | STABILIZE | 34.0 | 6 | 77 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23592613637447357 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 5 | 4-3 | 218 | SELL | STABILIZE | 34.0 | 6 | 75 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 5 | 4-3 | 219 | BUY | STABILIZE | 34.0 | 6 | 77 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26860544085502625 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 5 | 4-3 | 220 | SELL | STABILIZE | 34.0 | 6 | 75 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 |
| Jogador 5 | 4-4 | 222 | BUY | ALL_IN | 22.0 | 6 | 90 | 5 | 18.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0142651796340942 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -2e4ab22c-62d7-425c-9528-2e1315655c24,6084e8d8-82f2-47e3-b8e1-4077ad70efe5 |
| Jogador 5 | 4-4 | 223 | BUY | ALL_IN | 22.0 | 6 | 89 | 5 | 16.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29344213008880615 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 5 | 4-4 | 224 | MOVE_BENCH | ALL_IN | 22.0 | 6 | 87 | 5 | 16.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5662453174591064 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 225 | BUY | ALL_IN | 22.0 | 6 | 87 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04627562686800957 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 5 | 4-4 | 226 | SELL | ALL_IN | 22.0 | 6 | 86 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6822999715805054 | 0.0 | 0.0 | +— / -e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 |
| Jogador 5 | 4-4 | 227 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 6 | 89 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09364298731088638 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 228 | BUY | ALL_IN | 22.0 | 6 | 89 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.7548043727874756 | 0.0 | 0.0 | +5b6dec85-6970-4575-b364-21c3123995a5 / -— |
| Jogador 5 | 4-4 | 229 | EQUIP_FROM_INVENTORY | ALL_IN | 22.0 | 6 | 88 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09332827478647232 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 230 | MOVE_BOARD | ALL_IN | 22.0 | 6 | 88 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029620012268424034 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 232 | SELL | ALL_IN | 22.0 | 6 | 101 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060246389359235764 | 0.0 | 0.0 | +— / -45d53a67-4ed4-495d-8751-5ea0f72f91e9 |
| Jogador 5 | 4-5 | 233 | BUY | ALL_IN | 22.0 | 6 | 105 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8627127408981323 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 5 | 4-5 | 234 | SELL | ALL_IN | 22.0 | 6 | 102 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4814888834953308 | 0.0 | 0.0 | +— / -15c93ffb-d63e-43e6-aa46-ba2beed9cb53 |
| Jogador 5 | 4-5 | 235 | BUY | ALL_IN | 22.0 | 6 | 104 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3972090482711792 | 0.0 | 0.0 | +f99cdd31-4a55-4a5e-941a-2800b8afdd7a / -— |
| Jogador 5 | 4-5 | 236 | SELL | ALL_IN | 22.0 | 6 | 101 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1377333402633667 | 0.0 | 0.0 | +— / -f99cdd31-4a55-4a5e-941a-2800b8afdd7a |
| Jogador 5 | 4-5 | 237 | BUY | ALL_IN | 22.0 | 6 | 104 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1779838502407074 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 5 | 4-5 | 238 | REROLL | ALL_IN | 22.0 | 6 | 103 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 239 | SELL | ALL_IN | 22.0 | 6 | 101 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005133333150297403 | 0.0 | 0.0 | +— / -d6a00f0c-4823-44d6-b326-67595876998d |
| Jogador 5 | 4-5 | 240 | BUY | ALL_IN | 22.0 | 6 | 102 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21597640216350555 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 5 | 4-6 | 242 | SELL | ALL_IN | 9.0 | 6 | 111 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 5 | 4-6 | 243 | BUY | ALL_IN | 9.0 | 6 | 115 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0590457916259766 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -4af85188-f11e-4aca-8165-ba8e7f535670,bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 5 | 4-6 | 244 | BUY | ALL_IN | 9.0 | 6 | 112 | 5 | 22.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.051447443664073944 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -— |
| Jogador 5 | 4-6 | 245 | BUY | ALL_IN | 9.0 | 6 | 110 | 5 | 22.0 | Enfeitiçador/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14120322465896606 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 5 | 4-6 | 246 | SELL | ALL_IN | 9.0 | 6 | 107 | 5 | 22.0 | Enfeitiçador/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7191413044929504 | 0.0 | 0.0 | +— / -5c931416-3aeb-40d4-9e6f-612b0d387226 |
| Jogador 5 | 4-6 | 247 | BUY | ALL_IN | 9.0 | 6 | 115 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2311924695968628 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 5 | 4-6 | 248 | REROLL | ALL_IN | 9.0 | 6 | 113 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 249 | SELL | ALL_IN | 9.0 | 6 | 111 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005008143372833729 | 0.0 | 0.0 | +— / -db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 5 | 4-6 | 250 | BUY | ALL_IN | 9.0 | 6 | 113 | 5 | 22.0 | Enfeitiçador/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7572331428527832 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -— |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.24211829900741577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | -0.15334774553775787 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Sentry | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17399217188358307 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21841175854206085 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0372568368911743 | 0.0 | 0.0 | +3cb4d077-df9a-4fd2-9a68-7301aff1b657 / -— |
| Jogador 6 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039901405572891235 | 0.0 | 0.0 | +6a01f661-884f-4c25-9dbe-384a6fe3a5e6 / -— |
| Jogador 6 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012773334980010986 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011599136516451836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5750508904457092 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0249452590942383 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 43 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 55 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12839862704277039 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15210670232772827 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 57 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2897646129131317 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 58 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 59 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09100788831710815 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 64 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26298633217811584 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 65 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24710547924041748 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 6 | 2-2 | 66 | SELL | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -6a01f661-884f-4c25-9dbe-384a6fe3a5e6 |
| Jogador 6 | 2-2 | 67 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07944674044847488 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 68 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28886672854423523 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 6 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18029023706912994 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23834408819675446 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 75 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14500433206558228 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-3 | 76 | SELL | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15171855688095093 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 6 | 2-3 | 77 | PASS | STABILIZE | 89.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 82 | BUY | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.182968869805336 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 83 | BUY | STABILIZE | 83.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24054092168807983 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 84 | BUY | STABILIZE | 83.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8068609833717346 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 85 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 86 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013266666792333126 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-4 | 87 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10959629714488983 | 0.0 | 0.0 | +— / -048e9074-b134-49ed-a105-88dca63d1aa3 |
| Jogador 6 | 2-4 | 88 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 89 | SELL | STABILIZE | 83.0 | 5 | 0 | 0 | 8.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1438080221414566 | 0.0 | 0.0 | +— / -8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 |
| Jogador 6 | 2-4 | 90 | SELL | STABILIZE | 83.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14380386471748352 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 92 | BUY | STABILIZE | 83.0 | 5 | 10 | 1 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596822023391724 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 93 | SELL | STABILIZE | 83.0 | 5 | 9 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4177216589450836 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 2-5 | 94 | BUY_XP | STABILIZE | 83.0 | 5 | 12 | 1 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14300000667572021 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 95 | BUY_XP | STABILIZE | 83.0 | 5 | 8 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 96 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 8.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015375000424683094 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 97 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 0 | 0 | 8.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2040332406759262 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 98 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-5 | 99 | BUY | STABILIZE | 83.0 | 6 | 3 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34659820795059204 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 6 | 2-5 | 100 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.476666659116745 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 6 | 2-6 | 102 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3036162555217743 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 103 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32059720158576965 | 0.0 | 0.0 | +f5511428-5be8-475d-949c-1d840a0aed4d / -— |
| Jogador 6 | 2-6 | 104 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 105 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1613156497478485 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 106 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 107 | SELL | STABILIZE | 76.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.476666659116745 | 0.0 | 0.0 | +— / -f5511428-5be8-475d-949c-1d840a0aed4d |
| Jogador 6 | 2-6 | 108 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 6 | 2-6 | 109 | BUY | STABILIZE | 76.0 | 6 | 2 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3284234404563904 | 0.0 | 0.0 | +53bbd605-d60b-4555-b5e8-29f1cfbb83b4 / -— |
| Jogador 6 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 0 | 0 | 10.0 | Feérico/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006841098889708519 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 112 | BUY | STABILIZE | 72.0 | 6 | 7 | 0 | 10.0 | Feérico/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.304421991109848 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 113 | BUY | STABILIZE | 72.0 | 6 | 4 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18440033495426178 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 6 | 2-7 | 114 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 1 | 0 | 10.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3769831955432892 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 115 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 116 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024863226339221 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 117 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06015022471547127 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 118 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 119 | PASS | STABILIZE | 72.0 | 6 | 1 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 122 | BUY | STABILIZE | 72.0 | 6 | 8 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13859842717647552 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2202974408864975 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 124 | BUY | STABILIZE | 72.0 | 6 | 5 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1140725314617157 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 3 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39829960465431213 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 126 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 3 | 0 | 20.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 127 | PASS | STABILIZE | 72.0 | 6 | 3 | 0 | 20.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 132 | BUY | STABILIZE | 72.0 | 6 | 9 | 0 | 20.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8375436067581177 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -3ad41699-a484-4178-be10-d8f72dfd1f35,698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 3-2 | 133 | BUY | STABILIZE | 72.0 | 6 | 8 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8376479744911194 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -18934be2-4988-4f62-9f62-07ba151231f2,53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 7 | 0 | 16.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07265111804008484 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 7 | 0 | 12.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1977730393409729 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 136 | BUY_XP | STABILIZE | 72.0 | 6 | 7 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 137 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05951891839504242 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 138 | SELL | STABILIZE | 72.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-2 | 139 | EQUIP_FROM_INVENTORY | STABILIZE | 72.0 | 6 | 6 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15578892827033997 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 140 | EQUIP_FROM_INVENTORY | STABILIZE | 72.0 | 6 | 6 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18792887032032013 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 142 | BUY | STABILIZE | 63.0 | 6 | 11 | 1 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.20149825513362885 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 143 | EQUIP_FROM_INVENTORY | STABILIZE | 63.0 | 6 | 8 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14461596310138702 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 144 | BUY_XP | STABILIZE | 63.0 | 6 | 8 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 145 | BUY_XP | STABILIZE | 63.0 | 6 | 4 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 146 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 2.7755575615628914e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 147 | MOVE_BOARD | STABILIZE | 63.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05298897251486778 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 148 | SELL | STABILIZE | 63.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-3 | 149 | BUY | STABILIZE | 63.0 | 6 | 3 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06289397180080414 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 150 | PASS | STABILIZE | 63.0 | 6 | 0 | 0 | 18.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 152 | BUY | STABILIZE | 54.0 | 6 | 6 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7587546706199646 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 153 | BUY | STABILIZE | 54.0 | 6 | 3 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47269800305366516 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 154 | SELL | STABILIZE | 54.0 | 6 | 0 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ab127012-83d7-46f0-a16c-b20582d1179b |
| Jogador 6 | 3-4 | 155 | BUY | STABILIZE | 54.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2555975317955017 | 0.0 | 0.0 | +4698e3b3-0833-4895-a1f1-26b372b2f965 / -— |
| Jogador 6 | 3-4 | 156 | SELL | STABILIZE | 54.0 | 6 | 0 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -4698e3b3-0833-4895-a1f1-26b372b2f965 |
| Jogador 6 | 3-4 | 157 | SELL | STABILIZE | 54.0 | 6 | 2 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03936666622757912 | 0.0 | 0.0 | +— / -50f9a30c-27db-4ed0-804e-548f87950b17 |
| Jogador 6 | 3-4 | 158 | BUY_XP | STABILIZE | 54.0 | 6 | 5 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0609700009226799 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 159 | MOVE_BENCH | STABILIZE | 54.0 | 7 | 1 | 0 | 22.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40354666113853455 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014134891331195831 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 162 | BUY | STABILIZE | 54.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011323600076138973 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 163 | BUY | STABILIZE | 54.0 | 7 | 4 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010032772086560726 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 164 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057230331003665924 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 167 | PASS | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 172 | BUY | STABILIZE | 54.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07056333124637604 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 173 | BUY | STABILIZE | 54.0 | 7 | 4 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20360787212848663 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 174 | BUY | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26476797461509705 | 0.0 | 0.0 | +171724e7-58bd-404f-820b-2bb32c5c193e / -— |
| Jogador 6 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03738636523485184 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 176 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 177 | PASS | STABILIZE | 54.0 | 7 | 0 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 182 | BUY | STABILIZE | 54.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0869690477848053 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 183 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 2 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06402624398469925 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 184 | SELL | STABILIZE | 54.0 | 7 | 2 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -9.999999747378752e-05 | 0.0 | 0.0 | +— / -171724e7-58bd-404f-820b-2bb32c5c193e |
| Jogador 6 | 3-7 | 185 | BUY | STABILIZE | 54.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01989336870610714 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -— |
| Jogador 6 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 187 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 188 | PASS | STABILIZE | 54.0 | 7 | 1 | 0 | 28.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13425804674625397 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 54.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1318664252758026 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 194 | SELL | STABILIZE | 54.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021933333948254585 | 0.0 | 0.0 | +— / -89cec488-9a0e-4838-b486-2504a0742476 |
| Jogador 6 | 4-1 | 195 | BUY | STABILIZE | 54.0 | 7 | 9 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4498595595359802 | 0.0 | 0.0 | +ddf39480-6ce0-46d0-ac45-57114245ffba / -— |
| Jogador 6 | 4-1 | 196 | SELL | STABILIZE | 54.0 | 7 | 6 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002166666556149721 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-1 | 197 | BUY | STABILIZE | 54.0 | 7 | 9 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24046379327774048 | 0.0 | 0.0 | +6a30a366-c631-429d-9523-af769cdf48a4 / -— |
| Jogador 6 | 4-1 | 198 | BUY_XP | STABILIZE | 54.0 | 7 | 8 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 199 | BUY_XP | STABILIZE | 54.0 | 7 | 4 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 200 | MOVE_BOARD | STABILIZE | 54.0 | 7 | 0 | 0 | 28.0 | Feérico/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04503994435071945 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 202 | SELL | STABILIZE | 42.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007366666570305824 | 0.0 | 0.0 | +— / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 |
| Jogador 6 | 4-2 | 203 | BUY | STABILIZE | 42.0 | 7 | 8 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.759988009929657 | 0.0 | 0.0 | +7920bf77-c0ba-4906-a82d-6c18bc42f4d9 / -— |
| Jogador 6 | 4-2 | 204 | SELL | STABILIZE | 42.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02383333258330822 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 4-2 | 205 | BUY | STABILIZE | 42.0 | 7 | 8 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7452225089073181 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -06db3a99-d008-406a-ac86-30884335d7c2,ddf39480-6ce0-46d0-ac45-57114245ffba |
| Jogador 6 | 4-2 | 206 | BUY | STABILIZE | 42.0 | 7 | 5 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1508733332157135 | 0.0 | 0.0 | +00f38555-1887-4fe2-9930-934055269095 / -— |
| Jogador 6 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 209 | PASS | STABILIZE | 42.0 | 7 | 3 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 212 | BUY | STABILIZE | 42.0 | 7 | 9 | 0 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7855976223945618 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 6 | 4-3 | 213 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 214 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1293494552373886 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 215 | SELL | STABILIZE | 42.0 | 7 | 7 | 0 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02630000002682209 | 0.0 | 0.0 | +— / -f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 6 | 4-3 | 216 | BUY | STABILIZE | 42.0 | 7 | 15 | 1 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0051840925589203835 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 6 | 4-3 | 217 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 11 | 1 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 218 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 11 | 1 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 219 | PASS | STABILIZE | 42.0 | 7 | 11 | 1 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 222 | SELL | STABILIZE | 42.0 | 7 | 19 | 1 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036400001496076584 | 0.0 | 0.0 | +— / -00f38555-1887-4fe2-9930-934055269095 |
| Jogador 6 | 4-4 | 223 | BUY | STABILIZE | 42.0 | 7 | 21 | 2 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31175878643989563 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -— |
| Jogador 6 | 4-4 | 224 | SELL | STABILIZE | 42.0 | 7 | 20 | 2 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024477297440171242 | 0.0 | 0.0 | +— / -c7841e00-91da-410b-b00f-62f4bf32f666 |
| Jogador 6 | 4-4 | 225 | BUY | STABILIZE | 42.0 | 7 | 24 | 2 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.726860761642456 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -2ed895f2-1e83-426c-88fc-b9fb6403835d,9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 6 | 4-4 | 226 | BUY | STABILIZE | 42.0 | 7 | 21 | 2 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3293730914592743 | 0.0 | 0.0 | +1f7f2a48-1318-4fc6-87cc-03d557bf69ea / -— |
| Jogador 6 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 18 | 1 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 18 | 1 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 229 | PASS | STABILIZE | 42.0 | 7 | 18 | 1 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02856507897377014 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 232 | BUY | STABILIZE | 42.0 | 7 | 25 | 2 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05976177379488945 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 6 | 4-5 | 233 | SELL | STABILIZE | 42.0 | 7 | 24 | 2 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025086279958486557 | 0.0 | 0.0 | +— / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 |
| Jogador 6 | 4-5 | 234 | BUY | STABILIZE | 42.0 | 7 | 32 | 3 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02049347385764122 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -— |
| Jogador 6 | 4-5 | 235 | SELL | STABILIZE | 42.0 | 7 | 30 | 3 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030817069113254547 | 0.0 | 0.0 | +— / -262702a6-b710-4129-9dc6-0c1a04514ff9 |
| Jogador 6 | 4-5 | 236 | BUY | STABILIZE | 42.0 | 7 | 31 | 3 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14795535802841187 | 0.0 | 0.0 | +84981e98-bfb7-4c49-a020-51cf6d864881 / -— |
| Jogador 6 | 4-5 | 237 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 28 | 2 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004683318082243204 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 238 | SELL | STABILIZE | 42.0 | 7 | 28 | 2 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0715973973274231 | 0.0 | 0.0 | +— / -ac547bcb-d285-480d-b50e-3cfba572db5a |
| Jogador 6 | 4-5 | 239 | BUY | STABILIZE | 42.0 | 7 | 30 | 3 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1065499559044838 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 6 | 4-5 | 240 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 28 | 2 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 242 | SELL | STABILIZE | 42.0 | 7 | 37 | 3 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -715d5bfc-c8c3-4dec-a247-9e07ee2755e8 |
| Jogador 6 | 4-6 | 243 | BUY | STABILIZE | 42.0 | 7 | 39 | 3 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3137107193470001 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -— |
| Jogador 6 | 4-6 | 244 | SELL | STABILIZE | 42.0 | 7 | 35 | 3 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009100000374019146 | 0.0 | 0.0 | +— / -1f7f2a48-1318-4fc6-87cc-03d557bf69ea |
| Jogador 6 | 4-6 | 245 | BUY | STABILIZE | 42.0 | 7 | 38 | 3 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23978480696678162 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 6 | 4-6 | 246 | SELL | STABILIZE | 42.0 | 7 | 37 | 3 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08563333004713058 | 0.0 | 0.0 | +— / -84981e98-bfb7-4c49-a020-51cf6d864881 |
| Jogador 6 | 4-6 | 247 | BUY | STABILIZE | 42.0 | 7 | 40 | 4 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09816382825374603 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 6 | 4-6 | 248 | SELL | STABILIZE | 42.0 | 7 | 37 | 3 | 28.0 | Feérico/DA_18_GnarSmall | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07263333350419998 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 6 | 4-6 | 249 | SELL | STABILIZE | 42.0 | 7 | 40 | 4 | 28.0 | Feérico/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12099999934434891 | 0.0 | 0.0 | +— / -891aea62-e06a-46d4-8250-a3d4a56e847d |
| Jogador 6 | 4-6 | 250 | SELL | STABILIZE | 42.0 | 7 | 45 | 4 | 28.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17299999296665192 | 0.0 | 0.0 | +— / -4aa5d560-d9d3-45f9-802a-bdbe95788762 |
| Jogador 6 | 4-7 | 252 | BUY | STABILIZE | 42.0 | 7 | 61 | 5 | 28.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.947168231010437 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 6 | 4-7 | 253 | BUY | STABILIZE | 42.0 | 7 | 58 | 5 | 28.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.943839430809021 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -7920bf77-c0ba-4906-a82d-6c18bc42f4d9,7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 4-7 | 254 | BUY | STABILIZE | 42.0 | 7 | 55 | 5 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023702463135123253 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 6 | 4-7 | 255 | SELL | STABILIZE | 42.0 | 7 | 52 | 5 | 22.0 | Feérico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6270429491996765 | 0.0 | 0.0 | +— / -24b29fe6-466c-42d5-9f92-5d6114f0f98f |
| Jogador 6 | 4-7 | 256 | SELL | STABILIZE | 42.0 | 7 | 60 | 5 | 22.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07699999958276749 | 0.0 | 0.0 | +— / -de8de4b5-48ea-4947-ae08-2b90d94b0fc1 |
| Jogador 6 | 4-7 | 257 | SELL | STABILIZE | 42.0 | 7 | 63 | 5 | 22.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3549000024795532 | 0.0 | 0.0 | +— / -b0c1aba5-b1bd-48df-abec-19efa8e49d6d |
| Jogador 6 | 4-7 | 258 | BUY | STABILIZE | 42.0 | 7 | 64 | 5 | 22.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04072103649377823 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -— |
| Jogador 6 | 4-7 | 259 | MOVE_BENCH | STABILIZE | 42.0 | 7 | 62 | 5 | 22.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42093560099601746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 260 | MOVE_BOARD | STABILIZE | 42.0 | 7 | 62 | 5 | 28.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 262 | BUY | STABILIZE | 42.0 | 7 | 73 | 5 | 28.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1085014343261719 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 5-1 | 263 | BUY | STABILIZE | 42.0 | 7 | 70 | 5 | 22.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0971726179122925 | 0.0 | 0.0 | +58cbdbde-2151-438c-8897-902bef9bcd92 / -53bbd605-d60b-4555-b5e8-29f1cfbb83b4,80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 6 | 5-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 42.0 | 7 | 68 | 5 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12935870885849 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 265 | CRAFT_AND_EQUIP | STABILIZE | 42.0 | 7 | 68 | 5 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13648603856563568 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 266 | MOVE_BENCH | STABILIZE | 42.0 | 7 | 68 | 5 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3590344786643982 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 267 | MOVE_BENCH | STABILIZE | 42.0 | 7 | 68 | 5 | 18.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2681984305381775 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 268 | BUY | STABILIZE | 42.0 | 7 | 68 | 5 | 20.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056892119348049164 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 6 | 5-1 | 269 | MOVE_BENCH | STABILIZE | 42.0 | 7 | 64 | 5 | 20.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39683830738067627 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 270 | BUY | STABILIZE | 42.0 | 7 | 64 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24557311832904816 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 6 | 5-2 | 272 | BUY | STABILIZE | 27.0 | 7 | 71 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05755912885069847 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -— |
| Jogador 6 | 5-2 | 273 | BUY | STABILIZE | 27.0 | 7 | 68 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05388851836323738 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -— |
| Jogador 6 | 5-2 | 274 | BUY | STABILIZE | 27.0 | 7 | 67 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023248402401804924 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 6 | 5-2 | 275 | SELL | STABILIZE | 27.0 | 7 | 65 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5964999794960022 | 0.0 | 0.0 | +— / -58cbdbde-2151-438c-8897-902bef9bcd92 |
| Jogador 6 | 5-2 | 276 | BUY | STABILIZE | 27.0 | 7 | 70 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06766277551651001 | 0.0 | 0.0 | +5821f43b-b898-4842-b309-d175f2284a84 / -— |
| Jogador 6 | 5-2 | 277 | MOVE_BOARD | STABILIZE | 27.0 | 7 | 68 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 278 | REROLL | STABILIZE | 27.0 | 7 | 68 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573999971151352 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 279 | SELL | STABILIZE | 27.0 | 7 | 66 | 5 | 26.0 | Feérico/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5780666470527649 | 0.0 | 0.0 | +— / -b0c8ce74-5ce1-4ed0-82ac-f95013475f3c |
| Jogador 6 | 5-2 | 280 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 74 | 5 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.3735387623310089 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 282 | BUY | ALL_IN | 9.0 | 7 | 85 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.574916660785675 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 6 | 5-3 | 283 | BUY | ALL_IN | 9.0 | 7 | 83 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.14082030951976776 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 6 | 5-3 | 284 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 7 | 79 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12066523730754852 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 285 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 7 | 79 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1678723692893982 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 286 | SELL | ALL_IN | 9.0 | 7 | 79 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030225703492760658 | 0.0 | 0.0 | +— / -6594349f-ecaa-4212-b063-815acae6d0bb |
| Jogador 6 | 5-3 | 287 | BUY | ALL_IN | 9.0 | 7 | 80 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017245950177311897 | 0.0 | 0.0 | +d22aa2b7-7c7c-4d47-89be-0f1b8755971c / -— |
| Jogador 6 | 5-3 | 288 | REROLL | ALL_IN | 9.0 | 7 | 77 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0674000009894371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 289 | SELL | ALL_IN | 9.0 | 7 | 75 | 5 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014918148517608643 | 0.0 | 0.0 | +— / -a492f78e-91f0-48cb-891a-6518551da328 |
| Jogador 6 | 5-3 | 290 | BUY | ALL_IN | 9.0 | 7 | 77 | 5 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2574580907821655 | 0.0 | 0.0 | +a1357716-abf4-4d4f-abb8-34f2681f16dd / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589178562164307 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2799173593521118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.143971249461174 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 22 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012334865517914295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 23 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4041116237640381 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0485426187515259 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23102644085884094 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004352054558694363 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 32 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005867671221494675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 33 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0368766784667969 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24523751437664032 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007539904909208417 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1995791792869568 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 46 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8280633091926575 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19953078031539917 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24521686136722565 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 58 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30114036798477173 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 59 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4377893805503845 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 64 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0475770235061646 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 65 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15446753799915314 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 67 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17921476066112518 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 69 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04722195118665695 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 70 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -0d8b39fc-eb5c-4679-b615-50cdfdcf3eee |
| Jogador 7 | 2-3 | 72 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 1.0476582050323486 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-3 | 73 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.6828120946884155 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 7 | 2-3 | 74 | EQUIP_FROM_INVENTORY | STABILIZE | 96.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14097575843334198 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 75 | EQUIP_FROM_INVENTORY | STABILIZE | 96.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10850680619478226 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 76 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0981186255812645 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 77 | PASS | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 82 | BUY | STABILIZE | 96.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30692818760871887 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 83 | BUY | STABILIZE | 96.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2087995707988739 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 84 | SELL | STABILIZE | 96.0 | 5 | 2 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.127887561917305 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-4 | 85 | BUY_XP | STABILIZE | 96.0 | 5 | 4 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32358306646347046 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 87 | SELL | STABILIZE | 96.0 | 5 | 0 | 0 | 14.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08233333379030228 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-4 | 88 | BUY | STABILIZE | 96.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.227054625749588 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 7 | 2-4 | 89 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 14.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10826782137155533 | 0.0 | 0.0 | +— / -3280b28e-bd8f-494b-a78d-111744e2178b |
| Jogador 7 | 2-4 | 90 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0011077991221100092 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 92 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.323162704706192 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 93 | BUY | STABILIZE | 96.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32676929235458374 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 94 | BUY_XP | STABILIZE | 96.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 95 | SELL | STABILIZE | 96.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4610956013202667 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 7 | 2-5 | 96 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0436728335916996 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-5 | 97 | PASS | STABILIZE | 96.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 102 | BUY | STABILIZE | 96.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0054153203964233 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 103 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.963241457939148 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 104 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 105 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6157711148262024 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-6 | 106 | SELL | STABILIZE | 96.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6251818537712097 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 2-6 | 107 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050634998828172684 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 108 | SELL | STABILIZE | 96.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6269999742507935 | 0.0 | 0.0 | +— / -fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 2-6 | 109 | BUY_XP | STABILIZE | 96.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 110 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013304771855473518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 112 | BUY | STABILIZE | 96.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2818029820919037 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 113 | BUY_XP | STABILIZE | 96.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 114 | SELL | STABILIZE | 96.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01899999938905239 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 2-7 | 115 | BUY | STABILIZE | 96.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01704118587076664 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 116 | SELL | STABILIZE | 96.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03566666692495346 | 0.0 | 0.0 | +— / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c |
| Jogador 7 | 2-7 | 117 | BUY_XP | STABILIZE | 96.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 118 | SELL | STABILIZE | 96.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0230000019073486 | 0.0 | 0.0 | +— / -a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 2-7 | 119 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 120 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21613341569900513 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 122 | BUY | STABILIZE | 96.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2829407751560211 | 0.0 | 0.0 | +033a84d9-70f6-46a8-a6eb-a2f03be70400 / -— |
| Jogador 7 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18571749329566956 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 124 | BUY_XP | STABILIZE | 96.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 125 | SELL | STABILIZE | 96.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.619088888168335 | 0.0 | 0.0 | +— / -033a84d9-70f6-46a8-a6eb-a2f03be70400 |
| Jogador 7 | 3-1 | 126 | BUY | STABILIZE | 96.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0881374180316925 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 127 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002529659541323781 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 128 | SELL | STABILIZE | 96.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -ad1693cd-1ab5-43a9-8164-25929b8bd68e |
| Jogador 7 | 3-1 | 129 | BUY | STABILIZE | 96.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25238415598869324 | 0.0 | 0.0 | +5d00c8ab-55fb-42ec-b8ec-75011c7722fc / -— |
| Jogador 7 | 3-1 | 130 | BUY | STABILIZE | 96.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08629054576158524 | 0.0 | 0.0 | +dbe9f465-e302-46d0-9bd4-93969fde6ecb / -— |
| Jogador 7 | 3-2 | 132 | BUY | STABILIZE | 86.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26776769757270813 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 133 | BUY | STABILIZE | 86.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2524949610233307 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -— |
| Jogador 7 | 3-2 | 134 | SELL | STABILIZE | 86.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045099999755620956 | 0.0 | 0.0 | +— / -dbe9f465-e302-46d0-9bd4-93969fde6ecb |
| Jogador 7 | 3-2 | 135 | BUY | STABILIZE | 86.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.086279958486557 | 0.0 | 0.0 | +8043a64c-a04d-4399-b52d-2246fe74e470 / -— |
| Jogador 7 | 3-2 | 136 | SELL | STABILIZE | 86.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3343333303928375 | 0.0 | 0.0 | +— / -8043a64c-a04d-4399-b52d-2246fe74e470 |
| Jogador 7 | 3-2 | 137 | SELL | STABILIZE | 86.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030533334240317345 | 0.0 | 0.0 | +— / -5d00c8ab-55fb-42ec-b8ec-75011c7722fc |
| Jogador 7 | 3-2 | 138 | BUY | STABILIZE | 86.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31226786971092224 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -— |
| Jogador 7 | 3-2 | 139 | SELL | STABILIZE | 86.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19699999690055847 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 3-2 | 140 | BUY_XP | STABILIZE | 86.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 142 | BUY | STABILIZE | 86.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0881260558962822 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 143 | BUY | STABILIZE | 86.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17157508432865143 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -— |
| Jogador 7 | 3-3 | 144 | BUY | STABILIZE | 86.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003979954402893782 | 0.0 | 0.0 | +4d03897d-0113-4a29-a864-75305c142d97 / -— |
| Jogador 7 | 3-3 | 145 | SELL | STABILIZE | 86.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42633333802223206 | 0.0 | 0.0 | +— / -652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 7 | 3-3 | 146 | SELL | STABILIZE | 86.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09639959037303925 | 0.0 | 0.0 | +— / -4d03897d-0113-4a29-a864-75305c142d97 |
| Jogador 7 | 3-3 | 147 | SELL | STABILIZE | 86.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09566666930913925 | 0.0 | 0.0 | +— / -f116ca4e-dbe8-457e-83a5-958525aa384a |
| Jogador 7 | 3-3 | 148 | BUY | STABILIZE | 86.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2562914788722992 | 0.0 | 0.0 | +2399a42a-332c-42ee-9bd8-5f52bb921ffa / -— |
| Jogador 7 | 3-3 | 149 | BUY_XP | STABILIZE | 86.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 150 | SELL | STABILIZE | 86.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03433333337306976 | 0.0 | 0.0 | +— / -2399a42a-332c-42ee-9bd8-5f52bb921ffa |
| Jogador 7 | 3-4 | 152 | BUY | STABILIZE | 77.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079598546028137 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 7 | 3-4 | 153 | BUY | STABILIZE | 77.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.829063355922699 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -2c7e844d-925a-43bb-8be8-65a71d11f964,6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 3-4 | 154 | SELL | STABILIZE | 77.0 | 6 | 3 | 0 | 14.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5389999747276306 | 0.0 | 0.0 | +— / -cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 3-4 | 155 | BUY_XP | STABILIZE | 77.0 | 6 | 11 | 1 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0731000006198883 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 156 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 7 | 0 | 14.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2798396050930023 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 157 | BUY | STABILIZE | 77.0 | 7 | 7 | 0 | 16.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01227449532598257 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 158 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 4 | 0 | 16.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15020234882831573 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 159 | BUY | STABILIZE | 77.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2930259108543396 | 0.0 | 0.0 | +7e545d27-1847-4016-b42b-e7db1960ae89 / -— |
| Jogador 7 | 3-4 | 160 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 2 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005194046534597874 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 162 | BUY | STABILIZE | 77.0 | 7 | 7 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050442107021808624 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 163 | BUY | STABILIZE | 77.0 | 7 | 4 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1462979018688202 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 7 | 3-5 | 164 | BUY | STABILIZE | 77.0 | 7 | 3 | 0 | 22.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0790671557188034 | 0.0 | 0.0 | +f546078f-fc3e-44a9-9b8f-25c46a043168 / -— |
| Jogador 7 | 3-5 | 165 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0005324846133589745 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 166 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 167 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015002723783254623 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 168 | PASS | STABILIZE | 77.0 | 7 | 1 | 0 | 22.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 172 | BUY | STABILIZE | 66.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2784430980682373 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 173 | BUY | STABILIZE | 66.0 | 7 | 3 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23396363854408264 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 7 | 3-6 | 174 | MOVE_BOARD | STABILIZE | 66.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 175 | MOVE_BOARD | STABILIZE | 66.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015149371698498726 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 176 | PASS | STABILIZE | 66.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_18_Varus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 182 | BUY | STABILIZE | 56.0 | 7 | 6 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7983778119087219 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 183 | SELL | STABILIZE | 56.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024000000208616257 | 0.0 | 0.0 | +— / -7e545d27-1847-4016-b42b-e7db1960ae89 |
| Jogador 7 | 3-7 | 184 | BUY | STABILIZE | 56.0 | 7 | 4 | 0 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28540775179862976 | 0.0 | 0.0 | +21135c93-ae87-47a0-899c-7eaa0c2c30b8 / -— |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0021763218101114035 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 186 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 187 | PASS | STABILIZE | 56.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | STABILIZE | 56.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | STABILIZE | 56.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06441033631563187 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 194 | SELL | STABILIZE | 56.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07280000299215317 | 0.0 | 0.0 | +— / -f546078f-fc3e-44a9-9b8f-25c46a043168 |
| Jogador 7 | 4-1 | 195 | BUY | STABILIZE | 56.0 | 7 | 10 | 1 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2754330635070801 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 7 | 4-1 | 196 | SELL | STABILIZE | 56.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056166667491197586 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-1 | 197 | BUY | STABILIZE | 56.0 | 7 | 10 | 1 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014101250097155571 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 7 | 4-1 | 198 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.0459730371367186e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 199 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 200 | PASS | STABILIZE | 56.0 | 7 | 7 | 0 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 202 | SELL | STABILIZE | 56.0 | 7 | 13 | 1 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025875119492411613 | 0.0 | 0.0 | +— / -2faa526c-d29e-47a9-9eb3-5030750cb483 |
| Jogador 7 | 4-2 | 203 | BUY | STABILIZE | 56.0 | 7 | 16 | 1 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28390181064605713 | 0.0 | 0.0 | +07cc291c-137e-4668-9caf-3a1fa8f09c3d / -— |
| Jogador 7 | 4-2 | 204 | SELL | STABILIZE | 56.0 | 7 | 14 | 1 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4331328868865967 | 0.0 | 0.0 | +— / -fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 4-2 | 205 | BUY | STABILIZE | 56.0 | 7 | 16 | 1 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8037742972373962 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 7 | 4-2 | 206 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 14 | 1 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0016470480477437377 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 207 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 14 | 1 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021653084084391594 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 208 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 14 | 1 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015874959528446198 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 209 | PASS | STABILIZE | 56.0 | 7 | 14 | 1 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 212 | SELL | STABILIZE | 44.0 | 7 | 20 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4166666567325592 | 0.0 | 0.0 | +— / -b2a77bec-e150-4d98-847c-9f2cfb50cbe7 |
| Jogador 7 | 4-3 | 213 | BUY | STABILIZE | 44.0 | 7 | 23 | 2 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23566953837871552 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 7 | 4-3 | 214 | SELL | STABILIZE | 44.0 | 7 | 19 | 1 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08910000324249268 | 0.0 | 0.0 | +— / -69ccc61a-403b-4025-8359-b2061dc6ad10 |
| Jogador 7 | 4-3 | 215 | BUY | STABILIZE | 44.0 | 7 | 22 | 2 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0021252629812806845 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 7 | 4-3 | 216 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 20 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 217 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 20 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 218 | PASS | STABILIZE | 44.0 | 7 | 20 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029164021834731102 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 222 | SELL | STABILIZE | 44.0 | 7 | 28 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07280000299215317 | 0.0 | 0.0 | +— / -8455b875-27e0-4172-9311-5cbb3e2242b9 |
| Jogador 7 | 4-4 | 223 | BUY | STABILIZE | 44.0 | 7 | 30 | 3 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6798591017723083 | 0.0 | 0.0 | +7b49fb38-6e0e-4a72-a2ce-0527827d36a6 / -— |
| Jogador 7 | 4-4 | 224 | SELL | STABILIZE | 44.0 | 7 | 27 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0724666640162468 | 0.0 | 0.0 | +— / -e85c6ab6-f36c-40b4-88e2-b7380b4c9652 |
| Jogador 7 | 4-4 | 225 | BUY | STABILIZE | 44.0 | 7 | 31 | 3 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23816519975662231 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 28 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007950632832944393 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 28 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015032805502414703 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 228 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 28 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014966653659939766 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 229 | PASS | STABILIZE | 44.0 | 7 | 28 | 2 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03535238280892372 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 232 | SELL | STABILIZE | 44.0 | 7 | 35 | 3 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5608501434326172 | 0.0 | 0.0 | +— / -42f739bb-e676-4a27-a96f-c09d09d592bb |
| Jogador 7 | 4-5 | 233 | BUY | STABILIZE | 44.0 | 7 | 36 | 3 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7560385465621948 | 0.0 | 0.0 | +0f5471bd-1451-4979-adc9-aced6bb63610 / -— |
| Jogador 7 | 4-5 | 234 | SELL | STABILIZE | 44.0 | 7 | 33 | 3 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.531167209148407 | 0.0 | 0.0 | +— / -0f5471bd-1451-4979-adc9-aced6bb63610 |
| Jogador 7 | 4-5 | 235 | BUY | STABILIZE | 44.0 | 7 | 36 | 3 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2443084567785263 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 7 | 4-5 | 236 | SELL | STABILIZE | 44.0 | 7 | 32 | 3 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0141333332285285 | 0.0 | 0.0 | +— / -9717d30c-f073-470c-a6ce-7db8257de559 |
| Jogador 7 | 4-5 | 237 | BUY | STABILIZE | 44.0 | 7 | 36 | 3 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0029413807205855846 | 0.0 | 0.0 | +83228c14-cadb-45b4-9893-2fb12c40f4a8 / -— |
| Jogador 7 | 4-5 | 238 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 34 | 3 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.228085153570646e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 239 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 34 | 3 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01500041875988245 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 240 | PASS | STABILIZE | 44.0 | 7 | 34 | 3 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03999365121126175 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 242 | SELL | STABILIZE | 44.0 | 7 | 44 | 4 | 26.0 | Colosso/DA_18_Varus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007199999876320362 | 0.0 | 0.0 | +— / -83228c14-cadb-45b4-9893-2fb12c40f4a8 |
| Jogador 7 | 4-6 | 243 | BUY | STABILIZE | 44.0 | 7 | 46 | 4 | 26.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9279980063438416 | 0.0 | 0.0 | +8b75555c-d84d-4b8a-8d6c-012585a05b99 / -1ff50c59-5133-459e-8bf1-d449c26efabf,4e206e09-40e3-4699-81cb-8aaf01109dea |
| Jogador 7 | 4-6 | 244 | BUY | STABILIZE | 44.0 | 7 | 45 | 4 | 24.0 | Colosso/DA_18_Varus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8934519290924072 | 0.0 | 0.0 | +18e21ac6-f873-4310-95c8-bd8e62612479 / -0cf5c315-d2f3-4854-a95b-07912b83ea81,7b49fb38-6e0e-4a72-a2ce-0527827d36a6 |
| Jogador 7 | 4-6 | 245 | MOVE_BENCH | STABILIZE | 44.0 | 7 | 42 | 4 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34986141324043274 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 246 | BUY | STABILIZE | 44.0 | 7 | 42 | 4 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2235581874847412 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |
| Jogador 7 | 4-6 | 247 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 39 | 3 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 7.232757752717589e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 248 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 39 | 3 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020632876083254814 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 249 | MOVE_BENCH | STABILIZE | 44.0 | 7 | 39 | 3 | 22.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37976738810539246 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 250 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 39 | 3 | 28.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0031120458152145147 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 252 | BUY | STABILIZE | 44.0 | 7 | 50 | 5 | 28.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8058632016181946 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 7 | 4-7 | 253 | BUY | STABILIZE | 44.0 | 7 | 48 | 4 | 28.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08321524411439896 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 7 | 4-7 | 254 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 45 | 4 | 28.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 255 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 45 | 4 | 28.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016279662027955055 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 256 | PASS | STABILIZE | 44.0 | 7 | 45 | 4 | 28.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04820634797215462 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 44.0 | 7 | 55 | 5 | 28.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13705605268478394 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 44.0 | 7 | 55 | 5 | 28.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1063995361328125 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 264 | SELL | STABILIZE | 44.0 | 7 | 55 | 5 | 28.0 | Colosso/DA_18_Hecarim | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46922966837882996 | 0.0 | 0.0 | +— / -18e21ac6-f873-4310-95c8-bd8e62612479 |
| Jogador 7 | 5-1 | 265 | BUY | STABILIZE | 44.0 | 7 | 63 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03898745775222778 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 7 | 5-1 | 266 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 58 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002770810096990317 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 267 | SELL | STABILIZE | 44.0 | 7 | 58 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -80130f72-2d7c-49db-8d6f-4c0a962260e8 |
| Jogador 7 | 5-1 | 268 | BUY | STABILIZE | 44.0 | 7 | 61 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09065485000610352 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 7 | 5-1 | 269 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 59 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0033760694786906242 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 270 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 59 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015113186091184616 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 272 | SELL | STABILIZE | 44.0 | 7 | 71 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03042815625667572 | 0.0 | 0.0 | +— / -98b600a1-736b-437d-a69e-8a7f7235d9c3 |
| Jogador 7 | 5-2 | 273 | BUY | STABILIZE | 44.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44750404357910156 | 0.0 | 0.0 | +9414ca8e-930e-4a0e-8cbd-42d8997d8705 / -— |
| Jogador 7 | 5-2 | 274 | SELL | STABILIZE | 44.0 | 7 | 71 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02419999986886978 | 0.0 | 0.0 | +— / -c7a7408a-e7bd-428d-9935-4d5a002d8d9f |
| Jogador 7 | 5-2 | 275 | BUY | STABILIZE | 44.0 | 7 | 76 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12008195370435715 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 7 | 5-2 | 276 | SELL | STABILIZE | 44.0 | 7 | 73 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03893333300948143 | 0.0 | 0.0 | +— / -986fbe1e-1826-4be7-a5d6-410a4c0a3f2f |
| Jogador 7 | 5-2 | 277 | BUY | STABILIZE | 44.0 | 7 | 76 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08821967244148254 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 7 | 5-2 | 278 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 74 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00011979924602201208 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 279 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 74 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 280 | MOVE_BOARD | STABILIZE | 44.0 | 7 | 74 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 282 | SELL | STABILIZE | 31.0 | 7 | 84 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03164219483733177 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 7 | 5-3 | 283 | BUY | STABILIZE | 31.0 | 7 | 86 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00147728412412107 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 7 | 5-3 | 284 | SELL | STABILIZE | 31.0 | 7 | 84 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -f84cc827-410f-47eb-bd95-bd650acfdd4b |
| Jogador 7 | 5-3 | 285 | BUY | STABILIZE | 31.0 | 7 | 86 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0014843569369986653 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 7 | 5-3 | 286 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 84 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 287 | SELL | STABILIZE | 31.0 | 7 | 84 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013799999840557575 | 0.0 | 0.0 | +— / -973ba75e-ffa8-41f5-a3fb-e238e34d0216 |
| Jogador 7 | 5-3 | 288 | BUY | STABILIZE | 31.0 | 7 | 86 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22435583174228668 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 7 | 5-3 | 289 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 83 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.868327894451795e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 290 | MOVE_BOARD | STABILIZE | 31.0 | 7 | 83 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01501319371163845 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 292 | SELL | ALL_IN | 16.0 | 7 | 94 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 7 | 5-4 | 293 | BUY | ALL_IN | 16.0 | 7 | 97 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0506768226623535 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -21135c93-ae87-47a0-899c-7eaa0c2c30b8,bcd06176-e1d7-43fb-abd4-b6faea8c7927 |
| Jogador 7 | 5-4 | 294 | BUY | ALL_IN | 16.0 | 7 | 95 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9041376113891602 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 7 | 5-4 | 295 | BUY | ALL_IN | 16.0 | 7 | 92 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04767488315701485 | 0.0 | 0.0 | +eb418af1-c963-4da2-b052-86a153fc5ba1 / -— |
| Jogador 7 | 5-4 | 296 | SELL | ALL_IN | 16.0 | 7 | 88 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.70169997215271 | 0.0 | 0.0 | +— / -57ba484a-6228-4263-8171-00a8a5893bea |
| Jogador 7 | 5-4 | 297 | BUY | ALL_IN | 16.0 | 7 | 93 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11102264374494553 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -— |
| Jogador 7 | 5-4 | 298 | MOVE_BOARD | ALL_IN | 16.0 | 7 | 91 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 9.105077083404467e-07 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 299 | SELL | ALL_IN | 16.0 | 7 | 91 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031234577298164368 | 0.0 | 0.0 | +— / -7f9f3188-2482-4518-9fd2-34f0ea1527a9 |
| Jogador 7 | 5-4 | 300 | BUY | ALL_IN | 16.0 | 7 | 93 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02668636105954647 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -— |
| Jogador 7 | 5-5 | 302 | SELL | ALL_IN | 16.0 | 7 | 102 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0285333339124918 | 0.0 | 0.0 | +— / -0c96798c-ee23-488b-974f-74e8e3da6aa6 |
| Jogador 7 | 5-5 | 303 | BUY | ALL_IN | 16.0 | 7 | 104 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43293464183807373 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 7 | 5-5 | 304 | SELL | ALL_IN | 16.0 | 7 | 101 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020733334124088287 | 0.0 | 0.0 | +— / -eb418af1-c963-4da2-b052-86a153fc5ba1 |
| Jogador 7 | 5-5 | 305 | BUY | ALL_IN | 16.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20241650938987732 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 7 | 5-5 | 306 | SELL | ALL_IN | 16.0 | 7 | 104 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06532410532236099 | 0.0 | 0.0 | +— / -6fb5e8f1-2656-486b-9478-161c1b430d5f |
| Jogador 7 | 5-5 | 307 | BUY | ALL_IN | 16.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2317601591348648 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 7 | 5-5 | 308 | SELL | ALL_IN | 16.0 | 7 | 102 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 |
| Jogador 7 | 5-5 | 309 | BUY | ALL_IN | 16.0 | 7 | 105 | 5 | 28.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27637672424316406 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 7 | 5-5 | 310 | MOVE_BOARD | ALL_IN | 16.0 | 7 | 102 | 5 | 28.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.29289698600769043 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.24373739957809448 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031589943915605545 | 0.0 | 0.0 | +88a02960-5ebe-4b20-b667-1a8ce2728578 / -— |
| Jogador 8 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16182130575180054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620654344558716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012301865965127945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5023400187492371 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0144696235656738 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3603994846343994 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 42 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28139108419418335 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 43 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9762644171714783 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 44 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17347893118858337 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 45 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25109246373176575 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 46 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1158239021897316 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 47 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 55 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1142820119857788 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -88a02960-5ebe-4b20-b667-1a8ce2728578,dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 2-1 | 56 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2007744014263153 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 57 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1791006177663803 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 4.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05933481082320213 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 59 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.103461742401123 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -322e9047-623a-4fec-a0f9-d21d2fbcd88a,4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 2-1 | 60 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12411493062973022 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4076586961746216 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 62 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04551059752702713 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-2 | 64 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2568693459033966 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 65 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21238096058368683 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 66 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058597031980752945 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 67 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1110355481505394 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 68 | SELL | STABILIZE | 94.0 | 4 | 0 | 0 | 12.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045099999755620956 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 69 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5003097653388977 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 70 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 1 | 0 | 12.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04973304644227028 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 72 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9851475954055786 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-3 | 73 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0478975772857666 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-3 | 74 | BUY | STABILIZE | 89.0 | 4 | 5 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36942148208618164 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 75 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 4 | 0 | 10.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41361966729164124 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 76 | BUY | STABILIZE | 89.0 | 4 | 4 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3013145625591278 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 77 | SELL | STABILIZE | 89.0 | 4 | 1 | 0 | 14.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6290000081062317 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-3 | 78 | BUY_XP | STABILIZE | 89.0 | 4 | 4 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 79 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 4.163336342344337e-17 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 80 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1763976365327835 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 82 | BUY | STABILIZE | 82.0 | 5 | 6 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20249995589256287 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 83 | BUY | STABILIZE | 82.0 | 5 | 3 | 0 | 14.0 | —/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12413080781698227 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 84 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 0 | 0 | 14.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35189196467399597 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 85 | SELL | STABILIZE | 82.0 | 5 | 0 | 0 | 20.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10233332961797714 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-4 | 86 | BUY | STABILIZE | 82.0 | 5 | 1 | 0 | 20.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1823289543390274 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 8 | 2-4 | 87 | SELL | STABILIZE | 82.0 | 5 | 0 | 0 | 20.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4129999876022339 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 8 | 2-4 | 88 | BUY | STABILIZE | 82.0 | 5 | 1 | 0 | 20.0 | —/DA_Karma18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13785012066364288 | 0.0 | 0.0 | +3644801e-2247-403d-8b81-d2d3f15c2f55 / -— |
| Jogador 8 | 2-4 | 89 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 0 | 0 | 20.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05297031253576279 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 90 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 0 | 0 | 16.0 | —/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03435591980814934 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 92 | BUY | STABILIZE | 82.0 | 5 | 6 | 0 | 18.0 | —/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8992213606834412 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 93 | BUY | STABILIZE | 82.0 | 5 | 5 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8559896945953369 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 94 | BUY | STABILIZE | 82.0 | 5 | 3 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11531834304332733 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 95 | SELL | STABILIZE | 82.0 | 5 | 0 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008233333006501198 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-5 | 96 | SELL | STABILIZE | 82.0 | 5 | 3 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07699999958276749 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 2-5 | 97 | SELL | STABILIZE | 82.0 | 5 | 6 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09152868390083313 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-5 | 98 | SELL | STABILIZE | 82.0 | 5 | 9 | 0 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3351041376590729 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 2-5 | 99 | SELL | STABILIZE | 82.0 | 5 | 11 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4196385443210602 | 0.0 | 0.0 | +— / -2e656a3d-eed0-40bb-a831-443d972d6588 |
| Jogador 8 | 2-5 | 100 | BUY | STABILIZE | 82.0 | 5 | 14 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08225987106561661 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-6 | 102 | BUY | STABILIZE | 75.0 | 5 | 19 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27790141105651855 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 103 | BUY | STABILIZE | 75.0 | 5 | 16 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20321227610111237 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 104 | BUY | STABILIZE | 75.0 | 5 | 13 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17212773859500885 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 8 | 2-6 | 105 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 12 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6072707772254944 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 106 | SELL | STABILIZE | 75.0 | 5 | 12 | 1 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38100001215934753 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 8 | 2-6 | 107 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 13 | 1 | 22.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1011485829949379 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 108 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 13 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03319073095917702 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 109 | SELL | STABILIZE | 75.0 | 5 | 13 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07566666603088379 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 2-6 | 110 | SELL | STABILIZE | 75.0 | 5 | 15 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4270159602165222 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 2-7 | 112 | BUY | STABILIZE | 75.0 | 5 | 25 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8914176225662231 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 113 | BUY | STABILIZE | 75.0 | 5 | 22 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048808611929416656 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 114 | BUY | STABILIZE | 75.0 | 5 | 19 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1113896369934082 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 8 | 2-7 | 115 | SELL | STABILIZE | 75.0 | 5 | 18 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3943333327770233 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 8 | 2-7 | 116 | SELL | STABILIZE | 75.0 | 5 | 19 | 1 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31700000166893005 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 117 | BUY | STABILIZE | 75.0 | 5 | 22 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09064831584692001 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 118 | SELL | STABILIZE | 75.0 | 5 | 21 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38833022117614746 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 119 | SELL | STABILIZE | 75.0 | 5 | 22 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5649296045303345 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 120 | SELL | STABILIZE | 75.0 | 5 | 25 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14149701595306396 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 3-1 | 122 | BUY | STABILIZE | 75.0 | 5 | 35 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08792201429605484 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 123 | CRAFT_AND_EQUIP | STABILIZE | 75.0 | 5 | 31 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.25733646750450134 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 124 | BUY | STABILIZE | 75.0 | 5 | 31 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07927091419696808 | 0.0 | 0.0 | +88420167-3841-43dd-b1d0-3e5ab2294c78 / -— |
| Jogador 8 | 3-1 | 125 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 29 | 2 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3870648741722107 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 126 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 29 | 2 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1765119582414627 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 127 | PASS | STABILIZE | 75.0 | 5 | 29 | 2 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08049999922513962 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 132 | BUY | STABILIZE | 65.0 | 5 | 36 | 3 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09462468326091766 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 133 | BUY | STABILIZE | 65.0 | 5 | 32 | 3 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0080405930057168 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 134 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 31 | 3 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05643419176340103 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 135 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 31 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13058973848819733 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 136 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 31 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07398592680692673 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 137 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 31 | 3 | 20.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03333483636379242 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 138 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 31 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39968132972717285 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 139 | MOVE_BENCH | STABILIZE | 65.0 | 5 | 31 | 3 | 16.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38065603375434875 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 140 | PASS | STABILIZE | 65.0 | 5 | 31 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12349999696016312 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 142 | BUY | STABILIZE | 55.0 | 5 | 40 | 4 | 18.0 | Enfeitiçador/DA_Karma18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2411165088415146 | 0.0 | 0.0 | +8df39648-f588-452a-b234-32da76c43aff / -— |
| Jogador 8 | 3-3 | 143 | SELL | STABILIZE | 55.0 | 5 | 39 | 3 | 18.0 | Enfeitiçador/DA_Karma18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5040000081062317 | 0.0 | 0.0 | +— / -76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 3-3 | 144 | BUY | STABILIZE | 55.0 | 5 | 42 | 4 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.5730512738227844 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 145 | EQUIP_FROM_INVENTORY | STABILIZE | 55.0 | 5 | 41 | 4 | 18.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15898019075393677 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 146 | SELL | STABILIZE | 55.0 | 5 | 41 | 4 | 18.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009810009971261024 | 0.0 | 0.0 | +— / -4ac49c80-f0c3-47ae-a031-96928d244e13 |
| Jogador 8 | 3-3 | 147 | SELL | STABILIZE | 55.0 | 5 | 45 | 4 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06967785209417343 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 3-3 | 148 | BUY | STABILIZE | 55.0 | 5 | 49 | 4 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30220091342926025 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 8 | 3-3 | 149 | SELL | STABILIZE | 55.0 | 5 | 47 | 4 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2290000021457672 | 0.0 | 0.0 | +— / -1af578c1-57cf-4752-93e7-d0eebc6e8ae5 |
| Jogador 8 | 3-3 | 150 | SELL | STABILIZE | 55.0 | 5 | 49 | 4 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42316704988479614 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-4 | 152 | BUY | STABILIZE | 55.0 | 5 | 61 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9433402419090271 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -5de56114-806a-4f58-8241-b3b8434a2154,b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 3-4 | 153 | BUY | STABILIZE | 55.0 | 5 | 60 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8967228531837463 | 0.0 | 0.0 | +e8355df5-8ee7-44a3-ab88-3708c14fd5dc / -— |
| Jogador 8 | 3-4 | 154 | SELL | STABILIZE | 55.0 | 5 | 59 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6388999819755554 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 8 | 3-4 | 155 | BUY | STABILIZE | 55.0 | 5 | 62 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07551882416009903 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 156 | SELL | STABILIZE | 55.0 | 5 | 59 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08841681480407715 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-4 | 157 | SELL | STABILIZE | 55.0 | 5 | 60 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4120052456855774 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-4 | 158 | SELL | STABILIZE | 55.0 | 5 | 63 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6363000273704529 | 0.0 | 0.0 | +— / -8df39648-f588-452a-b234-32da76c43aff |
| Jogador 8 | 3-4 | 159 | SELL | STABILIZE | 55.0 | 5 | 64 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9801444411277771 | 0.0 | 0.0 | +— / -e8355df5-8ee7-44a3-ab88-3708c14fd5dc |
| Jogador 8 | 3-4 | 160 | SELL | STABILIZE | 55.0 | 5 | 65 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8622981905937195 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 3-5 | 162 | BUY | STABILIZE | 55.0 | 5 | 77 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9885488748550415 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 163 | BUY | STABILIZE | 55.0 | 5 | 74 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3999256193637848 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 164 | BUY | STABILIZE | 55.0 | 5 | 72 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9508921504020691 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -— |
| Jogador 8 | 3-5 | 165 | BUY | STABILIZE | 55.0 | 5 | 70 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2612634599208832 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 166 | SELL | STABILIZE | 55.0 | 5 | 68 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32760000228881836 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 3-5 | 167 | SELL | STABILIZE | 55.0 | 5 | 70 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4123174250125885 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 3-5 | 168 | SELL | STABILIZE | 55.0 | 5 | 72 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6575999855995178 | 0.0 | 0.0 | +— / -9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 169 | SELL | STABILIZE | 55.0 | 5 | 74 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23757220804691315 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 8 | 3-5 | 170 | BUY | STABILIZE | 55.0 | 5 | 76 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2689902186393738 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 8 | 3-6 | 172 | BUY | STABILIZE | 45.0 | 5 | 85 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9476484060287476 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 8 | 3-6 | 173 | BUY | STABILIZE | 45.0 | 5 | 84 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8274149298667908 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 174 | BUY | STABILIZE | 45.0 | 5 | 82 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10713594406843185 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 175 | SELL | STABILIZE | 45.0 | 5 | 78 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02630000002682209 | 0.0 | 0.0 | +— / -fa5dc86b-f736-4083-b9df-5cc174b726f2 |
| Jogador 8 | 3-6 | 176 | SELL | STABILIZE | 45.0 | 5 | 79 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40486666560173035 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 8 | 3-6 | 177 | BUY | STABILIZE | 45.0 | 5 | 83 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03183892369270325 | 0.0 | 0.0 | +5f79a010-9e28-4a94-be40-973a17313186 / -— |
| Jogador 8 | 3-6 | 178 | SELL | STABILIZE | 45.0 | 5 | 80 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3779033422470093 | 0.0 | 0.0 | +— / -5f79a010-9e28-4a94-be40-973a17313186 |
| Jogador 8 | 3-6 | 179 | SELL | STABILIZE | 45.0 | 5 | 83 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5545971989631653 | 0.0 | 0.0 | +— / -23366968-ed3f-43d0-9f24-bb7691bf5d45 |
| Jogador 8 | 3-6 | 180 | SELL | STABILIZE | 45.0 | 5 | 85 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.998180627822876 | 0.0 | 0.0 | +— / -b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 8 | 3-7 | 182 | BUY | STABILIZE | 36.0 | 6 | 97 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4755825400352478 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 8 | 3-7 | 183 | BUY | STABILIZE | 36.0 | 6 | 96 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09142447263002396 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 184 | BUY | STABILIZE | 36.0 | 6 | 93 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024430546909570694 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 185 | BUY | STABILIZE | 36.0 | 6 | 90 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25968676805496216 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 8 | 3-7 | 186 | MOVE_BENCH | STABILIZE | 36.0 | 6 | 88 | 5 | 18.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41341179609298706 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 187 | BUY | STABILIZE | 36.0 | 6 | 88 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0436958409845829 | 0.0 | 0.0 | +014c92c3-e588-4e8b-b4bd-93cee45d74af / -— |
| Jogador 8 | 3-7 | 188 | MOVE_BOARD | STABILIZE | 36.0 | 6 | 87 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0034821724984794855 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 189 | MOVE_BOARD | STABILIZE | 36.0 | 6 | 87 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014877605251967907 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 190 | MOVE_BOARD | STABILIZE | 36.0 | 6 | 87 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01983482390642166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 192 | BUY | STABILIZE | 36.0 | 6 | 98 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.012042760848999 | 0.0 | 0.0 | +b750b244-a898-479e-9a8e-f30a3f4b0005 / -— |
| Jogador 8 | 4-1 | 193 | BUY | STABILIZE | 36.0 | 6 | 97 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.36653849482536316 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 8 | 4-1 | 194 | BUY | STABILIZE | 36.0 | 6 | 95 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.16324402391910553 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 8 | 4-1 | 195 | BUY | STABILIZE | 36.0 | 6 | 92 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08179929852485657 | 0.0 | 0.0 | +e94d3ae5-8c17-4d86-b6d9-f8141ac1756b / -— |
| Jogador 8 | 4-1 | 196 | CRAFT_AND_EQUIP | STABILIZE | 36.0 | 6 | 90 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2516119182109833 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 197 | CRAFT_AND_EQUIP | STABILIZE | 36.0 | 6 | 90 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.24717986583709717 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 198 | SELL | STABILIZE | 36.0 | 6 | 90 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01133333332836628 | 0.0 | 0.0 | +— / -014c92c3-e588-4e8b-b4bd-93cee45d74af |
| Jogador 8 | 4-1 | 199 | BUY | STABILIZE | 36.0 | 6 | 91 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12788830697536469 | 0.0 | 0.0 | +6fa83356-562b-4a26-a77d-3e989089e70a / -— |
| Jogador 8 | 4-1 | 200 | SELL | STABILIZE | 36.0 | 6 | 90 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -6fa83356-562b-4a26-a77d-3e989089e70a |
| Jogador 8 | 4-2 | 202 | BUY | STABILIZE | 36.0 | 6 | 102 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7835310101509094 | 0.0 | 0.0 | +ea460790-b046-451d-9174-8b613e476241 / -— |
| Jogador 8 | 4-2 | 203 | SELL | STABILIZE | 36.0 | 6 | 101 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030246460810303688 | 0.0 | 0.0 | +— / -e94d3ae5-8c17-4d86-b6d9-f8141ac1756b |
| Jogador 8 | 4-2 | 204 | BUY | STABILIZE | 36.0 | 6 | 103 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5626617670059204 | 0.0 | 0.0 | +cb30dcaa-bc26-4584-9b50-24e47e70fcb0 / -— |
| Jogador 8 | 4-2 | 205 | SELL | STABILIZE | 36.0 | 6 | 101 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 4-2 | 206 | BUY | STABILIZE | 36.0 | 6 | 104 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06518248468637466 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 8 | 4-2 | 207 | SELL | STABILIZE | 36.0 | 6 | 101 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017266666516661644 | 0.0 | 0.0 | +— / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 |
| Jogador 8 | 4-2 | 208 | BUY | STABILIZE | 36.0 | 6 | 104 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19468234479427338 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 8 | 4-2 | 209 | SELL | STABILIZE | 36.0 | 6 | 100 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025066666305065155 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 4-2 | 210 | BUY | STABILIZE | 36.0 | 6 | 103 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2139401137828827 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 8 | 4-3 | 212 | SELL | ALL_IN | 24.0 | 6 | 111 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00786666665226221 | 0.0 | 0.0 | +— / -6388773b-0e99-40a9-8d68-895dcf16fce6 |
| Jogador 8 | 4-3 | 213 | BUY | ALL_IN | 24.0 | 6 | 113 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3815498948097229 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 8 | 4-3 | 214 | SELL | ALL_IN | 24.0 | 6 | 111 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03373333439230919 | 0.0 | 0.0 | +— / -301afc05-ad23-4ed2-a835-108235c399e0 |
| Jogador 8 | 4-3 | 215 | BUY | ALL_IN | 24.0 | 6 | 114 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2414752095937729 | 0.0 | 0.0 | +94e3fa7e-029d-4de6-a1e4-9e67ce1b699e / -— |
| Jogador 8 | 4-3 | 216 | SELL | ALL_IN | 24.0 | 6 | 111 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0009333333582617342 | 0.0 | 0.0 | +— / -ba7f039a-929c-4537-9eb6-f1dc4563cca8 |
| Jogador 8 | 4-3 | 217 | BUY | ALL_IN | 24.0 | 6 | 115 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1525450348854065 | 0.0 | 0.0 | +6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 / -— |
| Jogador 8 | 4-3 | 218 | SELL | ALL_IN | 24.0 | 6 | 112 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030896281823515892 | 0.0 | 0.0 | +— / -6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 |
| Jogador 8 | 4-3 | 219 | BUY | ALL_IN | 24.0 | 6 | 115 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15553610026836395 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 8 | 4-3 | 220 | SELL | ALL_IN | 24.0 | 6 | 113 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008315461687743664 | 0.0 | 0.0 | +— / -a7893c5d-2faa-4292-9240-f3cc5813151e |
| Jogador 8 | 4-4 | 222 | BUY | ALL_IN | 12.0 | 6 | 126 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9233018755912781 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -— |
| Jogador 8 | 4-4 | 223 | SELL | ALL_IN | 12.0 | 6 | 124 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05428285151720047 | 0.0 | 0.0 | +— / -94e3fa7e-029d-4de6-a1e4-9e67ce1b699e |
| Jogador 8 | 4-4 | 224 | BUY | ALL_IN | 12.0 | 6 | 127 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44860753417015076 | 0.0 | 0.0 | +d53646ff-bb49-4f82-b761-faa4657f01cc / -— |
| Jogador 8 | 4-4 | 225 | SELL | ALL_IN | 12.0 | 6 | 126 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7077000141143799 | 0.0 | 0.0 | +— / -d53646ff-bb49-4f82-b761-faa4657f01cc |
| Jogador 8 | 4-4 | 226 | BUY | ALL_IN | 12.0 | 6 | 127 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46414536237716675 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 8 | 4-4 | 227 | SELL | ALL_IN | 12.0 | 6 | 124 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.616787314414978 | 0.0 | 0.0 | +— / -cb30dcaa-bc26-4584-9b50-24e47e70fcb0 |
| Jogador 8 | 4-4 | 228 | BUY | ALL_IN | 12.0 | 6 | 126 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2445986270904541 | 0.0 | 0.0 | +5477420d-3b98-4863-b2e7-f414d3fa1f01 / -— |
| Jogador 8 | 4-4 | 229 | SELL | ALL_IN | 12.0 | 6 | 125 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048351041972637177 | 0.0 | 0.0 | +— / -5477420d-3b98-4863-b2e7-f414d3fa1f01 |
| Jogador 8 | 4-4 | 230 | BUY | ALL_IN | 12.0 | 6 | 126 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21700681746006012 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 8 | 4-5 | 232 | SELL | ALL_IN | 12.0 | 6 | 136 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0034000000450760126 | 0.0 | 0.0 | +— / -d175e09c-3ed6-4fb3-8c97-0c167862e29e |
| Jogador 8 | 4-5 | 233 | BUY | ALL_IN | 12.0 | 6 | 137 | 5 | 22.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.046858787536621 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,ea460790-b046-451d-9174-8b613e476241 |
| Jogador 8 | 4-5 | 234 | BUY | ALL_IN | 12.0 | 6 | 136 | 5 | 20.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2390187382698059 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 8 | 4-5 | 235 | MOVE_BENCH | ALL_IN | 12.0 | 6 | 133 | 5 | 20.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38623544573783875 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 236 | BUY | ALL_IN | 12.0 | 6 | 133 | 5 | 26.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1674945056438446 | 0.0 | 0.0 | +a5c83255-d413-4d36-92a8-3552e6785108 / -— |
| Jogador 8 | 4-5 | 237 | SELL | ALL_IN | 12.0 | 6 | 131 | 5 | 26.0 | Enfeitiçador/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6881623268127441 | 0.0 | 0.0 | +— / -ded275a3-9551-4816-8112-f0a25524412c |
| Jogador 8 | 4-5 | 238 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 6 | 134 | 5 | 26.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.055838242173194885 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 239 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 6 | 134 | 5 | 26.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07864778488874435 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 240 | BUY | ALL_IN | 12.0 | 6 | 134 | 5 | 26.0 | Enfeitiçador/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016310257837176323 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 264 | 351 | 83 | 18 | 45 | 3 | 0 | 0 | 55 | 70.0 |
- Jogador 1 — gasto por ação: BUY: 155g, BUY_XP: 196g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 56g, stage 3: 65g, stage 4: 94g, stage 5: 52g, stage 6: 78g
| Jogador 2 | 305 | 367 | 227 | 8 | 19 | 1 | 0 | 0 | 156 | 50.0 |
- Jogador 2 — gasto por ação: BUY: 283g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 56g, stage 3: 77g, stage 4: 62g, stage 5: 80g, stage 6: 85g
| Jogador 3 | 269 | 280 | 203 | 7 | 7 | 1 | 2 | 0 | 206 | 30.0 |
- Jogador 3 — gasto por ação: BUY: 244g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 49g, stage 3: 46g, stage 4: 68g, stage 5: 72g, stage 6: 38g
| Jogador 4 | 162 | 130 | 55 | 3 | 6 | 1 | 1 | 0 | 67 | 28.0 |
- Jogador 4 — gasto por ação: BUY: 96g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 58g, stage 3: 40g, stage 4: 26g
| Jogador 5 | 186 | 190 | 130 | 6 | 4 | 0 | 3 | 0 | 111 | 22.0 |
- Jogador 5 — gasto por ação: BUY: 160g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 6g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 59g, stage 3: 68g, stage 4: 56g
| Jogador 6 | 206 | 222 | 121 | 7 | 12 | 0 | 2 | 0 | 74 | 30.0 |
- Jogador 6 — gasto por ação: BUY: 162g, BUY_XP: 56g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 64g, stage 3: 57g, stage 4: 60g, stage 5: 36g
| Jogador 7 | 227 | 226 | 134 | 8 | 10 | 1 | 0 | 0 | 102 | 28.0 |
- Jogador 7 — gasto por ação: BUY: 178g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 66g, stage 3: 67g, stage 4: 43g, stage 5: 44g
| Jogador 8 | 184 | 156 | 121 | 3 | 1 | 0 | 0 | 0 | 132 | 26.0 |
- Jogador 8 — gasto por ação: BUY: 152g, BUY_XP: 4g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 52g, stage 3: 50g, stage 4: 47g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 49 | 4 |
- Jogador 1 · 3-7 · step 186: PASS com 13g, HP 100, nível 7/8 (STABILIZE).
- Jogador 1 · 4-2 · step 210: PASS com 33g, HP 100, nível 7/8 (STABILIZE).
- Jogador 1 · 4-4 · step 227: PASS com 49g, HP 100, nível 7/8 (FAST8).
- Jogador 1 · 4-5 · step 240: PASS com 60g, HP 100, nível 7/8 (FAST8).
| Jogador 2 | 21 | 4 |
- Jogador 2 · 3-4 · step 160: PASS com 11g, HP 62, nível 6/8 (STABILIZE).
- Jogador 2 · 3-5 · step 167: PASS com 12g, HP 62, nível 6/8 (STABILIZE).
- Jogador 2 · 4-2 · step 207: PASS com 20g, HP 62, nível 7/8 (STABILIZE).
- Jogador 2 · 4-5 · step 240: PASS com 51g, HP 49, nível 7/8 (STABILIZE).
| Jogador 3 | 8 | 9 |
- Jogador 3 · 3-1 · step 129: PASS com 7g, HP 100, nível 6/8 (STABILIZE).
- Jogador 3 · 3-2 · step 138: PASS com 11g, HP 100, nível 6/8 (STABILIZE).
- Jogador 3 · 3-3 · step 147: PASS com 11g, HP 90, nível 6/8 (STABILIZE).
- Jogador 3 · 3-4 · step 158: PASS com 18g, HP 90, nível 6/8 (STABILIZE).
- Jogador 3 · 3-5 · step 169: PASS com 17g, HP 90, nível 6/8 (STABILIZE).
- Jogador 3 · 3-7 · step 188: PASS com 33g, HP 81, nível 6/8 (STABILIZE).
- Jogador 3 · 4-3 · step 220: PASS com 59g, HP 69, nível 6/8 (STABILIZE).
- Jogador 3 · 6-2 · step 350: REROLL com 200g, HP 23, nível 7/8 (ALL_IN).
- Jogador 3 · 6-3 · step 360: REROLL com 208g, HP 5, nível 7/8 (ALL_IN).
| Jogador 4 | 8 | 9 |
- Jogador 4 · 3-4 · step 159: PASS com 4g, HP 52, nível 6/8 (STABILIZE).
- Jogador 4 · 3-5 · step 167: PASS com 14g, HP 52, nível 6/8 (STABILIZE).
- Jogador 4 · 3-6 · step 180: PASS com 23g, HP 41, nível 6/8 (STABILIZE).
- Jogador 4 · 3-7 · step 186: PASS com 28g, HP 41, nível 6/8 (STABILIZE).
- Jogador 4 · 4-1 · step 200: PASS com 37g, HP 41, nível 6/8 (STABILIZE).
- Jogador 4 · 4-2 · step 208: PASS com 43g, HP 27, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 219: PASS com 53g, HP 16, nível 6/8 (ALL_IN).
- Jogador 4 · 4-4 · step 227: REROLL com 61g, HP 2, nível 7/8 (ALL_IN).
- Jogador 4 · 4-5 · step 238: PASS com 67g, HP 2, nível 7/8 (ALL_IN).
| Jogador 5 | 6 | 4 |
- Jogador 5 · 3-3 · step 150: PASS com 20g, HP 90, nível 6/8 (STABILIZE).
- Jogador 5 · 3-7 · step 189: REROLL com 49g, HP 55, nível 6/8 (STABILIZE).
- Jogador 5 · 4-5 · step 238: REROLL com 103g, HP 22, nível 6/8 (ALL_IN).
- Jogador 5 · 4-6 · step 248: REROLL com 113g, HP 9, nível 6/8 (ALL_IN).
| Jogador 6 | 14 | 4 |
- Jogador 6 · 4-3 · step 219: PASS com 11g, HP 42, nível 7/8 (STABILIZE).
- Jogador 6 · 4-4 · step 229: PASS com 18g, HP 42, nível 7/8 (STABILIZE).
- Jogador 6 · 5-2 · step 278: REROLL com 68g, HP 27, nível 7/8 (STABILIZE).
- Jogador 6 · 5-3 · step 288: REROLL com 77g, HP 9, nível 7/8 (ALL_IN).
| Jogador 7 | 12 | 6 |
- Jogador 7 · 4-1 · step 200: PASS com 7g, HP 56, nível 7/8 (STABILIZE).
- Jogador 7 · 4-2 · step 209: PASS com 14g, HP 56, nível 7/8 (STABILIZE).
- Jogador 7 · 4-3 · step 218: PASS com 20g, HP 44, nível 7/8 (STABILIZE).
- Jogador 7 · 4-4 · step 229: PASS com 28g, HP 44, nível 7/8 (STABILIZE).
- Jogador 7 · 4-5 · step 240: PASS com 34g, HP 44, nível 7/8 (STABILIZE).
- Jogador 7 · 4-7 · step 256: PASS com 45g, HP 44, nível 7/8 (STABILIZE).
| Jogador 8 | 1 | 2 |
- Jogador 8 · 3-1 · step 127: PASS com 29g, HP 75, nível 5/8 (STABILIZE).
- Jogador 8 · 3-2 · step 140: PASS com 31g, HP 65, nível 5/8 (STABILIZE).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 2 | 2 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 264 | 56 | 42 | 166 | 0.0031 | 0.2117 | 0.0018 | 0.2636 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0263 (65 ações), BUY_XP: Δ 0.0040 (49 ações), CRAFT_AND_EQUIP: Δ 0.0026 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (9 ações), MOVE_BENCH: Δ 0.0039 (20 ações), MOVE_BOARD: Δ 0.0251 (64 ações), PASS: Δ 0.0000 (24 ações), SELL: Δ 0.0236 (26 ações)
| Jogador 2 | 305 | 46 | 38 | 221 | 0.0037 | 0.5418 | 0.0024 | 0.3881 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0073 (117 ações), BUY_XP: Δ 0.0050 (21 ações), CRAFT_AND_EQUIP: Δ 0.0155 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (7 ações), MOVE_BENCH: Δ 0.0092 (18 ações), MOVE_BOARD: Δ 0.0254 (42 ações), PASS: Δ 0.0000 (12 ações), SELL: Δ 0.0067 (81 ações)
| Jogador 3 | 269 | 45 | 46 | 178 | 0.0021 | 0.6299 | 0.0012 | 0.3110 | 0.0009 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0206 (106 ações), BUY_XP: Δ 0.0019 (8 ações), CRAFT_AND_EQUIP: Δ 0.0109 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0031 (28 ações), MOVE_BOARD: Δ 0.0573 (33 ações), PASS: Δ 0.0000 (16 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0125 (68 ações)
| Jogador 4 | 162 | 42 | 32 | 88 | 0.0001 | -0.0442 | -0.0009 | 0.3668 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0168 (49 ações), BUY_XP: Δ 0.0135 (8 ações), CRAFT_AND_EQUIP: Δ 0.0028 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0008 (3 ações), MOVE_BENCH: Δ 0.0212 (36 ações), MOVE_BOARD: Δ -0.0184 (19 ações), PASS: Δ 0.0000 (18 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0134 (23 ações)
| Jogador 5 | 186 | 23 | 22 | 141 | 0.0012 | -0.1451 | -0.0007 | 0.3286 | 0.0020 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0133 (84 ações), BUY_XP: Δ 0.0162 (6 ações), CRAFT_AND_EQUIP: Δ 0.0835 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.2075 (2 ações), MOVE_BENCH: Δ -0.0564 (11 ações), MOVE_BOARD: Δ 0.0714 (7 ações), PASS: Δ 0.0000 (8 ações), REROLL: Δ 0.0000 (3 ações), SELL: Δ 0.0090 (60 ações)
| Jogador 6 | 206 | 34 | 27 | 145 | -0.0011 | -0.7031 | -0.0022 | 0.4401 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0122 (71 ações), BUY_XP: Δ 0.0046 (14 ações), CRAFT_AND_EQUIP: Δ 0.0295 (7 ações), EQUIP_FROM_INVENTORY: Δ -0.0004 (5 ações), MOVE_BENCH: Δ 0.0210 (15 ações), MOVE_BOARD: Δ -0.0173 (34 ações), PASS: Δ 0.0000 (16 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0155 (42 ações)
| Jogador 7 | 227 | 33 | 35 | 159 | 0.0033 | 0.2802 | 0.0019 | 0.3084 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0063 (78 ações), BUY_XP: Δ 0.0083 (12 ações), CRAFT_AND_EQUIP: Δ 0.0106 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0301 (2 ações), MOVE_BENCH: Δ -0.0106 (9 ações), MOVE_BOARD: Δ 0.0163 (52 ações), PASS: Δ 0.0000 (16 ações), SELL: Δ 0.0048 (51 ações)
| Jogador 8 | 184 | 32 | 31 | 121 | -0.0006 | -0.1736 | -0.0027 | 0.3507 | 0.0022 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0020 (80 ações), BUY_XP: Δ 0.0000 (1 ações), CRAFT_AND_EQUIP: Δ 0.0042 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0054 (3 ações), MOVE_BENCH: Δ 0.0168 (24 ações), MOVE_BOARD: Δ -0.0457 (9 ações), PASS: Δ 0.0000 (6 ações), SELL: Δ 0.0005 (56 ações)
- Jogador 1 — rounds avaliados: 38; correlação estrutural/combate: 0.103; posicional/combate: 0.032.
- Jogador 1 — combate positive: score estrutural prévio 0.253
  score posicional prévio 0.268
- Jogador 1 — combate negative: score estrutural prévio 0.205
  score posicional prévio 0.303
- Jogador 2 — rounds avaliados: 38; correlação estrutural/combate: 0.153; posicional/combate: -0.043.
- Jogador 2 — combate positive: score estrutural prévio 0.631
  score posicional prévio 0.374
- Jogador 2 — combate negative: score estrutural prévio 0.426
  score posicional prévio 0.383
- Jogador 3 — rounds avaliados: 35; correlação estrutural/combate: -0.042; posicional/combate: -0.198.
- Jogador 3 — combate positive: score estrutural prévio 0.567
  score posicional prévio 0.285
- Jogador 3 — combate negative: score estrutural prévio 0.617
  score posicional prévio 0.349
- Jogador 4 — rounds avaliados: 23; correlação estrutural/combate: 0.452; posicional/combate: -0.142.
- Jogador 4 — combate positive: score estrutural prévio 0.190
  score posicional prévio 0.368
- Jogador 4 — combate negative: score estrutural prévio -0.121
  score posicional prévio 0.378
- Jogador 5 — rounds avaliados: 24; correlação estrutural/combate: 0.394; posicional/combate: -0.167.
- Jogador 5 — combate positive: score estrutural prévio -0.018
  score posicional prévio 0.316
- Jogador 5 — combate negative: score estrutural prévio -0.189
  score posicional prévio 0.332
- Jogador 6 — rounds avaliados: 28; correlação estrutural/combate: 0.242; posicional/combate: 0.202.
- Jogador 6 — combate positive: score estrutural prévio -0.550
  score posicional prévio 0.473
- Jogador 6 — combate negative: score estrutural prévio -0.792
  score posicional prévio 0.425
- Jogador 7 — rounds avaliados: 30; correlação estrutural/combate: -0.263; posicional/combate: -0.307.
- Jogador 7 — combate positive: score estrutural prévio 0.185
  score posicional prévio 0.266
- Jogador 7 — combate negative: score estrutural prévio 0.456
  score posicional prévio 0.352
- Jogador 8 — rounds avaliados: 23; correlação estrutural/combate: 0.260; posicional/combate: -0.079.
- Jogador 8 — combate positive: score estrutural prévio 0.007
  score posicional prévio 0.355
- Jogador 8 — combate negative: score estrutural prévio -0.242
  score posicional prévio 0.356

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 302 | OK (302) | 5 | 3 | 0 | 0 | 8 | 3 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Deathblade, TFT_Item_IonicSpark, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_RedBuff, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 342 | OK (342) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 2 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_GargoyleStoneplate, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 303 | OK (303) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_RedBuff, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 184 | OK (184) | 5 | 0 | 0 | 1 | 5 | 3 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 209 | OK (209) | 5 | 0 | 0 | 1 | 5 | 2 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 233 | OK (233) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_JeweledGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 256 | OK (256) | 7 | 0 | 0 | 0 | 7 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 29.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 206 | OK (206) | 5 | 0 | 0 | 1 | 5 | 2 |
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
| Jogador 1 | 2-3 | 9 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 18% → 18% | 10 → 7 | 11 | 5 → 5 | 0.000 | 0.274 |
| Jogador 1 | 2-4 | 8 | 4.000 | -2.000 | 0 → 0 | 3 → 2 | 18% → 18% | 7 → 8 | 8 | 5 → 5 | 0.019 | 0.000 |
| Jogador 1 | 2-5 | 9 | 6.000 | 0.000 | 0 → 0 | 2 → 3 | 18% → 21% | 8 → 8 | 8 | 5 → 6 | 0.058 | 0.317 |
| Jogador 1 | 2-6 | 8 | 4.000 | 8.000 | 0 → 0 | 3 → 2 | 21% → 21% | 8 → 9 | 7 | 6 → 6 | 0.001 | 0.344 |
| Jogador 1 | 2-7 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 18% | 9 → 9 | 10 | 6 → 6 | -0.048 | 0.000 |
| Jogador 1 | 3-1 | 8 | 4.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 21% | 9 → 10 | 11 | 6 → 6 | 0.012 | 0.364 |
| Jogador 1 | 3-2 | 7 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 10 → 11 | 8 | 6 → 6 | -0.059 | 0.402 |
| Jogador 1 | 3-3 | 10 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 21% → 21% | 11 → 9 | 13 | 6 → 6 | 0.098 | 0.272 |
| Jogador 1 | 3-4 | 10 | 0.000 | -6.000 | 0 → 0 | 4 → 4 | 21% → 21% | 9 → 8 | 15 | 6 → 7 | 0.005 | 0.000 |
| Jogador 1 | 3-5 | 10 | 4.000 | 0.000 | 0 → 0 | 4 → 3 | 21% → 25% | 8 → 9 | 8 | 7 → 7 | -0.133 | 0.300 |
| Jogador 1 | 3-6 | 7 | 0.000 | 14.000 | 0 → 0 | 3 → 4 | 25% → 25% | 9 → 11 | 7 | 7 → 7 | 0.079 | 0.441 |
| Jogador 1 | 3-7 | 6 | 0.000 | -2.000 | 0 → 0 | 4 → 5 | 25% → 25% | 11 → 22 | 3 | 7 → 7 | -0.053 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 2.000 | 0 → 0 | 5 → 6 | 25% → 25% | 22 → 32 | 3 | 7 → 7 | 0.117 | 0.298 |
| Jogador 1 | 4-2 | 10 | 0.000 | -2.000 | 0 → 0 | 6 → 5 | 25% → 25% | 32 → 45 | 4 | 7 → 7 | -0.008 | 0.308 |
| Jogador 1 | 4-3 | 10 | 4.000 | -6.000 | 0 → 0 | 5 → 4 | 25% → 25% | 45 → 55 | 12 | 7 → 7 | -0.090 | 0.314 |
| Jogador 1 | 4-4 | 7 | 0.000 | 12.000 | 0 → 0 | 4 → 4 | 25% → 25% | 55 → 61 | 6 | 7 → 7 | 0.001 | 0.000 |
| Jogador 1 | 4-5 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 61 → 70 | 7 | 7 → 7 | 0.024 | -0.271 |
| Jogador 1 | 4-6 | 10 | -4.000 | 0.000 | 0 → 0 | 4 → 2 | 25% → 21% | 70 → 57 | 26 | 7 → 8 | -0.013 | 0.276 |
| Jogador 1 | 4-7 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 57 → 28 | 36 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 10 | -4.000 | -2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 28 → 34 | 14 | 8 → 8 | 0.049 | -0.280 |
| Jogador 1 | 5-2 | 8 | 14.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 29% | 34 → 35 | 7 | 8 → 8 | 0.004 | 0.393 |
| Jogador 1 | 5-3 | 10 | -4.000 | 2.000 | 0 → 0 | 4 → 4 | 29% → 25% | 35 → 41 | 12 | 8 → 8 | -0.020 | 0.301 |
| Jogador 1 | 5-4 | 10 | 2.000 | -10.000 | 0 → 0 | 4 → 5 | 25% → 29% | 41 → 44 | 14 | 8 → 8 | 0.022 | 0.000 |
| Jogador 1 | 5-5 | 6 | 0.000 | 10.000 | 0 → 0 | 5 → 5 | 29% → 29% | 44 → 50 | 5 | 8 → 8 | 0.011 | 0.493 |
| Jogador 1 | 5-6 | 4 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 29% → 29% | 50 → 61 | 0 | 8 → 9 | -0.006 | 0.000 |
| Jogador 1 | 5-7 | 5 | 10.000 | -10.000 | 0 → 0 | 5 → 5 | 29% → 32% | 61 → 72 | 0 | 9 → 9 | 0.001 | 0.000 |
| Jogador 1 | 6-1 | 9 | 0.000 | 12.000 | 0 → 0 | 5 → 5 | 32% → 32% | 72 → 74 | 10 | 9 → 9 | -0.005 | 0.340 |
| Jogador 1 | 6-2 | 10 | -4.000 | 2.000 | 0 → 0 | 5 → 4 | 32% → 25% | 74 → 63 | 25 | 9 → 9 | 0.001 | 0.310 |
| Jogador 1 | 6-3 | 10 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 63 → 38 | 36 | 9 → 10 | 0.000 | 0.309 |
| Jogador 1 | 6-4 | 2 | 16.000 | -16.000 | 0 → 1 | 4 → 4 | 25% → 29% | 38 → 49 | 0 | 10 → 10 | 0.047 | 0.000 |
| Jogador 1 | 6-5 | 7 | 8.000 | 0.000 | 1 → 1 | 4 → 5 | 29% → 32% | 49 → 58 | 4 | 10 → 10 | 0.001 | 0.446 |
| Jogador 1 | 6-6 | 5 | 6.000 | 0.000 | 1 → 1 | 5 → 5 | 32% → 36% | 58 → 56 | 3 | 10 → 10 | 0.008 | 0.629 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 17, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 62 ações e piorou em 44.
- Jogador 1 — estado final: ouro 56, nível 10, vida 73.0, colocação 1.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 9 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.003 | -0.257 |
| Jogador 2 | 2-2 | 8 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.011 | -0.310 |
| Jogador 2 | 2-3 | 4 | 2.000 | 0.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 7 | 5 | 4 → 5 | 0.003 | -0.580 |
| Jogador 2 | 2-4 | 10 | 4.000 | 8.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 7 | 8 | 5 → 5 | 0.023 | 0.000 |
| Jogador 2 | 2-5 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 7 | 13 | 5 → 5 | -0.000 | -0.253 |
| Jogador 2 | 2-6 | 7 | 2.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 21% | 7 → 7 | 7 | 5 → 6 | 0.062 | -0.362 |
| Jogador 2 | 2-7 | 10 | 6.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 10 | 10 | 6 → 6 | -0.001 | 0.000 |
| Jogador 2 | 3-1 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 10 → 10 | 14 | 6 → 6 | 0.001 | -0.263 |
| Jogador 2 | 3-2 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 10 → 9 | 13 | 6 → 6 | 0.000 | 0.281 |
| Jogador 2 | 3-3 | 10 | 0.000 | -6.000 | 1 → 1 | 2 → 3 | 21% → 21% | 9 → 15 | 14 | 6 → 6 | -0.051 | 0.281 |
| Jogador 2 | 3-4 | 10 | 0.000 | 8.000 | 1 → 1 | 3 → 4 | 21% → 21% | 15 → 18 | 6 | 6 → 6 | 0.060 | 0.000 |
| Jogador 2 | 3-5 | 7 | 0.000 | 12.000 | 1 → 1 | 4 → 4 | 21% → 21% | 18 → 20 | 6 | 6 → 6 | 0.005 | 0.395 |
| Jogador 2 | 3-6 | 10 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 20 → 25 | 7 | 6 → 7 | -0.005 | 0.276 |
| Jogador 2 | 3-7 | 10 | 0.000 | -8.000 | 1 → 1 | 4 → 3 | 21% → 21% | 25 → 32 | 17 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 10 | 2.000 | 14.000 | 1 → 1 | 3 → 4 | 21% → 25% | 32 → 25 | 18 | 7 → 7 | 0.006 | 0.288 |
| Jogador 2 | 4-2 | 7 | 0.000 | 4.000 | 1 → 1 | 4 → 3 | 25% → 25% | 25 → 31 | 5 | 7 → 7 | -0.091 | 0.395 |
| Jogador 2 | 4-3 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 25% → 25% | 31 → 42 | 7 | 7 → 7 | 0.038 | -0.285 |
| Jogador 2 | 4-4 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 4 | 25% → 25% | 42 → 51 | 10 | 7 → 7 | 0.001 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 5 | 25% → 25% | 51 → 62 | 8 | 7 → 7 | 0.034 | 0.288 |
| Jogador 2 | 4-6 | 10 | 2.000 | -4.000 | 1 → 1 | 5 → 4 | 25% → 21% | 62 → 73 | 4 | 7 → 7 | -0.039 | -0.258 |
| Jogador 2 | 4-7 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 21% → 21% | 73 → 79 | 10 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 10 | 6.000 | 0.000 | 1 → 1 | 4 → 5 | 21% → 25% | 79 → 86 | 11 | 7 → 7 | -0.006 | 0.000 |
| Jogador 2 | 5-2 | 10 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 25% → 25% | 86 → 95 | 14 | 7 → 7 | 0.000 | 0.296 |
| Jogador 2 | 5-3 | 10 | -2.000 | -2.000 | 1 → 1 | 5 → 4 | 25% → 21% | 95 → 94 | 21 | 7 → 7 | -0.001 | 0.000 |
| Jogador 2 | 5-4 | 10 | 10.000 | -10.000 | 1 → 1 | 4 → 4 | 21% → 25% | 94 → 99 | 11 | 7 → 8 | -0.004 | 0.000 |
| Jogador 2 | 5-5 | 9 | 10.000 | 10.000 | 1 → 1 | 4 → 4 | 25% → 29% | 99 → 99 | 10 | 8 → 8 | -0.052 | -0.311 |
| Jogador 2 | 5-6 | 9 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 29% → 29% | 99 → 109 | 4 | 8 → 8 | 0.063 | 0.334 |
| Jogador 2 | 5-7 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 5 | 29% → 29% | 109 → 120 | 9 | 8 → 8 | 0.049 | 0.000 |
| Jogador 2 | 6-1 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 29% → 29% | 120 → 130 | 11 | 8 → 8 | 0.002 | 0.000 |
| Jogador 2 | 6-2 | 10 | 0.000 | -6.000 | 1 → 1 | 5 → 5 | 29% → 29% | 130 → 143 | 10 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-3 | 10 | 0.000 | 0.000 | 1 → 1 | 5 → 6 | 29% → 29% | 143 → 153 | 14 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-4 | 10 | 0.000 | 10.000 | 1 → 1 | 6 → 6 | 29% → 29% | 153 → 145 | 27 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 10 | -2.000 | -10.000 | 1 → 1 | 6 → 4 | 29% → 29% | 145 → 160 | 11 | 8 → 8 | -0.020 | -0.290 |
| Jogador 2 | 6-6 | 10 | -50.000 | -44.000 | 1 → 0 | 4 → 0 | 29% → 0% | 160 → 156 | 12 | 8 → 8 | -0.125 | -0.295 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 58, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 51 ações e piorou em 40.
- Jogador 2 — estado final: ouro 156, nível 8, vida 3.0, colocação 2.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 8 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.009 | 0.320 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.595 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 8 | 7 | 4 → 5 | 0.006 | 0.502 |
| Jogador 3 | 2-4 | 9 | 6.000 | 2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 8 → 6 | 8 | 5 → 5 | 0.024 | 0.000 |
| Jogador 3 | 2-5 | 4 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 18% → 18% | 6 → 8 | 5 | 5 → 5 | -0.000 | 0.701 |
| Jogador 3 | 2-6 | 10 | 6.000 | -4.000 | 1 → 3 | 3 → 1 | 18% → 18% | 8 → 8 | 9 | 5 → 5 | 0.005 | 0.270 |
| Jogador 3 | 2-7 | 10 | 0.000 | 0.000 | 3 → 3 | 1 → 2 | 18% → 18% | 8 → 11 | 11 | 5 → 6 | 0.003 | 0.000 |
| Jogador 3 | 3-1 | 9 | 2.000 | 6.000 | 3 → 3 | 2 → 3 | 18% → 21% | 11 → 16 | 4 | 6 → 6 | 0.009 | 0.312 |
| Jogador 3 | 3-2 | 8 | 6.000 | 0.000 | 3 → 3 | 3 → 1 | 21% → 21% | 16 → 17 | 5 | 6 → 6 | -0.028 | -0.329 |
| Jogador 3 | 3-3 | 7 | 0.000 | 12.000 | 3 → 3 | 1 → 2 | 21% → 21% | 17 → 18 | 6 | 6 → 6 | 0.073 | 0.419 |
| Jogador 3 | 3-4 | 8 | -2.000 | 4.000 | 3 → 2 | 2 → 3 | 21% → 21% | 18 → 24 | 3 | 6 → 6 | -0.003 | 0.000 |
| Jogador 3 | 3-5 | 9 | 0.000 | 10.000 | 2 → 2 | 3 → 2 | 21% → 21% | 24 → 25 | 10 | 6 → 6 | 0.000 | 0.322 |
| Jogador 3 | 3-6 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 25 → 30 | 12 | 6 → 6 | 0.013 | -0.254 |
| Jogador 3 | 3-7 | 8 | 0.000 | -2.000 | 2 → 2 | 2 → 3 | 21% → 21% | 30 → 41 | 6 | 6 → 6 | 0.017 | 0.000 |
| Jogador 3 | 4-1 | 10 | 2.000 | 4.000 | 2 → 2 | 3 → 3 | 21% → 21% | 41 → 44 | 12 | 6 → 6 | -0.005 | -0.271 |
| Jogador 3 | 4-2 | 10 | 0.000 | -8.000 | 2 → 2 | 3 → 4 | 21% → 21% | 44 → 61 | 9 | 6 → 6 | -0.001 | 0.285 |
| Jogador 3 | 4-3 | 10 | -2.000 | 6.000 | 2 → 2 | 4 → 4 | 21% → 21% | 61 → 71 | 7 | 6 → 6 | -0.001 | 0.298 |
| Jogador 3 | 4-4 | 10 | 0.000 | -8.000 | 2 → 2 | 4 → 4 | 21% → 21% | 71 → 86 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 10 | 0.000 | -4.000 | 2 → 2 | 4 → 4 | 21% → 21% | 86 → 100 | 10 | 6 → 6 | 0.000 | 0.285 |
| Jogador 3 | 4-6 | 10 | 0.000 | 2.000 | 2 → 2 | 4 → 4 | 21% → 21% | 100 → 109 | 11 | 6 → 6 | 0.000 | -0.276 |
| Jogador 3 | 4-7 | 10 | 0.000 | -6.000 | 2 → 2 | 4 → 3 | 21% → 21% | 109 → 121 | 11 | 6 → 7 | 0.005 | 0.000 |
| Jogador 3 | 5-1 | 10 | 6.000 | -6.000 | 2 → 2 | 3 → 4 | 21% → 25% | 121 → 132 | 5 | 7 → 7 | -0.049 | 0.301 |
| Jogador 3 | 5-2 | 10 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 25% → 25% | 132 → 142 | 6 | 7 → 7 | 0.054 | 0.000 |
| Jogador 3 | 5-3 | 10 | -4.000 | 4.000 | 2 → 2 | 4 → 4 | 25% → 21% | 142 → 145 | 19 | 7 → 7 | -0.004 | 0.294 |
| Jogador 3 | 5-4 | 10 | 4.000 | -8.000 | 2 → 2 | 4 → 5 | 21% → 25% | 145 → 158 | 10 | 7 → 7 | -0.004 | 0.000 |
| Jogador 3 | 5-5 | 10 | 0.000 | 12.000 | 2 → 2 | 5 → 5 | 25% → 25% | 158 → 164 | 14 | 7 → 7 | -0.050 | 0.297 |
| Jogador 3 | 5-6 | 10 | 0.000 | -2.000 | 2 → 2 | 5 → 5 | 25% → 25% | 164 → 175 | 9 | 7 → 7 | 0.066 | -0.285 |
| Jogador 3 | 5-7 | 10 | 0.000 | -8.000 | 2 → 2 | 5 → 5 | 25% → 25% | 175 → 189 | 9 | 7 → 7 | -0.006 | 0.000 |
| Jogador 3 | 6-1 | 10 | 0.000 | 0.000 | 2 → 2 | 5 → 6 | 25% → 25% | 189 → 199 | 12 | 7 → 7 | -0.063 | -0.285 |
| Jogador 3 | 6-2 | 10 | -6.000 | 2.000 | 2 → 2 | 6 → 5 | 25% → 21% | 199 → 209 | 12 | 7 → 7 | -0.011 | -0.290 |
| Jogador 3 | 6-3 | 10 | -30.000 | -32.000 | 2 → 0 | 5 → 0 | 21% → 0% | 209 → 206 | 14 | 7 → 7 | -0.062 | -0.290 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 35, COMPOSITION_COMPATIBILITY: 37, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 22; mudanças de composição: 0; posicionamento melhorou em 49 ações e piorou em 48.
- Jogador 3 — estado final: ouro 206, nível 7, vida 5.0, colocação 3.
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
| Jogador 4 | 3-1 | 10 | -4.000 | 10.000 | 0 → 0 | 2 → 3 | 21% → 21% | 9 → 8 | 10 | 6 → 6 | -0.007 | -0.263 |
| Jogador 4 | 3-2 | 10 | 6.000 | 2.000 | 0 → 1 | 3 → 2 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | -0.031 | -0.278 |
| Jogador 4 | 3-3 | 8 | -4.000 | 12.000 | 1 → 1 | 2 → 2 | 21% → 21% | 9 → 10 | 6 | 6 → 6 | -0.024 | -0.329 |
| Jogador 4 | 3-4 | 9 | 4.000 | 8.000 | 1 → 1 | 2 → 3 | 21% → 21% | 10 → 11 | 6 | 6 → 6 | 0.042 | 0.000 |
| Jogador 4 | 3-5 | 7 | 0.000 | -4.000 | 1 → 1 | 3 → 4 | 21% → 21% | 11 → 23 | 2 | 6 → 6 | -0.040 | -0.404 |
| Jogador 4 | 3-6 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 23 → 31 | 8 | 6 → 6 | 0.072 | 0.277 |
| Jogador 4 | 3-7 | 6 | 0.000 | 6.000 | 1 → 1 | 4 → 5 | 21% → 21% | 31 → 35 | 3 | 6 → 6 | -0.157 | 0.000 |
| Jogador 4 | 4-1 | 10 | -4.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 35 → 45 | 1 | 6 → 6 | 0.075 | -0.288 |
| Jogador 4 | 4-2 | 8 | 2.000 | 2.000 | 1 → 0 | 5 → 5 | 21% → 21% | 45 → 53 | 5 | 6 → 6 | -0.108 | -0.334 |
| Jogador 4 | 4-3 | 9 | 4.000 | -2.000 | 0 → 0 | 5 → 6 | 21% → 21% | 53 → 64 | 3 | 6 → 7 | 0.039 | -0.331 |
| Jogador 4 | 4-4 | 10 | 6.000 | 2.000 | 0 → 0 | 6 → 6 | 21% → 25% | 64 → 69 | 11 | 7 → 7 | 0.041 | 0.000 |
| Jogador 4 | 4-5 | 8 | -32.000 | -44.000 | 0 → 0 | 6 → 0 | 25% → 0% | 69 → 67 | 6 | 7 → 7 | -0.067 | -0.334 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 47 ações e piorou em 33.
- Jogador 4 — estado final: ouro 67, nível 7, vida 2.0, colocação 8.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.347 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.628 |
| Jogador 5 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 5 | 11 | 4 → 5 | -0.007 | -0.237 |
| Jogador 5 | 2-4 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 5 → 6 | 11 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 10 | 2.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 6 | 13 | 5 → 6 | -0.006 | 0.269 |
| Jogador 5 | 2-6 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 9 | 7 | 6 → 6 | 0.019 | -0.242 |
| Jogador 5 | 2-7 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 11 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-1 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 1 | 21% → 21% | 11 → 16 | 10 | 6 → 6 | 0.001 | 0.276 |
| Jogador 5 | 3-2 | 10 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 16 → 25 | 9 | 6 → 6 | 0.000 | 0.295 |
| Jogador 5 | 3-3 | 10 | 2.000 | 8.000 | 0 → 0 | 1 → 2 | 21% → 21% | 25 → 27 | 12 | 6 → 6 | 0.001 | -0.276 |
| Jogador 5 | 3-4 | 10 | 0.000 | -8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 27 → 39 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 10 | 0.000 | 8.000 | 0 → 0 | 3 → 2 | 21% → 21% | 39 → 44 | 10 | 6 → 6 | -0.056 | -0.288 |
| Jogador 5 | 3-6 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 44 → 57 | 6 | 6 → 6 | -0.000 | -0.291 |
| Jogador 5 | 3-7 | 10 | 0.000 | 20.000 | 0 → 0 | 2 → 3 | 21% → 21% | 57 → 55 | 15 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 55 → 63 | 9 | 6 → 6 | 0.041 | -0.273 |
| Jogador 5 | 4-2 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 63 → 76 | 8 | 6 → 6 | -0.022 | -0.258 |
| Jogador 5 | 4-3 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 76 → 90 | 7 | 6 → 6 | 0.000 | -0.281 |
| Jogador 5 | 4-4 | 10 | 4.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 90 → 101 | 5 | 6 → 6 | 0.030 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 5 | 21% → 21% | 101 → 111 | 13 | 6 → 6 | 0.000 | -0.285 |
| Jogador 5 | 4-6 | 10 | -22.000 | -42.000 | 0 → 0 | 5 → 0 | 21% → 0% | 111 → 111 | 14 | 6 → 6 | -0.030 | -0.295 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 36, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 12; mudanças de composição: 1; posicionamento melhorou em 25 ações e piorou em 23.
- Jogador 5 — estado final: ouro 111, nível 6, vida 9.0, colocação 6.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.018 | -0.346 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 2 → 3 | 14% → 14% | 9 → 10 | 13 | 5 → 5 | 0.006 | 0.000 |
| Jogador 6 | 2-5 | 10 | 2.000 | -12.000 | 0 → 0 | 3 → 4 | 14% → 18% | 10 → 9 | 14 | 5 → 6 | 0.052 | -0.269 |
| Jogador 6 | 2-6 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 3 | 18% → 18% | 9 → 7 | 14 | 6 → 6 | 0.002 | -0.226 |
| Jogador 6 | 2-7 | 9 | 6.000 | 6.000 | 0 → 0 | 3 → 3 | 18% → 21% | 7 → 8 | 6 | 6 → 6 | -0.055 | 0.000 |
| Jogador 6 | 3-1 | 7 | 4.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | 0.017 | 0.402 |
| Jogador 6 | 3-2 | 10 | -2.000 | -2.000 | 0 → 0 | 3 → 1 | 21% → 18% | 9 → 11 | 6 | 6 → 6 | 0.017 | -0.264 |
| Jogador 6 | 3-3 | 10 | 4.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 21% | 11 → 6 | 14 | 6 → 6 | 0.020 | -0.254 |
| Jogador 6 | 3-4 | 10 | 6.000 | -4.000 | 0 → 0 | 1 → 3 | 21% → 25% | 6 → 7 | 12 | 6 → 7 | -0.008 | 0.000 |
| Jogador 6 | 3-5 | 7 | 0.000 | 12.000 | 0 → 0 | 3 → 3 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | 0.020 | 0.436 |
| Jogador 6 | 3-6 | 7 | 0.000 | 14.000 | 0 → 0 | 3 → 3 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | -0.011 | 0.388 |
| Jogador 6 | 3-7 | 8 | 0.000 | 12.000 | 0 → 0 | 3 → 3 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | 0.014 | 0.000 |
| Jogador 6 | 4-1 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 25% → 25% | 7 → 5 | 12 | 7 → 7 | 0.005 | -0.281 |
| Jogador 6 | 4-2 | 9 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 5 → 9 | 8 | 7 → 7 | -0.007 | 0.326 |
| Jogador 6 | 4-3 | 9 | 0.000 | 0.000 | 0 → 0 | 4 → 5 | 25% → 25% | 9 → 19 | 6 | 7 → 7 | 0.026 | 0.335 |
| Jogador 6 | 4-4 | 9 | 0.000 | -4.000 | 0 → 0 | 5 → 4 | 25% → 25% | 19 → 25 | 7 | 7 → 7 | -0.007 | 0.000 |
| Jogador 6 | 4-5 | 10 | 0.000 | -2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 25 → 37 | 8 | 7 → 7 | 0.007 | 0.306 |
| Jogador 6 | 4-6 | 10 | 0.000 | -24.000 | 0 → 0 | 4 → 4 | 25% → 25% | 37 → 61 | 8 | 7 → 7 | 0.000 | 0.293 |
| Jogador 6 | 4-7 | 10 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 25% → 25% | 61 → 73 | 11 | 7 → 7 | -0.008 | 0.000 |
| Jogador 6 | 5-1 | 10 | -2.000 | 16.000 | 0 → 0 | 4 → 2 | 25% → 21% | 73 → 71 | 12 | 7 → 7 | -0.040 | -0.285 |
| Jogador 6 | 5-2 | 10 | 4.000 | -8.000 | 0 → 0 | 2 → 2 | 21% → 25% | 71 → 85 | 10 | 7 → 7 | 0.000 | -0.295 |
| Jogador 6 | 5-3 | 10 | -30.000 | -26.000 | 0 → 0 | 2 → 0 | 25% → 0% | 85 → 74 | 14 | 7 → 7 | 0.033 | -0.278 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 28, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 38 ações e piorou em 28.
- Jogador 6 — estado final: ouro 74, nível 7, vida 9.0, colocação 5.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 7 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.014 | 0.391 |
| Jogador 7 | 2-2 | 8 | 4.000 | -2.000 | 0 → 0 | 3 → 2 | 14% → 14% | 8 → 8 | 8 | 4 → 4 | 0.000 | -0.283 |
| Jogador 7 | 2-3 | 7 | 2.000 | 6.000 | 0 → 1 | 2 → 2 | 14% → 14% | 8 → 9 | 5 | 4 → 5 | 0.082 | 0.391 |
| Jogador 7 | 2-4 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 14% → 14% | 9 → 8 | 13 | 5 → 5 | -0.074 | 0.000 |
| Jogador 7 | 2-5 | 7 | 6.000 | -2.000 | 1 → 1 | 2 → 1 | 14% → 18% | 8 → 9 | 8 | 5 → 5 | 0.013 | 0.352 |
| Jogador 7 | 2-6 | 10 | 0.000 | -8.000 | 1 → 1 | 1 → 3 | 18% → 18% | 9 → 8 | 16 | 5 → 6 | 0.007 | 0.256 |
| Jogador 7 | 2-7 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 2 | 18% → 18% | 8 → 7 | 13 | 6 → 6 | 0.056 | 0.000 |
| Jogador 7 | 3-1 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 5 | 12 | 6 → 6 | 0.053 | -0.273 |
| Jogador 7 | 3-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 18% → 18% | 5 → 6 | 12 | 6 → 6 | 0.000 | 0.282 |
| Jogador 7 | 3-3 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 18% → 18% | 6 → 7 | 11 | 6 → 6 | 0.000 | -0.254 |
| Jogador 7 | 3-4 | 10 | 2.000 | -2.000 | 1 → 1 | 3 → 3 | 18% → 21% | 7 → 7 | 13 | 6 → 7 | -0.037 | 0.000 |
| Jogador 7 | 3-5 | 8 | 4.000 | 8.000 | 1 → 1 | 3 → 3 | 21% → 25% | 7 → 7 | 6 | 7 → 7 | 0.057 | -0.341 |
| Jogador 7 | 3-6 | 6 | 0.000 | 14.000 | 1 → 1 | 3 → 3 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | -0.055 | -0.430 |
| Jogador 7 | 3-7 | 7 | 0.000 | 8.000 | 1 → 1 | 3 → 4 | 25% → 25% | 6 → 8 | 6 | 7 → 7 | -0.039 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 5 | 25% → 25% | 8 → 13 | 6 | 7 → 7 | 0.001 | 0.304 |
| Jogador 7 | 4-2 | 9 | 0.000 | -2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 13 → 20 | 4 | 7 → 7 | -0.015 | -0.307 |
| Jogador 7 | 4-3 | 8 | 0.000 | 0.000 | 1 → 1 | 5 → 4 | 25% → 25% | 20 → 28 | 6 | 7 → 7 | 0.000 | 0.367 |
| Jogador 7 | 4-4 | 9 | 0.000 | 0.000 | 1 → 1 | 4 → 5 | 25% → 25% | 28 → 35 | 6 | 7 → 7 | 0.100 | 0.000 |
| Jogador 7 | 4-5 | 10 | 0.000 | 2.000 | 1 → 1 | 5 → 5 | 25% → 25% | 35 → 44 | 9 | 7 → 7 | -0.004 | 0.301 |
| Jogador 7 | 4-6 | 10 | 2.000 | 0.000 | 1 → 2 | 5 → 3 | 25% → 25% | 44 → 50 | 7 | 7 → 7 | -0.082 | 0.311 |
| Jogador 7 | 4-7 | 6 | 0.000 | 10.000 | 2 → 2 | 3 → 4 | 25% → 25% | 50 → 55 | 5 | 7 → 7 | -0.004 | 0.000 |
| Jogador 7 | 5-1 | 10 | 0.000 | -4.000 | 2 → 2 | 4 → 4 | 25% → 25% | 55 → 71 | 7 | 7 → 7 | 0.040 | 0.296 |
| Jogador 7 | 5-2 | 10 | 0.000 | -6.000 | 2 → 2 | 4 → 5 | 25% → 25% | 71 → 84 | 7 | 7 → 7 | 0.030 | -0.280 |
| Jogador 7 | 5-3 | 10 | 0.000 | 2.000 | 2 → 2 | 5 → 5 | 25% → 25% | 84 → 94 | 7 | 7 → 7 | -0.013 | -0.285 |
| Jogador 7 | 5-4 | 10 | 0.000 | 4.000 | 2 → 2 | 5 → 5 | 25% → 25% | 94 → 102 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 10 | -28.000 | -52.000 | 2 → 0 | 5 → 0 | 25% → 0% | 102 → 102 | 10 | 7 → 7 | -0.097 | -0.280 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 32, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 38 ações e piorou em 37.
- Jogador 7 — estado final: ouro 102, nível 7, vida 16.0, colocação 4.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 9 | 6.000 | 0.000 | 0 → 2 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.002 | -0.287 |
| Jogador 8 | 2-2 | 8 | 0.000 | 10.000 | 2 → 1 | 0 → 0 | 14% → 14% | 6 → 7 | 6 | 4 → 4 | 0.002 | -0.296 |
| Jogador 8 | 2-3 | 10 | 2.000 | 4.000 | 1 → 2 | 0 → 0 | 14% → 14% | 7 → 6 | 10 | 4 → 5 | 0.008 | -0.269 |
| Jogador 8 | 2-4 | 10 | 4.000 | 8.000 | 2 → 2 | 0 → 0 | 14% → 18% | 6 → 6 | 8 | 5 → 5 | 0.009 | 0.000 |
| Jogador 8 | 2-5 | 10 | 0.000 | -12.000 | 2 → 2 | 0 → 2 | 18% → 18% | 6 → 19 | 8 | 5 → 5 | -0.022 | -0.264 |
| Jogador 8 | 2-6 | 10 | 0.000 | 2.000 | 2 → 2 | 2 → 2 | 18% → 18% | 19 → 25 | 7 | 5 → 5 | 0.036 | 0.238 |
| Jogador 8 | 2-7 | 10 | 0.000 | -6.000 | 2 → 2 | 2 → 2 | 18% → 18% | 25 → 35 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 7 | 2.000 | 10.000 | 2 → 2 | 2 → 2 | 18% → 18% | 35 → 36 | 6 | 5 → 5 | -0.047 | -0.369 |
| Jogador 8 | 3-2 | 10 | -2.000 | 12.000 | 2 → 1 | 2 → 2 | 18% → 18% | 36 → 40 | 5 | 5 → 5 | 0.053 | -0.263 |
| Jogador 8 | 3-3 | 10 | 0.000 | -18.000 | 1 → 1 | 2 → 2 | 18% → 18% | 40 → 61 | 4 | 5 → 5 | 0.006 | 0.272 |
| Jogador 8 | 3-4 | 10 | 0.000 | -12.000 | 1 → 1 | 2 → 0 | 18% → 18% | 61 → 77 | 5 | 5 → 5 | -0.022 | 0.000 |
| Jogador 8 | 3-5 | 10 | 0.000 | 4.000 | 1 → 1 | 0 → 1 | 18% → 18% | 77 → 85 | 10 | 5 → 5 | -0.000 | -0.258 |
| Jogador 8 | 3-6 | 10 | 0.000 | -2.000 | 1 → 1 | 1 → 1 | 18% → 18% | 85 → 97 | 10 | 5 → 6 | 0.005 | -0.259 |
| Jogador 8 | 3-7 | 10 | 4.000 | 16.000 | 1 → 1 | 1 → 1 | 18% → 21% | 97 → 98 | 10 | 6 → 6 | 0.012 | 0.000 |
| Jogador 8 | 4-1 | 10 | 0.000 | 14.000 | 1 → 1 | 1 → 2 | 21% → 21% | 98 → 102 | 9 | 6 → 6 | 0.000 | 0.290 |
| Jogador 8 | 4-2 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 4 | 21% → 21% | 102 → 111 | 12 | 6 → 6 | 0.000 | -0.291 |
| Jogador 8 | 4-3 | 10 | 0.000 | -8.000 | 1 → 1 | 4 → 4 | 21% → 21% | 111 → 126 | 10 | 6 → 6 | 0.000 | -0.276 |
| Jogador 8 | 4-4 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 126 → 136 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 10 | -22.000 | -32.000 | 1 → 0 | 4 → 0 | 21% → 0% | 136 → 132 | 8 | 6 → 6 | -0.042 | -0.290 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 28, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 36 ações e piorou em 32.
- Jogador 8 — estado final: ouro 132, nível 6, vida 12.0, colocação 7.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 65 | 26 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 2 | 0 | 0 |
| Jogador 2 | 117 | 81 | 5 | 5 | 6 | 1 | 0 | 0 | 32 | 6 | 1 | 0 |
| Jogador 3 | 106 | 68 | 0 | 0 | 0 | 0 | 0 | 0 | 39 | 0 | 1 | 0 |
| Jogador 4 | 49 | 23 | 0 | 0 | 0 | 1 | 1 | 0 | 4 | 4 | 0 | 0 |
| Jogador 5 | 84 | 60 | 7 | 9 | 12 | 2 | 2 | 3 | 17 | 1 | 1 | 0 |
| Jogador 6 | 71 | 42 | 2 | 2 | 2 | 1 | 0 | 2 | 4 | 1 | 1 | 0 |
| Jogador 7 | 78 | 51 | 1 | 3 | 3 | 0 | 1 | 0 | 12 | 6 | 1 | 0 |
| Jogador 8 | 80 | 56 | 3 | 6 | 7 | 1 | 0 | 0 | 9 | 2 | 3 | 0 |
- Jogador 1 — venda DA_18_Rakan (2-7, step 117): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Akali_AD (3-1, step 126): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 1 — venda DA_18_Shen (3-7, step 182): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Alistar (4-2, step 202): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Azir (4-2, step 204): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_KogMaw18_AD (5-3, step 283): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 2 — venda DA_18_Warwick (3-7, step 188): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rengar (4-5, step 236): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Rakan (4-6, step 244): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_Soraka (6-5, step 374): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_18_RekSai (3-5, step 162): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_Scuttlecrab18 (3-6, step 177): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_Vi18 (3-7, step 182): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Rengar (4-6, step 247): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Rengar (4-6, step 249): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_KhaZix (5-2, step 274): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Rengar (5-4, step 296): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Rakan (2-5, step 98): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Rakan (2-7, step 116): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_Tristana (3-2, step 136): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Kobuko (3-4, step 159): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-5, step 168): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_CrimsonRaptor18 (4-6, step 246): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Yorick (2-6, step 108): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Sentry (3-2, step 138): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Rakan (3-3, step 148): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 6 — venda DA_KogMaw18_AD (4-7, step 255): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Fiddlesticks18 (5-2, step 279): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 7 — venda DA_18_Camille (2-5, step 95): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_18_Rakan (2-7, step 118): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_Murkwolf18 (4-2, step 204): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rengar (4-3, step 212): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Diana (4-5, step 234): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (5-1, step 264): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Tristana (2-7, step 119): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Akali_AD (3-3, step 150): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_Karma18 (3-4, step 154): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Kobuko (3-4, step 159): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Warwick (3-4, step 160): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_LeBlanc (3-5, step 168): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Elise (3-6, step 179): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (3-6, step 180): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Elise (4-4, step 227): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (4-5, step 237): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **6**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-7 | 117 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 3-7 | 182 | SOLD_CORE_UNIT | Venda de 'DA_18_Shen' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-2 | 202 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-2 | 204 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Azir' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 68 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 69 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-4 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-5 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-6 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 253 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 254 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 255 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 256 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 257 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 258 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 259 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 260 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 4-7 | 261 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 262 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 263 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 264 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 265 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 266 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 516 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 744 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-5 | 867 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-6 | 974 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 975 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 2-7 | 1113 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-7 | 1114 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-1 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1319 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-2 | 1320 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1455 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-3 | 1456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1585 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-4 | 1586 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1719 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-5 | 1720 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1819 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-6 | 1820 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1907 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 1908 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2050 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-1 | 2051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2188 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-2 | 2189 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 2327 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-3 | 2328 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2425 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-4 | 2426 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2560 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2561 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 2691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-6 | 2692 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 2817 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-7 | 2818 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 2954 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 3063 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 3206 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-4 | 3342 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-4 | 3343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-5 | 3432 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 5-5 | 3433 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-6 | 3494 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-7 | 3573 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-1 | 3702 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-1 | 3703 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-2 | 3838 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-2 | 3839 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-3 | 3965 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-3 | 3966 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-4 | 4004 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 6-4 | 4005 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-5 | 4110 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-6 | 4189 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| MEDIUM | Jogador 1 | 3-6 | 1884 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-1 | 2165 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-5 | 2668 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2717 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2728 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2739 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2750 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2761 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2772 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2783 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-6 | 2794 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 4-7 | 2931 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-2 | 3183 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-3 | 3285 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-3 | 3296 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 1 | 5-3 | 3307 | ECON_NON_UNIT_SPEND_BELOW_50_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 2-5 | 96 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-5 | 98 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Leona) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-7 | 118 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 3-1 | 126 | PURCHASE_SALE_REVIEW | Compra de DA_18_Teemo foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 3-2 | 138 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-2 | 140 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-4 | 155 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 3-7 | 188 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-5 | 236 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 220 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 230 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 240 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 283 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 284 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 285 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 286 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 287 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 288 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 289 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 290 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-3 | 291 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 292 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 293 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 294 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 295 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 296 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 297 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 298 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 299 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 300 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-4 | 301 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 302 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 303 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 304 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 305 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 306 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 307 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 308 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 309 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-5 | 311 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 312 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 313 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 314 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 315 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 316 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 317 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 318 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 319 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-6 | 321 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 322 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 323 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 324 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 325 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 326 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 327 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 328 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 329 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 330 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 5-7 | 331 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 332 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 333 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 334 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 335 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 336 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 337 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 338 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 339 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 340 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-1 | 341 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 342 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 343 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 344 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 345 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 346 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 347 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 348 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 349 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 350 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-2 | 351 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-3 | 352 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 2 | 6-6 | 382 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 383 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 384 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 385 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 386 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 387 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 388 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 389 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 390 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 6-6 | 391 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-7 | 1123 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-1 | 1258 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-2 | 1390 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-3 | 1527 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-4 | 1662 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-5 | 1763 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-6 | 1900 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 3-7 | 2037 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-1 | 2172 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-2 | 2275 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-3 | 2413 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 2414 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2554 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2555 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3107 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3245 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3378 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-4 | 3515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-5 | 3639 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-5 | 3640 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-6 | 3770 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-7 | 3910 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-1 | 4047 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-2 | 4183 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-3 | 4321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-4 | 4454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-5 | 4595 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 6-6 | 4734 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 6-6 | 4735 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 3-3 | 1639 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-4 | 1740 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-1 | 2252 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-4 | 2670 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 5-4 | 3616 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 3 | 2-7 | 118 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yorick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 3 | 3-6 | 177 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 3-7 | 182 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 4-6 | 247 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 4-6 | 249 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-2 | 274 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-4 | 296 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 4-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 4-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 334 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 6-1 | 335 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-1 | 450 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-2 | 512 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-3 | 582 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-4 | 700 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 758 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 889 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1021 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1143 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1254 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 1963 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-2 | 2098 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-4 | 3320 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-5 | 3456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-6 | 3596 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-7 | 3731 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-1 | 3871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-2 | 4008 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-3 | 4148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 6-3 | 4149 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 3-1 | 1231 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-2 | 1327 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-3 | 1435 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-4 | 1557 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 3-6 | 1806 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 3 | 4-2 | 2207 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-1 | 1225 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1368 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-2 | 1369 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1478 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-3 | 1479 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 1600 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-5 | 1696 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1828 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1913 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-7 | 1914 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 2053 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2165 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-2 | 2166 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2297 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-3 | 2298 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 2438 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 4-4 | 2439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 2550 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-5 | 2551 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 3-4 | 1672 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-5 | 1805 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-6 | 1890 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-7 | 2030 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-1 | 2142 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-4 | 87 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Caitlyn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Camille) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-6 | 107 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Elise) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 118 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 2-7 | 119 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Scuttlecrab18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-1 | 129 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 136 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 138 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Shen) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-2 | 140 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-4 | 156 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-4 | 158 | PURCHASE_SALE_REVIEW | Compra de DA_18_Alistar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 5 | 3-4 | 159 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 3-5 | 168 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-6 | 178 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 4 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 186 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Scuttlecrab18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 5 | 3-7 | 188 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 5 | 4-6 | 246 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 59 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 60 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 3-5 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 4-2 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 690 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-5 | 823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-6 | 957 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-7 | 1092 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-1 | 1227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-2 | 1360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-3 | 1494 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-4 | 1627 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-5 | 1766 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-6 | 1902 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 3-7 | 2037 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-1 | 2173 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 2309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 2444 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 2585 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 2723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-6 | 2860 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 4-6 | 2861 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 3-2 | 1471 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 6 | 2-3 | 76 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 2-5 | 100 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Cinderling18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 2-6 | 108 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 3-2 | 138 | SOLD_CORE_UNIT | Venda de 'DA_18_Sentry' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 3-4 | 156 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Murkwolf18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| HIGH | Jogador 6 | 4-7 | 255 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 6 | 2-6 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 3-7 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 4-2 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-2 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-3 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 226 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 227 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 228 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 229 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-4 | 231 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 232 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 233 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 234 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 235 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 236 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 237 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 238 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 239 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 240 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-5 | 241 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 242 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 243 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 244 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 245 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 246 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 247 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 248 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 249 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 250 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-6 | 251 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 4-7 | 252 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
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
| LOW | Jogador 6 | 2-6 | 952 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1072 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1169 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1308 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1309 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-3 | 1442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1443 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-4 | 1577 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1578 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 3-5 | 1678 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1774 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1882 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 2014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 2257 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 2380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 2525 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 2667 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 2809 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 2950 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 3087 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 3226 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-3 | 3227 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 4-2 | 2234 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-3 | 2357 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 7 | 2-4 | 89 | PURCHASE_SALE_REVIEW | Compra de DA_Scuttlecrab18 foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 7 | 2-7 | 118 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-2 | 136 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Ornn) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 3-3 | 146 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Gromp18_AP) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 3-3 | 150 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 7 | 4-2 | 204 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-3 | 212 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 4-5 | 234 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-1 | 264 | SOLD_CORE_UNIT | Venda de 'DA_18_Hecarim' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
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
| LOW | Jogador 7 | 3-1 | 1292 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1425 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1561 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1695 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1807 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 3-7 | 1992 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 2130 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-1 | 2131 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2257 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 2370 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 2371 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2499 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2643 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 2789 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2879 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 3022 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 3167 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 3592 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 5-5 | 3593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 4-1 | 2234 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-2 | 2347 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-3 | 2476 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-4 | 2620 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-6 | 2856 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 46 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 2-6 | 106 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_RekSai) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Varus) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 116 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Vi18) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 118 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Akali_AD) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 2-7 | 119 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 3-3 | 149 | PURCHASE_SALE_REVIEW | Compra de DA_18_LeBlanc foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-3 | 150 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 3-4 | 154 | SOLD_CORE_UNIT | Venda de 'DA_Karma18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-4 | 157 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_CrimsonRaptor18) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-4 | 159 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-4 | 160 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-5 | 166 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Yunara) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 8 | 3-5 | 168 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_LeBlanc' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-6 | 176 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Malphite) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 8 | 3-6 | 178 | PURCHASE_SALE_REVIEW | Compra de DA_18_Hecarim foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 8 | 3-6 | 179 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-6 | 180 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 4-4 | 227 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 4-5 | 237 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 445 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 824 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 958 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 1095 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1232 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1329 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1330 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1465 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1466 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1605 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1606 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1744 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1745 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 1883 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1884 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 2021 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 2022 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2156 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 2157 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2294 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 2295 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2433 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 2434 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2569 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 2570 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2708 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 2709 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2853 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 4-5 | 2854 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-7 | 1306 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-1 | 1442 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
