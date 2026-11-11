# Strategic Planner — recomendações

Direção atual e recomendação do planner são mantidas separadas. O planner não altera o compromisso ativo nesta fase.

> Recomendações em shadow mode são diagnósticos heurísticos. Elas não foram executadas nem alteraram a ação do PPO.

| Jogador | Round | Steps observados | Observações | Direção ativa | Decisão | Direção alvo | Âncora | Confiança | Custo de transição | Preservadas | Substituíveis | Candidatos avaliados (ID/direção/score/resultado) | Motivo |
|---|---|---|---:|---|---|---:|---:|---:|---:|---|---|---|---|
| Jogador 1 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 1 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 6 |  |  | insufficient_evidence |
| Jogador 1 | 1-2 | 10–20 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 6, 0 |  |  | insufficient_evidence |
| Jogador 1 | 1-3 | 22–26 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 0, 6 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 2-1 | 44–48 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 0, 6, 7 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 0, 6 | 12, 14 |  | insufficient_evidence |
| Jogador 1 | 2-3 | 62–68 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 0, 6 | 12, 23 |  | insufficient_evidence |
| Jogador 1 | 2-4 | 71–76 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 7, 6, 0 | 12, 23, 33 |  | insufficient_evidence |
| Jogador 1 | 2-5 | 80–80 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 7, 6, 0 | 12, 23, 33 |  | insufficient_evidence |
| Jogador 1 | 2-5 | 81–81 | 1 | Inferno | ABANDON | — | -1 | 0.650 | 0.000 | 7 | 12, 7, 0, 23, 6, 23, 0, 33 |  | board_deficit |
| Jogador 1 | 2-5 | 82–82 | 1 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 0, 7, 23, 6, 23, 0 | 12, 33, 18 |  | board_advantage |
| Jogador 1 | 2-6 | 84–90 | 7 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 23, 7, 7, 23, 0, 33 | 12, 34, 18, 28 |  | board_advantage |
| Jogador 1 | 2-7 | 92–97 | 6 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 23, 7, 23, 33 | 12, 19, 34, 18, 28 |  | board_advantage |
| Jogador 1 | 3-1 | 99–100 | 2 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 7, 23, 23, 33 | 12, 19, 19, 34, 18, 28 |  | board_advantage |
| Jogador 1 | 3-2 | 102–102 | 1 | Fumegante | KEEP | Fumegante | 45 | 0.950 | 0.545 | 12, 0, 19, 7, 19, 33 | 23, 23, 34, 18, 28 | 45:Sabugueiro:39.065:selected_best_candidate, 45:Carrasco:35.002:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 3-2 | 103–108 | 6 | Inferno | KEEP | Inferno | 45 | 0.950 | 0.400 | 23, 0, 19, 7, 23, 33 | 12, 35, 34, 18, 28 | 45:Sabugueiro:39.320:selected_best_candidate, 45:Carrasco:35.531:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 3-3 | 110–110 | 1 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 23, 19, 0, 7, 23, 33 | 12, 35, 34, 18, 28 |  | board_advantage |
| Jogador 1 | 3-4 | 112–116 | 5 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 23, 0, 19, 7, 23, 33 | 12, 31, 35, 34, 18, 28, 1, 16 |  | board_advantage |
| Jogador 1 | 3-5 | 119–120 | 2 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 19, 7, 33, 23 | 12, 31, 35, 34, 18, 28, 1, 16 |  | board_advantage |
| Jogador 1 | 3-6 | 122–126 | 5 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.769 | 19, 0, 7, 23, 33, 23, 23 | 18, 12, 31, 35, 34, 28, 1, 16 | 49:Primordial:33.347:valid_but_not_selected, 49:Adaptador:39.642:selected_best_candidate | board_advantage |
| Jogador 1 | 3-7 | 128–130 | 3 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.769 | 19, 0, 7, 23, 33, 23 | 18, 12, 31, 35, 34, 28, 1, 16, 16 | 49:Primordial:31.883:valid_but_not_selected, 49:Adaptador:38.723:selected_best_candidate | board_advantage |
| Jogador 1 | 4-1 | 132–136 | 5 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 12, 19, 7, 23, 33, 23 | 18, 31, 35, 34, 28, 40, 16, 16 |  | board_advantage |
| Jogador 1 | 4-2 | 138–140 | 3 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 12, 19, 7, 23, 33, 23 | 18, 31, 35, 36, 40, 16, 16 |  | board_advantage |
| Jogador 1 | 4-3 | 142–146 | 5 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 12, 19, 7, 23, 33 | 18, 31, 6, 35, 37, 36, 40, 16, 16 |  | board_advantage |
| Jogador 1 | 4-4 | 148–150 | 3 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 12, 0, 19, 7, 33 | 18, 31, 6, 35, 14, 37, 36, 40, 16, 16 |  | board_advantage |
| Jogador 1 | 4-5 | 152–156 | 5 | Inferno | KEEP | Inferno | 47 | 0.950 | 0.667 | 0, 19, 7, 12, 33 | 31, 18, 29, 35, 47, 37, 36, 40, 16, 16 | 47:Espinhos Negros:36.020:selected_best_candidate, 47:Monólito:31.597:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-6 | 158–160 | 3 | Inferno | KEEP | Inferno | 47 | 0.950 | 0.769 | 0, 19, 7, 12, 33 | 31, 18, 29, 35, 47, 18, 36, 40, 16, 16 | 47:Espinhos Negros:36.184:selected_best_candidate, 47:Monólito:35.505:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-7 | 162–162 | 1 | Inferno | KEEP | Inferno | 47 | 0.950 | 0.400 | 0, 19, 7, 12, 33 | 31, 18, 29, 35, 47, 18, 36, 16, 16 | 47:Espinhos Negros:37.157:selected_best_candidate, 47:Monólito:32.708:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-7 | 163–165 | 3 | Adaptador | KEEP | Adaptador | 47 | 0.950 | 0.400 | 0, 18, 19, 7, 12, 33, 18, 36 | 31, 29, 35, 47, 38, 16, 16 | 47:Espinhos Negros:38.094:selected_best_candidate, 47:Monólito:33.145:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-7 | 166–166 | 1 | Adaptador | KEEP | Adaptador | 51 | 0.950 | 0.400 | 0, 18, 19, 7, 12, 33, 18, 36 | 31, 29, 35, 47, 38, 16, 16 | 51:Florescer:41.259:selected_best_candidate, 51:Lutador:37.943:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-1 | 168–170 | 3 | Adaptador | KEEP | Adaptador | 41 | 0.950 | 0.400 | 0, 18, 19, 7, 12, 33, 18, 36 | 31, 29, 35, 47, 29, 16, 16 | 41:Florescer:44.010:selected_best_candidate, 41:Enfeitiçador:42.600:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-2 | 172–172 | 1 | Adaptador | KEEP | Adaptador | 47 | 0.950 | 0.400 | 0, 18, 19, 7, 12, 33, 18, 36 | 31, 29, 35, 47, 29, 16, 16 | 47:Espinhos Negros:36.899:selected_best_candidate, 47:Monólito:35.922:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-2 | 173–175 | 3 | Adaptador | KEEP | Adaptador | -1 | 0.000 | 0.000 | 0, 18, 19, 7, 12, 0, 33, 18, 36 | 31, 29, 35, 29, 16 |  | board_advantage |
| Jogador 2 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 2 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 11 |  |  | insufficient_evidence |
| Jogador 2 | 1-2 | 10–20 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 11, 11 |  |  | insufficient_evidence |
| Jogador 2 | 1-3 | 22–32 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 11, 4 |  |  | insufficient_evidence |
| Jogador 2 | 1-4 | 34–40 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 11, 11, 11 | 13 |  | insufficient_evidence |
| Jogador 2 | 2-1 | 44–50 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 11 | 40 |  | insufficient_evidence |
| Jogador 2 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 11, 7 | 12, 0, 22, 40 |  | insufficient_evidence |
| Jogador 2 | 2-3 | 62–69 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 0, 22, 8, 40 |  | insufficient_evidence |
| Jogador 2 | 2-4 | 71–78 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 12, 32, 22, 10, 40, 30 |  | insufficient_evidence |
| Jogador 2 | 2-5 | 80–80 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 4, 7, 11, 7 | 32, 12, 12, 22, 10, 40, 30 |  | insufficient_evidence |
| Jogador 2 | 2-5 | 81–81 | 1 | Feérico | ABANDON | — | -1 | 0.650 | 0.000 |  | 32, 4, 12, 7, 11, 12, 7, 22, 10, 40, 30, 39 |  | board_deficit |
| Jogador 2 | 2-5 | 82–82 | 1 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 12, 7, 11, 12, 7, 39 | 32, 10, 40, 30 |  | board_advantage |
| Jogador 2 | 2-6 | 84–90 | 7 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 12, 7, 11, 12, 7, 39 | 32, 22, 10, 30 |  | board_advantage |
| Jogador 2 | 2-7 | 92–97 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 12, 7, 11, 7, 12, 39 | 32, 8, 22, 10, 32, 30 |  | board_advantage |
| Jogador 2 | 3-1 | 99–100 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 7, 12, 7, 12, 39 | 32, 8, 22, 10, 32, 30, 37 |  | board_advantage |
| Jogador 2 | 3-2 | 102–108 | 7 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 7, 7, 39 | 32, 8, 22, 10, 32, 30, 37 |  | board_advantage |
| Jogador 2 | 3-3 | 110–110 | 1 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.667 | 4, 11, 7, 7, 39 | 32, 8, 22, 10, 32, 30, 37 | 49:Primordial:34.719:selected_best_candidate, 49:Adaptador:34.205:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 3-4 | 112–117 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 7, 7, 39, 39 | 32, 8, 25, 10, 32, 30, 37 |  | board_advantage |
| Jogador 2 | 3-5 | 119–120 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 7, 7, 39, 39 | 32, 8, 10, 10, 32, 30, 37 |  | board_advantage |
| Jogador 2 | 3-6 | 122–126 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 7, 7, 39, 39 | 32, 8, 10, 37, 10, 35, 30, 37 |  | board_advantage |
| Jogador 2 | 3-7 | 128–130 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 7, 7, 39 | 32, 8, 10, 37, 30, 37 |  | board_advantage |
| Jogador 2 | 4-1 | 132–136 | 5 | Feérico | KEEP | Feérico | 45 | 0.950 | 0.667 | 4, 11, 7, 7, 4, 39 | 32, 8, 10, 32, 37, 30, 24, 37 | 45:Sabugueiro:39.006:selected_best_candidate, 45:Carrasco:36.891:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 4-2 | 138–140 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 39, 4, 7 | 32, 8, 10, 37, 32, 30, 24, 37 |  | board_advantage |
| Jogador 2 | 4-3 | 142–146 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 39, 4, 11, 4, 7 | 32, 32, 10, 8, 34, 38, 37, 30, 24, 37 |  | board_advantage |
| Jogador 2 | 4-4 | 148–150 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 39, 4, 11, 4, 7 | 32, 32, 10, 8, 34, 38, 0, 37, 30, 24 |  | board_advantage |
| Jogador 2 | 4-5 | 152–155 | 4 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 11, 4, 39, 4, 7 | 32, 8, 10, 32, 34, 38, 0, 37, 30, 24, 38 |  | board_advantage |
| Jogador 2 | 4-6 | 158–160 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 11, 4, 39, 4, 11, 7 | 32, 8, 10, 32, 34, 38, 0, 30, 24, 38 |  | board_advantage |
| Jogador 2 | 4-7 | 162–166 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 11, 39, 4, 11 | 8, 32, 10, 32, 34, 38, 25, 30, 24, 38, 8 |  | board_advantage |
| Jogador 2 | 5-1 | 168–170 | 3 | Feérico | KEEP | Feérico | 70 | 0.950 | 0.667 | 4, 11, 39, 4, 11 | 32, 10, 8, 32, 34, 38, 25, 30, 24, 38, 8 | 70:Sabugueiro:39.387:selected_best_candidate, 70:Avatar:35.703:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 5-2 | 172–175 | 4 | Feérico | KEEP | Feérico | 42 | 0.950 | 0.400 | 4, 11, 39, 4, 11 | 32, 10, 8, 32, 34, 33, 38, 30, 24, 42, 8 | 42:Inferno:36.388:valid_but_not_selected, 42:Colosso:37.787:selected_best_candidate | board_advantage |
| Jogador 3 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 3 | 1-1 | 2–4 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0 |  |  | insufficient_evidence |
| Jogador 3 | 1-2 | 10–20 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 0, 13 |  |  | insufficient_evidence |
| Jogador 3 | 1-3 | 22–32 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 8, 0 |  |  | insufficient_evidence |
| Jogador 3 | 1-4 | 34–38 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 0 | 18, 1 |  | insufficient_evidence |
| Jogador 3 | 2-1 | 44–50 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 0 | 15, 18, 1, 23 |  | insufficient_evidence |
| Jogador 3 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 8, 0 | 15, 18, 1, 23, 15, 29 |  | insufficient_evidence |
| Jogador 3 | 2-3 | 62–65 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 8, 0 | 15, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-4 | 71–78 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 0, 8 | 15, 32, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-5 | 80–80 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 0, 8 | 15, 32, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-5 | 81–81 | 1 | Colosso | ABANDON | — | -1 | 0.650 | 0.000 | 0 | 8, 15, 13, 32, 18, 1, 23, 15, 29, 21, 7, 8, 13 |  | board_deficit |
| Jogador 3 | 2-5 | 82–82 | 1 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 8, 15, 13, 0, 15, 7, 8, 13 | 32, 18, 1, 23, 29, 21 |  | board_advantage |
| Jogador 3 | 2-6 | 84–90 | 7 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 8, 13, 0, 15, 7, 8 | 32, 18, 1, 29, 21 |  | board_advantage |
| Jogador 3 | 2-7 | 92–97 | 6 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 8, 0, 13, 15, 15, 7, 8, 13 | 1, 18, 32, 29, 29, 21 |  | board_advantage |
| Jogador 3 | 3-1 | 99–100 | 2 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 8, 0, 13, 15, 15, 7, 8, 13 | 1, 18, 32, 29, 29, 21 |  | board_advantage |
| Jogador 3 | 3-2 | 102–107 | 6 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 0, 8, 15, 15, 7, 13 | 29, 18, 32, 1, 29, 21 |  | board_advantage |
| Jogador 3 | 3-3 | 110–110 | 1 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.545 | 13, 0, 8, 15, 15, 7, 13 | 29, 18, 32, 1, 29, 21 | 52:Primordial:42.840:selected_best_candidate, 52:Caçador:41.380:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-4 | 112–112 | 1 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.400 | 13, 0, 8, 15, 15, 7, 13 | 29, 18, 32, 1, 29, 52, 21 | 52:Primordial:43.579:selected_best_candidate, 52:Caçador:42.681:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-4 | 113–116 | 4 | Colosso | ADAPT | Primordial | 52 | 0.650 | 0.400 | 13, 0, 8, 52, 40, 13 | 1, 18, 32, 29, 29, 15, 15, 21, 7 | 52:Primordial:43.908:selected_best_candidate, 52:Caçador:43.013:not_best_scoring_candidate | anchor_opportunity |
| Jogador 3 | 3-5 | 119–119 | 1 | Colosso | KEEP | Colosso | 49 | 0.950 | 0.545 | 13, 0, 8, 15, 15, 7, 40, 13 | 1, 18, 32, 29, 29, 52, 21 | 49:Primordial:40.552:valid_but_not_selected, 49:Adaptador:42.533:selected_best_candidate | board_advantage |
| Jogador 3 | 3-5 | 120–120 | 1 | Colosso | ADAPT | Adaptador | 49 | 0.650 | 0.545 | 13, 18, 0, 15, 15, 13 | 1, 32, 29, 29, 52, 21, 7, 40 | 49:Primordial:40.268:valid_but_not_selected, 49:Adaptador:44.103:selected_best_candidate | anchor_opportunity |
| Jogador 3 | 3-6 | 122–122 | 1 | Colosso | ADAPT | Primordial | 52 | 0.650 | 0.400 | 13, 0, 40, 15, 15, 52, 40, 13 | 1, 18, 32, 29, 29, 21, 7 | 52:Primordial:44.240:selected_best_candidate, 52:Caçador:43.440:not_best_scoring_candidate | anchor_opportunity |
| Jogador 3 | 3-6 | 123–126 | 4 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.400 | 40, 13, 0, 15, 15, 7, 40, 13 | 18, 32, 29, 29, 52, 21 | 52:Primordial:43.237:selected_best_candidate, 52:Caçador:42.443:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-7 | 128–130 | 3 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.545 | 13, 0, 40, 15, 15, 7, 40, 13 | 32, 18, 32, 29, 29, 52, 21 | 52:Primordial:42.975:selected_best_candidate, 52:Caçador:42.180:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-1 | 132–136 | 5 | Colosso | KEEP | Colosso | 53 | 0.950 | 0.667 | 0, 40, 13, 15, 15, 7, 40, 13 | 29, 32, 18, 32, 29, 52, 21 | 53:Flora Fatalis:32.519:valid_but_not_selected, 53:Carrasco:36.422:selected_best_candidate | board_advantage |
| Jogador 3 | 4-2 | 138–140 | 3 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.545 | 0, 40, 15, 15, 7, 40, 13 | 29, 32, 18, 32, 29, 18, 52, 21 | 52:Primordial:42.065:selected_best_candidate, 52:Caçador:41.445:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-3 | 142–144 | 3 | Colosso | KEEP | Colosso | 51 | 0.950 | 0.667 | 32, 0, 40, 15, 15, 7, 40, 13 | 18, 18, 32, 29, 29, 52, 21 | 51:Florescer:38.964:selected_best_candidate, 51:Lutador:35.330:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-4 | 148–150 | 3 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.400 | 40, 32, 0, 15, 15, 7, 40, 13 | 18, 32, 29, 29, 18, 52 | 52:Primordial:41.128:selected_best_candidate, 52:Caçador:40.269:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-5 | 152–156 | 5 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.222 | 32, 0, 40, 15, 15, 7, 40, 13 | 18, 18, 32, 29, 29, 52, 33 | 52:Primordial:43.455:selected_best_candidate, 52:Caçador:42.068:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-6 | 158–158 | 1 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.222 | 32, 40, 0, 15, 15, 7, 40, 13 | 18, 32, 29, 29, 18, 52, 33 | 52:Primordial:43.352:selected_best_candidate, 52:Caçador:42.240:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-6 | 159–160 | 2 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 32, 40, 0, 15, 7, 40, 13 | 18, 32, 29, 29, 18, 33 |  | board_advantage |
| Jogador 3 | 4-7 | 162–166 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 0, 22, 40, 7, 13 | 32, 29, 29, 21, 33, 18 |  | board_advantage |
| Jogador 3 | 5-1 | 168–170 | 3 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 0, 22, 22, 40, 7, 13 | 29, 32, 29, 21, 9, 33, 18 |  | board_advantage |
| Jogador 3 | 5-2 | 172–175 | 4 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 0, 22, 22, 40, 7, 7, 13 | 29, 32, 29, 21, 9, 33 |  | board_advantage |
| Jogador 3 | 5-3 | 177–180 | 4 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 0, 22, 22, 7, 7, 13 | 29, 32, 29, 21, 36, 35, 33 |  | board_advantage |
| Jogador 3 | 5-4 | 182–185 | 4 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 22, 0, 15, 22, 7, 7, 13 | 29, 32, 29, 33, 36, 33 |  | board_advantage |
| Jogador 3 | 5-5 | 187–190 | 4 | Colosso | KEEP | Colosso | 64 | 0.950 | 0.222 | 15, 32, 22, 0, 15, 22, 7, 7, 13 | 29, 32, 29, 27, 36, 33 | 64:Espinhos Negros:40.651:selected_best_candidate, 64:Avatar:37.301:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 5-6 | 192–194 | 2 | Colosso | ADAPT | Florescer | 41 | 0.650 | 0.545 | 15, 32, 0, 15, 36, 13 | 29, 22, 32, 29, 27, 22, 33, 64, 7, 7 | 41:Florescer:44.596:selected_best_candidate, 41:Enfeitiçador:42.193:not_best_scoring_candidate | anchor_opportunity |
| Jogador 3 | 5-6 | 193–195 | 2 | Colosso | KEEP | Colosso | 41 | 0.950 | 0.545 | 15, 32, 22, 0, 15, 22, 7, 7, 13 | 29, 32, 29, 27, 33, 64 | 41:Florescer:42.706:selected_best_candidate, 41:Enfeitiçador:41.194:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 5-7 | 197–199 | 3 | Colosso | KEEP | Colosso | 64 | 0.950 | 0.222 | 15, 32, 22, 0, 15, 22, 13, 7, 7, 13 | 29, 32, 29, 27, 33, 64 | 64:Espinhos Negros:40.062:selected_best_candidate, 64:Avatar:36.712:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 5-7 | 200–200 | 1 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 22, 0, 15, 22, 13, 7, 7, 13 | 29, 32, 29, 27, 33 |  | board_advantage |
| Jogador 3 | 6-1 | 202–205 | 4 | Colosso | KEEP | Colosso | 41 | 0.950 | 0.545 | 15, 32, 22, 0, 32, 15, 22, 13, 7, 7, 13 | 29, 29, 35, 33, 33 | 41:Florescer:42.501:selected_best_candidate, 41:Enfeitiçador:41.788:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 6-2 | 207–210 | 4 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 22, 0, 32, 22, 13, 7, 7, 13 | 29, 29, 35, 18, 39, 33 |  | board_advantage |
| Jogador 3 | 6-3 | 212–215 | 4 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 32, 0, 32, 13, 7, 7, 13 | 29, 29, 35, 18, 25, 33 |  | board_advantage |
| Jogador 3 | 6-4 | 217–220 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 15, 32, 35, 0, 32, 18, 18, 13, 44, 13 | 29, 29, 33, 7, 7 | 44:Fera do Rift:48.089:selected_best_candidate, 44:Vanguarda:45.639:not_best_scoring_candidate | anchor_opportunity |
| Jogador 3 | 6-5 | 222–225 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 15, 32, 35, 0, 32, 18, 18, 13, 44, 13 | 29, 29, 33, 7, 7 | 44:Fera do Rift:48.225:selected_best_candidate, 44:Vanguarda:44.759:not_best_scoring_candidate | anchor_opportunity |
| Jogador 3 | 6-6 | 227–230 | 4 | Colosso | ADAPT | Fera do Rift | 50 | 0.650 | 0.400 | 15, 32, 35, 0, 32, 18, 18, 50, 13, 44, 13 | 29, 29, 7, 7 | 50:Fera do Rift:48.548:selected_best_candidate, 50:Devastador:42.539:not_best_scoring_candidate | anchor_opportunity |
| Jogador 3 | 6-7 | 232–233 | 2 | Colosso | KEEP | Colosso | 43 | 0.950 | 0.545 | 15, 32, 0, 32, 13, 7, 7, 13 | 29, 35, 29, 18, 18, 50, 44 | 43:Lunar:44.285:valid_but_not_selected, 43:Fumegante:44.650:selected_best_candidate | board_advantage |
| Jogador 3 | 6-7 | 234–235 | 2 | Colosso | ADAPT | Fera do Rift | 50 | 0.650 | 0.400 | 15, 32, 35, 0, 32, 18, 18, 50, 13, 44, 13 | 29, 29, 7, 7 | 50:Fera do Rift:48.511:selected_best_candidate, 50:Devastador:42.549:not_best_scoring_candidate | anchor_opportunity |
| Jogador 3 | 7-1 | 237–240 | 4 | Colosso | KEEP | Colosso | 47 | 0.950 | 0.545 | 15, 32, 0, 32, 13, 0, 7, 7, 13 | 29, 35, 29, 18, 18, 50, 44 | 47:Espinhos Negros:38.296:selected_best_candidate, 47:Monólito:34.724:not_best_scoring_candidate | board_advantage |
| Jogador 4 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 4 | 1-1 | 2–4 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7 |  |  | insufficient_evidence |
| Jogador 4 | 1-2 | 10–20 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 1, 7, 13 |  |  | insufficient_evidence |
| Jogador 4 | 1-3 | 22–26 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13 | 3, 6 |  | insufficient_evidence |
| Jogador 4 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1 | 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-1 | 44–48 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1, 13 | 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1, 13 | 3, 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-3 | 62–69 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 13, 13, 33 | 3, 0, 0, 3 |  | insufficient_evidence |
| Jogador 4 | 2-4 | 71–72 | 2 | — | INITIAL_SELECTION | Fumegante | 43 | 0.950 | 1.000 | 7, 13, 13, 43, 33 | 0, 3, 0, 3 | 43:Lunar:40.908:valid_but_not_selected, 43:Fumegante:41.136:selected_best_candidate | anchor_opportunity |
| Jogador 4 | 2-4 | 73–78 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 13, 13, 33 | 0, 3, 0 |  | insufficient_evidence |
| Jogador 4 | 2-5 | 80–80 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 13, 13, 33 | 0, 3, 0 |  | insufficient_evidence |
| Jogador 4 | 2-5 | 81–81 | 1 | Florescer | ABANDON | — | -1 | 0.650 | 0.000 | 13 | 7, 0, 3, 13, 30, 33, 0 |  | board_deficit |
| Jogador 4 | 2-5 | 82–82 | 1 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 3, 13, 13, 26, 33 | 0, 30, 0 |  | board_advantage |
| Jogador 4 | 2-6 | 84–90 | 7 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 0, 3, 13, 13, 0 |  |  | board_advantage |
| Jogador 4 | 2-7 | 92–97 | 6 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 7, 3, 13, 13, 36, 0 | 11 |  | board_advantage |
| Jogador 4 | 3-1 | 99–100 | 2 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 3, 13, 13, 7, 36, 0 | 11 |  | board_advantage |
| Jogador 4 | 3-2 | 102–108 | 7 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 36, 0, 3, 13, 13 | 11 |  | board_advantage |
| Jogador 4 | 3-3 | 110–110 | 1 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 36, 0, 3, 13, 13 | 11, 30 |  | board_advantage |
| Jogador 4 | 3-4 | 112–117 | 6 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 0, 36, 7, 3, 13, 13, 0, 0, 36, 26 | 11, 30 |  | board_advantage |
| Jogador 4 | 3-5 | 119–120 | 2 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 36, 7, 3, 13, 0, 13, 0, 0, 36, 26, 26 | 11, 30 |  | board_advantage |
| Jogador 4 | 3-6 | 122–126 | 5 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 36, 7, 3, 13, 0, 13, 0, 0, 36, 26 | 11, 30, 30 |  | board_advantage |
| Jogador 4 | 3-7 | 128–130 | 3 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 0, 13, 3, 13, 7, 0, 0, 36, 26 | 11, 30, 30 |  | board_advantage |
| Jogador 4 | 4-1 | 132–136 | 5 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 0, 13, 3, 13, 7, 0, 0, 7, 36, 26 | 11, 30, 25, 25, 30 |  | board_advantage |
| Jogador 4 | 4-2 | 138–140 | 3 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 13, 0, 3, 13, 7, 0, 0, 7, 36, 26 | 11, 30, 25, 25, 30 |  | board_advantage |
| Jogador 4 | 4-3 | 142–146 | 5 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 13, 0, 3, 13, 0, 0, 26, 26 | 11, 30, 25, 25, 30 |  | board_advantage |
| Jogador 4 | 4-4 | 148–150 | 3 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 13, 0, 3, 13, 26, 0, 0 | 11, 25, 27, 25, 30 |  | board_advantage |
| Jogador 4 | 4-5 | 152–156 | 5 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 0, 13, 7, 3, 13, 26, 0, 0 | 11, 25, 27, 25, 39, 32, 30 |  | board_advantage |
| Jogador 4 | 4-6 | 158–160 | 3 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 0, 7, 13, 3, 13, 26, 0, 0 | 11, 25, 27, 30, 39, 32, 30 |  | board_advantage |
| Jogador 5 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 5 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13 |  |  | insufficient_evidence |
| Jogador 5 | 1-2 | 10–20 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 11 |  |  | insufficient_evidence |
| Jogador 5 | 1-3 | 22–23 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13 | 26 |  | insufficient_evidence |
| Jogador 5 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13 | 26, 7, 22 |  | insufficient_evidence |
| Jogador 5 | 2-1 | 44–49 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 7, 26, 28, 22 |  | insufficient_evidence |
| Jogador 5 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 7, 26, 28, 22, 7 |  | insufficient_evidence |
| Jogador 5 | 2-3 | 62–69 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 26, 1, 22, 7 |  | insufficient_evidence |
| Jogador 5 | 2-4 | 71–78 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 22, 33, 20 |  | insufficient_evidence |
| Jogador 5 | 2-5 | 80–80 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 22, 33 |  | insufficient_evidence |
| Jogador 5 | 2-5 | 81–81 | 1 | Espinhos Negros | ABANDON | — | -1 | 0.650 | 0.000 | 13 | 28, 8, 11, 4, 37, 22, 8, 33 |  | board_deficit |
| Jogador 5 | 2-5 | 82–82 | 1 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 37, 0, 22, 33 |  | board_advantage |
| Jogador 5 | 2-6 | 84–90 | 7 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 37, 33 |  | board_advantage |
| Jogador 5 | 2-7 | 92–92 | 1 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 37, 1, 33 |  | board_advantage |
| Jogador 5 | 2-7 | 93–97 | 5 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 11, 33, 13, 13 | 4, 37, 1, 26 |  | board_advantage |
| Jogador 5 | 3-1 | 99–100 | 2 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 11, 33, 13, 13 | 4, 37, 26, 26 |  | board_advantage |
| Jogador 5 | 3-2 | 102–104 | 3 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 11, 33, 13, 13 | 37, 4, 26, 39, 24 |  | board_advantage |
| Jogador 5 | 3-2 | 105–108 | 4 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 11, 33, 37, 13, 4, 39, 13, 24 | 28, 23 |  | board_advantage |
| Jogador 5 | 3-3 | 110–110 | 1 | Vivaz | KEEP | Vivaz | 41 | 0.950 | 0.545 | 11, 33, 37, 13, 4, 39, 13, 24 | 28, 23 | 41:Florescer:42.547:selected_best_candidate, 41:Enfeitiçador:42.418:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 3-4 | 112–117 | 6 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 11, 33, 37, 13, 4, 37, 39, 13, 24, 4 | 28, 14 |  | board_advantage |
| Jogador 5 | 3-5 | 119–120 | 2 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 11, 33, 37, 13, 4, 37, 39, 13, 24, 4 | 28, 8 |  | board_advantage |
| Jogador 5 | 3-6 | 122–126 | 5 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 11, 33, 37, 13, 4, 37, 39, 13, 24, 4, 24 | 28, 12 |  | board_advantage |
| Jogador 5 | 3-7 | 128–130 | 3 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 11, 33, 37, 13, 4, 37, 39, 13, 24, 4, 24 | 28 |  | board_advantage |
| Jogador 5 | 4-1 | 132–136 | 5 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 11, 33, 37, 13, 4, 37, 39, 13, 24, 4, 24 | 28, 38, 30, 7 |  | board_advantage |
| Jogador 5 | 4-2 | 138–140 | 3 | Vivaz | KEEP | Vivaz | 53 | 0.950 | 0.545 | 11, 24, 37, 13, 4, 37, 39, 13, 33, 4, 24 | 28, 38, 30, 8 | 53:Flora Fatalis:38.671:valid_but_not_selected, 53:Carrasco:38.753:selected_best_candidate | board_advantage |
| Jogador 5 | 4-3 | 142–146 | 5 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 11, 24, 37, 13, 4, 37, 39, 33, 13, 33, 4, 24 | 28, 30 |  | board_advantage |
| Jogador 5 | 4-4 | 148–150 | 3 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 39, 11, 37, 13, 4, 37, 33, 13, 33, 4, 24 | 28 |  | board_advantage |
| Jogador 5 | 4-5 | 152–156 | 5 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 39, 33, 11, 37, 13, 37, 33, 13, 24, 4 | 28, 8, 0 |  | board_advantage |
| Jogador 5 | 4-6 | 158–160 | 3 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 39, 33, 11, 37, 13, 37, 33, 13, 24 | 28, 8, 0, 0, 30 |  | board_advantage |
| Jogador 5 | 4-7 | 162–166 | 5 | Vivaz | KEEP | Vivaz | 43 | 0.950 | 0.222 | 39, 33, 11, 37, 13, 37, 33, 13 | 28, 8, 0, 30, 12 | 43:Lunar:40.525:valid_but_not_selected, 43:Fumegante:40.609:selected_best_candidate | board_advantage |
| Jogador 5 | 5-1 | 168–170 | 3 | Vivaz | KEEP | Vivaz | 50 | 0.950 | 0.400 | 39, 33, 11, 37, 13, 37, 33, 13, 39 | 28, 43, 8, 0, 30, 12 | 50:Fera do Rift:37.476:valid_but_not_selected, 50:Devastador:40.084:selected_best_candidate | board_advantage |
| Jogador 5 | 5-2 | 172–175 | 4 | Vivaz | KEEP | Vivaz | 43 | 0.950 | 0.667 | 39, 33, 11, 37, 37, 13, 24, 33, 13, 4, 39 | 28, 43, 0, 30, 12 | 43:Lunar:42.010:selected_best_candidate, 43:Fumegante:40.789:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 5-3 | 177–178 | 2 | Vivaz | KEEP | Vivaz | 43 | 0.950 | 0.545 | 39, 33, 11, 37, 37, 13, 24, 33, 13, 4, 24, 39 | 28, 43, 30, 12 | 43:Lunar:42.955:selected_best_candidate, 43:Fumegante:41.147:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 5-3 | 179–180 | 2 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 39, 11, 37, 37, 13, 24, 33, 13, 4, 24, 39 | 28, 30, 12 |  | board_advantage |
| Jogador 6 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 6 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 2 |  |  | insufficient_evidence |
| Jogador 6 | 1-2 | 10–20 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 2, 12, 13 |  |  | insufficient_evidence |
| Jogador 6 | 1-3 | 22–32 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 2, 12, 13 | 4 |  | insufficient_evidence |
| Jogador 6 | 1-4 | 34–35 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 4 |  | insufficient_evidence |
| Jogador 6 | 2-1 | 44–48 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 4, 7 |  | insufficient_evidence |
| Jogador 6 | 2-2 | 52–56 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 7, 19 |  | insufficient_evidence |
| Jogador 6 | 2-3 | 62–67 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 19, 15, 18 |  | insufficient_evidence |
| Jogador 6 | 2-4 | 71–78 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 31, 7, 15, 18, 7 |  | insufficient_evidence |
| Jogador 6 | 2-5 | 80–80 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 31, 7, 15, 18, 7 |  | insufficient_evidence |
| Jogador 6 | 2-5 | 81–81 | 1 | Feérico | ABANDON | — | -1 | 0.650 | 0.000 | 2 | 12, 12, 2, 39, 13, 13, 31, 7, 15, 18, 7 |  | board_deficit |
| Jogador 6 | 2-5 | 82–82 | 1 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 39, 2, 13, 13, 7, 7 | 19, 31, 15, 18 |  | board_advantage |
| Jogador 6 | 2-6 | 84–90 | 7 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 39, 2, 7, 7 | 9, 19, 19 |  | board_advantage |
| Jogador 6 | 2-7 | 92–97 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 39, 2, 7, 7 | 19 |  | board_advantage |
| Jogador 6 | 3-1 | 99–100 | 2 | Feérico | KEEP | Feérico | 41 | 0.950 | 0.545 | 12, 12, 2, 39, 2, 7, 7 | 19, 30 | 41:Florescer:37.852:selected_best_candidate, 41:Enfeitiçador:37.098:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-2 | 102–108 | 7 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 12, 2, 12, 39 | 19, 30, 14 |  | board_advantage |
| Jogador 6 | 3-3 | 110–110 | 1 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 2, 12, 39, 7 | 14, 19, 30 |  | board_advantage |
| Jogador 6 | 3-4 | 112–117 | 6 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.545 | 12, 12, 39, 2, 7, 39, 46 | 14, 19, 30, 35 | 46:Feérico:42.678:selected_best_candidate, 46:Defendente:37.878:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-5 | 119–120 | 2 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.545 | 12, 12, 39, 2, 7, 39, 46 | 14, 19, 30, 35, 35 | 46:Feérico:42.810:selected_best_candidate, 46:Defendente:38.910:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-6 | 122–126 | 5 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.545 | 12, 2, 12, 39, 39, 46 | 19, 14, 30, 14, 35, 35 | 46:Feérico:39.402:selected_best_candidate, 46:Defendente:34.164:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-7 | 128–128 | 1 | Feérico | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 12, 2, 12, 39, 39, 35, 35 | 19, 14, 30, 14, 46 | 44:Fera do Rift:41.878:selected_best_candidate, 44:Vanguarda:40.950:not_best_scoring_candidate | anchor_opportunity |
| Jogador 6 | 3-7 | 129–130 | 2 | Feérico | KEEP | Feérico | 44 | 0.950 | 0.545 | 12, 12, 39, 39, 46 | 14, 19, 14, 30, 35, 35 | 44:Fera do Rift:38.582:selected_best_candidate, 44:Vanguarda:37.745:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-1 | 132–136 | 5 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.400 | 12, 12, 39, 39, 46 | 14, 19, 14, 30, 9, 35, 35 | 46:Feérico:39.765:selected_best_candidate, 46:Defendente:36.528:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-2 | 138–140 | 3 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.400 | 12, 14, 12, 46, 39 | 9, 19, 14, 30, 35, 35 | 46:Feérico:40.598:selected_best_candidate, 46:Defendente:37.481:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-3 | 142–143 | 2 | Feérico | KEEP | Feérico | 42 | 0.950 | 0.545 | 12, 14, 12, 46, 39 | 9, 19, 14, 30, 20, 19, 35, 35 | 42:Inferno:38.011:valid_but_not_selected, 42:Colosso:38.133:selected_best_candidate | board_advantage |
| Jogador 6 | 4-3 | 144–146 | 3 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.769 | 12, 14, 12, 46, 35, 35 | 9, 19, 14, 30, 20, 19, 0, 42 | 46:Feérico:37.299:selected_best_candidate, 46:Defendente:36.249:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-4 | 148–150 | 3 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.400 | 12, 14, 12, 46, 35, 35, 7 | 9, 19, 14, 30, 20, 19, 42, 38 | 46:Feérico:40.486:selected_best_candidate, 46:Defendente:37.524:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-5 | 152–156 | 5 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.667 | 12, 14, 46, 35, 35, 7 | 9, 19, 14, 30, 10, 19, 42, 38 | 46:Feérico:41.572:selected_best_candidate, 46:Defendente:38.572:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-6 | 158–160 | 3 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.400 | 12, 14, 46, 46, 35, 35, 7 | 30, 9, 19, 14, 19, 42, 38 | 46:Feérico:40.593:selected_best_candidate, 46:Defendente:36.058:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-7 | 162–166 | 5 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.400 | 14, 46, 39, 12, 46, 35, 35, 7 | 30, 9, 19, 19, 42, 38 | 46:Feérico:42.814:selected_best_candidate, 46:Defendente:38.014:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 5-1 | 168–169 | 2 | Feérico | ADAPT | Fumegante | 43 | 0.650 | 0.667 | 14, 46, 19, 12, 46, 35, 35 | 30, 9, 39, 7, 42, 38 | 43:Lunar:44.856:valid_but_not_selected, 43:Fumegante:46.015:selected_best_candidate | transition_cost |
| Jogador 6 | 5-1 | 170–170 | 1 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.400 | 14, 46, 39, 12, 46, 35, 35, 7 | 30, 9, 19, 43, 42, 38 | 46:Feérico:43.144:selected_best_candidate, 46:Defendente:38.344:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 5-2 | 172–175 | 4 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.545 | 14, 46, 39, 19, 46, 35, 35, 7 | 30, 9, 11, 43, 42, 38 | 46:Feérico:39.972:selected_best_candidate, 46:Defendente:34.470:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 7 | 1-1 | 2–2 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0 |  |  | insufficient_evidence |
| Jogador 7 | 1-2 | 10–20 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 10 |  |  | insufficient_evidence |
| Jogador 7 | 1-3 | 22–27 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 10, 0 | 13 |  | insufficient_evidence |
| Jogador 7 | 1-4 | 34–38 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 0, 7, 0, 10 | 13, 1 |  | insufficient_evidence |
| Jogador 7 | 2-1 | 44–48 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 0, 7, 0, 10 | 13, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 7, 31, 10 | 13, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-3 | 62–69 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 31, 7, 28 | 13, 1, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-4 | 71–78 | 4 | — | INITIAL_SELECTION | Fera do Rift | 44 | 0.950 | 1.000 | 31, 7, 28, 44 | 13, 33, 1, 1, 13, 23 | 44:Fera do Rift:38.444:selected_best_candidate, 44:Vanguarda:32.220:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-5 | 80–80 | 1 | — | INITIAL_SELECTION | Fera do Rift | 44 | 0.950 | 1.000 | 31, 7, 28, 44 | 33, 13, 1, 1, 13, 23 | 44:Fera do Rift:42.336:selected_best_candidate, 44:Vanguarda:38.129:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-5 | 81–81 | 1 | Colosso | PIVOT | Fera do Rift | 44 | 0.950 | 0.400 | 7, 35, 44 | 31, 28, 33, 13, 1, 1, 13, 23 | 44:Fera do Rift:44.140:selected_best_candidate, 44:Vanguarda:40.224:not_best_scoring_candidate | board_deficit |
| Jogador 7 | 2-5 | 82–82 | 1 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 31, 7, 28, 35, 44 | 33, 13, 1, 1, 13, 23, 12 | 44:Fera do Rift:44.652:selected_best_candidate, 44:Vanguarda:40.750:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-6 | 84–90 | 7 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 31, 28, 7, 35, 44, 7 | 33, 13, 1, 13, 12, 33 | 44:Fera do Rift:46.357:selected_best_candidate, 44:Vanguarda:39.165:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-7 | 92–96 | 3 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 31, 28, 44, 7, 35, 7 | 33, 13, 37, 1, 13, 12, 33 | 44:Fera do Rift:44.736:selected_best_candidate, 44:Vanguarda:40.916:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-7 | 94–97 | 3 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 31, 28, 13, 7, 13, 7 | 33, 35, 37, 1, 12, 33 | 44:Fera do Rift:44.860:selected_best_candidate, 44:Vanguarda:41.130:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 3-1 | 99–100 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 7, 28, 35, 15, 7 | 33, 13, 37, 1, 13, 12, 33 | 44:Fera do Rift:47.889:selected_best_candidate, 44:Vanguarda:44.132:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-2 | 102–105 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 7, 28, 35, 15, 7 | 33, 13, 37, 1, 13, 40, 12, 33 | 44:Fera do Rift:49.371:selected_best_candidate, 44:Vanguarda:45.615:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-3 | 110–110 | 1 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 7, 28, 35, 15, 7 | 33, 13, 37, 1, 13, 40, 12, 33 | 44:Fera do Rift:49.368:selected_best_candidate, 44:Vanguarda:45.611:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-4 | 112–117 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 15, 31, 28, 35, 7 | 13, 29, 37, 13, 40, 12, 33 | 44:Fera do Rift:50.044:selected_best_candidate, 44:Vanguarda:42.793:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-5 | 119–120 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 15, 35, 31, 28, 7 | 13, 12, 29, 37, 13, 40, 12, 33 | 44:Fera do Rift:50.602:selected_best_candidate, 44:Vanguarda:46.818:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-6 | 122–126 | 5 | Colosso | KEEP | Colosso | 43 | 0.950 | 0.400 | 44, 15, 31, 13, 28, 31, 13, 40, 33 | 35, 12, 29, 37, 12, 29 | 43:Lunar:44.436:selected_best_candidate, 43:Fumegante:43.211:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 3-7 | 128–130 | 3 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 44, 15, 35, 31, 13, 28, 31 | 12, 29, 37, 13, 40, 12, 37, 29 | 44:Fera do Rift:44.524:selected_best_candidate, 44:Vanguarda:41.603:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 4-1 | 132–136 | 5 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.545 | 44, 15, 31, 13, 28, 22, 31, 13, 40 | 35, 12, 29, 12, 29 | 44:Fera do Rift:41.794:selected_best_candidate, 44:Vanguarda:40.869:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-2 | 138–140 | 3 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.545 | 44, 15, 31, 13, 28, 22, 31, 13, 40, 22 | 35, 12, 29, 12, 29 | 44:Fera do Rift:43.825:selected_best_candidate, 44:Vanguarda:41.382:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-3 | 142–142 | 1 | Colosso | KEEP | Colosso | 53 | 0.950 | 0.667 | 44, 15, 31, 13, 28, 22, 31, 13, 40, 22 | 35, 12, 12, 29 | 53:Flora Fatalis:30.271:valid_but_not_selected, 53:Carrasco:32.797:selected_best_candidate | board_advantage |
| Jogador 7 | 4-3 | 143–146 | 4 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.222 | 44, 15, 31, 13, 28, 22, 31, 13, 40, 22 | 35, 12, 53, 12, 20 | 44:Fera do Rift:44.371:selected_best_candidate, 44:Vanguarda:40.597:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-4 | 148–150 | 3 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.222 | 44, 15, 31, 13, 28, 22, 31, 13, 40, 22 | 35, 12, 35, 53, 12, 20 | 44:Fera do Rift:45.302:selected_best_candidate, 44:Vanguarda:41.497:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-5 | 152–152 | 1 | Colosso | KEEP | Colosso | 45 | 0.950 | 0.667 | 44, 15, 31, 13, 28, 22, 31, 13, 40, 22 | 35, 12, 35, 53, 12 | 45:Sabugueiro:41.229:selected_best_candidate, 45:Carrasco:38.773:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-5 | 153–156 | 4 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.222 | 44, 15, 31, 13, 28, 22, 31, 13, 40, 22 | 35, 12, 35, 12, 45 | 44:Fera do Rift:44.905:selected_best_candidate, 44:Vanguarda:41.123:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-6 | 158–160 | 3 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 15, 35, 13, 28, 35, 31 | 12, 22, 13, 40, 12, 22, 45 | 44:Fera do Rift:49.739:selected_best_candidate, 44:Vanguarda:45.918:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 4-7 | 162–166 | 5 | Colosso | KEEP | Colosso | 52 | 0.950 | 0.222 | 44, 15, 35, 35, 13, 28, 15, 22, 7, 13, 40, 22 | 12, 30, 12, 45 | 52:Primordial:45.248:selected_best_candidate, 52:Caçador:45.098:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 5-1 | 168–170 | 3 | Colosso | KEEP | Colosso | 56 | 0.950 | 0.545 | 44, 15, 35, 35, 13, 28, 15, 22, 7, 13, 40, 22 | 12, 30, 12, 18 | 56:Florescer:41.715:selected_best_candidate, 56:Caçador:41.024:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 5-2 | 172–175 | 4 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.222 | 44, 15, 35, 35, 13, 28, 15, 22, 7, 13, 40, 22 | 12, 30, 12 | 44:Fera do Rift:48.256:selected_best_candidate, 44:Vanguarda:44.502:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 5-3 | 177–180 | 4 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.222 | 44, 15, 35, 35, 13, 28, 15, 22, 7, 13, 40, 22 | 12, 30, 12 | 44:Fera do Rift:48.158:selected_best_candidate, 44:Vanguarda:44.502:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 5-4 | 182–185 | 4 | Colosso | KEEP | Colosso | 50 | 0.950 | 0.222 | 44, 15, 35, 35, 13, 28, 15, 22, 7, 13, 40, 22 | 12, 12, 33 | 50:Fera do Rift:48.816:selected_best_candidate, 50:Devastador:40.311:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 5-5 | 187–190 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 15, 35, 35, 13, 28, 15 | 12, 22, 7, 13, 40, 12, 22, 33 | 44:Fera do Rift:50.579:selected_best_candidate, 44:Vanguarda:46.739:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-6 | 192–195 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 15, 35, 35, 13, 28, 15 | 12, 22, 7, 13, 40, 12, 22, 33 | 44:Fera do Rift:50.579:selected_best_candidate, 44:Vanguarda:46.738:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-7 | 197–200 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 35, 15, 13, 28, 15 | 12, 22, 7, 13, 40, 12, 22, 33 | 44:Fera do Rift:50.791:selected_best_candidate, 44:Vanguarda:47.004:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 6-1 | 202–205 | 4 | Colosso | KEEP | Colosso | 45 | 0.950 | 0.667 | 44, 35, 15, 15, 28, 13, 22, 7, 13, 40, 22 | 12, 39, 27, 12, 33 | 45:Sabugueiro:41.844:selected_best_candidate, 45:Carrasco:40.601:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 6-2 | 207–209 | 3 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 13, 28, 35, 15 | 12, 27, 22, 7, 13, 40, 12, 22, 33 | 44:Fera do Rift:50.968:selected_best_candidate, 44:Vanguarda:47.192:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 6-2 | 210–210 | 1 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 13, 28, 35, 22, 7, 13, 40, 22 | 12, 27, 12, 33 | 44:Fera do Rift:46.351:selected_best_candidate, 44:Vanguarda:44.526:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 6-3 | 212–215 | 4 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 13, 28, 35, 35, 22, 7, 13, 40, 22 | 12, 27, 30, 33 | 44:Fera do Rift:47.564:selected_best_candidate, 44:Vanguarda:43.332:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 6-4 | 217–219 | 2 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 13, 35, 28, 35, 22, 7, 13, 40, 22 | 12, 27, 33, 26, 30, 33 | 44:Fera do Rift:48.002:selected_best_candidate, 44:Vanguarda:43.704:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 6-4 | 218–220 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 44, 13, 35, 28, 35 | 27, 12, 33, 26, 22, 7, 13, 40, 30, 22, 33 | 44:Fera do Rift:48.052:selected_best_candidate, 44:Vanguarda:43.753:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 6-5 | 222–225 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 44, 13, 35, 28, 35, 2 | 27, 12, 33, 22, 7, 13, 40, 30, 32, 33 | 44:Fera do Rift:50.158:selected_best_candidate, 44:Vanguarda:46.122:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 6-6 | 227–230 | 4 | Colosso | KEEP | Colosso | 41 | 0.950 | 0.545 | 44, 13, 35, 28, 35, 35, 7, 13, 40 | 27, 12, 33, 2, 30, 27, 33 | 41:Florescer:46.284:selected_best_candidate, 41:Enfeitiçador:44.421:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 6-7 | 232–235 | 4 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 13, 35, 28, 35, 35, 2 | 27, 12, 33, 7, 13, 40, 24, 27, 33 | 44:Fera do Rift:52.499:selected_best_candidate, 44:Vanguarda:48.262:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 7-1 | 237–240 | 4 | Colosso | KEEP | Colosso | 46 | 0.950 | 0.400 | 44, 13, 35, 28, 35, 35, 7, 13, 28 | 27, 12, 33, 2, 27, 33 | 46:Feérico:42.481:selected_best_candidate, 46:Defendente:40.357:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 8 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7 |  |  | insufficient_evidence |
| Jogador 8 | 1-2 | 10–20 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 7, 11 |  |  | insufficient_evidence |
| Jogador 8 | 1-3 | 22–24 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7, 3 | 13 |  | insufficient_evidence |
| Jogador 8 | 1-4 | 34–39 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7, 3 | 12, 12 |  | insufficient_evidence |
| Jogador 8 | 2-1 | 44–50 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7 | 12, 24 |  | insufficient_evidence |
| Jogador 8 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 11, 7, 3 | 24, 25, 12, 34, 0, 4 |  | insufficient_evidence |
| Jogador 8 | 2-3 | 62–69 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 3, 3, 11 | 4, 28, 25, 12, 34, 0, 24 |  | insufficient_evidence |
| Jogador 8 | 2-4 | 71–78 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 28, 7, 3, 3 | 4, 4, 25, 2, 34, 0, 24, 22, 32 |  | insufficient_evidence |
| Jogador 8 | 2-5 | 80–80 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 28, 3, 7, 3 | 4, 4, 25, 2, 34, 0, 24, 22, 32 |  | insufficient_evidence |
| Jogador 8 | 2-5 | 81–81 | 1 | Enfeitiçador | ABANDON | — | -1 | 0.650 | 0.000 | 7 | 4, 28, 3, 4, 25, 2, 34, 0, 24, 3, 22, 32, 3 |  | board_deficit |
| Jogador 8 | 2-5 | 82–82 | 1 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 3, 7, 3, 3 | 4, 4, 25, 34, 0, 24, 22, 32 |  | board_advantage |
| Jogador 8 | 2-6 | 84–90 | 7 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 3, 7, 7, 3, 3 | 4, 4, 25, 25, 34, 29, 39, 32 |  | board_advantage |
| Jogador 8 | 2-7 | 92–97 | 6 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 3, 7, 7, 3, 3 | 4, 4, 25, 25, 29, 39, 39 |  | board_advantage |
| Jogador 8 | 3-1 | 99–100 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 46 | 0.950 | 0.545 | 28, 3, 7, 7, 3, 3 | 4, 4, 25, 25, 0, 29, 39, 39 | 46:Feérico:36.396:valid_but_not_selected, 46:Defendente:37.759:selected_best_candidate | board_advantage |
| Jogador 8 | 3-2 | 102–108 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.667 | 28, 3, 7, 7, 3, 3 | 4, 4, 25, 25, 50, 39, 39 | 50:Fera do Rift:32.412:valid_but_not_selected, 50:Devastador:33.130:selected_best_candidate | board_advantage |
| Jogador 8 | 3-3 | 110–110 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.667 | 28, 3, 7, 7, 3, 3 | 4, 4, 25, 25, 50, 23, 39, 39 | 50:Fera do Rift:34.179:valid_but_not_selected, 50:Devastador:34.339:selected_best_candidate | board_advantage |
| Jogador 8 | 3-4 | 112–117 | 6 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.857 | 28, 3, 3, 7, 7 | 25, 25, 35, 50, 4, 39, 39 | 50:Fera do Rift:34.423:selected_best_candidate, 50:Devastador:33.346:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-5 | 119–120 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.857 | 28, 3, 3, 7, 7, 28 | 25, 25, 35, 50, 22, 4, 39, 39 | 50:Fera do Rift:35.534:selected_best_candidate, 50:Devastador:33.957:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-6 | 122–123 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 47 | 0.950 | 0.667 | 28, 3, 3, 7, 28 | 25, 25, 35, 50, 22, 39, 39 | 47:Espinhos Negros:36.047:selected_best_candidate, 47:Monólito:29.161:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-6 | 124–126 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.667 | 28, 3, 3, 50, 28 | 25, 25, 35, 47, 22, 39, 39 | 50:Fera do Rift:34.562:selected_best_candidate, 50:Devastador:33.038:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-7 | 128–130 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.667 | 28, 3, 3, 11, 50, 28 | 25, 25, 35, 47, 22, 27, 39, 39 | 50:Fera do Rift:39.236:selected_best_candidate, 50:Devastador:36.811:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-1 | 132–136 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.667 | 25, 28, 3, 3, 11, 11, 50, 28 | 25, 35, 47, 22, 27, 39, 39 | 50:Fera do Rift:38.227:selected_best_candidate, 50:Devastador:37.078:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-2 | 138–138 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.857 | 25, 28, 3, 3, 11, 11, 50, 28 | 25, 35, 47, 27, 39, 39 | 52:Primordial:38.348:valid_but_not_selected, 52:Caçador:38.553:selected_best_candidate | board_advantage |
| Jogador 8 | 4-2 | 139–140 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.667 | 25, 28, 3, 3, 11, 11, 50, 28 | 25, 35, 47, 52, 27, 39, 39 | 50:Fera do Rift:38.151:selected_best_candidate, 50:Devastador:37.104:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-3 | 142–146 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.769 | 25, 28, 3, 11, 3, 11, 20, 50, 28 | 25, 47, 29, 27, 39, 39 | 50:Fera do Rift:34.866:valid_but_not_selected, 50:Devastador:36.899:selected_best_candidate | board_advantage |
| Jogador 8 | 4-4 | 148–150 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.667 | 3, 28, 25, 11, 3, 11, 20, 50, 20, 28 | 25, 47, 27, 39, 39 | 50:Fera do Rift:35.470:valid_but_not_selected, 50:Devastador:38.900:selected_best_candidate | board_advantage |
| Jogador 8 | 4-5 | 152–156 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.545 | 3, 25, 11, 3, 11, 50, 28, 20 | 25, 39, 47 | 50:Fera do Rift:34.617:valid_but_not_selected, 50:Devastador:38.039:selected_best_candidate | board_advantage |
| Jogador 8 | 4-6 | 158–160 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.545 | 3, 25, 11, 11, 3, 50, 28, 20 | 25, 36, 39, 47, 31 | 50:Fera do Rift:34.999:valid_but_not_selected, 50:Devastador:38.436:selected_best_candidate | board_advantage |

