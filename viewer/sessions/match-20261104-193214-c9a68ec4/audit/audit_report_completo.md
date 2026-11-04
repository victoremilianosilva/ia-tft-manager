# Auditoria da partida TFT

- Arquivos lidos: **16**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5704**
- Achados: **279**
- CRITICAL: 0 | HIGH: 16 | MEDIUM: 58 | LOW: 205

## Metadados da sessão

- Match ID: c9a68ec4-4d13-416d-afca-f42eca388209
- Seed: 20261016 | Engine: cpp | Política determinística: True
- Checkpoint SHA-256: e827f464e234eb812733bb6b9e0aca7965612c6e53b5f869c707567a2f261f0c
- Policy: TFTPolicy | Observation dim: 7237 | Action dims: [9, 5, 9, 28, 28, 28]
- Sidecars estruturados descobertos: 8

- Decisões analisadas enquanto os jogadores estavam vivos: **4787**
- Entradas posteriores à eliminação ignoradas: **917**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Revisão prioritária — jogadores 4, 6 e 7

| Jogador | Ouro final | Nível final | XP purchases | Janelas XP/stabilização | Compras com valor identificado | Vendas para revisar | Vendas compensadas | Componentes sem craft observado | Bigornas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 4 | 1 | 6 | 0 | 48 | 58 | 1 | 1 | não/inconclusivo | 0 |
| Jogador 6 | 211 | 7 | 5 | 56 | 72 | 4 | 1 | não/inconclusivo | 0 |
| Jogador 7 | 72 | 6 | 0 | 39 | 45 | 1 | 2 | não/inconclusivo | 0 |

A tabela prioriza a inspeção desses três jogadores; as tabelas completas abaixo continuam incluindo os oito participantes.

## Reconstrução de decisões dos logs legados

Esta seção usa o que está explícito em cada linha de ação. HP, nível, máscara legal e canais separados de recompensa não são inferidos quando o log não os registra.

| Jogador | Ações | Compras | Vendas | XP | Rerolls | Passes | Movimentos | Δ recompensa média | Mudanças comp/foco | Warnings posicionamento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 200 | 48 | 8 | 0 | 34 | 21 | 79 | 0.1118 | 20 | 17 |
- Jogador 1 — ações por estratégia: ALL_IN::BUY: 1, ALL_IN::MOVE_BENCH: 3, ALL_IN::MOVE_BOARD: 2, ALL_IN::PASS: 1, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 3, FAST8::PASS: 1, STABILIZE::BUY: 47, STABILIZE::ITEM: 10, STABILIZE::MOVE_BENCH: 42, STABILIZE::MOVE_BOARD: 28, STABILIZE::PASS: 19, STABILIZE::REROLL: 34, STABILIZE::SELL: 8
- Jogador 1 — recompensas por ação: BUY: média 0.6290 (n=48), ITEM: média 0.1760 (n=10), MOVE_BENCH: média -0.0130 (n=46), MOVE_BOARD: média -0.0188 (n=33), PASS: média -0.0086 (n=21), REROLL: média -0.1665 (n=34), SELL: média -0.3162 (n=8)
| Jogador 2 | 228 | 64 | 24 | 0 | 30 | 23 | 78 | 0.0881 | 18 | 28 |
- Jogador 2 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::MOVE_BENCH: 4, ALL_IN::REROLL: 5, ALL_IN::SELL: 4, FAST8::BUY: 1, FAST8::MOVE_BENCH: 1, FAST8::MOVE_BOARD: 3, FAST8::PASS: 2, STABILIZE::BUY: 59, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 48, STABILIZE::MOVE_BOARD: 22, STABILIZE::PASS: 21, STABILIZE::REROLL: 25, STABILIZE::SELL: 20
- Jogador 2 — recompensas por ação: BUY: média 0.5273 (n=64), ITEM: média 0.1800 (n=9), MOVE_BENCH: média -0.1055 (n=53), MOVE_BOARD: média 0.0100 (n=25), PASS: média -0.0383 (n=23), REROLL: média -0.1427 (n=30), SELL: média -0.1996 (n=24)
| Jogador 3 | 294 | 65 | 23 | 0 | 29 | 36 | 126 | 0.0483 | 15 | 36 |
- Jogador 3 — ações por estratégia: FAST8::BUY: 17, FAST8::ITEM: 6, FAST8::MOVE_BENCH: 58, FAST8::MOVE_BOARD: 19, FAST8::PASS: 17, FAST8::SELL: 8, STABILIZE::BUY: 48, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 29, STABILIZE::MOVE_BOARD: 20, STABILIZE::PASS: 19, STABILIZE::REROLL: 29, STABILIZE::SELL: 15
- Jogador 3 — recompensas por ação: BUY: média 0.5674 (n=65), ITEM: média 0.1193 (n=15), MOVE_BENCH: média -0.1186 (n=87), MOVE_BOARD: média -0.0051 (n=39), PASS: média -0.0714 (n=36), REROLL: média -0.1924 (n=29), SELL: média -0.2517 (n=23)
| Jogador 4 | 234 | 58 | 12 | 0 | 51 | 25 | 77 | 0.1062 | 19 | 29 |
- Jogador 4 — ações por estratégia: ALL_IN::BUY: 7, ALL_IN::ITEM: 2, ALL_IN::MOVE_BOARD: 7, ALL_IN::PASS: 3, ALL_IN::REROLL: 4, STABILIZE::BUY: 51, STABILIZE::ITEM: 9, STABILIZE::MOVE_BENCH: 41, STABILIZE::MOVE_BOARD: 29, STABILIZE::PASS: 22, STABILIZE::REROLL: 47, STABILIZE::SELL: 12
- Jogador 4 — recompensas por ação: BUY: média 0.5998 (n=58), ITEM: média 0.1636 (n=11), MOVE_BENCH: média -0.0049 (n=41), MOVE_BOARD: média -0.0142 (n=36), PASS: média -0.0060 (n=25), REROLL: média -0.1653 (n=51), SELL: média -0.2042 (n=12)
| Jogador 5 | 249 | 71 | 28 | 0 | 48 | 23 | 72 | 0.1006 | 19 | 10 |
- Jogador 5 — ações por estratégia: ALL_IN::BUY: 4, ALL_IN::REROLL: 1, ALL_IN::SELL: 3, FAST8::BUY: 1, FAST8::MOVE_BENCH: 7, FAST8::PASS: 1, STABILIZE::BUY: 66, STABILIZE::ITEM: 7, STABILIZE::MOVE_BENCH: 31, STABILIZE::MOVE_BOARD: 34, STABILIZE::PASS: 22, STABILIZE::REROLL: 47, STABILIZE::SELL: 25
- Jogador 5 — recompensas por ação: BUY: média 0.5292 (n=71), ITEM: média 0.1743 (n=7), MOVE_BENCH: média 0.0018 (n=38), MOVE_BOARD: média -0.0129 (n=34), PASS: média -0.0096 (n=23), REROLL: média -0.1512 (n=48), SELL: média -0.2107 (n=28)
| Jogador 6 | 319 | 72 | 23 | 5 | 33 | 36 | 135 | 0.0703 | 15 | 28 |
- Jogador 6 — ações por estratégia: ALL_IN::MOVE_BENCH: 6, ALL_IN::PASS: 1, FAST8::BUY: 14, FAST8::BUY_XP: 5, FAST8::ITEM: 7, FAST8::MOVE_BENCH: 38, FAST8::MOVE_BOARD: 26, FAST8::OTHER: 1, FAST8::PASS: 14, FAST8::SELL: 3, STABILIZE::BUY: 58, STABILIZE::ITEM: 6, STABILIZE::MOVE_BENCH: 44, STABILIZE::MOVE_BOARD: 21, STABILIZE::OTHER: 1, STABILIZE::PASS: 21, STABILIZE::REROLL: 33, STABILIZE::SELL: 20
- Jogador 6 — recompensas por ação: BUY: média 0.5926 (n=72), BUY_XP: média 0.0200 (n=5), ITEM: média 0.1431 (n=13), MOVE_BENCH: média -0.0765 (n=88), MOVE_BOARD: média -0.0060 (n=47), OTHER: média -0.0200 (n=2), PASS: média -0.1069 (n=36), REROLL: média -0.1806 (n=33), SELL: média -0.2326 (n=23)
| Jogador 7 | 183 | 45 | 7 | 0 | 26 | 21 | 76 | 0.1175 | 7 | 23 |
- Jogador 7 — ações por estratégia: ALL_IN::BUY: 8, ALL_IN::MOVE_BENCH: 1, ALL_IN::REROLL: 8, ALL_IN::SELL: 2, STABILIZE::BUY: 37, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 50, STABILIZE::MOVE_BOARD: 25, STABILIZE::PASS: 21, STABILIZE::REROLL: 18, STABILIZE::SELL: 5
- Jogador 7 — recompensas por ação: BUY: média 0.6651 (n=45), ITEM: média 0.1575 (n=8), MOVE_BENCH: média -0.0541 (n=51), MOVE_BOARD: média -0.0204 (n=25), PASS: média -0.0543 (n=21), REROLL: média -0.1350 (n=26), SELL: média -0.2529 (n=7)
| Jogador 8 | 257 | 53 | 19 | 0 | 17 | 33 | 124 | 0.0328 | 22 | 34 |
- Jogador 8 — ações por estratégia: FAST8::BUY: 8, FAST8::ITEM: 2, FAST8::MOVE_BENCH: 18, FAST8::MOVE_BOARD: 17, FAST8::PASS: 11, FAST8::SELL: 3, LOSS_STREAK::BUY: 3, LOSS_STREAK::MOVE_BOARD: 2, LOSS_STREAK::PASS: 1, LOSS_STREAK::REROLL: 1, LOSS_STREAK::SELL: 1, STABILIZE::BUY: 42, STABILIZE::ITEM: 8, STABILIZE::MOVE_BENCH: 70, STABILIZE::MOVE_BOARD: 17, STABILIZE::OTHER: 1, STABILIZE::PASS: 21, STABILIZE::REROLL: 16, STABILIZE::SELL: 15
- Jogador 8 — recompensas por ação: BUY: média 0.5047 (n=53), ITEM: média 0.1620 (n=10), MOVE_BENCH: média -0.1082 (n=88), MOVE_BOARD: média -0.0169 (n=36), OTHER: média -0.0200 (n=1), PASS: média -0.0936 (n=33), REROLL: média -0.1882 (n=17), SELL: média -0.1837 (n=19)

### Timeline por decisão

| Jogador | Round | Horário | Ação | Estratégia | Motivo | Ouro observado | Juros | Comp direction | Focus | Recompensa | Sinal para revisar |
|---|---|---|---|---|---|---:|---:|---|---|---:|---|
| Jogador 1 | ? | 19:32:17 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.2600 |  |
| Jogador 1 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 1-1 | 19:32:24 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 1 | 1-1 | 19:32:24 | MOVE Bench -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3200 |  |
| Jogador 1 | 1-1 | 19:32:24 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3100 |  |
| Jogador 1 | 1-1 | 19:32:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 1 | 1-1 | 19:32:25 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0600 |  |
| Jogador 1 | 1-1 | 19:32:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.6400 |  |
| Jogador 1 | 1-1 | 19:32:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 1-1 | 19:32:29 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 1 | 1-2 | 19:32:30 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 1 | 1-2 | 19:32:30 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2500 |  |
| Jogador 1 | 1-2 | 19:32:31 | MOVE Board -> Board: Akali (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-2 | 19:32:31 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 1 | 1-2 | 19:32:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | 1-2 | 19:32:32 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0600 |  |
| Jogador 1 | 1-2 | 19:32:32 | MOVE Board -> Board: Ornn (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 1-2 | 19:32:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0100 |  |
| Jogador 1 | 1-2 | 19:32:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-2 | 19:32:33 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 1-2 | 19:32:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-3 | 19:32:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 1 | 1-3 | 19:32:37 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-3 | 19:32:37 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-3 | 19:32:37 | MOVE Board -> Board: Rakan (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 19:32:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 1 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_GiantsBelt -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2000 |  |
| Jogador 1 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 1 | 1-4 | 19:32:44 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.3900 |  |
| Jogador 1 | 1-4 | 19:32:44 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.2700 |  |
| Jogador 1 | 1-4 | 19:32:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.2200 |  |
| Jogador 1 | 1-4 | 19:32:45 | MOVE Board -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 1-4 | 19:32:46 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 1 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-1 | 19:32:50 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | 0.8700 |  |
| Jogador 1 | 2-1 | 19:32:50 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.3100 |  |
| Jogador 1 | 2-1 | 19:32:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1600 |  |
| Jogador 1 | 2-1 | 19:32:51 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.9300 |  |
| Jogador 1 | 2-1 | 19:32:51 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.5200 |  |
| Jogador 1 | 2-1 | 19:32:51 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-1 | 19:32:52 | MOVE Board -> Board: Leona (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.0100 |  |
| Jogador 1 | 2-1 | 19:32:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | 0.0000 |  |
| Jogador 1 | 2-2 | 19:32:56 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Ornn | 0.8900 |  |
| Jogador 1 | 2-2 | 19:32:57 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | 0.1400 |  |
| Jogador 1 | 2-2 | 19:32:57 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Ornn | -0.1600 |  |
| Jogador 1 | 2-2 | 19:32:57 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.9500 |  |
| Jogador 1 | 2-2 | 19:32:58 | MOVE Bench -> Board: Varus (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-2 | 19:32:58 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5700 |  |
| Jogador 1 | 2-2 | 19:32:58 | MOVE Board -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-2 | 19:32:59 | MOVE Board -> Board: Rakan (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 1 | 2-2 | 19:32:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 1 | 2-3 | 19:33:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.9200 |  |
| Jogador 1 | 2-3 | 19:33:04 | MOVE Bench -> Board: Rakan (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.2000 |  |
| Jogador 1 | 2-3 | 19:33:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1600 |  |
| Jogador 1 | 2-3 | 19:33:04 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | 0.1500 |  |
| Jogador 1 | 2-3 | 19:33:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.1600 |  |
| Jogador 1 | 2-3 | 19:33:05 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.8500 |  |
| Jogador 1 | 2-3 | 19:33:05 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0300 |  |
| Jogador 1 | 2-3 | 19:33:05 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.1800 |  |
| Jogador 1 | 2-3 | 19:33:06 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.8400 |  |
| Jogador 1 | 2-3 | 19:33:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-3 | 19:33:09 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4400 |  |
| Jogador 1 | 2-4 | 19:33:11 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | 0.0100 |  |
| Jogador 1 | 2-4 | 19:33:11 | MOVE Bench -> Board: Rakan (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | 0.1100 |  |
| Jogador 1 | 2-4 | 19:33:11 | MOVE Bench -> Board: Leona (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | -0.4100 |  |
| Jogador 1 | 2-4 | 19:33:11 | MOVE Bench -> Board: Leona (i:2.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | -0.8100 |  |
| Jogador 1 | 2-4 | 19:33:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Defendente | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-5 | 19:33:18 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Defendente | DA_18_Rakan | 0.8200 |  |
| Jogador 1 | 2-5 | 19:33:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Rakan | 0.6900 |  |
| Jogador 1 | 2-5 | 19:33:19 | MOVE Bench -> Board: Vi (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Rakan | 0.0100 |  |
| Jogador 1 | 2-5 | 19:33:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Rakan | -0.1600 |  |
| Jogador 1 | 2-5 | 19:33:20 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | -0.3100 |  |
| Jogador 1 | 2-5 | 19:33:20 | EQUIP_FROM_INVENTORY: TFT_Item_Morellonomicon -> Rakan (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | 0.1500 |  |
| Jogador 1 | 2-5 | 19:33:21 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Rakan (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Defendente | DA_18_Rakan | 0.1500 |  |
| Jogador 1 | 2-5 | 19:33:21 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Defendente | DA_18_Rakan | 0.9000 |  |
| Jogador 1 | 2-5 | 19:33:21 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Defendente | DA_18_Rakan | -0.1600 |  |
| Jogador 1 | 2-5 | 19:33:22 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.3700 |  |
| Jogador 1 | 2-5 | 19:33:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 2-6 | 19:33:26 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | 0.9500 |  |
| Jogador 1 | 2-6 | 19:33:26 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | 0.8600 |  |
| Jogador 1 | 2-6 | 19:33:26 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | 0.4100 |  |
| Jogador 1 | 2-6 | 19:33:26 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | -0.0300 |  |
| Jogador 1 | 2-6 | 19:33:26 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 1 | 2-6 | 19:33:27 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 1 | 2-6 | 19:33:27 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 1 | 2-6 | 19:33:27 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | 0.3300 |  |
| Jogador 1 | 2-6 | 19:33:29 | MOVE Bench -> Board: Shen (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | -0.5000 |  |
| Jogador 1 | 2-6 | 19:33:29 | MOVE Board -> Board: Rakan (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | -0.0200 |  |
| Jogador 1 | 2-6 | 19:33:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 2-7 | 19:33:34 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Shen | 0.8100 |  |
| Jogador 1 | 2-7 | 19:33:34 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Shen | -0.1600 |  |
| Jogador 1 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Shen | 0.1800 |  |
| Jogador 1 | 2-7 | 19:33:34 | MOVE Bench -> Board: Vi (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Shen | -0.3800 |  |
| Jogador 1 | 2-7 | 19:33:35 | MOVE Bench -> Board: Shen (i:4.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Shen | 0.1000 |  |
| Jogador 1 | 2-7 | 19:33:35 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | -0.2200 |  |
| Jogador 1 | 2-7 | 19:33:35 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 2-7 | 19:33:35 | MOVE Bench -> Board: Leona (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | -0.7600 |  |
| Jogador 1 | 2-7 | 19:33:36 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-1 | 19:33:42 | MOVE Bench -> Board: Vi (i:6.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Shen | 0.0500 |  |
| Jogador 1 | 3-1 | 19:33:43 | MOVE Bench -> Board: Leona (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 3-1 | 19:33:43 | MOVE Bench -> Board: Leona (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Shen | -0.7600 |  |
| Jogador 1 | 3-1 | 19:33:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-2 | 19:33:52 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | 0.8300 |  |
| Jogador 1 | 3-2 | 19:33:52 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | 0.1500 |  |
| Jogador 1 | 3-2 | 19:33:52 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 3-2 | 19:33:53 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | 0.4400 |  |
| Jogador 1 | 3-2 | 19:33:53 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Shen | -0.3000 |  |
| Jogador 1 | 3-2 | 19:33:53 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Shen | 0.1000 |  |
| Jogador 1 | 3-2 | 19:33:54 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 3-2 | 19:33:54 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Shen | -0.4100 |  |
| Jogador 1 | 3-2 | 19:33:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-3 | 19:34:00 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Shen | 0.8300 |  |
| Jogador 1 | 3-3 | 19:34:00 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Shen | 0.2700 |  |
| Jogador 1 | 3-3 | 19:34:01 | MOVE Bench -> Board: Xayah (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Shen | 0.4600 |  |
| Jogador 1 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | -0.2200 |  |
| Jogador 1 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Shen | -0.2400 |  |
| Jogador 1 | 3-3 | 19:34:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Shen | 0.2900 |  |
| Jogador 1 | 3-3 | 19:34:04 | MOVE Board -> Board: Xayah (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-3 | 19:34:04 | MOVE Board -> Board: Rakan (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-3 | 19:34:04 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Shen | -0.0100 |  |
| Jogador 1 | 3-3 | 19:34:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 1 | 3-4 | 19:34:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Shen | 0.8100 |  |
| Jogador 1 | 3-4 | 19:34:11 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Colosso | DA_18_Xayah | -0.3100 |  |
| Jogador 1 | 3-4 | 19:34:11 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Colosso | DA_18_Xayah | 0.8100 |  |
| Jogador 1 | 3-4 | 19:34:12 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Colosso | DA_18_Xayah | -0.1900 |  |
| Jogador 1 | 3-4 | 19:34:12 | EQUIP_FROM_INVENTORY: TFT_Item_JeweledGauntlet -> Vi (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Colosso | DA_18_Xayah | 0.1600 |  |
| Jogador 1 | 3-4 | 19:34:12 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Colosso | DA_18_Xayah | 0.7700 |  |
| Jogador 1 | 3-4 | 19:34:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Colosso | DA_18_Xayah | -0.1600 |  |
| Jogador 1 | 3-4 | 19:34:13 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 0 | Colosso | DA_18_Xayah | 0.8100 |  |
| Jogador 1 | 3-4 | 19:34:13 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Colosso | DA_18_Xayah | -0.1600 |  |
| Jogador 1 | 3-4 | 19:34:15 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Xayah | 0.8100 |  |
| Jogador 1 | 3-4 | 19:34:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Xayah | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 1 | 3-5 | 19:34:19 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_18_Xayah | 0.2100 |  |
| Jogador 1 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_18_Xayah | -0.2200 |  |
| Jogador 1 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Xayah | -0.1600 |  |
| Jogador 1 | 3-5 | 19:34:20 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Colosso | DA_18_Rakan | 0.8400 |  |
| Jogador 1 | 3-5 | 19:34:22 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 1 | 3-5 | 19:34:22 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 1 | 3-5 | 19:34:23 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_18_Rakan | -0.2400 |  |
| Jogador 1 | 3-5 | 19:34:23 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Colosso | DA_18_Rakan | 0.8300 |  |
| Jogador 1 | 3-5 | 19:34:23 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Colosso | DA_18_Rakan | 0.4000 |  |
| Jogador 1 | 3-5 | 19:34:24 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 1 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 1 | 3-5 | 19:34:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 1 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 3-6 | 19:34:30 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | 0.2800 |  |
| Jogador 1 | 3-6 | 19:34:30 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 1 | 3-6 | 19:34:30 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Xayah | 0.2900 |  |
| Jogador 1 | 3-6 | 19:34:31 | MOVE Bench -> Board: Shen (i:4.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Xayah | -0.2900 |  |
| Jogador 1 | 3-6 | 19:34:31 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Xayah | -0.1600 |  |
| Jogador 1 | 3-6 | 19:34:31 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Xayah | -0.2200 |  |
| Jogador 1 | 3-6 | 19:34:32 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Xayah | 0.0000 |  |
| Jogador 1 | 3-6 | 19:34:32 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Xayah | -0.3800 |  |
| Jogador 1 | 3-6 | 19:34:32 | MOVE Board -> Board: Sejuani (i:4.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Xayah | -0.3000 |  |
| Jogador 1 | 3-6 | 19:34:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Xayah | 0.0000 |  |
| Jogador 1 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_RecurveBow -> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Xayah | 0.2300 |  |
| Jogador 1 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Xayah | 0.2300 |  |
| Jogador 1 | 3-7 | 19:34:40 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Xayah | -0.4000 |  |
| Jogador 1 | 3-7 | 19:34:40 | MOVE Bench -> Board: Vi (i:6.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Xayah | -0.1200 |  |
| Jogador 1 | 3-7 | 19:34:40 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Xayah | 0.0000 |  |
| Jogador 1 | 4-1 | 19:34:48 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Xayah | 0.4100 |  |
| Jogador 1 | 4-1 | 19:34:48 | MOVE Board -> Board: Varus (i:2.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Xayah | 0.0100 |  |
| Jogador 1 | 4-1 | 19:34:48 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 4-1 | 19:34:51 | MOVE Board -> Board: Rakan (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Xayah | -0.0100 |  |
| Jogador 1 | 4-1 | 19:34:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 11 | 0 | Colosso | DA_18_Xayah | 0.0000 |  |
| Jogador 1 | 4-2 | 19:35:00 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_18_Xayah | 0.8100 |  |
| Jogador 1 | 4-2 | 19:35:01 | REROLL | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_18_Xayah | -0.0900 |  |
| Jogador 1 | 4-2 | 19:35:01 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Colosso | DA_18_Rakan | -0.5000 |  |
| Jogador 1 | 4-2 | 19:35:01 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Vi (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Colosso | DA_18_Rakan | 0.1400 |  |
| Jogador 1 | 4-2 | 19:35:02 | EQUIP_FROM_INVENTORY: TFT_Item_RapidFireCannon -> Vi (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Colosso | DA_18_Rakan | 0.1400 |  |
| Jogador 1 | 4-2 | 19:35:02 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_18_Rakan | 0.8100 |  |
| Jogador 1 | 4-2 | 19:35:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_18_Rakan | -0.0900 |  |
| Jogador 1 | 4-2 | 19:35:02 | MOVE Board -> Board: Shen (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 1 | 4-2 | 19:35:03 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Colosso | DA_18_Rakan | -0.3200 |  |
| Jogador 1 | 4-2 | 19:35:06 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Colosso | DA_18_Rakan | 0.2800 |  |
| Jogador 1 | 4-3 | 19:35:10 | REROLL | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Colosso | DA_18_Rakan | -0.0900 |  |
| Jogador 1 | 4-3 | 19:35:10 | VENDEU: Varus (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 24 | 1 | Colosso | DA_18_Rakan | -0.3300 |  |
| Jogador 1 | 4-3 | 19:35:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 23 | 1 | Colosso | DA_18_Rakan | 0.8800 |  |
| Jogador 1 | 4-3 | 19:35:11 | REROLL | STABILIZE | STABILIZE: pressão de vida | 21 | 1 | Colosso | DA_18_Rakan | -0.0900 |  |
| Jogador 1 | 4-3 | 19:35:11 | REROLL | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_18_Rakan | -0.1700 |  |
| Jogador 1 | 4-3 | 19:35:12 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_18_Shen | 0.8100 |  |
| Jogador 1 | 4-3 | 19:35:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_18_Shen | -0.0900 |  |
| Jogador 1 | 4-3 | 19:35:12 | MOVE Bench -> Board: Shen (i:4.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_18_Shen | 0.0900 |  |
| Jogador 1 | 4-3 | 19:35:16 | REROLL | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_18_Shen | -0.0900 |  |
| Jogador 1 | 4-4 | 19:35:20 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_18_Shen | 0.2100 |  |
| Jogador 1 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_18_Shen | -0.0900 |  |
| Jogador 1 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_18_Shen | -0.0900 |  |
| Jogador 1 | 4-4 | 19:35:20 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 20 | 1 | Colosso | DA_18_Rakan | -0.2000 |  |
| Jogador 1 | 4-4 | 19:35:21 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_Vi18 | 0.7900 |  |
| Jogador 1 | 4-4 | 19:35:21 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_Vi18 | -0.2400 |  |
| Jogador 1 | 4-4 | 19:35:21 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_Vi18 | 0.8300 |  |
| Jogador 1 | 4-4 | 19:35:21 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_Vi18 | 0.3800 |  |
| Jogador 1 | 4-4 | 19:35:25 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_Vi18 | 0.3800 |  |
| Jogador 1 | 4-4 | 19:35:26 | REROLL | STABILIZE | STABILIZE: pressão de vida | 13 | 1 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 1 | 4-5 | 19:35:29 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_Vi18 | 0.9000 |  |
| Jogador 1 | 4-5 | 19:35:30 | MOVE Bench -> Board: Vi (i:12.0) <-> Shen (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_Vi18 | -0.2900 |  |
| Jogador 1 | 4-5 | 19:35:30 | MOVE Bench -> Board: Shen (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_Vi18 | 0.2100 |  |
| Jogador 1 | 4-5 | 19:35:30 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_Vi18 | 0.4000 |  |
| Jogador 1 | 4-5 | 19:35:31 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 1 | 4-5 | 19:35:31 | MOVE Board -> Board: Shen (i:8.0) <-> Leona (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_Vi18 | -0.0200 |  |
| Jogador 1 | 4-5 | 19:35:31 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 20 | 1 | Colosso | DA_Vi18 | -0.1800 |  |
| Jogador 2 | ? | 19:32:17 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.2300 |  |
| Jogador 2 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-1 | 19:32:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0400 |  |
| Jogador 2 | 1-1 | 19:32:24 | MOVE Bench -> Board: Veigar (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 1-1 | 19:32:24 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 1-1 | 19:32:25 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-2 | 19:32:30 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 1.1200 |  |
| Jogador 2 | 1-2 | 19:32:30 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-2 | 19:32:31 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 1-2 | 19:32:31 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 1-2 | 19:32:31 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 1-2 | 19:32:32 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.2200 |  |
| Jogador 2 | 1-2 | 19:32:32 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 1-2 | 19:32:32 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.9400 |  |
| Jogador 2 | 1-2 | 19:32:32 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.6900 |  |
| Jogador 2 | 1-2 | 19:32:33 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.3200 |  |
| Jogador 2 | 1-2 | 19:32:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-3 | 19:32:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.4100 |  |
| Jogador 2 | 1-3 | 19:32:37 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 1.0800 |  |
| Jogador 2 | 1-3 | 19:32:37 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 1.0100 |  |
| Jogador 2 | 1-3 | 19:32:37 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 1-3 | 19:32:38 | MOVE Board -> Board: Rubrivirim (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1100 |  |
| Jogador 2 | 1-3 | 19:32:38 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1300 |  |
| Jogador 2 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 19:32:43 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.2700 |  |
| Jogador 2 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.1700 |  |
| Jogador 2 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 1-4 | 19:32:44 | MOVE Bench -> Board: Veigar (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.5900 |  |
| Jogador 2 | 1-4 | 19:32:44 | MOVE Bench -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.5100 |  |
| Jogador 2 | 1-4 | 19:32:44 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.2100 |  |
| Jogador 2 | 1-4 | 19:32:45 | MOVE Board -> Board: Veigar (i:4.0) <-> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 1-4 | 19:32:46 | MOVE Board -> Board: Rubrivirim (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 1-4 | 19:32:46 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 1-4 | 19:32:46 | MOVE Board -> Board: Veigar (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.3400 |  |
| Jogador 2 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-1 | 19:32:50 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 1.0500 |  |
| Jogador 2 | 2-1 | 19:32:50 | MOVE Bench -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.0800 |  |
| Jogador 2 | 2-1 | 19:32:51 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | 0.3200 |  |
| Jogador 2 | 2-1 | 19:32:51 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.2500 |  |
| Jogador 2 | 2-1 | 19:32:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 2-1 | 19:32:51 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.3400 |  |
| Jogador 2 | 2-1 | 19:32:52 | MOVE Board -> Board: Kobuko (i:2.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 2 | 2-1 | 19:32:52 | MOVE Board -> Board: Veigar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1400 |  |
| Jogador 2 | 2-1 | 19:32:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-1 | 19:32:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-2 | 19:32:56 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.8400 |  |
| Jogador 2 | 2-2 | 19:32:57 | COMPROU: Caitlyn (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.1800 |  |
| Jogador 2 | 2-2 | 19:32:57 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.2200 |  |
| Jogador 2 | 2-2 | 19:32:57 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-2 | 19:32:58 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1800 |  |
| Jogador 2 | 2-2 | 19:32:58 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | -0.5400 |  |
| Jogador 2 | 2-2 | 19:32:58 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.1600 |  |
| Jogador 2 | 2-2 | 19:32:59 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.1000 |  |
| Jogador 2 | 2-2 | 19:32:59 | MOVE Board -> Board: Rubrivirim (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0300 |  |
| Jogador 2 | 2-2 | 19:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-3 | 19:33:04 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-3 | 19:33:04 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.8800 |  |
| Jogador 2 | 2-3 | 19:33:04 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 2 | 2-3 | 19:33:04 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 2-3 | 19:33:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 2-3 | 19:33:05 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 19:33:05 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.8700 |  |
| Jogador 2 | 2-3 | 19:33:05 | VENDEU: Caitlyn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 2 | 2-3 | 19:33:06 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Veigar | 0.0600 |  |
| Jogador 2 | 2-3 | 19:33:07 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 2-3 | 19:33:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-4 | 19:33:11 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-4 | 19:33:11 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Vivaz | DA_18_Veigar | 0.9500 |  |
| Jogador 2 | 2-4 | 19:33:11 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Vivaz | DA_18_Veigar | 0.9400 |  |
| Jogador 2 | 2-4 | 19:33:11 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Xayah | 0.3300 |  |
| Jogador 2 | 2-4 | 19:33:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Vivaz | DA_18_Xayah | -0.1600 |  |
| Jogador 2 | 2-4 | 19:33:12 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | 0.1000 |  |
| Jogador 2 | 2-4 | 19:33:13 | MOVE Bench -> Board: Xayah (i:4.0) <-> Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | 0.1000 |  |
| Jogador 2 | 2-4 | 19:33:14 | MOVE Bench -> Board: Tristana (i:6.0) <-> Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | 0.0500 |  |
| Jogador 2 | 2-4 | 19:33:14 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | 0.3400 |  |
| Jogador 2 | 2-4 | 19:33:14 | MOVE Board -> Board: Rakan (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | -0.0100 |  |
| Jogador 2 | 2-4 | 19:33:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | 0.0000 |  |
| Jogador 2 | 2-5 | 19:33:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Xayah | 0.9000 |  |
| Jogador 2 | 2-5 | 19:33:18 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Xayah | 0.4000 |  |
| Jogador 2 | 2-5 | 19:33:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Vivaz | DA_18_Xayah | -0.2200 |  |
| Jogador 2 | 2-5 | 19:33:19 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | -0.1800 |  |
| Jogador 2 | 2-5 | 19:33:20 | MOVE Board -> Board: Rubrivirim (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | 0.0000 |  |
| Jogador 2 | 2-5 | 19:33:20 | MOVE Board -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | -0.0300 |  |
| Jogador 2 | 2-5 | 19:33:21 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Vivaz | DA_18_Xayah | 0.0000 |  |
| Jogador 2 | 2-6 | 19:33:26 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Vivaz | DA_18_Veigar | -0.1800 |  |
| Jogador 2 | 2-6 | 19:33:26 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Vivaz | DA_18_Veigar | 0.0900 |  |
| Jogador 2 | 2-6 | 19:33:26 | MOVE Bench -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Vivaz | DA_18_Veigar | -0.0900 |  |
| Jogador 2 | 2-6 | 19:33:26 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Vivaz | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 2-6 | 19:33:26 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Vivaz | DA_18_Veigar | -0.2300 |  |
| Jogador 2 | 2-6 | 19:33:27 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Vivaz | DA_18_Veigar | -0.1400 |  |
| Jogador 2 | 2-6 | 19:33:27 | MOVE Board -> Board: Shen (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-6 | 19:33:27 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 2-6 | 19:33:29 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Vivaz | DA_18_Veigar | -0.0200 |  |
| Jogador 2 | 2-6 | 19:33:29 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Veigar | 0.9500 |  |
| Jogador 2 | 2-6 | 19:33:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Vivaz | DA_18_Veigar | 0.0000 |  |
| Jogador 2 | 2-7 | 19:33:34 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Vivaz | DA_18_Veigar | 0.2900 |  |
| Jogador 2 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Vivaz | DA_18_Veigar | 0.2600 |  |
| Jogador 2 | 2-7 | 19:33:34 | MOVE Bench -> Board: Kobuko (i:4.0) <-> Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Vivaz | DA_18_Veigar | -0.3800 |  |
| Jogador 2 | 2-7 | 19:33:34 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Vivaz | DA_18_Kobuko | -0.3700 |  |
| Jogador 2 | 2-7 | 19:33:35 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Kobuko (i:4.0) (tabuleiro slot 22) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Vivaz | DA_18_Kobuko | 0.1900 |  |
| Jogador 2 | 2-7 | 19:33:35 | MOVE Bench -> Board: Veigar (i:2.0) <-> Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Vivaz | DA_18_Kobuko | -0.4200 |  |
| Jogador 2 | 2-7 | 19:33:35 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Vivaz | DA_18_Kobuko | -0.8200 |  |
| Jogador 2 | 2-7 | 19:33:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Vivaz | DA_18_Kobuko | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 2-7 | 19:33:39 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Vivaz | DA_18_Kobuko | 0.4200 |  |
| Jogador 2 | 3-1 | 19:33:42 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Vivaz | DA_18_Kobuko | 0.7400 |  |
| Jogador 2 | 3-1 | 19:33:43 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | 0.8400 |  |
| Jogador 2 | 3-1 | 19:33:43 | MOVE Bench -> Board: Rubrivirim (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | 0.3300 |  |
| Jogador 2 | 3-1 | 19:33:43 | MOVE Bench -> Board: Kobuko (i:4.0) <-> Rubrivirim (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | 0.0700 |  |
| Jogador 2 | 3-1 | 19:33:43 | MOVE Bench -> Board: Rubrivirim (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | 0.4600 |  |
| Jogador 2 | 3-1 | 19:33:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Vivaz | DA_18_Kobuko | -0.1600 |  |
| Jogador 2 | 3-1 | 19:33:44 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Vivaz | DA_18_Kobuko | 0.2800 |  |
| Jogador 2 | 3-1 | 19:33:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Vivaz | DA_18_Kobuko | -0.1600 |  |
| Jogador 2 | 3-1 | 19:33:44 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Vivaz | DA_18_Kobuko | 0.7200 |  |
| Jogador 2 | 3-1 | 19:33:46 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 1 | Vivaz | DA_18_Kobuko | -0.1600 |  |
| Jogador 2 | 3-1 | 19:33:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 1 | Vivaz | DA_18_Kobuko | 0.0000 |  |
| Jogador 2 | 3-2 | 19:33:52 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Vivaz | DA_18_Kobuko | 0.0200 |  |
| Jogador 2 | 3-2 | 19:33:52 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Vivaz | DA_18_Kobuko | 0.8400 |  |
| Jogador 2 | 3-2 | 19:33:52 | MOVE Board -> Board: Rubrivirim (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Vivaz | DA_18_Kobuko | 0.0600 |  |
| Jogador 2 | 3-2 | 19:33:53 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Vivaz | DA_18_Kobuko | -0.1600 |  |
| Jogador 2 | 3-2 | 19:33:53 | MOVE Bench -> Board: Teemo (i:4.0) <-> Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Vivaz | DA_18_Kobuko | -0.6700 |  |
| Jogador 2 | 3-2 | 19:33:53 | MOVE Bench -> Board: Kobuko (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Vivaz | DA_18_Kobuko | -0.3600 |  |
| Jogador 2 | 3-2 | 19:33:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Vivaz | DA_18_Kobuko | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-3 | 19:34:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Vivaz | DA_18_Kobuko | 0.2200 |  |
| Jogador 2 | 3-3 | 19:34:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | 0.8100 |  |
| Jogador 2 | 3-3 | 19:34:01 | MOVE Bench -> Board: Tristana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | 0.1000 |  |
| Jogador 2 | 3-3 | 19:34:01 | MOVE Bench -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | -0.4100 |  |
| Jogador 2 | 3-3 | 19:34:01 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | -0.5500 |  |
| Jogador 2 | 3-3 | 19:34:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Vivaz | DA_18_Kobuko | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-4 | 19:34:10 | MOVE Bench -> Board: Kobuko (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Vivaz | DA_18_Kobuko | -0.3900 |  |
| Jogador 2 | 3-4 | 19:34:11 | VENDEU: Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 1 | Vivaz | DA_18_Kobuko | -0.5400 |  |
| Jogador 2 | 3-4 | 19:34:11 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Vivaz | DA_18_Kobuko | 0.3000 |  |
| Jogador 2 | 3-4 | 19:34:12 | MOVE Bench -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Vivaz | DA_18_Kobuko | -0.4000 |  |
| Jogador 2 | 3-4 | 19:34:12 | MOVE Bench -> Board: Tristana (i:6.0) <-> Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Vivaz | DA_18_Kobuko | -0.3100 |  |
| Jogador 2 | 3-4 | 19:34:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 1 | Vivaz | DA_18_Kobuko | -0.0200 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-5 | 19:34:19 | VENDEU: Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Vivaz | DA_Cinderling18 | -0.3600 |  |
| Jogador 2 | 3-5 | 19:34:19 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Rubrivirim (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 2 | Vivaz | DA_Cinderling18 | 0.1700 |  |
| Jogador 2 | 3-5 | 19:34:19 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Vivaz | DA_Cinderling18 | 0.8300 |  |
| Jogador 2 | 3-5 | 19:34:20 | MOVE Bench -> Board: Veigar (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Vivaz | DA_Cinderling18 | -0.4100 |  |
| Jogador 2 | 3-5 | 19:34:22 | MOVE Bench -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Vivaz | DA_Cinderling18 | -0.4100 |  |
| Jogador 2 | 3-5 | 19:34:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 38 | 2 | Vivaz | DA_Cinderling18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-6 | 19:34:30 | VENDEU: Krugue (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 3 | Vivaz | DA_Cinderling18 | 0.1000 |  |
| Jogador 2 | 3-6 | 19:34:30 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Vivaz | DA_Cinderling18 | 0.9000 |  |
| Jogador 2 | 3-6 | 19:34:30 | MOVE Bench -> Board: Tristana (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 3 | Vivaz | DA_Cinderling18 | 0.1100 |  |
| Jogador 2 | 3-6 | 19:34:31 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Vivaz | DA_Cinderling18 | -0.1700 |  |
| Jogador 2 | 3-6 | 19:34:31 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Vivaz | DA_Cinderling18 | 0.5300 |  |
| Jogador 2 | 3-6 | 19:34:31 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Vivaz | DA_Cinderling18 | -0.1600 |  |
| Jogador 2 | 3-6 | 19:34:32 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Vivaz | DA_Cinderling18 | 0.8300 |  |
| Jogador 2 | 3-6 | 19:34:32 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Vivaz | DA_Cinderling18 | -0.2400 |  |
| Jogador 2 | 3-6 | 19:34:32 | VENDEU: Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Vivaz | DA_Cinderling18 | -0.2200 |  |
| Jogador 2 | 3-6 | 19:34:35 | COMPROU: Rammus (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Vivaz | DA_Cinderling18 | 0.2300 |  |
| Jogador 2 | 3-6 | 19:34:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 39 | 3 | Vivaz | DA_Cinderling18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Vivaz | DA_Cinderling18 | 0.1800 |  |
| Jogador 2 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Vivaz | DA_Cinderling18 | 0.1800 |  |
| Jogador 2 | 3-7 | 19:34:40 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 3 | Vivaz | DA_18_Tristana | -0.2700 |  |
| Jogador 2 | 3-7 | 19:34:40 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 3 | Vivaz | DA_18_Veigar | 0.9300 |  |
| Jogador 2 | 3-7 | 19:34:40 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 47 | 3 | Vivaz | DA_18_Veigar | 0.3300 |  |
| Jogador 2 | 3-7 | 19:34:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Vivaz | DA_18_Veigar | -0.2200 |  |
| Jogador 2 | 3-7 | 19:34:44 | MOVE Bench -> Board: Teemo (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 3 | Vivaz | DA_18_Veigar | -0.4000 |  |
| Jogador 2 | 3-7 | 19:34:44 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Vivaz | DA_18_Veigar | -0.1800 |  |
| Jogador 2 | 3-7 | 19:34:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 40 | 3 | Vivaz | DA_18_Veigar | -0.1600 |  |
| Jogador 2 | 3-7 | 19:34:45 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Vivaz | DA_Cinderling18 | -0.3700 |  |
| Jogador 2 | 3-7 | 19:34:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Vivaz | DA_Cinderling18 | -0.1900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-1 | 19:34:48 | MOVE Bench -> Board: Rubrivirim (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Vivaz | DA_Cinderling18 | -0.6700 |  |
| Jogador 2 | 4-1 | 19:34:48 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Vivaz | DA_Cinderling18 | 0.4500 |  |
| Jogador 2 | 4-1 | 19:34:48 | MOVE Bench -> Board: Tristana (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Vivaz | DA_18_Tristana | -0.0900 |  |
| Jogador 2 | 4-1 | 19:34:51 | MOVE Bench -> Board: Teemo (i:4.0) <-> Rubrivirim (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Vivaz | DA_18_Tristana | -0.3300 |  |
| Jogador 2 | 4-1 | 19:34:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 52 | 4 | Vivaz | DA_18_Tristana | -0.0900 |  |
| Jogador 2 | 4-2 | 19:35:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Vivaz | DA_18_Tristana | 0.0700 |  |
| Jogador 2 | 4-2 | 19:35:01 | MOVE Board -> Board: Tristana (i:6.0) <-> Rubrivirim (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Vivaz | DA_Cinderling18 | 0.1100 |  |
| Jogador 2 | 4-2 | 19:35:01 | MOVE Board -> Board: Rubrivirim (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Vivaz | DA_Cinderling18 | -0.0700 |  |
| Jogador 2 | 4-2 | 19:35:01 | MOVE Board -> Board: Shen (i:4.0) <-> Tristana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Vivaz | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 4-2 | 19:35:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Vivaz | DA_18_Tristana | -0.2400 |  |
| Jogador 2 | 4-3 | 19:35:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Vivaz | DA_18_Xayah | 0.9300 |  |
| Jogador 2 | 4-3 | 19:35:10 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Vivaz | DA_18_Xayah | 0.4000 |  |
| Jogador 2 | 4-3 | 19:35:10 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Vivaz | DA_18_Xayah | 0.3300 |  |
| Jogador 2 | 4-3 | 19:35:11 | REROLL | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Vivaz | DA_18_Xayah | -0.0900 |  |
| Jogador 2 | 4-3 | 19:35:11 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Vivaz | DA_18_Xayah | 0.9600 |  |
| Jogador 2 | 4-3 | 19:35:12 | MOVE Bench -> Board: Xayah (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Vivaz | DA_18_Xayah | 0.0700 |  |
| Jogador 2 | 4-3 | 19:35:12 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Vivaz | DA_18_Xayah | 0.4100 |  |
| Jogador 2 | 4-3 | 19:35:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Vivaz | DA_18_Xayah | -0.1500 |  |
| Jogador 2 | 4-3 | 19:35:16 | MOVE Board -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Vivaz | DA_18_Xayah | 0.0000 |  |
| Jogador 2 | 4-4 | 19:35:20 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 73 | 5 | Vivaz | DA_18_Xayah | 0.8700 |  |
| Jogador 2 | 4-4 | 19:35:20 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_Cinderling18 | 0.9600 |  |
| Jogador 2 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Vivaz | DA_Cinderling18 | -0.0900 |  |
| Jogador 2 | 4-4 | 19:35:20 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Vivaz | DA_18_Xayah | 0.8600 |  |
| Jogador 2 | 4-4 | 19:35:21 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Vivaz | DA_18_Xayah | 0.9500 |  |
| Jogador 2 | 4-4 | 19:35:21 | REROLL | STABILIZE | STABILIZE: pressão de vida | 66 | 5 | Vivaz | DA_18_Xayah | -0.0900 |  |
| Jogador 2 | 4-4 | 19:35:21 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Vivaz | DA_18_Xayah | 0.3400 |  |
| Jogador 2 | 4-4 | 19:35:21 | MOVE Bench -> Board: Xayah (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Vivaz | DA_18_Xayah | -0.4800 |  |
| Jogador 2 | 4-4 | 19:35:25 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Vivaz | DA_18_Xayah | 0.3700 |  |
| Jogador 2 | 4-4 | 19:35:26 | REROLL | STABILIZE | STABILIZE: pressão de vida | 63 | 5 | Vivaz | DA_18_Xayah | -0.0900 |  |
| Jogador 2 | 4-5 | 19:35:29 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Vivaz | DA_18_Xayah | 0.1200 |  |
| Jogador 2 | 4-5 | 19:35:30 | REROLL | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Vivaz | DA_18_Xayah | -0.0900 |  |
| Jogador 2 | 4-5 | 19:35:30 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_Cinderling18 | -0.4200 |  |
| Jogador 2 | 4-5 | 19:35:30 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Vivaz | DA_Cinderling18 | 0.3500 |  |
| Jogador 2 | 4-5 | 19:35:31 | MOVE Board -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Vivaz | DA_Cinderling18 | 0.0600 |  |
| Jogador 2 | 4-5 | 19:35:31 | REROLL | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Vivaz | DA_Cinderling18 | -0.0900 |  |
| Jogador 2 | 4-5 | 19:35:31 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Vivaz | DA_Cinderling18 | -0.3400 |  |
| Jogador 2 | 4-5 | 19:35:35 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 70 | 5 | Vivaz | DA_18_Teemo | 0.3900 |  |
| Jogador 2 | 4-5 | 19:35:35 | REROLL | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Vivaz | DA_18_Teemo | -0.1500 |  |
| Jogador 2 | 4-5 | 19:35:35 | MOVE Bench -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 68 | 5 | Vivaz | DA_18_Teemo | 0.1000 |  |
| Jogador 2 | 4-6 | 19:35:39 | VENDEU: Rubrivirim (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 83 | 5 | Vivaz | DA_18_Teemo | -0.4600 |  |
| Jogador 2 | 4-6 | 19:35:39 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Vivaz | DA_18_Teemo | 0.9300 |  |
| Jogador 2 | 4-6 | 19:35:40 | MOVE Bench -> Board: Rakan (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Vivaz | DA_18_Teemo | -0.4100 |  |
| Jogador 2 | 4-6 | 19:35:40 | MOVE Bench -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Vivaz | DA_18_Teemo | -0.2400 |  |
| Jogador 2 | 4-6 | 19:35:40 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 81 | 5 | Vivaz | DA_18_Teemo | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_ChainVest -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Vivaz | DA_18_Teemo | 0.1400 |  |
| Jogador 2 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Vivaz | DA_18_Teemo | 0.1500 |  |
| Jogador 2 | 4-7 | 19:35:50 | MOVE Bench -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Vivaz | DA_18_Teemo | -0.2200 |  |
| Jogador 2 | 4-7 | 19:35:50 | MOVE Bench -> Board: Rakan (i:2.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Vivaz | DA_18_Teemo | -0.4300 |  |
| Jogador 2 | 4-7 | 19:35:50 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 92 | 5 | Vivaz | DA_18_Teemo | -0.1500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 2 | 5-1 | 19:35:59 | VENDEU: Teemo (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Vivaz | DA_18_Tristana | -0.3800 |  |
| Jogador 2 | 5-1 | 19:36:00 | COMPROU: Veigar (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Vivaz | DA_18_Tristana | 0.3800 |  |
| Jogador 2 | 5-1 | 19:36:00 | MOVE Bench -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Vivaz | DA_18_Tristana | 0.0100 |  |
| Jogador 2 | 5-1 | 19:36:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 104 | 5 | Vivaz | DA_18_Tristana | -0.0900 |  |
| Jogador 2 | 5-1 | 19:36:00 | VENDEU: Azir (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 107 | 5 | Vivaz | DA_18_Tristana | 0.0000 |  |
| Jogador 2 | 5-1 | 19:36:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Vivaz | DA_18_Tristana | 0.9200 |  |
| Jogador 2 | 5-1 | 19:36:05 | VENDEU: Diana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Tristana | -0.0100 |  |
| Jogador 2 | 5-1 | 19:36:05 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 108 | 5 | Vivaz | DA_18_Tristana | 0.3400 |  |
| Jogador 2 | 5-1 | 19:36:05 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 106 | 5 | Vivaz | DA_18_Tristana | -0.0900 |  |
| Jogador 2 | 5-2 | 19:36:09 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 115 | 5 | Vivaz | DA_18_Tristana | -0.0900 |  |
| Jogador 2 | 5-2 | 19:36:10 | VENDEU: Rubrivirim (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 116 | 5 | Vivaz | DA_18_Tristana | -0.1800 |  |
| Jogador 2 | 5-2 | 19:36:10 | COMPROU: Rammus (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 113 | 5 | Vivaz | DA_18_Tristana | 0.9100 |  |
| Jogador 2 | 5-2 | 19:36:10 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 111 | 5 | Vivaz | DA_18_Tristana | -0.0900 |  |
| Jogador 2 | 5-2 | 19:36:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Tristana | -0.0900 |  |
| Jogador 2 | 5-2 | 19:36:11 | MOVE Bench -> Board: Tristana (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Tristana | 0.0600 |  |
| Jogador 2 | 5-2 | 19:36:15 | MOVE Bench -> Board: Rakan (i:2.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Tristana | -0.4200 |  |
| Jogador 2 | 5-2 | 19:36:15 | MOVE Bench -> Board: Tristana (i:6.0) <-> Tristana (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 109 | 5 | Vivaz | DA_18_Tristana | -0.2700 |  |
| Jogador 3 | ? | 19:32:17 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 19:32:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 1-1 | 19:32:24 | MOVE Bench -> Board: Yorick (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.7200 |  |
| Jogador 3 | 1-1 | 19:32:24 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.4100 |  |
| Jogador 3 | 1-1 | 19:32:25 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1200 |  |
| Jogador 3 | 1-1 | 19:32:25 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 1-1 | 19:32:25 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.6300 |  |
| Jogador 3 | 1-1 | 19:32:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-1 | 19:32:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 1-2 | 19:32:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0400 |  |
| Jogador 3 | 1-2 | 19:32:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 3 | 1-2 | 19:32:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-2 | 19:32:35 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.6800 |  |
| Jogador 3 | 1-3 | 19:32:37 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 1-3 | 19:32:37 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2200 |  |
| Jogador 3 | 1-3 | 19:32:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 3 | 1-3 | 19:32:37 | MOVE Board -> Board: Akali (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 19:32:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 1-3 | 19:32:38 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 19:32:38 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 1-4 | 19:32:43 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 3 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1500 |  |
| Jogador 3 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 3 | 1-4 | 19:32:44 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 3 | 1-4 | 19:32:44 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 1-4 | 19:32:44 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.6800 |  |
| Jogador 3 | 1-4 | 19:32:45 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-1 | 19:32:50 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.3700 |  |
| Jogador 3 | 2-1 | 19:32:50 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.6400 |  |
| Jogador 3 | 2-1 | 19:32:51 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.2400 |  |
| Jogador 3 | 2-1 | 19:32:51 | MOVE Bench -> Board: Akali (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.1100 |  |
| Jogador 3 | 2-1 | 19:32:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2200 |  |
| Jogador 3 | 2-1 | 19:32:51 | MOVE Bench -> Board: Yorick (i:2.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.7300 |  |
| Jogador 3 | 2-1 | 19:32:52 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 2-1 | 19:32:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-2 | 19:32:56 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.9900 |  |
| Jogador 3 | 2-2 | 19:32:57 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 3 | 2-2 | 19:32:57 | MOVE Bench -> Board: Grompe (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 2-2 | 19:32:57 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.5800 |  |
| Jogador 3 | 2-2 | 19:32:58 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 2-2 | 19:32:58 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.2300 |  |
| Jogador 3 | 2-2 | 19:32:58 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 2-2 | 19:32:59 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-3 | 19:33:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | 0.9700 |  |
| Jogador 3 | 2-3 | 19:33:04 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.7400 |  |
| Jogador 3 | 2-3 | 19:33:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 2-3 | 19:33:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.9500 |  |
| Jogador 3 | 2-3 | 19:33:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3200 |  |
| Jogador 3 | 2-3 | 19:33:05 | MOVE Bench -> Board: Grompe (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-3 | 19:33:05 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3900 |  |
| Jogador 3 | 2-3 | 19:33:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.2200 |  |
| Jogador 3 | 2-3 | 19:33:06 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | -0.0700 |  |
| Jogador 3 | 2-3 | 19:33:07 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Hecarim (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0800 |  |
| Jogador 3 | 2-3 | 19:33:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-4 | 19:33:11 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Hecarim (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Yorick | 0.0700 |  |
| Jogador 3 | 2-4 | 19:33:11 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Yorick | 0.2200 |  |
| Jogador 3 | 2-4 | 19:33:11 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Yorick | -0.1600 |  |
| Jogador 3 | 2-4 | 19:33:11 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Yorick | 0.7800 |  |
| Jogador 3 | 2-4 | 19:33:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_18_Yorick | -0.1600 |  |
| Jogador 3 | 2-4 | 19:33:12 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Yorick | 0.9500 |  |
| Jogador 3 | 2-4 | 19:33:13 | MOVE Board -> Board: Hecarim (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-4 | 19:33:14 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Yorick | -0.0200 |  |
| Jogador 3 | 2-4 | 19:33:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-5 | 19:33:18 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Yorick | -0.3500 |  |
| Jogador 3 | 2-5 | 19:33:18 | MOVE Bench -> Board: Grompe (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Yorick | 0.2300 |  |
| Jogador 3 | 2-5 | 19:33:19 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Yorick | -0.3900 |  |
| Jogador 3 | 2-5 | 19:33:19 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Yorick | -0.2600 |  |
| Jogador 3 | 2-5 | 19:33:20 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-6 | 19:33:26 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Devastador | DA_18_Yorick | 0.3200 |  |
| Jogador 3 | 2-6 | 19:33:26 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Yorick | -0.2400 |  |
| Jogador 3 | 2-6 | 19:33:26 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Yorick | 0.3300 |  |
| Jogador 3 | 2-6 | 19:33:26 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Yorick | 0.9000 |  |
| Jogador 3 | 2-6 | 19:33:26 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Yorick | -0.1600 |  |
| Jogador 3 | 2-6 | 19:33:27 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Devastador | DA_18_Yorick | -0.2200 |  |
| Jogador 3 | 2-6 | 19:33:27 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Yorick | -0.1600 |  |
| Jogador 3 | 2-6 | 19:33:27 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Yorick | -0.3200 |  |
| Jogador 3 | 2-6 | 19:33:29 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_18_Yorick | 0.8800 |  |
| Jogador 3 | 2-6 | 19:33:29 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Devastador | DA_18_Yorick | -0.2200 |  |
| Jogador 3 | 2-6 | 19:33:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Devastador | DA_18_Yorick | 0.0000 |  |
| Jogador 3 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_BFSword -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Yorick | 0.1800 |  |
| Jogador 3 | 2-7 | 19:33:34 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Yorick | -0.1600 |  |
| Jogador 3 | 2-7 | 19:33:34 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | -0.1900 |  |
| Jogador 3 | 2-7 | 19:33:34 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 2-7 | 19:33:35 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 2-7 | 19:33:35 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 2-7 | 19:33:35 | MOVE Bench -> Board: Camille (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 2-7 | 19:33:35 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | 0.4000 |  |
| Jogador 3 | 2-7 | 19:33:36 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Devastador | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 2-7 | 19:33:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | 2-7 | 19:33:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 19:33:42 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.2700 |  |
| Jogador 3 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 3-1 | 19:33:43 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-1 | 19:33:43 | MOVE Board -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-1 | 19:33:43 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-2 | 19:33:52 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-2 | 19:33:52 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Diana (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Devastador | DA_18_Akali_AD | 0.1800 |  |
| Jogador 3 | 3-2 | 19:33:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.2800 |  |
| Jogador 3 | 3-2 | 19:33:53 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | 0.0200 |  |
| Jogador 3 | 3-2 | 19:33:53 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Devastador | DA_18_Akali_AD | 0.5700 |  |
| Jogador 3 | 3-2 | 19:33:53 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Akali_AD | -0.2200 |  |
| Jogador 3 | 3-2 | 19:33:54 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-2 | 19:33:54 | VENDEU: Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Akali_AD | 0.0900 |  |
| Jogador 3 | 3-2 | 19:33:54 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.7600 |  |
| Jogador 3 | 3-2 | 19:33:57 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.5900 |  |
| Jogador 3 | 3-2 | 19:33:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 19:34:00 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Devastador | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 3-3 | 19:34:00 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Akali_AD | 0.8300 |  |
| Jogador 3 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-3 | 19:34:01 | MOVE Board -> Board: Akali (i:2.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-3 | 19:34:01 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 3-3 | 19:34:04 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-4 | 19:34:10 | COMPROU: Grompe (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Devastador | DA_Gromp18_AP | 0.2900 |  |
| Jogador 3 | 3-4 | 19:34:11 | MOVE Board -> Board: Hecarim (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Devastador | DA_Gromp18_AP | 0.0000 |  |
| Jogador 3 | 3-4 | 19:34:11 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Devastador | DA_Gromp18_AP | -0.0100 |  |
| Jogador 3 | 3-4 | 19:34:12 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_Gromp18_AP | 0.2000 |  |
| Jogador 3 | 3-4 | 19:34:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_Gromp18_AP | -0.2200 |  |
| Jogador 3 | 3-4 | 19:34:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_Gromp18_AP | -0.1600 |  |
| Jogador 3 | 3-4 | 19:34:12 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Akali_AD | 0.8100 |  |
| Jogador 3 | 3-4 | 19:34:13 | VENDEU: Grompe (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | -0.3100 |  |
| Jogador 3 | 3-4 | 19:34:13 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | 0.2900 |  |
| Jogador 3 | 3-4 | 19:34:15 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 3-4 | 19:34:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 3-5 | 19:34:19 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Devastador | DA_18_Akali_AD | -0.3400 |  |
| Jogador 3 | 3-5 | 19:34:19 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Devastador | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Devastador | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 3-5 | 19:34:20 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Akali_AD | -0.1600 |  |
| Jogador 3 | 3-5 | 19:34:22 | VENDEU: Lobo Trevoguari (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Devastador | DA_18_Akali_AD | -0.0600 |  |
| Jogador 3 | 3-5 | 19:34:22 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | 0.7200 |  |
| Jogador 3 | 3-5 | 19:34:23 | VENDEU: Grompe (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Devastador | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 3-5 | 19:34:23 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Akali_AD | 0.8400 |  |
| Jogador 3 | 3-5 | 19:34:23 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 3-5 | 19:34:24 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Diana | 0.8300 |  |
| Jogador 3 | 3-5 | 19:34:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-6 | 19:34:30 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Diana | 0.2500 |  |
| Jogador 3 | 3-6 | 19:34:30 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Diana | 0.5800 |  |
| Jogador 3 | 3-6 | 19:34:30 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-6 | 19:34:31 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Diana | -0.0400 |  |
| Jogador 3 | 3-6 | 19:34:31 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Diana | -0.1600 |  |
| Jogador 3 | 3-6 | 19:34:31 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Diana | 0.8400 |  |
| Jogador 3 | 3-6 | 19:34:32 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Diana | 0.4200 |  |
| Jogador 3 | 3-6 | 19:34:32 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Devastador | DA_18_Diana | 0.2900 |  |
| Jogador 3 | 3-6 | 19:34:32 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | -0.2200 |  |
| Jogador 3 | 3-6 | 19:34:35 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-6 | 19:34:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-7 | 19:34:39 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Devastador | DA_18_Diana | 0.2900 |  |
| Jogador 3 | 3-7 | 19:34:39 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Devastador | DA_18_Diana | 0.2800 |  |
| Jogador 3 | 3-7 | 19:34:40 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Devastador | DA_18_Diana | 0.1800 |  |
| Jogador 3 | 3-7 | 19:34:40 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_GiantsBelt -> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Devastador | DA_18_Diana | 0.1600 |  |
| Jogador 3 | 3-7 | 19:34:40 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | -0.1600 |  |
| Jogador 3 | 3-7 | 19:34:44 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Devastador | DA_18_Diana | -0.2600 |  |
| Jogador 3 | 3-7 | 19:34:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Devastador | DA_18_Diana | 0.8100 |  |
| Jogador 3 | 3-7 | 19:34:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | -0.2200 |  |
| Jogador 3 | 3-7 | 19:34:44 | MOVE Board -> Board: Akali (i:4.0) <-> Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 3-7 | 19:34:45 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 3-7 | 19:34:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Devastador | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 4-1 | 19:34:48 | VENDEU: Diana (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Devastador | DA_18_Akali_AD | -0.2800 |  |
| Jogador 3 | 4-1 | 19:34:48 | EQUIP_FROM_INVENTORY: TFT_Item_InfinityEdge -> Hecarim (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Devastador | DA_18_Akali_AD | 0.0700 |  |
| Jogador 3 | 4-1 | 19:34:48 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Devastador | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 4-1 | 19:34:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Devastador | DA_18_Akali_AD | -0.2200 |  |
| Jogador 3 | 4-1 | 19:34:52 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Devastador | DA_18_Akali_AD | -0.6300 |  |
| Jogador 3 | 4-1 | 19:34:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Devastador | DA_18_Akali_AD | 0.8000 |  |
| Jogador 3 | 4-1 | 19:34:52 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Devastador | DA_18_Akali_AD | -0.2400 |  |
| Jogador 3 | 4-1 | 19:34:52 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Devastador | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 4-1 | 19:34:53 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Devastador | DA_18_Akali_AD | 0.7200 |  |
| Jogador 3 | 4-1 | 19:34:53 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Devastador | DA_18_Akali_AD | 0.4200 |  |
| Jogador 3 | 4-1 | 19:34:53 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 7 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 19:35:00 | MOVE Board -> Board: Camille (i:2.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-2 | 19:35:01 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-2 | 19:35:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 14 | 0 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 19:35:10 | MOVE Board -> Board: Akali (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-3 | 19:35:10 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-3 | 19:35:10 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 22 | 1 | Devastador | DA_18_Akali_AD | -0.1100 |  |
| Jogador 3 | 4-4 | 19:35:20 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Devastador | DA_18_Akali_AD | 0.2000 |  |
| Jogador 3 | 4-4 | 19:35:20 | MOVE Board -> Board: Akali (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-4 | 19:35:20 | MOVE Board -> Board: Hecarim (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Devastador | DA_18_Akali_AD | -0.0200 |  |
| Jogador 3 | 4-4 | 19:35:20 | MOVE Board -> Board: Camille (i:2.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-4 | 19:35:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 29 | 2 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 4-5 | 19:35:29 | VENDEU: Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 40 | 3 | Devastador | DA_18_Akali_AD | -0.2900 |  |
| Jogador 3 | 4-5 | 19:35:30 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Devastador | DA_18_Akali_AD | 0.2100 |  |
| Jogador 3 | 4-5 | 19:35:30 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Devastador | DA_18_Akali_AD | 0.0000 |  |
| Jogador 3 | 4-5 | 19:35:30 | MOVE Board -> Board: Akali (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-5 | 19:35:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 37 | 3 | Devastador | DA_18_Akali_AD | -0.0400 |  |
| Jogador 3 | 4-6 | 19:35:39 | MOVE Bench -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 4-6 | 19:35:39 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 4-6 | 19:35:40 | MOVE Board -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Devastador | DA_18_Akali_AD | -0.0100 |  |
| Jogador 3 | 4-6 | 19:35:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 45 | 3 | Devastador | DA_18_Akali_AD | -0.0500 |  |
| Jogador 3 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Akali_AD | 0.2000 |  |
| Jogador 3 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Akali_AD | 0.1400 |  |
| Jogador 3 | 4-7 | 19:35:50 | MOVE Bench -> Board: Akali (i:4.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 4-7 | 19:35:50 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Akali_AD | -0.4200 |  |
| Jogador 3 | 4-7 | 19:35:50 | MOVE Bench -> Board: Akali (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Akali_AD | -0.3100 |  |
| Jogador 3 | 4-7 | 19:35:51 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 4 | Devastador | DA_18_Akali_AD | -0.0900 |  |
| Jogador 3 | 5-1 | 19:35:59 | MOVE Bench -> Board: Akali (i:4.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-1 | 19:36:00 | MOVE Bench -> Board: Camille (i:2.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Devastador | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 5-1 | 19:36:00 | MOVE Bench -> Board: Akali (i:4.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Devastador | DA_18_Akali_AD | -0.3100 |  |
| Jogador 3 | 5-1 | 19:36:00 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 65 | 5 | Devastador | DA_18_Akali_AD | -0.1000 |  |
| Jogador 3 | 5-2 | 19:36:09 | VENDEU: Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 80 | 5 | Devastador | DA_18_Akali_AD | -0.5400 |  |
| Jogador 3 | 5-2 | 19:36:10 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Devastador | DA_18_Warwick | 0.9500 |  |
| Jogador 3 | 5-2 | 19:36:10 | COMPROU: Hecarim (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Warwick | 0.3600 |  |
| Jogador 3 | 5-2 | 19:36:10 | MOVE Bench -> Board: Warwick (i:8.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Warwick | 0.1000 |  |
| Jogador 3 | 5-2 | 19:36:11 | MOVE Bench -> Board: Camille (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Warwick | 0.0800 |  |
| Jogador 3 | 5-2 | 19:36:11 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Warwick (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Warwick | -0.7700 |  |
| Jogador 3 | 5-2 | 19:36:15 | MOVE Bench -> Board: Warwick (i:8.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Warwick | 0.0800 |  |
| Jogador 3 | 5-2 | 19:36:15 | MOVE Bench -> Board: Camille (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 75 | 5 | Devastador | DA_18_Warwick | 0.0800 |  |
| Jogador 3 | 5-3 | 19:36:20 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Devastador | DA_18_Warwick | -0.2500 |  |
| Jogador 3 | 5-3 | 19:36:20 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Devastador | DA_18_Warwick | -0.4100 |  |
| Jogador 3 | 5-3 | 19:36:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 87 | 5 | Devastador | DA_18_Warwick | -0.2700 |  |
| Jogador 3 | 5-4 | 19:36:31 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Warwick | 0.4000 |  |
| Jogador 3 | 5-4 | 19:36:31 | MOVE Bench -> Board: Camille (i:2.0) <-> Warwick (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Warwick | -0.7100 |  |
| Jogador 3 | 5-4 | 19:36:31 | MOVE Bench -> Board: Warwick (i:8.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Warwick | 0.0900 |  |
| Jogador 3 | 5-4 | 19:36:32 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Warwick | -0.4100 |  |
| Jogador 3 | 5-4 | 19:36:32 | MOVE Bench -> Board: Camille (i:2.0) <-> Warwick (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Warwick | -0.7300 |  |
| Jogador 3 | 5-4 | 19:36:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Devastador | DA_18_Warwick | -0.1200 |  |
| Jogador 3 | 5-5 | 19:36:41 | VENDEU: Warwick (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 112 | 5 | Devastador | DA_18_Akali_AD | -0.3700 |  |
| Jogador 3 | 5-5 | 19:36:41 | COMPROU: Diana (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Devastador | DA_18_Akali_AD | 0.8900 |  |
| Jogador 3 | 5-5 | 19:36:42 | MOVE Bench -> Board: Diana (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-5 | 19:36:42 | VENDEU: Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Devastador | DA_18_Akali_AD | -0.2600 |  |
| Jogador 3 | 5-5 | 19:36:42 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Devastador | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 5-5 | 19:36:42 | MOVE Bench -> Board: Camille (i:2.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-5 | 19:36:43 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 5-5 | 19:36:43 | MOVE Bench -> Board: Diana (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 5-6 | 19:36:52 | VENDEU: Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 124 | 5 | Devastador | DA_18_Akali_AD | -0.2700 |  |
| Jogador 3 | 5-6 | 19:36:52 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.8500 |  |
| Jogador 3 | 5-6 | 19:36:52 | MOVE Bench -> Board: Camille (i:2.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-6 | 19:36:52 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 5-6 | 19:36:53 | MOVE Bench -> Board: Diana (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 5-6 | 19:36:53 | MOVE Bench -> Board: Camille (i:2.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 5-6 | 19:36:53 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 5-6 | 19:36:53 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -0.7200 |  |
| Jogador 3 | 5-6 | 19:36:54 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 122 | 5 | Devastador | DA_18_Akali_AD | -0.1500 |  |
| Jogador 3 | 5-7 | 19:37:02 | EQUIP_FROM_INVENTORY: TFT_Item_GuinsoosRageblade -> Diana (i:6.0) (tabuleiro slot 12) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Devastador | DA_18_Akali_AD | 0.0800 |  |
| Jogador 3 | 5-7 | 19:37:03 | MOVE Bench -> Board: Akali (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 5-7 | 19:37:03 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 5-7 | 19:37:03 | MOVE Bench -> Board: Camille (i:2.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Devastador | DA_18_Akali_AD | -0.7700 |  |
| Jogador 3 | 5-7 | 19:37:03 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 133 | 5 | Devastador | DA_18_Akali_AD | -0.1700 |  |
| Jogador 3 | 6-1 | 19:37:13 | MOVE Bench -> Board: Akali (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 143 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 6-1 | 19:37:13 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 143 | 5 | Devastador | DA_18_Akali_AD | -0.4100 |  |
| Jogador 3 | 6-1 | 19:37:14 | MOVE Bench -> Board: Camille (i:2.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 143 | 5 | Devastador | DA_18_Akali_AD | -0.6600 |  |
| Jogador 3 | 6-1 | 19:37:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 143 | 5 | Devastador | DA_18_Akali_AD | -0.1800 |  |
| Jogador 3 | 6-2 | 19:37:24 | MOVE Bench -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Devastador | DA_18_Akali_AD | 0.1000 |  |
| Jogador 3 | 6-2 | 19:37:25 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 154 | 5 | Devastador | DA_18_Akali_AD | -0.7300 |  |
| Jogador 3 | 6-2 | 19:37:25 | VENDEU: Akali (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Devastador | DA_18_Diana | -0.3800 |  |
| Jogador 3 | 6-2 | 19:37:25 | EQUIP_FROM_INVENTORY: TFT_Item_TitansResolve -> Aronguejo (i:4.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Devastador | DA_18_Diana | 0.0400 |  |
| Jogador 3 | 6-2 | 19:37:25 | EQUIP_FROM_INVENTORY: TFT_Item_Redemption -> Aronguejo (i:4.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Devastador | DA_18_Diana | 0.0600 |  |
| Jogador 3 | 6-2 | 19:37:25 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Devastador | DA_18_Diana | 0.4800 |  |
| Jogador 3 | 6-2 | 19:37:26 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Devastador | DA_18_Diana | -0.6400 |  |
| Jogador 3 | 6-2 | 19:37:26 | MOVE Bench -> Board: Diana (i:6.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Devastador | DA_18_Diana | 0.0800 |  |
| Jogador 3 | 6-2 | 19:37:26 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Devastador | DA_18_Diana | -0.1000 |  |
| Jogador 3 | 6-3 | 19:37:35 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | -0.7100 |  |
| Jogador 3 | 6-3 | 19:37:35 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 168 | 5 | Devastador | DA_18_Diana | -0.4700 |  |
| Jogador 3 | 6-3 | 19:37:35 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | 0.3800 |  |
| Jogador 3 | 6-3 | 19:37:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | 0.1000 |  |
| Jogador 3 | 6-3 | 19:37:36 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | -0.4100 |  |
| Jogador 3 | 6-3 | 19:37:36 | MOVE Bench -> Board: Diana (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | 0.0300 |  |
| Jogador 3 | 6-3 | 19:37:36 | MOVE Bench -> Board: Akali (i:2.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | 0.0800 |  |
| Jogador 3 | 6-3 | 19:37:37 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | -0.4100 |  |
| Jogador 3 | 6-3 | 19:37:37 | MOVE Bench -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Devastador | DA_18_Diana | 0.1000 |  |
| Jogador 3 | 6-4 | 19:37:47 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Devastador | DA_18_Diana | 0.0300 |  |
| Jogador 3 | 6-4 | 19:37:48 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Devastador | DA_18_Diana | -0.7600 |  |
| Jogador 3 | 6-4 | 19:37:48 | MOVE Bench -> Board: Akali (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Devastador | DA_18_Diana | 0.0800 |  |
| Jogador 3 | 6-4 | 19:37:48 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Devastador | DA_18_Diana | 0.0400 |  |
| Jogador 3 | 6-4 | 19:37:48 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Devastador | DA_18_Diana | -0.7600 |  |
| Jogador 3 | 6-4 | 19:37:49 | MOVE Bench -> Board: Akali (i:2.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Devastador | DA_18_Diana | -0.4000 |  |
| Jogador 3 | 6-4 | 19:37:49 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Devastador | DA_18_Diana | -0.2100 |  |
| Jogador 3 | 6-5 | 19:38:01 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 190 | 5 | Devastador | DA_18_Diana | 0.6000 |  |
| Jogador 3 | 6-5 | 19:38:02 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Devastador | DA_18_Diana | 0.9500 |  |
| Jogador 3 | 6-5 | 19:38:02 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Devastador | DA_18_Diana | 0.0000 |  |
| Jogador 3 | 6-5 | 19:38:02 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Devastador | DA_18_Diana | -0.0100 |  |
| Jogador 3 | 6-5 | 19:38:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 189 | 5 | Devastador | DA_18_Diana | -0.2300 |  |
| Jogador 3 | 6-6 | 19:38:13 | VENDEU: Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 202 | 5 | Devastador | DA_18_Diana | -0.2400 |  |
| Jogador 3 | 6-6 | 19:38:13 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 200 | 5 | Devastador | DA_Murkwolf18 | 1.0100 |  |
| Jogador 3 | 6-6 | 19:38:13 | COMPROU: Elise (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 198 | 5 | Devastador | DA_Murkwolf18 | 0.2800 |  |
| Jogador 3 | 6-6 | 19:38:14 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 198 | 5 | Devastador | DA_Murkwolf18 | 0.0000 |  |
| Jogador 3 | 6-6 | 19:38:14 | MOVE Board -> Board: Akali (i:2.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 198 | 5 | Devastador | DA_Murkwolf18 | -0.0200 |  |
| Jogador 3 | 6-6 | 19:38:14 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 198 | 5 | Devastador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 3 | 6-6 | 19:38:14 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 198 | 5 | Devastador | DA_Murkwolf18 | -0.4000 |  |
| Jogador 3 | 6-7 | 19:38:25 | EQUIP_FROM_INVENTORY: TFT_Item_Deathblade -> Diana (i:6.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 209 | 5 | Devastador | DA_Murkwolf18 | 0.0700 |  |
| Jogador 3 | 6-7 | 19:38:26 | COMPROU: Warwick (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 207 | 5 | Devastador | DA_Murkwolf18 | 1.0100 |  |
| Jogador 3 | 6-7 | 19:38:26 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 204 | 5 | Devastador | DA_Fiddlesticks18 | 1.0100 |  |
| Jogador 3 | 6-7 | 19:38:26 | MOVE Bench -> Board: Akali (i:2.0) <-> Hecarim (i:6.0) | STABILIZE | STABILIZE: excedente alto e tabuleiro fraco no late game | 204 | 5 | Devastador | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 3 | 6-7 | 19:38:26 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 204 | 5 | Devastador | DA_Fiddlesticks18 | 0.3900 |  |
| Jogador 3 | 6-7 | 19:38:27 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 204 | 5 | Devastador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 3 | 6-7 | 19:38:27 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Hecarim (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 204 | 5 | Devastador | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 3 | 6-7 | 19:38:27 | MOVE Bench -> Board: Hecarim (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 204 | 5 | Devastador | DA_Fiddlesticks18 | -0.0800 |  |
| Jogador 3 | 6-7 | 19:38:27 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Diana (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 204 | 5 | Devastador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 3 | 7-1 | 19:38:37 | COMPROU: Vi (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 214 | 5 | Devastador | DA_Fiddlesticks18 | -0.0700 |  |
| Jogador 3 | 7-1 | 19:38:38 | COMPROU: Sivir (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 210 | 5 | Devastador | DA_Fiddlesticks18 | -0.2500 |  |
| Jogador 3 | 7-1 | 19:38:38 | MOVE Board -> Board: Diana (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 210 | 5 | Devastador | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 3 | 7-1 | 19:38:38 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Akali (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 210 | 5 | Devastador | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 3 | 7-1 | 19:38:38 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 210 | 5 | Devastador | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 4 | ? | 19:32:17 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3500 |  |
| Jogador 4 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 19:32:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2700 |  |
| Jogador 4 | 1-1 | 19:32:24 | MOVE Bench -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.7100 |  |
| Jogador 4 | 1-1 | 19:32:24 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.4300 |  |
| Jogador 4 | 1-1 | 19:32:25 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0400 |  |
| Jogador 4 | 1-1 | 19:32:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.0400 |  |
| Jogador 4 | 1-1 | 19:32:25 | MOVE Bench -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.7300 |  |
| Jogador 4 | 1-1 | 19:32:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-1 | 19:32:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.4800 |  |
| Jogador 4 | 1-2 | 19:32:30 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1700 |  |
| Jogador 4 | 1-2 | 19:32:30 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0600 |  |
| Jogador 4 | 1-2 | 19:32:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 1-2 | 19:32:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0100 |  |
| Jogador 4 | 1-2 | 19:32:31 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 1-2 | 19:32:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0500 |  |
| Jogador 4 | 1-2 | 19:32:32 | MOVE Board -> Board: Rakan (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 1-2 | 19:32:32 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 1-2 | 19:32:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 19:32:33 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-2 | 19:32:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 4 | 1-3 | 19:32:37 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 1.0100 |  |
| Jogador 4 | 1-3 | 19:32:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 4 | 1-3 | 19:32:37 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.9800 |  |
| Jogador 4 | 1-3 | 19:32:37 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-3 | 19:32:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 4 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 1-4 | 19:32:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.9800 |  |
| Jogador 4 | 1-4 | 19:32:43 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.3900 |  |
| Jogador 4 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.1600 |  |
| Jogador 4 | 1-4 | 19:32:44 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | 0.1200 |  |
| Jogador 4 | 1-4 | 19:32:44 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.8500 |  |
| Jogador 4 | 1-4 | 19:32:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.2200 |  |
| Jogador 4 | 1-4 | 19:32:45 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.0700 |  |
| Jogador 4 | 1-4 | 19:32:46 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1800 |  |
| Jogador 4 | 1-4 | 19:32:46 | MOVE Board -> Board: Ornn (i:2.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 1-4 | 19:32:46 | MOVE Board -> Board: Camille (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 2-1 | 19:32:50 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9500 |  |
| Jogador 4 | 2-1 | 19:32:50 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 4 | 2-1 | 19:32:51 | MOVE Bench -> Board: Ornn (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.8300 |  |
| Jogador 4 | 2-1 | 19:32:51 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.5800 |  |
| Jogador 4 | 2-1 | 19:32:51 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.3000 |  |
| Jogador 4 | 2-1 | 19:32:51 | MOVE Board -> Board: Yorick (i:2.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-1 | 19:32:52 | MOVE Board -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 2-1 | 19:32:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-2 | 19:32:56 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 4 | 2-2 | 19:32:57 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 4 | 2-2 | 19:32:57 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 2-2 | 19:32:57 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.9500 |  |
| Jogador 4 | 2-2 | 19:32:58 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.8400 |  |
| Jogador 4 | 2-2 | 19:32:58 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 2-2 | 19:32:58 | EQUIP_FROM_INVENTORY: TFT_Item_Leviathan -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1300 |  |
| Jogador 4 | 2-2 | 19:32:59 | EQUIP_FROM_INVENTORY: TFT_Item_AdaptiveHelm -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | 0.1000 |  |
| Jogador 4 | 2-2 | 19:32:59 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 2-2 | 19:33:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.9000 |  |
| Jogador 4 | 2-2 | 19:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-3 | 19:33:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9500 |  |
| Jogador 4 | 2-3 | 19:33:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Xayah | 0.3300 |  |
| Jogador 4 | 2-3 | 19:33:04 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.1500 |  |
| Jogador 4 | 2-3 | 19:33:04 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | -0.0200 |  |
| Jogador 4 | 2-3 | 19:33:05 | MOVE Bench -> Board: Ornn (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.5100 |  |
| Jogador 4 | 2-3 | 19:33:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.1600 |  |
| Jogador 4 | 2-3 | 19:33:05 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.9000 |  |
| Jogador 4 | 2-3 | 19:33:05 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Akali_AD | -0.2500 |  |
| Jogador 4 | 2-3 | 19:33:06 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 0.9000 |  |
| Jogador 4 | 2-3 | 19:33:07 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 2-3 | 19:33:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-4 | 19:33:11 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Sabugueiro | DA_18_Rakan | -0.2100 |  |
| Jogador 4 | 2-4 | 19:33:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_18_Rakan | 0.1600 |  |
| Jogador 4 | 2-4 | 19:33:11 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Sabugueiro | DA_18_LeBlanc | -0.1900 |  |
| Jogador 4 | 2-4 | 19:33:11 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Sabugueiro | DA_18_Akali_AD | 0.7000 |  |
| Jogador 4 | 2-4 | 19:33:12 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Sabugueiro | DA_18_Akali_AD | 0.2000 |  |
| Jogador 4 | 2-4 | 19:33:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Sabugueiro | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 2-4 | 19:33:13 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Sabugueiro | DA_18_Akali_AD | 0.9500 |  |
| Jogador 4 | 2-4 | 19:33:14 | MOVE Bench -> Board: Xayah (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Sabugueiro | DA_18_Akali_AD | 0.1300 |  |
| Jogador 4 | 2-4 | 19:33:14 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_18_Akali_AD | 0.1400 |  |
| Jogador 4 | 2-4 | 19:33:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_18_Akali_AD | 0.4100 |  |
| Jogador 4 | 2-4 | 19:33:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Sabugueiro | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-5 | 19:33:18 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_18_Akali_AD | 0.1400 |  |
| Jogador 4 | 2-5 | 19:33:18 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_18_Akali_AD | -0.3900 |  |
| Jogador 4 | 2-5 | 19:33:19 | MOVE Bench -> Board: Akali (i:2.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_18_Akali_AD | -0.4100 |  |
| Jogador 4 | 2-5 | 19:33:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 2-5 | 19:33:24 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Sabugueiro | DA_18_Akali_AD | 0.4000 |  |
| Jogador 4 | 2-6 | 19:33:26 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | 0.9500 |  |
| Jogador 4 | 2-6 | 19:33:26 | MOVE Bench -> Board: Akali (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | 0.0600 |  |
| Jogador 4 | 2-6 | 19:33:26 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | -0.3100 |  |
| Jogador 4 | 2-6 | 19:33:26 | MOVE Bench -> Board: Akali (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | 0.0400 |  |
| Jogador 4 | 2-6 | 19:33:26 | MOVE Bench -> Board: Akali (i:2.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | -0.7300 |  |
| Jogador 4 | 2-6 | 19:33:27 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | -0.3100 |  |
| Jogador 4 | 2-6 | 19:33:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-6 | 19:33:31 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Sabugueiro | DA_18_Akali_AD | 0.5700 |  |
| Jogador 4 | 2-7 | 19:33:34 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Sabugueiro | DA_18_Akali_AD | 0.7200 |  |
| Jogador 4 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Sabugueiro | DA_18_Akali_AD | 0.2200 |  |
| Jogador 4 | 2-7 | 19:33:34 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Sabugueiro | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 2-7 | 19:33:34 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Sabugueiro | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 2-7 | 19:33:35 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Sabugueiro | DA_18_Akali_AD | 0.8400 |  |
| Jogador 4 | 2-7 | 19:33:35 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | 0.7900 |  |
| Jogador 4 | 2-7 | 19:33:35 | MOVE Bench -> Board: Akali (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | 0.0600 |  |
| Jogador 4 | 2-7 | 19:33:35 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | -0.3700 |  |
| Jogador 4 | 2-7 | 19:33:36 | MOVE Bench -> Board: Akali (i:4.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | -0.2500 |  |
| Jogador 4 | 2-7 | 19:33:37 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 2-7 | 19:33:39 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | -0.0900 |  |
| Jogador 4 | 3-1 | 19:33:42 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Sabugueiro | DA_18_Akali_AD | 0.2900 |  |
| Jogador 4 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Sabugueiro | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Sabugueiro | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Sabugueiro | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Sabugueiro | DA_18_Akali_AD | -0.2400 |  |
| Jogador 4 | 3-1 | 19:33:44 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | 0.0100 |  |
| Jogador 4 | 3-1 | 19:33:44 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Sabugueiro | DA_18_Akali_AD | 0.8100 |  |
| Jogador 4 | 3-1 | 19:33:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 1 | Sabugueiro | DA_18_Akali_AD | -0.2400 |  |
| Jogador 4 | 3-1 | 19:33:44 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | -0.1800 |  |
| Jogador 4 | 3-1 | 19:33:46 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Sejuani (i:4.0) (tabuleiro slot 24) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | 0.1000 |  |
| Jogador 4 | 3-1 | 19:33:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Sabugueiro | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-2 | 19:33:52 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Sabugueiro | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-2 | 19:33:52 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Sabugueiro | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-2 | 19:33:52 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Sabugueiro | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-2 | 19:33:53 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Sabugueiro | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-2 | 19:33:53 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Sabugueiro | DA_18_Akali_AD | 0.8200 |  |
| Jogador 4 | 3-2 | 19:33:53 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Sabugueiro | DA_18_Akali_AD | -0.3400 |  |
| Jogador 4 | 3-2 | 19:33:54 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Sabugueiro | DA_18_Akali_AD | -0.8400 |  |
| Jogador 4 | 3-2 | 19:33:54 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Sabugueiro | DA_18_Akali_AD | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 3-2 | 19:33:57 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Sabugueiro | DA_18_Akali_AD | 0.5900 |  |
| Jogador 4 | 3-3 | 19:34:00 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-3 | 19:34:00 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 1 | Colosso | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 1 | Colosso | DA_18_Akali_AD | -0.2400 |  |
| Jogador 4 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 1 | Colosso | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 1 | Colosso | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 1 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 1 | Colosso | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-3 | 19:34:05 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 1 | Colosso | DA_18_Akali_AD | -0.0600 |  |
| Jogador 4 | 3-3 | 19:34:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 1 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-4 | 19:34:10 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 4 | 3-4 | 19:34:11 | MOVE Bench -> Board: Akali (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | -0.3300 |  |
| Jogador 4 | 3-4 | 19:34:11 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.5100 |  |
| Jogador 4 | 3-4 | 19:34:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-4 | 19:34:12 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.2800 |  |
| Jogador 4 | 3-4 | 19:34:12 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0100 |  |
| Jogador 4 | 3-4 | 19:34:12 | MOVE Board -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 3-4 | 19:34:13 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | -0.0200 |  |
| Jogador 4 | 3-4 | 19:34:13 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-5 | 19:34:19 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 4 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.2200 |  |
| Jogador 4 | 3-5 | 19:34:20 | MOVE Board -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 19:34:22 | MOVE Board -> Board: Sejuani (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.0100 |  |
| Jogador 4 | 3-5 | 19:34:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-6 | 19:34:30 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8000 |  |
| Jogador 4 | 3-6 | 19:34:30 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Akali_AD | -0.2300 |  |
| Jogador 4 | 3-6 | 19:34:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.8400 |  |
| Jogador 4 | 3-6 | 19:34:31 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Akali_AD | 0.4500 |  |
| Jogador 4 | 3-6 | 19:34:31 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-6 | 19:34:31 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Akali_AD | 0.2800 |  |
| Jogador 4 | 3-6 | 19:34:32 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-6 | 19:34:32 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.8400 |  |
| Jogador 4 | 3-6 | 19:34:32 | MOVE Bench -> Board: Akali (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | -0.5900 |  |
| Jogador 4 | 3-6 | 19:34:35 | MOVE Bench -> Board: Akali (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.1800 |  |
| Jogador 4 | 3-6 | 19:34:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Akali_AD | 0.0000 |  |
| Jogador 4 | 3-7 | 19:34:39 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.8100 |  |
| Jogador 4 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.2500 |  |
| Jogador 4 | 3-7 | 19:34:40 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Akali_AD | 0.2100 |  |
| Jogador 4 | 3-7 | 19:34:40 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Akali_AD | -0.1600 |  |
| Jogador 4 | 3-7 | 19:34:40 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Yorick | -0.4000 |  |
| Jogador 4 | 3-7 | 19:34:44 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Yorick | 0.2800 |  |
| Jogador 4 | 3-7 | 19:34:44 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Yorick | -0.3300 |  |
| Jogador 4 | 3-7 | 19:34:44 | MOVE Bench -> Board: LeBlanc (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Yorick | 0.4400 |  |
| Jogador 4 | 3-7 | 19:34:44 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Yorick (i:2.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Yorick | 0.1600 |  |
| Jogador 4 | 3-7 | 19:34:45 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Yorick | 0.8000 |  |
| Jogador 4 | 3-7 | 19:34:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-1 | 19:34:48 | MOVE Bench -> Board: Yorick (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Yorick | 0.1000 |  |
| Jogador 4 | 4-1 | 19:34:48 | MOVE Bench -> Board: Akali (i:2.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Yorick | -0.5800 |  |
| Jogador 4 | 4-1 | 19:34:48 | MOVE Bench -> Board: Akali (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Yorick | -0.3800 |  |
| Jogador 4 | 4-1 | 19:34:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Yorick | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 4 | 4-1 | 19:34:53 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Colosso | DA_18_Yorick | 0.4300 |  |
| Jogador 4 | 4-2 | 19:35:00 | REROLL | STABILIZE | STABILIZE: pressão de vida | 18 | 1 | Colosso | DA_18_Yorick | -0.2300 |  |
| Jogador 4 | 4-2 | 19:35:01 | REROLL | STABILIZE | STABILIZE: pressão de vida | 16 | 1 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-2 | 19:35:01 | REROLL | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Colosso | DA_18_Yorick | -0.1500 |  |
| Jogador 4 | 4-2 | 19:35:01 | REROLL | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Colosso | DA_18_Yorick | -0.1500 |  |
| Jogador 4 | 4-2 | 19:35:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Colosso | DA_18_Yorick | -0.1500 |  |
| Jogador 4 | 4-2 | 19:35:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 8 | 1 | Colosso | DA_18_Yorick | -0.1700 |  |
| Jogador 4 | 4-2 | 19:35:02 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 5 | 1 | Colosso | DA_18_Yorick | 0.7900 |  |
| Jogador 4 | 4-2 | 19:35:02 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 1 | Colosso | DA_18_Yorick | -0.1500 |  |
| Jogador 4 | 4-2 | 19:35:03 | REROLL | STABILIZE | STABILIZE: pressão de vida | 1 | 1 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-2 | 19:35:06 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 1 | Colosso | DA_18_Yorick | 0.8000 |  |
| Jogador 4 | 4-3 | 19:35:10 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-3 | 19:35:10 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-3 | 19:35:10 | VENDEU: Kayle (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Yorick | -0.1400 |  |
| Jogador 4 | 4-3 | 19:35:11 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Yorick | 0.2800 |  |
| Jogador 4 | 4-3 | 19:35:11 | MOVE Board -> Board: Akali (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_LeBlanc | 0.0100 |  |
| Jogador 4 | 4-3 | 19:35:12 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-3 | 19:35:12 | MOVE Board -> Board: Sejuani (i:4.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 4-3 | 19:35:12 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Yorick | -0.1500 |  |
| Jogador 4 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Yorick | -0.1500 |  |
| Jogador 4 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-4 | 19:35:20 | MOVE Board -> Board: Akali (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_LeBlanc | 0.0000 |  |
| Jogador 4 | 4-4 | 19:35:21 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_LeBlanc | -0.0200 |  |
| Jogador 4 | 4-4 | 19:35:21 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_LeBlanc | -0.0100 |  |
| Jogador 4 | 4-4 | 19:35:21 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_LeBlanc | 0.0000 |  |
| Jogador 4 | 4-5 | 19:35:29 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 8 | 0 | Colosso | DA_18_Yorick | -0.2400 |  |
| Jogador 4 | 4-5 | 19:35:30 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_18_Yorick | 0.8400 |  |
| Jogador 4 | 4-5 | 19:35:30 | MOVE Bench -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 7 | 0 | Colosso | DA_18_Yorick | 0.4000 |  |
| Jogador 4 | 4-5 | 19:35:30 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-5 | 19:35:31 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Yorick | 0.8400 |  |
| Jogador 4 | 4-5 | 19:35:31 | MOVE Bench -> Board: Sejuani (i:8.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_18_Yorick | 0.1000 |  |
| Jogador 4 | 4-5 | 19:35:31 | REROLL | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Yorick | -0.1500 |  |
| Jogador 4 | 4-5 | 19:35:35 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Yorick | 0.4000 |  |
| Jogador 4 | 4-5 | 19:35:35 | MOVE Board -> Board: Sejuani (i:8.0) <-> Akali (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 4-5 | 19:35:35 | MOVE Board -> Board: Akali (i:4.0) <-> LeBlanc (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_18_Yorick | -0.0200 |  |
| Jogador 4 | 4-6 | 19:35:39 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-6 | 19:35:39 | COMPROU: Leona (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Colosso | DA_18_Yorick | 0.8100 |  |
| Jogador 4 | 4-6 | 19:35:40 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_18_Yorick | 0.2700 |  |
| Jogador 4 | 4-6 | 19:35:40 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-6 | 19:35:40 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | 0.2100 |  |
| Jogador 4 | 4-6 | 19:35:40 | MOVE Board -> Board: Vi (i:6.0) <-> Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 4-6 | 19:35:45 | MOVE Board -> Board: Sejuani (i:8.0) <-> Akali (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 4-6 | 19:35:45 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | -0.0500 |  |
| Jogador 4 | 4-7 | 19:35:49 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Colosso | DA_18_Yorick | 0.8300 |  |
| Jogador 4 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Colosso | DA_18_Yorick | 0.2000 |  |
| Jogador 4 | 4-7 | 19:35:50 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_TearOfTheGoddess -> Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 6 | 0 | Colosso | DA_18_Yorick | 0.1500 |  |
| Jogador 4 | 4-7 | 19:35:50 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 4 | 0 | Colosso | DA_18_Yorick | 0.3000 |  |
| Jogador 4 | 4-7 | 19:35:50 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 2 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-7 | 19:35:51 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 4-7 | 19:35:55 | MOVE Board -> Board: Akali (i:4.0) <-> LeBlanc (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Yorick | -0.0300 |  |
| Jogador 4 | 4-7 | 19:35:55 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Yorick | -0.2400 |  |
| Jogador 4 | 4-7 | 19:35:55 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 0 | 0 | Colosso | DA_18_Yorick | -0.0500 |  |
| Jogador 4 | 5-1 | 19:35:59 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 5 | 0 | Colosso | DA_18_Yorick | 0.2800 |  |
| Jogador 4 | 5-1 | 19:36:00 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 3 | 0 | Colosso | DA_18_Yorick | -0.0900 |  |
| Jogador 4 | 5-1 | 19:36:00 | COMPROU: Kayle (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | 0.7300 |  |
| Jogador 4 | 5-1 | 19:36:00 | MOVE Board -> Board: Akali (i:2.0) <-> Sejuani (i:8.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | 0.0000 |  |
| Jogador 4 | 5-1 | 19:36:00 | MOVE Board -> Board: Sejuani (i:8.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | -0.0100 |  |
| Jogador 4 | 5-1 | 19:36:01 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 1 | 0 | Colosso | DA_18_Yorick | -0.0500 |  |
| Jogador 5 | ? | 19:32:17 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.3200 |  |
| Jogador 5 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 19:32:24 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1100 |  |
| Jogador 5 | 1-1 | 19:32:24 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.6400 |  |
| Jogador 5 | 1-1 | 19:32:24 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.4200 |  |
| Jogador 5 | 1-1 | 19:32:25 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.2700 |  |
| Jogador 5 | 1-1 | 19:32:25 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0900 |  |
| Jogador 5 | 1-1 | 19:32:25 | MOVE Bench -> Board: Veigar (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.5700 |  |
| Jogador 5 | 1-1 | 19:32:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-1 | 19:32:29 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4000 |  |
| Jogador 5 | 1-2 | 19:32:30 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2800 |  |
| Jogador 5 | 1-2 | 19:32:30 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0600 |  |
| Jogador 5 | 1-2 | 19:32:31 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 5 | 1-2 | 19:32:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0200 |  |
| Jogador 5 | 1-2 | 19:32:31 | MOVE Board -> Board: Veigar (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 5 | 1-2 | 19:32:32 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0900 |  |
| Jogador 5 | 1-2 | 19:32:32 | MOVE Board -> Board: Yorick (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0100 |  |
| Jogador 5 | 1-2 | 19:32:32 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0100 |  |
| Jogador 5 | 1-2 | 19:32:32 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 5 | 1-2 | 19:32:33 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.3300 |  |
| Jogador 5 | 1-2 | 19:32:33 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 5 | 1-3 | 19:32:37 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | 0.3200 |  |
| Jogador 5 | 1-3 | 19:32:37 | MOVE Bench -> Board: Leona (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | -0.0900 |  |
| Jogador 5 | 1-3 | 19:32:37 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.3400 |  |
| Jogador 5 | 1-3 | 19:32:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 1-3 | 19:32:38 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0100 |  |
| Jogador 5 | 1-3 | 19:32:38 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.0100 |  |
| Jogador 5 | 1-3 | 19:32:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.0400 |  |
| Jogador 5 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 1-4 | 19:32:43 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.9700 |  |
| Jogador 5 | 1-4 | 19:32:43 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.5400 |  |
| Jogador 5 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.1900 |  |
| Jogador 5 | 1-4 | 19:32:44 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | 0.1600 |  |
| Jogador 5 | 1-4 | 19:32:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Sejuani | -0.4000 |  |
| Jogador 5 | 1-4 | 19:32:44 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Sejuani | 0.2600 |  |
| Jogador 5 | 1-4 | 19:32:45 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.2200 |  |
| Jogador 5 | 1-4 | 19:32:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 1-4 | 19:32:46 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | -0.0200 |  |
| Jogador 5 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sejuani | 0.0000 |  |
| Jogador 5 | 2-1 | 19:32:50 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.9800 |  |
| Jogador 5 | 2-1 | 19:32:50 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.7500 |  |
| Jogador 5 | 2-1 | 19:32:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-1 | 19:32:51 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1500 |  |
| Jogador 5 | 2-1 | 19:32:51 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.0600 |  |
| Jogador 5 | 2-1 | 19:32:51 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1300 |  |
| Jogador 5 | 2-1 | 19:32:52 | MOVE Board -> Board: Yorick (i:2.0) <-> Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-1 | 19:32:52 | MOVE Board -> Board: Leona (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-1 | 19:32:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-2 | 19:32:56 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 0.7600 |  |
| Jogador 5 | 2-2 | 19:32:57 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-2 | 19:32:57 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 0.0100 |  |
| Jogador 5 | 2-2 | 19:32:57 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-2 | 19:32:58 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-2 | 19:32:58 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | 0.6900 |  |
| Jogador 5 | 2-2 | 19:32:58 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-2 | 19:32:59 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Ornn | 0.8900 |  |
| Jogador 5 | 2-2 | 19:32:59 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Ornn | -0.1600 |  |
| Jogador 5 | 2-2 | 19:33:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.9500 |  |
| Jogador 5 | 2-2 | 19:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-3 | 19:33:04 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | — | DA_18_Rakan | 0.9200 |  |
| Jogador 5 | 2-3 | 19:33:04 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 0.3300 |  |
| Jogador 5 | 2-3 | 19:33:04 | MOVE Bench -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Rakan | 0.6400 |  |
| Jogador 5 | 2-3 | 19:33:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-3 | 19:33:05 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Rakan | 0.8900 |  |
| Jogador 5 | 2-3 | 19:33:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Rakan | -0.2200 |  |
| Jogador 5 | 2-3 | 19:33:05 | COMPROU: Warwick (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2400 |  |
| Jogador 5 | 2-3 | 19:33:05 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-3 | 19:33:06 | VENDEU: Ornn (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Rakan | -0.2600 |  |
| Jogador 5 | 2-3 | 19:33:07 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3100 |  |
| Jogador 5 | 2-3 | 19:33:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-4 | 19:33:11 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | 0.1100 |  |
| Jogador 5 | 2-4 | 19:33:11 | VENDEU: Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | -0.1700 |  |
| Jogador 5 | 2-4 | 19:33:11 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | 0.1000 |  |
| Jogador 5 | 2-4 | 19:33:11 | VENDEU: Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | -0.0100 |  |
| Jogador 5 | 2-4 | 19:33:12 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | 0.8400 |  |
| Jogador 5 | 2-4 | 19:33:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-4 | 19:33:13 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | 0.0100 |  |
| Jogador 5 | 2-4 | 19:33:14 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.0100 |  |
| Jogador 5 | 2-4 | 19:33:14 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-4 | 19:33:14 | VENDEU: Warwick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-4 | 19:33:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-5 | 19:33:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.0600 |  |
| Jogador 5 | 2-5 | 19:33:18 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.5700 |  |
| Jogador 5 | 2-5 | 19:33:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-5 | 19:33:19 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | 0.1700 |  |
| Jogador 5 | 2-5 | 19:33:20 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.3600 |  |
| Jogador 5 | 2-5 | 19:33:20 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.7200 |  |
| Jogador 5 | 2-5 | 19:33:21 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-5 | 19:33:21 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 5 | 2-5 | 19:33:21 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Rakan | -0.2700 |  |
| Jogador 5 | 2-5 | 19:33:22 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.1700 |  |
| Jogador 5 | 2-5 | 19:33:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-6 | 19:33:26 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | -0.3600 |  |
| Jogador 5 | 2-6 | 19:33:26 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.6600 |  |
| Jogador 5 | 2-6 | 19:33:26 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-6 | 19:33:26 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | -0.2700 |  |
| Jogador 5 | 2-6 | 19:33:26 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | 0.9400 |  |
| Jogador 5 | 2-6 | 19:33:27 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | 0.9400 |  |
| Jogador 5 | 2-6 | 19:33:27 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.6300 |  |
| Jogador 5 | 2-6 | 19:33:27 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 5 | 2-6 | 19:33:29 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.3300 |  |
| Jogador 5 | 2-6 | 19:33:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | 0.5600 |  |
| Jogador 5 | 2-6 | 19:33:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 2-7 | 19:33:34 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Rakan | 0.2300 |  |
| Jogador 5 | 2-7 | 19:33:34 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 5 | 2-7 | 19:33:34 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.0100 |  |
| Jogador 5 | 2-7 | 19:33:35 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-7 | 19:33:35 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.3300 |  |
| Jogador 5 | 2-7 | 19:33:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 2-7 | 19:33:35 | VENDEU: Leona (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | -0.2400 |  |
| Jogador 5 | 2-7 | 19:33:36 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | 0.6900 |  |
| Jogador 5 | 2-7 | 19:33:37 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 2-7 | 19:33:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-1 | 19:33:42 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | -0.3600 |  |
| Jogador 5 | 3-1 | 19:33:43 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | 0.2600 |  |
| Jogador 5 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 3-1 | 19:33:43 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.2700 |  |
| Jogador 5 | 3-1 | 19:33:44 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | 0.7800 |  |
| Jogador 5 | 3-1 | 19:33:44 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Rakan | -0.1900 |  |
| Jogador 5 | 3-1 | 19:33:44 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 3-1 | 19:33:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 5 | 3-1 | 19:33:46 | MOVE Board -> Board: LeBlanc (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0100 |  |
| Jogador 5 | 3-1 | 19:33:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-2 | 19:33:52 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | -0.3600 |  |
| Jogador 5 | 3-2 | 19:33:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | 0.2800 |  |
| Jogador 5 | 3-2 | 19:33:52 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 3-2 | 19:33:53 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Rakan | -0.1900 |  |
| Jogador 5 | 3-2 | 19:33:53 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | 0.5600 |  |
| Jogador 5 | 3-2 | 19:33:53 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 3-2 | 19:33:54 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Rakan | -0.2700 |  |
| Jogador 5 | 3-2 | 19:33:54 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yunara | 0.8300 |  |
| Jogador 5 | 3-2 | 19:33:54 | MOVE Board -> Board: Rakan (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 3-2 | 19:33:57 | MOVE Board -> Board: Yorick (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yunara | -0.0200 |  |
| Jogador 5 | 3-2 | 19:33:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Yunara | 0.0000 |  |
| Jogador 5 | 3-3 | 19:34:00 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Yunara | 0.8000 |  |
| Jogador 5 | 3-3 | 19:34:00 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Rakan | 0.2900 |  |
| Jogador 5 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Rakan | -0.2200 |  |
| Jogador 5 | 3-3 | 19:34:01 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Rakan | 0.0000 |  |
| Jogador 5 | 3-3 | 19:34:01 | VENDEU: Yunara (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Colosso | DA_18_Rakan | -0.2800 |  |
| Jogador 5 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 3-3 | 19:34:04 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Rakan | 0.8000 |  |
| Jogador 5 | 3-3 | 19:34:04 | VENDEU: Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Rakan | -0.3600 |  |
| Jogador 5 | 3-3 | 19:34:04 | COMPROU: Kayle (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Kayle | 0.7800 |  |
| Jogador 5 | 3-3 | 19:34:05 | MOVE Board -> Board: Yorick (i:2.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Kayle | 0.0000 |  |
| Jogador 5 | 3-3 | 19:34:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Kayle | 0.0000 |  |
| Jogador 5 | 3-4 | 19:34:10 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_18_Kayle | 0.6500 |  |
| Jogador 5 | 3-4 | 19:34:11 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Kayle | -0.1600 |  |
| Jogador 5 | 3-4 | 19:34:11 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Kayle | 0.2800 |  |
| Jogador 5 | 3-4 | 19:34:12 | MOVE Bench -> Board: Azir (i:6.0) <-> LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Kayle | 0.1000 |  |
| Jogador 5 | 3-4 | 19:34:12 | MOVE Bench -> Board: LeBlanc (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Kayle | -0.4100 |  |
| Jogador 5 | 3-4 | 19:34:12 | MOVE Bench -> Board: Yorick (i:2.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Kayle | -0.3000 |  |
| Jogador 5 | 3-4 | 19:34:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Colosso | DA_18_Kayle | 0.0000 |  |
| Jogador 5 | 3-5 | 19:34:19 | VENDEU: Kayle (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 3-5 | 19:34:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Rakan | 0.8400 |  |
| Jogador 5 | 3-5 | 19:34:19 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Rakan | 0.2100 |  |
| Jogador 5 | 3-5 | 19:34:20 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_18_Rakan | 0.5700 |  |
| Jogador 5 | 3-5 | 19:34:22 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Rakan | 0.6900 |  |
| Jogador 5 | 3-5 | 19:34:22 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Rakan | -0.1600 |  |
| Jogador 5 | 3-5 | 19:34:23 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Vi18 | 0.8300 |  |
| Jogador 5 | 3-5 | 19:34:23 | MOVE Bench -> Board: Karma (i:2.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Vi18 | -0.7200 |  |
| Jogador 5 | 3-5 | 19:34:23 | MOVE Bench -> Board: Azir (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Vi18 | 0.5200 |  |
| Jogador 5 | 3-5 | 19:34:24 | MOVE Bench -> Board: Azir (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Vi18 | 0.0800 |  |
| Jogador 5 | 3-5 | 19:34:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 5 | 3-6 | 19:34:30 | MOVE Bench -> Board: Karma (i:2.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Vi18 | -0.4000 |  |
| Jogador 5 | 3-6 | 19:34:30 | MOVE Bench -> Board: Azir (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 5 | 3-6 | 19:34:30 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Colosso | DA_Vi18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Vi18 | 0.1200 |  |
| Jogador 5 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_NeedlesslyLargeRod -> Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Vi18 | 0.2500 |  |
| Jogador 5 | 3-7 | 19:34:40 | MOVE Bench -> Board: Azir (i:6.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Vi18 | 0.0900 |  |
| Jogador 5 | 3-7 | 19:34:40 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Colosso | DA_Vi18 | -0.1600 |  |
| Jogador 5 | 3-7 | 19:34:40 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Vi18 | 0.8300 |  |
| Jogador 5 | 3-7 | 19:34:44 | MOVE Bench -> Board: Karma (i:2.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 5 | 3-7 | 19:34:44 | MOVE Bench -> Board: Azir (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 5 | 3-7 | 19:34:44 | MOVE Bench -> Board: LeBlanc (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Vi18 | 0.5200 |  |
| Jogador 5 | 3-7 | 19:34:44 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Colosso | DA_Vi18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-1 | 19:34:48 | MOVE Bench -> Board: Azir (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_Vi18 | 0.0900 |  |
| Jogador 5 | 4-1 | 19:34:48 | MOVE Bench -> Board: Karma (i:2.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 5 | 4-1 | 19:34:48 | MOVE Bench -> Board: Azir (i:6.0) <-> Azir (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 5 | 4-1 | 19:34:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Vi18 | -0.1100 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 5 | 4-1 | 19:34:53 | MOVE Bench -> Board: Vi (i:12.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 18 | 1 | Colosso | DA_Vi18 | 0.5900 |  |
| Jogador 5 | 4-2 | 19:35:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_Vi18 | 0.7100 |  |
| Jogador 5 | 4-2 | 19:35:01 | MOVE Bench -> Board: Azir (i:6.0) <-> Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_Vi18 | -0.4000 |  |
| Jogador 5 | 4-2 | 19:35:01 | MOVE Bench -> Board: Azir (i:6.0) <-> Karma (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_Vi18 | 0.0800 |  |
| Jogador 5 | 4-2 | 19:35:01 | MOVE Bench -> Board: Karma (i:2.0) <-> Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 5 | 4-2 | 19:35:02 | MOVE Bench -> Board: Azir (i:6.0) <-> Azir (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_Vi18 | -0.4100 |  |
| Jogador 5 | 4-2 | 19:35:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_Vi18 | -0.1100 |  |
| Jogador 5 | 4-2 | 19:35:06 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 24 | 1 | Colosso | DA_Vi18 | 0.4000 |  |
| Jogador 5 | 4-3 | 19:35:10 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 30 | 2 | Colosso | DA_Vi18 | 0.3200 |  |
| Jogador 5 | 4-3 | 19:35:10 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 28 | 2 | Colosso | DA_Vi18 | 0.7700 |  |
| Jogador 5 | 4-3 | 19:35:10 | REROLL | STABILIZE | STABILIZE: pressão de vida | 26 | 2 | Colosso | DA_Vi18 | -0.1500 |  |
| Jogador 5 | 4-3 | 19:35:11 | REROLL | STABILIZE | STABILIZE: pressão de vida | 24 | 2 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 4-3 | 19:35:11 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 22 | 2 | Colosso | DA_Vi18 | 0.8800 |  |
| Jogador 5 | 4-3 | 19:35:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 20 | 2 | Colosso | DA_Vi18 | -0.1500 |  |
| Jogador 5 | 4-3 | 19:35:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 18 | 2 | Colosso | DA_Vi18 | -0.2300 |  |
| Jogador 5 | 4-3 | 19:35:12 | REROLL | STABILIZE | STABILIZE: pressão de vida | 16 | 2 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 4-3 | 19:35:16 | REROLL | STABILIZE | STABILIZE: pressão de vida | 14 | 2 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 19 | 1 | Colosso | DA_Vi18 | -0.2300 |  |
| Jogador 5 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 17 | 1 | Colosso | DA_Vi18 | -0.1500 |  |
| Jogador 5 | 4-4 | 19:35:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 15 | 1 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 4-4 | 19:35:20 | COMPROU: Azir (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Colosso | DA_18_Azir | 0.8600 |  |
| Jogador 5 | 4-4 | 19:35:21 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Colosso | DA_18_Azir | 0.0600 |  |
| Jogador 5 | 4-4 | 19:35:21 | MOVE Bench -> Board: Karma (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Colosso | DA_18_Azir | 0.4000 |  |
| Jogador 5 | 4-4 | 19:35:21 | REROLL | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Colosso | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 4-4 | 19:35:21 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Colosso | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-4 | 19:35:25 | MOVE Bench -> Board: Yunara (i:8.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Colosso | DA_18_Azir | 0.0400 |  |
| Jogador 5 | 4-4 | 19:35:26 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 1 | Colosso | DA_18_Azir | 0.7800 |  |
| Jogador 5 | 4-5 | 19:35:29 | REROLL | STABILIZE | STABILIZE: pressão de vida | 14 | 1 | Colosso | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 4-5 | 19:35:30 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 12 | 1 | Colosso | DA_18_Azir | 0.3000 |  |
| Jogador 5 | 4-5 | 19:35:30 | REROLL | STABILIZE | STABILIZE: pressão de vida | 10 | 1 | Colosso | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 4-5 | 19:35:30 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 9 | 1 | Colosso | DA_18_Azir | 0.2300 |  |
| Jogador 5 | 4-5 | 19:35:31 | REROLL | STABILIZE | STABILIZE: pressão de vida | 7 | 1 | Colosso | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 4-5 | 19:35:31 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 1 | Colosso | DA_18_Azir | -0.1500 |  |
| Jogador 5 | 4-5 | 19:35:31 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 1 | Colosso | DA_18_Azir | 0.8100 |  |
| Jogador 5 | 4-5 | 19:35:35 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 1 | Colosso | DA_18_Azir | -0.1500 |  |
| Jogador 5 | 4-5 | 19:35:35 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 1 | Colosso | DA_18_Azir | -0.1500 |  |
| Jogador 5 | 4-5 | 19:35:35 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 1 | Colosso | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-6 | 19:35:39 | REROLL | STABILIZE | STABILIZE: pressão de vida | 5 | 0 | Colosso | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 4-6 | 19:35:39 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_18_Azir | 0.2800 |  |
| Jogador 5 | 4-6 | 19:35:40 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Azir | -0.1500 |  |
| Jogador 5 | 4-6 | 19:35:40 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-6 | 19:35:40 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Azir | -0.0200 |  |
| Jogador 5 | 4-6 | 19:35:40 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_18_Azir | 0.0000 |  |
| Jogador 5 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_RecurveBow + TFT_Item_GiantsBelt -> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Azir | 0.1600 |  |
| Jogador 5 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NeedlesslyLargeRod -> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 6 | 0 | Colosso | DA_18_Azir | 0.1100 |  |
| Jogador 5 | 4-7 | 19:35:50 | REROLL | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_18_Azir | -0.0900 |  |
| Jogador 5 | 4-7 | 19:35:50 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | 0.8000 |  |
| Jogador 5 | 4-7 | 19:35:50 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 5 | 4-7 | 19:35:51 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 5 | 4-7 | 19:35:55 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 5 | 4-7 | 19:35:55 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 5 | 5-1 | 19:35:59 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 4 | 0 | Colosso | DA_Vi18 | 0.7900 |  |
| Jogador 5 | 5-1 | 19:36:00 | REROLL | STABILIZE | STABILIZE: pressão de vida | 2 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-1 | 19:36:00 | REROLL | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-1 | 19:36:00 | MOVE Board -> Board: Rakan (i:4.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 5 | 5-1 | 19:36:00 | MOVE Board -> Board: Yunara (i:8.0) <-> LeBlanc (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 0 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 5 | 5-1 | 19:36:01 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 3 | 0 | Colosso | DA_Vi18 | -0.2500 |  |
| Jogador 5 | 5-1 | 19:36:05 | COMPROU: Yunara (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | 0.2900 |  |
| Jogador 5 | 5-1 | 19:36:05 | MOVE Board -> Board: LeBlanc (i:8.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | 0.0000 |  |
| Jogador 5 | 5-1 | 19:36:05 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 1 | 0 | Colosso | DA_Vi18 | -0.0100 |  |
| Jogador 5 | 5-2 | 19:36:09 | VENDEU: Azir (i:12.0) | ALL_IN | HP crítico: gastar para sobreviver | 15 | 0 | Colosso | DA_Vi18 | -0.2500 |  |
| Jogador 5 | 5-2 | 19:36:10 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 0 | Colosso | DA_Vi18 | 0.8000 |  |
| Jogador 5 | 5-2 | 19:36:10 | VENDEU: Yorick (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 16 | 0 | Colosso | DA_Vi18 | -0.3600 |  |
| Jogador 5 | 5-2 | 19:36:10 | COMPROU: Rakan (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 15 | 0 | Colosso | DA_Vi18 | 0.2800 |  |
| Jogador 5 | 5-2 | 19:36:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 13 | 0 | Colosso | DA_Vi18 | -0.0900 |  |
| Jogador 5 | 5-2 | 19:36:11 | VENDEU: Yunara (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 15 | 0 | Colosso | DA_Vi18 | -0.2600 |  |
| Jogador 5 | 5-2 | 19:36:15 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 13 | 0 | Colosso | DA_Vi18 | 0.8200 |  |
| Jogador 5 | 5-2 | 19:36:15 | COMPROU: Karma (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 12 | 0 | Colosso | DA_Vi18 | 0.8200 |  |
| Jogador 6 | ? | 19:32:17 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.1700 |  |
| Jogador 6 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Sentry | 0.0000 |  |
| Jogador 6 | 1-1 | 19:32:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.1700 |  |
| Jogador 6 | 1-1 | 19:32:24 | MOVE Bench -> Board: Yorick (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.2300 |  |
| Jogador 6 | 1-1 | 19:32:24 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 6 | 1-1 | 19:32:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.4000 |  |
| Jogador 6 | 1-1 | 19:32:25 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4400 |  |
| Jogador 6 | 1-1 | 19:32:25 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.2000 |  |
| Jogador 6 | 1-1 | 19:32:26 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.3500 |  |
| Jogador 6 | 1-1 | 19:32:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-1 | 19:32:29 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.4900 |  |
| Jogador 6 | 1-2 | 19:32:30 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.1900 |  |
| Jogador 6 | 1-2 | 19:32:30 | MOVE Bench -> Board: Teemo (i:4.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.3400 |  |
| Jogador 6 | 1-2 | 19:32:31 | MOVE Board -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 1-2 | 19:32:31 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-3 | 19:32:37 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 1.0000 |  |
| Jogador 6 | 1-3 | 19:32:37 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 1-3 | 19:32:37 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2000 |  |
| Jogador 6 | 1-3 | 19:32:37 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0300 |  |
| Jogador 6 | 1-3 | 19:32:38 | MOVE Board -> Board: Teemo (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 1-3 | 19:32:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 1-3 | 19:32:38 | MOVE Board -> Board: Yorick (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Teemo | -0.3400 |  |
| Jogador 6 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Teemo | 0.0000 |  |
| Jogador 6 | 1-4 | 19:32:43 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Teemo | 0.8900 |  |
| Jogador 6 | 1-4 | 19:32:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | 0.2800 |  |
| Jogador 6 | 1-4 | 19:32:43 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | 0.8900 |  |
| Jogador 6 | 1-4 | 19:32:44 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | 0.2100 |  |
| Jogador 6 | 1-4 | 19:32:44 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | 0.2000 |  |
| Jogador 6 | 1-4 | 19:32:44 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | 0.4100 |  |
| Jogador 6 | 1-4 | 19:32:45 | MOVE Bench -> Board: Karma (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | -0.0200 |  |
| Jogador 6 | 1-4 | 19:32:46 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.3800 |  |
| Jogador 6 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-1 | 19:32:50 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.5200 |  |
| Jogador 6 | 2-1 | 19:32:50 | MOVE Bench -> Board: Camille (i:2.0) <-> Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | -0.4000 |  |
| Jogador 6 | 2-1 | 19:32:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Yorick | -0.1600 |  |
| Jogador 6 | 2-1 | 19:32:51 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | 0.8800 |  |
| Jogador 6 | 2-1 | 19:32:51 | VENDEU: Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | -0.3300 |  |
| Jogador 6 | 2-1 | 19:32:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Teemo | -0.2200 |  |
| Jogador 6 | 2-1 | 19:32:52 | VENDEU: Karma (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Teemo | -0.5000 |  |
| Jogador 6 | 2-1 | 19:32:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.9500 |  |
| Jogador 6 | 2-1 | 19:32:52 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Teemo | -0.2900 |  |
| Jogador 6 | 2-1 | 19:32:52 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | 0.9200 |  |
| Jogador 6 | 2-1 | 19:32:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Teemo | 0.0000 |  |
| Jogador 6 | 2-2 | 19:32:56 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Yorick | 1.0500 |  |
| Jogador 6 | 2-2 | 19:32:57 | MOVE Bench -> Board: Yorick (i:4.0) <-> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Yorick | 0.1000 |  |
| Jogador 6 | 2-2 | 19:32:57 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Yorick | 0.1500 |  |
| Jogador 6 | 2-2 | 19:32:57 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 1.0400 |  |
| Jogador 6 | 2-2 | 19:32:58 | MOVE Bench -> Board: Camille (i:4.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | -0.7200 |  |
| Jogador 6 | 2-2 | 19:32:58 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Yorick | 0.3900 |  |
| Jogador 6 | 2-2 | 19:32:58 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | -0.1600 |  |
| Jogador 6 | 2-2 | 19:32:59 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.3500 |  |
| Jogador 6 | 2-2 | 19:32:59 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.0400 |  |
| Jogador 6 | 2-2 | 19:33:00 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.5400 |  |
| Jogador 6 | 2-2 | 19:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-3 | 19:33:04 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Yorick | 0.9800 |  |
| Jogador 6 | 2-3 | 19:33:04 | COMPROU: Karma (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.9800 |  |
| Jogador 6 | 2-3 | 19:33:04 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-3 | 19:33:04 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.0200 |  |
| Jogador 6 | 2-3 | 19:33:05 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2500 |  |
| Jogador 6 | 2-3 | 19:33:05 | MOVE Board -> Board: Camille (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.0300 |  |
| Jogador 6 | 2-3 | 19:33:05 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 2-3 | 19:33:05 | MOVE Board -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0200 |  |
| Jogador 6 | 2-3 | 19:33:06 | MOVE Board -> Board: Yorick (i:4.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.0100 |  |
| Jogador 6 | 2-3 | 19:33:07 | MOVE Board -> Board: Camille (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | -0.3700 |  |
| Jogador 6 | 2-3 | 19:33:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-4 | 19:33:11 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Emanador | DA_18_Yorick | 0.3600 |  |
| Jogador 6 | 2-4 | 19:33:11 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Emanador | DA_18_Yorick | 0.2900 |  |
| Jogador 6 | 2-4 | 19:33:11 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Emanador | DA_18_Yorick | 0.0900 |  |
| Jogador 6 | 2-4 | 19:33:11 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Emanador | DA_18_Yorick | -0.1600 |  |
| Jogador 6 | 2-4 | 19:33:12 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Yorick | 0.9000 |  |
| Jogador 6 | 2-4 | 19:33:12 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_18_Yorick | 0.9000 |  |
| Jogador 6 | 2-4 | 19:33:13 | MOVE Bench -> Board: Teemo (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_18_Yorick | -0.4000 |  |
| Jogador 6 | 2-4 | 19:33:14 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_18_Yorick | 0.0500 |  |
| Jogador 6 | 2-4 | 19:33:14 | VENDEU: Karma (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Emanador | DA_18_Yorick | -0.0200 |  |
| Jogador 6 | 2-4 | 19:33:14 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Yorick | -0.2200 |  |
| Jogador 6 | 2-4 | 19:33:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Yorick | 0.0000 |  |
| Jogador 6 | 2-5 | 19:33:18 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Emanador | DA_18_Yorick | 0.4200 |  |
| Jogador 6 | 2-5 | 19:33:18 | COMPROU: Vi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Emanador | DA_18_Yorick | 0.5100 |  |
| Jogador 6 | 2-5 | 19:33:19 | MOVE Bench -> Board: Vi (i:6.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Emanador | DA_18_Yorick | -0.3900 |  |
| Jogador 6 | 2-5 | 19:33:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Emanador | DA_18_Yorick | -0.1600 |  |
| Jogador 6 | 2-5 | 19:33:20 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Teemo | 0.9500 |  |
| Jogador 6 | 2-5 | 19:33:20 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Teemo | 0.5800 |  |
| Jogador 6 | 2-5 | 19:33:21 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Teemo | 0.0800 |  |
| Jogador 6 | 2-5 | 19:33:21 | MOVE Board -> Board: Yorick (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Teemo | -0.1700 |  |
| Jogador 6 | 2-5 | 19:33:21 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Teemo | -0.0100 |  |
| Jogador 6 | 2-5 | 19:33:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | Emanador | DA_18_Teemo | 0.0000 |  |
| Jogador 6 | 2-6 | 19:33:26 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Emanador | DA_18_Teemo | 0.9500 |  |
| Jogador 6 | 2-6 | 19:33:26 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Emanador | DA_18_Teemo | -0.1600 |  |
| Jogador 6 | 2-6 | 19:33:26 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Emanador | DA_18_Teemo | 0.3300 |  |
| Jogador 6 | 2-6 | 19:33:26 | MOVE Bench -> Board: Cascalho (i:4.0) <-> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Emanador | DA_18_Teemo | -0.2300 |  |
| Jogador 6 | 2-6 | 19:33:26 | MOVE Bench -> Board: Kog'Maw (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | Emanador | DA_18_Teemo | 0.5800 |  |
| Jogador 6 | 2-6 | 19:33:27 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_Sentinel18 | 0.3300 |  |
| Jogador 6 | 2-6 | 19:33:27 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_Sentinel18 | -0.2900 |  |
| Jogador 6 | 2-6 | 19:33:27 | MOVE Board -> Board: Azuporã (i:8.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_Sentinel18 | 0.2500 |  |
| Jogador 6 | 2-6 | 19:33:29 | MOVE Board -> Board: Kog'Maw (i:6.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 2-6 | 19:33:29 | MOVE Board -> Board: Vi (i:6.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_Sentinel18 | -0.0200 |  |
| Jogador 6 | 2-6 | 19:33:29 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Emanador | DA_Sentinel18 | 0.0000 |  |
| Jogador 6 | 2-7 | 19:33:34 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Emanador | DA_Sentinel18 | 0.2000 |  |
| Jogador 6 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NegatronCloak -> Kog'Maw (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Emanador | DA_Sentinel18 | 0.2400 |  |
| Jogador 6 | 2-7 | 19:33:34 | VENDEU: Camille (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Emanador | DA_Sentinel18 | -0.1900 |  |
| Jogador 6 | 2-7 | 19:33:34 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Emanador | DA_Sentinel18 | 0.2300 |  |
| Jogador 6 | 2-7 | 19:33:35 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 2-7 | 19:33:35 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 2-7 | 19:33:35 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Emanador | DA_Sentinel18 | -0.3200 |  |
| Jogador 6 | 2-7 | 19:33:35 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Emanador | DA_Sentinel18 | 0.8000 |  |
| Jogador 6 | 2-7 | 19:33:36 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 2-7 | 19:33:37 | VENDEU: Teemo (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Emanador | DA_Sentinel18 | -0.3400 |  |
| Jogador 6 | 2-7 | 19:33:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Emanador | DA_Sentinel18 | 0.0000 |  |
| Jogador 6 | 3-1 | 19:33:42 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Emanador | DA_Sentinel18 | -0.0400 |  |
| Jogador 6 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-1 | 19:33:43 | VENDEU: Aronguejo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Emanador | DA_Sentinel18 | 0.0100 |  |
| Jogador 6 | 3-1 | 19:33:43 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 0 | Emanador | DA_Sentinel18 | 0.8100 |  |
| Jogador 6 | 3-1 | 19:33:43 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-1 | 19:33:44 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 0 | Emanador | DA_Sentinel18 | -0.2500 |  |
| Jogador 6 | 3-1 | 19:33:44 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Emanador | DA_KogMaw18_AD | 0.7500 |  |
| Jogador 6 | 3-1 | 19:33:44 | MOVE Bench -> Board: Akali (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Emanador | DA_KogMaw18_AD | -0.3500 |  |
| Jogador 6 | 3-1 | 19:33:44 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Emanador | DA_KogMaw18_AD | 0.1800 |  |
| Jogador 6 | 3-1 | 19:33:46 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Emanador | DA_KogMaw18_AD | -0.1600 |  |
| Jogador 6 | 3-1 | 19:33:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Emanador | DA_KogMaw18_AD | 0.0000 |  |
| Jogador 6 | 3-2 | 19:33:52 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Emanador | DA_KogMaw18_AD | 0.4800 |  |
| Jogador 6 | 3-2 | 19:33:52 | VENDEU: Kog'Maw (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 0 | Emanador | DA_Sentinel18 | -0.2800 |  |
| Jogador 6 | 3-2 | 19:33:52 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Yorick (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 0 | Emanador | DA_Sentinel18 | 0.1400 |  |
| Jogador 6 | 3-2 | 19:33:53 | COMPROU: Hecarim (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 0 | Emanador | DA_Sentinel18 | 0.2300 |  |
| Jogador 6 | 3-2 | 19:33:53 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 0 | Emanador | DA_Sentinel18 | -0.2400 |  |
| Jogador 6 | 3-2 | 19:33:53 | VENDEU: Rubrivirim (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 0 | Emanador | DA_Sentinel18 | 0.0100 |  |
| Jogador 6 | 3-2 | 19:33:54 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Emanador | DA_Sentinel18 | 0.8000 |  |
| Jogador 6 | 3-2 | 19:33:54 | MOVE Bench -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Emanador | DA_Sentinel18 | 0.4000 |  |
| Jogador 6 | 3-2 | 19:33:54 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 0 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 3-2 | 19:33:57 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-2 | 19:33:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 0 | Emanador | DA_Sentinel18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-3 | 19:34:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Emanador | DA_Sentinel18 | 0.2900 |  |
| Jogador 6 | 3-3 | 19:34:00 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-3 | 19:34:01 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Emanador | DA_Sentinel18 | -0.2900 |  |
| Jogador 6 | 3-3 | 19:34:01 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Emanador | DA_Sentinel18 | 0.2900 |  |
| Jogador 6 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Sentinel18 | -0.2400 |  |
| Jogador 6 | 3-3 | 19:34:04 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Emanador | DA_Sentinel18 | -0.1800 |  |
| Jogador 6 | 3-3 | 19:34:04 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Sentinel18 | 0.2100 |  |
| Jogador 6 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Emanador | DA_Sentinel18 | -0.2200 |  |
| Jogador 6 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-3 | 19:34:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-3 | 19:34:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-4 | 19:34:10 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Emanador | DA_Sentinel18 | -0.2700 |  |
| Jogador 6 | 3-4 | 19:34:11 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Sentinel18 | 0.3000 |  |
| Jogador 6 | 3-4 | 19:34:11 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-4 | 19:34:12 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Emanador | DA_Sentinel18 | -0.2700 |  |
| Jogador 6 | 3-4 | 19:34:12 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Emanador | DA_Sentinel18 | 0.8500 |  |
| Jogador 6 | 3-4 | 19:34:12 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Sentinel18 | 0.7700 |  |
| Jogador 6 | 3-4 | 19:34:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-4 | 19:34:13 | COMPROU: Azuporã (Custo 4 \| i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.8000 |  |
| Jogador 6 | 3-4 | 19:34:13 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.5500 |  |
| Jogador 6 | 3-4 | 19:34:15 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Emanador | DA_Sentinel18 | -0.2200 |  |
| Jogador 6 | 3-4 | 19:34:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Emanador | DA_Sentinel18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-5 | 19:34:19 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Emanador | DA_Sentinel18 | 0.3000 |  |
| Jogador 6 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Emanador | DA_Sentinel18 | -0.3000 |  |
| Jogador 6 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-5 | 19:34:20 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Emanador | DA_Sentinel18 | 0.8100 |  |
| Jogador 6 | 3-5 | 19:34:22 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-5 | 19:34:22 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Emanador | DA_Sentinel18 | -0.3700 |  |
| Jogador 6 | 3-5 | 19:34:23 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.2800 |  |
| Jogador 6 | 3-5 | 19:34:23 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-5 | 19:34:23 | VENDEU: Akali (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Emanador | DA_Sentinel18 | -0.3200 |  |
| Jogador 6 | 3-5 | 19:34:24 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Emanador | DA_Sentinel18 | 0.8100 |  |
| Jogador 6 | 3-5 | 19:34:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 12 | 1 | Emanador | DA_Sentinel18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-6 | 19:34:30 | VENDEU: Hecarim (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Emanador | DA_Sentinel18 | -0.1500 |  |
| Jogador 6 | 3-6 | 19:34:30 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Emanador | DA_Sentinel18 | 0.2900 |  |
| Jogador 6 | 3-6 | 19:34:30 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-6 | 19:34:31 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Emanador | DA_Sentinel18 | -0.2000 |  |
| Jogador 6 | 3-6 | 19:34:31 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Emanador | DA_Sentinel18 | 0.8500 |  |
| Jogador 6 | 3-6 | 19:34:31 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Emanador | DA_Sentinel18 | 0.8500 |  |
| Jogador 6 | 3-6 | 19:34:32 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Emanador | DA_Sentinel18 | -0.2400 |  |
| Jogador 6 | 3-6 | 19:34:32 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Emanador | DA_Sentinel18 | 0.2900 |  |
| Jogador 6 | 3-6 | 19:34:32 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-6 | 19:34:35 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.8300 |  |
| Jogador 6 | 3-6 | 19:34:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Sentinel18 | 0.1500 |  |
| Jogador 6 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Emanador | DA_Sentinel18 | 0.1700 |  |
| Jogador 6 | 3-7 | 19:34:40 | COMPROU: Master Yi (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Emanador | DA_Sentinel18 | 0.1700 |  |
| Jogador 6 | 3-7 | 19:34:40 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-7 | 19:34:40 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Emanador | DA_Sentinel18 | 0.8000 |  |
| Jogador 6 | 3-7 | 19:34:44 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Emanador | DA_Sentinel18 | 0.6200 |  |
| Jogador 6 | 3-7 | 19:34:44 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.4800 |  |
| Jogador 6 | 3-7 | 19:34:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 1 | Emanador | DA_Sentinel18 | -0.1600 |  |
| Jogador 6 | 3-7 | 19:34:44 | VENDEU: Cascalho (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 1 | Emanador | DA_Sentinel18 | -0.3500 |  |
| Jogador 6 | 3-7 | 19:34:45 | COMPROU: Cascalho (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.8100 |  |
| Jogador 6 | 3-7 | 19:34:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 13 | 1 | Emanador | DA_Sentinel18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-1 | 19:34:48 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Emanador | DA_Sentinel18 | -0.2200 |  |
| Jogador 6 | 4-1 | 19:34:48 | MOVE Bench -> Board: Camille (i:2.0) <-> Cascalho (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Emanador | DA_Sentinel18 | -0.8200 |  |
| Jogador 6 | 4-1 | 19:34:48 | MOVE Bench -> Board: Cascalho (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Emanador | DA_Sentinel18 | -0.1700 |  |
| Jogador 6 | 4-1 | 19:34:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Emanador | DA_Sentinel18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 4-1 | 19:34:53 | MOVE Bench -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 21 | 1 | Emanador | DA_Sentinel18 | -0.1100 |  |
| Jogador 6 | 4-2 | 19:35:00 | MOVE Board -> Board: Camille (i:2.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Emanador | DA_Sentinel18 | 0.0000 |  |
| Jogador 6 | 4-2 | 19:35:01 | MOVE Board -> Board: Camille (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 4-2 | 19:35:01 | MOVE Board -> Board: Cascalho (i:2.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Emanador | DA_Sentinel18 | 0.2200 |  |
| Jogador 6 | 4-2 | 19:35:01 | MOVE Board -> Board: Camille (i:2.0) <-> Camille (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Emanador | DA_Sentinel18 | -0.0200 |  |
| Jogador 6 | 4-2 | 19:35:02 | MOVE Board -> Board: Camille (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 4-2 | 19:35:02 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 32 | 2 | Emanador | DA_Sentinel18 | -0.1800 |  |
| Jogador 6 | 4-3 | 19:35:10 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 43 | 3 | Emanador | DA_Sentinel18 | 0.8500 |  |
| Jogador 6 | 4-3 | 19:35:10 | MOVE Bench -> Board: Yorick (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Emanador | DA_Sentinel18 | 0.2300 |  |
| Jogador 6 | 4-3 | 19:35:10 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Emanador | DA_Sentinel18 | 0.4000 |  |
| Jogador 6 | 4-3 | 19:35:11 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 4-3 | 19:35:11 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Emanador | DA_Sentinel18 | -0.0200 |  |
| Jogador 6 | 4-3 | 19:35:12 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 43 | 3 | Emanador | DA_Sentinel18 | -0.1900 |  |
| Jogador 6 | 4-4 | 19:35:20 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Emanador | DA_Sentinel18 | 0.3000 |  |
| Jogador 6 | 4-4 | 19:35:20 | MOVE Board -> Board: Vi (i:6.0) <-> Cascalho (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 4-4 | 19:35:20 | MOVE Board -> Board: Cascalho (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 4-4 | 19:35:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 4 | Emanador | DA_Sentinel18 | -0.2200 |  |
| Jogador 6 | 4-5 | 19:35:29 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 63 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 4-5 | 19:35:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 59 | 5 | Emanador | DA_Sentinel18 | 0.0200 |  |
| Jogador 6 | 4-5 | 19:35:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 55 | 5 | Emanador | DA_Sentinel18 | 0.0200 |  |
| Jogador 6 | 4-5 | 19:35:30 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 5 | Emanador | DA_Sentinel18 | 0.0200 |  |
| Jogador 6 | 4-5 | 19:35:31 | MOVE Board -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 51 | 5 | Emanador | DA_Sentinel18 | 0.0000 |  |
| Jogador 6 | 4-5 | 19:35:31 | VENDEU: Yorick (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 5 | Emanador | DA_Sentinel18 | -0.1100 |  |
| Jogador 6 | 4-5 | 19:35:31 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Vi (i:6.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 4-5 | 19:35:35 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Vi (i:6.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 5 | Emanador | DA_Sentinel18 | 0.0700 |  |
| Jogador 6 | 4-5 | 19:35:35 | EQUIP_FROM_INVENTORY: TFT_Item_Bloodthirster -> Vi (i:6.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 54 | 5 | Emanador | DA_Sentinel18 | 0.1000 |  |
| Jogador 6 | 4-5 | 19:35:35 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 53 | 5 | Emanador | DA_Sentinel18 | 0.2600 |  |
| Jogador 6 | 4-6 | 19:35:39 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Emanador | DA_Sentinel18 | 0.8900 |  |
| Jogador 6 | 4-6 | 19:35:39 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Emanador | DA_Sentinel18 | 0.4700 |  |
| Jogador 6 | 4-6 | 19:35:40 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Emanador | DA_Sentinel18 | -0.0200 |  |
| Jogador 6 | 4-6 | 19:35:40 | MOVE Board -> Board: Vi (i:6.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 4-6 | 19:35:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 62 | 5 | Emanador | DA_Sentinel18 | -0.0900 |  |
| Jogador 6 | 4-7 | 19:35:49 | COMPROU: Aronguejo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Emanador | DA_Sentinel18 | 0.3100 |  |
| Jogador 6 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_NegatronCloak -> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Emanador | DA_Sentinel18 | 0.1500 |  |
| Jogador 6 | 4-7 | 19:35:50 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_TearOfTheGoddess -> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Emanador | DA_Sentinel18 | 0.1300 |  |
| Jogador 6 | 4-7 | 19:35:50 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Emanador | DA_Sentinel18 | -0.3900 |  |
| Jogador 6 | 4-7 | 19:35:50 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Azuporã (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Emanador | DA_Murkwolf18 | -0.7500 |  |
| Jogador 6 | 4-7 | 19:35:51 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 70 | 5 | Emanador | DA_Murkwolf18 | -0.2600 |  |
| Jogador 6 | 5-1 | 19:35:59 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Emanador | DA_Murkwolf18 | 0.8800 |  |
| Jogador 6 | 5-1 | 19:36:00 | MOVE Bench -> Board: Azuporã (i:8.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Emanador | DA_Murkwolf18 | 0.1200 |  |
| Jogador 6 | 5-1 | 19:36:00 | MOVE Bench -> Board: Aronguejo (i:4.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 79 | 5 | Emanador | DA_Murkwolf18 | -0.4000 |  |
| Jogador 6 | 5-1 | 19:36:00 | VENDEU: Camille (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-1 | 19:36:00 | EQUIP_FROM_INVENTORY: TFT_Item_PowerGauntlet -> Rakan (i:2.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Emanador | DA_Murkwolf18 | 0.1200 |  |
| Jogador 6 | 5-1 | 19:36:01 | EQUIP_FROM_INVENTORY: TFT_Item_HextechGunblade -> Aronguejo (i:4.0) (tabuleiro slot 6) | FAST8 | FAST8: composição planejada exige nível 8 | 82 | 5 | Emanador | DA_Murkwolf18 | 0.1000 |  |
| Jogador 6 | 5-1 | 19:36:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 78 | 5 | Emanador | DA_Murkwolf18 | 0.0200 |  |
| Jogador 6 | 5-1 | 19:36:05 | BUY XP | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Emanador | DA_Murkwolf18 | 0.0200 |  |
| Jogador 6 | 5-1 | 19:36:05 | MOVE Board -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 74 | 5 | Emanador | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 5-2 | 19:36:09 | COMPROU: Cascalho (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Emanador | DA_Murkwolf18 | 0.3700 |  |
| Jogador 6 | 5-2 | 19:36:10 | MOVE Bench -> Board: Lobo Trevoguari (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Emanador | DA_Murkwolf18 | 0.5900 |  |
| Jogador 6 | 5-2 | 19:36:10 | MOVE Board -> Board: Lobo Trevoguari (i:4.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Emanador | DA_Murkwolf18 | -0.0200 |  |
| Jogador 6 | 5-2 | 19:36:10 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-2 | 19:36:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 85 | 5 | Emanador | DA_Murkwolf18 | -0.2700 |  |
| Jogador 6 | 5-3 | 19:36:20 | MOVE Board -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Emanador | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 5-3 | 19:36:20 | MOVE Board -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-3 | 19:36:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 96 | 5 | Emanador | DA_Murkwolf18 | -0.2800 |  |
| Jogador 6 | 5-4 | 19:36:31 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Emanador | DA_Murkwolf18 | 0.0200 |  |
| Jogador 6 | 5-4 | 19:36:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-4 | 19:36:31 | MOVE Board -> Board: Vi (i:6.0) <-> Lobo Trevoguari (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-4 | 19:36:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 107 | 5 | Emanador | DA_Murkwolf18 | -0.2900 |  |
| Jogador 6 | 5-5 | 19:36:41 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Emanador | DA_Murkwolf18 | 0.9500 |  |
| Jogador 6 | 5-5 | 19:36:41 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Emanador | DA_Murkwolf18 | 0.6000 |  |
| Jogador 6 | 5-5 | 19:36:42 | MOVE Board -> Board: Lobo Trevoguari (i:8.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Emanador | DA_Murkwolf18 | -0.0200 |  |
| Jogador 6 | 5-5 | 19:36:42 | MOVE Board -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-5 | 19:36:42 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 117 | 5 | Emanador | DA_Murkwolf18 | -0.3000 |  |
| Jogador 6 | 5-6 | 19:36:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 127 | 5 | Emanador | DA_Murkwolf18 | 0.8200 |  |
| Jogador 6 | 5-6 | 19:36:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 127 | 5 | Emanador | DA_Murkwolf18 | 0.0000 |  |
| Jogador 6 | 5-6 | 19:36:52 | MOVE Board -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 127 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-6 | 19:36:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 127 | 5 | Emanador | DA_Murkwolf18 | -0.3000 |  |
| Jogador 6 | 5-7 | 19:37:02 | EQUIP_FROM_INVENTORY: DA_18_EmblemSpellweaver -> Lobo Trevoguari (i:8.0) (tabuleiro slot 19) | FAST8 | FAST8: composição planejada exige nível 8 | 138 | 5 | Emanador | DA_Murkwolf18 | -0.0100 |  |
| Jogador 6 | 5-7 | 19:37:03 | COMPROU: Azuporã (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Emanador | DA_Sentinel18 | 1.0100 |  |
| Jogador 6 | 5-7 | 19:37:03 | COMPROU: Lobo Trevoguari (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Emanador | DA_Sentinel18 | 0.4000 |  |
| Jogador 6 | 5-7 | 19:37:03 | VENDEU: Cascalho (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 135 | 5 | Emanador | DA_Sentinel18 | -0.3300 |  |
| Jogador 6 | 5-7 | 19:37:03 | COMPROU: Akali (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Emanador | DA_Sentinel18 | 0.3300 |  |
| Jogador 6 | 5-7 | 19:37:04 | MOVE Board -> Board: Vi (i:6.0) <-> Aronguejo (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Emanador | DA_Sentinel18 | 0.0000 |  |
| Jogador 6 | 5-7 | 19:37:04 | MOVE Board -> Board: Aronguejo (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Emanador | DA_Sentinel18 | -0.0100 |  |
| Jogador 6 | 5-7 | 19:37:04 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Emanador | DA_Sentinel18 | -0.1700 |  |
| Jogador 6 | 6-1 | 19:37:13 | COMPROU: Kog'Maw (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 142 | 5 | Emanador | DA_Sentinel18 | 1.0100 |  |
| Jogador 6 | 6-1 | 19:37:13 | COMPROU: Teemo (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | 0.3800 |  |
| Jogador 6 | 6-1 | 19:37:14 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | 0.1000 |  |
| Jogador 6 | 6-1 | 19:37:14 | MOVE Bench -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | 0.0600 |  |
| Jogador 6 | 6-1 | 19:37:14 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | -0.4100 |  |
| Jogador 6 | 6-1 | 19:37:14 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 6-1 | 19:37:15 | MOVE Bench -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | 0.0600 |  |
| Jogador 6 | 6-1 | 19:37:15 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | -0.0900 |  |
| Jogador 6 | 6-1 | 19:37:15 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 140 | 5 | Emanador | DA_Sentinel18 | -0.1000 |  |
| Jogador 6 | 6-2 | 19:37:24 | COMPROU: Morgana (Custo 4 \| i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Emanador | DA_Sentinel18 | 0.3500 |  |
| Jogador 6 | 6-2 | 19:37:25 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Emanador | DA_Sentinel18 | -0.3900 |  |
| Jogador 6 | 6-2 | 19:37:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 6-2 | 19:37:25 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Emanador | DA_Sentinel18 | -0.1200 |  |
| Jogador 6 | 6-2 | 19:37:25 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Emanador | DA_Sentinel18 | -0.4100 |  |
| Jogador 6 | 6-2 | 19:37:25 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Emanador | DA_Sentinel18 | -0.1800 |  |
| Jogador 6 | 6-3 | 19:37:35 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Emanador | DA_Sentinel18 | 0.1000 |  |
| Jogador 6 | 6-3 | 19:37:35 | MOVE Bench -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Emanador | DA_Sentinel18 | 0.0600 |  |
| Jogador 6 | 6-3 | 19:37:35 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Emanador | DA_Sentinel18 | -0.1100 |  |
| Jogador 6 | 6-3 | 19:37:36 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Emanador | DA_Sentinel18 | -0.4100 |  |
| Jogador 6 | 6-3 | 19:37:36 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 157 | 5 | Emanador | DA_Sentinel18 | -0.1900 |  |
| Jogador 6 | 6-4 | 19:37:47 | MOVE Bench -> Board: Rakan (i:2.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Emanador | DA_Sentinel18 | 0.1000 |  |
| Jogador 6 | 6-4 | 19:37:48 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Emanador | DA_Sentinel18 | -0.1100 |  |
| Jogador 6 | 6-4 | 19:37:48 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Emanador | DA_Sentinel18 | -0.4100 |  |
| Jogador 6 | 6-4 | 19:37:48 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 167 | 5 | Emanador | DA_Sentinel18 | -0.2000 |  |
| Jogador 6 | 6-5 | 19:38:01 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | -0.4000 |  |
| Jogador 6 | 6-5 | 19:38:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 6-5 | 19:38:02 | MOVE Bench -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | 0.0600 |  |
| Jogador 6 | 6-5 | 19:38:02 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | -0.4100 |  |
| Jogador 6 | 6-5 | 19:38:02 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 6-5 | 19:38:02 | MOVE Bench -> Board: Vi (i:6.0) <-> Master Yi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 6-5 | 19:38:03 | MOVE Bench -> Board: Master Yi (i:6.0) <-> Lobo Trevoguari (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | -0.8200 |  |
| Jogador 6 | 6-5 | 19:38:03 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Vi (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | 0.1500 |  |
| Jogador 6 | 6-5 | 19:38:03 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 178 | 5 | Emanador | DA_Sentinel18 | -0.6200 |  |
| Jogador 6 | 6-6 | 19:38:13 | MOVE Bench -> Board: Rakan (i:2.0) <-> Lobo Trevoguari (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 189 | 5 | Emanador | DA_Sentinel18 | -0.7300 |  |
| Jogador 6 | 6-6 | 19:38:13 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 189 | 5 | Emanador | DA_Sentinel18 | 0.1300 |  |
| Jogador 6 | 6-6 | 19:38:13 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 189 | 5 | Emanador | DA_Sentinel18 | -0.6400 |  |
| Jogador 6 | 6-6 | 19:38:14 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 189 | 5 | Emanador | DA_Sentinel18 | -0.3100 |  |
| Jogador 6 | 6-6 | 19:38:14 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 189 | 5 | Emanador | DA_Sentinel18 | -0.2600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 6 | 6-7 | 19:38:25 | EQUIP_FROM_INVENTORY: DA_18_EmblemRapidfire -> Aronguejo (i:4.0) (tabuleiro slot 12) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | -0.0300 |  |
| Jogador 6 | 6-7 | 19:38:26 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | 0.1000 |  |
| Jogador 6 | 6-7 | 19:38:26 | MOVE Bench -> Board: Vi (i:6.0) <-> Lobo Trevoguari (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | -0.8600 |  |
| Jogador 6 | 6-7 | 19:38:26 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | 0.1200 |  |
| Jogador 6 | 6-7 | 19:38:26 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 6-7 | 19:38:27 | MOVE Bench -> Board: Vi (i:6.0) <-> Lobo Trevoguari (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | -0.8600 |  |
| Jogador 6 | 6-7 | 19:38:27 | MOVE Bench -> Board: Lobo Trevoguari (i:8.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | 0.1300 |  |
| Jogador 6 | 6-7 | 19:38:27 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | 0.1000 |  |
| Jogador 6 | 6-7 | 19:38:27 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 200 | 5 | Emanador | DA_Sentinel18 | -0.3900 |  |
| Jogador 6 | 7-1 | 19:38:37 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Emanador | DA_Sentinel18 | -0.4000 |  |
| Jogador 6 | 7-1 | 19:38:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 7-1 | 19:38:38 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Emanador | DA_Sentinel18 | -0.4100 |  |
| Jogador 6 | 7-1 | 19:38:38 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Emanador | DA_Sentinel18 | 0.0800 |  |
| Jogador 6 | 7-1 | 19:38:38 | MOVE Bench -> Board: Vi (i:6.0) <-> Vi (i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Emanador | DA_Sentinel18 | -0.1200 |  |
| Jogador 6 | 7-1 | 19:38:39 | MOVE Bench -> Board: Vi (i:6.0) <-> Rakan (i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Emanador | DA_Sentinel18 | -0.6200 |  |
| Jogador 6 | 7-1 | 19:38:39 | PASSOU TURNO | ALL_IN | HP crítico: gastar para sobreviver | 211 | 5 | Emanador | DA_Sentinel18 | -0.3800 |  |
| Jogador 7 | ? | 19:32:17 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3500 |  |
| Jogador 7 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 19:32:24 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2600 |  |
| Jogador 7 | 1-1 | 19:32:24 | MOVE Bench -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.8600 |  |
| Jogador 7 | 1-1 | 19:32:24 | MOVE Bench -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.6300 |  |
| Jogador 7 | 1-1 | 19:32:25 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.1900 |  |
| Jogador 7 | 1-1 | 19:32:25 | MOVE Bench -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.3700 |  |
| Jogador 7 | 1-1 | 19:32:25 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.1000 |  |
| Jogador 7 | 1-1 | 19:32:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-1 | 19:32:29 | MOVE Bench -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.3400 |  |
| Jogador 7 | 1-2 | 19:32:30 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-2 | 19:32:30 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.2300 |  |
| Jogador 7 | 1-2 | 19:32:31 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 1-2 | 19:32:31 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0200 |  |
| Jogador 7 | 1-2 | 19:32:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 1-2 | 19:32:32 | MOVE Board -> Board: Varus (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | -0.2300 |  |
| Jogador 7 | 1-2 | 19:32:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 19:32:37 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | 1.0200 |  |
| Jogador 7 | 1-3 | 19:32:37 | COMPROU: Camille (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 1-3 | 19:32:37 | MOVE Board -> Board: Akali (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-3 | 19:32:37 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0500 |  |
| Jogador 7 | 1-3 | 19:32:38 | MOVE Board -> Board: Varus (i:2.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.2800 |  |
| Jogador 7 | 1-3 | 19:32:38 | MOVE Board -> Board: Akali (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.0200 |  |
| Jogador 7 | 1-3 | 19:32:38 | MOVE Board -> Board: Rakan (i:2.0) <-> Varus (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | -0.3500 |  |
| Jogador 7 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 1-4 | 19:32:43 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.9600 |  |
| Jogador 7 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_SparringGloves -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.2100 |  |
| Jogador 7 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_NegatronCloak + TFT_Item_GiantsBelt -> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1800 |  |
| Jogador 7 | 1-4 | 19:32:44 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Yorick | 0.4900 |  |
| Jogador 7 | 1-4 | 19:32:44 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Yorick | 0.3100 |  |
| Jogador 7 | 1-4 | 19:32:44 | MOVE Bench -> Board: Shen (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Shen | -0.3600 |  |
| Jogador 7 | 1-4 | 19:32:45 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Shen | -0.2200 |  |
| Jogador 7 | 1-4 | 19:32:46 | VENDEU: Camille (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Shen | -0.0800 |  |
| Jogador 7 | 1-4 | 19:32:46 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 1.0500 |  |
| Jogador 7 | 1-4 | 19:32:46 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.5500 |  |
| Jogador 7 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 19:32:50 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Akali_AD | 1.1200 |  |
| Jogador 7 | 2-1 | 19:32:50 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.1600 |  |
| Jogador 7 | 2-1 | 19:32:51 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.3700 |  |
| Jogador 7 | 2-1 | 19:32:51 | MOVE Bench -> Board: Yorick (i:2.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | -0.6800 |  |
| Jogador 7 | 2-1 | 19:32:51 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-1 | 19:32:55 | MOVE Bench -> Board: Varus (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.6400 |  |
| Jogador 7 | 2-2 | 19:32:56 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 7 | 2-2 | 19:32:57 | MOVE Bench -> Board: Shen (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.0900 |  |
| Jogador 7 | 2-2 | 19:32:57 | MOVE Board -> Board: Shen (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.0100 |  |
| Jogador 7 | 2-2 | 19:32:57 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | -0.1300 |  |
| Jogador 7 | 2-2 | 19:32:58 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.0000 |  |
| Jogador 7 | 2-3 | 19:33:04 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | — | DA_18_Akali_AD | 0.3200 |  |
| Jogador 7 | 2-3 | 19:33:04 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | — | DA_18_Akali_AD | 0.1400 |  |
| Jogador 7 | 2-3 | 19:33:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | — | DA_18_Akali_AD | -0.1600 |  |
| Jogador 7 | 2-3 | 19:33:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Akali_AD | 0.8900 |  |
| Jogador 7 | 2-3 | 19:33:05 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Akali_AD | 0.8800 |  |
| Jogador 7 | 2-3 | 19:33:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Akali_AD | -0.1600 |  |
| Jogador 7 | 2-3 | 19:33:05 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Shen | 0.9400 |  |
| Jogador 7 | 2-3 | 19:33:05 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Shen | -0.3500 |  |
| Jogador 7 | 2-3 | 19:33:06 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Shen | 0.5600 |  |
| Jogador 7 | 2-3 | 19:33:07 | MOVE Board -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Shen | -0.1600 |  |
| Jogador 7 | 2-3 | 19:33:07 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-4 | 19:33:11 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Shen | 0.8800 |  |
| Jogador 7 | 2-4 | 19:33:11 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | Colosso | DA_18_Shen | -0.1600 |  |
| Jogador 7 | 2-4 | 19:33:11 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Shen | 0.9500 |  |
| Jogador 7 | 2-4 | 19:33:11 | MOVE Bench -> Board: Xayah (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Shen | 0.1200 |  |
| Jogador 7 | 2-4 | 19:33:12 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Shen | 0.4700 |  |
| Jogador 7 | 2-4 | 19:33:12 | MOVE Bench -> Board: Yorick (i:2.0) <-> Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | Colosso | DA_18_Shen | -0.0300 |  |
| Jogador 7 | 2-4 | 19:33:13 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Shen | 0.8900 |  |
| Jogador 7 | 2-4 | 19:33:14 | MOVE Bench -> Board: Xayah (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Shen | 0.0700 |  |
| Jogador 7 | 2-4 | 19:33:14 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Shen | -0.3700 |  |
| Jogador 7 | 2-4 | 19:33:14 | MOVE Board -> Board: Xayah (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Shen | 0.2600 |  |
| Jogador 7 | 2-4 | 19:33:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-5 | 19:33:18 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Shen | 0.9500 |  |
| Jogador 7 | 2-5 | 19:33:18 | MOVE Bench -> Board: Yorick (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Shen | -0.1700 |  |
| Jogador 7 | 2-5 | 19:33:19 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Shen | -0.1400 |  |
| Jogador 7 | 2-5 | 19:33:19 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-5 | 19:33:24 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Shen | 0.1600 |  |
| Jogador 7 | 2-6 | 19:33:26 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | -0.0300 |  |
| Jogador 7 | 2-6 | 19:33:26 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | 0.5600 |  |
| Jogador 7 | 2-6 | 19:33:26 | MOVE Board -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-6 | 19:33:26 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | 0.0000 |  |
| Jogador 7 | 2-6 | 19:33:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Colosso | DA_18_Shen | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 2-7 | 19:33:34 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_18_Shen | 0.7800 |  |
| Jogador 7 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NeedlesslyLargeRod -> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_18_Shen | 0.1100 |  |
| Jogador 7 | 2-7 | 19:33:34 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_18_Shen | -0.4700 |  |
| Jogador 7 | 2-7 | 19:33:34 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_18_Shen | -0.3400 |  |
| Jogador 7 | 2-7 | 19:33:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 15 | 1 | Colosso | DA_18_Shen | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-1 | 19:33:42 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 7 | 3-1 | 19:33:43 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_Fiddlesticks18 | -0.2300 |  |
| Jogador 7 | 3-1 | 19:33:43 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_Fiddlesticks18 | 0.5400 |  |
| Jogador 7 | 3-1 | 19:33:43 | COMPROU: Diana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | 0.1700 |  |
| Jogador 7 | 3-1 | 19:33:43 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | 0.0100 |  |
| Jogador 7 | 3-1 | 19:33:44 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | -0.3500 |  |
| Jogador 7 | 3-1 | 19:33:44 | MOVE Bench -> Board: Fiddlesticks (i:12.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 7 | 3-1 | 19:33:44 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 3-1 | 19:33:44 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 7 | 3-1 | 19:33:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-2 | 19:33:52 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_Fiddlesticks18 | 0.2900 |  |
| Jogador 7 | 3-2 | 19:33:52 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 23 | 1 | Colosso | DA_Fiddlesticks18 | -0.6100 |  |
| Jogador 7 | 3-2 | 19:33:52 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 7 | 3-2 | 19:33:53 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_Fiddlesticks18 | 0.7700 |  |
| Jogador 7 | 3-2 | 19:33:53 | MOVE Bench -> Board: Yorick (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_Fiddlesticks18 | 0.6800 |  |
| Jogador 7 | 3-2 | 19:33:53 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 7 | 3-2 | 19:33:54 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | -0.4000 |  |
| Jogador 7 | 3-2 | 19:33:54 | MOVE Bench -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | 0.0700 |  |
| Jogador 7 | 3-2 | 19:33:54 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 17 | 1 | Colosso | DA_Fiddlesticks18 | -0.3600 |  |
| Jogador 7 | 3-2 | 19:33:57 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Fiddlesticks18 | 0.8400 |  |
| Jogador 7 | 3-2 | 19:33:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Fiddlesticks18 | -0.0600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-3 | 19:34:00 | MOVE Bench -> Board: Yorick (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 7 | 3-3 | 19:34:00 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Colosso | DA_Fiddlesticks18 | 0.5100 |  |
| Jogador 7 | 3-3 | 19:34:01 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 24 | 1 | Colosso | DA_Fiddlesticks18 | 0.3100 |  |
| Jogador 7 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 22 | 1 | Colosso | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 7 | 3-3 | 19:34:01 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_Fiddlesticks18 | 0.3000 |  |
| Jogador 7 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Colosso | DA_Fiddlesticks18 | -0.3000 |  |
| Jogador 7 | 3-3 | 19:34:04 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Colosso | DA_Fiddlesticks18 | 0.2900 |  |
| Jogador 7 | 3-3 | 19:34:04 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 16 | 1 | Colosso | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 7 | 3-3 | 19:34:04 | VENDEU: Shen (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 21 | 1 | Colosso | DA_Fiddlesticks18 | 0.0400 |  |
| Jogador 7 | 3-3 | 19:34:05 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_Fiddlesticks18 | 0.8200 |  |
| Jogador 7 | 3-3 | 19:34:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Colosso | DA_Fiddlesticks18 | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-4 | 19:34:10 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Colosso | DA_Fiddlesticks18 | -0.2400 |  |
| Jogador 7 | 3-4 | 19:34:11 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Colosso | DA_Fiddlesticks18 | -0.1600 |  |
| Jogador 7 | 3-4 | 19:34:11 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Colosso | DA_Fiddlesticks18 | -0.5500 |  |
| Jogador 7 | 3-4 | 19:34:12 | MOVE Bench -> Board: Yorick (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Colosso | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 7 | 3-4 | 19:34:12 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Fiddlesticks18 | -0.3700 |  |
| Jogador 7 | 3-4 | 19:34:12 | EQUIP_FROM_INVENTORY: TFT_Item_NightHarvester -> Yorick (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 7 | 3-4 | 19:34:12 | EQUIP_FROM_INVENTORY: TFT_Item_SpectralGauntlet -> Yorick (i:4.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Fiddlesticks18 | 0.1500 |  |
| Jogador 7 | 3-4 | 19:34:13 | MOVE Board -> Board: Yorick (i:2.0) <-> Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 3-4 | 19:34:13 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 3-4 | 19:34:15 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Fiddlesticks18 | -0.4200 |  |
| Jogador 7 | 3-4 | 19:34:16 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Colosso | DA_Fiddlesticks18 | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: pressão de vida | 37 | 2 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-5 | 19:34:19 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 36 | 2 | Colosso | DA_Fiddlesticks18 | 0.8500 |  |
| Jogador 7 | 3-5 | 19:34:19 | REROLL | STABILIZE | STABILIZE: pressão de vida | 34 | 2 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-5 | 19:34:20 | REROLL | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 3-5 | 19:34:22 | MOVE Bench -> Board: Yorick (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Colosso | DA_Fiddlesticks18 | 0.1000 |  |
| Jogador 7 | 3-5 | 19:34:22 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.7900 |  |
| Jogador 7 | 3-5 | 19:34:23 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.4200 |  |
| Jogador 7 | 3-5 | 19:34:23 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 32 | 2 | Colosso | DA_Fiddlesticks18 | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-6 | 19:34:30 | MOVE Bench -> Board: Yorick (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Colosso | DA_Fiddlesticks18 | 0.1100 |  |
| Jogador 7 | 3-6 | 19:34:30 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Colosso | DA_Fiddlesticks18 | -0.7700 |  |
| Jogador 7 | 3-6 | 19:34:30 | MOVE Bench -> Board: Rakan (i:2.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 7 | 3-6 | 19:34:31 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 43 | 3 | Colosso | DA_Fiddlesticks18 | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_ChainVest + TFT_Item_RecurveBow -> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_Fiddlesticks18 | 0.1800 |  |
| Jogador 7 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_Fiddlesticks18 | 0.2000 |  |
| Jogador 7 | 3-7 | 19:34:40 | MOVE Bench -> Board: Yorick (i:2.0) <-> Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_Fiddlesticks18 | -0.5300 |  |
| Jogador 7 | 3-7 | 19:34:40 | MOVE Bench -> Board: Yorick (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_Fiddlesticks18 | 0.0900 |  |
| Jogador 7 | 3-7 | 19:34:40 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Yorick (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_Fiddlesticks18 | -0.4100 |  |
| Jogador 7 | 3-7 | 19:34:44 | VENDEU: Sejuani (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Colosso | DA_Fiddlesticks18 | -0.3200 |  |
| Jogador 7 | 3-7 | 19:34:44 | EQUIP_FROM_INVENTORY: TFT_Item_ArchangelsStaff -> Fiddlesticks (i:6.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: pressão de vida | 60 | 4 | Colosso | DA_Fiddlesticks18 | 0.0500 |  |
| Jogador 7 | 3-7 | 19:34:44 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 59 | 4 | Colosso | DA_Fiddlesticks18 | 0.9600 |  |
| Jogador 7 | 3-7 | 19:34:44 | REROLL | STABILIZE | STABILIZE: pressão de vida | 57 | 4 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 3-7 | 19:34:45 | REROLL | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_Fiddlesticks18 | -0.1500 |  |
| Jogador 7 | 3-7 | 19:34:45 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 55 | 4 | Colosso | DA_Fiddlesticks18 | -0.2500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-1 | 19:34:48 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 65 | 5 | Colosso | DA_Fiddlesticks18 | 0.8800 |  |
| Jogador 7 | 4-1 | 19:34:48 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 64 | 5 | Colosso | DA_Fiddlesticks18 | 0.4100 |  |
| Jogador 7 | 4-1 | 19:34:48 | REROLL | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-1 | 19:34:51 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Fiddlesticks18 | 0.4000 |  |
| Jogador 7 | 4-1 | 19:34:52 | MOVE Board -> Board: Rek'Sai (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 4-1 | 19:34:52 | MOVE Board -> Board: Rakan (i:2.0) <-> Fiddlesticks (i:12.0) | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Fiddlesticks18 | -0.0100 |  |
| Jogador 7 | 4-1 | 19:34:52 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 62 | 5 | Colosso | DA_Fiddlesticks18 | -0.2600 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-2 | 19:35:00 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.9700 |  |
| Jogador 7 | 4-2 | 19:35:01 | REROLL | STABILIZE | STABILIZE: pressão de vida | 69 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-2 | 19:35:01 | VENDEU: Yorick (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 72 | 5 | Colosso | DA_Fiddlesticks18 | -0.5400 |  |
| Jogador 7 | 4-2 | 19:35:01 | COMPROU: Varus (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_Fiddlesticks18 | 1.0100 |  |
| Jogador 7 | 4-2 | 19:35:02 | MOVE Board -> Board: Fiddlesticks (i:12.0) <-> Vazio | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_Fiddlesticks18 | 0.0000 |  |
| Jogador 7 | 4-2 | 19:35:02 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 4-2 | 19:35:02 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 71 | 5 | Colosso | DA_Fiddlesticks18 | -0.2900 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 7 | 4-3 | 19:35:10 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 81 | 5 | Colosso | DA_Fiddlesticks18 | 0.5900 |  |
| Jogador 7 | 4-3 | 19:35:10 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 79 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-3 | 19:35:10 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 77 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-3 | 19:35:11 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-3 | 19:35:11 | COMPROU: Yorick (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Colosso | DA_Fiddlesticks18 | 1.0500 |  |
| Jogador 7 | 4-3 | 19:35:12 | COMPROU: Varus (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Colosso | DA_Fiddlesticks18 | 0.4400 |  |
| Jogador 7 | 4-3 | 19:35:12 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 71 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-3 | 19:35:12 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_Fiddlesticks18 | 0.9500 |  |
| Jogador 7 | 4-3 | 19:35:16 | MOVE Bench -> Board: Diana (i:6.0) <-> Vazio | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_Fiddlesticks18 | 0.4400 |  |
| Jogador 7 | 4-4 | 19:35:20 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 80 | 5 | Colosso | DA_Fiddlesticks18 | 0.4300 |  |
| Jogador 7 | 4-4 | 19:35:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 78 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-4 | 19:35:20 | COMPROU: Sejuani (Custo 2 \| i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 76 | 5 | Colosso | DA_Fiddlesticks18 | 0.3800 |  |
| Jogador 7 | 4-4 | 19:35:20 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 74 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-4 | 19:35:21 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-4 | 19:35:21 | VENDEU: Rek'Sai (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 75 | 5 | Colosso | DA_Fiddlesticks18 | -0.0200 |  |
| Jogador 7 | 4-4 | 19:35:21 | COMPROU: Diana (Custo 3 \| i:6.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Colosso | DA_Fiddlesticks18 | 0.9200 |  |
| Jogador 7 | 4-4 | 19:35:21 | REROLL | ALL_IN | HP crítico: gastar para sobreviver | 70 | 5 | Colosso | DA_Fiddlesticks18 | -0.0900 |  |
| Jogador 7 | 4-4 | 19:35:25 | VENDEU: Varus (i:4.0) | ALL_IN | HP crítico: gastar para sobreviver | 73 | 5 | Colosso | DA_Fiddlesticks18 | -0.4800 |  |
| Jogador 7 | 4-4 | 19:35:26 | COMPROU: Akali (Custo 1 \| i:2.0) | ALL_IN | HP crítico: gastar para sobreviver | 72 | 5 | Colosso | DA_Fiddlesticks18 | 0.9900 |  |
| Jogador 8 | ? | 19:32:17 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3500 |  |
| Jogador 8 | ? | 19:32:18 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 19:32:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.1000 |  |
| Jogador 8 | 1-1 | 19:32:24 | MOVE Bench -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.8600 |  |
| Jogador 8 | 1-1 | 19:32:24 | MOVE Bench -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.5600 |  |
| Jogador 8 | 1-1 | 19:32:25 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.1200 |  |
| Jogador 8 | 1-1 | 19:32:25 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.3700 |  |
| Jogador 8 | 1-1 | 19:32:25 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | -0.1100 |  |
| Jogador 8 | 1-1 | 19:32:26 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0000 |  |
| Jogador 8 | 1-1 | 19:32:29 | MOVE Bench -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.3400 |  |
| Jogador 8 | 1-2 | 19:32:30 | COMPROU: Yorick (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-2 | 19:32:30 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.2900 |  |
| Jogador 8 | 1-2 | 19:32:31 | MOVE Board -> Board: Veigar (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 8 | 1-2 | 19:32:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0200 |  |
| Jogador 8 | 1-2 | 19:32:31 | MOVE Board -> Board: Rakan (i:2.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Rakan | 0.0200 |  |
| Jogador 8 | 1-2 | 19:32:32 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.2400 |  |
| Jogador 8 | 1-2 | 19:32:32 | MOVE Board -> Board: Kobuko (i:2.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 8 | 1-2 | 19:32:32 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 1-3 | 19:32:37 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.9900 |  |
| Jogador 8 | 1-3 | 19:32:37 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 1.1100 |  |
| Jogador 8 | 1-3 | 19:32:37 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.3300 |  |
| Jogador 8 | 1-3 | 19:32:37 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0300 |  |
| Jogador 8 | 1-3 | 19:32:38 | MOVE Board -> Board: Veigar (i:2.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.3200 |  |
| Jogador 8 | 1-3 | 19:32:38 | MOVE Board -> Board: Kobuko (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.0200 |  |
| Jogador 8 | 1-3 | 19:32:38 | MOVE Board -> Board: Veigar (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.3600 |  |
| Jogador 8 | 1-3 | 19:32:38 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 1-4 | 19:32:43 | COMPROU: Xayah (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.4000 |  |
| Jogador 8 | 1-4 | 19:32:43 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_GiantsBelt -> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.1700 |  |
| Jogador 8 | 1-4 | 19:32:43 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.4100 |  |
| Jogador 8 | 1-4 | 19:32:44 | CRAFT_AND_EQUIP: TFT_Item_TearOfTheGoddess + TFT_Item_NegatronCloak -> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_18_Xayah | 0.1100 |  |
| Jogador 8 | 1-4 | 19:32:44 | COMPROU: Teemo (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.3200 |  |
| Jogador 8 | 1-4 | 19:32:44 | MOVE Bench -> Board: Teemo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.1200 |  |
| Jogador 8 | 1-4 | 19:32:45 | MOVE Board -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0100 |  |
| Jogador 8 | 1-4 | 19:32:46 | MOVE Board -> Board: Rakan (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | -0.0600 |  |
| Jogador 8 | 1-4 | 19:32:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Xayah | 0.0000 |  |
| Jogador 8 | 2-1 | 19:32:50 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | — | DA_18_Xayah | 0.9100 |  |
| Jogador 8 | 2-1 | 19:32:50 | COMPROU: Krugue (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Xayah | 0.2600 |  |
| Jogador 8 | 2-1 | 19:32:51 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 0 | 0 | — | DA_18_Xayah | -0.2200 |  |
| Jogador 8 | 2-1 | 19:32:51 | VENDEU: Xayah (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 3 | 0 | — | DA_Krug18 | -0.3000 |  |
| Jogador 8 | 2-1 | 19:32:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_Krug18 | 0.9800 |  |
| Jogador 8 | 2-1 | 19:32:51 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.9500 |  |
| Jogador 8 | 2-1 | 19:32:52 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.4300 |  |
| Jogador 8 | 2-1 | 19:32:52 | MOVE Bench -> Board: Kobuko (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0200 |  |
| Jogador 8 | 2-1 | 19:32:52 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.1900 |  |
| Jogador 8 | 2-1 | 19:32:52 | MOVE Bench -> Board: Teemo (i:4.0) <-> Kobuko (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.1100 |  |
| Jogador 8 | 2-1 | 19:32:52 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 2-2 | 19:32:56 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 1.0300 |  |
| Jogador 8 | 2-2 | 19:32:57 | MOVE Bench -> Board: Kobuko (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.1000 |  |
| Jogador 8 | 2-2 | 19:32:57 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | — | DA_18_Veigar | 0.3000 |  |
| Jogador 8 | 2-2 | 19:32:57 | COMPROU: Sejuani (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 4 | 0 | — | DA_18_Veigar | 0.2500 |  |
| Jogador 8 | 2-2 | 19:32:58 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 2 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 8 | 2-2 | 19:32:58 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.3700 |  |
| Jogador 8 | 2-2 | 19:32:58 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0700 |  |
| Jogador 8 | 2-2 | 19:32:59 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 8 | 2-2 | 19:32:59 | MOVE Board -> Board: Rakan (i:2.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | -0.0100 |  |
| Jogador 8 | 2-2 | 19:33:00 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 1 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 2-3 | 19:33:04 | COMPROU: Rakan (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 6 | 0 | — | DA_18_Veigar | 0.8300 |  |
| Jogador 8 | 2-3 | 19:33:04 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 5 | 0 | — | DA_18_Veigar | 0.7800 |  |
| Jogador 8 | 2-3 | 19:33:04 | REROLL | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 3 | 0 | — | DA_18_Veigar | -0.1600 |  |
| Jogador 8 | 2-3 | 19:33:04 | COMPROU: Tristana (Custo 3 \| i:6.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Veigar | 0.1000 |  |
| Jogador 8 | 2-3 | 19:33:05 | MOVE Board -> Board: Kobuko (i:4.0) <-> Sejuani (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 2-3 | 19:33:05 | MOVE Board -> Board: Sejuani (i:4.0) <-> Rakan (i:2.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Veigar | -0.0200 |  |
| Jogador 8 | 2-3 | 19:33:05 | PASSOU TURNO | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 0 | 0 | — | DA_18_Veigar | 0.0000 |  |
| Jogador 8 | 2-4 | 19:33:11 | VENDEU: Veigar (i:4.0) | LOSS_STREAK | LOSS_STREAK: converter derrota em economia sem risco crítico | 9 | 0 | Colosso | DA_18_Kobuko | -0.2700 |  |
| Jogador 8 | 2-4 | 19:33:11 | EQUIP_FROM_INVENTORY: TFT_Item_SteraksGage -> Kobuko (i:4.0) (tabuleiro slot 19) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Kobuko | 0.1300 |  |
| Jogador 8 | 2-4 | 19:33:11 | COMPROU: Leona (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Colosso | DA_18_Kobuko | 0.1200 |  |
| Jogador 8 | 2-4 | 19:33:11 | VENDEU: Xayah (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Colosso | DA_18_Kobuko | -0.0200 |  |
| Jogador 8 | 2-4 | 19:33:12 | COMPROU: LeBlanc (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Colosso | DA_18_Kobuko | 0.0500 |  |
| Jogador 8 | 2-4 | 19:33:12 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Colosso | DA_18_Kobuko | -0.1600 |  |
| Jogador 8 | 2-4 | 19:33:13 | MOVE Bench -> Board: Teemo (i:4.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Lutador | DA_18_Kobuko | -0.0900 |  |
| Jogador 8 | 2-4 | 19:33:14 | VENDEU: LeBlanc (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 7 | 0 | Lutador | DA_18_Kobuko | 0.0200 |  |
| Jogador 8 | 2-4 | 19:33:14 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Lutador | DA_18_Kobuko | 0.1500 |  |
| Jogador 8 | 2-4 | 19:33:14 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Lutador | DA_18_Kobuko | -0.3600 |  |
| Jogador 8 | 2-4 | 19:33:14 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 5 | 0 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 2-5 | 19:33:18 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_18_Kobuko | 0.1000 |  |
| Jogador 8 | 2-5 | 19:33:18 | MOVE Bench -> Board: Teemo (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_18_Kobuko | 0.2700 |  |
| Jogador 8 | 2-5 | 19:33:19 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Lutador | DA_18_Kobuko | -0.0600 |  |
| Jogador 8 | 2-5 | 19:33:19 | MOVE Bench -> Board: Akali (i:2.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Lutador | DA_18_Kobuko | -0.5200 |  |
| Jogador 8 | 2-5 | 19:33:20 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Lutador | DA_18_Kobuko | 0.3200 |  |
| Jogador 8 | 2-5 | 19:33:20 | MOVE Bench -> Board: Teemo (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 10 | 0 | Lutador | DA_18_Kobuko | -0.1000 |  |
| Jogador 8 | 2-5 | 19:33:21 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Lutador | DA_18_Kobuko | -0.2400 |  |
| Jogador 8 | 2-5 | 19:33:21 | VENDEU: Leona (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 9 | 0 | Lutador | DA_18_Kobuko | 0.0100 |  |
| Jogador 8 | 2-5 | 19:33:21 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 8 | 0 | Lutador | DA_18_Kobuko | 0.9200 |  |
| Jogador 8 | 2-5 | 19:33:22 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Lutador | DA_18_Kobuko | -0.2200 |  |
| Jogador 8 | 2-5 | 19:33:22 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 6 | 0 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 2-6 | 19:33:26 | VENDEU: Akali (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 14 | 0 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 2-6 | 19:33:26 | COMPROU: Fiddlesticks (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_18_Kobuko | 0.1400 |  |
| Jogador 8 | 2-6 | 19:33:26 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_18_Kobuko | 0.0900 |  |
| Jogador 8 | 2-6 | 19:33:26 | MOVE Bench -> Board: Teemo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_18_Kobuko | -0.7900 |  |
| Jogador 8 | 2-6 | 19:33:26 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_18_Kobuko | -0.6100 |  |
| Jogador 8 | 2-6 | 19:33:27 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 11 | 0 | Lutador | DA_18_Kobuko | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 2-7 | 19:33:34 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_RecurveBow -> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Lutador | DA_18_Kobuko | 0.1400 |  |
| Jogador 8 | 2-7 | 19:33:34 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 19 | 1 | Lutador | DA_18_Kobuko | 0.2200 |  |
| Jogador 8 | 2-7 | 19:33:34 | VENDEU: Yorick (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 20 | 1 | Lutador | DA_18_Kobuko | 0.0900 |  |
| Jogador 8 | 2-7 | 19:33:34 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Lutador | DA_18_Kobuko | 0.7300 |  |
| Jogador 8 | 2-7 | 19:33:35 | MOVE Bench -> Board: Teemo (i:4.0) <-> Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Lutador | DA_18_Kobuko | -0.4000 |  |
| Jogador 8 | 2-7 | 19:33:35 | MOVE Bench -> Board: Rek'Sai (i:2.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Lutador | DA_18_Kobuko | -0.6100 |  |
| Jogador 8 | 2-7 | 19:33:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 18 | 1 | Lutador | DA_18_Kobuko | 0.0000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-1 | 19:33:42 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 25 | 1 | Lutador | DA_18_Kobuko | 0.1000 |  |
| Jogador 8 | 3-1 | 19:33:43 | VENDEU: Teemo (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Lutador | DA_18_Kobuko | 0.0100 |  |
| Jogador 8 | 3-1 | 19:33:43 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Rek'Sai (i:2.0) (tabuleiro slot 8) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 27 | 1 | Lutador | DA_18_Kobuko | 0.1500 |  |
| Jogador 8 | 3-1 | 19:33:43 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | 0.8500 |  |
| Jogador 8 | 3-1 | 19:33:43 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | 0.0900 |  |
| Jogador 8 | 3-1 | 19:33:44 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | 0.4500 |  |
| Jogador 8 | 3-1 | 19:33:44 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | -0.7700 |  |
| Jogador 8 | 3-1 | 19:33:44 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | 0.0800 |  |
| Jogador 8 | 3-1 | 19:33:44 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Rakan (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | -0.2900 |  |
| Jogador 8 | 3-1 | 19:33:46 | MOVE Bench -> Board: Rakan (i:2.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | -0.7500 |  |
| Jogador 8 | 3-1 | 19:33:46 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 1 | Lutador | DA_18_Kobuko | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-2 | 19:33:52 | COMPROU: Tristana (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Lutador | DA_18_Kobuko | 0.8100 |  |
| Jogador 8 | 3-2 | 19:33:52 | COMPROU: Rakan (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_18_Kobuko | 0.8700 |  |
| Jogador 8 | 3-2 | 19:33:52 | MOVE Bench -> Board: Tristana (i:6.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_18_Kobuko | 0.0400 |  |
| Jogador 8 | 3-2 | 19:33:53 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_18_Kobuko | 0.2500 |  |
| Jogador 8 | 3-2 | 19:33:53 | MOVE Bench -> Board: Alistar (i:4.0) <-> Tristana (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_18_Kobuko | -0.4100 |  |
| Jogador 8 | 3-2 | 19:33:53 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_18_Kobuko | 0.0600 |  |
| Jogador 8 | 3-2 | 19:33:54 | MOVE Bench -> Board: Alistar (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 31 | 2 | Lutador | DA_18_Kobuko | -0.0500 |  |
| Jogador 8 | 3-2 | 19:33:54 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 29 | 2 | Lutador | DA_18_Kobuko | -0.2400 |  |
| Jogador 8 | 3-2 | 19:33:54 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 28 | 2 | Lutador | DA_18_Kobuko | 0.2900 |  |
| Jogador 8 | 3-2 | 19:33:57 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Lutador | DA_18_Kobuko | -0.1600 |  |
| Jogador 8 | 3-2 | 19:33:57 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 26 | 2 | Lutador | DA_18_Kobuko | -0.0800 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-3 | 19:34:00 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_18_Kobuko | 0.8200 |  |
| Jogador 8 | 3-3 | 19:34:00 | VENDEU: Rakan (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 37 | 2 | Lutador | DA_18_Kobuko | -0.3000 |  |
| Jogador 8 | 3-3 | 19:34:01 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Lutador | DA_18_Kobuko | 0.3100 |  |
| Jogador 8 | 3-3 | 19:34:01 | MOVE Board -> Board: Alistar (i:4.0) <-> Kobuko (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 36 | 2 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 3-3 | 19:34:01 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_18_Kobuko | -0.2200 |  |
| Jogador 8 | 3-3 | 19:34:04 | MOVE Board -> Board: Kobuko (i:4.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 34 | 2 | Lutador | DA_18_Kobuko | 0.0100 |  |
| Jogador 8 | 3-3 | 19:34:04 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 35 | 2 | Lutador | DA_18_Kobuko | -0.3700 |  |
| Jogador 8 | 3-3 | 19:34:04 | COMPROU: Cassiopeia (Custo 3 \| i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 3-3 | 19:34:04 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 32 | 2 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 3-3 | 19:34:05 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Lutador | DA_18_Kobuko | -0.2200 |  |
| Jogador 8 | 3-3 | 19:34:05 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 30 | 2 | Lutador | DA_18_Kobuko | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-4 | 19:34:10 | VENDEU: Cassiopeia (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 42 | 3 | Lutador | DA_18_Kobuko | 0.0900 |  |
| Jogador 8 | 3-4 | 19:34:11 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Lutador | DA_18_Kobuko | 0.3200 |  |
| Jogador 8 | 3-4 | 19:34:11 | MOVE Bench -> Board: Veigar (i:2.0) <-> Alistar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Lutador | DA_18_Kobuko | -0.3100 |  |
| Jogador 8 | 3-4 | 19:34:12 | MOVE Bench -> Board: Alistar (i:4.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Lutador | DA_18_Kobuko | -0.2800 |  |
| Jogador 8 | 3-4 | 19:34:12 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 41 | 3 | Lutador | DA_18_Kobuko | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-5 | 19:34:19 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Veigar (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Lutador | DA_18_Kobuko | -0.3800 |  |
| Jogador 8 | 3-5 | 19:34:19 | VENDEU: Rek'Sai (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Lutador | DA_18_Kobuko | -0.3800 |  |
| Jogador 8 | 3-5 | 19:34:19 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Lutador | DA_18_Kobuko | 0.2400 |  |
| Jogador 8 | 3-5 | 19:34:20 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Lutador | DA_18_Kobuko | -0.1600 |  |
| Jogador 8 | 3-5 | 19:34:22 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Lutador | DA_18_Kobuko | -0.2300 |  |
| Jogador 8 | 3-5 | 19:34:22 | COMPROU: Ornn (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Lutador | DA_18_Kobuko | 0.2400 |  |
| Jogador 8 | 3-5 | 19:34:23 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Lutador | DA_18_Kobuko | -0.1600 |  |
| Jogador 8 | 3-5 | 19:34:23 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Lutador | DA_18_Kobuko | -0.1600 |  |
| Jogador 8 | 3-5 | 19:34:23 | VENDEU: Ornn (i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 45 | 4 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 3-5 | 19:34:24 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Lutador | DA_18_Kobuko | 0.8800 |  |
| Jogador 8 | 3-5 | 19:34:24 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Lutador | DA_18_Kobuko | -0.1300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-6 | 19:34:30 | COMPROU: Alistar (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Lutador | DA_18_Alistar | 0.9000 |  |
| Jogador 8 | 3-6 | 19:34:30 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Lutador | DA_18_Veigar | 0.3400 |  |
| Jogador 8 | 3-6 | 19:34:30 | COMPROU: Veigar (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Lutador | DA_18_Veigar | 0.8600 |  |
| Jogador 8 | 3-6 | 19:34:31 | MOVE Bench -> Board: Alistar (i:8.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Lutador | DA_18_Veigar | 0.0900 |  |
| Jogador 8 | 3-6 | 19:34:31 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Vazio | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 50 | 4 | Lutador | DA_18_Veigar | 0.4000 |  |
| Jogador 8 | 3-6 | 19:34:31 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 48 | 4 | Lutador | DA_18_Veigar | -0.2300 |  |
| Jogador 8 | 3-6 | 19:34:32 | COMPROU: Shen (Custo 2 \| i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 46 | 4 | Lutador | DA_18_Veigar | 0.2400 |  |
| Jogador 8 | 3-6 | 19:34:32 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Lutador | DA_18_Veigar | -0.1600 |  |
| Jogador 8 | 3-6 | 19:34:32 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Lutador | DA_18_Veigar | -0.4000 |  |
| Jogador 8 | 3-6 | 19:34:35 | MOVE Bench -> Board: Alistar (i:8.0) <-> Fiddlesticks (i:6.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Lutador | DA_18_Veigar | 0.0800 |  |
| Jogador 8 | 3-6 | 19:34:35 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 44 | 4 | Lutador | DA_18_Veigar | -0.0300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_SparringGloves + TFT_Item_GiantsBelt -> Alistar (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Lutador | DA_18_Veigar | 0.2000 |  |
| Jogador 8 | 3-7 | 19:34:39 | CRAFT_AND_EQUIP: TFT_Item_BFSword + TFT_Item_NeedlesslyLargeRod -> Alistar (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Lutador | DA_18_Veigar | 0.1900 |  |
| Jogador 8 | 3-7 | 19:34:40 | VENDEU: Veigar (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 56 | 4 | Lutador | DA_18_Alistar | -0.3300 |  |
| Jogador 8 | 3-7 | 19:34:40 | COMPROU: Kobuko (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Lutador | DA_18_Alistar | 0.9600 |  |
| Jogador 8 | 3-7 | 19:34:40 | MOVE Bench -> Board: Fiddlesticks (i:6.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 55 | 4 | Lutador | DA_18_Alistar | 0.0400 |  |
| Jogador 8 | 3-7 | 19:34:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 53 | 4 | Lutador | DA_18_Alistar | -0.0900 |  |
| Jogador 8 | 3-7 | 19:34:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 52 | 4 | Lutador | DA_18_Alistar | 0.3900 |  |
| Jogador 8 | 3-7 | 19:34:44 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 51 | 4 | Lutador | DA_18_Alistar | 0.9300 |  |
| Jogador 8 | 3-7 | 19:34:44 | REROLL | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Lutador | DA_18_Alistar | -0.1700 |  |
| Jogador 8 | 3-7 | 19:34:45 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:8.0) | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Lutador | DA_18_Kobuko | -0.4000 |  |
| Jogador 8 | 3-7 | 19:34:45 | PASSOU TURNO | STABILIZE | STABILIZE: tabuleiro fraco sob pressão | 49 | 4 | Lutador | DA_18_Kobuko | -0.0500 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 4-1 | 19:34:48 | MOVE Bench -> Board: Alistar (i:8.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 61 | 5 | Lutador | DA_18_Kobuko | 0.6000 |  |
| Jogador 8 | 4-1 | 19:34:48 | COMPROU: Ornn (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_18_Kobuko | 0.1700 |  |
| Jogador 8 | 4-1 | 19:34:48 | MOVE Board -> Board: Alistar (i:8.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 4-1 | 19:34:51 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Kobuko (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_18_Alistar | -0.0200 |  |
| Jogador 8 | 4-1 | 19:34:52 | MOVE Board -> Board: Kobuko (i:4.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 8 | 4-1 | 19:34:52 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 60 | 5 | Lutador | DA_18_Alistar | -0.0900 |  |
| Jogador 8 | 4-2 | 19:35:00 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 8 | 4-2 | 19:35:01 | MOVE Board -> Board: Shen (i:4.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 8 | 4-2 | 19:35:01 | MOVE Board -> Board: Alistar (i:8.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Lutador | DA_18_Alistar | -0.0200 |  |
| Jogador 8 | 4-2 | 19:35:01 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 72 | 5 | Lutador | DA_18_Alistar | -0.0900 |  |
| Jogador 8 | 4-3 | 19:35:10 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Kobuko (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 4-3 | 19:35:10 | MOVE Board -> Board: Kobuko (i:4.0) <-> Sejuani (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Lutador | DA_18_Kobuko | -0.0100 |  |
| Jogador 8 | 4-3 | 19:35:10 | MOVE Board -> Board: Sejuani (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Lutador | DA_18_Kobuko | -0.0100 |  |
| Jogador 8 | 4-3 | 19:35:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 84 | 5 | Lutador | DA_18_Kobuko | -0.1000 |  |
| Jogador 8 | 4-4 | 19:35:20 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Lutador | DA_18_Kobuko | 0.0000 |  |
| Jogador 8 | 4-4 | 19:35:20 | MOVE Board -> Board: Shen (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Lutador | DA_18_Kobuko | -0.0200 |  |
| Jogador 8 | 4-4 | 19:35:20 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 95 | 5 | Lutador | DA_18_Kobuko | -0.1100 |  |
| Jogador 8 | 4-5 | 19:35:29 | VENDEU: Kobuko (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 111 | 5 | Lutador | DA_18_Alistar | -0.5400 |  |
| Jogador 8 | 4-5 | 19:35:30 | COMPROU: Krugue (Custo 3 \| i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Lutador | DA_18_Alistar | 0.8100 |  |
| Jogador 8 | 4-5 | 19:35:30 | VENDEU: Ornn (i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 109 | 5 | Lutador | DA_18_Alistar | -0.1400 |  |
| Jogador 8 | 4-5 | 19:35:30 | COMPROU: Veigar (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Lutador | DA_18_Alistar | 0.8900 |  |
| Jogador 8 | 4-5 | 19:35:31 | MOVE Board -> Board: Rek'Sai (i:4.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 8 | 4-5 | 19:35:31 | MOVE Board -> Board: Alistar (i:8.0) <-> Kobuko (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 8 | 4-5 | 19:35:31 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 108 | 5 | Lutador | DA_18_Alistar | -0.2600 |  |
| Jogador 8 | 4-6 | 19:35:39 | COMPROU: Rubrivirim (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 8 | 4-6 | 19:35:39 | MOVE Board -> Board: Kobuko (i:4.0) <-> Vazio | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Lutador | DA_18_Alistar | 0.0000 |  |
| Jogador 8 | 4-6 | 19:35:40 | MOVE Board -> Board: Sejuani (i:4.0) <-> Fiddlesticks (i:6.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 8 | 4-6 | 19:35:40 | MOVE Board -> Board: Fiddlesticks (i:6.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Lutador | DA_18_Alistar | -0.0100 |  |
| Jogador 8 | 4-6 | 19:35:40 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 121 | 5 | Lutador | DA_18_Alistar | -0.1300 |  |
| Jogador 8 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Kobuko (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Lutador | DA_18_Alistar | 0.2000 |  |
| Jogador 8 | 4-7 | 19:35:49 | CRAFT_AND_EQUIP: TFT_Item_NeedlesslyLargeRod + TFT_Item_NegatronCloak -> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 134 | 5 | Lutador | DA_18_Alistar | 0.2100 |  |
| Jogador 8 | 4-7 | 19:35:50 | COMPROU: Shen (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Lutador | DA_18_Alistar | 0.4100 |  |
| Jogador 8 | 4-7 | 19:35:50 | MOVE Bench -> Board: Veigar (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Lutador | DA_18_Alistar | 0.1000 |  |
| Jogador 8 | 4-7 | 19:35:50 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Lutador | DA_18_Alistar | -0.4200 |  |
| Jogador 8 | 4-7 | 19:35:51 | MOVE Bench -> Board: Alistar (i:8.0) <-> Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Lutador | DA_18_Alistar | -0.3200 |  |
| Jogador 8 | 4-7 | 19:35:55 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 132 | 5 | Lutador | DA_18_Alistar | -0.1500 |  |
| Jogador 8 | 5-1 | 19:35:59 | VENDEU: Veigar (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 149 | 5 | Lutador | DA_18_Alistar | -0.3600 |  |
| Jogador 8 | 5-1 | 19:36:00 | COMPROU: Rek'Sai (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 148 | 5 | Lutador | DA_18_Alistar | 0.9500 |  |
| Jogador 8 | 5-1 | 19:36:00 | COMPROU: Kobuko (Custo 1 \| i:2.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Lutador | DA_18_Alistar | 0.3600 |  |
| Jogador 8 | 5-1 | 19:36:00 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Lutador | DA_18_RekSai | 0.0600 |  |
| Jogador 8 | 5-1 | 19:36:00 | MOVE Bench -> Board: Alistar (i:8.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Lutador | DA_18_RekSai | 0.0900 |  |
| Jogador 8 | 5-1 | 19:36:01 | MOVE Bench -> Board: Shen (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-1 | 19:36:05 | MOVE Board -> Board: Shen (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Lutador | DA_18_RekSai | -0.0200 |  |
| Jogador 8 | 5-1 | 19:36:05 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 147 | 5 | Lutador | DA_18_RekSai | -0.3200 |  |
| Jogador 8 | 5-2 | 19:36:09 | COMPROU: Alistar (Custo 2 \| i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Lutador | DA_18_Alistar | 0.3800 |  |
| Jogador 8 | 5-2 | 19:36:10 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Lutador | DA_18_Alistar | -0.4000 |  |
| Jogador 8 | 5-2 | 19:36:10 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Lutador | DA_18_Alistar | 0.0500 |  |
| Jogador 8 | 5-2 | 19:36:10 | MOVE Bench -> Board: Alistar (i:8.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Lutador | DA_18_Alistar | -0.3700 |  |
| Jogador 8 | 5-2 | 19:36:11 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-2 | 19:36:11 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 155 | 5 | Lutador | DA_18_Alistar | -0.1800 |  |
| Jogador 8 | 5-3 | 19:36:20 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Alistar (i:8.0) | FAST8 | FAST8: composição planejada exige nível 8 | 166 | 5 | Lutador | DA_18_Alistar | 0.0600 |  |
| Jogador 8 | 5-3 | 19:36:20 | MOVE Bench -> Board: Alistar (i:8.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 166 | 5 | Lutador | DA_18_Alistar | 0.0900 |  |
| Jogador 8 | 5-3 | 19:36:20 | MOVE Bench -> Board: Shen (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 166 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-3 | 19:36:21 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 166 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-3 | 19:36:21 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 166 | 5 | Lutador | DA_18_Alistar | -0.1900 |  |
| Jogador 8 | 5-4 | 19:36:31 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Shen (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 176 | 5 | Lutador | DA_18_Alistar | 0.1000 |  |
| Jogador 8 | 5-4 | 19:36:31 | MOVE Bench -> Board: Shen (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 176 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-4 | 19:36:31 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Rek'Sai (i:4.0) | FAST8 | FAST8: composição planejada exige nível 8 | 176 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-4 | 19:36:32 | PASSOU TURNO | FAST8 | FAST8: composição planejada exige nível 8 | 176 | 5 | Lutador | DA_18_Alistar | -0.1900 |  |
| Jogador 8 | 5-5 | 19:36:41 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Alistar (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Lutador | DA_18_Alistar | 0.0600 |  |
| Jogador 8 | 5-5 | 19:36:41 | MOVE Bench -> Board: Alistar (i:8.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Lutador | DA_18_Alistar | -0.3700 |  |
| Jogador 8 | 5-5 | 19:36:42 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Lutador | DA_18_Alistar | 0.0800 |  |
| Jogador 8 | 5-5 | 19:36:42 | MOVE Bench -> Board: Shen (i:4.0) <-> Alistar (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Lutador | DA_18_Alistar | -0.4200 |  |
| Jogador 8 | 5-5 | 19:36:42 | MOVE Bench -> Board: Alistar (i:8.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Lutador | DA_18_Alistar | -0.3700 |  |
| Jogador 8 | 5-5 | 19:36:42 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 186 | 5 | Lutador | DA_18_Alistar | -0.2300 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 5-6 | 19:36:52 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | 0.1000 |  |
| Jogador 8 | 5-6 | 19:36:52 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | 0.0500 |  |
| Jogador 8 | 5-6 | 19:36:52 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-6 | 19:36:52 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Alistar (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | 0.0500 |  |
| Jogador 8 | 5-6 | 19:36:53 | MOVE Bench -> Board: Alistar (i:8.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | 0.0900 |  |
| Jogador 8 | 5-6 | 19:36:53 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | -0.4000 |  |
| Jogador 8 | 5-6 | 19:36:53 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Alistar (i:8.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | 0.0700 |  |
| Jogador 8 | 5-6 | 19:36:53 | MOVE Bench -> Board: Alistar (i:8.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | 0.1000 |  |
| Jogador 8 | 5-6 | 19:36:54 | MOVE Bench -> Board: Shen (i:4.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 197 | 5 | Lutador | DA_18_Alistar | -0.4000 |  |
| Jogador 8 | 5-7 | 19:37:02 | EQUIP_FROM_INVENTORY: DA_18_EmblemHunter -> Fiddlesticks (i:6.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 208 | 5 | Lutador | DA_18_Alistar | -0.0200 |  |
| Jogador 8 | 5-7 | 19:37:03 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 208 | 5 | Lutador | DA_18_Alistar | -0.4000 |  |
| Jogador 8 | 5-7 | 19:37:03 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 208 | 5 | Lutador | DA_18_Alistar | 0.0800 |  |
| Jogador 8 | 5-7 | 19:37:03 | MOVE Bench -> Board: Shen (i:4.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 208 | 5 | Lutador | DA_18_Alistar | 0.0500 |  |
| Jogador 8 | 5-7 | 19:37:03 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 208 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-7 | 19:37:04 | MOVE Bench -> Board: Rek'Sai (i:4.0) <-> Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 208 | 5 | Lutador | DA_18_Alistar | -0.4100 |  |
| Jogador 8 | 5-7 | 19:37:04 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 208 | 5 | Lutador | DA_18_Alistar | -0.3000 | STABILIZE_PASS_WITH_GOLD_REVIEW |
| Jogador 8 | 6-1 | 19:37:13 | VENDEU: Rek'Sai (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 222 | 5 | Lutador | DA_18_Alistar | -0.5400 |  |
| Jogador 8 | 6-1 | 19:37:13 | EQUIP_FROM_INVENTORY: TFT_Item_LastWhisper -> Fiddlesticks (i:6.0) (tabuleiro slot 25) | STABILIZE | STABILIZE: pressão de vida | 222 | 5 | Lutador | DA_18_Alistar | 0.1200 |  |
| Jogador 8 | 6-1 | 19:37:14 | COMPROU: Akali (Custo 1 \| i:2.0) | STABILIZE | STABILIZE: pressão de vida | 221 | 5 | Lutador | DA_18_Alistar | 0.0800 |  |
| Jogador 8 | 6-1 | 19:37:14 | MOVE Bench -> Board: Akali (i:2.0) <-> Sejuani (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 221 | 5 | Lutador | DA_18_Alistar | 0.0600 |  |
| Jogador 8 | 6-1 | 19:37:14 | MOVE Bench -> Board: Sejuani (i:4.0) <-> Shen (i:4.0) | STABILIZE | STABILIZE: pressão de vida | 221 | 5 | Lutador | DA_18_Alistar | -0.4000 |  |
| Jogador 8 | 6-1 | 19:37:14 | MOVE Bench -> Board: Shen (i:4.0) <-> Akali (i:2.0) | STABILIZE | STABILIZE: pressão de vida | 221 | 5 | Lutador | DA_18_Alistar | -0.0500 |  |
| Jogador 8 | 6-1 | 19:37:15 | PASSOU TURNO | STABILIZE | STABILIZE: pressão de vida | 221 | 5 | Lutador | DA_18_Alistar | -0.3200 | STABILIZE_PASS_WITH_GOLD_REVIEW |

As flags FAST8/SLOWROLL/STABILIZE/ECON são candidatos de revisão, não violações definitivas: logs legados não incluem a máscara legal completa nem sempre registram HP, nível e alternativas no mesmo instante.

### Evidência adicional dos logs do Viewer

| Jogador | Rounds observados | Snapshots de loja | Ofertas vistas | Snapshots de itens | Itens não vazios | Observações de ouro | Transições comp/foco | Warnings de posição |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 24 | 58 | 290 | 24 | 15 | 200 | 20 | 17 |
| Jogador 2 | 28 | 58 | 290 | 28 | 16 | 228 | 18 | 28 |
| Jogador 3 | 41 | 70 | 350 | 41 | 19 | 294 | 15 | 36 |
| Jogador 4 | 27 | 78 | 390 | 27 | 16 | 234 | 19 | 29 |
| Jogador 5 | 28 | 76 | 380 | 28 | 16 | 249 | 19 | 10 |
| Jogador 6 | 41 | 74 | 370 | 41 | 18 | 319 | 15 | 28 |
| Jogador 7 | 23 | 49 | 245 | 23 | 14 | 183 | 7 | 23 |
| Jogador 8 | 34 | 51 | 255 | 34 | 17 | 257 | 22 | 34 |

Essas contagens complementam os snapshots estruturados: ofertas e avisos textuais não provam, isoladamente, que uma compra, venda ou posição era a melhor decisão.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 200 | 200 | 200 | 0 | 190 | 0 | 200 | 200 | 200 | 48/38 |
| Jogador 2 | 228 | 228 | 228 | 0 | 219 | 0 | 228 | 228 | 228 | 64/50 |
| Jogador 3 | 294 | 294 | 294 | 0 | 279 | 0 | 294 | 294 | 294 | 65/51 |
| Jogador 4 | 234 | 234 | 234 | 0 | 223 | 0 | 234 | 234 | 234 | 58/44 |
| Jogador 5 | 249 | 249 | 249 | 0 | 242 | 0 | 249 | 249 | 249 | 71/60 |
| Jogador 6 | 319 | 319 | 319 | 0 | 304 | 0 | 319 | 319 | 319 | 72/57 |
| Jogador 7 | 183 | 183 | 183 | 0 | 175 | 0 | 183 | 183 | 183 | 45/31 |
| Jogador 8 | 257 | 257 | 257 | 0 | 246 | 0 | 257 | 257 | 257 | 53/39 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.2637415826320648 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32052889466285706 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31222331523895264 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.2252703607082367 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05667584389448166 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6403698325157166 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4284442961215973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.34094762802124023 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 60 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2520047426223755 | 0.0 | 0.0 | +699bd379-c986-4107-9c35-eeb8b49cf182 / -— |
| Jogador 1 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01501765102148056 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06358975917100906 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006125867832452059 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00713548855856061 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 69 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0391172170639038 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9816498160362244 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 90 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9799399971961975 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 115 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1962990164756775 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 116 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18199634552001953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 117 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3948453664779663 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 118 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2684793770313263 | 0.0 | 0.0 | +57652644-f861-47bc-addd-90760a272b22 / -— |
| Jogador 1 | 2-1 | 119 | REROLL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 120 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 121 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 122 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 139 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8749674558639526 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 1 | 2-2 | 140 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31325000524520874 | 0.0 | 0.0 | +9bb3da58-fe6f-4298-8529-859cceb4857e / -— |
| Jogador 1 | 2-2 | 141 | REROLL | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 142 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9330201148986816 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-2 | 143 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5209478735923767 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 144 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 145 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 146 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 162 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8929517865180969 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 1 | 2-3 | 163 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13709589838981628 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 1 | 2-3 | 164 | REROLL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 165 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Ornn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9495192766189575 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -2718f555-b782-4fea-a68f-31395ad34232,c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-3 | 166 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010436366312205791 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 167 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5665645003318787 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 168 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 169 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 170 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 183 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9244980812072754 | 0.0 | 0.0 | +f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 / -c448b2c1-7854-4c8c-a51b-eca2791eb639,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-4 | 184 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 4 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19659395515918732 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 185 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16365981101989746 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 1 | 2-4 | 186 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1459723263978958 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 187 | REROLL | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 188 | BUY | STABILIZE | 96.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8472685813903809 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 1 | 2-4 | 189 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029467985033988953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 190 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18281179666519165 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 191 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8394416570663452 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 192 | PASS | STABILIZE | 96.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 201 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44326531887054443 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 205 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01265045814216137 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 1 | 2-5 | 206 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 2 | 0 | 8.0 | Defendente/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10754021257162094 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 207 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 2 | 0 | 10.0 | Defendente/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 208 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 2 | 0 | 10.0 | Defendente/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8129616975784302 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 209 | PASS | STABILIZE | 96.0 | 4 | 2 | 0 | 8.0 | Defendente/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 225 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 8 | 0 | 8.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8205644488334656 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 226 | BUY | STABILIZE | 90.0 | 5 | 8 | 0 | 12.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6887523531913757 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 1 | 2-6 | 227 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 12.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010149235837161541 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 228 | REROLL | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 229 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | Defendente/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30722594261169434 | 0.0 | 0.0 | +— / -c42b5c69-faa4-4147-bbb7-072c772c0f80 |
| Jogador 1 | 2-6 | 230 | EQUIP_FROM_INVENTORY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15402115881443024 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 231 | EQUIP_FROM_INVENTORY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14576083421707153 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 232 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | Defendente/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8968194127082825 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 1 | 2-6 | 233 | REROLL | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | Defendente/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 234 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | Defendente/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3680690824985504 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 1 | 2-6 | 235 | PASS | STABILIZE | 90.0 | 5 | 6 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 243 | BUY | STABILIZE | 83.0 | 5 | 12 | 1 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9483902454376221 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -341df1a1-a619-420a-926a-0fe048aa1456,57652644-f861-47bc-addd-90760a272b22 |
| Jogador 1 | 2-7 | 244 | BUY | STABILIZE | 83.0 | 5 | 11 | 1 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8596120476722717 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -8aecef4c-747d-4f03-a858-85fe309988ab,9bb3da58-fe6f-4298-8529-859cceb4857e |
| Jogador 1 | 2-7 | 245 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 9 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40583544969558716 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 246 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 9 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026857681572437286 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 247 | REROLL | STABILIZE | 83.0 | 5 | 9 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 248 | REROLL | STABILIZE | 83.0 | 5 | 7 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 249 | REROLL | STABILIZE | 83.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 250 | BUY | STABILIZE | 83.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32788923382759094 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -— |
| Jogador 1 | 2-7 | 251 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5035939812660217 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 252 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019302451983094215 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 253 | PASS | STABILIZE | 83.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 262 | BUY | STABILIZE | 83.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8058532476425171 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 1 | 3-1 | 263 | REROLL | STABILIZE | 83.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 264 | CRAFT_AND_EQUIP | STABILIZE | 83.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17994529008865356 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 265 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3753054738044739 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 266 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 3 | 0 | 16.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09743263572454453 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 267 | REROLL | STABILIZE | 83.0 | 5 | 3 | 0 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 268 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.001566231600008905 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 269 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7628220319747925 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 270 | PASS | STABILIZE | 83.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 282 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05410334840416908 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 283 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 7 | 0 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 284 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 7 | 0 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7580539584159851 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 285 | PASS | STABILIZE | 83.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 302 | BUY | STABILIZE | 73.0 | 5 | 12 | 1 | 14.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8347765207290649 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -699bd379-c986-4107-9c35-eeb8b49cf182,d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 1 | 3-3 | 303 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 11 | 1 | 10.0 | Colosso/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1509123295545578 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 304 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 305 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4364005923271179 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 306 | REROLL | STABILIZE | 73.0 | 5 | 11 | 1 | 22.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30399999022483826 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 307 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09789765626192093 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 308 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 309 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41124507784843445 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 310 | PASS | STABILIZE | 73.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 316 | BUY | STABILIZE | 62.0 | 5 | 15 | 1 | 22.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8345903754234314 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2,cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 3-4 | 317 | BUY | STABILIZE | 62.0 | 5 | 14 | 1 | 20.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2733282446861267 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 1 | 3-4 | 318 | MOVE_BENCH | STABILIZE | 62.0 | 5 | 13 | 1 | 20.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4646308124065399 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 319 | REROLL | STABILIZE | 62.0 | 5 | 13 | 1 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 320 | REROLL | STABILIZE | 62.0 | 5 | 11 | 1 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 321 | BUY | STABILIZE | 62.0 | 5 | 9 | 0 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28749361634254456 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 1 | 3-4 | 322 | MOVE_BOARD | STABILIZE | 62.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0033946416806429625 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 323 | MOVE_BOARD | STABILIZE | 62.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 324 | MOVE_BOARD | STABILIZE | 62.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014996841549873352 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 325 | PASS | STABILIZE | 62.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 332 | BUY | STABILIZE | 62.0 | 5 | 14 | 1 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8077418804168701 | 0.0 | 0.0 | +88eb7a9e-aada-4146-adaf-4d3e8a5bdd67 / -— |
| Jogador 1 | 3-5 | 333 | SELL | STABILIZE | 62.0 | 5 | 13 | 1 | 24.0 | Colosso/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3092131018638611 | 0.0 | 0.0 | +— / -b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 1 | 3-5 | 334 | BUY | STABILIZE | 62.0 | 5 | 18 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.806117594242096 | 0.0 | 0.0 | +6875f839-cf68-443f-9776-887087b375d3 / -— |
| Jogador 1 | 3-5 | 335 | SELL | STABILIZE | 62.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1876421570777893 | 0.0 | 0.0 | +— / -6eecc806-dcf8-47df-bc1d-bc5bc5f07099 |
| Jogador 1 | 3-5 | 336 | EQUIP_FROM_INVENTORY | STABILIZE | 62.0 | 5 | 20 | 2 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15965889394283295 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 337 | BUY | STABILIZE | 62.0 | 5 | 20 | 2 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7728188633918762 | 0.0 | 0.0 | +80241b75-9eb3-4b89-a754-8df65ec59786 / -88eb7a9e-aada-4146-adaf-4d3e8a5bdd67,c93990ff-0a6f-46bc-8fc1-12623d55abc1 |
| Jogador 1 | 3-5 | 338 | REROLL | STABILIZE | 62.0 | 5 | 19 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 339 | BUY | STABILIZE | 62.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079962134361267 | 0.0 | 0.0 | +5594beb6-a447-4be2-a6e0-ae5c4f94fe70 / -— |
| Jogador 1 | 3-5 | 340 | REROLL | STABILIZE | 62.0 | 5 | 16 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 341 | BUY | STABILIZE | 62.0 | 5 | 14 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8101851344108582 | 0.0 | 0.0 | +6e40ac88-b1d5-4294-b92e-5bc3902fc385 / -6875f839-cf68-443f-9776-887087b375d3,b2517873-8317-401b-8461-1d86969edbd7 |
| Jogador 1 | 3-5 | 342 | PASS | STABILIZE | 62.0 | 5 | 13 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 347 | BUY | STABILIZE | 62.0 | 5 | 20 | 2 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2112198770046234 | 0.0 | 0.0 | +54decd6d-cd7a-4905-9ab0-9a7bb44776b7 / -— |
| Jogador 1 | 3-6 | 348 | REROLL | STABILIZE | 62.0 | 5 | 18 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 349 | REROLL | STABILIZE | 62.0 | 5 | 16 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 350 | BUY | STABILIZE | 62.0 | 5 | 14 | 1 | 24.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379981517791748 | 0.0 | 0.0 | +3e2a71c7-189b-4be3-a23b-8594f7f16ba4 / -5594beb6-a447-4be2-a6e0-ae5c4f94fe70,b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 1 | 3-6 | 351 | BUY | STABILIZE | 62.0 | 5 | 13 | 1 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28761714696884155 | 0.0 | 0.0 | +4accaece-f84d-43da-967c-8c733bb95174 / -— |
| Jogador 1 | 3-6 | 352 | REROLL | STABILIZE | 62.0 | 5 | 12 | 1 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 353 | REROLL | STABILIZE | 62.0 | 5 | 10 | 1 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 354 | BUY | STABILIZE | 62.0 | 5 | 8 | 0 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8266035914421082 | 0.0 | 0.0 | +14a36be6-92b0-4c1a-8c3c-d3fdeb425992 / -2faa526c-d29e-47a9-9eb3-5030750cb483,f64919a5-eb2c-4e23-91ed-0067b3d90951 |
| Jogador 1 | 3-6 | 355 | MOVE_BENCH | STABILIZE | 62.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4024387001991272 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 356 | REROLL | STABILIZE | 62.0 | 5 | 6 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 357 | PASS | STABILIZE | 62.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 362 | BUY | STABILIZE | 52.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2842043936252594 | 0.0 | 0.0 | +086093f9-0a81-4d85-9916-c256df0c1c33 / -— |
| Jogador 1 | 3-7 | 363 | REROLL | STABILIZE | 52.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 364 | BUY | STABILIZE | 52.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28781718015670776 | 0.0 | 0.0 | +44497322-c916-4b15-8631-8f533aeada38 / -— |
| Jogador 1 | 3-7 | 365 | MOVE_BENCH | STABILIZE | 52.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2898375988006592 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 366 | REROLL | STABILIZE | 52.0 | 5 | 4 | 0 | 24.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 367 | REROLL | STABILIZE | 52.0 | 5 | 2 | 0 | 24.0 | Colosso/DA_18_Xayah | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 368 | MOVE_BOARD | STABILIZE | 52.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0482212928764056e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 369 | MOVE_BENCH | STABILIZE | 52.0 | 5 | 0 | 0 | 24.0 | Colosso/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.380989670753479 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 370 | MOVE_BOARD | STABILIZE | 52.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3016802966594696 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 371 | PASS | STABILIZE | 52.0 | 5 | 0 | 0 | 22.0 | Colosso/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 376 | CRAFT_AND_EQUIP | STABILIZE | 52.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22807781398296356 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 377 | CRAFT_AND_EQUIP | STABILIZE | 52.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23283952474594116 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 378 | MOVE_BENCH | STABILIZE | 52.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 379 | MOVE_BENCH | STABILIZE | 52.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11743022501468658 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 380 | PASS | STABILIZE | 52.0 | 5 | 5 | 0 | 24.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 388 | MOVE_BENCH | STABILIZE | 40.0 | 6 | 11 | 1 | 24.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4117453992366791 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 389 | MOVE_BOARD | FAST8 | 40.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Xayah | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008973521180450916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 390 | MOVE_BOARD | FAST8 | 40.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Xayah | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 391 | MOVE_BOARD | FAST8 | 40.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Xayah | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 392 | PASS | FAST8 | 40.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Xayah | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 402 | BUY | STABILIZE | 29.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8078838586807251 | 0.0 | 0.0 | +fd6cc418-93d8-43df-8efa-d8a995a4b1a2 / -— |
| Jogador 1 | 4-3 | 403 | REROLL | STABILIZE | 29.0 | 6 | 17 | 1 | 26.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 404 | SELL | STABILIZE | 29.0 | 6 | 15 | 1 | 26.0 | Colosso/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5017871856689453 | 0.0 | 0.0 | +— / -7a419783-907e-47e2-bf69-29a54ee18a02 |
| Jogador 1 | 4-3 | 405 | EQUIP_FROM_INVENTORY | STABILIZE | 29.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1411052793264389 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 406 | EQUIP_FROM_INVENTORY | STABILIZE | 29.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.14061583578586578 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 407 | BUY | STABILIZE | 29.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8069341778755188 | 0.0 | 0.0 | +14eedbb5-3ec9-4d55-8eb5-69e8ebc7dbad / -— |
| Jogador 1 | 4-3 | 408 | REROLL | STABILIZE | 29.0 | 6 | 17 | 1 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 409 | MOVE_BOARD | STABILIZE | 29.0 | 6 | 15 | 1 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.723194383084774e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 410 | SELL | STABILIZE | 29.0 | 6 | 15 | 1 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3176864981651306 | 0.0 | 0.0 | +— / -80241b75-9eb3-4b89-a754-8df65ec59786 |
| Jogador 1 | 4-3 | 411 | BUY | STABILIZE | 29.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2783195376396179 | 0.0 | 0.0 | +51ba748b-8f9f-4455-a86d-c01bf2304d35 / -— |
| Jogador 1 | 4-4 | 413 | REROLL | STABILIZE | 18.0 | 6 | 23 | 2 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 414 | SELL | STABILIZE | 18.0 | 6 | 21 | 2 | 26.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33068591356277466 | 0.0 | 0.0 | +— / -27102740-ce4d-4bec-a9eb-ed936f6bc364 |
| Jogador 1 | 4-4 | 415 | BUY | STABILIZE | 18.0 | 6 | 24 | 2 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8750430345535278 | 0.0 | 0.0 | +c3ffcc8c-9d09-4d3e-ba6a-16a833a9217c / -44497322-c916-4b15-8631-8f533aeada38,fd6cc418-93d8-43df-8efa-d8a995a4b1a2 |
| Jogador 1 | 4-4 | 416 | REROLL | STABILIZE | 18.0 | 6 | 23 | 2 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 417 | REROLL | STABILIZE | 18.0 | 6 | 21 | 2 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 418 | BUY | STABILIZE | 18.0 | 6 | 19 | 1 | 26.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.805875837802887 | 0.0 | 0.0 | +cbe0150a-bb32-4e17-83b7-c24ec2815fdd / -— |
| Jogador 1 | 4-4 | 419 | REROLL | STABILIZE | 18.0 | 6 | 17 | 1 | 26.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 420 | MOVE_BENCH | STABILIZE | 18.0 | 6 | 15 | 1 | 26.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08549293875694275 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 421 | REROLL | STABILIZE | 18.0 | 6 | 15 | 1 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 423 | BUY | STABILIZE | 18.0 | 6 | 20 | 2 | 24.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21193748712539673 | 0.0 | 0.0 | +4851aa6f-058c-46ae-9314-123b8bc7915d / -— |
| Jogador 1 | 4-5 | 424 | REROLL | STABILIZE | 18.0 | 6 | 19 | 1 | 24.0 | Colosso/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 425 | REROLL | STABILIZE | 18.0 | 6 | 17 | 1 | 24.0 | Colosso/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 426 | SELL | STABILIZE | 18.0 | 6 | 15 | 1 | 24.0 | Colosso/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2033262550830841 | 0.0 | 0.0 | +— / -14a36be6-92b0-4c1a-8c3c-d3fdeb425992 |
| Jogador 1 | 4-5 | 427 | BUY | STABILIZE | 18.0 | 6 | 20 | 2 | 24.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7941925525665283 | 0.0 | 0.0 | +ef978d68-7314-41e8-b0e3-244970fc0d1d / -86c535a4-a22b-4667-bc0f-46b4843d97cc,c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 1 | 4-5 | 428 | MOVE_BENCH | STABILIZE | 18.0 | 6 | 17 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23812104761600494 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 429 | BUY | STABILIZE | 18.0 | 6 | 17 | 1 | 20.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8327471613883972 | 0.0 | 0.0 | +930468cf-9098-4f59-af90-155cbfaaee59 / -086093f9-0a81-4d85-9916-c256df0c1c33,cbe0150a-bb32-4e17-83b7-c24ec2815fdd |
| Jogador 1 | 4-5 | 430 | MOVE_BENCH | STABILIZE | 18.0 | 6 | 15 | 1 | 12.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3828505873680115 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 431 | MOVE_BENCH | STABILIZE | 18.0 | 6 | 15 | 1 | 20.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3843686282634735 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 432 | REROLL | STABILIZE | 18.0 | 6 | 15 | 1 | 26.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 434 | BUY | ALL_IN | 9.0 | 6 | 21 | 2 | 26.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9018423557281494 | 0.0 | 0.0 | +4fbb6900-3a31-4ec9-81d1-cf87cb3b61ad / -14eedbb5-3ec9-4d55-8eb5-69e8ebc7dbad,4accaece-f84d-43da-967c-8c733bb95174 |
| Jogador 1 | 4-6 | 435 | MOVE_BENCH | ALL_IN | 9.0 | 6 | 20 | 2 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2927771210670471 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 436 | MOVE_BENCH | ALL_IN | 9.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20628789067268372 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 437 | MOVE_BENCH | ALL_IN | 9.0 | 6 | 20 | 2 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4021743834018707 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 438 | MOVE_BOARD | ALL_IN | 9.0 | 6 | 20 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014729626476764679 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 439 | MOVE_BOARD | ALL_IN | 9.0 | 6 | 20 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01515471376478672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 440 | PASS | ALL_IN | 9.0 | 6 | 20 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1799047589302063 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.22566726803779602 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03405897319316864 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 34 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.1177810430526733 | 0.0 | 0.0 | +11a1c814-5357-4f19-944f-aa11d6bf8384 / -f0d714b2-9165-4d27-97f5-04b552d02548,fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-3 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 0.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, SELL, PASS | True | True | 0.2713311016559601 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 61 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08052181452512741 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 62 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31944066286087036 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25654974579811096 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | 0.2154524177312851 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 65 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | 0.005346417892724276 | 0.0 | 0.0 | +18770ba0-b5a0-4c41-92a5-de4d5e3078b9 / -— |
| Jogador 2 | 1-3 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9413929581642151 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 67 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6900305151939392 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.31566473841667175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 69 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.41172298789024353 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0842299461364746 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0083845853805542 | 0.0 | 0.0 | +780538e0-4319-45d7-9d96-ace3e3d95c3d / -— |
| Jogador 2 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3442862331867218 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11487516760826111 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 91 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12649598717689514 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 92 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26861807703971863 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 2 | 2-1 | 115 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1677388697862625 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 116 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18191318213939667 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 117 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.593920886516571 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5118404626846313 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 119 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21371684968471527 | 0.0 | 0.0 | +6556f264-6237-4af2-ab1b-52bf9a6246c1 / -— |
| Jogador 2 | 2-1 | 120 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003659249283373356 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 121 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021355735138058662 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 122 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33311739563941956 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 123 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3381402790546417 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 124 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 139 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0478421449661255 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -43759c90-bd65-4632-8aa4-56ab63ae84fe,9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-2 | 140 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08292334526777267 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 141 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3157466948032379 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 142 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2546539306640625 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 2 | 2-2 | 143 | REROLL | STABILIZE | 95.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 144 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34323766827583313 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 2 | 2-2 | 145 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1064215824007988 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 146 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13670769333839417 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 147 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 148 | PASS | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 162 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8387037515640259 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 2 | 2-3 | 163 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17900528013706207 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 2 | 2-3 | 164 | REROLL | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 165 | BUY | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006576012820005417 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 2 | 2-3 | 166 | BUY | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17656268179416656 | 0.0 | 0.0 | +2e4ab22c-62d7-425c-9528-2e1315655c24 / -— |
| Jogador 2 | 2-3 | 167 | SELL | STABILIZE | 90.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5352749824523926 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 2 | 2-3 | 168 | BUY | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15720795094966888 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 2 | 2-3 | 169 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09520387649536133 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 170 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029495112597942352 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 171 | PASS | STABILIZE | 90.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 183 | SELL | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009759999811649323 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 2 | 2-4 | 184 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8845224976539612 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 2 | 2-4 | 185 | SELL | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009759999811649323 | 0.0 | 0.0 | +— / -2e4ab22c-62d7-425c-9528-2e1315655c24 |
| Jogador 2 | 2-4 | 186 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08974742889404297 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 2 | 2-4 | 187 | REROLL | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 188 | SELL | STABILIZE | 90.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0060043116100132465 | 0.0 | 0.0 | +— / -18082e05-51e8-4142-b541-c3d7d781b878 |
| Jogador 2 | 2-4 | 189 | BUY | STABILIZE | 90.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8657770156860352 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 2 | 2-4 | 190 | SELL | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014642550610005856 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 2 | 2-4 | 191 | BUY | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060998473316431046 | 0.0 | 0.0 | +8980fd33-79c8-4825-95e9-9298680cbc6d / -— |
| Jogador 2 | 2-4 | 192 | REROLL | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Veigar | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 193 | PASS | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 205 | SELL | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021913401782512665 | 0.0 | 0.0 | +— / -8980fd33-79c8-4825-95e9-9298680cbc6d |
| Jogador 2 | 2-5 | 206 | BUY | STABILIZE | 90.0 | 4 | 8 | 0 | 10.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9476950764656067 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -7c218f01-e884-46da-8a1a-2d2db27a5ff1,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 2 | 2-5 | 207 | BUY | STABILIZE | 90.0 | 4 | 7 | 0 | 10.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9396625757217407 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1,43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 2 | 2-5 | 208 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 10.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3333710730075836 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 2 | 2-5 | 209 | REROLL | STABILIZE | 90.0 | 4 | 5 | 0 | 10.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 210 | BUY | STABILIZE | 90.0 | 4 | 3 | 0 | 10.0 | Vivaz/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10102643072605133 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 2 | 2-5 | 211 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 1 | 0 | 10.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09757330268621445 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 212 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 1 | 0 | 12.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.054623253643512726 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 213 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 1 | 0 | 14.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33720862865448 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 214 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 1 | 0 | 14.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 215 | PASS | STABILIZE | 90.0 | 4 | 1 | 0 | 14.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 225 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 14.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8990009427070618 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 2 | 2-6 | 226 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 5 | 0 | 14.0 | Vivaz/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3960810899734497 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 227 | REROLL | STABILIZE | 85.0 | 5 | 5 | 0 | 16.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 228 | BUY | STABILIZE | 85.0 | 5 | 3 | 0 | 16.0 | Vivaz/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17866909503936768 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 2-6 | 229 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 1 | 0 | 16.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 230 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 1 | 0 | 16.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02644098922610283 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 231 | PASS | STABILIZE | 85.0 | 5 | 1 | 0 | 16.0 | Vivaz/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 243 | SELL | STABILIZE | 79.0 | 5 | 7 | 0 | 16.0 | Vivaz/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1844448447227478 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 2 | 2-7 | 244 | BUY | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08999591320753098 | 0.0 | 0.0 | +fe3fea0b-bb55-4236-830e-828a00a9e529 / -— |
| Jogador 2 | 2-7 | 245 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 9 | 0 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08836720883846283 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 246 | REROLL | STABILIZE | 79.0 | 5 | 9 | 0 | 18.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 247 | SELL | STABILIZE | 79.0 | 5 | 7 | 0 | 18.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23346561193466187 | 0.0 | 0.0 | +— / -1e504283-c5d1-4eb3-915e-20533ec3a756 |
| Jogador 2 | 2-7 | 248 | BUY | STABILIZE | 79.0 | 5 | 10 | 1 | 18.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13548994064331055 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -— |
| Jogador 2 | 2-7 | 249 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 7 | 0 | 18.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004346377216279507 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 250 | REROLL | STABILIZE | 79.0 | 5 | 7 | 0 | 18.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 251 | SELL | STABILIZE | 79.0 | 5 | 5 | 0 | 18.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022308235988020897 | 0.0 | 0.0 | +— / -6556f264-6237-4af2-ab1b-52bf9a6246c1 |
| Jogador 2 | 2-7 | 252 | BUY | STABILIZE | 79.0 | 5 | 6 | 0 | 18.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9496407508850098 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -046de242-84d0-4f44-a171-345f16a6e719,fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 2 | 2-7 | 253 | PASS | STABILIZE | 79.0 | 5 | 5 | 0 | 16.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 262 | BUY | STABILIZE | 79.0 | 5 | 11 | 1 | 16.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2879430949687958 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 2 | 3-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2646680474281311 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 264 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38110366463661194 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 265 | SELL | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37049999833106995 | 0.0 | 0.0 | +— / -11a1c814-5357-4f19-944f-aa11d6bf8384 |
| Jogador 2 | 3-1 | 266 | EQUIP_FROM_INVENTORY | STABILIZE | 79.0 | 5 | 13 | 1 | 16.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18904860317707062 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 267 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 13 | 1 | 16.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41776496171951294 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 268 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 13 | 1 | 14.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.822192907333374 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 269 | PASS | STABILIZE | 79.0 | 5 | 13 | 1 | 14.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 278 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 13 | 1 | 14.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41848888993263245 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 282 | BUY | STABILIZE | 68.0 | 5 | 20 | 2 | 16.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7397010922431946 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 2 | 3-2 | 283 | BUY | STABILIZE | 68.0 | 5 | 19 | 1 | 16.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8370348811149597 | 0.0 | 0.0 | +b26a039f-581c-4de2-8a75-f7e8a4ef0e4a / -18770ba0-b5a0-4c41-92a5-de4d5e3078b9,780538e0-4319-45d7-9d96-ace3e3d95c3d |
| Jogador 2 | 3-2 | 284 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 18 | 1 | 12.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32721996307373047 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 285 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 18 | 1 | 16.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06790439039468765 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 286 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 18 | 1 | 16.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4576440453529358 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 287 | REROLL | STABILIZE | 68.0 | 5 | 18 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 288 | BUY | STABILIZE | 68.0 | 5 | 16 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2845107614994049 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 2 | 3-2 | 289 | REROLL | STABILIZE | 68.0 | 5 | 14 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 290 | BUY | STABILIZE | 68.0 | 5 | 12 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7239931225776672 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 2 | 3-2 | 291 | REROLL | STABILIZE | 68.0 | 5 | 9 | 0 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 292 | PASS | STABILIZE | 68.0 | 5 | 7 | 0 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 302 | SELL | STABILIZE | 59.0 | 5 | 13 | 1 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018719999119639397 | 0.0 | 0.0 | +— / -e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 2 | 3-3 | 303 | BUY | STABILIZE | 59.0 | 5 | 15 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379919528961182 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -5af104f2-7959-4ca5-91a9-7d44494532ea,b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 2 | 3-3 | 304 | MOVE_BOARD | STABILIZE | 59.0 | 5 | 14 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06464820355176926 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 305 | REROLL | STABILIZE | 59.0 | 5 | 14 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 306 | MOVE_BENCH | STABILIZE | 59.0 | 5 | 12 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6694835424423218 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 307 | MOVE_BENCH | STABILIZE | 59.0 | 5 | 12 | 1 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3553239107131958 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 308 | PASS | STABILIZE | 59.0 | 5 | 12 | 1 | 18.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 316 | BUY | STABILIZE | 50.0 | 5 | 20 | 2 | 18.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2225416600704193 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -— |
| Jogador 2 | 3-4 | 317 | BUY | STABILIZE | 50.0 | 5 | 19 | 1 | 18.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079929947853088 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -— |
| Jogador 2 | 3-4 | 318 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 18 | 1 | 18.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0996888279914856 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 319 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 18 | 1 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 320 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 18 | 1 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5511825680732727 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 321 | PASS | STABILIZE | 50.0 | 5 | 18 | 1 | 22.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 332 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 26 | 2 | 22.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3859313428401947 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 333 | SELL | STABILIZE | 50.0 | 5 | 26 | 2 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5352749824523926 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 2 | 3-5 | 334 | BUY | STABILIZE | 50.0 | 5 | 29 | 2 | 20.0 | Vivaz/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29766225814819336 | 0.0 | 0.0 | +ae89881d-8a08-4f60-ad51-1b0fe152958d / -— |
| Jogador 2 | 3-5 | 335 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 28 | 2 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 336 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 28 | 2 | 20.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3085438013076782 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 337 | PASS | STABILIZE | 50.0 | 5 | 28 | 2 | 22.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024000000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 347 | SELL | STABILIZE | 50.0 | 5 | 36 | 3 | 22.0 | Vivaz/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3561515212059021 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 2 | 3-6 | 348 | EQUIP_FROM_INVENTORY | STABILIZE | 50.0 | 5 | 39 | 3 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16797128319740295 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 349 | BUY | STABILIZE | 50.0 | 5 | 39 | 3 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8265891671180725 | 0.0 | 0.0 | +9fd5cb87-62ee-43bc-85db-7f166ac20532 / -— |
| Jogador 2 | 3-6 | 350 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 38 | 3 | 22.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4086911380290985 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 351 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 38 | 3 | 18.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 352 | PASS | STABILIZE | 50.0 | 5 | 38 | 3 | 18.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 362 | SELL | STABILIZE | 50.0 | 5 | 48 | 4 | 18.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.096106618642807 | 0.0 | 0.0 | +— / -89cec488-9a0e-4838-b486-2504a0742476 |
| Jogador 2 | 3-7 | 363 | BUY | STABILIZE | 50.0 | 5 | 51 | 5 | 18.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8992356061935425 | 0.0 | 0.0 | +91539d01-1b4f-442a-99b0-56b534ea8063 / -57ba484a-6228-4263-8171-00a8a5893bea,7f9f3188-2482-4518-9fd2-34f0ea1527a9 |
| Jogador 2 | 3-7 | 364 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 50 | 5 | 18.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10648908466100693 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 365 | REROLL | STABILIZE | 50.0 | 5 | 50 | 5 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 366 | BUY | STABILIZE | 50.0 | 5 | 48 | 4 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5255324244499207 | 0.0 | 0.0 | +0f9f9720-95ff-4236-b5c7-deefe45b2f21 / -— |
| Jogador 2 | 3-7 | 367 | REROLL | STABILIZE | 50.0 | 5 | 45 | 4 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 368 | BUY | STABILIZE | 50.0 | 5 | 43 | 4 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8312460780143738 | 0.0 | 0.0 | +391c4f37-41d1-44a9-8bde-ea4a11ef96c5 / -— |
| Jogador 2 | 3-7 | 369 | REROLL | STABILIZE | 50.0 | 5 | 41 | 4 | 22.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 370 | SELL | STABILIZE | 50.0 | 5 | 39 | 3 | 22.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22118359804153442 | 0.0 | 0.0 | +— / -91539d01-1b4f-442a-99b0-56b534ea8063 |
| Jogador 2 | 3-7 | 371 | BUY | STABILIZE | 50.0 | 5 | 42 | 4 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23363427817821503 | 0.0 | 0.0 | +3d7b58af-0df4-452d-b82e-049660a817ec / -— |
| Jogador 2 | 3-7 | 372 | PASS | STABILIZE | 50.0 | 5 | 39 | 3 | 22.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 376 | CRAFT_AND_EQUIP | STABILIZE | 50.0 | 5 | 48 | 4 | 22.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 377 | CRAFT_AND_EQUIP | STABILIZE | 50.0 | 5 | 48 | 4 | 22.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18187563121318817 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 378 | SELL | STABILIZE | 50.0 | 5 | 48 | 4 | 22.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2749653160572052 | 0.0 | 0.0 | +— / -ae89881d-8a08-4f60-ad51-1b0fe152958d |
| Jogador 2 | 4-1 | 379 | BUY | STABILIZE | 50.0 | 5 | 49 | 4 | 22.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9276219606399536 | 0.0 | 0.0 | +93884291-af65-432f-a1a2-09d82066ca1c / -9fd5cb87-62ee-43bc-85db-7f166ac20532,fe3fea0b-bb55-4236-830e-828a00a9e529 |
| Jogador 2 | 4-1 | 380 | BUY | STABILIZE | 50.0 | 5 | 48 | 4 | 22.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3332013189792633 | 0.0 | 0.0 | +0cb30b20-2d68-4168-94b6-5198b58776bb / -— |
| Jogador 2 | 4-1 | 381 | REROLL | STABILIZE | 50.0 | 5 | 47 | 4 | 22.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 382 | MOVE_BENCH | STABILIZE | 50.0 | 5 | 45 | 4 | 22.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39963191747665405 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 383 | BUY | STABILIZE | 50.0 | 5 | 45 | 4 | 20.0 | Vivaz/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18264469504356384 | 0.0 | 0.0 | +48db898e-cf31-47c7-aab7-fd47be1938a1 / -— |
| Jogador 2 | 4-1 | 384 | REROLL | STABILIZE | 50.0 | 5 | 42 | 4 | 20.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 385 | SELL | STABILIZE | 50.0 | 5 | 40 | 4 | 20.0 | Vivaz/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37049999833106995 | 0.0 | 0.0 | +— / -93884291-af65-432f-a1a2-09d82066ca1c |
| Jogador 2 | 4-1 | 386 | PASS | STABILIZE | 50.0 | 5 | 43 | 4 | 20.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1850000023841858 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 388 | MOVE_BENCH | STABILIZE | 40.0 | 6 | 52 | 5 | 20.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6707537174224854 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 389 | MOVE_BENCH | STABILIZE | 40.0 | 6 | 52 | 5 | 18.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45099076628685 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 390 | MOVE_BENCH | STABILIZE | 40.0 | 6 | 52 | 5 | 22.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08947828412055969 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 391 | MOVE_BENCH | STABILIZE | 40.0 | 6 | 52 | 5 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32677677273750305 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 392 | PASS | FAST8 | 40.0 | 6 | 52 | 5 | 26.0 | Vivaz/DA_18_Tristana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08990325033664703 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 402 | BUY | FAST8 | 40.0 | 6 | 63 | 5 | 26.0 | Vivaz/DA_18_Tristana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07270370423793793 | 0.0 | 0.0 | +c8f4e80f-e7f3-4c57-a5c6-f784026242d5 / -— |
| Jogador 2 | 4-3 | 403 | MOVE_BOARD | FAST8 | 40.0 | 6 | 62 | 5 | 26.0 | Vivaz/DA_18_Tristana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1105995699763298 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 404 | MOVE_BOARD | FAST8 | 40.0 | 6 | 62 | 5 | 26.0 | Vivaz/DA_Cinderling18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06704054772853851 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 405 | MOVE_BOARD | FAST8 | 40.0 | 6 | 62 | 5 | 26.0 | Vivaz/DA_Cinderling18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 406 | PASS | FAST8 | 40.0 | 6 | 62 | 5 | 26.0 | Vivaz/DA_18_Tristana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23616938292980194 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 413 | BUY | STABILIZE | 28.0 | 6 | 72 | 5 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9280046224594116 | 0.0 | 0.0 | +8ba44734-6dbf-4708-9a31-41b6e0684e2b / -9fe58106-e0c4-4ecc-b152-13c8c0eb564e,f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 2 | 4-4 | 414 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 71 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39566871523857117 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 415 | BUY | STABILIZE | 28.0 | 6 | 71 | 5 | 26.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33439862728118896 | 0.0 | 0.0 | +0ed34e7f-b3f2-4127-8af6-ebe9fcca9d78 / -— |
| Jogador 2 | 4-4 | 416 | REROLL | STABILIZE | 28.0 | 6 | 70 | 5 | 26.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 417 | BUY | STABILIZE | 28.0 | 6 | 68 | 5 | 26.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9593043923377991 | 0.0 | 0.0 | +89069a13-82c4-43ac-98e6-4d3fedf12662 / -391c4f37-41d1-44a9-8bde-ea4a11ef96c5,c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |
| Jogador 2 | 4-4 | 418 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 66 | 5 | 22.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06994125992059708 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 419 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 66 | 5 | 22.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40541958808898926 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 420 | REROLL | STABILIZE | 28.0 | 6 | 66 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15000000596046448 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 421 | MOVE_BOARD | STABILIZE | 28.0 | 6 | 64 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1102230246251565e-16 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 423 | BUY | STABILIZE | 28.0 | 6 | 74 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8723598718643188 | 0.0 | 0.0 | +111c3751-b943-49fc-bd22-a26fcd8b27dc / -— |
| Jogador 2 | 4-5 | 424 | BUY | STABILIZE | 28.0 | 6 | 73 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9596918225288391 | 0.0 | 0.0 | +5be4c98b-88ed-4c40-a801-9ba4483f0639 / -0cb30b20-2d68-4168-94b6-5198b58776bb,111c3751-b943-49fc-bd22-a26fcd8b27dc |
| Jogador 2 | 4-5 | 425 | REROLL | STABILIZE | 28.0 | 6 | 72 | 5 | 24.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 426 | BUY | STABILIZE | 28.0 | 6 | 70 | 5 | 24.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8584775924682617 | 0.0 | 0.0 | +b63dabe0-b759-458c-b83c-75f41aab7a24 / -— |
| Jogador 2 | 4-5 | 427 | BUY | STABILIZE | 28.0 | 6 | 69 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9526990056037903 | 0.0 | 0.0 | +036b1890-6e85-4078-aba8-48d839ad60b4 / -0ed34e7f-b3f2-4127-8af6-ebe9fcca9d78,b63dabe0-b759-458c-b83c-75f41aab7a24 |
| Jogador 2 | 4-5 | 428 | REROLL | STABILIZE | 28.0 | 6 | 68 | 5 | 22.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 429 | BUY | STABILIZE | 28.0 | 6 | 66 | 5 | 22.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3361446261405945 | 0.0 | 0.0 | +d177aea8-6d8a-4ca3-adfa-db937c764082 / -— |
| Jogador 2 | 4-5 | 430 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 65 | 5 | 22.0 | Vivaz/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4803904592990875 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 431 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 65 | 5 | 18.0 | Vivaz/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3738965094089508 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 432 | REROLL | STABILIZE | 28.0 | 6 | 65 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 434 | BUY | STABILIZE | 28.0 | 6 | 74 | 5 | 24.0 | Vivaz/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12007901817560196 | 0.0 | 0.0 | +23044b71-aec5-492b-9e33-ee9ab2550a8f / -— |
| Jogador 2 | 4-6 | 435 | REROLL | STABILIZE | 28.0 | 6 | 71 | 5 | 24.0 | Vivaz/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 436 | SELL | STABILIZE | 28.0 | 6 | 69 | 5 | 24.0 | Vivaz/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.424623966217041 | 0.0 | 0.0 | +— / -8ba44734-6dbf-4708-9a31-41b6e0684e2b |
| Jogador 2 | 4-6 | 437 | BUY | STABILIZE | 28.0 | 6 | 72 | 5 | 24.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3470953702926636 | 0.0 | 0.0 | +258d87c6-8363-4b09-9cbf-331fdc0f464c / -— |
| Jogador 2 | 4-6 | 438 | MOVE_BOARD | STABILIZE | 28.0 | 6 | 71 | 5 | 24.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06058849021792412 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 439 | REROLL | STABILIZE | 28.0 | 6 | 71 | 5 | 24.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 440 | SELL | STABILIZE | 28.0 | 6 | 69 | 5 | 24.0 | Vivaz/DA_Cinderling18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3421268165111542 | 0.0 | 0.0 | +— / -036b1890-6e85-4078-aba8-48d839ad60b4 |
| Jogador 2 | 4-6 | 441 | BUY | STABILIZE | 28.0 | 6 | 72 | 5 | 24.0 | Vivaz/DA_Cinderling18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3944144546985626 | 0.0 | 0.0 | +65a6e6b9-53bd-4a2c-bb91-63cdef76730c / -— |
| Jogador 2 | 4-6 | 442 | REROLL | STABILIZE | 28.0 | 6 | 70 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15000000596046448 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 443 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 68 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09932126104831696 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 445 | SELL | STABILIZE | 28.0 | 6 | 80 | 5 | 28.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46055060625076294 | 0.0 | 0.0 | +— / -5be4c98b-88ed-4c40-a801-9ba4483f0639 |
| Jogador 2 | 4-7 | 446 | BUY | STABILIZE | 28.0 | 6 | 83 | 5 | 28.0 | Vivaz/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9297805428504944 | 0.0 | 0.0 | +77a7f368-0b1d-4041-948d-e8593093b5d0 / -— |
| Jogador 2 | 4-7 | 447 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 81 | 5 | 28.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4144269824028015 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 448 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 81 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23731732368469238 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 449 | PASS | STABILIZE | 28.0 | 6 | 81 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13090263307094574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 455 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 6 | 92 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14109884202480316 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 456 | CRAFT_AND_EQUIP | STABILIZE | 28.0 | 6 | 92 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14794868230819702 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 457 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 92 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21567708253860474 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 458 | MOVE_BENCH | STABILIZE | 28.0 | 6 | 92 | 5 | 28.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4296981394290924 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 459 | PASS | STABILIZE | 28.0 | 6 | 92 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15301524102687836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 465 | SELL | ALL_IN | 13.0 | 6 | 102 | 5 | 24.0 | Vivaz/DA_18_Teemo | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3765000104904175 | 0.0 | 0.0 | +— / -89069a13-82c4-43ac-98e6-4d3fedf12662 |
| Jogador 2 | 5-2 | 466 | BUY | ALL_IN | 13.0 | 6 | 107 | 5 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3826195001602173 | 0.0 | 0.0 | +db633749-ec3c-490a-8a58-a426f41afed7 / -— |
| Jogador 2 | 5-2 | 467 | MOVE_BENCH | ALL_IN | 13.0 | 6 | 106 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014913338236510754 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 468 | REROLL | ALL_IN | 13.0 | 6 | 106 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 469 | SELL | ALL_IN | 13.0 | 6 | 104 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004399999976158142 | 0.0 | 0.0 | +— / -48db898e-cf31-47c7-aab7-fd47be1938a1 |
| Jogador 2 | 5-2 | 470 | BUY | ALL_IN | 13.0 | 6 | 107 | 5 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9151210188865662 | 0.0 | 0.0 | +1b9be41c-ccaf-43a1-9d99-e8b1d9981d23 / -— |
| Jogador 2 | 5-2 | 471 | SELL | ALL_IN | 13.0 | 6 | 106 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007600000128149986 | 0.0 | 0.0 | +— / -23044b71-aec5-492b-9e33-ee9ab2550a8f |
| Jogador 2 | 5-2 | 472 | BUY | ALL_IN | 13.0 | 6 | 109 | 5 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33968988060951233 | 0.0 | 0.0 | +fa35466e-27f9-459b-b219-7c579660f2c9 / -— |
| Jogador 2 | 5-2 | 473 | REROLL | ALL_IN | 13.0 | 6 | 108 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 475 | REROLL | ALL_IN | 13.0 | 6 | 117 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 476 | SELL | ALL_IN | 13.0 | 6 | 115 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1846880167722702 | 0.0 | 0.0 | +— / -fa35466e-27f9-459b-b219-7c579660f2c9 |
| Jogador 2 | 5-3 | 477 | BUY | ALL_IN | 13.0 | 6 | 116 | 5 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9101913571357727 | 0.0 | 0.0 | +2c3ee2f8-9088-403f-804e-8c824bec878b / -— |
| Jogador 2 | 5-3 | 478 | REROLL | ALL_IN | 13.0 | 6 | 113 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 479 | REROLL | ALL_IN | 13.0 | 6 | 111 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 480 | MOVE_BENCH | ALL_IN | 13.0 | 6 | 109 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061417143791913986 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 481 | MOVE_BENCH | ALL_IN | 13.0 | 6 | 109 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42462870478630066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 482 | MOVE_BENCH | ALL_IN | 13.0 | 6 | 109 | 5 | 24.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26688358187675476 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7215380668640137 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.409182608127594 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.11721326410770416 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053920041769742966 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6344926357269287 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3983960747718811 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0395824909210205 | 0.0 | 0.0 | +477d3aa4-2130-4a0e-8254-2688ac860569 / -— |
| Jogador 3 | 1-3 | 60 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179726123809814 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -36f58657-5835-4389-95e9-a7d26464c2aa,477d3aa4-2130-4a0e-8254-2688ac860569 |
| Jogador 3 | 1-3 | 61 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 81 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.675592303276062 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21337006986141205 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21570172905921936 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 3 | 1-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04519401863217354 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06703637540340424 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 91 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 92 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012483438476920128 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9622392654418945 | 0.0 | 0.0 | +584812e9-d314-4de0-97e2-604c5c69466c / -— |
| Jogador 3 | 2-1 | 115 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1504356414079666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 116 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1286839246749878 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 117 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2585686445236206 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42213723063468933 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6844756007194519 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 120 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01678675413131714 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 121 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 139 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3685818314552307 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 3 | 2-2 | 140 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6435485482215881 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 141 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23616217076778412 | 0.0 | 0.0 | +5db33b7c-1844-4f4f-8317-ac08f66d4c1e / -— |
| Jogador 3 | 2-2 | 142 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11351386457681656 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 143 | REROLL | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 144 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 14.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7340817451477051 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 145 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6633161902427673 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 146 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 162 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9860872626304626 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -584812e9-d314-4de0-97e2-604c5c69466c,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 2-3 | 163 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34926244616508484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 164 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41493380069732666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 165 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5843704342842102 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 166 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17919738590717316 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 3 | 2-3 | 167 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23419570922851562 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 168 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01628408208489418 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 169 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 183 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9718174934387207 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 3 | 2-4 | 184 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7370911836624146 | 0.0 | 0.0 | +f5511428-5be8-475d-949c-1d840a0aed4d / -— |
| Jogador 3 | 2-4 | 185 | REROLL | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 186 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9479668736457825 | 0.0 | 0.0 | +4a0403a3-c999-4d4c-83f0-7270e8576aed / -2938180d-94e5-4bb7-832e-baa51f820ba2,c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 2-4 | 187 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3219335973262787 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 3 | 2-4 | 188 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0003718390071298927 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 189 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38688355684280396 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 190 | REROLL | STABILIZE | 95.0 | 4 | 2 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 191 | SELL | STABILIZE | 95.0 | 4 | 0 | 0 | 20.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06964000314474106 | 0.0 | 0.0 | +— / -53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 3 | 2-4 | 192 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 4 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07781879603862762 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 193 | PASS | STABILIZE | 95.0 | 4 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 205 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 4 | 8 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0680704265832901 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 206 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21731533110141754 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 3 | 2-5 | 207 | REROLL | STABILIZE | 95.0 | 4 | 7 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 208 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7833278179168701 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 3 | 2-5 | 209 | REROLL | STABILIZE | 95.0 | 4 | 4 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 210 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9464161396026611 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -5ead8548-7453-4fa1-856e-674995576a48,f5511428-5be8-475d-949c-1d840a0aed4d |
| Jogador 3 | 2-5 | 211 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -3.5926836972066667e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 212 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 1 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015095321461558342 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 213 | PASS | STABILIZE | 95.0 | 4 | 1 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 225 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35429108142852783 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 226 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 18.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2290150374174118 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 227 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38887912034988403 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 228 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 24.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26194319128990173 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 229 | PASS | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 243 | BUY | STABILIZE | 95.0 | 5 | 14 | 1 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3246519863605499 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 3 | 2-7 | 244 | REROLL | STABILIZE | 95.0 | 5 | 11 | 1 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 245 | BUY | STABILIZE | 95.0 | 5 | 9 | 0 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3313882648944855 | 0.0 | 0.0 | +f5ae964e-f157-48d1-8088-8b8a45a398b6 / -— |
| Jogador 3 | 2-7 | 246 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9047293663024902 | 0.0 | 0.0 | +cbcde5b6-8f03-4d96-ade5-1ef113ab25bc / -— |
| Jogador 3 | 2-7 | 247 | REROLL | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | Devastador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 248 | REROLL | STABILIZE | 95.0 | 5 | 5 | 0 | 22.0 | Devastador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 249 | REROLL | STABILIZE | 95.0 | 5 | 3 | 0 | 22.0 | Devastador/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 250 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 22.0 | Devastador/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3187672793865204 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 3 | 2-7 | 251 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 22.0 | Devastador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.883592426776886 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 3 | 2-7 | 252 | REROLL | STABILIZE | 95.0 | 5 | 2 | 0 | 22.0 | Devastador/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 253 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 22.0 | Devastador/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 95.0 | 5 | 6 | 0 | 22.0 | Devastador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18316741287708282 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 263 | REROLL | STABILIZE | 95.0 | 5 | 6 | 0 | 22.0 | Devastador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 264 | SELL | STABILIZE | 95.0 | 5 | 4 | 0 | 22.0 | Devastador/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18737372756004333 | 0.0 | 0.0 | +— / -4a0403a3-c999-4d4c-83f0-7270e8576aed |
| Jogador 3 | 3-1 | 265 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8036986589431763 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 3 | 3-1 | 266 | SELL | STABILIZE | 95.0 | 5 | 4 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003301315475255251 | 0.0 | 0.0 | +— / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 3 | 3-1 | 267 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8328184485435486 | 0.0 | 0.0 | +cb30dcaa-bc26-4584-9b50-24e47e70fcb0 / -584e7960-a541-4d45-8ea1-8a75e288c387,e6ee6b15-d413-4678-8ffb-29272199a53d |
| Jogador 3 | 3-1 | 268 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 4 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09898941218852997 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 269 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 4 | 0 | 18.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3963964283466339 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 270 | REROLL | STABILIZE | 95.0 | 5 | 4 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 271 | BUY | STABILIZE | 95.0 | 5 | 2 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879995107650757 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 3 | 3-1 | 272 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 22.0 | Devastador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 282 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26721248030662537 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 3 | 3-2 | 283 | REROLL | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 284 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 5 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 285 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 5 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 286 | PASS | STABILIZE | 95.0 | 5 | 5 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 302 | SELL | STABILIZE | 95.0 | 5 | 12 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23703600466251373 | 0.0 | 0.0 | +— / -cb30dcaa-bc26-4584-9b50-24e47e70fcb0 |
| Jogador 3 | 3-3 | 303 | EQUIP_FROM_INVENTORY | STABILIZE | 95.0 | 5 | 15 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18046380579471588 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 304 | BUY | STABILIZE | 95.0 | 5 | 15 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2849094867706299 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 3 | 3-3 | 305 | SELL | STABILIZE | 95.0 | 5 | 13 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017920000478625298 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 3 | 3-3 | 306 | BUY | STABILIZE | 95.0 | 5 | 14 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.568155825138092 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -— |
| Jogador 3 | 3-3 | 307 | REROLL | STABILIZE | 95.0 | 5 | 12 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 308 | REROLL | STABILIZE | 95.0 | 5 | 10 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 309 | SELL | STABILIZE | 95.0 | 5 | 8 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08671999722719193 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 3-3 | 310 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7573770880699158 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -cbcde5b6-8f03-4d96-ade5-1ef113ab25bc,f5ae964e-f157-48d1-8088-8b8a45a398b6 |
| Jogador 3 | 3-3 | 311 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 9 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5944862365722656 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 312 | PASS | STABILIZE | 95.0 | 5 | 9 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 316 | REROLL | STABILIZE | 86.0 | 5 | 14 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 317 | BUY | STABILIZE | 86.0 | 5 | 12 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8302178382873535 | 0.0 | 0.0 | +407092ea-3a14-4555-9ebd-64a36c41d1d0 / -210d2415-663d-4768-bbc2-238766c2b863,ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 3 | 3-4 | 318 | REROLL | STABILIZE | 86.0 | 5 | 10 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 319 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 8 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006297152140177786 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 320 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 8 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 321 | PASS | STABILIZE | 86.0 | 5 | 8 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 332 | BUY | STABILIZE | 86.0 | 5 | 13 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.285676509141922 | 0.0 | 0.0 | +910b14c4-57bc-44ce-b925-30a6d92a7651 / -— |
| Jogador 3 | 3-5 | 333 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 11 | 1 | 22.0 | Devastador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00020069742458872497 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 334 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 11 | 1 | 22.0 | Devastador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010334743186831474 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 335 | BUY | STABILIZE | 86.0 | 5 | 11 | 1 | 22.0 | Devastador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20119157433509827 | 0.0 | 0.0 | +db7ea53f-4df7-4c05-9462-75b527575615 / -— |
| Jogador 3 | 3-5 | 336 | REROLL | STABILIZE | 86.0 | 5 | 9 | 0 | 22.0 | Devastador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 337 | REROLL | STABILIZE | 86.0 | 5 | 7 | 0 | 22.0 | Devastador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 338 | BUY | STABILIZE | 86.0 | 5 | 5 | 0 | 22.0 | Devastador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079986572265625 | 0.0 | 0.0 | +61c89fb9-3f6f-4386-a3b9-5e4fc71ee9c3 / -— |
| Jogador 3 | 3-5 | 339 | SELL | STABILIZE | 86.0 | 5 | 4 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3070161044597626 | 0.0 | 0.0 | +— / -407092ea-3a14-4555-9ebd-64a36c41d1d0 |
| Jogador 3 | 3-5 | 340 | BUY | STABILIZE | 86.0 | 5 | 9 | 0 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2872525751590729 | 0.0 | 0.0 | +1932532c-8c2d-45c1-bdcc-77fc7d6bb4a8 / -— |
| Jogador 3 | 3-5 | 341 | REROLL | STABILIZE | 86.0 | 5 | 8 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 342 | PASS | STABILIZE | 86.0 | 5 | 6 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 347 | SELL | STABILIZE | 86.0 | 5 | 12 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34209200739860535 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 3 | 3-6 | 348 | BUY | STABILIZE | 86.0 | 5 | 15 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8040778040885925 | 0.0 | 0.0 | +77c36245-d5ea-4f94-bc0c-680d4a77794a / -— |
| Jogador 3 | 3-6 | 349 | REROLL | STABILIZE | 86.0 | 5 | 14 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 350 | REROLL | STABILIZE | 86.0 | 5 | 12 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 351 | SELL | STABILIZE | 86.0 | 5 | 10 | 1 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05972079187631607 | 0.0 | 0.0 | +— / -db7ea53f-4df7-4c05-9462-75b527575615 |
| Jogador 3 | 3-6 | 352 | BUY | STABILIZE | 86.0 | 5 | 12 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7239784598350525 | 0.0 | 0.0 | +42dcd971-9003-42c7-89f4-271ba5fe868d / -— |
| Jogador 3 | 3-6 | 353 | SELL | STABILIZE | 86.0 | 5 | 9 | 0 | 22.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08867363631725311 | 0.0 | 0.0 | +— / -910b14c4-57bc-44ce-b925-30a6d92a7651 |
| Jogador 3 | 3-6 | 354 | BUY | STABILIZE | 86.0 | 5 | 11 | 1 | 22.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379992842674255 | 0.0 | 0.0 | +0498225d-8106-4d05-8c91-f11b7c94904f / -3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58,61c89fb9-3f6f-4386-a3b9-5e4fc71ee9c3 |
| Jogador 3 | 3-6 | 355 | REROLL | STABILIZE | 86.0 | 5 | 10 | 1 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 356 | BUY | STABILIZE | 86.0 | 5 | 8 | 0 | 20.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8339857459068298 | 0.0 | 0.0 | +6f89a47a-1ab1-48ed-ba66-bcbaa3e74231 / -42dcd971-9003-42c7-89f4-271ba5fe868d,98558a52-389f-46fc-b370-6345603f4103 |
| Jogador 3 | 3-6 | 357 | PASS | STABILIZE | 86.0 | 5 | 5 | 0 | 14.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 362 | MOVE_BENCH | STABILIZE | 76.0 | 5 | 10 | 1 | 14.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24818679690361023 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 363 | MOVE_BENCH | STABILIZE | 76.0 | 5 | 10 | 1 | 16.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5813395380973816 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 364 | MOVE_BOARD | STABILIZE | 76.0 | 5 | 10 | 1 | 20.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012201494537293911 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 365 | BUY | STABILIZE | 76.0 | 5 | 10 | 1 | 20.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03797351196408272 | 0.0 | 0.0 | +dbe39ade-b405-44db-9289-c7dd9e840754 / -— |
| Jogador 3 | 3-7 | 366 | REROLL | STABILIZE | 76.0 | 5 | 7 | 0 | 20.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 367 | BUY | STABILIZE | 76.0 | 5 | 5 | 0 | 20.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8371427655220032 | 0.0 | 0.0 | +876b71be-47f0-45df-800e-d40cb8905423 / -1932532c-8c2d-45c1-bdcc-77fc7d6bb4a8,77c36245-d5ea-4f94-bc0c-680d4a77794a |
| Jogador 3 | 3-7 | 368 | MOVE_BENCH | STABILIZE | 76.0 | 5 | 4 | 0 | 18.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4212982654571533 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 369 | BUY | STABILIZE | 76.0 | 5 | 4 | 0 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28799861669540405 | 0.0 | 0.0 | +b3d39de6-2ee8-41d3-bd7d-fe6efb7067b1 / -— |
| Jogador 3 | 3-7 | 370 | REROLL | STABILIZE | 76.0 | 5 | 3 | 0 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 371 | MOVE_BOARD | STABILIZE | 76.0 | 5 | 1 | 0 | 24.0 | Devastador/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008522948483005166 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 372 | PASS | STABILIZE | 76.0 | 5 | 1 | 0 | 24.0 | Devastador/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 376 | BUY | STABILIZE | 76.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28659769892692566 | 0.0 | 0.0 | +0805d2e7-a19e-4760-b726-78436ad911b1 / -— |
| Jogador 3 | 4-1 | 377 | BUY | STABILIZE | 76.0 | 5 | 5 | 0 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28260233998298645 | 0.0 | 0.0 | +6375ddab-b4ed-4bec-b6fd-1178b2bc1843 / -— |
| Jogador 3 | 4-1 | 378 | CRAFT_AND_EQUIP | STABILIZE | 76.0 | 5 | 3 | 0 | 24.0 | Devastador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 379 | CRAFT_AND_EQUIP | STABILIZE | 76.0 | 5 | 3 | 0 | 24.0 | Devastador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16295602917671204 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 380 | REROLL | STABILIZE | 76.0 | 5 | 3 | 0 | 24.0 | Devastador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 381 | SELL | STABILIZE | 76.0 | 5 | 1 | 0 | 24.0 | Devastador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26169198751449585 | 0.0 | 0.0 | +— / -876b71be-47f0-45df-800e-d40cb8905423 |
| Jogador 3 | 4-1 | 382 | BUY | STABILIZE | 76.0 | 5 | 4 | 0 | 24.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079986572265625 | 0.0 | 0.0 | +0088ca46-2bd7-4e4e-a102-8cfdc86bc494 / -— |
| Jogador 3 | 4-1 | 383 | REROLL | STABILIZE | 76.0 | 5 | 3 | 0 | 24.0 | Devastador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 384 | MOVE_BOARD | STABILIZE | 76.0 | 5 | 1 | 0 | 24.0 | Devastador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 385 | MOVE_BOARD | STABILIZE | 76.0 | 5 | 1 | 0 | 24.0 | Devastador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 386 | PASS | STABILIZE | 76.0 | 5 | 1 | 0 | 24.0 | Devastador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 388 | SELL | STABILIZE | 76.0 | 6 | 7 | 0 | 24.0 | Devastador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28049999475479126 | 0.0 | 0.0 | +— / -6f89a47a-1ab1-48ed-ba66-bcbaa3e74231 |
| Jogador 3 | 4-2 | 389 | EQUIP_FROM_INVENTORY | STABILIZE | 76.0 | 6 | 15 | 1 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06805270910263062 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 390 | BUY | STABILIZE | 76.0 | 6 | 15 | 1 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.801967442035675 | 0.0 | 0.0 | +6f557758-bcc6-4354-9119-c86fc5dde945 / -— |
| Jogador 3 | 4-2 | 391 | REROLL | STABILIZE | 76.0 | 6 | 13 | 1 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 392 | SELL | STABILIZE | 76.0 | 6 | 11 | 1 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.628000020980835 | 0.0 | 0.0 | +— / -b3d39de6-2ee8-41d3-bd7d-fe6efb7067b1 |
| Jogador 3 | 4-2 | 393 | BUY | STABILIZE | 76.0 | 6 | 12 | 1 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7998717427253723 | 0.0 | 0.0 | +f58ffa1b-941a-4e40-a60e-25f6b4293fc7 / -— |
| Jogador 3 | 4-2 | 394 | REROLL | STABILIZE | 76.0 | 6 | 11 | 1 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 395 | SELL | STABILIZE | 76.0 | 6 | 9 | 0 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2944999933242798 | 0.0 | 0.0 | +— / -0088ca46-2bd7-4e4e-a102-8cfdc86bc494 |
| Jogador 3 | 4-2 | 396 | BUY | STABILIZE | 76.0 | 6 | 10 | 1 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7164624929428101 | 0.0 | 0.0 | +31b8f77b-a5e2-4a86-b937-6cfe7b282e6d / -— |
| Jogador 3 | 4-2 | 397 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 7 | 0 | 24.0 | Devastador/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42270010709762573 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 398 | PASS | FAST8 | 76.0 | 6 | 7 | 0 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 402 | MOVE_BOARD | FAST8 | 76.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -5.973100269329734e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 403 | MOVE_BOARD | FAST8 | 76.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 404 | PASS | FAST8 | 76.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 413 | MOVE_BOARD | FAST8 | 76.0 | 6 | 22 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 414 | MOVE_BOARD | FAST8 | 76.0 | 6 | 22 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014850112609565258 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 415 | PASS | FAST8 | 76.0 | 6 | 22 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10999999940395355 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 423 | BUY | FAST8 | 76.0 | 6 | 30 | 3 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1979987919330597 | 0.0 | 0.0 | +8d8a6e85-5880-48c8-9f78-abdfcf0de5be / -— |
| Jogador 3 | 4-5 | 424 | MOVE_BOARD | FAST8 | 76.0 | 6 | 29 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0001557579671498388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 425 | MOVE_BOARD | FAST8 | 76.0 | 6 | 29 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015023156069219112 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 426 | MOVE_BOARD | FAST8 | 76.0 | 6 | 29 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014995913952589035 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 427 | PASS | FAST8 | 76.0 | 6 | 29 | 2 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 434 | SELL | FAST8 | 76.0 | 6 | 39 | 3 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2944999933242798 | 0.0 | 0.0 | +— / -8d8a6e85-5880-48c8-9f78-abdfcf0de5be |
| Jogador 3 | 4-6 | 435 | BUY | FAST8 | 76.0 | 6 | 40 | 4 | 26.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20656490325927734 | 0.0 | 0.0 | +66bd6f3f-7045-4580-9bb2-42895d646912 / -— |
| Jogador 3 | 4-6 | 436 | MOVE_BOARD | FAST8 | 76.0 | 6 | 37 | 3 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 437 | MOVE_BOARD | FAST8 | 76.0 | 6 | 37 | 3 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 438 | PASS | FAST8 | 76.0 | 6 | 37 | 3 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.040714286267757416 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 445 | MOVE_BENCH | FAST8 | 65.0 | 6 | 45 | 4 | 26.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09771032631397247 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 446 | MOVE_BENCH | FAST8 | 65.0 | 6 | 45 | 4 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499873995780945 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 447 | MOVE_BOARD | FAST8 | 65.0 | 6 | 45 | 4 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 448 | PASS | FAST8 | 65.0 | 6 | 45 | 4 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04642857238650322 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 455 | CRAFT_AND_EQUIP | FAST8 | 65.0 | 6 | 54 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2045421004295349 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 456 | CRAFT_AND_EQUIP | FAST8 | 65.0 | 6 | 54 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14072878658771515 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 457 | MOVE_BENCH | FAST8 | 65.0 | 6 | 54 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09999482333660126 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 458 | MOVE_BENCH | FAST8 | 65.0 | 6 | 54 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41508349776268005 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 459 | MOVE_BENCH | FAST8 | 65.0 | 6 | 54 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31491512060165405 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 460 | PASS | FAST8 | 65.0 | 6 | 54 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09039177000522614 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 465 | MOVE_BENCH | FAST8 | 65.0 | 6 | 65 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09993565082550049 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 466 | MOVE_BENCH | FAST8 | 65.0 | 6 | 65 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6627777814865112 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 467 | MOVE_BENCH | FAST8 | 65.0 | 6 | 65 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3149421513080597 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 468 | PASS | FAST8 | 65.0 | 6 | 65 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0982365682721138 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 475 | SELL | FAST8 | 65.0 | 6 | 77 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5412750244140625 | 0.0 | 0.0 | +— / -5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 5-3 | 476 | BUY | FAST8 | 65.0 | 6 | 80 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9494928121566772 | 0.0 | 0.0 | +a1848184-da18-4e8e-b7a5-41cde2673904 / -362f7357-283e-4f88-bff3-ffa6314af821,6f557758-bcc6-4354-9119-c86fc5dde945 |
| Jogador 3 | 5-3 | 477 | BUY | FAST8 | 65.0 | 6 | 78 | 5 | 28.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35980311036109924 | 0.0 | 0.0 | +05ae971c-7924-42fa-b861-d9363a1b2b0a / -— |
| Jogador 3 | 5-3 | 478 | MOVE_BENCH | FAST8 | 65.0 | 6 | 75 | 5 | 28.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09614364802837372 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 479 | MOVE_BENCH | FAST8 | 65.0 | 6 | 75 | 5 | 34.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08381716907024384 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 480 | MOVE_BENCH | FAST8 | 65.0 | 6 | 75 | 5 | 32.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7652680277824402 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 481 | MOVE_BENCH | FAST8 | 65.0 | 6 | 75 | 5 | 28.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08114111423492432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 482 | MOVE_BENCH | FAST8 | 65.0 | 6 | 75 | 5 | 34.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08381911367177963 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 484 | MOVE_BENCH | FAST8 | 65.0 | 6 | 87 | 5 | 32.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2507705092430115 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 485 | MOVE_BENCH | FAST8 | 65.0 | 6 | 87 | 5 | 30.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41395795345306396 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 486 | PASS | FAST8 | 65.0 | 6 | 87 | 5 | 34.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26963603496551514 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 494 | BUY | FAST8 | 65.0 | 6 | 98 | 5 | 34.0 | Devastador/DA_18_Warwick | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3950009047985077 | 0.0 | 0.0 | +93ba6ab0-57c7-4d25-bc20-cf37ba106cf4 / -— |
| Jogador 3 | 5-5 | 495 | MOVE_BENCH | FAST8 | 65.0 | 6 | 96 | 5 | 34.0 | Devastador/DA_18_Warwick | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7104370594024658 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 496 | MOVE_BENCH | FAST8 | 65.0 | 6 | 96 | 5 | 28.0 | Devastador/DA_18_Warwick | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08505000174045563 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 497 | MOVE_BENCH | FAST8 | 65.0 | 6 | 96 | 5 | 30.0 | Devastador/DA_18_Warwick | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41390514373779297 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 498 | MOVE_BENCH | FAST8 | 65.0 | 6 | 96 | 5 | 34.0 | Devastador/DA_18_Warwick | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7254396080970764 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 499 | PASS | FAST8 | 65.0 | 6 | 96 | 5 | 28.0 | Devastador/DA_18_Warwick | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12311458587646484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 503 | SELL | FAST8 | 65.0 | 6 | 107 | 5 | 28.0 | Devastador/DA_18_Warwick | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3668519854545593 | 0.0 | 0.0 | +— / -a1848184-da18-4e8e-b7a5-41cde2673904 |
| Jogador 3 | 5-6 | 504 | BUY | FAST8 | 65.0 | 6 | 112 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8877955675125122 | 0.0 | 0.0 | +350b71be-3cdb-4da2-aeef-0be87772e418 / -— |
| Jogador 3 | 5-6 | 505 | MOVE_BENCH | FAST8 | 65.0 | 6 | 109 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09828183054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 506 | SELL | FAST8 | 65.0 | 6 | 109 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26037999987602234 | 0.0 | 0.0 | +— / -943437ce-e190-4790-986b-4e66e49637a7 |
| Jogador 3 | 5-6 | 507 | BUY | FAST8 | 65.0 | 6 | 111 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8495027422904968 | 0.0 | 0.0 | +62e15c47-d04c-469b-8439-f0ae0499b6aa / -— |
| Jogador 3 | 5-6 | 508 | MOVE_BENCH | FAST8 | 65.0 | 6 | 109 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09861886501312256 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 509 | MOVE_BENCH | FAST8 | 65.0 | 6 | 109 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4149632155895233 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 510 | MOVE_BENCH | FAST8 | 65.0 | 6 | 109 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08340256661176682 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 512 | SELL | FAST8 | 65.0 | 6 | 121 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27086034417152405 | 0.0 | 0.0 | +— / -05ae971c-7924-42fa-b861-d9363a1b2b0a |
| Jogador 3 | 5-7 | 513 | BUY | FAST8 | 65.0 | 6 | 124 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.849555253982544 | 0.0 | 0.0 | +417431c9-5b55-4e64-bfd4-f6be7b3b5912 / -— |
| Jogador 3 | 5-7 | 514 | MOVE_BENCH | FAST8 | 65.0 | 6 | 122 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09935048967599869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 515 | MOVE_BENCH | FAST8 | 65.0 | 6 | 122 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4149642586708069 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 516 | MOVE_BENCH | FAST8 | 65.0 | 6 | 122 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08337462693452835 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 517 | MOVE_BENCH | FAST8 | 65.0 | 6 | 122 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08434917777776718 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 518 | MOVE_BENCH | FAST8 | 65.0 | 6 | 122 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4149649739265442 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 519 | MOVE_BENCH | FAST8 | 65.0 | 6 | 122 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7179088592529297 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 520 | PASS | FAST8 | 65.0 | 6 | 122 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14548039436340332 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 522 | EQUIP_FROM_INVENTORY | FAST8 | 65.0 | 6 | 133 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08069960027933121 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 523 | MOVE_BENCH | FAST8 | 65.0 | 6 | 133 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10013166815042496 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 524 | MOVE_BENCH | FAST8 | 65.0 | 6 | 133 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4147641062736511 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 525 | MOVE_BENCH | FAST8 | 65.0 | 6 | 133 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7722819447517395 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 526 | PASS | FAST8 | 65.0 | 6 | 133 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1693210005760193 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 532 | MOVE_BENCH | FAST8 | 47.0 | 6 | 143 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10013385117053986 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 533 | MOVE_BENCH | FAST8 | 47.0 | 6 | 143 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41476115584373474 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 534 | MOVE_BENCH | FAST8 | 47.0 | 6 | 143 | 5 | 32.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.655936598777771 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 535 | PASS | FAST8 | 47.0 | 6 | 143 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17909477651119232 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 542 | MOVE_BENCH | FAST8 | 47.0 | 6 | 154 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09997184574604034 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 543 | MOVE_BENCH | FAST8 | 47.0 | 6 | 154 | 5 | 28.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7253299951553345 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 544 | SELL | FAST8 | 47.0 | 6 | 154 | 5 | 30.0 | Devastador/DA_18_Akali_AD | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3765000104904175 | 0.0 | 0.0 | +— / -0498225d-8106-4d05-8c91-f11b7c94904f |
| Jogador 3 | 6-3 | 545 | EQUIP_FROM_INVENTORY | FAST8 | 47.0 | 6 | 157 | 5 | 30.0 | Devastador/DA_18_Diana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04249311238527298 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 546 | EQUIP_FROM_INVENTORY | FAST8 | 47.0 | 6 | 157 | 5 | 30.0 | Devastador/DA_18_Diana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.055838074535131454 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 547 | BUY | FAST8 | 47.0 | 6 | 157 | 5 | 30.0 | Devastador/DA_18_Diana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4754512310028076 | 0.0 | 0.0 | +f90a87cd-1091-462f-a639-46107a1ca207 / -— |
| Jogador 3 | 6-3 | 548 | MOVE_BENCH | FAST8 | 47.0 | 6 | 155 | 5 | 30.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6399955749511719 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 549 | MOVE_BENCH | FAST8 | 47.0 | 6 | 155 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08492877334356308 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 550 | MOVE_BENCH | FAST8 | 47.0 | 6 | 155 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09642117470502853 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 552 | MOVE_BENCH | FAST8 | 47.0 | 6 | 167 | 5 | 30.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7069031000137329 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 553 | SELL | FAST8 | 47.0 | 6 | 167 | 5 | 32.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4729520082473755 | 0.0 | 0.0 | +— / -f58ffa1b-941a-4e40-a60e-25f6b4293fc7 |
| Jogador 3 | 6-4 | 554 | BUY | FAST8 | 47.0 | 6 | 168 | 5 | 32.0 | Devastador/DA_18_Diana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3839057683944702 | 0.0 | 0.0 | +fa03a1fd-0ed3-42a8-9d5d-a75a7fe38fd3 / -— |
| Jogador 3 | 6-4 | 555 | MOVE_BENCH | FAST8 | 47.0 | 6 | 167 | 5 | 32.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09974978119134903 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 556 | MOVE_BENCH | FAST8 | 47.0 | 6 | 167 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41495460271835327 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 557 | MOVE_BENCH | FAST8 | 47.0 | 6 | 167 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026650849729776382 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 558 | MOVE_BENCH | FAST8 | 47.0 | 6 | 167 | 5 | 32.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08475647121667862 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 559 | MOVE_BENCH | FAST8 | 47.0 | 6 | 167 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41495558619499207 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 560 | MOVE_BENCH | FAST8 | 47.0 | 6 | 167 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0999855101108551 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 562 | MOVE_BENCH | FAST8 | 47.0 | 6 | 178 | 5 | 30.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031947504729032516 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 563 | MOVE_BENCH | FAST8 | 47.0 | 6 | 178 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.76204514503479 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 564 | MOVE_BENCH | FAST8 | 47.0 | 6 | 178 | 5 | 32.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08452239632606506 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 565 | MOVE_BENCH | FAST8 | 47.0 | 6 | 178 | 5 | 30.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04401382803916931 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 566 | MOVE_BENCH | FAST8 | 47.0 | 6 | 178 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7618557810783386 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 567 | MOVE_BENCH | FAST8 | 47.0 | 6 | 178 | 5 | 32.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3980095386505127 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 568 | PASS | FAST8 | 47.0 | 6 | 178 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21407921612262726 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 572 | MOVE_BENCH | FAST8 | 47.0 | 7 | 190 | 5 | 28.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5993193984031677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 573 | BUY | FAST8 | 47.0 | 7 | 190 | 5 | 34.0 | Devastador/DA_18_Diana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9485666155815125 | 0.0 | 0.0 | +874c674c-2608-4ae4-8d63-1dc3a091f635 / -— |
| Jogador 3 | 6-6 | 574 | MOVE_BOARD | FAST8 | 47.0 | 7 | 189 | 5 | 34.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 575 | MOVE_BOARD | FAST8 | 47.0 | 7 | 189 | 5 | 34.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 576 | PASS | FAST8 | 47.0 | 7 | 189 | 5 | 34.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22528816759586334 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-7 | 582 | SELL | FAST8 | 47.0 | 7 | 201 | 5 | 34.0 | Devastador/DA_18_Diana | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24089199304580688 | 0.0 | 0.0 | +— / -0805d2e7-a19e-4760-b726-78436ad911b1 |
| Jogador 3 | 6-7 | 583 | BUY | FAST8 | 47.0 | 7 | 202 | 5 | 34.0 | Devastador/DA_18_Diana | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.009895920753479 | 0.0 | 0.0 | +9008a31e-0e47-4170-9bc6-2d44c2c88395 / -62e15c47-d04c-469b-8439-f0ae0499b6aa,6375ddab-b4ed-4bec-b6fd-1178b2bc1843 |
| Jogador 3 | 6-7 | 584 | BUY | FAST8 | 47.0 | 7 | 200 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2751375138759613 | 0.0 | 0.0 | +cfd3ba9f-8197-4822-ac15-34dc514c7c06 / -— |
| Jogador 3 | 6-7 | 585 | MOVE_BOARD | FAST8 | 47.0 | 7 | 198 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 6.224236130947247e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-7 | 586 | MOVE_BOARD | FAST8 | 47.0 | 7 | 198 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015102362260222435 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-7 | 587 | MOVE_BOARD | FAST8 | 47.0 | 7 | 198 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-7 | 588 | PASS | FAST8 | 47.0 | 7 | 198 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40252572298049927 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 592 | EQUIP_FROM_INVENTORY | FAST8 | 47.0 | 7 | 209 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0714000016450882 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 593 | BUY | FAST8 | 47.0 | 7 | 209 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0094618797302246 | 0.0 | 0.0 | +960df220-42b3-42b0-ab7e-d89acfd2b46c / -417431c9-5b55-4e64-bfd4-f6be7b3b5912,93ba6ab0-57c7-4d25-bc20-cf37ba106cf4 |
| Jogador 3 | 7-1 | 594 | BUY | FAST8 | 47.0 | 7 | 207 | 5 | 34.0 | Devastador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0091098546981812 | 0.0 | 0.0 | +7c9a635f-2222-4cfa-86c4-ab5e27b33ad2 / -31b8f77b-a5e2-4a86-b937-6cfe7b282e6d,dbe39ade-b405-44db-9289-c7dd9e840754 |
| Jogador 3 | 7-1 | 595 | MOVE_BENCH | FAST8 | 47.0 | 7 | 204 | 5 | 28.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09261970221996307 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 596 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 204 | 5 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38939589262008667 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 597 | MOVE_BOARD | FAST8 | 47.0 | 7 | 204 | 5 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010071668773889542 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 598 | MOVE_BENCH | FAST8 | 47.0 | 7 | 204 | 5 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09715250134468079 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 599 | MOVE_BENCH | FAST8 | 47.0 | 7 | 204 | 5 | 36.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08142980188131332 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 600 | MOVE_BOARD | FAST8 | 47.0 | 7 | 204 | 5 | 38.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-2 | 602 | BUY | FAST8 | 47.0 | 7 | 217 | 5 | 38.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07253057509660721 | 0.0 | 0.0 | +90b68954-1c93-477d-aa66-152148d0443f / -— |
| Jogador 3 | 7-2 | 603 | BUY | FAST8 | 47.0 | 7 | 214 | 5 | 38.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24502959847450256 | 0.0 | 0.0 | +5f64aaee-ddcb-43b6-b368-d8160c3eee67 / -— |
| Jogador 3 | 7-2 | 604 | MOVE_BOARD | FAST8 | 47.0 | 7 | 210 | 5 | 38.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-2 | 605 | MOVE_BOARD | FAST8 | 47.0 | 7 | 210 | 5 | 38.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014900407753884792 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-2 | 606 | PASS | FAST8 | 47.0 | 7 | 210 | 5 | 38.0 | Devastador/DA_Fiddlesticks18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4149296283721924 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7106347680091858 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42604145407676697 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.040587835013866425 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04059188812971115 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7344216704368591 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48277533054351807 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17116713523864746 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 60 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059527866542339325 | 0.0 | 0.0 | +34439867-85f7-4392-a985-337c6af81a1a / -— |
| Jogador 4 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010326534509658813 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04556276649236679 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004066083114594221 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0006478755967691541 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 69 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.01265287399292 | 0.0 | 0.0 | +4fbb2e46-1524-47c6-85a1-79266fd4da28 / -— |
| Jogador 4 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33894720673561096 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9755119681358337 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02010534144937992 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 91 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9806723594665527 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 115 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3914872109889984 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 116 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15649743378162384 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 117 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11584341526031494 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 118 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.850678026676178 | 0.0 | 0.0 | +838eb81f-88a4-41a2-b2e5-7d6784d86773 / -— |
| Jogador 4 | 2-1 | 119 | REROLL | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 120 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07373570650815964 | 0.0 | 0.0 | +— / -57f213f7-34b1-4a4a-8047-afa5e404e5c4 |
| Jogador 4 | 2-1 | 121 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18365584313869476 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 4 | 2-1 | 122 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00020089421013835818 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 123 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01587444730103016 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 124 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 139 | BUY | STABILIZE | 94.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.947799026966095 | 0.0 | 0.0 | +3c6ac558-6b59-4a97-814e-bff0ff895232 / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793,eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-2 | 140 | BUY | STABILIZE | 94.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0156217813491821 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -4fbb2e46-1524-47c6-85a1-79266fd4da28,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-2 | 141 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8324756026268005 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 142 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5834711790084839 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 143 | BUY | STABILIZE | 94.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2979184091091156 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 4 | 2-2 | 144 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 145 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006430448032915592 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 146 | PASS | STABILIZE | 94.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 162 | BUY | STABILIZE | 88.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3527976870536804 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 4 | 2-3 | 163 | BUY | STABILIZE | 88.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8884117603302002 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 4 | 2-3 | 164 | REROLL | STABILIZE | 88.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 165 | BUY | STABILIZE | 88.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9476871490478516 | 0.0 | 0.0 | +0c6afd45-be8c-4f89-8fdc-938247537ab9 / -2c7e844d-925a-43bb-8be8-65a71d11f964,fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 4 | 2-3 | 166 | BUY | STABILIZE | 88.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359877467155457 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -— |
| Jogador 4 | 2-3 | 167 | SELL | STABILIZE | 88.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21771599352359772 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 4 | 2-3 | 168 | EQUIP_FROM_INVENTORY | STABILIZE | 88.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13382108509540558 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 169 | EQUIP_FROM_INVENTORY | STABILIZE | 88.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10471868515014648 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 170 | REROLL | STABILIZE | 88.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 171 | BUY | STABILIZE | 88.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8971366882324219 | 0.0 | 0.0 | +032b5960-ec2a-4a26-ad67-862a20f30523 / -— |
| Jogador 4 | 2-3 | 172 | PASS | STABILIZE | 88.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 183 | BUY | STABILIZE | 88.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9493377804756165 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -032b5960-ec2a-4a26-ad67-862a20f30523,9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 2-4 | 184 | BUY | STABILIZE | 88.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33180367946624756 | 0.0 | 0.0 | +19cba1be-95ae-4cf0-a600-0c5eb8d081b0 / -— |
| Jogador 4 | 2-4 | 185 | BUY | STABILIZE | 88.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15497533977031708 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 4 | 2-4 | 186 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Xayah | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018156735226511955 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 187 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Xayah | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5050302147865295 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 188 | REROLL | STABILIZE | 88.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 189 | BUY | STABILIZE | 88.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8991560339927673 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 4 | 2-4 | 190 | SELL | STABILIZE | 88.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25427067279815674 | 0.0 | 0.0 | +— / -0c6afd45-be8c-4f89-8fdc-938247537ab9 |
| Jogador 4 | 2-4 | 191 | BUY | STABILIZE | 88.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8958880305290222 | 0.0 | 0.0 | +7115c5a0-d443-49d8-b8a4-e51e259572df / -— |
| Jogador 4 | 2-4 | 192 | REROLL | STABILIZE | 88.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 193 | PASS | STABILIZE | 88.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 205 | SELL | STABILIZE | 88.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20916399359703064 | 0.0 | 0.0 | +— / -3c6ac558-6b59-4a97-814e-bff0ff895232 |
| Jogador 4 | 2-5 | 206 | BUY | STABILIZE | 88.0 | 4 | 8 | 0 | 10.0 | Sabugueiro/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16103343665599823 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 4 | 2-5 | 207 | SELL | STABILIZE | 88.0 | 4 | 7 | 0 | 10.0 | Sabugueiro/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1933351755142212 | 0.0 | 0.0 | +— / -6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 4 | 2-5 | 208 | BUY | STABILIZE | 88.0 | 4 | 10 | 1 | 10.0 | Sabugueiro/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7036653757095337 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -7115c5a0-d443-49d8-b8a4-e51e259572df,a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 4 | 2-5 | 209 | BUY | STABILIZE | 88.0 | 4 | 9 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19959501922130585 | 0.0 | 0.0 | +566309fd-e810-47ec-b876-a8705c1170ab / -— |
| Jogador 4 | 2-5 | 210 | REROLL | STABILIZE | 88.0 | 4 | 6 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 211 | BUY | STABILIZE | 88.0 | 4 | 4 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.945978045463562 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -34439867-85f7-4392-a985-337c6af81a1a,838eb81f-88a4-41a2-b2e5-7d6784d86773 |
| Jogador 4 | 2-5 | 212 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 3 | 0 | 6.0 | Sabugueiro/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13382868468761444 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 213 | BUY | STABILIZE | 88.0 | 4 | 3 | 0 | 8.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13882800936698914 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 4 | 2-5 | 214 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 2 | 0 | 8.0 | Sabugueiro/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40511947870254517 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 215 | PASS | STABILIZE | 88.0 | 4 | 2 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 225 | BUY | STABILIZE | 88.0 | 5 | 9 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13646511733531952 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 4 | 2-6 | 226 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38898611068725586 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 227 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 12.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40775442123413086 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 228 | PASS | STABILIZE | 88.0 | 5 | 7 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 241 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 10.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4030696451663971 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 243 | BUY | STABILIZE | 88.0 | 5 | 14 | 1 | 12.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9493544101715088 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -0e9aa759-0538-4168-a523-02a5f8e09e0a,9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 2-7 | 244 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 13 | 1 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05977471545338631 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 245 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 13 | 1 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30861493945121765 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 246 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 13 | 1 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0352645218372345 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 247 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 13 | 1 | 12.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7283143401145935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 248 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 13 | 1 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.312440425157547 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 249 | PASS | STABILIZE | 88.0 | 5 | 13 | 1 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 259 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 13 | 1 | 10.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5734235644340515 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 262 | BUY | STABILIZE | 88.0 | 5 | 20 | 2 | 14.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7198767066001892 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 4 | 3-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 5 | 18 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21593134105205536 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 264 | REROLL | STABILIZE | 88.0 | 5 | 18 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 265 | REROLL | STABILIZE | 88.0 | 5 | 16 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 266 | BUY | STABILIZE | 88.0 | 5 | 14 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8378734588623047 | 0.0 | 0.0 | +7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed / -19cba1be-95ae-4cf0-a600-0c5eb8d081b0,e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 4 | 3-1 | 267 | BUY | STABILIZE | 88.0 | 5 | 13 | 1 | 12.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7855079174041748 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 4 | 3-1 | 268 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 12 | 1 | 12.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06096893921494484 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 269 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 12 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3686613142490387 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 270 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 12 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2526744306087494 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 271 | PASS | STABILIZE | 88.0 | 5 | 12 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 278 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 12 | 1 | 14.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09490007907152176 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 282 | BUY | STABILIZE | 79.0 | 5 | 18 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879818081855774 | 0.0 | 0.0 | +1f7f2a48-1318-4fc6-87cc-03d557bf69ea / -— |
| Jogador 4 | 3-2 | 283 | REROLL | STABILIZE | 79.0 | 5 | 17 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 284 | REROLL | STABILIZE | 79.0 | 5 | 15 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 285 | REROLL | STABILIZE | 79.0 | 5 | 13 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 286 | REROLL | STABILIZE | 79.0 | 5 | 11 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 287 | SELL | STABILIZE | 79.0 | 5 | 9 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010146821849048138 | 0.0 | 0.0 | +— / -a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 4 | 3-2 | 288 | BUY | STABILIZE | 79.0 | 5 | 12 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8064174056053162 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -— |
| Jogador 4 | 3-2 | 289 | REROLL | STABILIZE | 79.0 | 5 | 11 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 290 | SELL | STABILIZE | 79.0 | 5 | 9 | 0 | 18.0 | Sabugueiro/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17784132063388824 | 0.0 | 0.0 | +— / -7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed |
| Jogador 4 | 3-2 | 291 | EQUIP_FROM_INVENTORY | STABILIZE | 79.0 | 5 | 12 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10253247618675232 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 292 | PASS | STABILIZE | 79.0 | 5 | 12 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 302 | REROLL | STABILIZE | 79.0 | 5 | 19 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 303 | REROLL | STABILIZE | 79.0 | 5 | 17 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 304 | REROLL | STABILIZE | 79.0 | 5 | 15 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 305 | REROLL | STABILIZE | 79.0 | 5 | 13 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 306 | BUY | STABILIZE | 79.0 | 5 | 11 | 1 | 18.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8245165348052979 | 0.0 | 0.0 | +9414ca8e-930e-4a0e-8cbd-42d8997d8705 / -26462e09-ab6e-4b87-85a8-6bda974b0c45,561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 4 | 3-3 | 307 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33527395129203796 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 308 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.839299201965332 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 309 | PASS | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 311 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 10 | 1 | 16.0 | Sabugueiro/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5853718519210815 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 316 | REROLL | STABILIZE | 79.0 | 5 | 18 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 317 | REROLL | STABILIZE | 79.0 | 5 | 16 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 318 | REROLL | STABILIZE | 79.0 | 5 | 14 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 319 | REROLL | STABILIZE | 79.0 | 5 | 12 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 320 | REROLL | STABILIZE | 79.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 321 | REROLL | STABILIZE | 79.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 322 | REROLL | STABILIZE | 79.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 323 | REROLL | STABILIZE | 79.0 | 5 | 4 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 324 | REROLL | STABILIZE | 79.0 | 5 | 2 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 325 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 0 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06194368377327919 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 326 | PASS | STABILIZE | 79.0 | 5 | 0 | 0 | 18.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 332 | BUY | STABILIZE | 79.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079409599304199 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -0023f061-5310-4e39-849a-22ad49993d8c,4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 4 | 3-5 | 333 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32890987396240234 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 334 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 4 | 0 | 12.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5094632506370544 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 335 | REROLL | STABILIZE | 79.0 | 5 | 4 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 336 | BUY | STABILIZE | 79.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2789851725101471 | 0.0 | 0.0 | +1505b8ee-8c59-40ae-b774-fdce1230b8ef / -— |
| Jogador 4 | 3-5 | 337 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005798711441457272 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 338 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 339 | MOVE_BOARD | STABILIZE | 79.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017763732001185417 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 340 | PASS | STABILIZE | 79.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 347 | BUY | STABILIZE | 69.0 | 5 | 6 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24832122027873993 | 0.0 | 0.0 | +e22ad17a-827b-42f7-95a6-9e334471b0b9 / -— |
| Jogador 4 | 3-6 | 348 | REROLL | STABILIZE | 69.0 | 5 | 4 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 349 | REROLL | STABILIZE | 69.0 | 5 | 2 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 350 | MOVE_BOARD | STABILIZE | 69.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00874157715588808 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 351 | MOVE_BOARD | STABILIZE | 69.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 352 | PASS | STABILIZE | 69.0 | 5 | 0 | 0 | 16.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 362 | BUY | STABILIZE | 59.0 | 5 | 6 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7986317276954651 | 0.0 | 0.0 | +30d632db-738f-4a3c-84dc-ff4a4705ecdf / -— |
| Jogador 4 | 3-7 | 363 | SELL | STABILIZE | 59.0 | 5 | 5 | 0 | 16.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2301526665687561 | 0.0 | 0.0 | +— / -9414ca8e-930e-4a0e-8cbd-42d8997d8705 |
| Jogador 4 | 3-7 | 364 | BUY | STABILIZE | 59.0 | 5 | 8 | 0 | 16.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.836371660232544 | 0.0 | 0.0 | +15c32810-3029-4027-abcf-14005de787bf / -8a4d0946-b80f-4fbb-ab7c-d43c2697c34e,f3e882b5-333e-44e3-ae82-cacacc8b1137 |
| Jogador 4 | 3-7 | 365 | MOVE_BENCH | STABILIZE | 59.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4522755444049835 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 366 | REROLL | STABILIZE | 59.0 | 5 | 7 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 367 | BUY | STABILIZE | 59.0 | 5 | 5 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2847219407558441 | 0.0 | 0.0 | +877a1ed4-302c-493b-a973-ac9ca3d3e6a4 / -— |
| Jogador 4 | 3-7 | 368 | REROLL | STABILIZE | 59.0 | 5 | 4 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 369 | BUY | STABILIZE | 59.0 | 5 | 2 | 0 | 18.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8354266285896301 | 0.0 | 0.0 | +d6d15e43-3f39-40c6-8a07-a05854ef835d / -6084e8d8-82f2-47e3-b8e1-4077ad70efe5,9bd6852a-b7a4-468c-a8cc-5318f7906eae |
| Jogador 4 | 3-7 | 370 | MOVE_BENCH | STABILIZE | 59.0 | 5 | 0 | 0 | 10.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5920607447624207 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 371 | MOVE_BENCH | STABILIZE | 59.0 | 5 | 0 | 0 | 8.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1796387881040573 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 372 | PASS | STABILIZE | 59.0 | 5 | 0 | 0 | 12.0 | Colosso/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 376 | BUY | STABILIZE | 59.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8079961538314819 | 0.0 | 0.0 | +4d7ec7ee-5678-4796-a6e4-43af72c50bc3 / -— |
| Jogador 4 | 4-1 | 377 | CRAFT_AND_EQUIP | STABILIZE | 59.0 | 5 | 5 | 0 | 12.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2474905103445053 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 378 | CRAFT_AND_EQUIP | STABILIZE | 59.0 | 5 | 5 | 0 | 12.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.21380899846553802 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 379 | REROLL | STABILIZE | 59.0 | 5 | 5 | 0 | 12.0 | Colosso/DA_18_Akali_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 380 | SELL | STABILIZE | 59.0 | 5 | 3 | 0 | 12.0 | Colosso/DA_18_Akali_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40128400921821594 | 0.0 | 0.0 | +— / -15c32810-3029-4027-abcf-14005de787bf |
| Jogador 4 | 4-1 | 381 | BUY | STABILIZE | 59.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28478753566741943 | 0.0 | 0.0 | +35f90973-e578-4be1-aaa5-9ee8073b0776 / -— |
| Jogador 4 | 4-1 | 382 | SELL | STABILIZE | 59.0 | 5 | 4 | 0 | 12.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3321959972381592 | 0.0 | 0.0 | +— / -d6d15e43-3f39-40c6-8a07-a05854ef835d |
| Jogador 4 | 4-1 | 383 | MOVE_BENCH | STABILIZE | 59.0 | 5 | 9 | 0 | 12.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | True | 0.4418928623199463 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 384 | EQUIP_FROM_INVENTORY | STABILIZE | 59.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.16194897890090942 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 385 | BUY | STABILIZE | 59.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8004158735275269 | 0.0 | 0.0 | +f88e593a-bc21-43b4-afac-fdfb5c3afb35 / -— |
| Jogador 4 | 4-1 | 386 | PASS | STABILIZE | 59.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 388 | MOVE_BENCH | STABILIZE | 50.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0999116599559784 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 389 | MOVE_BENCH | STABILIZE | 50.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5771995186805725 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 390 | MOVE_BENCH | STABILIZE | 50.0 | 6 | 13 | 1 | 18.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3792359530925751 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 391 | PASS | STABILIZE | 50.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 397 | MOVE_BENCH | STABILIZE | 50.0 | 6 | 13 | 1 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42734235525131226 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 402 | REROLL | STABILIZE | 38.0 | 6 | 20 | 2 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23399999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 403 | REROLL | STABILIZE | 38.0 | 6 | 18 | 1 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 404 | REROLL | STABILIZE | 38.0 | 6 | 16 | 1 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 405 | REROLL | STABILIZE | 38.0 | 6 | 14 | 1 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 406 | REROLL | STABILIZE | 38.0 | 6 | 12 | 1 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 407 | REROLL | STABILIZE | 38.0 | 6 | 10 | 1 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 408 | BUY | STABILIZE | 38.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7916561961174011 | 0.0 | 0.0 | +9b2d1fe7-34d0-43fd-9f0a-d9b24a5383a9 / -— |
| Jogador 4 | 4-3 | 409 | REROLL | STABILIZE | 38.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 410 | REROLL | STABILIZE | 38.0 | 6 | 3 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 411 | BUY | STABILIZE | 38.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8008906841278076 | 0.0 | 0.0 | +736abf5b-a118-4174-964a-c264be63a40f / -— |
| Jogador 4 | 4-4 | 413 | REROLL | STABILIZE | 38.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 414 | REROLL | STABILIZE | 38.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 415 | SELL | STABILIZE | 38.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13665999472141266 | 0.0 | 0.0 | +— / -e22ad17a-827b-42f7-95a6-9e334471b0b9 |
| Jogador 4 | 4-4 | 416 | BUY | STABILIZE | 38.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28397464752197266 | 0.0 | 0.0 | +b2da3efe-dcf0-45d8-a04c-8479e0039c54 / -— |
| Jogador 4 | 4-4 | 417 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014647327363491058 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 418 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_LeBlanc | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003824929939582944 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 419 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01667521893978119 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 420 | PASS | STABILIZE | 38.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 423 | REROLL | STABILIZE | 38.0 | 6 | 7 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 424 | REROLL | STABILIZE | 38.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 425 | REROLL | STABILIZE | 38.0 | 6 | 3 | 0 | 24.0 | Colosso/DA_18_Yorick | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 426 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0029137826059013605 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 427 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015640277415513992 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 428 | MOVE_BOARD | STABILIZE | 38.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00774535583332181 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 429 | PASS | STABILIZE | 38.0 | 6 | 1 | 0 | 24.0 | Colosso/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 434 | SELL | STABILIZE | 27.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24171599745750427 | 0.0 | 0.0 | +— / -b2da3efe-dcf0-45d8-a04c-8479e0039c54 |
| Jogador 4 | 4-6 | 435 | BUY | STABILIZE | 27.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379989266395569 | 0.0 | 0.0 | +7a633b87-7843-4229-97b6-87f15674a3a9 / -1f7f2a48-1318-4fc6-87cc-03d557bf69ea,4d7ec7ee-5678-4796-a6e4-43af72c50bc3 |
| Jogador 4 | 4-6 | 436 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40178990364074707 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 437 | REROLL | STABILIZE | 27.0 | 6 | 7 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 438 | BUY | STABILIZE | 27.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8356624841690063 | 0.0 | 0.0 | +8274a707-0d7f-4247-9807-67fd058a9bca / -35f90973-e578-4be1-aaa5-9ee8073b0776,f88e593a-bc21-43b4-afac-fdfb5c3afb35 |
| Jogador 4 | 4-6 | 439 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09947378933429718 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 440 | REROLL | STABILIZE | 27.0 | 6 | 3 | 0 | 26.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 441 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40397313237190247 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 442 | MOVE_BOARD | STABILIZE | 27.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01492274459451437 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 443 | MOVE_BOARD | STABILIZE | 27.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016218096017837524 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 445 | REROLL | ALL_IN | 15.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 446 | BUY | ALL_IN | 15.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8135427832603455 | 0.0 | 0.0 | +7073577c-eeed-41fe-b295-c65b4b2ff03c / -1505b8ee-8c59-40ae-b774-fdce1230b8ef,30d632db-738f-4a3c-84dc-ff4a4705ecdf |
| Jogador 4 | 4-7 | 447 | BUY | ALL_IN | 15.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27300676703453064 | 0.0 | 0.0 | +b2366192-02e1-44e1-8736-7808cf55f373 / -— |
| Jogador 4 | 4-7 | 448 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002233050297945738 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 449 | BUY | ALL_IN | 15.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21016481518745422 | 0.0 | 0.0 | +eff5f3cb-b52e-44e7-9f04-1c8ea5ee73ec / -— |
| Jogador 4 | 4-7 | 450 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 451 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01495008822530508 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 452 | PASS | ALL_IN | 15.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 455 | BUY | ALL_IN | 15.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8256692290306091 | 0.0 | 0.0 | +e8609452-3ee8-4e44-81f3-140fc86601e3 / -6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97,736abf5b-a118-4174-964a-c264be63a40f |
| Jogador 4 | 5-1 | 456 | CRAFT_AND_EQUIP | ALL_IN | 15.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20254960656166077 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 457 | CRAFT_AND_EQUIP | ALL_IN | 15.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1534176915884018 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 458 | BUY | ALL_IN | 15.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2996506989002228 | 0.0 | 0.0 | +8e4d8d8b-7f1a-4026-9a21-27f11cee1bf3 / -— |
| Jogador 4 | 5-1 | 459 | REROLL | ALL_IN | 15.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 460 | REROLL | ALL_IN | 15.0 | 6 | 2 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 461 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026043113321065903 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 462 | MOVE_BOARD | ALL_IN | 15.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2360847294330597 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 463 | PASS | ALL_IN | 15.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 465 | BUY | ALL_IN | 1.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.277035653591156 | 0.0 | 0.0 | +da54ab9b-bc3c-4e2f-b9f6-5dc69c1de6ae / -— |
| Jogador 4 | 5-2 | 466 | REROLL | ALL_IN | 1.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 467 | BUY | ALL_IN | 1.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7299752235412598 | 0.0 | 0.0 | +27a61809-879e-4071-b586-d5d5968797bb / -— |
| Jogador 4 | 5-2 | 468 | MOVE_BOARD | ALL_IN | 1.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017849743599072099 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 469 | MOVE_BOARD | ALL_IN | 1.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 470 | PASS | ALL_IN | 1.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3222387135028839 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10612095892429352 | 0.0 | 0.0 | +02c39b42-90d5-4e01-9380-460b6c1cb993 / -— |
| Jogador 5 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6402381062507629 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41766050457954407 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.2695513963699341 | 0.0 | 0.0 | +9c678a7f-3209-4d1b-addd-385f7d4b89fa / -— |
| Jogador 5 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09030357003211975 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5726093649864197 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39686816930770874 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2752682566642761 | 0.0 | 0.0 | +3002832d-1e66-428b-a25e-007c716764a3 / -— |
| Jogador 5 | 1-3 | 60 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056116100400686264 | 0.0 | 0.0 | +9c93476e-a7be-457d-8543-8802507a8d3f / -— |
| Jogador 5 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021990563720464706 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010232674889266491 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08959921449422836 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010029196739196777 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006768754217773676 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 67 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 68 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32866206765174866 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 69 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32085517048835754 | 0.0 | 0.0 | +634004e3-6a89-4cb3-929d-39ef6d3bce3c / -— |
| Jogador 5 | 1-4 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08503548055887222 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34036198258399963 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007192936725914478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 91 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 92 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041122037917375565 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9727697968482971 | 0.0 | 0.0 | +eecc4b9d-82ef-4c04-ba8d-b299fcec55ed / -— |
| Jogador 5 | 2-1 | 115 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5398070812225342 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 116 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18643656373023987 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 117 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16079473495483398 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 118 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40222206711769104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 119 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26098549365997314 | 0.0 | 0.0 | +c1362110-700c-4ff7-9347-eaa6d512081b / -— |
| Jogador 5 | 2-1 | 120 | REROLL | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 121 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00041759328451007605 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 122 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016811536625027657 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 123 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 139 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9810956120491028 | 0.0 | 0.0 | +e6ac7c34-615e-4ccc-bc0f-8ba583bf5ca1 / -— |
| Jogador 5 | 2-2 | 140 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7450041174888611 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 5 | 2-2 | 141 | REROLL | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 142 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1521143764257431 | 0.0 | 0.0 | +37192022-05ce-4f51-b5d3-353242887fe1 / -— |
| Jogador 5 | 2-2 | 143 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06181051582098007 | 0.0 | 0.0 | +— / -9c678a7f-3209-4d1b-addd-385f7d4b89fa |
| Jogador 5 | 2-2 | 144 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12512852251529694 | 0.0 | 0.0 | +b1ecd1fa-793c-40ad-a9e3-9d35d5030339 / -— |
| Jogador 5 | 2-2 | 145 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 146 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008038325235247612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 147 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 162 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7648224234580994 | 0.0 | 0.0 | +fb186a97-59a4-4b3a-be2f-dadd2670dc95 / -— |
| Jogador 5 | 2-3 | 163 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007455337909050286 | 0.0 | 0.0 | +— / -b1ecd1fa-793c-40ad-a9e3-9d35d5030339 |
| Jogador 5 | 2-3 | 164 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013600600883364677 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 5 | 2-3 | 165 | REROLL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 166 | SELL | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011359999887645245 | 0.0 | 0.0 | +— / -c1362110-700c-4ff7-9347-eaa6d512081b |
| Jogador 5 | 2-3 | 167 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6863497495651245 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 5 | 2-3 | 168 | SELL | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006560000125318766 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 5 | 2-3 | 169 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8915321230888367 | 0.0 | 0.0 | +1d709136-338f-4fef-90fc-b2aa1b83d879 / -37192022-05ce-4f51-b5d3-353242887fe1,caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 5 | 2-3 | 170 | REROLL | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 171 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9496835470199585 | 0.0 | 0.0 | +14bbd76c-fca8-4017-89b5-e586bb1cae70 / -634004e3-6a89-4cb3-929d-39ef6d3bce3c,e6ac7c34-615e-4ccc-bc0f-8ba583bf5ca1 |
| Jogador 5 | 2-3 | 172 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 183 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9205996990203857 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -3002832d-1e66-428b-a25e-007c716764a3,6951a681-f5b9-4c22-9182-46b4d2c3cbb3 |
| Jogador 5 | 2-4 | 184 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.326839804649353 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 5 | 2-4 | 185 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6387689709663391 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 186 | REROLL | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 187 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8867665529251099 | 0.0 | 0.0 | +1e0a3ead-540d-4169-a1fc-3e79592564a0 / -— |
| Jogador 5 | 2-4 | 188 | REROLL | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 189 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24038082361221313 | 0.0 | 0.0 | +3acb90a6-bcf2-41d1-848f-f2aec19a2163 / -— |
| Jogador 5 | 2-4 | 190 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018693010788410902 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 191 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26273998618125916 | 0.0 | 0.0 | +— / -1d709136-338f-4fef-90fc-b2aa1b83d879 |
| Jogador 5 | 2-4 | 192 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.309773325920105 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 5 | 2-4 | 193 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 205 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11090332269668579 | 0.0 | 0.0 | +3f253868-2de5-4189-95a0-705f62682958 / -— |
| Jogador 5 | 2-5 | 206 | SELL | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1710847020149231 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 5 | 2-5 | 207 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09949542582035065 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -— |
| Jogador 5 | 2-5 | 208 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006149676628410816 | 0.0 | 0.0 | +— / -3f253868-2de5-4189-95a0-705f62682958 |
| Jogador 5 | 2-5 | 209 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.837489128112793 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 5 | 2-5 | 210 | REROLL | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 211 | SELL | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013120000250637531 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 5 | 2-5 | 212 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008879397064447403 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 5 | 2-5 | 213 | REROLL | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 214 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002266561146825552 | 0.0 | 0.0 | +— / -3acb90a6-bcf2-41d1-848f-f2aec19a2163 |
| Jogador 5 | 2-5 | 215 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 225 | BUY | STABILIZE | 100.0 | 5 | 11 | 1 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056922752410173416 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 5 | 2-6 | 226 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 8 | 0 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5714043974876404 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 227 | REROLL | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 228 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16923147439956665 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 5 | 2-6 | 229 | SELL | STABILIZE | 100.0 | 5 | 5 | 0 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3610999882221222 | 0.0 | 0.0 | +— / -65a6d68c-90ae-4e31-8bbc-82e8ec75b3de |
| Jogador 5 | 2-6 | 230 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7157594561576843 | 0.0 | 0.0 | +5a16a58c-7001-4448-8ca5-6293f35e2c94 / -— |
| Jogador 5 | 2-6 | 231 | REROLL | STABILIZE | 100.0 | 5 | 4 | 0 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 232 | REROLL | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 233 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 12.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2706548571586609 | 0.0 | 0.0 | +— / -eecc4b9d-82ef-4c04-ba8d-b299fcec55ed |
| Jogador 5 | 2-6 | 234 | BUY | STABILIZE | 100.0 | 5 | 1 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16923226416110992 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 5 | 2-6 | 235 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 12.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 243 | SELL | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3610999882221222 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 5 | 2-7 | 244 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6559984683990479 | 0.0 | 0.0 | +69ccc61a-403b-4025-8359-b2061dc6ad10 / -— |
| Jogador 5 | 2-7 | 245 | REROLL | STABILIZE | 100.0 | 5 | 8 | 0 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 246 | SELL | STABILIZE | 100.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2699250876903534 | 0.0 | 0.0 | +— / -69ccc61a-403b-4025-8359-b2061dc6ad10 |
| Jogador 5 | 2-7 | 247 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9438833594322205 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -d71a866d-0c5a-41c2-9996-0e179f062aa2,d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 5 | 2-7 | 248 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9380121231079102 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -9c93476e-a7be-457d-8543-8802507a8d3f,fb186a97-59a4-4b3a-be2f-dadd2670dc95 |
| Jogador 5 | 2-7 | 249 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.629672110080719 | 0.0 | 0.0 | +9b509d0e-ae62-4bfa-a551-f46ea68c64f4 / -— |
| Jogador 5 | 2-7 | 250 | REROLL | STABILIZE | 100.0 | 5 | 4 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 251 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 10.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33019858598709106 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 252 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 12.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5618991851806641 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 253 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 262 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2877202033996582 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 5 | 3-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2292184829711914 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 264 | REROLL | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 265 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005018261261284351 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 5 | 3-1 | 266 | REROLL | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 267 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3305962085723877 | 0.0 | 0.0 | +— / -bd0feb3d-9ff5-4678-862f-202b3bf74d5c |
| Jogador 5 | 3-1 | 268 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879818379878998 | 0.0 | 0.0 | +16acc555-c819-4f7c-b406-2f48f11ffc87 / -— |
| Jogador 5 | 3-1 | 269 | SELL | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23703600466251373 | 0.0 | 0.0 | +— / -0d693604-37ed-4f64-9a87-ded68f8a2dea |
| Jogador 5 | 3-1 | 270 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6881493926048279 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 5 | 3-1 | 271 | REROLL | STABILIZE | 100.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 272 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 282 | SELL | STABILIZE | 91.0 | 5 | 8 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3610999882221222 | 0.0 | 0.0 | +— / -16acc555-c819-4f7c-b406-2f48f11ffc87 |
| Jogador 5 | 3-2 | 283 | BUY | STABILIZE | 91.0 | 5 | 9 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.262093722820282 | 0.0 | 0.0 | +cc9b5fff-2223-4721-a8b2-4f70e196b851 / -— |
| Jogador 5 | 3-2 | 284 | REROLL | STABILIZE | 91.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 285 | REROLL | STABILIZE | 91.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 286 | SELL | STABILIZE | 91.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26990753412246704 | 0.0 | 0.0 | +— / -9b509d0e-ae62-4bfa-a551-f46ea68c64f4 |
| Jogador 5 | 3-2 | 287 | BUY | STABILIZE | 91.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7813675403594971 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 5 | 3-2 | 288 | SELL | STABILIZE | 91.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19308091700077057 | 0.0 | 0.0 | +— / -090f2ba6-5514-49ba-a80d-a0711cd06245 |
| Jogador 5 | 3-2 | 289 | BUY | STABILIZE | 91.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879825532436371 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 5 | 3-2 | 290 | REROLL | STABILIZE | 91.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 291 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014165130443871021 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 292 | PASS | STABILIZE | 91.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 302 | SELL | STABILIZE | 81.0 | 5 | 6 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3610999882221222 | 0.0 | 0.0 | +— / -ded275a3-9551-4816-8112-f0a25524412c |
| Jogador 5 | 3-3 | 303 | BUY | STABILIZE | 81.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2789236009120941 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 5 | 3-3 | 304 | REROLL | STABILIZE | 81.0 | 5 | 6 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 305 | SELL | STABILIZE | 81.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19308286905288696 | 0.0 | 0.0 | +— / -aaebedb3-18bf-4ae6-948e-7b326b573f1c |
| Jogador 5 | 3-3 | 306 | BUY | STABILIZE | 81.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5645813345909119 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 5 | 3-3 | 307 | REROLL | STABILIZE | 81.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 308 | SELL | STABILIZE | 81.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2698593735694885 | 0.0 | 0.0 | +— / -d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 5 | 3-3 | 309 | BUY | STABILIZE | 81.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8254020810127258 | 0.0 | 0.0 | +e9bb05f6-3838-423a-bfd2-3791379b479e / -a11208a9-96bf-468e-ab92-2ead6308be26,cc9b5fff-2223-4721-a8b2-4f70e196b851 |
| Jogador 5 | 3-3 | 310 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0003468239738140255 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 311 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015004838816821575 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 312 | PASS | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 316 | BUY | STABILIZE | 81.0 | 5 | 7 | 0 | 14.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8035053014755249 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 5 | 3-4 | 317 | BUY | STABILIZE | 81.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879825532436371 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 5 | 3-4 | 318 | REROLL | STABILIZE | 81.0 | 5 | 3 | 0 | 14.0 | Colosso/DA_18_Rakan | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 319 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00012463385064620525 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 320 | SELL | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2803761661052704 | 0.0 | 0.0 | +— / -e9bb05f6-3838-423a-bfd2-3791379b479e |
| Jogador 5 | 3-4 | 321 | REROLL | STABILIZE | 81.0 | 5 | 6 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 322 | BUY | STABILIZE | 81.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8027774691581726 | 0.0 | 0.0 | +d79de824-d9b2-4dfb-a7be-a359b416aea1 / -— |
| Jogador 5 | 3-4 | 323 | SELL | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3610999882221222 | 0.0 | 0.0 | +— / -3faf4ab2-44b3-4779-985b-658c64791c28 |
| Jogador 5 | 3-4 | 324 | BUY | STABILIZE | 81.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7801298499107361 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -235510e3-df54-4de9-9bcf-bff6d47e364a,d8ecc66e-097d-4caa-a657-90fcd1286c2b |
| Jogador 5 | 3-4 | 325 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.7646804053583764e-06 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 326 | PASS | STABILIZE | 81.0 | 5 | 0 | 0 | 14.0 | Colosso/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 332 | BUY | STABILIZE | 81.0 | 5 | 5 | 0 | 14.0 | Colosso/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6465750336647034 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -— |
| Jogador 5 | 3-5 | 333 | REROLL | STABILIZE | 81.0 | 5 | 4 | 0 | 14.0 | Colosso/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 334 | BUY | STABILIZE | 81.0 | 5 | 2 | 0 | 14.0 | Colosso/DA_18_Kayle | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2773633897304535 | 0.0 | 0.0 | +7904ab26-de3f-4144-b70f-ed620b41c907 / -— |
| Jogador 5 | 3-5 | 335 | MOVE_BENCH | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09911742806434631 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 336 | MOVE_BENCH | STABILIZE | 81.0 | 5 | 1 | 0 | 16.0 | Colosso/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4148481786251068 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 337 | MOVE_BENCH | STABILIZE | 81.0 | 5 | 1 | 0 | 18.0 | Colosso/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30493131279945374 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 338 | PASS | STABILIZE | 81.0 | 5 | 1 | 0 | 14.0 | Colosso/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 347 | SELL | STABILIZE | 70.0 | 5 | 6 | 0 | 14.0 | Colosso/DA_18_Kayle | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15571600198745728 | 0.0 | 0.0 | +— / -aa803972-8af8-46d7-b430-079819730c36 |
| Jogador 5 | 3-6 | 348 | BUY | STABILIZE | 70.0 | 5 | 11 | 1 | 14.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379880785942078 | 0.0 | 0.0 | +c5f81113-0e4a-4d08-beab-f19d808ef10c / -1e0a3ead-540d-4169-a1fc-3e79592564a0,f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 3-6 | 349 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 10 | 1 | 10.0 | Colosso/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21291007101535797 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 350 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 10 | 1 | 16.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5660501718521118 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 351 | BUY | STABILIZE | 70.0 | 5 | 10 | 1 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6942010521888733 | 0.0 | 0.0 | +e0035f8b-bf6a-4d55-b814-ff11e3c25750 / -— |
| Jogador 5 | 3-6 | 352 | REROLL | STABILIZE | 70.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 353 | BUY | STABILIZE | 70.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8315344452857971 | 0.0 | 0.0 | +23181987-d0b2-4e8c-a1a7-48a1e28179f7 / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,d79de824-d9b2-4dfb-a7be-a359b416aea1 |
| Jogador 5 | 3-6 | 354 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 4 | 0 | 16.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7224700450897217 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 355 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 4 | 0 | 12.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.518371045589447 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 356 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 4 | 0 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08410972356796265 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 357 | PASS | STABILIZE | 70.0 | 5 | 4 | 0 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 362 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 10 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39638960361480713 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 363 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 364 | PASS | STABILIZE | 70.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 376 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 5 | 16 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12150540202856064 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 377 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 5 | 16 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2543240189552307 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 378 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 16 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0911058858036995 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 379 | REROLL | STABILIZE | 70.0 | 5 | 16 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 380 | BUY | STABILIZE | 70.0 | 5 | 14 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8280158042907715 | 0.0 | 0.0 | +aabb68a2-aa23-402a-a8ca-36ef9f9f6f3e / -5a16a58c-7001-4448-8ca5-6293f35e2c94,ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b |
| Jogador 5 | 4-1 | 381 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 12 | 1 | 18.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40530815720558167 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 382 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 12 | 1 | 14.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 383 | MOVE_BENCH | STABILIZE | 70.0 | 5 | 12 | 1 | 14.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5204039812088013 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 384 | PASS | STABILIZE | 70.0 | 5 | 12 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 388 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 18 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09368904680013657 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 389 | MOVE_BENCH | FAST8 | 59.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4110081195831299 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 390 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 18 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 391 | PASS | STABILIZE | 59.0 | 6 | 18 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1071428582072258 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 397 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 18 | 1 | 22.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5918490290641785 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 402 | BUY | FAST8 | 47.0 | 6 | 25 | 2 | 34.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7113192081451416 | 0.0 | 0.0 | +01b2472f-5f9d-44e3-8c9a-05f7be8acba0 / -02c39b42-90d5-4e01-9380-460b6c1cb993,c3596d89-03d2-4fc7-afaf-591f10423252 |
| Jogador 5 | 4-3 | 403 | MOVE_BENCH | FAST8 | 47.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 404 | MOVE_BENCH | FAST8 | 47.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07581380754709244 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 405 | MOVE_BENCH | FAST8 | 47.0 | 6 | 24 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40757691860198975 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 406 | MOVE_BENCH | FAST8 | 47.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 407 | PASS | FAST8 | 47.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11142857372760773 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 411 | MOVE_BENCH | FAST8 | 47.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_Vi18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40260034799575806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 413 | BUY | STABILIZE | 35.0 | 6 | 32 | 3 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31590133905410767 | 0.0 | 0.0 | +9506d09a-fe30-43ab-adf8-da602402512c / -— |
| Jogador 5 | 4-4 | 414 | BUY | STABILIZE | 35.0 | 6 | 30 | 3 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7684062719345093 | 0.0 | 0.0 | +f286569d-fde3-4b8e-b5d7-3949c0990dd2 / -— |
| Jogador 5 | 4-4 | 415 | REROLL | STABILIZE | 35.0 | 6 | 28 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 416 | REROLL | STABILIZE | 35.0 | 6 | 26 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 417 | BUY | STABILIZE | 35.0 | 6 | 24 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8786936402320862 | 0.0 | 0.0 | +25e7949c-4a66-434d-b5f6-f85cfa009977 / -9506d09a-fe30-43ab-adf8-da602402512c,f286569d-fde3-4b8e-b5d7-3949c0990dd2 |
| Jogador 5 | 4-4 | 418 | REROLL | STABILIZE | 35.0 | 6 | 22 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 419 | REROLL | STABILIZE | 35.0 | 6 | 20 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23399999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 420 | REROLL | STABILIZE | 35.0 | 6 | 18 | 1 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 421 | REROLL | STABILIZE | 35.0 | 6 | 16 | 1 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 423 | REROLL | STABILIZE | 35.0 | 6 | 21 | 2 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23399999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 424 | REROLL | STABILIZE | 35.0 | 6 | 19 | 1 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 425 | REROLL | STABILIZE | 35.0 | 6 | 17 | 1 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 426 | BUY | STABILIZE | 35.0 | 6 | 15 | 1 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8638849854469299 | 0.0 | 0.0 | +ec6e37dd-4da6-470d-974a-ac4cd8f475db / -c3f8419e-a450-4247-bb65-8de8dba1c8ee,f2dbe099-e518-4261-b120-9f327b112dcb |
| Jogador 5 | 4-5 | 427 | MOVE_BENCH | STABILIZE | 35.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05701635405421257 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 428 | MOVE_BENCH | STABILIZE | 35.0 | 6 | 12 | 1 | 32.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39502474665641785 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 429 | REROLL | STABILIZE | 35.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 430 | MOVE_BOARD | STABILIZE | 35.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004698591772466898 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 431 | MOVE_BENCH | STABILIZE | 35.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041340284049510956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 432 | BUY | STABILIZE | 35.0 | 6 | 10 | 1 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.783313512802124 | 0.0 | 0.0 | +e83877c6-9f89-4d78-a054-041d2c834a2e / -7904ab26-de3f-4144-b70f-ed620b41c907,e0035f8b-bf6a-4d55-b814-ff11e3c25750 |
| Jogador 5 | 4-6 | 434 | REROLL | STABILIZE | 35.0 | 6 | 16 | 1 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 435 | BUY | STABILIZE | 35.0 | 6 | 14 | 1 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29912009835243225 | 0.0 | 0.0 | +62fab04b-8481-4cb4-ab50-c95f2832c040 / -— |
| Jogador 5 | 4-6 | 436 | REROLL | STABILIZE | 35.0 | 6 | 12 | 1 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 437 | BUY | STABILIZE | 35.0 | 6 | 10 | 1 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22583477199077606 | 0.0 | 0.0 | +789b9568-52f9-4b36-8878-041a1df030ec / -— |
| Jogador 5 | 4-6 | 438 | REROLL | STABILIZE | 35.0 | 6 | 9 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 439 | REROLL | STABILIZE | 35.0 | 6 | 7 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 440 | BUY | STABILIZE | 35.0 | 6 | 5 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8054330945014954 | 0.0 | 0.0 | +71e674f6-b2f0-461b-92a7-ec42176238ab / -— |
| Jogador 5 | 4-6 | 441 | REROLL | STABILIZE | 35.0 | 6 | 4 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 442 | REROLL | STABILIZE | 35.0 | 6 | 2 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 443 | MOVE_BOARD | STABILIZE | 35.0 | 6 | 0 | 0 | 40.0 | Colosso/DA_18_Azir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 445 | REROLL | STABILIZE | 35.0 | 6 | 7 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 446 | BUY | STABILIZE | 35.0 | 6 | 5 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28392305970191956 | 0.0 | 0.0 | +270bd445-51fa-4bcb-961f-92e1830e478d / -— |
| Jogador 5 | 4-7 | 447 | REROLL | STABILIZE | 35.0 | 6 | 2 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 448 | MOVE_BOARD | STABILIZE | 35.0 | 6 | 0 | 0 | 40.0 | Colosso/DA_18_Azir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 449 | MOVE_BOARD | STABILIZE | 35.0 | 6 | 0 | 0 | 40.0 | Colosso/DA_18_Azir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015015305019915104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 450 | PASS | STABILIZE | 35.0 | 6 | 0 | 0 | 40.0 | Colosso/DA_18_Azir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 455 | CRAFT_AND_EQUIP | STABILIZE | 35.0 | 6 | 6 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.16491328179836273 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 456 | CRAFT_AND_EQUIP | STABILIZE | 35.0 | 6 | 6 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11254727095365524 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 457 | REROLL | STABILIZE | 35.0 | 6 | 6 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 458 | BUY | STABILIZE | 35.0 | 6 | 4 | 0 | 40.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8039175868034363 | 0.0 | 0.0 | +ee9bb800-6ea3-44f4-8c77-054a433c9d2e / -— |
| Jogador 5 | 5-1 | 459 | MOVE_BOARD | STABILIZE | 35.0 | 6 | 1 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00011607231863308698 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 460 | MOVE_BOARD | STABILIZE | 35.0 | 6 | 1 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 461 | MOVE_BOARD | STABILIZE | 35.0 | 6 | 1 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 462 | PASS | STABILIZE | 35.0 | 6 | 1 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 465 | BUY | STABILIZE | 21.0 | 6 | 6 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7900205254554749 | 0.0 | 0.0 | +bad9ed1f-ca04-40ea-b621-b4ed9c1d1ea4 / -— |
| Jogador 5 | 5-2 | 466 | REROLL | STABILIZE | 21.0 | 6 | 4 | 0 | 40.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 467 | REROLL | STABILIZE | 21.0 | 6 | 2 | 0 | 40.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 468 | MOVE_BOARD | STABILIZE | 21.0 | 6 | 0 | 0 | 40.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 3.8279398722806945e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 469 | MOVE_BOARD | STABILIZE | 21.0 | 6 | 0 | 0 | 40.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 470 | SELL | STABILIZE | 21.0 | 6 | 0 | 0 | 40.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2500612139701843 | 0.0 | 0.0 | +— / -e83877c6-9f89-4d78-a054-041d2c834a2e |
| Jogador 5 | 5-2 | 471 | BUY | STABILIZE | 21.0 | 6 | 3 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2854187488555908 | 0.0 | 0.0 | +ff263c61-d416-4ed7-b4f3-386f736a160a / -— |
| Jogador 5 | 5-2 | 472 | MOVE_BOARD | STABILIZE | 21.0 | 6 | 1 | 0 | 40.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0009104203782044351 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 473 | MOVE_BOARD | STABILIZE | 21.0 | 6 | 1 | 0 | 40.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 475 | SELL | ALL_IN | 8.0 | 6 | 7 | 0 | 40.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2456156462430954 | 0.0 | 0.0 | +— / -ec6e37dd-4da6-470d-974a-ac4cd8f475db |
| Jogador 5 | 5-3 | 476 | BUY | ALL_IN | 8.0 | 6 | 15 | 1 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.795113742351532 | 0.0 | 0.0 | +62605065-c1fd-4bb3-ac4f-9fe0b6d247b4 / -— |
| Jogador 5 | 5-3 | 477 | SELL | ALL_IN | 8.0 | 6 | 13 | 1 | 40.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3609539568424225 | 0.0 | 0.0 | +— / -c5f81113-0e4a-4d08-beab-f19d808ef10c |
| Jogador 5 | 5-3 | 478 | BUY | ALL_IN | 8.0 | 6 | 16 | 1 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2778662443161011 | 0.0 | 0.0 | +65331a52-536c-4633-a5f2-759df2bd9a26 / -— |
| Jogador 5 | 5-3 | 479 | REROLL | ALL_IN | 8.0 | 6 | 15 | 1 | 40.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 480 | SELL | ALL_IN | 8.0 | 6 | 13 | 1 | 40.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26294681429862976 | 0.0 | 0.0 | +— / -ff263c61-d416-4ed7-b4f3-386f736a160a |
| Jogador 5 | 5-3 | 481 | BUY | ALL_IN | 8.0 | 6 | 15 | 1 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.818374752998352 | 0.0 | 0.0 | +95837027-9de8-4bac-a128-82bb3b7cc5bf / -62fab04b-8481-4cb4-ab50-c95f2832c040,bad9ed1f-ca04-40ea-b621-b4ed9c1d1ea4 |
| Jogador 5 | 5-3 | 482 | BUY | ALL_IN | 8.0 | 6 | 13 | 1 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8220580220222473 | 0.0 | 0.0 | +03433d41-2e04-44ba-83da-28d6fd544572 / -71e674f6-b2f0-461b-92a7-ec42176238ab,789b9568-52f9-4b36-8878-041a1df030ec |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.17109805345535278 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Sentry | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Sentry | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1729409396648407 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2306041121482849 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.036346435546875 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43516117334365845 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1968972384929657 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3494877517223358 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 38 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49431124329566956 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.19229832291603088 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.337342232465744 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0006781816482544 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.294776976108551 | 0.0 | 0.0 | +72aa8420-8dc2-4e9b-a10a-bd2a36f26656 / -— |
| Jogador 6 | 1-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20477211475372314 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 89 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026558782905340195 | 0.0 | 0.0 | +4fe99bfe-6eaa-4a36-b06e-60005fb92d30 / -— |
| Jogador 6 | 1-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013809510273858905 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 91 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019866235554218292 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 92 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3433563709259033 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8939233422279358 | 0.0 | 0.0 | +97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 / -— |
| Jogador 6 | 2-1 | 115 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.27666744589805603 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 116 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8864228129386902 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 117 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2132621556520462 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 118 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20137006044387817 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40861377120018005 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 120 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02389252930879593 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 121 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3817695677280426 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 122 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 139 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5229439735412598 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 6 | 2-2 | 140 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39918872714042664 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 141 | REROLL | STABILIZE | 96.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 142 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8810821175575256 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 6 | 2-2 | 143 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3315213918685913 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 2-2 | 144 | REROLL | STABILIZE | 96.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 145 | SELL | STABILIZE | 96.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49769356846809387 | 0.0 | 0.0 | +— / -97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 |
| Jogador 6 | 2-2 | 146 | BUY | STABILIZE | 96.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9462426900863647 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -185ee377-0917-4209-905b-9486d5be0193,646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-2 | 147 | SELL | STABILIZE | 96.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2887200117111206 | 0.0 | 0.0 | +— / -2a2066ee-841b-49d5-8b82-1d47feb36d8c |
| Jogador 6 | 2-2 | 148 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9188879132270813 | 0.0 | 0.0 | +669a8da1-dcc8-403b-a7af-7c96abdc464d / -— |
| Jogador 6 | 2-2 | 149 | PASS | STABILIZE | 96.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 162 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0478850603103638 | 0.0 | 0.0 | +2892a7ad-b390-4e82-9aa5-6e15828881f4 / -425b1e77-5887-40b3-875e-c1f60dc6c513,908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-3 | 163 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 7 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09926324337720871 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 164 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15071910619735718 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 165 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0423656702041626 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -4fe99bfe-6eaa-4a36-b06e-60005fb92d30,e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 6 | 2-3 | 166 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7181041836738586 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 167 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3857952654361725 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 168 | REROLL | STABILIZE | 96.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 169 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35114675760269165 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 6 | 2-3 | 170 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037686172872781754 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 171 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.53522127866745 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 172 | PASS | STABILIZE | 96.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 183 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9757078886032104 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -— |
| Jogador 6 | 2-4 | 184 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9761934876441956 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -669a8da1-dcc8-403b-a7af-7c96abdc464d,72aa8420-8dc2-4e9b-a10a-bd2a36f26656 |
| Jogador 6 | 2-4 | 185 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002996184164658189 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 186 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018803061917424202 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 187 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2503775954246521 | 0.0 | 0.0 | +acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce / -— |
| Jogador 6 | 2-4 | 188 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032221779227256775 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 189 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2850748598575592 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 190 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019207751378417015 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 191 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 192 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.370617151260376 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 193 | PASS | STABILIZE | 96.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 205 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36041730642318726 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 6 | 2-5 | 206 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 16.0 | Emanador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2915591895580292 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 6 | 2-5 | 207 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 4 | 0 | 16.0 | Emanador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09231410920619965 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 208 | REROLL | STABILIZE | 96.0 | 4 | 4 | 0 | 20.0 | Emanador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 209 | BUY | STABILIZE | 96.0 | 4 | 2 | 0 | 20.0 | Emanador/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8994251489639282 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 6 | 2-5 | 210 | BUY | STABILIZE | 96.0 | 4 | 1 | 0 | 20.0 | Emanador/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8976799845695496 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 6 | 2-5 | 211 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 0 | 0 | 20.0 | Emanador/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39650657773017883 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 212 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 0 | 0 | 18.0 | Emanador/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04938734322786331 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 213 | SELL | STABILIZE | 96.0 | 4 | 0 | 0 | 20.0 | Emanador/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018880000337958336 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 6 | 2-5 | 214 | REROLL | STABILIZE | 96.0 | 4 | 3 | 0 | 20.0 | Emanador/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 215 | PASS | STABILIZE | 96.0 | 4 | 1 | 0 | 20.0 | Emanador/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 225 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 8 | 0 | 20.0 | Emanador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41823530197143555 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 226 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 22.0 | Emanador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5089150667190552 | 0.0 | 0.0 | +7e545d27-1847-4016-b42b-e7db1960ae89 / -— |
| Jogador 6 | 2-6 | 227 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 5 | 0 | 22.0 | Emanador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.385789692401886 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 228 | REROLL | STABILIZE | 96.0 | 5 | 5 | 0 | 26.0 | Emanador/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 229 | BUY | STABILIZE | 96.0 | 5 | 3 | 0 | 26.0 | Emanador/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9473474025726318 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -3ffefe44-52ff-4118-83fb-ae8237b6caa0,c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 2-6 | 230 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 1 | 0 | 22.0 | Emanador/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5826569199562073 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 231 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 1 | 0 | 24.0 | Emanador/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08024270087480545 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 232 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 1 | 0 | 24.0 | Emanador/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17148643732070923 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 233 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 1 | 0 | 24.0 | Emanador/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 234 | PASS | STABILIZE | 96.0 | 5 | 1 | 0 | 24.0 | Emanador/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 243 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 24.0 | Emanador/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9496473073959351 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -3ad41699-a484-4178-be10-d8f72dfd1f35,e658854d-c531-46fc-8978-067953930510 |
| Jogador 6 | 2-7 | 244 | REROLL | STABILIZE | 96.0 | 5 | 7 | 0 | 22.0 | Emanador/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 245 | BUY | STABILIZE | 96.0 | 5 | 5 | 0 | 22.0 | Emanador/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33452922105789185 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 6 | 2-7 | 246 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 4 | 0 | 22.0 | Emanador/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22674044966697693 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 247 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 4 | 0 | 20.0 | Emanador/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5816323161125183 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 248 | BUY | STABILIZE | 96.0 | 5 | 4 | 0 | 26.0 | Emanador/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32864412665367126 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 6 | 2-7 | 249 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 0 | 0 | 26.0 | Emanador/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2862250804901123 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 250 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 30.0 | Emanador/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2467299997806549 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 251 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 30.0 | Emanador/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014819510281085968 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 252 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 0 | 0 | 30.0 | Emanador/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015090188011527061 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 253 | PASS | STABILIZE | 96.0 | 5 | 0 | 0 | 30.0 | Emanador/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 262 | BUY | STABILIZE | 96.0 | 5 | 6 | 0 | 30.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19691209495067596 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 6 | 3-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 5 | 5 | 0 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.23561012744903564 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 264 | SELL | STABILIZE | 96.0 | 5 | 5 | 0 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18695884943008423 | 0.0 | 0.0 | +— / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff |
| Jogador 6 | 3-1 | 265 | BUY | STABILIZE | 96.0 | 5 | 8 | 0 | 30.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23266905546188354 | 0.0 | 0.0 | +9593a62e-442f-410a-8a0c-7d781e2487cc / -— |
| Jogador 6 | 3-1 | 266 | REROLL | STABILIZE | 96.0 | 5 | 7 | 0 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 267 | REROLL | STABILIZE | 96.0 | 5 | 5 | 0 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 268 | SELL | STABILIZE | 96.0 | 5 | 3 | 0 | 30.0 | Emanador/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32422178983688354 | 0.0 | 0.0 | +— / -b55260cd-3c6a-4cb8-99d0-b7c6471103ad |
| Jogador 6 | 3-1 | 269 | BUY | STABILIZE | 96.0 | 5 | 6 | 0 | 30.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8021110892295837 | 0.0 | 0.0 | +2e4c09f7-35e9-41f6-9570-45e67a1d8eaf / -— |
| Jogador 6 | 3-1 | 270 | REROLL | STABILIZE | 96.0 | 5 | 5 | 0 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 271 | SELL | STABILIZE | 96.0 | 5 | 3 | 0 | 30.0 | Emanador/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34077200293540955 | 0.0 | 0.0 | +— / -4af85188-f11e-4aca-8165-ba8e7f535670 |
| Jogador 6 | 3-1 | 272 | PASS | STABILIZE | 96.0 | 5 | 8 | 0 | 30.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 282 | BUY | STABILIZE | 96.0 | 5 | 16 | 1 | 30.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04415716975927353 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -— |
| Jogador 6 | 3-2 | 283 | REROLL | STABILIZE | 96.0 | 5 | 14 | 1 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 284 | SELL | STABILIZE | 96.0 | 5 | 12 | 1 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008805012330412865 | 0.0 | 0.0 | +— / -42cf45df-f7dd-418d-a241-d89e69523352 |
| Jogador 6 | 3-2 | 285 | BUY | STABILIZE | 96.0 | 5 | 14 | 1 | 30.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8071487545967102 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 6 | 3-2 | 286 | REROLL | STABILIZE | 96.0 | 5 | 13 | 1 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 287 | SELL | STABILIZE | 96.0 | 5 | 11 | 1 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2461400032043457 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 6 | 3-2 | 288 | BUY | STABILIZE | 96.0 | 5 | 12 | 1 | 30.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7539862394332886 | 0.0 | 0.0 | +772bccc4-15f4-4de2-95f8-82d0ed9a72d2 / -15893185-b1a5-4725-9e46-964e149ec287,2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 6 | 3-2 | 289 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 9 | 0 | 18.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3519628643989563 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 290 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 9 | 0 | 16.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18466290831565857 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 291 | REROLL | STABILIZE | 96.0 | 5 | 9 | 0 | 20.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 292 | PASS | STABILIZE | 96.0 | 5 | 7 | 0 | 20.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 302 | BUY | STABILIZE | 96.0 | 5 | 16 | 1 | 20.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4776436984539032 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -— |
| Jogador 6 | 3-3 | 303 | SELL | STABILIZE | 96.0 | 5 | 15 | 1 | 20.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28049999475479126 | 0.0 | 0.0 | +— / -772bccc4-15f4-4de2-95f8-82d0ed9a72d2 |
| Jogador 6 | 3-3 | 304 | EQUIP_FROM_INVENTORY | STABILIZE | 96.0 | 5 | 23 | 2 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1353493332862854 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 305 | BUY | STABILIZE | 96.0 | 5 | 23 | 2 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22709769010543823 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 6 | 3-3 | 306 | REROLL | STABILIZE | 96.0 | 5 | 20 | 2 | 20.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 307 | SELL | STABILIZE | 96.0 | 5 | 18 | 1 | 20.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007846618071198463 | 0.0 | 0.0 | +— / -9593a62e-442f-410a-8a0c-7d781e2487cc |
| Jogador 6 | 3-3 | 308 | BUY | STABILIZE | 96.0 | 5 | 19 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7976365685462952 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 6 | 3-3 | 309 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 17 | 1 | 20.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3997417092323303 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 310 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 17 | 1 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014590153470635414 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 311 | REROLL | STABILIZE | 96.0 | 5 | 17 | 1 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 312 | PASS | STABILIZE | 96.0 | 5 | 15 | 1 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0560000017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 316 | BUY | STABILIZE | 96.0 | 5 | 25 | 2 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2892155945301056 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -— |
| Jogador 6 | 3-4 | 317 | REROLL | STABILIZE | 96.0 | 5 | 24 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 318 | SELL | STABILIZE | 96.0 | 5 | 22 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28910112380981445 | 0.0 | 0.0 | +— / -8da82a9e-0746-43e1-81c3-fa22ec3bb863 |
| Jogador 6 | 3-4 | 319 | BUY | STABILIZE | 96.0 | 5 | 23 | 2 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2928112745285034 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 6 | 3-4 | 320 | REROLL | STABILIZE | 96.0 | 5 | 21 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 321 | SELL | STABILIZE | 96.0 | 5 | 19 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17641817033290863 | 0.0 | 0.0 | +— / -3880fbd9-322b-4375-b855-fbb779a0cb47 |
| Jogador 6 | 3-4 | 322 | BUY | STABILIZE | 96.0 | 5 | 20 | 2 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20925036072731018 | 0.0 | 0.0 | +b1d58916-6d8b-4071-a37d-a478395e6a1e / -— |
| Jogador 6 | 3-4 | 323 | REROLL | STABILIZE | 96.0 | 5 | 19 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 324 | REROLL | STABILIZE | 96.0 | 5 | 17 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 325 | REROLL | STABILIZE | 96.0 | 5 | 15 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 326 | PASS | STABILIZE | 96.0 | 5 | 13 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 332 | SELL | STABILIZE | 96.0 | 5 | 22 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2678622603416443 | 0.0 | 0.0 | +— / -b1d58916-6d8b-4071-a37d-a478395e6a1e |
| Jogador 6 | 3-5 | 333 | BUY | STABILIZE | 96.0 | 5 | 23 | 2 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2982301414012909 | 0.0 | 0.0 | +a960f5cb-d806-4d73-9146-244e1ecde6f2 / -— |
| Jogador 6 | 3-5 | 334 | REROLL | STABILIZE | 96.0 | 5 | 22 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 335 | SELL | STABILIZE | 96.0 | 5 | 20 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2708195149898529 | 0.0 | 0.0 | +— / -a960f5cb-d806-4d73-9146-244e1ecde6f2 |
| Jogador 6 | 3-5 | 336 | BUY | STABILIZE | 96.0 | 5 | 21 | 2 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.852780818939209 | 0.0 | 0.0 | +29c2eb81-6c39-41ff-96eb-a3b28d6e4b99 / -59f588eb-e3f3-4907-ab23-af073a26bd6a,a72137b3-498b-40e1-938a-639f56745f08 |
| Jogador 6 | 3-5 | 337 | BUY | STABILIZE | 96.0 | 5 | 20 | 2 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7722354531288147 | 0.0 | 0.0 | +12d02679-e950-433b-ad9e-679a89cf86d8 / -2e4c09f7-35e9-41f6-9570-45e67a1d8eaf,d9fdb961-a3e3-4e39-9970-e46ffd59fc3b |
| Jogador 6 | 3-5 | 338 | REROLL | STABILIZE | 96.0 | 5 | 19 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 339 | BUY | STABILIZE | 96.0 | 5 | 17 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8019904494285583 | 0.0 | 0.0 | +41cebf65-3d00-41d3-bc56-d1d126a6e261 / -— |
| Jogador 6 | 3-5 | 340 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 13 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5459240674972534 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 341 | REROLL | STABILIZE | 96.0 | 5 | 13 | 1 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 342 | PASS | STABILIZE | 96.0 | 5 | 11 | 1 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 347 | BUY | STABILIZE | 96.0 | 5 | 21 | 2 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2998173236846924 | 0.0 | 0.0 | +3acea3a8-5fa8-441c-85bc-59b2c30e9730 / -— |
| Jogador 6 | 3-6 | 348 | REROLL | STABILIZE | 96.0 | 5 | 20 | 2 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30399999022483826 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 349 | REROLL | STABILIZE | 96.0 | 5 | 18 | 1 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 350 | BUY | STABILIZE | 96.0 | 5 | 16 | 1 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079172968864441 | 0.0 | 0.0 | +77742642-57e8-4594-8bb9-5b2e80a86ba1 / -— |
| Jogador 6 | 3-6 | 351 | REROLL | STABILIZE | 96.0 | 5 | 15 | 1 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 352 | SELL | STABILIZE | 96.0 | 5 | 13 | 1 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37049999833106995 | 0.0 | 0.0 | +— / -29c2eb81-6c39-41ff-96eb-a3b28d6e4b99 |
| Jogador 6 | 3-6 | 353 | BUY | STABILIZE | 96.0 | 5 | 16 | 1 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.283937007188797 | 0.0 | 0.0 | +b3e5d552-7da1-42e6-9168-d054a829a1e9 / -— |
| Jogador 6 | 3-6 | 354 | REROLL | STABILIZE | 96.0 | 5 | 13 | 1 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 355 | SELL | STABILIZE | 96.0 | 5 | 11 | 1 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3200867772102356 | 0.0 | 0.0 | +— / -12d02679-e950-433b-ad9e-679a89cf86d8 |
| Jogador 6 | 3-6 | 356 | BUY | STABILIZE | 96.0 | 5 | 14 | 1 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8050089478492737 | 0.0 | 0.0 | +5268c681-31fe-4973-9d93-cd1413b64383 / -— |
| Jogador 6 | 3-6 | 357 | PASS | STABILIZE | 96.0 | 5 | 12 | 1 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 362 | SELL | STABILIZE | 96.0 | 5 | 22 | 2 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1495867520570755 | 0.0 | 0.0 | +— / -2f5d8cb8-8ba3-45e9-a345-00e931d34490 |
| Jogador 6 | 3-7 | 363 | BUY | STABILIZE | 96.0 | 5 | 25 | 2 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29097628593444824 | 0.0 | 0.0 | +ffb8808b-40c6-4268-8a8f-9c90095a59b6 / -— |
| Jogador 6 | 3-7 | 364 | REROLL | STABILIZE | 96.0 | 5 | 24 | 2 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 365 | SELL | STABILIZE | 96.0 | 5 | 22 | 2 | 24.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19985580444335938 | 0.0 | 0.0 | +— / -ffb8808b-40c6-4268-8a8f-9c90095a59b6 |
| Jogador 6 | 3-7 | 366 | BUY | STABILIZE | 96.0 | 5 | 23 | 2 | 24.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8505716919898987 | 0.0 | 0.0 | +22f5b2d1-9395-4a0a-9c44-b1dacd066c63 / -2d5214b0-3e0c-4e71-8664-2459bf616650,5268c681-31fe-4973-9d93-cd1413b64383 |
| Jogador 6 | 3-7 | 367 | BUY | STABILIZE | 96.0 | 5 | 21 | 2 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.852810800075531 | 0.0 | 0.0 | +e50e0ccc-eb5c-46e0-9049-d5c4d8ea471e / -3acea3a8-5fa8-441c-85bc-59b2c30e9730,77742642-57e8-4594-8bb9-5b2e80a86ba1 |
| Jogador 6 | 3-7 | 368 | REROLL | STABILIZE | 96.0 | 5 | 20 | 2 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 369 | BUY | STABILIZE | 96.0 | 5 | 18 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28791543841362 | 0.0 | 0.0 | +b8e39436-d35c-48a4-9382-4266bed6f0f1 / -— |
| Jogador 6 | 3-7 | 370 | REROLL | STABILIZE | 96.0 | 5 | 17 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 371 | BUY | STABILIZE | 96.0 | 5 | 15 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8331007361412048 | 0.0 | 0.0 | +44758e57-e66f-4728-96d0-af1fd04cc221 / -68b28241-1946-4304-8b10-ae24a13a8e60,a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 6 | 3-7 | 372 | PASS | STABILIZE | 96.0 | 5 | 13 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 376 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 5 | 22 | 2 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15038001537322998 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 377 | CRAFT_AND_EQUIP | STABILIZE | 96.0 | 5 | 22 | 2 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17341339588165283 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 378 | BUY | STABILIZE | 96.0 | 5 | 22 | 2 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1718100756406784 | 0.0 | 0.0 | +b5df9bf6-5601-488f-bdb3-2109875f255d / -— |
| Jogador 6 | 4-1 | 379 | REROLL | STABILIZE | 96.0 | 5 | 19 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 380 | BUY | STABILIZE | 96.0 | 5 | 17 | 1 | 20.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.803937554359436 | 0.0 | 0.0 | +2ea16654-a3ca-4b16-a4cd-989264343b5c / -— |
| Jogador 6 | 4-1 | 381 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 14 | 1 | 20.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6218917965888977 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 382 | BUY | STABILIZE | 96.0 | 5 | 14 | 1 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48171794414520264 | 0.0 | 0.0 | +f2b8bdda-c32d-4840-bfda-f25caf0c83fb / -— |
| Jogador 6 | 4-1 | 383 | REROLL | STABILIZE | 96.0 | 5 | 13 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 384 | SELL | STABILIZE | 96.0 | 5 | 11 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35161688923835754 | 0.0 | 0.0 | +— / -e50e0ccc-eb5c-46e0-9049-d5c4d8ea471e |
| Jogador 6 | 4-1 | 385 | BUY | STABILIZE | 96.0 | 5 | 14 | 1 | 22.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8077960014343262 | 0.0 | 0.0 | +a10be0a5-aca9-4c6f-bb3d-c98b5b99d431 / -— |
| Jogador 6 | 4-1 | 386 | PASS | STABILIZE | 96.0 | 5 | 13 | 1 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 388 | REROLL | STABILIZE | 96.0 | 6 | 23 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 389 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 21 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8191128373146057 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 390 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 21 | 2 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1740541309118271 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 391 | PASS | STABILIZE | 96.0 | 6 | 21 | 2 | 20.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029285714030265808 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 397 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 21 | 2 | 20.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1147538274526596 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 402 | MOVE_BOARD | FAST8 | 96.0 | 6 | 32 | 3 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003935793414711952 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 403 | MOVE_BOARD | FAST8 | 96.0 | 6 | 32 | 3 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08483704924583435 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 404 | MOVE_BOARD | FAST8 | 96.0 | 6 | 32 | 3 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21603450179100037 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 405 | MOVE_BOARD | FAST8 | 96.0 | 6 | 32 | 3 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015053646638989449 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 406 | MOVE_BOARD | FAST8 | 96.0 | 6 | 32 | 3 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 407 | PASS | FAST8 | 96.0 | 6 | 32 | 3 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17714285850524902 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 413 | BUY | FAST8 | 96.0 | 6 | 44 | 4 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8468517065048218 | 0.0 | 0.0 | +a9c196ea-e98e-44d7-addc-134e1cdc1c58 / -d6a929d8-6d7c-4bcd-880d-d819daca2ae0,f2b8bdda-c32d-4840-bfda-f25caf0c83fb |
| Jogador 6 | 4-4 | 414 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 43 | 4 | 22.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22779031097888947 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 415 | MOVE_BENCH | FAST8 | 96.0 | 6 | 43 | 4 | 26.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39757683873176575 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 416 | MOVE_BOARD | FAST8 | 96.0 | 6 | 43 | 4 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010723276063799858 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 417 | MOVE_BOARD | FAST8 | 96.0 | 6 | 43 | 4 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015057041309773922 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 418 | PASS | FAST8 | 96.0 | 6 | 43 | 4 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1850000023841858 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 423 | BUY | FAST8 | 96.0 | 6 | 55 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30145463347435 | 0.0 | 0.0 | +02daf8ea-6db2-4e17-ba25-53b01e4ad20a / -— |
| Jogador 6 | 4-5 | 424 | MOVE_BOARD | FAST8 | 96.0 | 6 | 53 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008891160599887371 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 425 | MOVE_BOARD | FAST8 | 96.0 | 6 | 53 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006073413882404566 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 426 | PASS | FAST8 | 96.0 | 6 | 53 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2215845137834549 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 434 | MOVE_BENCH | FAST8 | 83.0 | 6 | 63 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07765436917543411 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 435 | BUY_XP | FAST8 | 83.0 | 6 | 63 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016200000420212746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 436 | BUY_XP | FAST8 | 83.0 | 6 | 59 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016200000420212746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 437 | BUY_XP | FAST8 | 83.0 | 6 | 55 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016200000420212746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 438 | MOVE_BOARD | FAST8 | 83.0 | 6 | 51 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 439 | SELL | FAST8 | 83.0 | 6 | 51 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10762308537960052 | 0.0 | 0.0 | +— / -2892a7ad-b390-4e82-9aa5-6e15828881f4 |
| Jogador 6 | 4-6 | 440 | EQUIP_FROM_INVENTORY | FAST8 | 83.0 | 6 | 54 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07907115668058395 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 441 | EQUIP_FROM_INVENTORY | FAST8 | 83.0 | 6 | 54 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06660076975822449 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 442 | EQUIP_FROM_INVENTORY | FAST8 | 83.0 | 6 | 54 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10311135649681091 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 443 | BUY | FAST8 | 83.0 | 6 | 54 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2562078535556793 | 0.0 | 0.0 | +25e9ad31-6ad3-4715-8752-a138d7d45f42 / -— |
| Jogador 6 | 4-7 | 445 | BUY | FAST8 | 83.0 | 6 | 63 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8898302316665649 | 0.0 | 0.0 | +faf4e579-8c95-4fa0-bc1a-c2619c7fdb57 / -a10be0a5-aca9-4c6f-bb3d-c98b5b99d431,b8e39436-d35c-48a4-9382-4266bed6f0f1 |
| Jogador 6 | 4-7 | 446 | MOVE_BENCH | FAST8 | 83.0 | 6 | 62 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4696217179298401 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 447 | MOVE_BOARD | FAST8 | 83.0 | 6 | 62 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01824185624718666 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 448 | MOVE_BOARD | FAST8 | 83.0 | 6 | 62 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012795955874025822 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 449 | PASS | FAST8 | 83.0 | 6 | 62 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08728048950433731 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 455 | BUY | FAST8 | 83.0 | 6 | 72 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3069906234741211 | 0.0 | 0.0 | +478395b3-8de6-4599-90ea-f3315a0de63c / -— |
| Jogador 6 | 5-1 | 456 | CRAFT_AND_EQUIP | FAST8 | 83.0 | 6 | 70 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14823949337005615 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 457 | CRAFT_AND_EQUIP | FAST8 | 83.0 | 6 | 70 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13309358060359955 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 458 | MOVE_BENCH | FAST8 | 83.0 | 6 | 70 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38699066638946533 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 459 | MOVE_BENCH | FAST8 | 83.0 | 6 | 70 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.749627411365509 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 460 | PASS | FAST8 | 83.0 | 6 | 70 | 5 | 28.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2560470998287201 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 465 | BUY | FAST8 | 83.0 | 6 | 81 | 5 | 28.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8772101402282715 | 0.0 | 0.0 | +046c22f2-0efc-4829-9861-75984b2b3bc2 / -— |
| Jogador 6 | 5-2 | 466 | MOVE_BENCH | FAST8 | 83.0 | 6 | 79 | 5 | 28.0 | Emanador/DA_Murkwolf18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11898904293775558 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 467 | MOVE_BENCH | FAST8 | 83.0 | 6 | 79 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4002473056316376 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 468 | SELL | FAST8 | 83.0 | 6 | 79 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008080000057816505 | 0.0 | 0.0 | +— / -a9c196ea-e98e-44d7-addc-134e1cdc1c58 |
| Jogador 6 | 5-2 | 469 | EQUIP_FROM_INVENTORY | FAST8 | 83.0 | 6 | 82 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11663110554218292 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 470 | EQUIP_FROM_INVENTORY | FAST8 | 83.0 | 6 | 82 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10277444124221802 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 471 | BUY_XP | FAST8 | 83.0 | 6 | 82 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017999999225139618 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 472 | BUY_XP | FAST8 | 83.0 | 6 | 78 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017999999225139618 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 473 | MOVE_BOARD | FAST8 | 83.0 | 6 | 74 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 475 | BUY | FAST8 | 83.0 | 7 | 86 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37280914187431335 | 0.0 | 0.0 | +5328be02-308a-46b6-b7b4-0a2aa87c6e16 / -— |
| Jogador 6 | 5-3 | 476 | MOVE_BENCH | FAST8 | 83.0 | 7 | 85 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.593704879283905 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 477 | MOVE_BOARD | FAST8 | 83.0 | 7 | 85 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01702430658042431 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 478 | MOVE_BOARD | FAST8 | 83.0 | 7 | 85 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 479 | PASS | FAST8 | 83.0 | 7 | 85 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2679973244667053 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 484 | MOVE_BOARD | FAST8 | 83.0 | 7 | 96 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 485 | MOVE_BOARD | FAST8 | 83.0 | 7 | 96 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 486 | PASS | FAST8 | 83.0 | 7 | 96 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.277114599943161 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 494 | MOVE_BOARD | FAST8 | 83.0 | 7 | 107 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01661849394440651 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 495 | MOVE_BOARD | FAST8 | 83.0 | 7 | 107 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 496 | MOVE_BOARD | FAST8 | 83.0 | 7 | 107 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01470259204506874 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 497 | PASS | FAST8 | 83.0 | 7 | 107 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28645455837249756 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 503 | BUY | FAST8 | 83.0 | 7 | 119 | 5 | 36.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9497792720794678 | 0.0 | 0.0 | +c316c846-85b4-4436-b3d1-b3d96b0b68aa / -02daf8ea-6db2-4e17-ba25-53b01e4ad20a,046c22f2-0efc-4829-9861-75984b2b3bc2 |
| Jogador 6 | 5-6 | 504 | MOVE_BENCH | FAST8 | 83.0 | 7 | 117 | 5 | 32.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5992015600204468 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 505 | MOVE_BOARD | FAST8 | 83.0 | 7 | 117 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015178915113210678 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 506 | MOVE_BOARD | FAST8 | 83.0 | 7 | 117 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 507 | PASS | FAST8 | 83.0 | 7 | 117 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29510509967803955 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 512 | BUY | FAST8 | 83.0 | 7 | 128 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8239894509315491 | 0.0 | 0.0 | +5b26cffc-a739-41f1-acf8-d454592ff9a0 / -— |
| Jogador 6 | 5-7 | 513 | MOVE_BOARD | FAST8 | 83.0 | 7 | 127 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 514 | MOVE_BOARD | FAST8 | 83.0 | 7 | 127 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 515 | PASS | FAST8 | 83.0 | 7 | 127 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30388617515563965 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 522 | EQUIP_FROM_INVENTORY | FAST8 | 83.0 | 7 | 138 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.005105892196297646 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 523 | BUY | FAST8 | 83.0 | 7 | 138 | 5 | 40.0 | Emanador/DA_Murkwolf18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0099929571151733 | 0.0 | 0.0 | +5d3005e6-9b5a-46ed-abd3-491eca1b9229 / -41cebf65-3d00-41d3-bc56-d1d126a6e261,eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 6 | 6-1 | 524 | BUY | FAST8 | 83.0 | 7 | 134 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4044936001300812 | 0.0 | 0.0 | +094ccd16-3d5b-4054-ad80-e7cd9ab082e6 / -— |
| Jogador 6 | 6-1 | 525 | SELL | FAST8 | 83.0 | 7 | 132 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3265579044818878 | 0.0 | 0.0 | +— / -faf4e579-8c95-4fa0-bc1a-c2619c7fdb57 |
| Jogador 6 | 6-1 | 526 | BUY | FAST8 | 83.0 | 7 | 135 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33051756024360657 | 0.0 | 0.0 | +c0ef46f3-71f5-46eb-973b-964ab1da97f9 / -— |
| Jogador 6 | 6-1 | 527 | MOVE_BOARD | FAST8 | 83.0 | 7 | 134 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 528 | MOVE_BOARD | FAST8 | 83.0 | 7 | 134 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013443431816995144 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 529 | PASS | FAST8 | 83.0 | 7 | 134 | 5 | 32.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17029331624507904 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 532 | BUY | FAST8 | 83.0 | 7 | 145 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0099812746047974 | 0.0 | 0.0 | +8b4c2718-a172-40e3-a525-9b469fd7e778 / -2ea16654-a3ca-4b16-a4cd-989264343b5c,b3e5d552-7da1-42e6-9168-d054a829a1e9 |
| Jogador 6 | 6-2 | 533 | BUY | FAST8 | 83.0 | 7 | 142 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37620729207992554 | 0.0 | 0.0 | +a370a481-7e33-441f-b350-906b6d60ff13 / -— |
| Jogador 6 | 6-2 | 534 | MOVE_BENCH | FAST8 | 83.0 | 7 | 140 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09858502447605133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 535 | MOVE_BENCH | FAST8 | 83.0 | 7 | 140 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06085951253771782 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 536 | MOVE_BENCH | FAST8 | 83.0 | 7 | 140 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4135349988937378 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 537 | MOVE_BENCH | FAST8 | 83.0 | 7 | 140 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08374013751745224 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 538 | MOVE_BENCH | FAST8 | 83.0 | 7 | 140 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058756034821271896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 539 | MOVE_BENCH | FAST8 | 83.0 | 7 | 140 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09398684650659561 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 540 | MOVE_BENCH | FAST8 | 83.0 | 7 | 140 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 542 | BUY | FAST8 | 83.0 | 7 | 151 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3507198989391327 | 0.0 | 0.0 | +1dd1d3e0-59b9-4022-a28c-ffdcb56718cf / -— |
| Jogador 6 | 6-3 | 543 | MOVE_BENCH | FAST8 | 83.0 | 7 | 147 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3924143612384796 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 544 | MOVE_BENCH | FAST8 | 83.0 | 7 | 147 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08384189754724503 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 545 | MOVE_BENCH | FAST8 | 83.0 | 7 | 147 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 546 | MOVE_BENCH | FAST8 | 83.0 | 7 | 147 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4077838063240051 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 547 | PASS | FAST8 | 83.0 | 7 | 147 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1830344945192337 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 552 | MOVE_BENCH | FAST8 | 66.0 | 7 | 157 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09885187447071075 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 553 | MOVE_BENCH | FAST8 | 66.0 | 7 | 157 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06264206767082214 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 554 | MOVE_BENCH | FAST8 | 66.0 | 7 | 157 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10946567356586456 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 555 | MOVE_BENCH | FAST8 | 66.0 | 7 | 157 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.407771497964859 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 556 | PASS | FAST8 | 66.0 | 7 | 157 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19295376539230347 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 562 | MOVE_BENCH | FAST8 | 66.0 | 7 | 167 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09889165312051773 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 563 | MOVE_BENCH | FAST8 | 66.0 | 7 | 167 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1095050796866417 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 564 | MOVE_BENCH | FAST8 | 66.0 | 7 | 167 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40680238604545593 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 565 | PASS | FAST8 | 66.0 | 7 | 167 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20296630263328552 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 572 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40237241983413696 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 573 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08459991216659546 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 574 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060736335813999176 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 575 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4147714078426361 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 576 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 34.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08460543304681778 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 577 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07754890620708466 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 578 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8222375512123108 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 579 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 28.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14968478679656982 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 580 | MOVE_BENCH | FAST8 | 48.0 | 7 | 178 | 5 | 30.0 | Emanador/DA_Sentinel18 | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6224236488342285 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 582 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 189 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7348291873931885 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 583 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 189 | 5 | 28.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13477659225463867 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 584 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 189 | 5 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6372506618499756 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 585 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 189 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3144194185733795 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 586 | PASS | STABILIZE | 30.0 | 7 | 189 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2572881579399109 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 592 | EQUIP_FROM_INVENTORY | STABILIZE | 30.0 | 7 | 200 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 593 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09866886585950851 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 594 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.858533501625061 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 595 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 28.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11718453466892242 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 596 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08371549099683762 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 597 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8574321866035461 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 598 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 28.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13263694941997528 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 599 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0996067225933075 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 600 | MOVE_BENCH | STABILIZE | 30.0 | 7 | 200 | 5 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3918320834636688 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 602 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 211 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4038423001766205 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 603 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 211 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08459914475679398 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 604 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 211 | 5 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40670937299728394 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 605 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 211 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08453221619129181 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 606 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 211 | 5 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11500000208616257 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 607 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 211 | 5 | 30.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6247385144233704 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 608 | PASS | ALL_IN | 6.0 | 7 | 211 | 5 | 34.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38116759061813354 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8564506769180298 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6253763437271118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.18626636266708374 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37212279438972473 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10107407718896866 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3430940806865692 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0468392372131348 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 60 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2346935123205185 | 0.0 | 0.0 | +7159421f-b5ea-4d10-9cc5-59186d62983d / -— |
| Jogador 7 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00704618263989687 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021817119792103767 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019780343398451805 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22881516814231873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 65 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0217559337615967 | 0.0 | 0.0 | +d4c65b41-a22a-4d60-8a70-547d539e4903 / -— |
| Jogador 7 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18416021764278412 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 88 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04944236949086189 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.279008150100708 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 91 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015239769592881203 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 92 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3495708405971527 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9582158327102661 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 7 | 2-1 | 115 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20799483358860016 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 116 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17574279010295868 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 117 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48649078607559204 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 118 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3144250214099884 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3613455593585968 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 120 | REROLL | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 121 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07860428839921951 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-1 | 122 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Shen | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0477631092071533 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-1 | 123 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5494773387908936 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 124 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 139 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.115282654762268 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -47ec6577-cbf2-4275-b185-c19256223441,d4c65b41-a22a-4d60-8a70-547d539e4903 |
| Jogador 7 | 2-2 | 140 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16034574806690216 | 0.0 | 0.0 | +475e5206-4f54-4bbb-9db9-99d1895f0887 / -— |
| Jogador 7 | 2-2 | 141 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37199893593788147 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 142 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6786926984786987 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 143 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 158 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6416621804237366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 162 | BUY | STABILIZE | 94.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3196322023868561 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 7 | 2-3 | 163 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08977275341749191 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 164 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 165 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12811073660850525 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 166 | PASS | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 183 | BUY | STABILIZE | 89.0 | 4 | 12 | 1 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3176994323730469 | 0.0 | 0.0 | +c96b6357-8134-4e68-af0b-f5695a815597 / -— |
| Jogador 7 | 2-4 | 184 | BUY | STABILIZE | 89.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14363974332809448 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 7 | 2-4 | 185 | REROLL | STABILIZE | 89.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 186 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8927668929100037 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 7 | 2-4 | 187 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8816893696784973 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 7 | 2-4 | 188 | REROLL | STABILIZE | 89.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 189 | BUY | STABILIZE | 89.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9442884922027588 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -46838f8d-8037-485c-8c34-9639f14ada19,5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-4 | 190 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3479384183883667 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 191 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5605226159095764 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 192 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16037416458129883 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 193 | PASS | STABILIZE | 89.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 205 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8789501786231995 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 7 | 2-5 | 206 | REROLL | STABILIZE | 89.0 | 4 | 5 | 0 | 10.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 207 | BUY | STABILIZE | 89.0 | 4 | 3 | 0 | 10.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499434232711792 | 0.0 | 0.0 | +655deca9-2d3f-4e88-827a-5f49da8f3451 / -4e206e09-40e3-4699-81cb-8aaf01109dea,837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 7 | 2-5 | 208 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1188683807849884 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 209 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 2 | 0 | 8.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47198185324668884 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 210 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 2 | 0 | 10.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02837003581225872 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 211 | BUY | STABILIZE | 89.0 | 4 | 2 | 0 | 10.0 | Colosso/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8925319314002991 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 7 | 2-5 | 212 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 0 | 0 | 10.0 | Colosso/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06784303486347198 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 213 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 0 | 0 | 10.0 | Colosso/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36859071254730225 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 214 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 0 | 0 | 12.0 | Colosso/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2581345736980438 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 215 | PASS | STABILIZE | 89.0 | 4 | 0 | 0 | 12.0 | Colosso/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 225 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 12.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9493423104286194 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -9204a42c-6310-4b08-9bc7-8a2e786b077a,c96b6357-8134-4e68-af0b-f5695a815597 |
| Jogador 7 | 2-6 | 226 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 5 | 0 | 10.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17422620952129364 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 227 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 5 | 0 | 8.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1431681364774704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 228 | PASS | STABILIZE | 85.0 | 5 | 5 | 0 | 10.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 241 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 5 | 0 | 10.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15777064859867096 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 243 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03065592609345913 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 244 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5571762919425964 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 245 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 11 | 1 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004887938033789396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 246 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 11 | 1 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019039023900404572 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 247 | PASS | STABILIZE | 78.0 | 5 | 11 | 1 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 262 | BUY | STABILIZE | 78.0 | 5 | 18 | 1 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7770867943763733 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 7 | 3-1 | 263 | CRAFT_AND_EQUIP | STABILIZE | 78.0 | 5 | 15 | 1 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11197704076766968 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 264 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 15 | 1 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4719676971435547 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 265 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 15 | 1 | 16.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3395749628543854 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 266 | PASS | STABILIZE | 78.0 | 5 | 15 | 1 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0560000017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 282 | BUY | STABILIZE | 68.0 | 5 | 23 | 2 | 18.0 | Colosso/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8420168161392212 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -081b684f-5d42-45c5-9a68-12127e5330a7,ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 7 | 3-2 | 283 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 20 | 2 | 12.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23218369483947754 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 284 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 20 | 2 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5404699444770813 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 285 | BUY | STABILIZE | 68.0 | 5 | 20 | 2 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1686881184577942 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 7 | 3-2 | 286 | MOVE_BOARD | STABILIZE | 68.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0065782759338617325 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 287 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.349673330783844 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 288 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 17 | 1 | 14.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14589354395866394 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 289 | MOVE_BOARD | STABILIZE | 68.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016669664531946182 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 290 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41314569115638733 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 291 | PASS | STABILIZE | 68.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05700000002980232 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 302 | BUY | STABILIZE | 58.0 | 5 | 26 | 2 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2921599745750427 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 7 | 3-3 | 303 | MOVE_BENCH | STABILIZE | 58.0 | 5 | 23 | 2 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6142262816429138 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 304 | REROLL | STABILIZE | 58.0 | 5 | 23 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 305 | BUY | STABILIZE | 58.0 | 5 | 21 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.77068692445755 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -4ac49c80-f0c3-47ae-a031-96928d244e13,6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 7 | 3-3 | 306 | MOVE_BENCH | STABILIZE | 58.0 | 5 | 19 | 1 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6776750683784485 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 307 | REROLL | STABILIZE | 58.0 | 5 | 19 | 1 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 308 | MOVE_BENCH | STABILIZE | 58.0 | 5 | 17 | 1 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 309 | MOVE_BENCH | STABILIZE | 58.0 | 5 | 17 | 1 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0742931216955185 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 310 | MOVE_BENCH | STABILIZE | 58.0 | 5 | 17 | 1 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35694554448127747 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 311 | BUY | STABILIZE | 58.0 | 5 | 17 | 1 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379191160202026 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -242805ca-f275-4e04-a2f5-81e0b6680dd1,7159421f-b5ea-4d10-9cc5-59186d62983d |
| Jogador 7 | 3-3 | 312 | PASS | STABILIZE | 58.0 | 5 | 16 | 1 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05649999901652336 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 316 | MOVE_BENCH | STABILIZE | 47.0 | 5 | 25 | 2 | 24.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.176698237657547 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 317 | MOVE_BENCH | STABILIZE | 47.0 | 5 | 25 | 2 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5134350061416626 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 318 | BUY | STABILIZE | 47.0 | 5 | 25 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3063157796859741 | 0.0 | 0.0 | +95a2e19e-619f-4497-ba52-e9bbf06b364f / -— |
| Jogador 7 | 3-4 | 319 | REROLL | STABILIZE | 47.0 | 5 | 24 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 320 | BUY | STABILIZE | 47.0 | 5 | 22 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3005095422267914 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 7 | 3-4 | 321 | REROLL | STABILIZE | 47.0 | 5 | 21 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30399999022483826 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 322 | BUY | STABILIZE | 47.0 | 5 | 19 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28732162714004517 | 0.0 | 0.0 | +a810e10d-e7ef-4ece-8fb2-8b6471b557ec / -— |
| Jogador 7 | 3-4 | 323 | REROLL | STABILIZE | 47.0 | 5 | 18 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 324 | SELL | STABILIZE | 47.0 | 5 | 16 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040248699486255646 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 7 | 3-4 | 325 | BUY | STABILIZE | 47.0 | 5 | 21 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8219435811042786 | 0.0 | 0.0 | +8c4772c9-83f1-4021-b83f-a9ff1773bea0 / -— |
| Jogador 7 | 3-4 | 326 | PASS | STABILIZE | 47.0 | 5 | 20 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 332 | REROLL | STABILIZE | 47.0 | 5 | 30 | 3 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 333 | REROLL | STABILIZE | 47.0 | 5 | 28 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 334 | MOVE_BENCH | STABILIZE | 47.0 | 5 | 26 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5512513518333435 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 335 | MOVE_BENCH | STABILIZE | 47.0 | 5 | 26 | 2 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11308871954679489 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 336 | SELL | STABILIZE | 47.0 | 5 | 26 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37049999833106995 | 0.0 | 0.0 | +— / -655deca9-2d3f-4e88-827a-5f49da8f3451 |
| Jogador 7 | 3-5 | 337 | EQUIP_FROM_INVENTORY | STABILIZE | 47.0 | 5 | 29 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.18015651404857635 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 338 | EQUIP_FROM_INVENTORY | STABILIZE | 47.0 | 5 | 29 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.15170766413211823 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 339 | MOVE_BOARD | STABILIZE | 47.0 | 5 | 29 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010150759044336155 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 340 | MOVE_BOARD | STABILIZE | 47.0 | 5 | 29 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007918531075119972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 341 | MOVE_BENCH | STABILIZE | 47.0 | 5 | 29 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41972559690475464 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 342 | PASS | STABILIZE | 47.0 | 5 | 29 | 2 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08049999922513962 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 347 | REROLL | STABILIZE | 37.0 | 5 | 39 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 348 | BUY | STABILIZE | 37.0 | 5 | 37 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8453119993209839 | 0.0 | 0.0 | +20ed6aae-dc87-406e-8bf9-a5afde4c9fef / -— |
| Jogador 7 | 3-6 | 349 | REROLL | STABILIZE | 37.0 | 5 | 36 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 350 | REROLL | STABILIZE | 37.0 | 5 | 34 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 351 | MOVE_BENCH | STABILIZE | 37.0 | 5 | 32 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10478272289037704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 352 | MOVE_BENCH | STABILIZE | 37.0 | 5 | 32 | 3 | 24.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7860840559005737 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 353 | MOVE_BENCH | STABILIZE | 37.0 | 5 | 32 | 3 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4168650805950165 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 354 | PASS | STABILIZE | 37.0 | 5 | 32 | 3 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033300742506980896 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 362 | MOVE_BENCH | STABILIZE | 27.0 | 5 | 43 | 4 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10833337903022766 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 363 | MOVE_BENCH | STABILIZE | 27.0 | 5 | 43 | 4 | 24.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7707297801971436 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 364 | MOVE_BENCH | STABILIZE | 27.0 | 5 | 43 | 4 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41205477714538574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 365 | PASS | STABILIZE | 27.0 | 5 | 43 | 4 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05389999970793724 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 376 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 5 | 55 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18210986256599426 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 377 | CRAFT_AND_EQUIP | STABILIZE | 27.0 | 5 | 55 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.204301655292511 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 378 | MOVE_BENCH | STABILIZE | 27.0 | 5 | 55 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5272440314292908 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 379 | MOVE_BENCH | STABILIZE | 27.0 | 5 | 55 | 5 | 26.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08909370005130768 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 380 | MOVE_BENCH | STABILIZE | 27.0 | 5 | 55 | 5 | 24.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4133637845516205 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 381 | SELL | STABILIZE | 27.0 | 5 | 55 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3239719867706299 | 0.0 | 0.0 | +— / -e270a6b1-23dd-49a0-8694-ba911eae4c71 |
| Jogador 7 | 4-1 | 382 | EQUIP_FROM_INVENTORY | STABILIZE | 27.0 | 5 | 60 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04939994961023331 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 383 | BUY | STABILIZE | 27.0 | 5 | 60 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.962165117263794 | 0.0 | 0.0 | +da4921b5-0ae7-4339-b38b-6ebce7412120 / -20ed6aae-dc87-406e-8bf9-a5afde4c9fef,5de51369-647a-45bd-95b7-c8efe44c5484 |
| Jogador 7 | 4-1 | 384 | REROLL | STABILIZE | 27.0 | 5 | 59 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 385 | REROLL | STABILIZE | 27.0 | 5 | 57 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15000000596046448 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 386 | PASS | STABILIZE | 27.0 | 5 | 55 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25477924942970276 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 388 | BUY | STABILIZE | 27.0 | 6 | 66 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8795590996742249 | 0.0 | 0.0 | +ef39d938-bee9-4290-95a4-da8a51088653 / -— |
| Jogador 7 | 4-2 | 389 | BUY | STABILIZE | 27.0 | 6 | 65 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4061374068260193 | 0.0 | 0.0 | +7a36288b-fe0f-43e2-a2c5-c8a3f30e1436 / -— |
| Jogador 7 | 4-2 | 390 | REROLL | STABILIZE | 27.0 | 6 | 64 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 391 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 62 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4009171426296234 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 392 | MOVE_BOARD | STABILIZE | 27.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014637526124715805 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 393 | MOVE_BOARD | STABILIZE | 27.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 394 | PASS | STABILIZE | 27.0 | 6 | 62 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2592805027961731 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 402 | BUY | STABILIZE | 16.0 | 6 | 72 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9717934727668762 | 0.0 | 0.0 | +f8a1bccf-2f23-4377-b654-0552c76639fd / -— |
| Jogador 7 | 4-3 | 403 | REROLL | STABILIZE | 16.0 | 6 | 71 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 404 | SELL | STABILIZE | 16.0 | 6 | 69 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5412750244140625 | 0.0 | 0.0 | +— / -da4921b5-0ae7-4339-b38b-6ebce7412120 |
| Jogador 7 | 4-3 | 405 | BUY | STABILIZE | 16.0 | 6 | 72 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0100836753845215 | 0.0 | 0.0 | +eea286a9-93b6-4a95-b879-d0f1e8a99f3a / -a810e10d-e7ef-4ece-8fb2-8b6471b557ec,ef39d938-bee9-4290-95a4-da8a51088653 |
| Jogador 7 | 4-3 | 406 | MOVE_BOARD | STABILIZE | 16.0 | 6 | 71 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0026801947969943285 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 407 | MOVE_BOARD | STABILIZE | 16.0 | 6 | 71 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015534752979874611 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 408 | PASS | STABILIZE | 16.0 | 6 | 71 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28502973914146423 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 413 | BUY | ALL_IN | 4.0 | 6 | 82 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5888974070549011 | 0.0 | 0.0 | +8a51f51f-2adf-456e-97ba-64751dd1e9f0 / -— |
| Jogador 7 | 4-4 | 414 | REROLL | ALL_IN | 4.0 | 6 | 81 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 415 | REROLL | ALL_IN | 4.0 | 6 | 79 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 416 | REROLL | ALL_IN | 4.0 | 6 | 77 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 417 | BUY | ALL_IN | 4.0 | 6 | 75 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0525310039520264 | 0.0 | 0.0 | +c6c2fdca-2733-4b1e-880d-effad905e56f / -7a36288b-fe0f-43e2-a2c5-c8a3f30e1436,f8a1bccf-2f23-4377-b654-0552c76639fd |
| Jogador 7 | 4-4 | 418 | BUY | ALL_IN | 4.0 | 6 | 74 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4444611370563507 | 0.0 | 0.0 | +5c681d97-9cf2-4aeb-bf8c-0c7e88b7ffec / -— |
| Jogador 7 | 4-4 | 419 | REROLL | ALL_IN | 4.0 | 6 | 73 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 420 | BUY | ALL_IN | 4.0 | 6 | 71 | 5 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9453891515731812 | 0.0 | 0.0 | +dab6bb13-2a01-483f-92ab-63535c16c9e7 / -475e5206-4f54-4bbb-9db9-99d1895f0887,8a51f51f-2adf-456e-97ba-64751dd1e9f0 |
| Jogador 7 | 4-4 | 421 | MOVE_BENCH | ALL_IN | 4.0 | 6 | 70 | 5 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44165268540382385 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 423 | BUY | ALL_IN | 4.0 | 6 | 81 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43466922640800476 | 0.0 | 0.0 | +637c4336-cd0a-4bc5-9d0f-2adde2705bcc / -— |
| Jogador 7 | 4-5 | 424 | REROLL | ALL_IN | 4.0 | 6 | 80 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 425 | BUY | ALL_IN | 4.0 | 6 | 78 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38446179032325745 | 0.0 | 0.0 | +d3ecdc3d-1c44-412a-b1bd-c46596ca8a5a / -— |
| Jogador 7 | 4-5 | 426 | REROLL | ALL_IN | 4.0 | 6 | 76 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 427 | REROLL | ALL_IN | 4.0 | 6 | 74 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 428 | SELL | ALL_IN | 4.0 | 6 | 72 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015279999934136868 | 0.0 | 0.0 | +— / -dab6bb13-2a01-483f-92ab-63535c16c9e7 |
| Jogador 7 | 4-5 | 429 | BUY | ALL_IN | 4.0 | 6 | 75 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.915803074836731 | 0.0 | 0.0 | +2a349876-34a5-43bb-9cf1-4012cb1a573e / -— |
| Jogador 7 | 4-5 | 430 | REROLL | ALL_IN | 4.0 | 6 | 72 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 431 | SELL | ALL_IN | 4.0 | 6 | 70 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4840663969516754 | 0.0 | 0.0 | +— / -eea286a9-93b6-4a95-b879-d0f1e8a99f3a |
| Jogador 7 | 4-5 | 432 | BUY | ALL_IN | 4.0 | 6 | 73 | 5 | 34.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9905549883842468 | 0.0 | 0.0 | +2ff482a2-5f9e-4f82-a8ba-56f793ef3aa5 / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.3500058054924011 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 31 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8621518015861511 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5632055997848511 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.11721326410770416 | 0.0 | 0.0 | +47feb452-27a0-43f6-983f-ea1674f17ab8 / -— |
| Jogador 8 | 1-2 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37383633852005005 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10667502135038376 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 37 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.339524507522583 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 59 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2866302728652954 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 60 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2942139208316803 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00693113449960947 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022274859249591827 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02103283256292343 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 64 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23976927995681763 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 66 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 86 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9870408773422241 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 87 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1148040294647217 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -4ea4d9af-5729-414b-a102-b7fc80667118,74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32853665947914124 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 89 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028838705271482468 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 90 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3159549832344055 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 91 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01560225896537304 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 92 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35690051317214966 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3963126242160797 | 0.0 | 0.0 | +f17723af-f50c-4679-b557-39f9b6b8d1b6 / -— |
| Jogador 8 | 2-1 | 115 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1697477549314499 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 116 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.40924108028411865 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 117 | CRAFT_AND_EQUIP | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10557100921869278 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 118 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3231411576271057 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12034495919942856 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 120 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009248298592865467 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 121 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06207816302776337 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 122 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Xayah | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 139 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9065101742744446 | 0.0 | 0.0 | +e98ea24f-414b-4ccd-a19a-d98965ccc21c / -— |
| Jogador 8 | 2-2 | 140 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26024216413497925 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 8 | 2-2 | 141 | REROLL | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 142 | SELL | STABILIZE | 95.0 | 4 | 0 | 0 | 10.0 | —/DA_18_Xayah | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2982408404350281 | 0.0 | 0.0 | +— / -322e9047-623a-4fec-a0f9-d21d2fbcd88a |
| Jogador 8 | 2-2 | 143 | BUY | STABILIZE | 95.0 | 4 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9814724922180176 | 0.0 | 0.0 | +01f4a73c-7202-4ee3-964e-d32370c3c547 / -— |
| Jogador 8 | 2-2 | 144 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9497854709625244 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -01f4a73c-7202-4ee3-964e-d32370c3c547,64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-2 | 145 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42505890130996704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 146 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023056380450725555 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 147 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19499187171459198 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 148 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10727552324533463 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 149 | PASS | STABILIZE | 95.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 162 | BUY | STABILIZE | 89.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.033638834953308 | 0.0 | 0.0 | +226a1062-8e9a-4652-9da7-a2f215fa46ae / -47feb452-27a0-43f6-983f-ea1674f17ab8,e98ea24f-414b-4ccd-a19a-d98965ccc21c |
| Jogador 8 | 2-3 | 163 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09572360664606094 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 164 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3030826151371002 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 165 | BUY | STABILIZE | 89.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2460612803697586 | 0.0 | 0.0 | +03a4a455-ebf6-4587-8ab3-acd2b1038822 / -— |
| Jogador 8 | 2-3 | 166 | REROLL | STABILIZE | 89.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 167 | BUY | STABILIZE | 89.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36924901604652405 | 0.0 | 0.0 | +cf4575c2-3622-4493-91f1-c5efbe1fbd8b / -— |
| Jogador 8 | 2-3 | 168 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06768711656332016 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 169 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009888584725558758 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 170 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012768502347171307 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 171 | PASS | STABILIZE | 89.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 183 | BUY | LOSS_STREAK | 83.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8275435566902161 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 8 | 2-4 | 184 | BUY | LOSS_STREAK | 83.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.784724235534668 | 0.0 | 0.0 | +60c8a84d-7243-462c-a452-5901135c78b8 / -— |
| Jogador 8 | 2-4 | 185 | REROLL | LOSS_STREAK | 83.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 186 | BUY | LOSS_STREAK | 83.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0971907526254654 | 0.0 | 0.0 | +dc83202b-476c-4438-90aa-a615b764b7e4 / -— |
| Jogador 8 | 2-4 | 187 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011909815948456526 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 188 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020098354667425156 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 189 | PASS | LOSS_STREAK | 83.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 205 | SELL | LOSS_STREAK | 83.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26957792043685913 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-5 | 206 | EQUIP_FROM_INVENTORY | LOSS_STREAK | 83.0 | 4 | 9 | 0 | 12.0 | Colosso/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1273362934589386 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 207 | BUY | STABILIZE | 83.0 | 4 | 9 | 0 | 12.0 | Colosso/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1175018846988678 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -— |
| Jogador 8 | 2-5 | 208 | SELL | STABILIZE | 83.0 | 4 | 8 | 0 | 12.0 | Colosso/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0162564218044281 | 0.0 | 0.0 | +— / -f17723af-f50c-4679-b557-39f9b6b8d1b6 |
| Jogador 8 | 2-5 | 209 | BUY | STABILIZE | 83.0 | 4 | 9 | 0 | 12.0 | Colosso/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05001473054289818 | 0.0 | 0.0 | +8043a64c-a04d-4399-b52d-2246fe74e470 / -— |
| Jogador 8 | 2-5 | 210 | REROLL | STABILIZE | 83.0 | 4 | 7 | 0 | 12.0 | Colosso/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 211 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 5 | 0 | 12.0 | Colosso/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08807674795389175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 212 | SELL | STABILIZE | 83.0 | 4 | 5 | 0 | 14.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0163199994713068 | 0.0 | 0.0 | +— / -8043a64c-a04d-4399-b52d-2246fe74e470 |
| Jogador 8 | 2-5 | 213 | BUY | STABILIZE | 83.0 | 4 | 7 | 0 | 14.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15230940282344818 | 0.0 | 0.0 | +652ff984-c3ac-48d7-9fb6-e95aed0a047d / -— |
| Jogador 8 | 2-5 | 214 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 5 | 0 | 14.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35867488384246826 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 215 | PASS | STABILIZE | 83.0 | 4 | 5 | 0 | 14.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 225 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 11 | 1 | 14.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09561065584421158 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 226 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 11 | 1 | 12.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2693272531032562 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 227 | BUY | STABILIZE | 78.0 | 5 | 11 | 1 | 16.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057810038328170776 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -— |
| Jogador 8 | 2-6 | 228 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 10 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5213761329650879 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 229 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 10 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32242727279663086 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 230 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 10 | 1 | 14.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10347620397806168 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 231 | REROLL | STABILIZE | 78.0 | 5 | 10 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 232 | SELL | STABILIZE | 78.0 | 5 | 8 | 0 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008320000022649765 | 0.0 | 0.0 | +— / -96bf8f0a-9fe1-4182-95dc-903c1e623983 |
| Jogador 8 | 2-6 | 233 | BUY | STABILIZE | 78.0 | 5 | 9 | 0 | 16.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9165379405021667 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 8 | 2-6 | 234 | REROLL | STABILIZE | 78.0 | 5 | 8 | 0 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 235 | PASS | STABILIZE | 78.0 | 5 | 6 | 0 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 243 | SELL | STABILIZE | 72.0 | 5 | 13 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007999999797903001 | 0.0 | 0.0 | +— / -9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 |
| Jogador 8 | 2-7 | 244 | BUY | STABILIZE | 72.0 | 5 | 14 | 1 | 16.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14205461740493774 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 8 | 2-7 | 245 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 11 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09270869195461273 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 246 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 11 | 1 | 18.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7917730212211609 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 247 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 11 | 1 | 20.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6133679151535034 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 248 | PASS | STABILIZE | 72.0 | 5 | 11 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 262 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 5 | 19 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1425938606262207 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 263 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 19 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21537642180919647 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 264 | SELL | STABILIZE | 72.0 | 5 | 19 | 1 | 18.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08655789494514465 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 3-1 | 265 | BUY | STABILIZE | 72.0 | 5 | 20 | 2 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7280693650245667 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 8 | 3-1 | 266 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 18 | 1 | 18.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39952516555786133 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 267 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 18 | 1 | 20.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6112654209136963 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 268 | PASS | STABILIZE | 72.0 | 5 | 18 | 1 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 282 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 25 | 2 | 16.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09659405052661896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 283 | SELL | STABILIZE | 72.0 | 5 | 25 | 2 | 18.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009812959469854832 | 0.0 | 0.0 | +— / -a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 8 | 3-2 | 284 | EQUIP_FROM_INVENTORY | STABILIZE | 72.0 | 5 | 27 | 2 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1528998464345932 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 285 | BUY | STABILIZE | 72.0 | 5 | 27 | 2 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8525101542472839 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -60c8a84d-7243-462c-a452-5901135c78b8,65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 3-2 | 286 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 26 | 2 | 16.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09182757139205933 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 287 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 26 | 2 | 14.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4466204345226288 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 288 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 26 | 2 | 20.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7673195004463196 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 289 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 26 | 2 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07624343037605286 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 290 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 26 | 2 | 16.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2901599109172821 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 291 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 26 | 2 | 20.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7520043849945068 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 292 | PASS | STABILIZE | 72.0 | 5 | 26 | 2 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07900000363588333 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 302 | BUY | STABILIZE | 72.0 | 5 | 35 | 3 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8082513213157654 | 0.0 | 0.0 | +685fc2a9-6a67-445e-ab34-59ec1f986f8e / -— |
| Jogador 8 | 3-3 | 303 | BUY | STABILIZE | 72.0 | 5 | 32 | 3 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.865389883518219 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 8 | 3-3 | 304 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 31 | 3 | 14.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037633202970027924 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 305 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 31 | 3 | 14.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2525949478149414 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 306 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 31 | 3 | 20.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4077657163143158 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 307 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 31 | 3 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05641850456595421 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 308 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 31 | 3 | 18.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051569417119026184 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 309 | REROLL | STABILIZE | 72.0 | 5 | 31 | 3 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 310 | BUY | STABILIZE | 72.0 | 5 | 29 | 2 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2923472821712494 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 8 | 3-3 | 311 | REROLL | STABILIZE | 72.0 | 5 | 28 | 2 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 312 | PASS | STABILIZE | 72.0 | 5 | 26 | 2 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07900000363588333 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 316 | BUY | STABILIZE | 72.0 | 5 | 35 | 3 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8204752206802368 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 8 | 3-4 | 317 | SELL | STABILIZE | 72.0 | 5 | 34 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3031309247016907 | 0.0 | 0.0 | +— / -02e125a0-3563-47ec-a82a-cba5178731dd |
| Jogador 8 | 3-4 | 318 | BUY | STABILIZE | 72.0 | 5 | 37 | 3 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3122105598449707 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -— |
| Jogador 8 | 3-4 | 319 | MOVE_BOARD | STABILIZE | 72.0 | 5 | 36 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 320 | REROLL | STABILIZE | 72.0 | 5 | 36 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 321 | MOVE_BOARD | STABILIZE | 72.0 | 5 | 34 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008066651411354542 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 322 | SELL | STABILIZE | 72.0 | 5 | 34 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37450000643730164 | 0.0 | 0.0 | +— / -150a2da3-f559-4a40-a058-005e9c74e11f |
| Jogador 8 | 3-4 | 323 | BUY | STABILIZE | 72.0 | 5 | 35 | 3 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0023753333371132612 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 8 | 3-4 | 324 | MOVE_BOARD | STABILIZE | 72.0 | 5 | 32 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -6.759585085092112e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 325 | REROLL | STABILIZE | 72.0 | 5 | 32 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2240000069141388 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 326 | PASS | STABILIZE | 72.0 | 5 | 30 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 332 | SELL | STABILIZE | 72.0 | 5 | 39 | 3 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08586645871400833 | 0.0 | 0.0 | +— / -bfe7ca8a-6e89-4673-b142-262e012398a9 |
| Jogador 8 | 3-5 | 333 | BUY | STABILIZE | 72.0 | 5 | 42 | 4 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3245832324028015 | 0.0 | 0.0 | +e99948bb-f38f-41e0-b1c4-1864c35ffe14 / -— |
| Jogador 8 | 3-5 | 334 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 41 | 4 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3133068084716797 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 335 | MOVE_BENCH | STABILIZE | 72.0 | 5 | 41 | 4 | 20.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2817586064338684 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 336 | PASS | STABILIZE | 72.0 | 5 | 41 | 4 | 18.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030500000342726707 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 347 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 50 | 5 | 18.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38047581911087036 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 348 | SELL | STABILIZE | 63.0 | 5 | 50 | 5 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3765000104904175 | 0.0 | 0.0 | +— / -e99948bb-f38f-41e0-b1c4-1864c35ffe14 |
| Jogador 8 | 3-6 | 349 | BUY | STABILIZE | 63.0 | 5 | 51 | 5 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24413855373859406 | 0.0 | 0.0 | +4bb25db6-fab7-4bf2-89e8-1a43cc6eb6a6 / -— |
| Jogador 8 | 3-6 | 350 | SELL | STABILIZE | 63.0 | 5 | 50 | 5 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16478000581264496 | 0.0 | 0.0 | +— / -4bb25db6-fab7-4bf2-89e8-1a43cc6eb6a6 |
| Jogador 8 | 3-6 | 351 | REROLL | STABILIZE | 63.0 | 5 | 51 | 5 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23199999332427979 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 352 | BUY | STABILIZE | 63.0 | 5 | 49 | 4 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24200358986854553 | 0.0 | 0.0 | +82443408-b364-4e6e-864a-1dee6162dcb5 / -— |
| Jogador 8 | 3-6 | 353 | REROLL | STABILIZE | 63.0 | 5 | 48 | 4 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 354 | REROLL | STABILIZE | 63.0 | 5 | 46 | 4 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 355 | SELL | STABILIZE | 63.0 | 5 | 44 | 4 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002240000059828162 | 0.0 | 0.0 | +— / -82443408-b364-4e6e-864a-1dee6162dcb5 |
| Jogador 8 | 3-6 | 356 | BUY | STABILIZE | 63.0 | 5 | 45 | 4 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8822173476219177 | 0.0 | 0.0 | +5d9c01d4-6ea7-4b98-8ab3-8e549d7e5906 / -af404167-469a-447e-b415-dcb52033ef9b,f087511a-d834-4f41-9b99-00bf0f6dc061 |
| Jogador 8 | 3-6 | 357 | PASS | STABILIZE | 63.0 | 5 | 44 | 4 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12999999523162842 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 362 | BUY | STABILIZE | 63.0 | 5 | 54 | 5 | 22.0 | Lutador/DA_18_Kobuko | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8997092247009277 | 0.0 | 0.0 | +fe0cdc83-3953-4aad-86c0-cf907a803a8f / -0803068a-0141-4e75-ab81-12bb13986025,652ff984-c3ac-48d7-9fb6-e95aed0a047d |
| Jogador 8 | 3-7 | 363 | BUY | STABILIZE | 63.0 | 5 | 52 | 5 | 18.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34256842732429504 | 0.0 | 0.0 | +bb2609fb-c8cb-4e7a-b308-8cd512ff870d / -— |
| Jogador 8 | 3-7 | 364 | BUY | STABILIZE | 63.0 | 5 | 51 | 5 | 18.0 | Lutador/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8623140454292297 | 0.0 | 0.0 | +0474e055-4633-408f-837c-b93b86fa46be / -— |
| Jogador 8 | 3-7 | 365 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 50 | 5 | 18.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09479691088199615 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 366 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 50 | 5 | 20.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4040029048919678 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 367 | REROLL | STABILIZE | 63.0 | 5 | 50 | 5 | 26.0 | Lutador/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23399999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 368 | BUY | STABILIZE | 63.0 | 5 | 48 | 4 | 26.0 | Lutador/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2392975091934204 | 0.0 | 0.0 | +646dafa4-69ff-4189-8342-afea213a6790 / -— |
| Jogador 8 | 3-7 | 369 | REROLL | STABILIZE | 63.0 | 5 | 46 | 4 | 26.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 370 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 44 | 4 | 26.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4018220007419586 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 371 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 44 | 4 | 22.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08066468685865402 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 372 | PASS | STABILIZE | 63.0 | 5 | 44 | 4 | 24.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 376 | CRAFT_AND_EQUIP | STABILIZE | 63.0 | 5 | 53 | 5 | 24.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1985090970993042 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 377 | CRAFT_AND_EQUIP | STABILIZE | 63.0 | 5 | 53 | 5 | 24.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18941882252693176 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 378 | SELL | STABILIZE | 63.0 | 5 | 53 | 5 | 24.0 | Lutador/DA_18_Veigar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33393222093582153 | 0.0 | 0.0 | +— / -5d9c01d4-6ea7-4b98-8ab3-8e549d7e5906 |
| Jogador 8 | 4-1 | 379 | BUY | STABILIZE | 63.0 | 5 | 56 | 5 | 24.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9599810838699341 | 0.0 | 0.0 | +5776b728-11d5-47fe-a16a-c69bf0c0975b / -cf4575c2-3622-4493-91f1-c5efbe1fbd8b,f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 8 | 4-1 | 380 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 55 | 5 | 24.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04444143548607826 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 381 | REROLL | STABILIZE | 63.0 | 5 | 55 | 5 | 26.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 382 | BUY | STABILIZE | 63.0 | 5 | 53 | 5 | 26.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3940649926662445 | 0.0 | 0.0 | +28c6ef78-f842-45d2-b020-1cb2c0ee83c1 / -— |
| Jogador 8 | 4-1 | 383 | BUY | STABILIZE | 63.0 | 5 | 52 | 5 | 26.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9299906492233276 | 0.0 | 0.0 | +e14dbc54-2ddf-4a4a-afce-49045a4c34ac / -— |
| Jogador 8 | 4-1 | 384 | REROLL | STABILIZE | 63.0 | 5 | 51 | 5 | 26.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1720000058412552 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 385 | MOVE_BENCH | STABILIZE | 63.0 | 5 | 49 | 4 | 26.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4018218517303467 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 386 | PASS | STABILIZE | 63.0 | 5 | 49 | 4 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04928571358323097 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 388 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 61 | 5 | 22.0 | Lutador/DA_18_Kobuko | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5971131920814514 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 389 | BUY | FAST8 | 63.0 | 6 | 61 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16679807007312775 | 0.0 | 0.0 | +a0f77ac2-10b9-4e83-a9da-54bf70c1f177 / -— |
| Jogador 8 | 4-2 | 390 | MOVE_BOARD | FAST8 | 63.0 | 6 | 60 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0002373991592321545 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 391 | MOVE_BOARD | FAST8 | 63.0 | 6 | 60 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015461747534573078 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 392 | MOVE_BOARD | FAST8 | 63.0 | 6 | 60 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 393 | PASS | FAST8 | 63.0 | 6 | 60 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08595746010541916 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 402 | MOVE_BOARD | FAST8 | 63.0 | 6 | 72 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0013154109474271536 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 403 | MOVE_BOARD | FAST8 | 63.0 | 6 | 72 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 404 | MOVE_BOARD | FAST8 | 63.0 | 6 | 72 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015017475932836533 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 405 | PASS | FAST8 | 63.0 | 6 | 72 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09418163448572159 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 413 | MOVE_BOARD | FAST8 | 63.0 | 6 | 84 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00017175629909615964 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 414 | MOVE_BOARD | FAST8 | 63.0 | 6 | 84 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 415 | MOVE_BOARD | FAST8 | 63.0 | 6 | 84 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01481649000197649 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 416 | PASS | FAST8 | 63.0 | 6 | 84 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10289222747087479 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 423 | MOVE_BOARD | FAST8 | 63.0 | 6 | 95 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 424 | MOVE_BOARD | FAST8 | 63.0 | 6 | 95 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015039730817079544 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 425 | PASS | FAST8 | 63.0 | 6 | 95 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11115982383489609 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 434 | SELL | FAST8 | 63.0 | 6 | 108 | 5 | 30.0 | Lutador/DA_18_Kobuko | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5412750244140625 | 0.0 | 0.0 | +— / -5776b728-11d5-47fe-a16a-c69bf0c0975b |
| Jogador 8 | 4-6 | 435 | BUY | FAST8 | 63.0 | 6 | 111 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8076390624046326 | 0.0 | 0.0 | +cc95fa5f-96df-47bd-bdc4-5c78d2bbca72 / -— |
| Jogador 8 | 4-6 | 436 | SELL | FAST8 | 63.0 | 6 | 108 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1382313072681427 | 0.0 | 0.0 | +— / -a0f77ac2-10b9-4e83-a9da-54bf70c1f177 |
| Jogador 8 | 4-6 | 437 | BUY | FAST8 | 63.0 | 6 | 109 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8891944289207458 | 0.0 | 0.0 | +802fa29f-5d80-4bbe-92cb-bb63575f1ac3 / -0474e055-4633-408f-837c-b93b86fa46be,bb2609fb-c8cb-4e7a-b308-8cd512ff870d |
| Jogador 8 | 4-6 | 438 | MOVE_BOARD | FAST8 | 63.0 | 6 | 108 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -2.019358544202987e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 439 | MOVE_BOARD | FAST8 | 63.0 | 6 | 108 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 440 | PASS | FAST8 | 63.0 | 6 | 108 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26119381189346313 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 445 | BUY | FAST8 | 63.0 | 6 | 122 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013344335369765759 | 0.0 | 0.0 | +5f35f06e-eab3-4b4e-a5d6-fbddb0327295 / -— |
| Jogador 8 | 4-7 | 446 | MOVE_BOARD | FAST8 | 63.0 | 6 | 121 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00010510253923712298 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 447 | MOVE_BOARD | FAST8 | 63.0 | 6 | 121 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 448 | MOVE_BOARD | FAST8 | 63.0 | 6 | 121 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 449 | PASS | FAST8 | 63.0 | 6 | 121 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13145712018013 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 455 | CRAFT_AND_EQUIP | FAST8 | 63.0 | 6 | 134 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19766400754451752 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 456 | CRAFT_AND_EQUIP | FAST8 | 63.0 | 6 | 134 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20722195506095886 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 457 | BUY | FAST8 | 63.0 | 6 | 134 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41354402899742126 | 0.0 | 0.0 | +4d4dad01-cb4a-40cb-aa4f-6b52b3820f08 / -— |
| Jogador 8 | 5-1 | 458 | MOVE_BENCH | FAST8 | 63.0 | 6 | 132 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09751750528812408 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 459 | MOVE_BENCH | FAST8 | 63.0 | 6 | 132 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41872352361679077 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 460 | MOVE_BENCH | FAST8 | 63.0 | 6 | 132 | 5 | 26.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32172662019729614 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 461 | PASS | FAST8 | 63.0 | 6 | 132 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15432071685791016 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 465 | SELL | FAST8 | 63.0 | 6 | 146 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.356462687253952 | 0.0 | 0.0 | +— / -802fa29f-5d80-4bbe-92cb-bb63575f1ac3 |
| Jogador 8 | 5-2 | 466 | BUY | FAST8 | 63.0 | 6 | 149 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499934911727905 | 0.0 | 0.0 | +38a0b280-3ff2-4984-8ede-6d866099c5dd / -28c6ef78-f842-45d2-b020-1cb2c0ee83c1,e14dbc54-2ddf-4a4a-afce-49045a4c34ac |
| Jogador 8 | 5-2 | 467 | BUY | FAST8 | 63.0 | 6 | 148 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36212724447250366 | 0.0 | 0.0 | +b2692c06-cf9f-40f0-acad-9c43e7ce225b / -— |
| Jogador 8 | 5-2 | 468 | MOVE_BENCH | FAST8 | 63.0 | 6 | 147 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06497998535633087 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 469 | MOVE_BENCH | FAST8 | 63.0 | 6 | 147 | 5 | 26.0 | Lutador/DA_18_RekSai | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08511814475059509 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 470 | MOVE_BENCH | FAST8 | 63.0 | 6 | 147 | 5 | 30.0 | Lutador/DA_18_RekSai | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41488176584243774 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 471 | MOVE_BOARD | FAST8 | 63.0 | 6 | 147 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015031407587230206 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 472 | PASS | FAST8 | 63.0 | 6 | 147 | 5 | 30.0 | Lutador/DA_18_RekSai | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32178163528442383 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 475 | BUY | FAST8 | 48.0 | 6 | 157 | 5 | 30.0 | Lutador/DA_18_RekSai | BUY, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3811356723308563 | 0.0 | 0.0 | +de74a68e-4d86-4cf6-8994-739d087a91cd / -— |
| Jogador 8 | 5-3 | 476 | MOVE_BENCH | FAST8 | 48.0 | 6 | 155 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 477 | MOVE_BENCH | FAST8 | 48.0 | 6 | 155 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04992716386914253 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 478 | MOVE_BENCH | FAST8 | 48.0 | 6 | 155 | 5 | 26.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36731192469596863 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 479 | MOVE_BENCH | FAST8 | 48.0 | 6 | 155 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 480 | PASS | FAST8 | 48.0 | 6 | 155 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17504867911338806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 484 | MOVE_BENCH | FAST8 | 48.0 | 6 | 166 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06492141634225845 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 485 | MOVE_BENCH | FAST8 | 48.0 | 6 | 166 | 5 | 26.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0851479172706604 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 486 | MOVE_BENCH | FAST8 | 48.0 | 6 | 166 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41487574577331543 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 487 | MOVE_BENCH | FAST8 | 48.0 | 6 | 166 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 488 | PASS | FAST8 | 48.0 | 6 | 166 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18513096868991852 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 494 | MOVE_BENCH | FAST8 | 48.0 | 6 | 176 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09989261627197266 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 495 | MOVE_BENCH | FAST8 | 48.0 | 6 | 176 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4148804247379303 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 496 | MOVE_BENCH | FAST8 | 48.0 | 6 | 176 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 497 | PASS | FAST8 | 48.0 | 6 | 176 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19438038766384125 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 503 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 186 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06489772349596024 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 504 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 186 | 5 | 26.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3676401972770691 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 505 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 186 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08490368723869324 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 506 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 186 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4151025712490082 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 507 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 186 | 5 | 26.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3675529658794403 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 508 | PASS | STABILIZE | 33.0 | 6 | 186 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22717022895812988 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 512 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09989865124225616 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 513 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0500137135386467 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 514 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41498956084251404 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 515 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050156671553850174 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 516 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 26.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08522043377161026 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 517 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39999350905418396 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 518 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06506031006574631 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 519 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 26.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10011796653270721 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 520 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 197 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3998817503452301 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 522 | EQUIP_FROM_INVENTORY | STABILIZE | 17.0 | 6 | 208 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.015623856335878372 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 523 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 208 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 524 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 208 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08494804799556732 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 525 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 208 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04990893229842186 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 526 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 208 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499942541122437 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 527 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 208 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41499999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 528 | PASS | STABILIZE | 17.0 | 6 | 208 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3045889735221863 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 532 | SELL | STABILIZE | 17.0 | 6 | 219 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5412750244140625 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 8 | 6-2 | 533 | EQUIP_FROM_INVENTORY | STABILIZE | 17.0 | 6 | 222 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.11991959065198898 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 534 | BUY | STABILIZE | 17.0 | 6 | 222 | 5 | 30.0 | Lutador/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08087851107120514 | 0.0 | 0.0 | +4c6b9e2a-a3fd-4acf-b8d6-cf4daea385c4 / -— |
| Jogador 8 | 6-2 | 535 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 221 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060126159340143204 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 536 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 221 | 5 | 28.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40161725878715515 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 537 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 221 | 5 | 28.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0522799976170063 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 538 | PASS | STABILIZE | 17.0 | 6 | 221 | 5 | 30.0 | Lutador/DA_18_Alistar | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3181154727935791 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 200 | 135 | 28 | 9 | 0 | 0 | 34 | 1 | 20 | 36.0 |
- Jogador 1 — gasto por ação: BUY: 67g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 68g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 45g, stage 3: 50g, stage 4: 34g
| Jogador 2 | 228 | 152 | 60 | 8 | 0 | 0 | 30 | 2 | 109 | 24.0 |
- Jogador 2 — gasto por ação: BUY: 92g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 60g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 50g, stage 3: 36g, stage 4: 43g, stage 5: 16g
| Jogador 3 | 294 | 171 | 60 | 12 | 0 | 0 | 29 | 2 | 210 | 38.0 |
- Jogador 3 — gasto por ação: BUY: 113g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 58g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 62g, stage 4: 22g, stage 5: 14g, stage 6: 8g, stage 7: 12g
| Jogador 4 | 234 | 178 | 34 | 7 | 0 | 0 | 51 | 1 | 1 | 32.0 |
- Jogador 4 — gasto por ação: BUY: 76g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 102g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 7g, stage 2: 40g, stage 3: 67g, stage 4: 52g, stage 5: 12g
| Jogador 5 | 249 | 202 | 57 | 7 | 0 | 0 | 48 | 1 | 12 | 40.0 |
- Jogador 5 — gasto por ação: BUY: 106g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 96g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 61g, stage 3: 55g, stage 4: 58g, stage 5: 21g
| Jogador 6 | 319 | 206 | 57 | 8 | 5 | 0 | 33 | 5 | 211 | 34.0 |
- Jogador 6 — gasto por ação: BUY: 120g, BUY_XP: 20g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 66g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 50g, stage 3: 86g, stage 4: 31g, stage 5: 16g, stage 6: 16g, stage 7: 0g
| Jogador 7 | 183 | 116 | 23 | 5 | 0 | 0 | 26 | 1 | 72 | 34.0 |
- Jogador 7 — gasto por ação: BUY: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 52g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 30g, stage 3: 40g, stage 4: 40g
| Jogador 8 | 257 | 108 | 37 | 6 | 0 | 0 | 17 | 3 | 221 | 30.0 |
- Jogador 8 — gasto por ação: BUY: 74g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 34g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 40g, stage 3: 41g, stage 4: 13g, stage 5: 6g, stage 6: 1g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 0 | 38 |
- Jogador 1 · 2-2 · step 141: REROLL com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 1 · 2-6 · step 228: REROLL com 5g, HP 90, nível 5/8 (STABILIZE).
- Jogador 1 · 2-6 · step 233: REROLL com 5g, HP 90, nível 5/8 (STABILIZE).
- Jogador 1 · 2-6 · step 235: PASS com 6g, HP 90, nível 5/8 (STABILIZE).
- Jogador 1 · 2-7 · step 247: REROLL com 9g, HP 83, nível 5/8 (STABILIZE).
- Jogador 1 · 2-7 · step 248: REROLL com 7g, HP 83, nível 5/8 (STABILIZE).
- Jogador 1 · 2-7 · step 249: REROLL com 5g, HP 83, nível 5/8 (STABILIZE).
- Jogador 1 · 3-1 · step 263: REROLL com 5g, HP 83, nível 5/8 (STABILIZE).
- Jogador 1 · 3-2 · step 285: PASS com 7g, HP 83, nível 5/8 (STABILIZE).
- Jogador 1 · 3-3 · step 306: REROLL com 11g, HP 73, nível 5/8 (STABILIZE).
- Jogador 1 · 3-3 · step 310: PASS com 9g, HP 73, nível 5/8 (STABILIZE).
- Jogador 1 · 3-4 · step 319: REROLL com 13g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-4 · step 320: REROLL com 11g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-4 · step 325: PASS com 8g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-5 · step 338: REROLL com 19g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-5 · step 340: REROLL com 16g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-5 · step 342: PASS com 13g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-6 · step 348: REROLL com 18g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-6 · step 349: REROLL com 16g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-6 · step 352: REROLL com 12g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-6 · step 353: REROLL com 10g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-6 · step 356: REROLL com 6g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-6 · step 357: PASS com 4g, HP 62, nível 5/8 (STABILIZE).
- Jogador 1 · 3-7 · step 363: REROLL com 7g, HP 52, nível 5/8 (STABILIZE).
- Jogador 1 · 3-7 · step 366: REROLL com 4g, HP 52, nível 5/8 (STABILIZE).
- Jogador 1 · 4-1 · step 380: PASS com 5g, HP 52, nível 5/8 (STABILIZE).
- Jogador 1 · 4-2 · step 392: PASS com 11g, HP 40, nível 6/8 (FAST8).
- Jogador 1 · 4-3 · step 403: REROLL com 17g, HP 29, nível 6/8 (STABILIZE).
- Jogador 1 · 4-3 · step 408: REROLL com 17g, HP 29, nível 6/8 (STABILIZE).
- Jogador 1 · 4-4 · step 413: REROLL com 23g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-4 · step 416: REROLL com 23g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-4 · step 417: REROLL com 21g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-4 · step 419: REROLL com 17g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-4 · step 421: REROLL com 15g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-5 · step 424: REROLL com 19g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-5 · step 425: REROLL com 17g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-5 · step 432: REROLL com 15g, HP 18, nível 6/8 (STABILIZE).
- Jogador 1 · 4-6 · step 440: PASS com 20g, HP 9, nível 6/8 (ALL_IN).
| Jogador 2 | 0 | 42 |
- Jogador 2 · 2-2 · step 143: REROLL com 4g, HP 95, nível 4/8 (STABILIZE).
- Jogador 2 · 2-3 · step 164: REROLL com 4g, HP 90, nível 4/8 (STABILIZE).
- Jogador 2 · 2-4 · step 187: REROLL com 4g, HP 90, nível 4/8 (STABILIZE).
- Jogador 2 · 2-5 · step 209: REROLL com 5g, HP 90, nível 4/8 (STABILIZE).
- Jogador 2 · 2-6 · step 227: REROLL com 5g, HP 85, nível 5/8 (STABILIZE).
- Jogador 2 · 2-7 · step 246: REROLL com 9g, HP 79, nível 5/8 (STABILIZE).
- Jogador 2 · 2-7 · step 250: REROLL com 7g, HP 79, nível 5/8 (STABILIZE).
- Jogador 2 · 2-7 · step 253: PASS com 5g, HP 79, nível 5/8 (STABILIZE).
- Jogador 2 · 3-1 · step 269: PASS com 13g, HP 79, nível 5/8 (STABILIZE).
- Jogador 2 · 3-2 · step 287: REROLL com 18g, HP 68, nível 5/8 (STABILIZE).
- Jogador 2 · 3-2 · step 289: REROLL com 14g, HP 68, nível 5/8 (STABILIZE).
- Jogador 2 · 3-2 · step 291: REROLL com 9g, HP 68, nível 5/8 (STABILIZE).
- Jogador 2 · 3-2 · step 292: PASS com 7g, HP 68, nível 5/8 (STABILIZE).
- Jogador 2 · 3-3 · step 305: REROLL com 14g, HP 59, nível 5/8 (STABILIZE).
- Jogador 2 · 3-3 · step 308: PASS com 12g, HP 59, nível 5/8 (STABILIZE).
- Jogador 2 · 3-4 · step 321: PASS com 18g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 3-5 · step 337: PASS com 28g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 3-6 · step 352: PASS com 38g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 3-7 · step 365: REROLL com 50g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 3-7 · step 367: REROLL com 45g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 3-7 · step 369: REROLL com 41g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 3-7 · step 372: PASS com 39g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 4-1 · step 381: REROLL com 47g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 4-1 · step 384: REROLL com 42g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 4-1 · step 386: PASS com 43g, HP 50, nível 5/8 (STABILIZE).
- Jogador 2 · 4-2 · step 392: PASS com 52g, HP 40, nível 6/8 (FAST8).
- Jogador 2 · 4-3 · step 406: PASS com 62g, HP 40, nível 6/8 (FAST8).
- Jogador 2 · 4-4 · step 416: REROLL com 70g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-4 · step 420: REROLL com 66g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-5 · step 425: REROLL com 72g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-5 · step 428: REROLL com 68g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-5 · step 432: REROLL com 65g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-6 · step 435: REROLL com 71g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-6 · step 439: REROLL com 71g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-6 · step 442: REROLL com 70g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 4-7 · step 449: PASS com 81g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 5-1 · step 459: PASS com 92g, HP 28, nível 6/8 (STABILIZE).
- Jogador 2 · 5-2 · step 468: REROLL com 106g, HP 13, nível 6/8 (ALL_IN).
- Jogador 2 · 5-2 · step 473: REROLL com 108g, HP 13, nível 6/8 (ALL_IN).
- Jogador 2 · 5-3 · step 475: REROLL com 117g, HP 13, nível 6/8 (ALL_IN).
- Jogador 2 · 5-3 · step 478: REROLL com 113g, HP 13, nível 6/8 (ALL_IN).
- Jogador 2 · 5-3 · step 479: REROLL com 111g, HP 13, nível 6/8 (ALL_IN).
| Jogador 3 | 0 | 45 |
- Jogador 3 · 2-4 · step 185: REROLL com 6g, HP 95, nível 4/8 (STABILIZE).
- Jogador 3 · 2-5 · step 207: REROLL com 7g, HP 95, nível 4/8 (STABILIZE).
- Jogador 3 · 2-5 · step 209: REROLL com 4g, HP 95, nível 4/8 (STABILIZE).
- Jogador 3 · 2-6 · step 229: PASS com 7g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 244: REROLL com 11g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 247: REROLL com 7g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 2-7 · step 248: REROLL com 5g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-1 · step 263: REROLL com 6g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-1 · step 270: REROLL com 4g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-2 · step 283: REROLL com 7g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-2 · step 286: PASS com 5g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-3 · step 307: REROLL com 12g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-3 · step 308: REROLL com 10g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-3 · step 312: PASS com 9g, HP 95, nível 5/8 (STABILIZE).
- Jogador 3 · 3-4 · step 316: REROLL com 14g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-4 · step 318: REROLL com 10g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-4 · step 321: PASS com 8g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-5 · step 336: REROLL com 9g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-5 · step 337: REROLL com 7g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-5 · step 341: REROLL com 8g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-5 · step 342: PASS com 6g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 349: REROLL com 14g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 350: REROLL com 12g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 355: REROLL com 10g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-6 · step 357: PASS com 5g, HP 86, nível 5/8 (STABILIZE).
- Jogador 3 · 3-7 · step 366: REROLL com 7g, HP 76, nível 5/8 (STABILIZE).
- Jogador 3 · 4-2 · step 391: REROLL com 13g, HP 76, nível 6/8 (STABILIZE).
- Jogador 3 · 4-2 · step 394: REROLL com 11g, HP 76, nível 6/8 (STABILIZE).
- Jogador 3 · 4-2 · step 398: PASS com 7g, HP 76, nível 6/8 (FAST8).
- Jogador 3 · 4-3 · step 404: PASS com 14g, HP 76, nível 6/8 (FAST8).
- Jogador 3 · 4-4 · step 415: PASS com 22g, HP 76, nível 6/8 (FAST8).
- Jogador 3 · 4-5 · step 427: PASS com 29g, HP 76, nível 6/8 (FAST8).
- Jogador 3 · 4-6 · step 438: PASS com 37g, HP 76, nível 6/8 (FAST8).
- Jogador 3 · 4-7 · step 448: PASS com 45g, HP 65, nível 6/8 (FAST8).
- Jogador 3 · 5-1 · step 460: PASS com 54g, HP 65, nível 6/8 (FAST8).
- Jogador 3 · 5-2 · step 468: PASS com 65g, HP 65, nível 6/8 (FAST8).
- Jogador 3 · 5-4 · step 486: PASS com 87g, HP 65, nível 6/8 (FAST8).
- Jogador 3 · 5-5 · step 499: PASS com 96g, HP 65, nível 6/8 (FAST8).
- Jogador 3 · 5-7 · step 520: PASS com 122g, HP 65, nível 6/8 (FAST8).
- Jogador 3 · 6-1 · step 526: PASS com 133g, HP 65, nível 6/8 (FAST8).
- Jogador 3 · 6-2 · step 535: PASS com 143g, HP 47, nível 6/8 (FAST8).
- Jogador 3 · 6-5 · step 568: PASS com 178g, HP 47, nível 6/8 (FAST8).
- Jogador 3 · 6-6 · step 576: PASS com 189g, HP 47, nível 7/8 (FAST8).
- Jogador 3 · 6-7 · step 588: PASS com 198g, HP 47, nível 7/8 (FAST8).
- Jogador 3 · 7-2 · step 606: PASS com 210g, HP 47, nível 7/8 (FAST8).
| Jogador 4 | 0 | 48 |
- Jogador 4 · 2-3 · step 164: REROLL com 5g, HP 88, nível 4/8 (STABILIZE).
- Jogador 4 · 2-5 · step 210: REROLL com 6g, HP 88, nível 4/8 (STABILIZE).
- Jogador 4 · 2-6 · step 228: PASS com 7g, HP 88, nível 5/8 (STABILIZE).
- Jogador 4 · 2-7 · step 249: PASS com 13g, HP 88, nível 5/8 (STABILIZE).
- Jogador 4 · 3-1 · step 264: REROLL com 18g, HP 88, nível 5/8 (STABILIZE).
- Jogador 4 · 3-1 · step 265: REROLL com 16g, HP 88, nível 5/8 (STABILIZE).
- Jogador 4 · 3-1 · step 271: PASS com 12g, HP 88, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 283: REROLL com 17g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 284: REROLL com 15g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 285: REROLL com 13g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 286: REROLL com 11g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 289: REROLL com 11g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-2 · step 292: PASS com 12g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-3 · step 302: REROLL com 19g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-3 · step 303: REROLL com 17g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-3 · step 304: REROLL com 15g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-3 · step 305: REROLL com 13g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-3 · step 309: PASS com 10g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 316: REROLL com 18g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 317: REROLL com 16g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 318: REROLL com 14g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 319: REROLL com 12g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 320: REROLL com 10g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 321: REROLL com 8g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 322: REROLL com 6g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-4 · step 323: REROLL com 4g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-5 · step 335: REROLL com 4g, HP 79, nível 5/8 (STABILIZE).
- Jogador 4 · 3-6 · step 348: REROLL com 4g, HP 69, nível 5/8 (STABILIZE).
- Jogador 4 · 3-7 · step 366: REROLL com 7g, HP 59, nível 5/8 (STABILIZE).
- Jogador 4 · 3-7 · step 368: REROLL com 4g, HP 59, nível 5/8 (STABILIZE).
- Jogador 4 · 4-1 · step 379: REROLL com 5g, HP 59, nível 5/8 (STABILIZE).
- Jogador 4 · 4-1 · step 386: PASS com 7g, HP 59, nível 5/8 (STABILIZE).
- Jogador 4 · 4-2 · step 391: PASS com 13g, HP 50, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 402: REROLL com 20g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 403: REROLL com 18g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 404: REROLL com 16g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 405: REROLL com 14g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 406: REROLL com 12g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 407: REROLL com 10g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-3 · step 409: REROLL com 5g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-4 · step 413: REROLL com 6g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-4 · step 414: REROLL com 4g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-5 · step 423: REROLL com 7g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-5 · step 424: REROLL com 5g, HP 38, nível 6/8 (STABILIZE).
- Jogador 4 · 4-6 · step 437: REROLL com 7g, HP 27, nível 6/8 (STABILIZE).
- Jogador 4 · 4-7 · step 445: REROLL com 7g, HP 15, nível 6/8 (ALL_IN).
- Jogador 4 · 5-1 · step 459: REROLL com 4g, HP 15, nível 6/8 (ALL_IN).
- Jogador 4 · 5-2 · step 466: REROLL com 5g, HP 1, nível 6/8 (ALL_IN).
| Jogador 5 | 0 | 47 |
- Jogador 5 · 2-2 · step 141: REROLL com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-3 · step 165: REROLL com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-3 · step 170: REROLL com 5g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-4 · step 186: REROLL com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-4 · step 188: REROLL com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-5 · step 210: REROLL com 7g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-5 · step 213: REROLL com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-5 · step 215: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 5 · 2-6 · step 227: REROLL com 8g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 2-6 · step 231: REROLL com 4g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 2-7 · step 245: REROLL com 8g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 2-7 · step 250: REROLL com 4g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 3-1 · step 264: REROLL com 8g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 3-1 · step 266: REROLL com 4g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 3-1 · step 271: REROLL com 5g, HP 100, nível 5/8 (STABILIZE).
- Jogador 5 · 3-2 · step 284: REROLL com 7g, HP 91, nível 5/8 (STABILIZE).
- Jogador 5 · 3-2 · step 285: REROLL com 5g, HP 91, nível 5/8 (STABILIZE).
- Jogador 5 · 3-3 · step 304: REROLL com 6g, HP 81, nível 5/8 (STABILIZE).
- Jogador 5 · 3-3 · step 307: REROLL com 4g, HP 81, nível 5/8 (STABILIZE).
- Jogador 5 · 3-4 · step 321: REROLL com 6g, HP 81, nível 5/8 (STABILIZE).
- Jogador 5 · 3-5 · step 333: REROLL com 4g, HP 81, nível 5/8 (STABILIZE).
- Jogador 5 · 3-6 · step 352: REROLL com 9g, HP 70, nível 5/8 (STABILIZE).
- Jogador 5 · 3-6 · step 357: PASS com 4g, HP 70, nível 5/8 (STABILIZE).
- Jogador 5 · 3-7 · step 364: PASS com 10g, HP 70, nível 5/8 (STABILIZE).
- Jogador 5 · 4-1 · step 379: REROLL com 16g, HP 70, nível 5/8 (STABILIZE).
- Jogador 5 · 4-1 · step 384: PASS com 12g, HP 70, nível 5/8 (STABILIZE).
- Jogador 5 · 4-2 · step 391: PASS com 18g, HP 59, nível 6/8 (STABILIZE).
- Jogador 5 · 4-3 · step 407: PASS com 24g, HP 47, nível 6/8 (FAST8).
- Jogador 5 · 4-4 · step 415: REROLL com 28g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 416: REROLL com 26g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 418: REROLL com 22g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 419: REROLL com 20g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 420: REROLL com 18g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-4 · step 421: REROLL com 16g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-5 · step 423: REROLL com 21g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-5 · step 424: REROLL com 19g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-5 · step 425: REROLL com 17g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-5 · step 429: REROLL com 12g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-6 · step 434: REROLL com 16g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-6 · step 436: REROLL com 12g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-6 · step 438: REROLL com 9g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-6 · step 439: REROLL com 7g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-6 · step 441: REROLL com 4g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 4-7 · step 445: REROLL com 7g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 5-1 · step 457: REROLL com 6g, HP 35, nível 6/8 (STABILIZE).
- Jogador 5 · 5-2 · step 466: REROLL com 4g, HP 21, nível 6/8 (STABILIZE).
- Jogador 5 · 5-3 · step 479: REROLL com 15g, HP 8, nível 6/8 (ALL_IN).
| Jogador 6 | 5 | 56 |
- Jogador 6 · 2-2 · step 141: REROLL com 5g, HP 96, nível 4/8 (STABILIZE).
- Jogador 6 · 2-3 · step 168: REROLL com 6g, HP 96, nível 4/8 (STABILIZE).
- Jogador 6 · 2-5 · step 208: REROLL com 4g, HP 96, nível 4/8 (STABILIZE).
- Jogador 6 · 2-6 · step 228: REROLL com 5g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 2-7 · step 244: REROLL com 7g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-1 · step 266: REROLL com 7g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-1 · step 267: REROLL com 5g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-1 · step 270: REROLL com 5g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-1 · step 272: PASS com 8g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-2 · step 283: REROLL com 14g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-2 · step 286: REROLL com 13g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-2 · step 291: REROLL com 9g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-2 · step 292: PASS com 7g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-3 · step 306: REROLL com 20g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-3 · step 311: REROLL com 17g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-3 · step 312: PASS com 15g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-4 · step 317: REROLL com 24g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-4 · step 320: REROLL com 21g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-4 · step 323: REROLL com 19g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-4 · step 324: REROLL com 17g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-4 · step 325: REROLL com 15g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-4 · step 326: PASS com 13g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-5 · step 334: REROLL com 22g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-5 · step 338: REROLL com 19g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-5 · step 341: REROLL com 13g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-5 · step 342: PASS com 11g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-6 · step 348: REROLL com 20g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-6 · step 349: REROLL com 18g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-6 · step 351: REROLL com 15g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-6 · step 354: REROLL com 13g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-6 · step 357: PASS com 12g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-7 · step 364: REROLL com 24g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-7 · step 368: REROLL com 20g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-7 · step 370: REROLL com 17g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 3-7 · step 372: PASS com 13g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 4-1 · step 379: REROLL com 19g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 4-1 · step 383: REROLL com 13g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 4-1 · step 386: PASS com 13g, HP 96, nível 5/8 (STABILIZE).
- Jogador 6 · 4-2 · step 388: REROLL com 23g, HP 96, nível 6/8 (STABILIZE).
- Jogador 6 · 4-2 · step 391: PASS com 21g, HP 96, nível 6/8 (STABILIZE).
- Jogador 6 · 4-3 · step 407: PASS com 32g, HP 96, nível 6/8 (FAST8).
- Jogador 6 · 4-4 · step 418: PASS com 43g, HP 96, nível 6/8 (FAST8).
- Jogador 6 · 4-5 · step 426: PASS com 53g, HP 96, nível 6/8 (FAST8).
- Jogador 6 · 4-7 · step 449: PASS com 62g, HP 83, nível 6/8 (FAST8).
- Jogador 6 · 5-1 · step 460: PASS com 70g, HP 83, nível 6/8 (FAST8).
- Jogador 6 · 5-3 · step 479: PASS com 85g, HP 83, nível 7/8 (FAST8).
- Jogador 6 · 5-4 · step 486: PASS com 96g, HP 83, nível 7/8 (FAST8).
- Jogador 6 · 5-5 · step 497: PASS com 107g, HP 83, nível 7/8 (FAST8).
- Jogador 6 · 5-6 · step 507: PASS com 117g, HP 83, nível 7/8 (FAST8).
- Jogador 6 · 5-7 · step 515: PASS com 127g, HP 83, nível 7/8 (FAST8).
- Jogador 6 · 6-1 · step 529: PASS com 134g, HP 83, nível 7/8 (FAST8).
- Jogador 6 · 6-3 · step 547: PASS com 147g, HP 83, nível 7/8 (FAST8).
- Jogador 6 · 6-4 · step 556: PASS com 157g, HP 66, nível 7/8 (FAST8).
- Jogador 6 · 6-5 · step 565: PASS com 167g, HP 66, nível 7/8 (FAST8).
- Jogador 6 · 6-7 · step 586: PASS com 189g, HP 30, nível 7/8 (STABILIZE).
- Jogador 6 · 7-2 · step 608: PASS com 211g, HP 6, nível 7/8 (ALL_IN).
| Jogador 7 | 0 | 39 |
- Jogador 7 · 2-2 · step 143: PASS com 4g, HP 100, nível 4/8 (STABILIZE).
- Jogador 7 · 2-3 · step 166: PASS com 6g, HP 94, nível 4/8 (STABILIZE).
- Jogador 7 · 2-4 · step 185: REROLL com 9g, HP 89, nível 4/8 (STABILIZE).
- Jogador 7 · 2-4 · step 188: REROLL com 4g, HP 89, nível 4/8 (STABILIZE).
- Jogador 7 · 2-5 · step 206: REROLL com 5g, HP 89, nível 4/8 (STABILIZE).
- Jogador 7 · 2-6 · step 228: PASS com 5g, HP 85, nível 5/8 (STABILIZE).
- Jogador 7 · 2-7 · step 247: PASS com 11g, HP 78, nível 5/8 (STABILIZE).
- Jogador 7 · 3-1 · step 266: PASS com 15g, HP 78, nível 5/8 (STABILIZE).
- Jogador 7 · 3-2 · step 291: PASS com 17g, HP 68, nível 5/8 (STABILIZE).
- Jogador 7 · 3-3 · step 304: REROLL com 23g, HP 58, nível 5/8 (STABILIZE).
- Jogador 7 · 3-3 · step 307: REROLL com 19g, HP 58, nível 5/8 (STABILIZE).
- Jogador 7 · 3-3 · step 312: PASS com 16g, HP 58, nível 5/8 (STABILIZE).
- Jogador 7 · 3-4 · step 319: REROLL com 24g, HP 47, nível 5/8 (STABILIZE).
- Jogador 7 · 3-4 · step 321: REROLL com 21g, HP 47, nível 5/8 (STABILIZE).
- Jogador 7 · 3-4 · step 323: REROLL com 18g, HP 47, nível 5/8 (STABILIZE).
- Jogador 7 · 3-4 · step 326: PASS com 20g, HP 47, nível 5/8 (STABILIZE).
- Jogador 7 · 3-5 · step 332: REROLL com 30g, HP 47, nível 5/8 (STABILIZE).
- Jogador 7 · 3-5 · step 333: REROLL com 28g, HP 47, nível 5/8 (STABILIZE).
- Jogador 7 · 3-5 · step 342: PASS com 29g, HP 47, nível 5/8 (STABILIZE).
- Jogador 7 · 3-6 · step 347: REROLL com 39g, HP 37, nível 5/8 (STABILIZE).
- Jogador 7 · 3-6 · step 349: REROLL com 36g, HP 37, nível 5/8 (STABILIZE).
- Jogador 7 · 3-6 · step 350: REROLL com 34g, HP 37, nível 5/8 (STABILIZE).
- Jogador 7 · 3-6 · step 354: PASS com 32g, HP 37, nível 5/8 (STABILIZE).
- Jogador 7 · 3-7 · step 365: PASS com 43g, HP 27, nível 5/8 (STABILIZE).
- Jogador 7 · 4-1 · step 384: REROLL com 59g, HP 27, nível 5/8 (STABILIZE).
- Jogador 7 · 4-1 · step 385: REROLL com 57g, HP 27, nível 5/8 (STABILIZE).
- Jogador 7 · 4-1 · step 386: PASS com 55g, HP 27, nível 5/8 (STABILIZE).
- Jogador 7 · 4-2 · step 390: REROLL com 64g, HP 27, nível 6/8 (STABILIZE).
- Jogador 7 · 4-2 · step 394: PASS com 62g, HP 27, nível 6/8 (STABILIZE).
- Jogador 7 · 4-3 · step 403: REROLL com 71g, HP 16, nível 6/8 (STABILIZE).
- Jogador 7 · 4-3 · step 408: PASS com 71g, HP 16, nível 6/8 (STABILIZE).
- Jogador 7 · 4-4 · step 414: REROLL com 81g, HP 4, nível 6/8 (ALL_IN).
- Jogador 7 · 4-4 · step 415: REROLL com 79g, HP 4, nível 6/8 (ALL_IN).
- Jogador 7 · 4-4 · step 416: REROLL com 77g, HP 4, nível 6/8 (ALL_IN).
- Jogador 7 · 4-4 · step 419: REROLL com 73g, HP 4, nível 6/8 (ALL_IN).
- Jogador 7 · 4-5 · step 424: REROLL com 80g, HP 4, nível 6/8 (ALL_IN).
- Jogador 7 · 4-5 · step 426: REROLL com 76g, HP 4, nível 6/8 (ALL_IN).
- Jogador 7 · 4-5 · step 427: REROLL com 74g, HP 4, nível 6/8 (ALL_IN).
- Jogador 7 · 4-5 · step 430: REROLL com 72g, HP 4, nível 6/8 (ALL_IN).
| Jogador 8 | 0 | 40 |
- Jogador 8 · 2-3 · step 166: REROLL com 4g, HP 89, nível 4/8 (STABILIZE).
- Jogador 8 · 2-5 · step 210: REROLL com 7g, HP 83, nível 4/8 (STABILIZE).
- Jogador 8 · 2-5 · step 215: PASS com 5g, HP 83, nível 4/8 (STABILIZE).
- Jogador 8 · 2-6 · step 231: REROLL com 10g, HP 78, nível 5/8 (STABILIZE).
- Jogador 8 · 2-6 · step 234: REROLL com 8g, HP 78, nível 5/8 (STABILIZE).
- Jogador 8 · 2-6 · step 235: PASS com 6g, HP 78, nível 5/8 (STABILIZE).
- Jogador 8 · 2-7 · step 248: PASS com 11g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-1 · step 268: PASS com 18g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-2 · step 292: PASS com 26g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-3 · step 309: REROLL com 31g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-3 · step 311: REROLL com 28g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-3 · step 312: PASS com 26g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-4 · step 320: REROLL com 36g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-4 · step 325: REROLL com 32g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-4 · step 326: PASS com 30g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-5 · step 336: PASS com 41g, HP 72, nível 5/8 (STABILIZE).
- Jogador 8 · 3-6 · step 351: REROLL com 51g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 3-6 · step 353: REROLL com 48g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 3-6 · step 354: REROLL com 46g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 3-6 · step 357: PASS com 44g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 3-7 · step 367: REROLL com 50g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 3-7 · step 369: REROLL com 46g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 3-7 · step 372: PASS com 44g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 4-1 · step 381: REROLL com 55g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 4-1 · step 384: REROLL com 51g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 4-1 · step 386: PASS com 49g, HP 63, nível 5/8 (STABILIZE).
- Jogador 8 · 4-2 · step 393: PASS com 60g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 4-3 · step 405: PASS com 72g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 4-4 · step 416: PASS com 84g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 4-5 · step 425: PASS com 95g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 4-6 · step 440: PASS com 108g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 4-7 · step 449: PASS com 121g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 5-1 · step 461: PASS com 132g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 5-2 · step 472: PASS com 147g, HP 63, nível 6/8 (FAST8).
- Jogador 8 · 5-3 · step 480: PASS com 155g, HP 48, nível 6/8 (FAST8).
- Jogador 8 · 5-4 · step 488: PASS com 166g, HP 48, nível 6/8 (FAST8).
- Jogador 8 · 5-5 · step 497: PASS com 176g, HP 48, nível 6/8 (FAST8).
- Jogador 8 · 5-6 · step 508: PASS com 186g, HP 33, nível 6/8 (STABILIZE).
- Jogador 8 · 6-1 · step 528: PASS com 208g, HP 17, nível 6/8 (STABILIZE).
- Jogador 8 · 6-2 · step 538: PASS com 221g, HP 17, nível 6/8 (STABILIZE).

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 2 | 1 | 1 | 50.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 2 | 2 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 200 | 51 | 52 | 97 | 0.0027 | 0.0934 | 0.0016 | 0.3031 | 0.0011 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0181 (48 ações), CRAFT_AND_EQUIP: Δ 0.0000 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0072 (5 ações), MOVE_BENCH: Δ 0.0242 (46 ações), MOVE_BOARD: Δ -0.0063 (33 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ -0.0001 (34 ações), SELL: Δ 0.0600 (8 ações)
| Jogador 2 | 228 | 49 | 58 | 121 | 0.0004 | -0.2247 | -0.0011 | 0.3768 | 0.0014 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0009 (64 ações), CRAFT_AND_EQUIP: Δ 0.0195 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ -0.0343 (53 ações), MOVE_BOARD: Δ 0.0501 (25 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ -0.0060 (30 ações), SELL: Δ 0.0264 (24 ações)
| Jogador 3 | 294 | 77 | 69 | 148 | 0.0016 | 0.2742 | 0.0004 | 0.3361 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0232 (65 ações), CRAFT_AND_EQUIP: Δ 0.0098 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0007 (8 ações), MOVE_BENCH: Δ 0.0122 (87 ações), MOVE_BOARD: Δ 0.0006 (39 ações), PASS: Δ 0.0000 (36 ações), REROLL: Δ 0.0000 (29 ações), SELL: Δ 0.0361 (23 ações)
| Jogador 4 | 234 | 52 | 62 | 120 | -0.0011 | -0.0561 | -0.0018 | 0.1974 | 0.0007 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0309 (58 ações), CRAFT_AND_EQUIP: Δ 0.0069 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0230 (41 ações), MOVE_BOARD: Δ -0.0081 (36 ações), PASS: Δ 0.0000 (25 ações), REROLL: Δ 0.0000 (51 ações), SELL: Δ 0.0699 (12 ações)
| Jogador 5 | 249 | 54 | 53 | 142 | 0.0025 | 0.1712 | 0.0013 | 0.3104 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0290 (71 ações), CRAFT_AND_EQUIP: Δ 0.0148 (7 ações), MOVE_BENCH: Δ 0.0461 (38 ações), MOVE_BOARD: Δ -0.0069 (34 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ 0.0000 (48 ações), SELL: Δ 0.0380 (28 ações)
| Jogador 6 | 319 | 83 | 71 | 165 | 0.0006 | -0.0574 | -0.0007 | 0.3185 | 0.0013 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0416 (72 ações), BUY_XP: Δ 0.0000 (5 ações), CRAFT_AND_EQUIP: Δ 0.0058 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0064 (8 ações), MOVE_BENCH: Δ 0.0140 (88 ações), MOVE_BOARD: Δ 0.0227 (47 ações), PASS: Δ 0.0000 (36 ações), REROLL: Δ -0.0033 (33 ações), SELL: Δ 0.0394 (23 ações)
| Jogador 7 | 183 | 55 | 52 | 76 | 0.0014 | -0.1223 | -0.0002 | 0.3043 | 0.0016 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0370 (45 ações), CRAFT_AND_EQUIP: Δ 0.0196 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0120 (3 ações), MOVE_BENCH: Δ 0.0384 (51 ações), MOVE_BOARD: Δ -0.0211 (25 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ 0.0000 (26 ações), SELL: Δ 0.0514 (7 ações)
| Jogador 8 | 257 | 73 | 78 | 106 | 0.0027 | 0.1544 | 0.0011 | 0.2920 | 0.0017 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0336 (53 ações), CRAFT_AND_EQUIP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0061 (4 ações), MOVE_BENCH: Δ 0.0262 (88 ações), MOVE_BOARD: Δ -0.0156 (36 ações), PASS: Δ 0.0000 (33 ações), REROLL: Δ 0.0000 (17 ações), SELL: Δ 0.0375 (19 ações)
- Jogador 1 — rounds avaliados: 24; correlação estrutural/combate: 0.031; posicional/combate: -0.376.
- Jogador 1 — combate positive: score estrutural prévio 0.085
  score posicional prévio 0.247
- Jogador 1 — combate negative: score estrutural prévio 0.022
  score posicional prévio 0.330
- Jogador 2 — rounds avaliados: 28; correlação estrutural/combate: -0.188; posicional/combate: -0.000.
- Jogador 2 — combate positive: score estrutural prévio -0.307
  score posicional prévio 0.387
- Jogador 2 — combate negative: score estrutural prévio -0.139
  score posicional prévio 0.389
- Jogador 3 — rounds avaliados: 41; correlação estrutural/combate: 0.177; posicional/combate: 0.173.
- Jogador 3 — combate positive: score estrutural prévio 0.302
  score posicional prévio 0.353
- Jogador 3 — combate negative: score estrutural prévio 0.233
  score posicional prévio 0.340
- Jogador 4 — rounds avaliados: 27; correlação estrutural/combate: -0.334; posicional/combate: -0.031.
- Jogador 4 — combate positive: score estrutural prévio -0.266
  score posicional prévio 0.183
- Jogador 4 — combate negative: score estrutural prévio 0.033
  score posicional prévio 0.190
- Jogador 5 — rounds avaliados: 28; correlação estrutural/combate: -0.119; posicional/combate: -0.214.
- Jogador 5 — combate positive: score estrutural prévio 0.198
  score posicional prévio 0.294
- Jogador 5 — combate negative: score estrutural prévio 0.277
  score posicional prévio 0.361
- Jogador 6 — rounds avaliados: 41; correlação estrutural/combate: -0.112; posicional/combate: -0.254.
- Jogador 6 — combate positive: score estrutural prévio -0.085
  score posicional prévio 0.312
- Jogador 6 — combate negative: score estrutural prévio 0.034
  score posicional prévio 0.401
- Jogador 7 — rounds avaliados: 23; correlação estrutural/combate: -0.281; posicional/combate: -0.310.
- Jogador 7 — combate positive: score estrutural prévio -0.123
  score posicional prévio 0.300
- Jogador 7 — combate negative: score estrutural prévio -0.054
  score posicional prévio 0.333
- Jogador 8 — rounds avaliados: 34; correlação estrutural/combate: 0.077; posicional/combate: 0.074.
- Jogador 8 — combate positive: score estrutural prévio 0.320
  score posicional prévio 0.330
- Jogador 8 — combate negative: score estrutural prévio 0.281
  score posicional prévio 0.312

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 223 | OK (223) | 5 | 0 | 0 | 1 | 5 | 2 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_JeweledGauntlet, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 255 | OK (255) | 7 | 0 | 0 | 0 | 7 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_BrambleVest, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RabadonsDeathcap, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 335 | OK (335) | 9 | 0 | 0 | 0 | 9 | 2 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Deathblade, TFT_Item_GuinsoosRageblade, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 260 | OK (260) | 4 | 3 | 0 | 0 | 7 | 2 |
- Jogador 4 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_Leviathan, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 276 | OK (276) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 5 — IDs equipados observados: TFT_Item_GargoyleStoneplate, TFT_Item_JeweledGauntlet, TFT_Item_LastWhisper, TFT_Item_Leviathan, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 359 | OK (359) | 6 | 3 | 0 | 0 | 9 | 3 |
- Jogador 6 — IDs equipados observados: DA_18_EmblemRapidfire, DA_18_EmblemSpellweaver, TFT_Item_ArchangelsStaff, TFT_Item_Bloodthirster, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 205 | OK (205) | 5 | 0 | 0 | 1 | 5 | 2 |
- Jogador 7 — IDs equipados observados: TFT_Item_ArchangelsStaff, TFT_Item_IonicSpark, TFT_Item_NightHarvester, TFT_Item_SpectralGauntlet, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 290 | OK (290) | 8 | 0 | 0 | 0 | 8 | 1 |
- Jogador 8 — IDs equipados observados: DA_18_EmblemHunter, TFT_Item_AdaptiveHelm, TFT_Item_HextechGunblade, TFT_Item_IonicSpark, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 30.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 4); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.003 | 0.000 |
| Jogador 1 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 1 | 1-3 | 12 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.020 | 0.000 |
| Jogador 1 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.008 | 0.000 |
| Jogador 1 | 2-1 | 10 | 2.000 | 2.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 7 | 4 | 4 → 4 | -0.015 | 0.259 |
| Jogador 1 | 2-2 | 9 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 14% → 14% | 7 → 8 | 6 | 4 → 4 | -0.047 | 0.279 |
| Jogador 1 | 2-3 | 10 | 0.000 | 10.000 | 0 → 0 | 3 → 3 | 14% → 14% | 8 → 5 | 8 | 4 → 4 | -0.012 | -0.226 |
| Jogador 1 | 2-4 | 12 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 14% → 14% | 5 → 5 | 5 | 4 → 4 | -0.018 | 0.000 |
| Jogador 1 | 2-5 | 6 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 14% → 14% | 5 → 8 | 3 | 4 → 5 | 0.019 | -0.430 |
| Jogador 1 | 2-6 | 12 | 8.000 | -8.000 | 0 → 1 | 3 → 5 | 14% → 18% | 8 → 12 | 8 | 5 → 5 | 0.071 | -0.211 |
| Jogador 1 | 2-7 | 12 | -2.000 | 6.000 | 1 → 1 | 5 → 3 | 18% → 18% | 12 → 7 | 11 | 5 → 5 | -0.020 | 0.000 |
| Jogador 1 | 3-1 | 10 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 18% → 18% | 7 → 7 | 6 | 5 → 5 | 0.001 | 0.286 |
| Jogador 1 | 3-2 | 5 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 18% → 18% | 7 → 12 | 0 | 5 → 5 | 0.000 | -0.527 |
| Jogador 1 | 3-3 | 10 | 8.000 | -8.000 | 1 → 1 | 4 → 3 | 18% → 18% | 12 → 15 | 3 | 5 → 5 | 0.018 | -0.278 |
| Jogador 1 | 3-4 | 11 | 2.000 | 2.000 | 1 → 2 | 3 → 2 | 18% → 18% | 15 → 14 | 7 | 5 → 5 | 0.048 | 0.000 |
| Jogador 1 | 3-5 | 12 | 0.000 | -6.000 | 2 → 2 | 2 → 3 | 18% → 18% | 14 → 20 | 9 | 5 → 5 | -0.000 | 0.234 |
| Jogador 1 | 3-6 | 12 | -2.000 | 8.000 | 2 → 2 | 3 → 1 | 18% → 18% | 20 → 9 | 16 | 5 → 5 | -0.014 | -0.219 |
| Jogador 1 | 3-7 | 11 | 0.000 | 6.000 | 2 → 2 | 1 → 1 | 18% → 18% | 9 → 5 | 9 | 5 → 5 | -0.083 | 0.000 |
| Jogador 1 | 4-1 | 6 | 2.000 | -2.000 | 2 → 1 | 1 → 1 | 18% → 18% | 5 → 11 | 0 | 5 → 6 | 0.066 | -0.469 |
| Jogador 1 | 4-2 | 6 | 2.000 | -2.000 | 1 → 1 | 1 → 1 | 18% → 21% | 11 → 18 | 0 | 6 → 6 | 0.083 | -0.446 |
| Jogador 1 | 4-3 | 11 | 0.000 | 0.000 | 1 → 1 | 1 → 3 | 21% → 21% | 18 → 23 | 8 | 6 → 6 | 0.020 | -0.243 |
| Jogador 1 | 4-4 | 10 | -2.000 | 2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 23 → 20 | 13 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 11 | 2.000 | -8.000 | 1 → 2 | 3 → 1 | 21% → 21% | 20 → 21 | 12 | 6 → 6 | -0.090 | -0.231 |
| Jogador 1 | 4-6 | 8 | -26.000 | -30.000 | 2 → 0 | 1 → 0 | 21% → 0% | 21 → 20 | 1 | 6 → 6 | 0.002 | -0.341 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 15, PAIR_POTENTIAL: 15; mudanças de composição: 1; posicionamento melhorou em 55 ações e piorou em 54.
- Jogador 1 — estado final: ouro 20, nível 6, vida 9.0, colocação 7.
| Jogador 2 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.096 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.094 | 0.000 |
| Jogador 2 | 1-3 | 12 | 4.000 | 0.000 | 0 → 1 | 1 → 0 | 7% → 11% | 3 → 3 | 3 | 3 → 3 | 0.036 | 0.000 |
| Jogador 2 | 1-4 | 8 | 0.000 | 6.000 | 1 → 1 | 0 → 2 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.042 | 0.000 |
| Jogador 2 | 2-1 | 12 | 2.000 | 4.000 | 1 → 1 | 2 → 2 | 11% → 14% | 4 → 6 | 3 | 4 → 4 | -0.020 | -0.206 |
| Jogador 2 | 2-2 | 11 | 0.000 | 4.000 | 1 → 1 | 2 → 1 | 14% → 14% | 6 → 7 | 5 | 4 → 4 | 0.019 | -0.216 |
| Jogador 2 | 2-3 | 11 | 0.000 | 12.000 | 1 → 1 | 1 → 2 | 14% → 14% | 7 → 6 | 10 | 4 → 4 | -0.058 | 0.216 |
| Jogador 2 | 2-4 | 12 | 0.000 | 2.000 | 1 → 1 | 2 → 4 | 14% → 14% | 6 → 6 | 11 | 4 → 4 | 0.000 | 0.000 |
| Jogador 2 | 2-5 | 12 | 4.000 | -2.000 | 1 → 1 | 4 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 5 | 0.092 | -0.206 |
| Jogador 2 | 2-6 | 8 | 2.000 | 4.000 | 1 → 1 | 2 → 3 | 14% → 18% | 6 → 7 | 5 | 5 → 5 | -0.025 | -0.297 |
| Jogador 2 | 2-7 | 12 | 0.000 | -2.000 | 1 → 1 | 3 → 2 | 18% → 14% | 7 → 11 | 9 | 5 → 5 | 0.003 | 0.000 |
| Jogador 2 | 3-1 | 10 | 0.000 | -2.000 | 1 → 0 | 2 → 2 | 14% → 18% | 11 → 20 | 1 | 5 → 5 | -0.014 | -0.288 |
| Jogador 2 | 3-2 | 12 | 4.000 | 8.000 | 0 → 2 | 2 → 3 | 18% → 18% | 20 → 13 | 13 | 5 → 5 | 0.004 | -0.216 |
| Jogador 2 | 3-3 | 8 | -2.000 | -2.000 | 2 → 2 | 3 → 2 | 18% → 18% | 13 → 20 | 3 | 5 → 5 | 0.070 | -0.323 |
| Jogador 2 | 3-4 | 7 | 4.000 | 0.000 | 2 → 1 | 2 → 3 | 18% → 18% | 20 → 26 | 2 | 5 → 5 | -0.023 | 0.000 |
| Jogador 2 | 3-5 | 7 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 18% → 18% | 26 → 36 | 1 | 5 → 5 | 0.009 | 0.388 |
| Jogador 2 | 3-6 | 7 | -4.000 | 2.000 | 1 → 1 | 3 → 4 | 18% → 18% | 36 → 48 | 1 | 5 → 5 | -0.042 | 0.416 |
| Jogador 2 | 3-7 | 12 | 4.000 | 2.000 | 1 → 1 | 4 → 5 | 18% → 18% | 48 → 48 | 15 | 5 → 5 | 0.030 | 0.000 |
| Jogador 2 | 4-1 | 12 | -2.000 | 4.000 | 1 → 1 | 5 → 4 | 18% → 18% | 48 → 52 | 9 | 5 → 6 | 0.018 | -0.215 |
| Jogador 2 | 4-2 | 6 | 6.000 | -6.000 | 1 → 1 | 4 → 4 | 18% → 21% | 52 → 63 | 0 | 6 → 6 | -0.142 | 0.497 |
| Jogador 2 | 4-3 | 6 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 63 → 72 | 1 | 6 → 6 | 0.016 | -0.461 |
| Jogador 2 | 4-4 | 10 | -2.000 | 4.000 | 1 → 1 | 4 → 2 | 21% → 21% | 72 → 74 | 8 | 6 → 6 | 0.010 | 0.000 |
| Jogador 2 | 4-5 | 11 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 74 → 74 | 11 | 6 → 6 | -0.040 | 0.247 |
| Jogador 2 | 4-6 | 11 | 4.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 74 → 80 | 12 | 6 → 6 | 0.023 | 0.264 |
| Jogador 2 | 4-7 | 6 | -4.000 | 4.000 | 1 → 1 | 2 → 3 | 21% → 21% | 80 → 92 | 2 | 6 → 6 | 0.052 | 0.000 |
| Jogador 2 | 5-1 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 21% | 92 → 102 | 0 | 6 → 6 | -0.110 | -0.467 |
| Jogador 2 | 5-2 | 10 | 0.000 | -14.000 | 1 → 1 | 3 → 4 | 21% → 21% | 102 → 117 | 7 | 6 → 6 | 0.069 | 0.291 |
| Jogador 2 | 5-3 | 9 | -24.000 | -34.000 | 1 → 0 | 4 → 0 | 21% → 0% | 117 → 109 | 9 | 6 → 6 | -0.047 | -0.309 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 13, PAIR_POTENTIAL: 18; mudanças de composição: 0; posicionamento melhorou em 54 ações e piorou em 59.
- Jogador 2 — estado final: ouro 109, nível 6, vida 13.0, colocação 5.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 3 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.013 | 0.000 |
| Jogador 3 | 1-3 | 5 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.003 | 0.000 |
| Jogador 3 | 1-4 | 9 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.052 | 0.000 |
| Jogador 3 | 2-1 | 9 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 11% → 14% | 4 → 7 | 3 | 4 → 4 | -0.030 | 0.270 |
| Jogador 3 | 2-2 | 9 | 2.000 | 8.000 | 1 → 0 | 1 → 1 | 14% → 14% | 7 → 7 | 7 | 4 → 4 | -0.004 | 0.287 |
| Jogador 3 | 2-3 | 9 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 14% → 14% | 7 → 8 | 4 | 4 → 4 | 0.030 | -0.264 |
| Jogador 3 | 2-4 | 12 | 2.000 | 0.000 | 1 → 1 | 0 → 1 | 14% → 14% | 8 → 8 | 8 | 4 → 4 | 0.042 | 0.000 |
| Jogador 3 | 2-5 | 10 | 0.000 | 4.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 7 | 7 | 4 → 5 | -0.021 | 0.246 |
| Jogador 3 | 2-6 | 6 | 2.000 | -2.000 | 1 → 1 | 1 → 1 | 14% → 18% | 7 → 14 | 0 | 5 → 5 | -0.047 | 0.423 |
| Jogador 3 | 2-7 | 12 | 0.000 | 10.000 | 1 → 1 | 1 → 3 | 18% → 18% | 14 → 6 | 17 | 5 → 5 | -0.005 | 0.000 |
| Jogador 3 | 3-1 | 12 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 18% → 18% | 6 → 8 | 9 | 5 → 5 | -0.004 | 0.226 |
| Jogador 3 | 3-2 | 6 | 0.000 | 2.000 | 1 → 1 | 3 → 3 | 18% → 18% | 8 → 12 | 3 | 5 → 5 | -0.000 | 0.469 |
| Jogador 3 | 3-3 | 12 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 18% → 18% | 12 → 14 | 9 | 5 → 5 | -0.005 | -0.216 |
| Jogador 3 | 3-4 | 7 | 0.000 | 0.000 | 1 → 1 | 3 → 2 | 18% → 18% | 14 → 13 | 6 | 5 → 5 | 0.006 | 0.000 |
| Jogador 3 | 3-5 | 12 | 0.000 | 4.000 | 1 → 1 | 2 → 3 | 18% → 18% | 13 → 12 | 12 | 5 → 5 | 0.009 | 0.234 |
| Jogador 3 | 3-6 | 12 | -8.000 | 4.000 | 1 → 1 | 3 → 3 | 18% → 11% | 12 → 10 | 14 | 5 → 5 | -0.011 | -0.228 |
| Jogador 3 | 3-7 | 12 | 10.000 | -2.000 | 1 → 2 | 3 → 2 | 11% → 18% | 10 → 6 | 9 | 5 → 5 | -0.001 | 0.000 |
| Jogador 3 | 4-1 | 12 | 0.000 | 4.000 | 2 → 2 | 2 → 3 | 18% → 18% | 6 → 7 | 8 | 5 → 6 | 0.008 | 0.230 |
| Jogador 3 | 4-2 | 12 | 2.000 | -6.000 | 2 → 2 | 3 → 5 | 18% → 21% | 7 → 14 | 10 | 6 → 6 | 0.014 | 0.244 |
| Jogador 3 | 4-3 | 4 | 0.000 | 0.000 | 2 → 2 | 5 → 5 | 21% → 21% | 14 → 22 | 0 | 6 → 6 | -0.003 | 0.746 |
| Jogador 3 | 4-4 | 4 | 0.000 | 0.000 | 2 → 2 | 5 → 5 | 21% → 21% | 22 → 30 | 0 | 6 → 6 | 0.010 | 0.000 |
| Jogador 3 | 4-5 | 6 | 0.000 | 2.000 | 2 → 2 | 5 → 5 | 21% → 21% | 30 → 39 | 1 | 6 → 6 | 0.010 | 0.475 |
| Jogador 3 | 4-6 | 6 | 0.000 | 4.000 | 2 → 2 | 5 → 5 | 21% → 21% | 39 → 45 | 3 | 6 → 6 | 0.000 | -0.446 |
| Jogador 3 | 4-7 | 5 | 2.000 | -2.000 | 2 → 1 | 5 → 5 | 21% → 21% | 45 → 54 | 0 | 6 → 6 | 0.003 | 0.000 |
| Jogador 3 | 5-1 | 7 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 54 → 65 | 0 | 6 → 6 | 0.000 | 0.412 |
| Jogador 3 | 5-2 | 5 | 0.000 | 0.000 | 1 → 1 | 5 → 5 | 21% → 21% | 65 → 77 | 0 | 6 → 6 | -0.003 | 0.601 |
| Jogador 3 | 5-3 | 9 | 4.000 | -2.000 | 1 → 2 | 5 → 5 | 21% → 21% | 77 → 87 | 5 | 6 → 6 | 0.005 | 0.328 |
| Jogador 3 | 5-4 | 4 | 2.000 | -2.000 | 2 → 2 | 5 → 5 | 21% → 21% | 87 → 98 | 0 | 6 → 6 | 0.013 | 0.000 |
| Jogador 3 | 5-5 | 7 | -6.000 | 10.000 | 2 → 1 | 5 → 5 | 21% → 21% | 98 → 107 | 2 | 6 → 6 | -0.014 | 0.000 |
| Jogador 3 | 5-6 | 9 | 4.000 | -6.000 | 1 → 1 | 5 → 6 | 21% → 21% | 107 → 121 | 5 | 6 → 6 | 0.011 | 0.325 |
| Jogador 3 | 5-7 | 10 | -2.000 | 0.000 | 1 → 0 | 6 → 6 | 21% → 21% | 121 → 133 | 2 | 6 → 6 | -0.013 | 0.000 |
| Jogador 3 | 6-1 | 6 | 0.000 | 0.000 | 0 → 0 | 6 → 6 | 21% → 21% | 133 → 143 | 0 | 6 → 6 | -0.000 | -0.458 |
| Jogador 3 | 6-2 | 5 | -2.000 | 2.000 | 0 → 1 | 6 → 6 | 21% → 21% | 143 → 154 | 0 | 6 → 6 | 0.022 | 0.587 |
| Jogador 3 | 6-3 | 10 | 2.000 | -2.000 | 1 → 0 | 6 → 7 | 21% → 21% | 154 → 167 | 2 | 6 → 6 | -0.004 | 0.294 |
| Jogador 3 | 6-4 | 10 | 0.000 | 0.000 | 0 → 0 | 7 → 6 | 21% → 21% | 167 → 178 | 1 | 6 → 6 | -0.001 | 0.000 |
| Jogador 3 | 6-5 | 8 | -2.000 | 2.000 | 0 → 0 | 6 → 6 | 21% → 21% | 178 → 190 | 0 | 6 → 7 | 0.004 | 0.375 |
| Jogador 3 | 6-6 | 6 | 6.000 | -4.000 | 0 → 0 | 6 → 7 | 21% → 25% | 190 → 201 | 1 | 7 → 7 | -0.009 | 0.499 |
| Jogador 3 | 6-7 | 8 | 0.000 | 2.000 | 0 → 0 | 7 → 6 | 25% → 25% | 201 → 209 | 4 | 7 → 7 | -0.009 | 0.000 |
| Jogador 3 | 7-1 | 10 | 4.000 | -4.000 | 0 → 1 | 6 → 4 | 25% → 25% | 209 → 217 | 5 | 7 → 7 | -0.003 | 0.308 |
| Jogador 3 | 7-2 | 6 | 0.000 | 14.000 | 1 → 1 | 4 → 4 | 25% → 25% | 217 → 211 | 7 | 7 → 7 | -0.008 | 0.514 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 14, PAIR_POTENTIAL: 22; mudanças de composição: 0; posicionamento melhorou em 82 ações e piorou em 70.
- Jogador 3 — estado final: ouro 211, nível 7, vida 47.0, colocação 1.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 4 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.016 | 0.000 |
| Jogador 4 | 1-3 | 12 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.031 | 0.000 |
| Jogador 4 | 1-4 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.014 | 0.000 |
| Jogador 4 | 2-1 | 12 | 2.000 | 2.000 | 0 → 0 | 2 → 4 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.004 | -0.202 |
| Jogador 4 | 2-2 | 9 | 0.000 | 4.000 | 0 → 0 | 4 → 2 | 14% → 14% | 5 → 7 | 4 | 4 → 4 | -0.037 | -0.281 |
| Jogador 4 | 2-3 | 12 | 0.000 | 6.000 | 0 → 0 | 2 → 4 | 14% → 14% | 7 → 6 | 10 | 4 → 4 | -0.016 | 0.211 |
| Jogador 4 | 2-4 | 12 | 2.000 | 2.000 | 0 → 0 | 4 → 5 | 14% → 14% | 6 → 5 | 9 | 4 → 4 | 0.009 | 0.000 |
| Jogador 4 | 2-5 | 12 | 0.000 | 2.000 | 0 → 0 | 5 → 3 | 14% → 14% | 5 → 9 | 9 | 4 → 5 | -0.032 | 0.202 |
| Jogador 4 | 2-6 | 6 | 2.000 | 2.000 | 0 → 0 | 3 → 3 | 14% → 18% | 9 → 14 | 2 | 5 → 5 | 0.006 | 0.451 |
| Jogador 4 | 2-7 | 9 | 2.000 | -2.000 | 0 → 1 | 3 → 2 | 18% → 18% | 14 → 20 | 1 | 5 → 5 | -0.023 | 0.000 |
| Jogador 4 | 3-1 | 12 | 4.000 | 2.000 | 1 → 2 | 2 → 3 | 18% → 18% | 20 → 18 | 8 | 5 → 5 | 0.047 | -0.211 |
| Jogador 4 | 3-2 | 12 | 0.000 | -4.000 | 2 → 2 | 3 → 4 | 18% → 18% | 18 → 19 | 12 | 5 → 5 | 0.010 | 0.238 |
| Jogador 4 | 3-3 | 10 | 0.000 | 0.000 | 2 → 1 | 4 → 3 | 18% → 18% | 19 → 18 | 9 | 5 → 5 | -0.002 | 0.277 |
| Jogador 4 | 3-4 | 12 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 18% → 18% | 18 → 6 | 18 | 5 → 5 | -0.006 | 0.000 |
| Jogador 4 | 3-5 | 10 | -2.000 | 4.000 | 1 → 1 | 3 → 2 | 18% → 18% | 6 → 6 | 5 | 5 → 5 | 0.023 | -0.263 |
| Jogador 4 | 3-6 | 7 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 6 | 6 | 5 → 5 | -0.011 | -0.383 |
| Jogador 4 | 3-7 | 12 | -4.000 | 4.000 | 1 → 2 | 2 → 1 | 18% → 14% | 6 → 6 | 9 | 5 → 5 | -0.018 | 0.000 |
| Jogador 4 | 4-1 | 12 | 8.000 | -10.000 | 2 → 3 | 1 → 3 | 14% → 18% | 6 → 13 | 7 | 5 → 6 | 0.021 | -0.211 |
| Jogador 4 | 4-2 | 6 | 4.000 | -4.000 | 3 → 3 | 3 → 3 | 18% → 21% | 13 → 20 | 0 | 6 → 6 | 0.003 | -0.461 |
| Jogador 4 | 4-3 | 11 | 0.000 | 8.000 | 3 → 3 | 3 → 5 | 21% → 21% | 20 → 6 | 20 | 6 → 6 | 0.000 | 0.259 |
| Jogador 4 | 4-4 | 9 | 0.000 | 0.000 | 3 → 3 | 5 → 5 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | 0.015 | 0.000 |
| Jogador 4 | 4-5 | 8 | 0.000 | 0.000 | 3 → 3 | 5 → 5 | 21% → 21% | 7 → 6 | 6 | 6 → 6 | 0.055 | -0.334 |
| Jogador 4 | 4-6 | 11 | 8.000 | -12.000 | 3 → 4 | 5 → 3 | 21% → 21% | 6 → 7 | 7 | 6 → 6 | -0.021 | -0.247 |
| Jogador 4 | 4-7 | 9 | 0.000 | 6.000 | 4 → 4 | 3 → 2 | 21% → 21% | 7 → 7 | 6 | 6 → 6 | 0.036 | 0.000 |
| Jogador 4 | 5-1 | 10 | 0.000 | 4.000 | 4 → 4 | 2 → 1 | 21% → 21% | 7 → 6 | 7 | 6 → 6 | -0.096 | -0.278 |
| Jogador 4 | 5-2 | 7 | -32.000 | -28.000 | 4 → 0 | 1 → 0 | 21% → 0% | 6 → 1 | 5 | 6 → 6 | 0.011 | -0.407 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 16, PAIR_POTENTIAL: 18; mudanças de composição: 1; posicionamento melhorou em 57 ações e piorou em 62.
- Jogador 4 — estado final: ouro 1, nível 6, vida 1.0, colocação 6.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.006 | 0.000 |
| Jogador 5 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.002 | 0.000 |
| Jogador 5 | 1-3 | 12 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.020 | 0.000 |
| Jogador 5 | 1-4 | 9 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.055 | 0.000 |
| Jogador 5 | 2-1 | 11 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | 0.006 | 0.237 |
| Jogador 5 | 2-2 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 3 | 14% → 14% | 6 → 8 | 6 | 4 → 4 | 0.007 | 0.269 |
| Jogador 5 | 2-3 | 12 | -2.000 | 2.000 | 0 → 0 | 3 → 3 | 14% → 11% | 8 → 9 | 9 | 4 → 4 | -0.014 | 0.209 |
| Jogador 5 | 2-4 | 12 | 4.000 | 6.000 | 0 → 1 | 3 → 3 | 11% → 14% | 9 → 6 | 12 | 4 → 4 | 0.006 | 0.000 |
| Jogador 5 | 2-5 | 12 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 14% → 14% | 6 → 11 | 9 | 4 → 5 | 0.004 | 0.218 |
| Jogador 5 | 2-6 | 12 | 2.000 | 8.000 | 1 → 1 | 4 → 4 | 14% → 18% | 11 → 8 | 13 | 5 → 5 | -0.013 | 0.238 |
| Jogador 5 | 2-7 | 12 | 2.000 | -2.000 | 1 → 1 | 4 → 3 | 18% → 18% | 8 → 9 | 8 | 5 → 5 | -0.000 | 0.000 |
| Jogador 5 | 3-1 | 12 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 18% → 18% | 9 → 8 | 12 | 5 → 5 | 0.012 | -0.211 |
| Jogador 5 | 3-2 | 12 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 18% → 18% | 8 → 6 | 11 | 5 → 5 | 0.033 | -0.224 |
| Jogador 5 | 3-3 | 12 | 0.000 | -2.000 | 1 → 1 | 4 → 3 | 18% → 18% | 6 → 7 | 8 | 5 → 5 | 0.004 | 0.231 |
| Jogador 5 | 3-4 | 12 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 18% → 18% | 7 → 5 | 13 | 5 → 5 | 0.010 | 0.000 |
| Jogador 5 | 3-5 | 8 | 0.000 | 4.000 | 1 → 1 | 4 → 5 | 18% → 18% | 5 → 6 | 4 | 5 → 5 | -0.000 | -0.347 |
| Jogador 5 | 3-6 | 12 | 8.000 | -14.000 | 1 → 1 | 5 → 4 | 18% → 18% | 6 → 10 | 7 | 5 → 5 | -0.014 | 0.234 |
| Jogador 5 | 3-7 | 4 | -4.000 | 4.000 | 1 → 1 | 4 → 4 | 18% → 18% | 10 → 16 | 0 | 5 → 5 | 0.013 | 0.000 |
| Jogador 5 | 4-1 | 10 | 4.000 | -4.000 | 1 → 2 | 4 → 3 | 18% → 18% | 16 → 18 | 4 | 5 → 6 | -0.030 | -0.268 |
| Jogador 5 | 4-2 | 6 | 12.000 | -12.000 | 2 → 3 | 3 → 3 | 18% → 21% | 18 → 25 | 0 | 6 → 6 | 0.028 | -0.469 |
| Jogador 5 | 4-3 | 8 | 2.000 | -2.000 | 3 → 4 | 3 → 2 | 21% → 21% | 25 → 32 | 1 | 6 → 6 | -0.007 | -0.352 |
| Jogador 5 | 4-4 | 10 | 0.000 | 8.000 | 4 → 4 | 2 → 2 | 21% → 21% | 32 → 21 | 18 | 6 → 6 | -0.006 | 0.000 |
| Jogador 5 | 4-5 | 11 | 4.000 | -4.000 | 4 → 5 | 2 → 0 | 21% → 21% | 21 → 16 | 12 | 6 → 6 | 0.024 | 0.264 |
| Jogador 5 | 4-6 | 11 | 0.000 | 8.000 | 5 → 5 | 0 → 1 | 21% → 21% | 16 → 7 | 16 | 6 → 6 | 0.000 | 0.259 |
| Jogador 5 | 4-7 | 7 | 0.000 | 6.000 | 5 → 5 | 1 → 1 | 21% → 21% | 7 → 6 | 7 | 6 → 6 | -0.001 | 0.000 |
| Jogador 5 | 5-1 | 9 | 0.000 | 6.000 | 5 → 5 | 1 → 2 | 21% → 21% | 6 → 6 | 5 | 6 → 6 | 0.012 | -0.304 |
| Jogador 5 | 5-2 | 10 | 0.000 | 4.000 | 5 → 5 | 2 → 3 | 21% → 21% | 6 → 7 | 8 | 6 → 6 | -0.028 | -0.275 |
| Jogador 5 | 5-3 | 9 | -40.000 | -44.000 | 5 → 0 | 3 → 0 | 21% → 0% | 7 → 12 | 8 | 6 → 6 | -0.066 | -0.311 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 16, PAIR_POTENTIAL: 22; mudanças de composição: 0; posicionamento melhorou em 58 ações e piorou em 54.
- Jogador 5 — estado final: ouro 12, nível 6, vida 8.0, colocação 4.
| Jogador 6 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.098 | 0.000 |
| Jogador 6 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.023 | 0.000 |
| Jogador 6 | 1-3 | 5 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 6 | 1-4 | 9 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.059 | 0.000 |
| Jogador 6 | 2-1 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 4 | 11% → 14% | 4 → 6 | 3 | 4 → 4 | -0.011 | -0.231 |
| Jogador 6 | 2-2 | 12 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 14% → 14% | 6 → 8 | 9 | 4 → 4 | -0.007 | 0.224 |
| Jogador 6 | 2-3 | 12 | 8.000 | -2.000 | 0 → 2 | 4 → 2 | 14% → 14% | 8 → 8 | 7 | 4 → 4 | 0.029 | 0.209 |
| Jogador 6 | 2-4 | 12 | 0.000 | 12.000 | 2 → 2 | 2 → 2 | 14% → 14% | 8 → 7 | 7 | 4 → 4 | -0.022 | 0.000 |
| Jogador 6 | 2-5 | 12 | 4.000 | 2.000 | 2 → 1 | 2 → 4 | 14% → 14% | 7 → 8 | 9 | 4 → 5 | 0.006 | 0.228 |
| Jogador 6 | 2-6 | 11 | 4.000 | 2.000 | 1 → 1 | 4 → 4 | 14% → 18% | 8 → 8 | 7 | 5 → 5 | 0.027 | 0.235 |
| Jogador 6 | 2-7 | 12 | 6.000 | 4.000 | 1 → 1 | 4 → 3 | 18% → 18% | 8 → 6 | 8 | 5 → 5 | 0.060 | 0.000 |
| Jogador 6 | 3-1 | 12 | 0.000 | -10.000 | 1 → 1 | 3 → 4 | 18% → 18% | 6 → 16 | 9 | 5 → 5 | 0.015 | 0.254 |
| Jogador 6 | 3-2 | 12 | -10.000 | 10.000 | 1 → 1 | 4 → 3 | 18% → 14% | 16 → 16 | 12 | 5 → 5 | -0.029 | 0.238 |
| Jogador 6 | 3-3 | 12 | 2.000 | -4.000 | 1 → 1 | 3 → 5 | 14% → 18% | 16 → 25 | 10 | 5 → 5 | 0.011 | 0.246 |
| Jogador 6 | 3-4 | 12 | 0.000 | 4.000 | 1 → 1 | 5 → 4 | 18% → 18% | 25 → 22 | 14 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 3-5 | 12 | 2.000 | 4.000 | 1 → 1 | 4 → 3 | 18% → 18% | 22 → 21 | 13 | 5 → 5 | -0.013 | 0.246 |
| Jogador 6 | 3-6 | 12 | 0.000 | 6.000 | 1 → 1 | 3 → 5 | 18% → 18% | 21 → 22 | 15 | 5 → 5 | 0.010 | 0.243 |
| Jogador 6 | 3-7 | 12 | -4.000 | 0.000 | 1 → 1 | 5 → 2 | 18% → 14% | 22 → 22 | 13 | 5 → 5 | -0.017 | 0.000 |
| Jogador 6 | 4-1 | 12 | 2.000 | 10.000 | 1 → 1 | 2 → 5 | 14% → 18% | 22 → 23 | 12 | 5 → 6 | 0.012 | 0.249 |
| Jogador 6 | 4-2 | 6 | 4.000 | -4.000 | 1 → 0 | 5 → 5 | 18% → 21% | 23 → 32 | 2 | 6 → 6 | -0.117 | 0.467 |
| Jogador 6 | 4-3 | 7 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 21% → 21% | 32 → 44 | 0 | 6 → 6 | 0.150 | 0.419 |
| Jogador 6 | 4-4 | 7 | 6.000 | -6.000 | 0 → 1 | 5 → 4 | 21% → 21% | 44 → 55 | 1 | 6 → 6 | 0.005 | 0.000 |
| Jogador 6 | 4-5 | 5 | 0.000 | 4.000 | 1 → 1 | 4 → 4 | 21% → 21% | 55 → 63 | 2 | 6 → 6 | 0.015 | -0.550 |
| Jogador 6 | 4-6 | 11 | 0.000 | -2.000 | 1 → 0 | 4 → 4 | 21% → 21% | 63 → 63 | 13 | 6 → 6 | -0.004 | 0.000 |
| Jogador 6 | 4-7 | 6 | 0.000 | 0.000 | 0 → 0 | 4 → 3 | 21% → 21% | 63 → 72 | 1 | 6 → 6 | -0.105 | 0.000 |
| Jogador 6 | 5-1 | 7 | -4.000 | 8.000 | 0 → 0 | 3 → 3 | 21% → 21% | 72 → 81 | 2 | 6 → 6 | -0.010 | 0.419 |
| Jogador 6 | 5-2 | 10 | 4.000 | -4.000 | 0 → 0 | 3 → 4 | 21% → 21% | 81 → 86 | 10 | 6 → 7 | 0.017 | 0.296 |
| Jogador 6 | 5-3 | 6 | 4.000 | -2.000 | 0 → 0 | 4 → 4 | 21% → 25% | 86 → 96 | 1 | 7 → 7 | -0.012 | 0.000 |
| Jogador 6 | 5-4 | 4 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 96 → 107 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-5 | 5 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 107 → 119 | 0 | 7 → 7 | 0.046 | 0.581 |
| Jogador 6 | 5-6 | 6 | 4.000 | -4.000 | 0 → 1 | 4 → 3 | 25% → 25% | 119 → 128 | 2 | 7 → 7 | 0.004 | 0.000 |
| Jogador 6 | 5-7 | 5 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 128 → 138 | 1 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 6-1 | 9 | -6.000 | 8.000 | 1 → 1 | 4 → 3 | 25% → 25% | 138 → 145 | 7 | 7 → 7 | 0.008 | 0.000 |
| Jogador 6 | 6-2 | 10 | -4.000 | 8.000 | 1 → 1 | 3 → 2 | 25% → 25% | 145 → 151 | 5 | 7 → 7 | -0.012 | 0.000 |
| Jogador 6 | 6-3 | 7 | 4.000 | 4.000 | 1 → 1 | 2 → 2 | 25% → 25% | 151 → 157 | 4 | 7 → 7 | 0.005 | -0.393 |
| Jogador 6 | 6-4 | 6 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 157 → 167 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 6-5 | 5 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 167 → 178 | 0 | 7 → 7 | 0.000 | -0.560 |
| Jogador 6 | 6-6 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 178 → 189 | 0 | 7 → 7 | -0.005 | -0.280 |
| Jogador 6 | 6-7 | 6 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 189 → 200 | 0 | 7 → 7 | 0.004 | 0.000 |
| Jogador 6 | 7-1 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 200 → 211 | 0 | 7 → 7 | 0.002 | -0.285 |
| Jogador 6 | 7-2 | 8 | -34.000 | -64.000 | 1 → 0 | 2 → 0 | 25% → 0% | 211 → 211 | 0 | 7 → 7 | -0.066 | -0.356 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 26, IMMEDIATE_UPGRADE: 17, PAIR_POTENTIAL: 23; mudanças de composição: 0; posicionamento melhorou em 89 ações e piorou em 74.
- Jogador 6 — estado final: ouro 211, nível 7, vida 6.0, colocação 2.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.000 | 0.000 |
| Jogador 7 | 1-3 | 8 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.071 | 0.000 |
| Jogador 7 | 1-4 | 9 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.037 | 0.000 |
| Jogador 7 | 2-1 | 12 | 4.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 5 → 6 | 6 | 4 → 4 | 0.009 | 0.214 |
| Jogador 7 | 2-2 | 7 | 0.000 | 2.000 | 0 → 1 | 2 → 1 | 14% → 14% | 6 → 9 | 2 | 4 → 4 | 0.029 | -0.347 |
| Jogador 7 | 2-3 | 6 | 2.000 | 4.000 | 1 → 1 | 1 → 1 | 14% → 14% | 9 → 12 | 3 | 4 → 4 | -0.027 | -0.395 |
| Jogador 7 | 2-4 | 12 | -2.000 | 14.000 | 1 → 1 | 1 → 2 | 14% → 14% | 12 → 6 | 12 | 4 → 4 | -0.010 | 0.000 |
| Jogador 7 | 2-5 | 12 | 2.000 | 4.000 | 1 → 1 | 2 → 3 | 14% → 14% | 6 → 6 | 6 | 4 → 5 | 0.036 | -0.193 |
| Jogador 7 | 2-6 | 6 | 4.000 | -4.000 | 1 → 1 | 3 → 2 | 14% → 14% | 6 → 11 | 1 | 5 → 5 | 0.002 | -0.448 |
| Jogador 7 | 2-7 | 6 | 2.000 | -2.000 | 1 → 1 | 2 → 2 | 14% → 18% | 11 → 18 | 0 | 5 → 5 | 0.004 | 0.000 |
| Jogador 7 | 3-1 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 18% → 18% | 18 → 23 | 3 | 5 → 5 | -0.003 | -0.447 |
| Jogador 7 | 3-2 | 11 | 6.000 | 0.000 | 1 → 2 | 3 → 2 | 18% → 18% | 23 → 26 | 6 | 5 → 5 | 0.008 | -0.244 |
| Jogador 7 | 3-3 | 12 | 0.000 | 6.000 | 2 → 2 | 2 → 0 | 18% → 14% | 26 → 25 | 10 | 5 → 5 | -0.025 | -0.235 |
| Jogador 7 | 3-4 | 12 | 4.000 | -4.000 | 2 → 3 | 0 → 1 | 14% → 18% | 25 → 30 | 10 | 5 → 5 | 0.015 | 0.000 |
| Jogador 7 | 3-5 | 12 | -2.000 | -2.000 | 3 → 2 | 1 → 1 | 18% → 18% | 30 → 39 | 4 | 5 → 5 | 0.009 | -0.219 |
| Jogador 7 | 3-6 | 9 | 0.000 | 2.000 | 2 → 2 | 1 → 2 | 18% → 18% | 39 → 43 | 7 | 5 → 5 | -0.001 | -0.304 |
| Jogador 7 | 3-7 | 5 | 2.000 | -2.000 | 2 → 3 | 2 → 2 | 18% → 18% | 43 → 55 | 0 | 5 → 5 | 0.027 | 0.000 |
| Jogador 7 | 4-1 | 12 | 0.000 | -8.000 | 3 → 3 | 2 → 1 | 18% → 18% | 55 → 66 | 5 | 5 → 6 | 0.003 | 0.226 |
| Jogador 7 | 4-2 | 8 | 2.000 | 2.000 | 3 → 3 | 1 → 2 | 18% → 21% | 66 → 72 | 4 | 6 → 6 | 0.010 | -0.328 |
| Jogador 7 | 4-3 | 8 | 0.000 | -2.000 | 3 → 3 | 2 → 2 | 21% → 21% | 72 → 82 | 4 | 6 → 6 | -0.019 | -0.339 |
| Jogador 7 | 4-4 | 10 | 4.000 | 0.000 | 3 → 3 | 2 → 1 | 21% → 21% | 82 → 81 | 12 | 6 → 6 | -0.013 | 0.000 |
| Jogador 7 | 4-5 | 11 | -34.000 | -24.000 | 3 → 0 | 1 → 0 | 21% → 0% | 81 → 72 | 15 | 6 → 6 | -0.029 | -0.248 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 16, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 60 ações e piorou em 53.
- Jogador 7 — estado final: ouro 72, nível 6, vida 4.0, colocação 8.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.007 | 0.000 |
| Jogador 8 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.004 | 0.000 |
| Jogador 8 | 1-3 | 9 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.062 | 0.000 |
| Jogador 8 | 1-4 | 9 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.037 | 0.000 |
| Jogador 8 | 2-1 | 10 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 4 → 6 | 3 | 4 → 4 | -0.035 | -0.242 |
| Jogador 8 | 2-2 | 12 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 14% → 14% | 6 → 7 | 8 | 4 → 4 | 0.089 | -0.211 |
| Jogador 8 | 2-3 | 11 | 2.000 | 4.000 | 0 → 1 | 1 → 0 | 14% → 14% | 7 → 7 | 6 | 4 → 4 | -0.018 | -0.216 |
| Jogador 8 | 2-4 | 8 | 0.000 | 10.000 | 1 → 1 | 0 → 2 | 14% → 14% | 7 → 6 | 7 | 4 → 4 | -0.010 | 0.000 |
| Jogador 8 | 2-5 | 12 | 2.000 | -2.000 | 1 → 1 | 2 → 2 | 14% → 14% | 6 → 11 | 7 | 4 → 5 | 0.040 | -0.193 |
| Jogador 8 | 2-6 | 12 | 2.000 | 0.000 | 1 → 1 | 2 → 3 | 14% → 18% | 11 → 13 | 6 | 5 → 5 | 0.023 | -0.202 |
| Jogador 8 | 2-7 | 7 | 0.000 | 4.000 | 1 → 1 | 3 → 3 | 18% → 18% | 13 → 19 | 3 | 5 → 5 | -0.126 | 0.000 |
| Jogador 8 | 3-1 | 8 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 18% → 18% | 19 → 25 | 2 | 5 → 5 | 0.110 | 0.340 |
| Jogador 8 | 3-2 | 12 | 2.000 | -6.000 | 1 → 1 | 4 → 3 | 18% → 18% | 25 → 35 | 1 | 5 → 5 | -0.031 | 0.231 |
| Jogador 8 | 3-3 | 12 | 4.000 | 4.000 | 1 → 2 | 3 → 3 | 18% → 18% | 35 → 35 | 9 | 5 → 5 | -0.018 | 0.250 |
| Jogador 8 | 3-4 | 12 | 0.000 | 4.000 | 2 → 2 | 3 → 4 | 18% → 18% | 35 → 39 | 9 | 5 → 5 | 0.011 | 0.000 |
| Jogador 8 | 3-5 | 6 | -4.000 | 0.000 | 2 → 2 | 4 → 4 | 18% → 18% | 39 → 50 | 1 | 5 → 5 | 0.103 | -0.423 |
| Jogador 8 | 3-6 | 12 | 4.000 | -6.000 | 2 → 2 | 4 → 3 | 18% → 18% | 50 → 54 | 9 | 5 → 5 | -0.041 | 0.238 |
| Jogador 8 | 3-7 | 12 | 2.000 | 6.000 | 2 → 3 | 3 → 3 | 18% → 18% | 54 → 53 | 10 | 5 → 5 | -0.013 | 0.000 |
| Jogador 8 | 4-1 | 12 | -2.000 | 2.000 | 3 → 2 | 3 → 3 | 18% → 18% | 53 → 61 | 7 | 5 → 6 | 0.000 | 0.238 |
| Jogador 8 | 4-2 | 7 | 8.000 | -6.000 | 2 → 3 | 3 → 3 | 18% → 21% | 61 → 72 | 1 | 6 → 6 | 0.007 | 0.407 |
| Jogador 8 | 4-3 | 5 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 72 → 84 | 0 | 6 → 6 | 0.020 | 0.577 |
| Jogador 8 | 4-4 | 5 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 84 → 95 | 0 | 6 → 6 | 0.013 | 0.000 |
| Jogador 8 | 4-5 | 4 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 95 → 108 | 0 | 6 → 6 | -0.002 | 0.728 |
| Jogador 8 | 4-6 | 8 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 108 → 122 | 4 | 6 → 6 | 0.013 | 0.360 |
| Jogador 8 | 4-7 | 6 | 0.000 | 2.000 | 3 → 3 | 3 → 3 | 21% → 21% | 122 → 134 | 1 | 6 → 6 | -0.002 | 0.000 |
| Jogador 8 | 5-1 | 8 | 0.000 | 4.000 | 3 → 3 | 3 → 4 | 21% → 21% | 134 → 146 | 2 | 6 → 6 | 0.000 | 0.369 |
| Jogador 8 | 5-2 | 9 | 0.000 | -2.000 | 3 → 3 | 4 → 3 | 21% → 21% | 146 → 157 | 2 | 6 → 6 | -0.002 | -0.311 |
| Jogador 8 | 5-3 | 7 | 0.000 | 4.000 | 3 → 3 | 3 → 3 | 21% → 21% | 157 → 166 | 2 | 6 → 6 | 0.000 | 0.419 |
| Jogador 8 | 5-4 | 6 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 166 → 176 | 0 | 6 → 6 | -0.000 | 0.000 |
| Jogador 8 | 5-5 | 5 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 176 → 186 | 0 | 6 → 6 | -0.000 | -0.550 |
| Jogador 8 | 5-6 | 7 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 186 → 197 | 0 | 6 → 6 | 0.002 | -0.393 |
| Jogador 8 | 5-7 | 10 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 197 → 208 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 8 | 0.000 | 0.000 | 3 → 3 | 3 → 3 | 21% → 21% | 208 → 219 | 0 | 6 → 6 | 0.000 | 0.368 |
| Jogador 8 | 6-2 | 8 | -30.000 | -40.000 | 3 → 0 | 3 → 0 | 21% → 0% | 219 → 221 | 1 | 6 → 6 | -0.095 | -0.344 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 10, PAIR_POTENTIAL: 13; mudanças de composição: 1; posicionamento melhorou em 77 ações e piorou em 79.
- Jogador 8 — estado final: ouro 221, nível 6, vida 17.0, colocação 3.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 48 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 2 | 64 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Jogador 3 | 65 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 4 | 58 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 5 | 71 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 |
| Jogador 6 | 72 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 0 |
| Jogador 7 | 45 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jogador 8 | 53 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 |
- Jogador 1 — venda DA_18_Akali_AD (2-6, step 229): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Ornn (2-6, step 234): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Xayah (4-3, step 404): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_RekSai (2-7, step 247): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Kobuko (3-5, step 333): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 2 — venda DA_18_Veigar (4-1, step 385): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_18_Xayah (4-6, step 436): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 2 — venda DA_Cinderling18 (4-7, step 445): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 3 — venda DA_18_Diana (4-2, step 388): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Akali_AD (4-2, step 392): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Akali_AD (5-3, step 475): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_Scuttlecrab18 (5-6, step 506): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Hecarim (5-7, step 512): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Akali_AD (6-3, step 544): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_Camille (6-4, step 553): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Xayah (3-2, step 290): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_18_Akali_AD (4-1, step 380): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 5 — venda DA_18_Kobuko (2-5, step 206): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (2-6, step 233): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (2-7, step 246): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Leona (3-1, step 269): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-2, step 286): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_RekSai (3-3, step 308): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Yunara (3-4, step 320): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Kayle (3-6, step 347): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 5 — venda DA_18_Azir (5-3, step 475): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Teemo (3-1, step 271): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Camille (3-2, step 287): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 6 — venda DA_KogMaw18_AD (3-3, step 303): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Camille (3-4, step 321): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Akali_AD (3-6, step 355): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Sejuani (4-1, step 381): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 7 — venda DA_18_Yorick (4-3, step 404): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 7 — venda DA_18_Varus (4-5, step 431): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Veigar (2-5, step 205): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Rakan (3-4, step 317): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Kobuko (4-6, step 434): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_18_Veigar (5-2, step 465): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_RekSai (6-2, step 532): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.

Vendas de core/pares ignoradas antes da decisão da composição: **8**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-6 | 229 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 1 | 2-6 | 234 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 4-3 | 404 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Xayah' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 2-2 | 665 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 2-4 | 960 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 2-5 | 1045 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 2-7 | 1363 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1861 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 2022 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 2328 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 3-7 | 2329 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 2419 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 2508 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 2802 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 2952 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 4-5 | 2953 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 3066 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 4-6 | 3067 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 1 | 3-4 | 1999 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 2 | 2-7 | 247 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-1 | 385 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-6 | 436 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Xayah' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 1-2 | 115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-3 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-4 | 380 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 2-1 | 542 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-2 | 687 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-3 | 841 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-4 | 999 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-5 | 1158 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 2-6 | 1271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 3-2 | 1741 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-2 | 2553 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 2643 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-3 | 2644 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-4 | 2777 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-4 | 2778 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-5 | 2934 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 2935 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-6 | 3084 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-6 | 3085 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 4-7 | 3173 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-7 | 3174 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-1 | 3264 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-1 | 3265 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-2 | 3403 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 5-2 | 3404 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 2 | 5-3 | 3534 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 5-3 | 3535 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 2 | 2-7 | 1538 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-2 | 1832 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-3 | 1930 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-4 | 2031 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-5 | 2130 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-6 | 2288 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 3-7 | 2446 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-6 | 3150 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 2 | 4-7 | 3241 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 3 | 4-2 | 388 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 4-2 | 392 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-6 | 506 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-7 | 512 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 3 | 6-3 | 544 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 1-3 | 234 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-3 | 715 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-5 | 1010 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-6 | 1093 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 2-7 | 1252 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-1 | 1413 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-2 | 1501 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-3 | 1663 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-4 | 1762 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-5 | 1923 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-6 | 2086 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 3-7 | 2245 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-1 | 2409 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-2 | 2571 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-3 | 2633 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-5 | 2782 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-6 | 2871 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 4-7 | 2943 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-1 | 3045 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-2 | 3122 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-3 | 3245 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-4 | 3310 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-5 | 3411 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-6 | 3539 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 5-7 | 3683 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-1 | 3775 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-2 | 3852 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-3 | 4000 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-4 | 4143 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-5 | 4260 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-6 | 4350 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 6-7 | 4462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 7-1 | 4607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 3 | 7-2 | 4698 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| HIGH | Jogador 4 | 3-2 | 290 | SOLD_CORE_UNIT | Venda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 2-5 | 1187 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 1270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 2-6 | 1271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 2-7 | 1395 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 3-1 | 1557 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-1 | 1558 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-2 | 1723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-2 | 1724 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-3 | 1856 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-3 | 1857 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-4 | 2013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-4 | 2014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-5 | 2152 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 2250 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 2420 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-1 | 2587 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-2 | 2672 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 2673 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-3 | 2819 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-3 | 2820 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-4 | 2944 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 3056 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 3329 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 3463 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 4 | 5-1 | 3464 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-2 | 3566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-2 | 3567 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-6 | 1358 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 2-7 | 1522 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-1 | 1700 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 3-2 | 1821 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 4 | 4-1 | 2637 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 5 | 2-5 | 206 | SOLD_CORE_UNIT | Venda de 'DA_18_Kobuko' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 2-6 | 233 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 3-1 | 269 | SOLD_CORE_UNIT | Venda de 'DA_18_Leona' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-2 | 286 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 3-4 | 320 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 5 | 5-3 | 475 | SOLD_CORE_UNIT | Venda de 'DA_18_Azir' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 1-3 | 318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-5 | 3112 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 3260 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 3490 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 3631 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 5-2 | 3632 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 3762 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 5-3 | 3763 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 5 | 3-6 | 2476 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 3-7 | 2610 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 4-1 | 2682 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 6 | 3-1 | 271 | SOLD_CORE_UNIT | Venda de 'DA_18_Teemo' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 3-3 | 303 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 3-4 | 321 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 3-6 | 355 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-2 | 175 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 1-3 | 246 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 2-1 | 501 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 657 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 988 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 1147 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 1296 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 1456 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 1615 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 2816 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 3247 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 4-7 | 3336 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-1 | 3435 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-2 | 3573 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-3 | 3658 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-4 | 3723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-5 | 3800 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-6 | 3888 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-7 | 3965 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-2 | 4238 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-3 | 4343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-6 | 4664 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 6-7 | 4758 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 7-1 | 4910 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 7-2 | 5031 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 7-2 | 5032 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 6 | 3-2 | 1915 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-3 | 2071 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-4 | 2227 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-5 | 2386 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-6 | 2548 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 3-7 | 2707 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 4-1 | 2781 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 6 | 6-6 | 4735 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-5 | 431 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Varus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-3 | 271 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 1-4 | 391 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 550 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 551 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-2 | 646 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 2-3 | 733 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-3 | 734 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 2-4 | 892 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 2-5 | 1050 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 1135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1307 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1458 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1617 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1778 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1942 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 2143 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 2427 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 2540 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 2676 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 2825 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 4-5 | 2826 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-6 | 1195 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 2-7 | 1284 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-1 | 1435 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-2 | 1594 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-3 | 1755 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-4 | 1919 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-5 | 2046 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-6 | 2120 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 3-7 | 2289 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-1 | 2404 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 7 | 4-2 | 2517 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| HIGH | Jogador 8 | 2-5 | 205 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 3-4 | 317 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 1-3 | 282 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 403 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 538 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 849 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-4 | 961 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-5 | 1122 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-6 | 1277 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 2-7 | 1372 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-1 | 1484 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-2 | 1655 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-3 | 1815 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-4 | 1980 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-5 | 2064 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-6 | 2226 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 3-7 | 2384 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-1 | 2546 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 2652 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 2729 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 2806 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 2869 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 2985 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 3074 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 3190 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 3318 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 3423 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-4 | 3516 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-5 | 3593 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-6 | 3700 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-7 | 3850 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-1 | 3964 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 6-2 | 4079 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 6-2 | 4080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 8 | 2-6 | 1349 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 2-7 | 1461 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-1 | 1632 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-2 | 1792 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-3 | 1957 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-4 | 2041 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-5 | 2203 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-6 | 2361 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 3-7 | 2523 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-5 | 3677 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 5-7 | 3941 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 8 | 6-1 | 4055 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
\n\n---\n\n## Evidências resumidas dos achados\n\nO relatório apresenta métricas agregadas e a timeline em tabelas. Esta seção complementa apenas os achados com o contexto mínimo da decisão; snapshots, máscaras brutas e diagnósticos completos não são duplicados em Markdown.\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 2-6 · step 229\n\nVenda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 90.0, nível 5, ouro 3, força 16.0\n- Composição: Defendente / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.30722594261169434, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Akali_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 2-6 · step 234\n\nVenda de 'DA_18_Ornn' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 90.0, nível 5, ouro 3, força 16.0\n- Composição: Defendente / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3680690824985504, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ornn, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 1 · 4-3 · step 404\n\nVenda de 'DA_18_Xayah' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 29.0, nível 6, ouro 15, força 26.0\n- Composição: Colosso / DA_18_Xayah\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5017871856689453, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Xayah, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 2-2 · step 665\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 2-4 · step 960\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 2-5 · step 1045\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 2-7 · step 1363\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 3-4 · step 1861\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 3-5 · step 2022\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 3-7 · step 2328\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 3-7 · step 2329\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-1 · step 2419\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-2 · step 2508\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-4 · step 2802\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-5 · step 2952\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-5 · step 2953\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-6 · step 3066\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 1 · 4-6 · step 3067\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_1_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 1 · 3-4 · step 1999\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=13, comp_direction=Colosso, comp_focus=DA_18_Xayah, reward=0.0, raw_action=PASSOU TURNO\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 2-7 · step 247\n\nVenda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 79.0, nível 5, ouro 7, força 18.0\n- Composição: Vivaz / DA_18_Veigar\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.23346561193466187, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_RekSai, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 4-1 · step 385\n\nVenda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 50.0, nível 5, ouro 40, força 20.0\n- Composição: Vivaz / DA_18_Veigar\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.37049999833106995, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Veigar, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 2 · 4-6 · step 436\n\nVenda de 'DA_18_Xayah' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 28.0, nível 6, ouro 69, força 24.0\n- Composição: Vivaz / DA_18_Xayah\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.424623966217041, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Xayah, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-2 · step 115\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-3 · step 270\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 1-4 · step 380\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-1 · step 542\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-2 · step 687\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-3 · step 841\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-4 · step 999\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-5 · step 1158\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 2-6 · step 1271\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 3-2 · step 1741\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-2 · step 2553\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-3 · step 2643\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-3 · step 2644\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-4 · step 2777\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-4 · step 2778\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-5 · step 2934\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-5 · step 2935\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-6 · step 3084\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-6 · step 3085\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-7 · step 3173\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 4-7 · step 3174\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 5-1 · step 3264\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 5-1 · step 3265\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 5-2 · step 3403\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 5-2 · step 3404\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 5-3 · step 3534\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 2 · 5-3 · step 3535\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_2_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 2-7 · step 1538\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=13, comp_direction=Vivaz, comp_focus=DA_18_Kobuko, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 3-2 · step 1832\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=12, comp_direction=Vivaz, comp_focus=DA_18_Kobuko, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 3-3 · step 1930\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=18, comp_direction=Vivaz, comp_focus=DA_18_Kobuko, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 3-4 · step 2031\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=28, comp_direction=Vivaz, comp_focus=DA_18_Kobuko, reward=-0.02, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 3-5 · step 2130\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=38, comp_direction=Vivaz, comp_focus=DA_Cinderling18, reward=-0.03, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 3-6 · step 2288\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=39, comp_direction=Vivaz, comp_focus=DA_Cinderling18, reward=-0.03, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 3-7 · step 2446\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=43, comp_direction=Vivaz, comp_focus=DA_Cinderling18, reward=-0.19, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 4-6 · step 3150\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=81, comp_direction=Vivaz, comp_focus=DA_18_Teemo, reward=-0.13, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 2 · 4-7 · step 3241\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=92, comp_direction=Vivaz, comp_focus=DA_18_Teemo, reward=-0.15, raw_action=PASSOU TURNO\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 4-2 · step 388\n\nVenda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 76.0, nível 6, ouro 7, força 24.0\n- Composição: Devastador / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.28049999475479126, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 3 · 4-2 · step 392\n\nVenda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 76.0, nível 6, ouro 11, força 24.0\n- Composição: Devastador / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.628000020980835, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Akali_AD, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=2, higher_star_copies_after=2\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 3 · 5-6 · step 506\n\nVenda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 65.0, nível 6, ouro 109, força 32.0\n- Composição: Devastador / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.26037999987602234, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Scuttlecrab18, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 3 · 5-7 · step 512\n\nVenda de 'DA_18_Hecarim' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 65.0, nível 6, ouro 121, força 32.0\n- Composição: Devastador / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.27086034417152405, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Hecarim, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 6-3 · step 544\n\nVenda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 47.0, nível 6, ouro 154, força 30.0\n- Composição: Devastador / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3765000104904175, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Akali_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 1-3 · step 234\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-3 · step 715\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-5 · step 1010\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-6 · step 1093\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 2-7 · step 1252\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 3-1 · step 1413\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 3-2 · step 1501\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 3-3 · step 1663\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 3-4 · step 1762\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 3-5 · step 1923\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 3-6 · step 2086\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 3-7 · step 2245\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 4-1 · step 2409\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 4-2 · step 2571\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 4-3 · step 2633\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 4-5 · step 2782\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 4-6 · step 2871\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 4-7 · step 2943\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-1 · step 3045\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-2 · step 3122\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-3 · step 3245\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-4 · step 3310\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-5 · step 3411\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-6 · step 3539\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 5-7 · step 3683\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 6-1 · step 3775\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 6-2 · step 3852\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 6-3 · step 4000\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 6-4 · step 4143\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 6-5 · step 4260\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 6-6 · step 4350\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 6-7 · step 4462\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 7-1 · step 4607\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 3 · 7-2 · step 4698\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_3_log.tft\n\n### HIGH · SOLD_CORE_UNIT · Jogador 4 · 3-2 · step 290\n\nVenda de 'DA_18_Xayah' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 79.0, nível 5, ouro 9, força 18.0\n- Composição: Sabugueiro / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.17784132063388824, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Xayah, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 2-5 · step 1187\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 2-6 · step 1270\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 2-6 · step 1271\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 2-7 · step 1395\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-1 · step 1557\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-1 · step 1558\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-2 · step 1723\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-2 · step 1724\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-3 · step 1856\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-3 · step 1857\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-4 · step 2013\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-4 · step 2014\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-5 · step 2152\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-6 · step 2250\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 3-7 · step 2420\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-1 · step 2587\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-2 · step 2672\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-2 · step 2673\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-3 · step 2819\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-3 · step 2820\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-4 · step 2944\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-5 · step 3056\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 4-7 · step 3329\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-1 · step 3463\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-1 · step 3464\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-2 · step 3566\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 4 · 5-2 · step 3567\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_4_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 4 · 2-6 · step 1358\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=13, comp_direction=Sabugueiro, comp_focus=DA_18_Akali_AD, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 4 · 2-7 · step 1522\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=12, comp_direction=Sabugueiro, comp_focus=DA_18_Akali_AD, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 4 · 3-1 · step 1700\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=12, comp_direction=Sabugueiro, comp_focus=DA_18_Akali_AD, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 4 · 3-2 · step 1821\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=10, comp_direction=Sabugueiro, comp_focus=DA_18_Akali_AD, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 4 · 4-1 · step 2637\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=13, comp_direction=Colosso, comp_focus=DA_18_Yorick, reward=0.0, raw_action=PASSOU TURNO\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 2-5 · step 206\n\nVenda de 'DA_18_Kobuko' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 4, ouro 5, força 10.0\n- Composição: Colosso / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.1710847020149231, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Kobuko, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 2-6 · step 233\n\nVenda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 5, ouro 0, força 12.0\n- Composição: Colosso / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2706548571586609, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_RekSai, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 3-1 · step 269\n\nVenda de 'DA_18_Leona' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 5, ouro 4, força 14.0\n- Composição: Colosso / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.23703600466251373, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Leona, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 3-2 · step 286\n\nVenda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 91.0, nível 5, ouro 3, força 14.0\n- Composição: Colosso / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.26990753412246704, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_RekSai, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 3-4 · step 320\n\nVenda de 'DA_18_Yunara' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 81.0, nível 5, ouro 1, força 14.0\n- Composição: Colosso / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2803761661052704, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yunara, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 5-3 · step 475\n\nVenda de 'DA_18_Azir' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 8.0, nível 6, ouro 7, força 40.0\n- Composição: Colosso / DA_Vi18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2456156462430954, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Azir, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 1-3 · step 318\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 4-5 · step 3112\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 4-6 · step 3260\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 5-1 · step 3490\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 5-2 · step 3631\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 5-2 · step 3632\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 5-3 · step 3762\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 5 · 5-3 · step 3763\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_5_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 3-6 · step 2476\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=10, comp_direction=Colosso, comp_focus=DA_Vi18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 3-7 · step 2610\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=12, comp_direction=Colosso, comp_focus=DA_Vi18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 5 · 4-1 · step 2682\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=18, comp_direction=Colosso, comp_focus=DA_Vi18, reward=-0.11, raw_action=PASSOU TURNO\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 3-1 · step 271\n\nVenda de 'DA_18_Teemo' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 96.0, nível 5, ouro 3, força 30.0\n- Composição: Emanador / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.34077200293540955, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Teemo, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 3-3 · step 303\n\nVenda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 96.0, nível 5, ouro 15, força 20.0\n- Composição: Emanador / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.28049999475479126, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 6 · 3-4 · step 321\n\nVenda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 96.0, nível 5, ouro 19, força 22.0\n- Composição: Emanador / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.17641817033290863, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Camille, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 3-6 · step 355\n\nVenda de 'DA_18_Akali_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 96.0, nível 5, ouro 11, força 24.0\n- Composição: Emanador / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3200867772102356, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Akali_AD, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 1-2 · step 175\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 1-3 · step 246\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 2-1 · step 501\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 2-2 · step 657\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 2-3 · step 822\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 2-4 · step 988\n\nWarning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 2 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 2-5 · step 1147\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 2-6 · step 1296\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 2-7 · step 1456\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 3-1 · step 1615\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 4-2 · step 2816\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 4-6 · step 3247\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 4-7 · step 3336\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-1 · step 3435\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-2 · step 3573\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-3 · step 3658\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-4 · step 3723\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-5 · step 3800\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-6 · step 3888\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 5-7 · step 3965\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 6-2 · step 4238\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 6-3 · step 4343\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 6-6 · step 4664\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 6-7 · step 4758\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 7-1 · step 4910\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 7-2 · step 5031\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 6 · 7-2 · step 5032\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_6_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 3-2 · step 1915\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=15, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=-0.06, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 3-3 · step 2071\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=13, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 3-4 · step 2227\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=11, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 3-5 · step 2386\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=12, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 3-6 · step 2548\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=13, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 3-7 · step 2707\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=13, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 4-1 · step 2781\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=21, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=-0.03, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 6 · 6-6 · step 4735\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=189, comp_direction=Emanador, comp_focus=DA_Sentinel18, reward=-0.26, raw_action=PASSOU TURNO\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 7 · 4-5 · step 431\n\nVenda de 'DA_18_Varus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ALL_IN · motivo HP crítico: gastar para sobreviver\n- Estado: HP 4.0, nível 6, ouro 70, força 34.0\n- Composição: Colosso / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4840663969516754, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Varus, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-3 · step 271\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 1-4 · step 391\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-1 · step 550\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-1 · step 551\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-2 · step 646\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-3 · step 733\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-3 · step 734\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-4 · step 892\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-5 · step 1050\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 2-6 · step 1135\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 3-1 · step 1307\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 3-2 · step 1458\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 3-3 · step 1617\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 3-4 · step 1778\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 3-5 · step 1942\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 3-7 · step 2143\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-2 · step 2427\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-3 · step 2540\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-4 · step 2676\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-5 · step 2825\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 7 · 4-5 · step 2826\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_7_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 2-6 · step 1195\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=11, comp_direction=Colosso, comp_focus=DA_18_Shen, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 2-7 · step 1284\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=15, comp_direction=Colosso, comp_focus=DA_18_Shen, reward=-0.06, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-1 · step 1435\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=17, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.06, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-2 · step 1594\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=16, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.06, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-3 · step 1755\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=20, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-4 · step 1919\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=29, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.08, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-5 · step 2046\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=32, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.03, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-6 · step 2120\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=43, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.05, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 3-7 · step 2289\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=55, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.25, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 4-1 · step 2404\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=62, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.26, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 7 · 4-2 · step 2517\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=71, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18, reward=-0.29, raw_action=PASSOU TURNO\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 2-5 · step 205\n\nVenda de 'DA_18_Veigar' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia LOSS_STREAK · motivo LOSS_STREAK: converter derrota em economia sem risco crítico\n- Estado: HP 83.0, nível 4, ouro 6, força 12.0\n- Composição: — / DA_18_Veigar\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.26957792043685913, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Veigar, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 3-4 · step 317\n\nVenda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 72.0, nível 5, ouro 34, força 22.0\n- Composição: Lutador / DA_18_Kobuko\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3031309247016907, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Rakan, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-1 · step 44\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-2 · step 163\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-3 · step 282\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 1-4 · step 403\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 2-1 · step 538\n\nWarning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline.\n- Evidência adicional: line=⚠️ 1 carry(s) expostos na frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 2-3 · step 849\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 2-4 · step 961\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 2-5 · step 1122\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 2-6 · step 1277\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 2-7 · step 1372\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 3-1 · step 1484\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 3-2 · step 1655\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 3-3 · step 1815\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 3-4 · step 1980\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 3-5 · step 2064\n\nWarning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 1 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 3-6 · step 2226\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 3-7 · step 2384\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 4-1 · step 2546\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 4-2 · step 2652\n\nWarning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 3 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 4-3 · step 2729\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 4-4 · step 2806\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 4-5 · step 2869\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 4-6 · step 2985\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 4-7 · step 3074\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-1 · step 3190\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-2 · step 3318\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-3 · step 3423\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-4 · step 3516\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-5 · step 3593\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-6 · step 3700\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 5-7 · step 3850\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 6-1 · step 3964\n\nWarning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás.\n- Evidência adicional: line=⚠️ 2 tank(s) posicionados atrás, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 6-2 · step 4079\n\nWarning de posicionamento emitido pelo Viewer: sem frontline.\n- Evidência adicional: line=⚠️ sem frontline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### LOW · TEXT_POSITION_WARNING · Jogador 8 · 6-2 · step 4080\n\nWarning de posicionamento emitido pelo Viewer: sem backline.\n- Evidência adicional: line=⚠️ sem backline, source=C:\Users\Victor\Desktop\dev\Projects\TFT\viewer\sessions\match-20261104-193214-c9a68ec4\player_8_log.tft\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 2-6 · step 1349\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=11, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 2-7 · step 1461\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=18, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=0.0, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-1 · step 1632\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=26, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=-0.08, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-2 · step 1792\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=26, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=-0.08, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-3 · step 1957\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=30, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=-0.03, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-4 · step 2041\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=41, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=-0.03, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-5 · step 2203\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=44, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=-0.13, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-6 · step 2361\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=44, comp_direction=Lutador, comp_focus=DA_18_Veigar, reward=-0.03, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 3-7 · step 2523\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: tabuleiro fraco sob pressão, gold_after=49, comp_direction=Lutador, comp_focus=DA_18_Kobuko, reward=-0.05, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 5-5 · step 3677\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=186, comp_direction=Lutador, comp_focus=DA_18_Alistar, reward=-0.23, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 5-7 · step 3941\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=208, comp_direction=Lutador, comp_focus=DA_18_Alistar, reward=-0.3, raw_action=PASSOU TURNO\n\n### MEDIUM · STABILIZE_PASS_WITH_GOLD_REVIEW · Jogador 8 · 6-1 · step 4055\n\nPossível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado.\n- Evidência adicional: action=PASS, strategy=STABILIZE, strategy_reason=STABILIZE: pressão de vida, gold_after=221, comp_direction=Lutador, comp_focus=DA_18_Alistar, reward=-0.32, raw_action=PASSOU TURNO\n\n## Arquivos e rastreabilidade\n\n- Jogadores analisados: 8\n- Entradas analisadas: 5704\n- Decisões únicas estruturadas: 1964\n- Reconstruções textuais corroborativas (não somadas): 1964\n- Achados: 279\n- Os arquivos estruturados de origem permanecem separados deste relatório.\n- Campos ausentes são exibidos como “—”; não são inferidos como zero.\n