### Frequência das decisões

- ABANDON: 7
- ADAPT: 27
- INITIAL_SELECTION: 3
- INSUFFICIENT_EVIDENCE: 78
- KEEP: 170
- PIVOT: 1

Revisões estratégicas únicas: **286**.
Snapshots estratégicos observados: **1053** (inclui repetições por ação).
Candidatos de âncora avaliados: **238**.


### Auditoria de KEEP — continuidade fundamentada versus persistência

- KEEP auditados: **170**
- Confiança da direção atual: positive=170
- Motivos/path: current_direction_viable_without_alternative=82; alternative_below_minimum_adapt_advantage=76; best_anchor_matches_current_direction=12

| Jogador | Round | Step | Direção | Score atual | Conf. direção atual | Conf. alternativa | Score alternativa | Vantagem | Viável | Motivo | Lock | Candidato pendente | Streak | Limite PIVOT |
|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|
| Jogador 1 | 2-5 | 82 | Inferno | 44.095 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.819 |
| Jogador 1 | 2-6 | 90 | Inferno | 43.080 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.616 |
| Jogador 1 | 2-7 | 97 | Inferno | 43.451 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.690 |
| Jogador 1 | 3-1 | 100 | Inferno | 43.909 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.782 |
| Jogador 1 | 3-2 | 102 | Fumegante | 47.694 | 0.950 | 0.950 | 39.065 | -8.628 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 9.539 |
| Jogador 1 | 3-2 | 108 | Inferno | 43.676 | 0.950 | 0.950 | 39.320 | -4.356 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.735 |
| Jogador 1 | 3-3 | 110 | Inferno | 43.755 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.751 |
| Jogador 1 | 3-4 | 116 | Inferno | 43.706 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.741 |
| Jogador 1 | 3-5 | 120 | Inferno | 44.965 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.993 |
| Jogador 1 | 3-6 | 126 | Inferno | 45.544 | 0.950 | 0.950 | 39.642 | -5.902 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.109 |
| Jogador 1 | 3-7 | 130 | Inferno | 44.478 | 0.950 | 0.950 | 38.723 | -5.755 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.896 |
| Jogador 1 | 4-1 | 136 | Inferno | 44.428 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.886 |
| Jogador 1 | 4-2 | 140 | Inferno | 44.353 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.871 |
| Jogador 1 | 4-3 | 146 | Inferno | 44.766 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.953 |
| Jogador 1 | 4-4 | 150 | Inferno | 42.280 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.456 |
| Jogador 1 | 4-5 | 156 | Inferno | 40.093 | 0.950 | 0.950 | 36.020 | -4.073 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.019 |
| Jogador 1 | 4-6 | 160 | Inferno | 43.148 | 0.950 | 0.950 | 36.184 | -6.965 | True | alternative_below_minimum_adapt_advantage | True | Adaptador | 1 | 8.630 |
| Jogador 1 | 4-7 | 162 | Inferno | 42.460 | 0.950 | 0.950 | 37.157 | -5.302 | True | alternative_below_minimum_adapt_advantage | True | Adaptador | 2 | 8.492 |
| Jogador 1 | 4-7 | 165 | Adaptador | 46.687 | 0.950 | 0.950 | 38.094 | -8.593 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.337 |
| Jogador 1 | 4-7 | 166 | Adaptador | 46.388 | 0.950 | 0.950 | 41.259 | -5.129 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.278 |
| Jogador 1 | 5-1 | 170 | Adaptador | 46.687 | 0.950 | 0.950 | 44.010 | -2.677 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.337 |
| Jogador 1 | 5-2 | 172 | Adaptador | 46.874 | 0.950 | 0.950 | 36.899 | -9.975 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.375 |
| Jogador 1 | 5-2 | 175 | Adaptador | 47.278 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.456 |
| Jogador 2 | 2-5 | 82 | Feérico | 43.325 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.665 |
| Jogador 2 | 2-6 | 90 | Feérico | 43.436 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.687 |
| Jogador 2 | 2-7 | 97 | Feérico | 43.840 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.768 |
| Jogador 2 | 3-1 | 100 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 3-2 | 108 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 3-3 | 110 | Feérico | 43.819 | 0.950 | 0.950 | 34.719 | -9.100 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.764 |
| Jogador 2 | 3-4 | 117 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 3-5 | 120 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 3-6 | 126 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 3-7 | 130 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 4-1 | 136 | Feérico | 43.819 | 0.950 | 0.950 | 39.006 | -4.814 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.764 |
| Jogador 2 | 4-2 | 140 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 4-3 | 146 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 4-4 | 150 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 4-5 | 155 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 4-6 | 160 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 4-7 | 166 | Feérico | 43.819 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.764 |
| Jogador 2 | 5-1 | 170 | Feérico | 43.819 | 0.950 | 0.950 | 39.387 | -4.432 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.764 |
| Jogador 2 | 5-2 | 175 | Feérico | 43.819 | 0.950 | 0.950 | 37.787 | -6.032 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.764 |
| Jogador 3 | 2-5 | 82 | Colosso | 41.378 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.276 |
| Jogador 3 | 2-6 | 90 | Colosso | 41.915 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.383 |
| Jogador 3 | 2-7 | 97 | Colosso | 43.325 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.665 |
| Jogador 3 | 3-1 | 100 | Colosso | 44.647 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.929 |
| Jogador 3 | 3-2 | 107 | Colosso | 43.584 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.717 |
| Jogador 3 | 3-3 | 110 | Colosso | 43.596 | 0.950 | 0.950 | 42.840 | -0.756 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.719 |
| Jogador 3 | 3-4 | 112 | Colosso | 43.596 | 0.950 | 0.950 | 43.579 | -0.018 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.719 |
| Jogador 3 | 3-5 | 119 | Colosso | 43.596 | 0.950 | 0.950 | 42.533 | -1.063 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.719 |
| Jogador 3 | 3-6 | 126 | Colosso | 43.596 | 0.950 | 0.950 | 43.237 | -0.359 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.719 |
| Jogador 3 | 3-7 | 130 | Colosso | 43.596 | 0.950 | 0.950 | 42.975 | -0.621 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.719 |
| Jogador 3 | 4-1 | 136 | Colosso | 43.596 | 0.950 | 0.950 | 36.422 | -7.175 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.719 |
| Jogador 3 | 4-2 | 140 | Colosso | 43.750 | 0.950 | 0.950 | 42.065 | -1.685 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.750 |
| Jogador 3 | 4-3 | 144 | Colosso | 44.107 | 0.950 | 0.950 | 38.964 | -5.143 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.821 |
| Jogador 3 | 4-4 | 150 | Colosso | 43.462 | 0.950 | 0.950 | 41.128 | -2.335 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.692 |
| Jogador 3 | 4-5 | 156 | Colosso | 45.224 | 0.950 | 0.950 | 43.455 | -1.769 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.045 |
| Jogador 3 | 4-6 | 158 | Colosso | 45.030 | 0.950 | 0.950 | 43.352 | -1.678 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.006 |
| Jogador 3 | 4-6 | 160 | Colosso | 45.364 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.073 |
| Jogador 3 | 4-7 | 166 | Colosso | 46.116 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.223 |
| Jogador 3 | 5-1 | 170 | Colosso | 45.685 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.137 |
| Jogador 3 | 5-2 | 175 | Colosso | 45.678 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.136 |
| Jogador 3 | 5-3 | 180 | Colosso | 43.971 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.794 |
| Jogador 3 | 5-4 | 185 | Colosso | 43.275 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.655 |
| Jogador 3 | 5-5 | 190 | Colosso | 45.888 | 0.950 | 0.950 | 40.651 | -5.237 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.178 |
| Jogador 3 | 5-6 | 195 | Colosso | 45.187 | 0.950 | 0.950 | 42.706 | -2.481 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.037 |
| Jogador 3 | 5-7 | 199 | Colosso | 45.499 | 0.950 | 0.950 | 40.062 | -5.437 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.100 |
| Jogador 3 | 5-7 | 200 | Colosso | 45.538 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.108 |
| Jogador 3 | 6-1 | 205 | Colosso | 46.802 | 0.950 | 0.950 | 42.501 | -4.301 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.360 |
| Jogador 3 | 6-2 | 210 | Colosso | 46.463 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.293 |
| Jogador 3 | 6-3 | 215 | Colosso | 45.364 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.073 |
| Jogador 3 | 6-7 | 233 | Colosso | 45.170 | 0.950 | 0.950 | 44.650 | -0.520 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.034 |
| Jogador 3 | 7-1 | 240 | Colosso | 45.878 | 0.950 | 0.950 | 38.296 | -7.581 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.176 |
| Jogador 4 | 2-5 | 82 | Florescer | 43.703 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.741 |
| Jogador 4 | 2-6 | 90 | Florescer | 40.355 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.071 |
| Jogador 4 | 2-7 | 97 | Florescer | 43.038 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.608 |
| Jogador 4 | 3-1 | 100 | Florescer | 44.583 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.917 |
| Jogador 4 | 3-2 | 108 | Florescer | 44.241 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.848 |
| Jogador 4 | 3-3 | 110 | Florescer | 44.241 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.848 |
| Jogador 4 | 3-4 | 117 | Florescer | 47.594 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.519 |
| Jogador 4 | 3-5 | 120 | Florescer | 47.808 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.562 |
| Jogador 4 | 3-6 | 126 | Florescer | 48.437 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.687 |
| Jogador 4 | 3-7 | 130 | Florescer | 48.777 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.755 |
| Jogador 4 | 4-1 | 136 | Florescer | 48.954 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.791 |
| Jogador 4 | 4-2 | 140 | Florescer | 48.414 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.683 |
| Jogador 4 | 4-3 | 146 | Florescer | 48.580 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.716 |
| Jogador 4 | 4-4 | 150 | Florescer | 48.580 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.716 |
| Jogador 4 | 4-5 | 156 | Florescer | 48.925 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.785 |
| Jogador 4 | 4-6 | 160 | Florescer | 48.997 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.799 |
| Jogador 5 | 2-5 | 82 | Espinhos Negros | 41.470 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.294 |
| Jogador 5 | 2-6 | 90 | Espinhos Negros | 41.275 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.255 |
| Jogador 5 | 2-7 | 92 | Espinhos Negros | 40.957 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.191 |
| Jogador 5 | 2-7 | 97 | Enfeitiçador | 40.775 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.155 |
| Jogador 5 | 3-1 | 100 | Enfeitiçador | 40.761 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.152 |
| Jogador 5 | 3-2 | 104 | Enfeitiçador | 41.557 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.311 |
| Jogador 5 | 3-2 | 108 | Vivaz | 47.922 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.584 |
| Jogador 5 | 3-3 | 110 | Vivaz | 47.755 | 0.950 | 0.950 | 42.547 | -5.207 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.551 |
| Jogador 5 | 3-4 | 117 | Vivaz | 48.806 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.761 |
| Jogador 5 | 3-5 | 120 | Vivaz | 50.965 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 10.193 |
| Jogador 5 | 3-6 | 126 | Vivaz | 49.736 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.947 |
| Jogador 5 | 3-7 | 130 | Vivaz | 48.894 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.779 |
| Jogador 5 | 4-1 | 136 | Vivaz | 51.498 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 10.300 |
| Jogador 5 | 4-2 | 140 | Vivaz | 53.271 | 0.950 | 0.950 | 38.753 | -14.519 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.654 |
| Jogador 5 | 4-3 | 146 | Vivaz | 51.372 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 10.274 |
| Jogador 5 | 4-4 | 150 | Vivaz | 51.418 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 10.284 |
| Jogador 5 | 4-5 | 156 | Vivaz | 52.431 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 10.486 |
| Jogador 5 | 4-6 | 160 | Vivaz | 51.444 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 10.289 |
| Jogador 5 | 4-7 | 166 | Vivaz | 47.767 | 0.950 | 0.950 | 40.609 | -7.158 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.553 |
| Jogador 5 | 5-1 | 170 | Vivaz | 47.622 | 0.950 | 0.950 | 40.084 | -7.538 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.524 |
| Jogador 5 | 5-2 | 175 | Vivaz | 51.953 | 0.950 | 0.950 | 42.010 | -9.944 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.391 |
| Jogador 5 | 5-3 | 178 | Vivaz | 52.299 | 0.950 | 0.950 | 42.955 | -9.344 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.460 |
| Jogador 5 | 5-3 | 180 | Vivaz | 52.624 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 10.525 |
| Jogador 6 | 2-5 | 82 | Feérico | 42.164 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.433 |
| Jogador 6 | 2-6 | 90 | Feérico | 41.682 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.336 |
| Jogador 6 | 2-7 | 97 | Feérico | 41.682 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.336 |
| Jogador 6 | 3-1 | 100 | Feérico | 41.682 | 0.950 | 0.950 | 37.852 | -3.830 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.336 |
| Jogador 6 | 3-2 | 108 | Feérico | 41.682 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.336 |
| Jogador 6 | 3-3 | 110 | Feérico | 41.682 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.336 |
| Jogador 6 | 3-4 | 117 | Feérico | 41.682 | 0.950 | 0.950 | 42.678 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 3-5 | 120 | Feérico | 41.682 | 0.950 | 0.950 | 42.810 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 3-6 | 126 | Feérico | 41.682 | 0.950 | 0.950 | 39.402 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 3-7 | 130 | Feérico | 41.682 | 0.950 | 0.950 | 38.582 | -3.100 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.336 |
| Jogador 6 | 4-1 | 136 | Feérico | 41.682 | 0.950 | 0.950 | 39.765 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 4-2 | 140 | Feérico | 41.682 | 0.950 | 0.950 | 40.598 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 4-3 | 143 | Feérico | 41.682 | 0.950 | 0.950 | 38.133 | -3.549 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.336 |
| Jogador 6 | 4-3 | 146 | Feérico | 41.682 | 0.950 | 0.950 | 37.299 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 4-4 | 150 | Feérico | 41.682 | 0.950 | 0.950 | 40.486 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 4-5 | 156 | Feérico | 41.682 | 0.950 | 0.950 | 41.572 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 4-6 | 160 | Feérico | 41.682 | 0.950 | 0.950 | 40.593 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 4-7 | 166 | Feérico | 41.682 | 0.950 | 0.950 | 42.814 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 5-1 | 170 | Feérico | 41.682 | 0.950 | 0.950 | 43.144 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 6 | 5-2 | 175 | Feérico | 41.682 | 0.950 | 0.950 | 39.972 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.336 |
| Jogador 7 | 2-7 | 97 | Colosso | 44.766 | 0.950 | 0.950 | 44.860 | 0.094 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.953 |
| Jogador 7 | 3-6 | 126 | Colosso | 46.111 | 0.950 | 0.950 | 44.436 | -1.675 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.222 |
| Jogador 7 | 4-1 | 136 | Colosso | 44.629 | 0.950 | 0.950 | 41.794 | -2.835 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.926 |
| Jogador 7 | 4-2 | 140 | Colosso | 45.163 | 0.950 | 0.950 | 43.825 | -1.339 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.033 |
| Jogador 7 | 4-3 | 142 | Colosso | 44.891 | 0.950 | 0.950 | 32.797 | -12.094 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.978 |
| Jogador 7 | 4-3 | 146 | Colosso | 44.552 | 0.950 | 0.950 | 44.371 | -0.180 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.910 |
| Jogador 7 | 4-4 | 150 | Colosso | 45.643 | 0.950 | 0.950 | 45.302 | -0.341 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.129 |
| Jogador 7 | 4-5 | 152 | Colosso | 45.277 | 0.950 | 0.950 | 41.229 | -4.047 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.055 |
| Jogador 7 | 4-5 | 156 | Colosso | 45.202 | 0.950 | 0.950 | 44.905 | -0.297 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.040 |
| Jogador 7 | 4-7 | 166 | Colosso | 48.912 | 0.950 | 0.950 | 45.248 | -3.665 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.782 |
| Jogador 7 | 5-1 | 170 | Colosso | 48.612 | 0.950 | 0.950 | 41.715 | -6.897 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.722 |
| Jogador 7 | 5-2 | 175 | Colosso | 48.616 | 0.950 | 0.950 | 48.256 | -0.360 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.723 |
| Jogador 7 | 5-3 | 180 | Colosso | 48.617 | 0.950 | 0.950 | 48.158 | -0.459 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.723 |
| Jogador 7 | 5-4 | 185 | Colosso | 49.498 | 0.950 | 0.950 | 48.816 | -0.682 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.900 |
| Jogador 7 | 6-1 | 205 | Colosso | 49.451 | 0.950 | 0.950 | 41.844 | -7.607 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.890 |
| Jogador 7 | 6-2 | 210 | Colosso | 47.537 | 0.950 | 0.950 | 46.351 | -1.186 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.507 |
| Jogador 7 | 6-3 | 215 | Colosso | 47.990 | 0.950 | 0.950 | 47.564 | -0.425 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.598 |
| Jogador 7 | 6-4 | 219 | Colosso | 48.334 | 0.950 | 0.950 | 48.002 | -0.332 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.667 |
| Jogador 7 | 6-6 | 230 | Colosso | 49.166 | 0.950 | 0.950 | 46.284 | -2.883 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.833 |
| Jogador 7 | 7-1 | 240 | Colosso | 49.196 | 0.950 | 0.950 | 42.481 | -6.714 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.839 |
| Jogador 8 | 2-5 | 82 | Enfeitiçador | 41.083 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.217 |
| Jogador 8 | 2-6 | 90 | Enfeitiçador | 41.083 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.217 |
| Jogador 8 | 2-7 | 97 | Enfeitiçador | 41.083 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.217 |
| Jogador 8 | 3-1 | 100 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 37.759 | -3.324 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 3-2 | 108 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 33.130 | -7.953 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 3-3 | 110 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 34.339 | -6.744 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 3-4 | 117 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 34.423 | -6.660 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 3-5 | 120 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 35.534 | -5.549 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 3-6 | 123 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 36.047 | -5.036 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 3-6 | 126 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 34.562 | -6.521 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 3-7 | 130 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 39.236 | -1.846 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 4-1 | 136 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 38.227 | -2.856 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 4-2 | 138 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 38.553 | -2.530 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 4-2 | 140 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 38.151 | -2.931 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 4-3 | 146 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 36.899 | -4.184 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 4-4 | 150 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 38.900 | -2.183 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 4-5 | 156 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 38.039 | -3.044 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |
| Jogador 8 | 4-6 | 160 | Enfeitiçador | 41.083 | 0.950 | 0.950 | 38.436 | -2.647 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.217 |

### Unidades preservadas — sinais estratégicos versus investimento

| Jogador | Round | Unidade | Área | Estrelas | Classificação | Sinais estratégicos | Indicadores de investimento |
|---|---|---|---|---:|---|---|---|
| Jogador 1 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 2-5 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Ornn | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 1 | 2-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 2-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 2-6 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 2-6 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Akali | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 2-6 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 2-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 2-7 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-7 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 1 | 2-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 2-7 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-1 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-1 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-2 | Xayah | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-2 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-2 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-2 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-2 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-2 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-2 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-2 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-3 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-3 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-3 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-3 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-4 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-4 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-4 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-4 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-5 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-5 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-5 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 3-6 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-6 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-6 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-6 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-6 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 3-7 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-7 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-1 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-1 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-2 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-2 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-2 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-2 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-2 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-3 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-3 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 4-3 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-4 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-4 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-4 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-5 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-5 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-5 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-6 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-6 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-6 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-7 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-7 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-7 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-7 | Grompe | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 4-7 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-7 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-7 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-7 | Grompe | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-7 | Grompe | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 4-7 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-7 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 4-7 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 4-7 | Grompe | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-1 | Grompe | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 5-1 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-1 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 5-1 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 5-1 | Grompe | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-1 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-2 | Grompe | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 5-2 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-2 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 5-2 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 5-2 | Grompe | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-2 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-2 | Grompe | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 5-2 | Kayle | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-2 | Xayah | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 1 | 5-2 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-2 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 5-2 | Grompe | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-2 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 2-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-5 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-5 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-5 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 2-6 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-6 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-6 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 2-7 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-1 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-1 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-1 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-2 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-2 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-2 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-3 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-3 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-3 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-4 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-4 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-4 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-4 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-5 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-5 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-6 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-6 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-6 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-6 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-7 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-7 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-7 | Tristana | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-1 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-1 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-1 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-1 | Tristana | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-2 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-2 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 4-2 | Tristana | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-2 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-2 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-3 | Tristana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-3 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-3 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 4-3 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-3 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-4 | Tristana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-4 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-4 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 4-4 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-4 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 4-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-5 | Tristana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-5 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-5 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-6 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-6 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-6 | Tristana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-6 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-6 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-6 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-7 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-7 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-7 | Tristana | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-7 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-7 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 5-1 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 5-1 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 5-1 | Tristana | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 5-1 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 5-1 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 5-2 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 5-2 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 5-2 | Tristana | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 5-2 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 5-2 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-5 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-5 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-5 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-5 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-6 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 2-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-6 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 2-6 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-6 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-7 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-7 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 2-7 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 2-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-7 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-7 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-1 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 3-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-1 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-1 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-1 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-1 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 3-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-2 | Rek'Sai | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 3 | 3-2 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-2 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-3 | Rek'Sai | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 3 | 3-3 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-3 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-4 | Rek'Sai | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 3 | 3-4 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-4 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-5 | Rek'Sai | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 3 | 3-5 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-6 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 3-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-6 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-6 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-7 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 3-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-7 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-1 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-1 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 4-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-1 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-2 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-2 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 4-3 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-3 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-3 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-3 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 4-4 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-4 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-4 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-4 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 4-5 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-5 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 4-6 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-6 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-6 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-6 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 4-6 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-6 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-6 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-6 | Aronguejo | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 4-6 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-6 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 4-7 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 4-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-7 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-7 | Vi | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 4-7 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-7 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 5-1 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 5-1 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-1 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-1 | Vi | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 5-1 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 5-1 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 5-2 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-2 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-2 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Vi | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 5-2 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 5-3 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-3 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-3 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-3 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-3 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-3 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 5-4 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-4 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-4 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-4 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-4 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-4 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-4 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 5-5 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-5 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-5 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-5 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 5-6 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-6 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-6 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-6 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-6 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-6 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-6 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-6 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 3 | 5-7 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-7 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-7 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-1 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 6-1 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-1 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 6-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 6-1 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-2 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 6-2 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-2 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 6-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 6-2 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-2 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-2 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-3 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 6-3 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 6-3 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-3 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-3 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-7 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 6-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 6-7 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 6-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 6-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 7-1 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 7-1 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 7-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 7-1 | Kha'Zix | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 7-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 7-1 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 7-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 7-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 7-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-5 | Rakan | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-5 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-5 | Yunara | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 2-5 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 4 | 2-6 | Rakan | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-6 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-7 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-7 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 2-7 | Akali | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 4 | 3-1 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-1 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 3-1 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-1 | Akali | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 4 | 3-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 3-2 | Master Yi | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 3-2 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 3-3 | Master Yi | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 3-3 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-4 | Master Yi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 3-4 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-4 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-4 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-4 | Master Yi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-4 | Yunara | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-5 | Master Yi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 3-5 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Master Yi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Master Yi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 3-6 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Master Yi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 3-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-7 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 3-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 3-7 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-7 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-7 | Master Yi | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 3-7 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-1 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-1 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-1 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-1 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-1 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 4 | 4-1 | Master Yi | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-1 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-2 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-2 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-2 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-2 | Master Yi | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-2 | Yunara | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-3 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-3 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-4 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-4 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-4 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-5 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-5 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-6 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-6 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-5 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-5 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-6 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-6 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-7 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-7 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-7 | Cassiopeia | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-7 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-1 | Cassiopeia | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-1 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-2 | Cassiopeia | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Rammus | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-2 | Kobuko | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 3-2 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-3 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-3 | Rammus | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-3 | Kobuko | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-3 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 3-3 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-4 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 3-4 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-4 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-4 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-4 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 3-4 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-4 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-5 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 3-5 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-5 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-5 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-5 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 3-5 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-5 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-6 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-6 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-6 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-6 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 3-6 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-7 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-7 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-7 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-7 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 3-7 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-1 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-1 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-1 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-1 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-1 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-2 | Teemo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-2 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-2 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-2 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-2 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 5 | 4-2 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-3 | Teemo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-3 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-3 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-3 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-3 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-4 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-4 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-4 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-4 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Teemo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 5 | 4-5 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-5 | Kog'Maw | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-5 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-5 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-5 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-5 | Teemo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 5 | 4-5 | Kobuko | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 5 | 4-6 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-6 | Kog'Maw | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-6 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-6 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-6 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-6 | Teemo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 5 | 4-7 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-7 | Kog'Maw | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-7 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-7 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-1 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-1 | Kog'Maw | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-1 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-1 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-1 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-2 | Kog'Maw | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-2 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-2 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-2 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-2 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-2 | Kobuko | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-2 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Kog'Maw | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-3 | Kobuko | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-3 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Kog'Maw | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 5 | 5-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-3 | Kobuko | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-3 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Tristana | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-6 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-6 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Tristana | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Tristana | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 3-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-2 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 3-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Cascalho | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 3-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Tristana | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 3-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Cascalho | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 3-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Tristana | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 3-3 | Rakan | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 3-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Cascalho | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 3-4 | Rakan | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 3-4 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-4 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Cascalho | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 3-5 | Rakan | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 3-5 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-5 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Cascalho | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 3-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-6 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-7 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-1 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 4-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-2 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 4-2 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-3 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 4-3 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-3 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 4-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-4 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 4-4 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-4 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-4 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-5 | Xayah | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 4-5 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-5 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-5 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 4-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-5 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-6 | Xayah | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 4-6 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-6 | Alistar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-6 | Lillia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Lillia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-7 | Alistar | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 4-7 | Lillia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-7 | Xayah | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 6 | 4-7 | Lillia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-1 | Alistar | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 5-1 | Lillia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-1 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 5-1 | Xayah | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 6 | 5-1 | Lillia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-1 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-2 | Alistar | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 5-2 | Lillia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-2 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-2 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-2 | Lillia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-2 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-2 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-2 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 2-7 | Azuporã | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 2-7 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 2-7 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 2-7 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-6 | Azuporã | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-6 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-6 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 3-6 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 3-6 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 3-6 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-6 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 3-6 | Kog'Maw | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 7 | 4-1 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-1 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-1 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-1 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-1 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-1 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-2 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-2 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-2 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-2 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-3 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-3 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-4 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-4 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-4 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-4 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-5 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-5 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-5 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-5 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-5 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-5 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-5 | Aronguejo | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-5 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-5 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-5 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-5 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-5 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-7 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-7 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-7 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-7 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-7 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-7 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-7 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-7 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-7 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-7 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-7 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-1 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 5-1 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-1 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-1 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-1 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 5-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-1 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-1 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-1 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-2 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 5-2 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-2 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-2 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-2 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 5-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-2 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-2 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-2 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-3 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 5-3 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-3 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-3 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-3 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 5-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-3 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-3 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-3 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-4 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 5-4 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-4 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-4 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-4 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 5-4 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 5-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-4 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-4 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 5-4 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-1 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-1 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 7 | 6-1 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 6-1 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 6-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-1 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-1 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-1 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-1 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-2 | Azuporã | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 6-2 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-2 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 7 | 6-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-2 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-2 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-2 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-3 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-3 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-3 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 7 | 6-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-3 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-3 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-3 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-4 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-4 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-4 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 6-4 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-4 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 7 | 6-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-4 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-4 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-4 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-6 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-6 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-6 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 6-6 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-6 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 7 | 6-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-6 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-6 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-6 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 7-1 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 7-1 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 7-1 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 7-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 7-1 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 7 | 7-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 7-1 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 7-1 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 7-1 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 8 | 2-5 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 2-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 2-5 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-5 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 2-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 2-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 8 | 2-6 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 2-7 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 2-7 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-1 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-1 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-3 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-3 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-4 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-4 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-4 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-4 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-5 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-5 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-5 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-6 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-6 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 8 | 3-6 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-6 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 3-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-6 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 3-6 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-7 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-7 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 3-7 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-7 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 3-7 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 3-7 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-1 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-1 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 4-1 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-1 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 4-1 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-1 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-1 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 4-1 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-2 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 4-2 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 4-2 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-2 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 4-2 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-2 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 4-2 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 4-2 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-2 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 4-2 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-3 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-3 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 4-3 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-3 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-3 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 4-3 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-3 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-3 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-3 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 4-4 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-4 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-4 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-4 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-4 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 4-4 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 4-4 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 4-5 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-5 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-5 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 4-5 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-5 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-5 | Cassiopeia | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 8 | 4-5 | LeBlanc | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 8 | 4-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 4-6 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-6 | Warwick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-6 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-6 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 4-6 | Rubrivira | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 4-6 | Cassiopeia | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 8 | 4-6 | LeBlanc | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |

Unidades preservadas com evidência observável: **1319**.
Classificações são proxies do snapshot (core, traits, presença no board, estrelas, itens e cópias). Não provam que o Planner preservou por investimento anterior; custo passado não é valor estratégico por si só.

### Thresholds e histerese configurados

| Parâmetro | Valor padrão no StrategicPlannerConfig |
|---|---:|
| Score mínimo de âncora | 0.01 |
| Vantagem mínima para ADAPT | 0.10 |
| Vantagem absoluta para mudança | 0.75 |
| Vantagem relativa para mudança | 20% |
| Revisões consecutivas desbloqueado | 2 |
| Revisões consecutivas bloqueado | 3 |

CompositionDirectionPolicy possui política separada: vantagem absoluta 0.75, relativa 20% e 3 atualizações consecutivas quando bloqueada. Os valores são defaults do código; a auditoria não presume configuração customizada em runtime.

### Evolução posterior dos KEEP

| Jogador | Round | Step | Próximo round | Δ HP | Δ Ouro | Δ Board | Próximos 2 rounds Δ HP / Ouro / Board | Colocação final |
|---|---|---:|---|---:|---:|---:|---|---:|
| Jogador 1 | 2-5 | 82 | 2-6 | 0.000 | -4.000 | 6.000 | 0.0 / -1.0 / 6.0 | 6 |
| Jogador 1 | 2-6 | 90 | 2-7 | 0.000 | 3.000 | 0.000 | -11.0 / 6.0 / 4.0 | 6 |
| Jogador 1 | 2-7 | 97 | 3-1 | -11.000 | 3.000 | 4.000 | -22.0 / 4.0 / 8.0 | 6 |
| Jogador 1 | 3-1 | 100 | 3-2 | -11.000 | 1.000 | 4.000 | -20.0 / 5.0 / 4.0 | 6 |
| Jogador 1 | 3-2 | 102 | 3-3 | -9.000 | 4.000 | 0.000 | -9.0 / 8.0 / 0.0 | 6 |
| Jogador 1 | 3-2 | 108 | 3-3 | -9.000 | 4.000 | 0.000 | -9.0 / 8.0 / 0.0 | 6 |
| Jogador 1 | 3-3 | 110 | 3-4 | 0.000 | 4.000 | 0.000 | 0.0 / 10.0 / 2.0 | 6 |
| Jogador 1 | 3-4 | 116 | 3-5 | 0.000 | 6.000 | 2.000 | 0.0 / 11.0 / 2.0 | 6 |
| Jogador 1 | 3-5 | 120 | 3-6 | 0.000 | 5.000 | 0.000 | 0.0 / 17.0 / 0.0 | 6 |
| Jogador 1 | 3-6 | 126 | 3-7 | 0.000 | 12.000 | 0.000 | -10.0 / 22.0 / 0.0 | 6 |
| Jogador 1 | 3-7 | 130 | 4-1 | -10.000 | 10.000 | 0.000 | -10.0 / 19.0 / 0.0 | 6 |
| Jogador 1 | 4-1 | 136 | 4-2 | 0.000 | 9.000 | 0.000 | -11.0 / 15.0 / 0.0 | 6 |
| Jogador 1 | 4-2 | 140 | 4-3 | -11.000 | 6.000 | 0.000 | -11.0 / 20.0 / 0.0 | 6 |
| Jogador 1 | 4-3 | 146 | 4-4 | 0.000 | 14.000 | 0.000 | -12.0 / 20.0 / 0.0 | 6 |
| Jogador 1 | 4-4 | 150 | 4-5 | -12.000 | 6.000 | 0.000 | -24.0 / 21.0 / 0.0 | 6 |
| Jogador 1 | 4-5 | 156 | 4-6 | -12.000 | 15.000 | 0.000 | -12.0 / 24.0 / 0.0 | 6 |
| Jogador 1 | 4-6 | 160 | 4-7 | 0.000 | 9.000 | 0.000 | -15.0 / 17.0 / 0.0 | 6 |
| Jogador 1 | 4-7 | 162 | 5-1 | -15.000 | 8.000 | 0.000 | -17.0 / 12.0 / -28.0 | 6 |
| Jogador 1 | 4-7 | 165 | 5-1 | -15.000 | 8.000 | 0.000 | -17.0 / 12.0 / -28.0 | 6 |
| Jogador 1 | 4-7 | 166 | 5-1 | -15.000 | 8.000 | 0.000 | -17.0 / 12.0 / -28.0 | 6 |
| Jogador 1 | 5-1 | 170 | 5-2 | -2.000 | 4.000 | -28.000 | None / None / None | 6 |
| Jogador 1 | 5-2 | 172 | — | — | — | — | None / None / None | 6 |
| Jogador 1 | 5-2 | 175 | — | — | — | — | None / None / None | 6 |
| Jogador 2 | 2-5 | 82 | 2-6 | -5.000 | 2.000 | 0.000 | -5.0 / 0.0 / 2.0 | 5 |
| Jogador 2 | 2-6 | 90 | 2-7 | 0.000 | -2.000 | 2.000 | -8.0 / 1.0 / 2.0 | 5 |
| Jogador 2 | 2-7 | 97 | 3-1 | -8.000 | 3.000 | 0.000 | -18.0 / -1.0 / 0.0 | 5 |
| Jogador 2 | 3-1 | 100 | 3-2 | -10.000 | -4.000 | 0.000 | -10.0 / -1.0 / 0.0 | 5 |
| Jogador 2 | 3-2 | 108 | 3-3 | 0.000 | 3.000 | 0.000 | 0.0 / 6.0 / 0.0 | 5 |
| Jogador 2 | 3-3 | 110 | 3-4 | 0.000 | 3.000 | 0.000 | 0.0 / 6.0 / 0.0 | 5 |
| Jogador 2 | 3-4 | 117 | 3-5 | 0.000 | 3.000 | 0.000 | -12.0 / 12.0 / 0.0 | 5 |
| Jogador 2 | 3-5 | 120 | 3-6 | -12.000 | 9.000 | 0.000 | -12.0 / 8.0 / 0.0 | 5 |
| Jogador 2 | 3-6 | 126 | 3-7 | 0.000 | -1.000 | 0.000 | -12.0 / 4.0 / 6.0 | 5 |
| Jogador 2 | 3-7 | 130 | 4-1 | -12.000 | 5.000 | 6.000 | -22.0 / 12.0 / 12.0 | 5 |
| Jogador 2 | 4-1 | 136 | 4-2 | -10.000 | 7.000 | 6.000 | -10.0 / 10.0 / 12.0 | 5 |
| Jogador 2 | 4-2 | 140 | 4-3 | 0.000 | 3.000 | 6.000 | 0.0 / 7.0 / 6.0 | 5 |
| Jogador 2 | 4-3 | 146 | 4-4 | 0.000 | 4.000 | 0.000 | 0.0 / 12.0 / 0.0 | 5 |
| Jogador 2 | 4-4 | 150 | 4-5 | 0.000 | 8.000 | 0.000 | 0.0 / 30.0 / 0.0 | 5 |
| Jogador 2 | 4-5 | 155 | 4-6 | 0.000 | 22.000 | 0.000 | 0.0 / 31.0 / 0.0 | 5 |
| Jogador 2 | 4-6 | 160 | 4-7 | 0.000 | 9.000 | 0.000 | -15.0 / 21.0 / 0.0 | 5 |
| Jogador 2 | 4-7 | 166 | 5-1 | -15.000 | 12.000 | 0.000 | -28.0 / 0.0 / -36.0 | 5 |
| Jogador 2 | 5-1 | 170 | 5-2 | -13.000 | -12.000 | -36.000 | None / None / None | 5 |
| Jogador 2 | 5-2 | 175 | — | — | — | — | None / None / None | 5 |
| Jogador 3 | 2-5 | 82 | 2-6 | 0.000 | 7.000 | 0.000 | 0.0 / 0.0 / 0.0 | — |
| Jogador 3 | 2-6 | 90 | 2-7 | 0.000 | -7.000 | 0.000 | 0.0 / 2.0 / 4.0 | — |
| Jogador 3 | 2-7 | 97 | 3-1 | 0.000 | 9.000 | 4.000 | 0.0 / 18.0 / 8.0 | — |
| Jogador 3 | 3-1 | 100 | 3-2 | 0.000 | 9.000 | 4.000 | 0.0 / 16.0 / 4.0 | — |
| Jogador 3 | 3-2 | 107 | 3-3 | 0.000 | 7.000 | 0.000 | 0.0 / 15.0 / 0.0 | — |
| Jogador 3 | 3-3 | 110 | 3-4 | 0.000 | 8.000 | 0.000 | -9.0 / 17.0 / 0.0 | — |
| Jogador 3 | 3-4 | 112 | 3-5 | -9.000 | 9.000 | 0.000 | -9.0 / 21.0 / 4.0 | — |
| Jogador 3 | 3-5 | 119 | 3-6 | 0.000 | 12.000 | 4.000 | 0.0 / 22.0 / 4.0 | — |
| Jogador 3 | 3-6 | 126 | 3-7 | 0.000 | 10.000 | 0.000 | 0.0 / 25.0 / 2.0 | — |
| Jogador 3 | 3-7 | 130 | 4-1 | 0.000 | 15.000 | 2.000 | 0.0 / 25.0 / 2.0 | — |
| Jogador 3 | 4-1 | 136 | 4-2 | 0.000 | 10.000 | 0.000 | 0.0 / 22.0 / -2.0 | — |
| Jogador 3 | 4-2 | 140 | 4-3 | 0.000 | 12.000 | -2.000 | 0.0 / 22.0 / 0.0 | — |
| Jogador 3 | 4-3 | 144 | 4-4 | 0.000 | 10.000 | 2.000 | 0.0 / 23.0 / 2.0 | — |
| Jogador 3 | 4-4 | 150 | 4-5 | 0.000 | 13.000 | 0.000 | 0.0 / 27.0 / 0.0 | — |
| Jogador 3 | 4-5 | 156 | 4-6 | 0.000 | 14.000 | 0.000 | 0.0 / 20.0 / 4.0 | — |
| Jogador 3 | 4-6 | 158 | 4-7 | 0.000 | 6.000 | 4.000 | 0.0 / 17.0 / 4.0 | — |
| Jogador 3 | 4-6 | 160 | 4-7 | 0.000 | 6.000 | 4.000 | 0.0 / 17.0 / 4.0 | — |
| Jogador 3 | 4-7 | 166 | 5-1 | 0.000 | 11.000 | 0.000 | 0.0 / 30.0 / 0.0 | — |
| Jogador 3 | 5-1 | 170 | 5-2 | 0.000 | 19.000 | 0.000 | 0.0 / 37.0 / 4.0 | — |
| Jogador 3 | 5-2 | 175 | 5-3 | 0.000 | 18.000 | 4.000 | 0.0 / 27.0 / 4.0 | — |
| Jogador 3 | 5-3 | 180 | 5-4 | 0.000 | 9.000 | 0.000 | 0.0 / 14.0 / 0.0 | — |
| Jogador 3 | 5-4 | 185 | 5-5 | 0.000 | 5.000 | 0.000 | 0.0 / 24.0 / 0.0 | — |
| Jogador 3 | 5-5 | 190 | 5-6 | 0.000 | 19.000 | 0.000 | 0.0 / 36.0 / 0.0 | — |
| Jogador 3 | 5-6 | 195 | 5-7 | 0.000 | 17.000 | 0.000 | 0.0 / 33.0 / 0.0 | — |
| Jogador 3 | 5-7 | 199 | 6-1 | 0.000 | 16.000 | 0.000 | 0.0 / 31.0 / 0.0 | — |
| Jogador 3 | 5-7 | 200 | 6-1 | 0.000 | 16.000 | 0.000 | 0.0 / 31.0 / 0.0 | — |
| Jogador 3 | 6-1 | 205 | 6-2 | 0.000 | 15.000 | 0.000 | 0.0 / 30.0 / 2.0 | — |
| Jogador 3 | 6-2 | 210 | 6-3 | 0.000 | 15.000 | 2.000 | 0.0 / 21.0 / 2.0 | — |
| Jogador 3 | 6-3 | 215 | 6-4 | 0.000 | 6.000 | 0.000 | -16.0 / 17.0 / 0.0 | — |
| Jogador 3 | 6-7 | 233 | — | — | — | — | None / None / None | — |
| Jogador 3 | 7-1 | 240 | — | — | — | — | None / None / None | — |
| Jogador 4 | 2-5 | 82 | 2-6 | -8.000 | 12.000 | 0.000 | -8.0 / 10.0 / 2.0 | 8 |
| Jogador 4 | 2-6 | 90 | 2-7 | 0.000 | -2.000 | 2.000 | -9.0 / 5.0 / 8.0 | 8 |
| Jogador 4 | 2-7 | 97 | 3-1 | -9.000 | 7.000 | 6.000 | -19.0 / 11.0 / 10.0 | 8 |
| Jogador 4 | 3-1 | 100 | 3-2 | -10.000 | 4.000 | 4.000 | -19.0 / 14.0 / 4.0 | 8 |
| Jogador 4 | 3-2 | 108 | 3-3 | -9.000 | 10.000 | 0.000 | -9.0 / 15.0 / 0.0 | 8 |
| Jogador 4 | 3-3 | 110 | 3-4 | 0.000 | 5.000 | 0.000 | -9.0 / 12.0 / 0.0 | 8 |
| Jogador 4 | 3-4 | 117 | 3-5 | -9.000 | 7.000 | 0.000 | -9.0 / 16.0 / 0.0 | 8 |
| Jogador 4 | 3-5 | 120 | 3-6 | 0.000 | 9.000 | 0.000 | 0.0 / 14.0 / -4.0 | 8 |
| Jogador 4 | 3-6 | 126 | 3-7 | 0.000 | 5.000 | -4.000 | -13.0 / 12.0 / -4.0 | 8 |
| Jogador 4 | 3-7 | 130 | 4-1 | -13.000 | 7.000 | 0.000 | -24.0 / 21.0 / 0.0 | 8 |
| Jogador 4 | 4-1 | 136 | 4-2 | -11.000 | 14.000 | 0.000 | -11.0 / 29.0 / 0.0 | 8 |
| Jogador 4 | 4-2 | 140 | 4-3 | 0.000 | 15.000 | 0.000 | 0.0 / 24.0 / 0.0 | 8 |
| Jogador 4 | 4-3 | 146 | 4-4 | 0.000 | 9.000 | 0.000 | -12.0 / 11.0 / 0.0 | 8 |
| Jogador 4 | 4-4 | 150 | 4-5 | -12.000 | 2.000 | 0.000 | -15.0 / 9.0 / -18.0 | 8 |
| Jogador 4 | 4-5 | 156 | 4-6 | -3.000 | 7.000 | -18.000 | None / None / None | 8 |
| Jogador 4 | 4-6 | 160 | — | — | — | — | None / None / None | 8 |
| Jogador 5 | 2-5 | 82 | 2-6 | -6.000 | 8.000 | 0.000 | -6.0 / 14.0 / 4.0 | 3 |
| Jogador 5 | 2-6 | 90 | 2-7 | 0.000 | 6.000 | 4.000 | -9.0 / 9.0 / 10.0 | 3 |
| Jogador 5 | 2-7 | 92 | 3-1 | -9.000 | 3.000 | 6.000 | -9.0 / 0.0 / 6.0 | 3 |
| Jogador 5 | 2-7 | 97 | 3-1 | -9.000 | 3.000 | 6.000 | -9.0 / 0.0 / 6.0 | 3 |
| Jogador 5 | 3-1 | 100 | 3-2 | 0.000 | -3.000 | 0.000 | -10.0 / 0.0 / 0.0 | 3 |
| Jogador 5 | 3-2 | 104 | 3-3 | -10.000 | 3.000 | 0.000 | -10.0 / 11.0 / 0.0 | 3 |
| Jogador 5 | 3-2 | 108 | 3-3 | -10.000 | 3.000 | 0.000 | -10.0 / 11.0 / 0.0 | 3 |
| Jogador 5 | 3-3 | 110 | 3-4 | 0.000 | 8.000 | 0.000 | -9.0 / 12.0 / 0.0 | 3 |
| Jogador 5 | 3-4 | 117 | 3-5 | -9.000 | 4.000 | 0.000 | -19.0 / 15.0 / 0.0 | 3 |
| Jogador 5 | 3-5 | 120 | 3-6 | -10.000 | 11.000 | 0.000 | -10.0 / 18.0 / 0.0 | 3 |
| Jogador 5 | 3-6 | 126 | 3-7 | 0.000 | 7.000 | 0.000 | 0.0 / 14.0 / -2.0 | 3 |
| Jogador 5 | 3-7 | 130 | 4-1 | 0.000 | 7.000 | -2.000 | 0.0 / 22.0 / -2.0 | 3 |
| Jogador 5 | 4-1 | 136 | 4-2 | 0.000 | 15.000 | 0.000 | -11.0 / 26.0 / 0.0 | 3 |
| Jogador 5 | 4-2 | 140 | 4-3 | -11.000 | 11.000 | 0.000 | -11.0 / 18.0 / 2.0 | 3 |
| Jogador 5 | 4-3 | 146 | 4-4 | 0.000 | 7.000 | 2.000 | -14.0 / 19.0 / 6.0 | 3 |
| Jogador 5 | 4-4 | 150 | 4-5 | -14.000 | 12.000 | 4.000 | -25.0 / 18.0 / 4.0 | 3 |
| Jogador 5 | 4-5 | 156 | 4-6 | -11.000 | 6.000 | 0.000 | -11.0 / 17.0 / 0.0 | 3 |
| Jogador 5 | 4-6 | 160 | 4-7 | 0.000 | 11.000 | 0.000 | 0.0 / 19.0 / 6.0 | 3 |
| Jogador 5 | 4-7 | 166 | 5-1 | 0.000 | 8.000 | 6.000 | 0.0 / 21.0 / 6.0 | 3 |
| Jogador 5 | 5-1 | 170 | 5-2 | 0.000 | 13.000 | 0.000 | -15.0 / 9.0 / -34.0 | 3 |
| Jogador 5 | 5-2 | 175 | 5-3 | -15.000 | -4.000 | -34.000 | None / None / None | 3 |
| Jogador 5 | 5-3 | 178 | — | — | — | — | None / None / None | 3 |
| Jogador 5 | 5-3 | 180 | — | — | — | — | None / None / None | 3 |
| Jogador 6 | 2-5 | 82 | 2-6 | -5.000 | 13.000 | 0.000 | -5.0 / 15.0 / 4.0 | 4 |
| Jogador 6 | 2-6 | 90 | 2-7 | 0.000 | 2.000 | 4.000 | 0.0 / 7.0 / 4.0 | 4 |
| Jogador 6 | 2-7 | 97 | 3-1 | 0.000 | 5.000 | 0.000 | -10.0 / 8.0 / 4.0 | 4 |
| Jogador 6 | 3-1 | 100 | 3-2 | -10.000 | 3.000 | 4.000 | -10.0 / 9.0 / 4.0 | 4 |
| Jogador 6 | 3-2 | 108 | 3-3 | 0.000 | 6.000 | 0.000 | 0.0 / -2.0 / 0.0 | 4 |
| Jogador 6 | 3-3 | 110 | 3-4 | 0.000 | -8.000 | 0.000 | 0.0 / 2.0 / 0.0 | 4 |
| Jogador 6 | 3-4 | 117 | 3-5 | 0.000 | 10.000 | 0.000 | -10.0 / 17.0 / 0.0 | 4 |
| Jogador 6 | 3-5 | 120 | 3-6 | -10.000 | 7.000 | 0.000 | -10.0 / 20.0 / 0.0 | 4 |
| Jogador 6 | 3-6 | 126 | 3-7 | 0.000 | 13.000 | 0.000 | 0.0 / 23.0 / 0.0 | 4 |
| Jogador 6 | 3-7 | 130 | 4-1 | 0.000 | 10.000 | 0.000 | -11.0 / 15.0 / -4.0 | 4 |
| Jogador 6 | 4-1 | 136 | 4-2 | -11.000 | 5.000 | -4.000 | -22.0 / 18.0 / -4.0 | 4 |
| Jogador 6 | 4-2 | 140 | 4-3 | -11.000 | 13.000 | 0.000 | -11.0 / 22.0 / 0.0 | 4 |
| Jogador 6 | 4-3 | 143 | 4-4 | 0.000 | 9.000 | 0.000 | 0.0 / 18.0 / 6.0 | 4 |
| Jogador 6 | 4-3 | 146 | 4-4 | 0.000 | 9.000 | 0.000 | 0.0 / 18.0 / 6.0 | 4 |
| Jogador 6 | 4-4 | 150 | 4-5 | 0.000 | 9.000 | 6.000 | 0.0 / 16.0 / 14.0 | 4 |
| Jogador 6 | 4-5 | 156 | 4-6 | 0.000 | 7.000 | 8.000 | 0.0 / 15.0 / 10.0 | 4 |
| Jogador 6 | 4-6 | 160 | 4-7 | 0.000 | 8.000 | 2.000 | -17.0 / 12.0 / 6.0 | 4 |
| Jogador 6 | 4-7 | 166 | 5-1 | -17.000 | 4.000 | 4.000 | -30.0 / 3.0 / -34.0 | 4 |
| Jogador 6 | 5-1 | 170 | 5-2 | -13.000 | -1.000 | -38.000 | None / None / None | 4 |
| Jogador 6 | 5-2 | 175 | — | — | — | — | None / None / None | 4 |
| Jogador 7 | 2-7 | 97 | 3-1 | 0.000 | 5.000 | 0.000 | 0.0 / 2.0 / 0.0 | — |
| Jogador 7 | 3-6 | 126 | 3-7 | 0.000 | 20.000 | 0.000 | 0.0 / 33.0 / 0.0 | — |
| Jogador 7 | 4-1 | 136 | 4-2 | 0.000 | 17.000 | 0.000 | 0.0 / 24.0 / 2.0 | — |
| Jogador 7 | 4-2 | 140 | 4-3 | 0.000 | 7.000 | 2.000 | 0.0 / 19.0 / 2.0 | — |
| Jogador 7 | 4-3 | 142 | 4-4 | 0.000 | 12.000 | 0.000 | 0.0 / 24.0 / 0.0 | — |
| Jogador 7 | 4-3 | 146 | 4-4 | 0.000 | 12.000 | 0.000 | 0.0 / 24.0 / 0.0 | — |
| Jogador 7 | 4-4 | 150 | 4-5 | 0.000 | 12.000 | 0.000 | 0.0 / 24.0 / 0.0 | — |
| Jogador 7 | 4-5 | 152 | 4-6 | 0.000 | 12.000 | 0.000 | 0.0 / 32.0 / 0.0 | — |
| Jogador 7 | 4-5 | 156 | 4-6 | 0.000 | 12.000 | 0.000 | 0.0 / 32.0 / 0.0 | — |
| Jogador 7 | 4-7 | 166 | 5-1 | 0.000 | 12.000 | 0.000 | 0.0 / 25.0 / 0.0 | — |
| Jogador 7 | 5-1 | 170 | 5-2 | 0.000 | 13.000 | 0.000 | 0.0 / 28.0 / 0.0 | — |
| Jogador 7 | 5-2 | 175 | 5-3 | 0.000 | 15.000 | 0.000 | 0.0 / 25.0 / 0.0 | — |
| Jogador 7 | 5-3 | 180 | 5-4 | 0.000 | 10.000 | 0.000 | -14.0 / 22.0 / 0.0 | — |
| Jogador 7 | 5-4 | 185 | 5-5 | -14.000 | 12.000 | 0.000 | -28.0 / 22.0 / 0.0 | — |
| Jogador 7 | 6-1 | 205 | 6-2 | -17.000 | 16.000 | -6.000 | -33.0 / 22.0 / 6.0 | — |
| Jogador 7 | 6-2 | 210 | 6-3 | -16.000 | 6.000 | 12.000 | -16.0 / 15.0 / 12.0 | — |
| Jogador 7 | 6-3 | 215 | 6-4 | 0.000 | 9.000 | 0.000 | 0.0 / 19.0 / 0.0 | — |
| Jogador 7 | 6-4 | 219 | 6-5 | 0.000 | 10.000 | 0.000 | 0.0 / 22.0 / 0.0 | — |
| Jogador 7 | 6-6 | 230 | 6-7 | 0.000 | 11.000 | 0.000 | None / None / None | — |
| Jogador 7 | 7-1 | 240 | — | — | — | — | None / None / None | — |
| Jogador 8 | 2-5 | 82 | 2-6 | 0.000 | 4.000 | 0.000 | 0.0 / 12.0 / 0.0 | 7 |
| Jogador 8 | 2-6 | 90 | 2-7 | 0.000 | 8.000 | 0.000 | 0.0 / 18.0 / 0.0 | 7 |
| Jogador 8 | 2-7 | 97 | 3-1 | 0.000 | 10.000 | 0.000 | 0.0 / 16.0 / 0.0 | 7 |
| Jogador 8 | 3-1 | 100 | 3-2 | 0.000 | 6.000 | 0.000 | -9.0 / 16.0 / 0.0 | 7 |
| Jogador 8 | 3-2 | 108 | 3-3 | -9.000 | 10.000 | 0.000 | -9.0 / 12.0 / 4.0 | 7 |
| Jogador 8 | 3-3 | 110 | 3-4 | 0.000 | 2.000 | 4.000 | -9.0 / 12.0 / 4.0 | 7 |
| Jogador 8 | 3-4 | 117 | 3-5 | -9.000 | 10.000 | 0.000 | -21.0 / 19.0 / 2.0 | 7 |
| Jogador 8 | 3-5 | 120 | 3-6 | -12.000 | 9.000 | 2.000 | -12.0 / 16.0 / 4.0 | 7 |
| Jogador 8 | 3-6 | 123 | 3-7 | 0.000 | 7.000 | 2.000 | -11.0 / 19.0 / 2.0 | 7 |
| Jogador 8 | 3-6 | 126 | 3-7 | 0.000 | 7.000 | 2.000 | -11.0 / 19.0 / 2.0 | 7 |
| Jogador 8 | 3-7 | 130 | 4-1 | -11.000 | 12.000 | 0.000 | -22.0 / 20.0 / 0.0 | 7 |
| Jogador 8 | 4-1 | 136 | 4-2 | -11.000 | 8.000 | 0.000 | -25.0 / 23.0 / 0.0 | 7 |
| Jogador 8 | 4-2 | 138 | 4-3 | -14.000 | 15.000 | 0.000 | -14.0 / 32.0 / 0.0 | 7 |
| Jogador 8 | 4-2 | 140 | 4-3 | -14.000 | 15.000 | 0.000 | -14.0 / 32.0 / 0.0 | 7 |
| Jogador 8 | 4-3 | 146 | 4-4 | 0.000 | 17.000 | 0.000 | -12.0 / 20.0 / -4.0 | 7 |
| Jogador 8 | 4-4 | 150 | 4-5 | -12.000 | 3.000 | -4.000 | -18.0 / -5.0 / -24.0 | 7 |
| Jogador 8 | 4-5 | 156 | 4-6 | -6.000 | -8.000 | -20.000 | None / None / None | 7 |
| Jogador 8 | 4-6 | 160 | — | — | — | — | None / None / None | 7 |

A evolução posterior é associação temporal, não atribuição causal à recomendação shadow.


### Auditoria de INSUFFICIENT_EVIDENCE

| Jogador | Round | Step | Motivo específico | Geração de candidatos | Direção atual | Viável atual | Score atual | Score âncora | Vantagem | Mín. ADAPT | Limite PIVOT | Conf. âncora | Conf. direção atual | Âncora disponível | Filtros (considerados/gerados/catálogo ausente/planos vazios/âncora ausente) |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Jogador 1 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-3 | 26 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-1 | 48 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-3 | 68 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-4 | 76 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-5 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-3 | 32 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-4 | 40 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-3 | 69 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-4 | 78 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-5 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 16 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-1 | 4 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-3 | 32 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-4 | 38 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-3 | 65 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-4 | 78 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 16 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-5 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 18 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-1 | 4 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-3 | 26 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-1 | 48 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-3 | 69 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-4 | 78 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-5 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-3 | 23 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 9 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-1 | 49 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-3 | 69 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-4 | 78 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-5 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-3 | 32 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-4 | 35 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-1 | 48 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-2 | 56 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-3 | 67 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-4 | 78 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-5 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 16 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-1 | 2 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-3 | 27 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-4 | 38 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-1 | 48 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-3 | 69 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-2 | 20 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-3 | 24 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-4 | 39 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 7 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-3 | 69 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-4 | 78 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-5 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 18 / 0 / 0 / 0 / 0 |

**Motivos agregados:** unavailable=8; no_initial_anchor_available=70
**Motivos de geração agregados:** unavailable=8; no_cost_four_or_five_anchor=70
**Viabilidade da direção atual:** not_viable=78

Confiança da âncora e confiança da direção atual são derivadas de score e não são probabilidades calibradas. Snapshots por ação podem repetir a mesma revisão; não devem ser contados como revisões independentes.
