# Strategic Planner — recomendações

Direção atual e recomendação do planner são mantidas separadas. O planner não altera o compromisso ativo nesta fase.

> Recomendações em shadow mode são diagnósticos heurísticos. Elas não foram executadas nem alteraram a ação do PPO.

| Jogador | Round | Steps observados | Observações | Direção ativa | Decisão | Direção alvo | Âncora | Confiança | Custo de transição | Preservadas | Substituíveis | Candidatos avaliados (ID/direção/score/resultado) | Motivo |
|---|---|---|---:|---|---|---:|---:|---:|---:|---|---|---|---|
| Jogador 1 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 1 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 6 |  |  | insufficient_evidence |
| Jogador 1 | 1-2 | 13–21 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 6, 0 |  |  | insufficient_evidence |
| Jogador 1 | 1-3 | 23–27 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 0, 6 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 2-1 | 43–50 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 0, 6, 7 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 2-2 | 52–59 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 0, 6 | 12 |  | insufficient_evidence |
| Jogador 1 | 2-3 | 61–67 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 0, 6 | 12, 23 |  | insufficient_evidence |
| Jogador 1 | 2-4 | 70–72 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 7, 7, 6, 0 | 12, 23, 33 |  | insufficient_evidence |
| Jogador 1 | 2-5 | 74–74 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 0 | 12, 23, 33 |  | insufficient_evidence |
| Jogador 1 | 2-5 | 75–75 | 1 | Inferno | ABANDON | — | -1 | 0.650 | 0.000 | 7 | 12, 0, 6, 7, 23, 23, 0, 33 |  | board_deficit |
| Jogador 1 | 2-5 | 76–80 | 5 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 23, 23 | 12 |  | board_advantage |
| Jogador 1 | 2-6 | 82–87 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 12, 0 | 23, 23, 34 |  | board_advantage |
| Jogador 1 | 2-7 | 89–90 | 2 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 23, 0, 6, 23, 7, 0 | 12, 34 |  | board_advantage |
| Jogador 1 | 3-1 | 92–97 | 6 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 23, 0, 23, 6, 7, 0 | 12, 34 |  | board_advantage |
| Jogador 1 | 3-2 | 99–100 | 2 | Inferno | ADAPT | Sabugueiro | 45 | 0.650 | 0.222 | 0, 6, 12, 7, 0 | 23, 23, 35, 34 | 45:Sabugueiro:41.369:selected_best_candidate, 45:Carrasco:36.111:not_best_scoring_candidate | anchor_opportunity |
| Jogador 1 | 3-3 | 102–105 | 4 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 23, 0, 6, 7, 23, 0 | 12, 35, 31, 34 |  | board_advantage |
| Jogador 1 | 3-4 | 109–110 | 2 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 23, 0, 6, 7, 23, 0 | 12, 35, 31, 34, 15 |  | board_advantage |
| Jogador 1 | 3-5 | 112–117 | 6 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 0, 6, 7, 0, 23 | 31, 12, 15, 35, 1, 34 |  | board_advantage |
| Jogador 1 | 3-6 | 119–120 | 2 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.545 | 0, 6, 7, 0, 23 | 31, 12, 15, 35, 1, 34, 12 | 49:Primordial:35.691:valid_but_not_selected, 49:Adaptador:36.095:selected_best_candidate | board_advantage |
| Jogador 1 | 3-7 | 122–126 | 5 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.400 | 0, 7, 6, 0, 23 | 31, 12, 15, 35, 1, 34, 12, 49, 20 | 49:Primordial:35.755:selected_best_candidate, 49:Adaptador:33.835:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-1 | 128–130 | 3 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.667 | 0, 7, 6, 0, 23 | 31, 15, 12, 35, 1, 34, 12, 49, 20 | 49:Primordial:35.507:valid_but_not_selected, 49:Adaptador:35.584:selected_best_candidate | board_advantage |
| Jogador 1 | 4-2 | 132–136 | 5 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.400 | 7, 6, 23, 49 | 31, 15, 12, 35, 34, 36, 12, 25, 20 | 49:Primordial:34.038:selected_best_candidate, 49:Adaptador:31.558:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-3 | 138–140 | 3 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.400 | 7, 6, 23, 6, 23, 49 | 31, 15, 35, 12, 34, 36, 12, 25, 20 | 49:Primordial:34.383:selected_best_candidate, 49:Adaptador:32.567:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-4 | 142–146 | 5 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.667 | 7, 6, 23, 6, 23, 49 | 31, 15, 35, 12, 34, 36, 12, 30, 20 | 49:Primordial:37.095:selected_best_candidate, 49:Adaptador:36.290:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-5 | 148–150 | 2 | Inferno | KEEP | Inferno | 47 | 0.950 | 0.667 | 23, 7, 6, 6, 23, 49 | 31, 15, 35, 12, 47, 34, 36, 12, 30, 53 | 47:Espinhos Negros:36.309:selected_best_candidate, 47:Monólito:34.043:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-5 | 149–149 | 1 | Inferno | KEEP | Inferno | 53 | 0.950 | 0.400 | 23, 7, 6, 6, 23, 49 | 31, 15, 35, 12, 47, 34, 36, 12, 30 | 53:Flora Fatalis:37.501:valid_but_not_selected, 53:Carrasco:39.334:selected_best_candidate | board_advantage |
| Jogador 1 | 4-6 | 152–156 | 5 | Inferno | KEEP | Inferno | 47 | 0.950 | 0.545 | 23, 7, 6, 6, 23, 49 | 31, 15, 35, 12, 47, 31, 35, 12, 30, 53 | 47:Espinhos Negros:38.259:selected_best_candidate, 47:Monólito:36.102:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-7 | 158–158 | 1 | Inferno | KEEP | Inferno | 47 | 0.950 | 0.545 | 23, 7, 6, 6, 23, 49 | 31, 35, 15, 12, 47, 31, 35, 12, 30, 53 | 47:Espinhos Negros:37.338:selected_best_candidate, 47:Monólito:35.074:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-7 | 159–160 | 2 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.545 | 23, 7, 6, 6, 23, 49 | 31, 35, 15, 12, 33, 31, 35, 12, 30, 53 | 49:Primordial:37.365:selected_best_candidate, 49:Adaptador:35.487:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-1 | 162–166 | 5 | Inferno | KEEP | Inferno | 51 | 0.950 | 0.545 | 23, 7, 6, 6, 23, 49 | 35, 15, 12, 31, 33, 35, 12, 30, 53 | 51:Florescer:37.349:valid_but_not_selected, 51:Lutador:37.863:selected_best_candidate | board_advantage |
| Jogador 1 | 5-2 | 168–170 | 3 | Inferno | ADAPT | Enfeitiçador | 41 | 0.650 | 0.545 | 31, 7, 6, 6, 30, 49 | 23, 35, 15, 12, 33, 35, 12, 23, 53 | 41:Florescer:40.642:valid_but_not_selected, 41:Enfeitiçador:42.298:selected_best_candidate | anchor_opportunity |
| Jogador 1 | 5-3 | 172–175 | 4 | Inferno | KEEP | Inferno | 42 | 0.950 | 0.400 | 31, 7, 6, 23, 6, 42, 49 | 35, 15, 12, 33, 35, 12, 30, 53 | 42:Inferno:43.335:selected_best_candidate, 42:Colosso:43.080:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-4 | 177–180 | 3 | Inferno | KEEP | Inferno | 42 | 0.950 | 0.400 | 31, 7, 23, 6, 6, 23, 42, 49 | 35, 15, 33, 35, 30, 53 | 42:Inferno:37.847:valid_but_not_selected, 42:Colosso:39.511:selected_best_candidate | board_advantage |
| Jogador 1 | 5-4 | 178–178 | 1 | Inferno | KEEP | Inferno | 42 | 0.950 | 0.400 | 31, 7, 23, 6, 6, 42, 49 | 35, 15, 12, 33, 35, 30, 53 | 42:Inferno:42.644:selected_best_candidate, 42:Colosso:42.458:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-5 | 182–185 | 4 | Inferno | KEEP | Inferno | 62 | 0.950 | 0.545 | 31, 7, 23, 6, 6, 23, 42, 49 | 35, 15, 15, 62, 33, 35, 30, 20 | 62:Avatar:39.984:selected_best_candidate, 42:Inferno:37.502:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-6 | 187–189 | 2 | Inferno | KEEP | Inferno | 42 | 0.950 | 0.400 | 31, 7, 23, 6, 6, 23, 42, 49 | 35, 15, 15, 62, 33, 35, 30 | 62:Avatar:37.921:valid_but_not_selected, 42:Inferno:38.718:selected_best_candidate | board_advantage |
| Jogador 1 | 5-6 | 188–190 | 2 | Inferno | KEEP | Inferno | 62 | 0.950 | 0.222 | 31, 7, 23, 6, 6, 23, 42, 49 | 35, 15, 15, 62, 33, 35, 30, 29 | 62:Avatar:39.409:selected_best_candidate, 42:Inferno:39.001:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-7 | 192–194 | 2 | Inferno | KEEP | Inferno | 42 | 0.950 | 0.400 | 31, 7, 23, 6, 6, 23, 42, 49 | 35, 15, 15, 62, 33, 35, 30 | 62:Avatar:37.975:valid_but_not_selected, 42:Inferno:38.663:selected_best_candidate | board_advantage |
| Jogador 1 | 5-7 | 193–195 | 2 | Inferno | KEEP | Inferno | 62 | 0.950 | 0.222 | 31, 7, 23, 6, 6, 23, 42, 49 | 35, 15, 15, 62, 33, 35, 30, 32 | 62:Avatar:39.388:selected_best_candidate, 42:Inferno:39.127:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 6-1 | 197–200 | 3 | Inferno | KEEP | Inferno | 42 | 0.950 | 0.400 | 31, 7, 23, 6, 6, 23, 42, 49, 23 | 35, 15, 15, 33, 35, 30 | 42:Inferno:39.192:selected_best_candidate, 42:Colosso:37.987:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 6-1 | 198–198 | 1 | Inferno | KEEP | Inferno | 62 | 0.950 | 0.222 | 31, 7, 23, 6, 6, 23, 42, 49, 23 | 35, 15, 15, 62, 33, 35, 30 | 62:Avatar:39.746:selected_best_candidate, 42:Inferno:39.182:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 6-2 | 202–205 | 4 | Inferno | KEEP | Inferno | 53 | 0.950 | 0.400 | 31, 7, 23, 6, 35, 7, 0, 23, 42, 49, 23 | 15, 15, 33, 30 | 53:Flora Fatalis:38.197:valid_but_not_selected, 53:Carrasco:40.351:selected_best_candidate | board_advantage |
| Jogador 1 | 6-3 | 207–210 | 4 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.400 | 31, 7, 23, 6, 35, 49, 0, 23, 42, 49, 23 | 15, 15, 33, 30 | 49:Primordial:39.247:valid_but_not_selected, 49:Adaptador:43.301:selected_best_candidate | board_advantage |
| Jogador 1 | 6-4 | 212–214 | 3 | Inferno | ADAPT | Primordial | 52 | 0.650 | 0.400 | 31, 7, 23, 6, 35, 49, 49 | 15, 15, 33, 33, 0, 23, 30, 42, 23 | 52:Primordial:46.269:selected_best_candidate, 52:Caçador:43.419:not_best_scoring_candidate | anchor_opportunity |
| Jogador 1 | 6-4 | 215–215 | 1 | Inferno | KEEP | Inferno | 52 | 0.950 | 0.400 | 31, 7, 23, 6, 35, 49, 23, 42, 49, 23 | 15, 15, 33, 33, 30 | 52:Primordial:43.651:selected_best_candidate, 52:Caçador:42.144:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 6-5 | 217–220 | 3 | Inferno | KEEP | Inferno | 54 | 0.950 | 0.545 | 31, 7, 23, 6, 35, 49, 23, 42, 49, 23 | 15, 15, 54, 53, 30 | 54:Dama de Espinhos:33.173:valid_but_not_selected, 54:Invocador:38.323:selected_best_candidate | board_advantage |
| Jogador 1 | 6-5 | 218–218 | 1 | Inferno | KEEP | Inferno | 53 | 0.950 | 0.667 | 31, 7, 23, 6, 35, 49, 23, 42, 49, 23 | 15, 15, 54, 33, 30 | 53:Flora Fatalis:36.035:valid_but_not_selected, 53:Carrasco:37.041:selected_best_candidate | board_advantage |
| Jogador 1 | 6-6 | 222–225 | 4 | Inferno | KEEP | Inferno | 51 | 0.950 | 0.545 | 31, 7, 23, 6, 35, 49, 7, 23, 42, 49, 23 | 15, 15, 54, 30 | 51:Florescer:36.566:selected_best_candidate, 51:Lutador:35.216:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 2 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 11 |  |  | insufficient_evidence |
| Jogador 2 | 1-2 | 13–21 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 11, 11 |  |  | insufficient_evidence |
| Jogador 2 | 1-3 | 23–31 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 11, 4 |  |  | insufficient_evidence |
| Jogador 2 | 1-4 | 34–40 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 11, 11, 11 | 13 |  | insufficient_evidence |
| Jogador 2 | 2-1 | 43–50 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 11 | 0, 40 |  | insufficient_evidence |
| Jogador 2 | 2-2 | 52–59 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 11, 7 | 12, 0, 22, 40 |  | insufficient_evidence |
| Jogador 2 | 2-3 | 61–68 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 0, 22, 8, 40 |  | insufficient_evidence |
| Jogador 2 | 2-4 | 70–72 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 12, 0, 22, 8, 40, 30 |  | insufficient_evidence |
| Jogador 2 | 2-5 | 74–74 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 12, 0, 22, 8, 40, 30 |  | insufficient_evidence |
| Jogador 2 | 2-5 | 75–75 | 1 | Feérico | ABANDON | — | -1 | 0.650 | 0.000 |  | 7, 4, 12, 7, 11, 12, 0, 22, 8, 40, 30, 39 |  | board_deficit |
| Jogador 2 | 2-5 | 76–80 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 12, 7, 11, 12, 39 | 8, 30 |  | board_advantage |
| Jogador 2 | 2-6 | 82–87 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 12, 7, 11, 12, 39 | 8, 30 |  | board_advantage |
| Jogador 2 | 2-7 | 89–90 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 12, 7, 11, 12, 39 | 2, 8, 8, 30 |  | board_advantage |
| Jogador 2 | 3-1 | 92–97 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 12, 7, 11, 12 | 8, 8 |  | board_advantage |
| Jogador 2 | 3-2 | 99–100 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 12 | 8 |  | board_advantage |
| Jogador 2 | 3-3 | 102–107 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 8, 28, 25, 35, 8 |  | board_advantage |
| Jogador 2 | 3-4 | 109–110 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 12 | 8, 28, 35, 8 |  | board_advantage |
| Jogador 2 | 3-5 | 112–117 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 12 | 8, 28, 8, 37 |  | board_advantage |
| Jogador 2 | 3-6 | 119–120 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 12 | 8, 28, 8, 37 |  | board_advantage |
| Jogador 2 | 3-7 | 122–126 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 12, 39 | 8, 28, 28, 8, 37, 32, 34, 14 |  | board_advantage |
| Jogador 2 | 4-1 | 128–130 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 12, 39 | 8, 28, 28, 8, 37, 32, 34, 14 |  | board_advantage |
| Jogador 2 | 4-2 | 132–136 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 12, 39, 39 | 8, 28, 28, 8, 37, 32 |  | board_advantage |
| Jogador 2 | 4-3 | 138–140 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 12, 39, 39 | 8, 28, 28, 8, 37, 32, 24 |  | board_advantage |
| Jogador 2 | 4-4 | 142–146 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 4, 7, 39, 11, 11, 12, 39 | 28, 27, 28, 37, 32 |  | board_advantage |
| Jogador 2 | 4-5 | 148–150 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 4, 39, 11, 11, 11, 12, 7, 39 | 28, 27, 28, 37 |  | board_advantage |
| Jogador 3 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 3 | 1-1 | 2–4 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0 |  |  | insufficient_evidence |
| Jogador 3 | 1-2 | 13–21 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 0, 13 |  |  | insufficient_evidence |
| Jogador 3 | 1-3 | 23–31 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 8, 0 |  |  | insufficient_evidence |
| Jogador 3 | 1-4 | 34–38 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 0 | 18, 1 |  | insufficient_evidence |
| Jogador 3 | 2-1 | 43–50 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 8, 0 | 15, 18, 1, 23 |  | insufficient_evidence |
| Jogador 3 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8 | 15, 18, 1, 23, 15, 29 |  | insufficient_evidence |
| Jogador 3 | 2-3 | 61–64 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8 | 15, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-4 | 70–72 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8, 8 | 15, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-5 | 74–74 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8, 8 | 15, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-5 | 75–75 | 1 | Colosso | ABANDON | — | -1 | 0.650 | 0.000 | 0 | 15, 13, 18, 8, 13, 1, 23, 15, 29, 21, 7, 8 |  | board_deficit |
| Jogador 3 | 2-5 | 76–80 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 0, 13, 8, 13, 7, 8, 15 | 29, 18, 23, 1, 21 |  | board_advantage |
| Jogador 3 | 2-6 | 82–87 | 6 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 8, 0, 15, 7, 8, 15 | 29, 18, 26, 23, 1, 21 |  | board_advantage |
| Jogador 3 | 2-7 | 89–90 | 2 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 8, 0, 15, 15, 7, 8, 15 | 18, 29, 26, 23, 1, 21 |  | board_advantage |
| Jogador 3 | 3-1 | 92–97 | 6 | Devastador | KEEP | Devastador | -1 | 0.000 | 0.000 | 13, 29, 0, 1, 21, 8 | 18, 15, 26, 23, 15, 40, 7 |  | board_advantage |
| Jogador 3 | 3-2 | 99–100 | 2 | Devastador | KEEP | Devastador | -1 | 0.000 | 0.000 | 29, 13, 0, 1, 21, 8, 8 | 18, 15, 26, 23, 15, 40, 7 |  | board_advantage |
| Jogador 3 | 3-3 | 102–107 | 6 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 0, 29, 13, 1, 21, 8, 25 | 18, 40, 15, 23, 15, 7 | 52:Primordial:38.992:valid_but_not_selected, 52:Caçador:39.604:selected_best_candidate | board_advantage |
| Jogador 3 | 3-4 | 109–110 | 2 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 52, 29, 13, 0, 1, 21, 8, 25 | 18, 40, 15, 23, 15, 7 | 52:Primordial:39.532:selected_best_candidate, 52:Caçador:38.766:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-5 | 112–117 | 6 | Devastador | KEEP | Devastador | 49 | 0.950 | 0.545 | 52, 0, 13, 29, 1, 21, 8, 25 | 40, 18, 15, 40, 33, 15, 7 | 49:Primordial:38.560:valid_but_not_selected, 49:Adaptador:41.989:selected_best_candidate | board_advantage |
| Jogador 3 | 3-6 | 119–120 | 2 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 52, 0, 13, 29, 1, 21, 8, 25 | 40, 18, 15, 40, 15, 7 | 52:Primordial:39.654:selected_best_candidate, 52:Caçador:36.489:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-7 | 122–126 | 5 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 52, 0, 1, 13, 29, 1, 21, 25 | 18, 15, 32, 15, 7, 40 | 52:Primordial:38.286:selected_best_candidate, 52:Caçador:36.727:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-1 | 128–130 | 3 | Devastador | KEEP | Devastador | 53 | 0.950 | 0.857 | 52, 0, 1, 13, 29, 1, 21, 25 | 18, 15, 32, 15, 2, 7, 40 | 53:Flora Fatalis:30.995:valid_but_not_selected, 53:Carrasco:34.501:selected_best_candidate | board_advantage |
| Jogador 3 | 4-2 | 132–136 | 5 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 52, 0, 1, 13, 29, 1, 21, 25, 25 | 18, 15, 15, 18, 7 | 52:Primordial:37.413:valid_but_not_selected, 52:Caçador:40.239:selected_best_candidate | board_advantage |
| Jogador 3 | 4-3 | 138–140 | 3 | Devastador | KEEP | Devastador | 51 | 0.950 | 0.769 | 52, 0, 1, 13, 29, 1, 21, 25, 25 | 18, 15, 27, 15, 18, 7 | 51:Florescer:38.138:selected_best_candidate, 51:Lutador:34.963:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-4 | 142–146 | 5 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 52, 1, 0, 13, 29, 1, 21, 25, 25 | 18, 15, 20, 15, 18, 7 | 52:Primordial:37.651:valid_but_not_selected, 52:Caçador:38.515:selected_best_candidate | board_advantage |
| Jogador 3 | 4-5 | 148–150 | 3 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 0, 1, 52, 13, 29, 21, 1, 21, 25, 25 | 18, 15, 15, 18, 7 | 52:Primordial:38.979:valid_but_not_selected, 52:Caçador:39.972:selected_best_candidate | board_advantage |
| Jogador 3 | 4-6 | 152–156 | 5 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 0, 1, 52, 13, 29, 0, 21, 1, 21, 25, 25 | 18, 18, 7 | 52:Primordial:37.252:valid_but_not_selected, 52:Caçador:38.794:selected_best_candidate | board_advantage |
| Jogador 3 | 4-7 | 158–160 | 3 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 0, 1, 52, 13, 29, 0, 1, 21, 25, 25 | 18, 18, 7 | 52:Primordial:38.620:valid_but_not_selected, 52:Caçador:39.451:selected_best_candidate | board_advantage |
| Jogador 3 | 5-1 | 162–166 | 5 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 0, 1, 0, 52, 13, 29, 1, 21, 25, 25 | 22, 18, 9, 7 | 52:Primordial:39.928:valid_but_not_selected, 52:Caçador:41.874:selected_best_candidate | board_advantage |
| Jogador 3 | 5-2 | 168–170 | 3 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 0, 1, 0, 52, 13, 29, 1, 21, 25, 25 | 22, 7, 9, 12, 7 | 52:Primordial:37.306:valid_but_not_selected, 52:Caçador:39.239:selected_best_candidate | board_advantage |
| Jogador 3 | 5-3 | 172–175 | 4 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.400 | 0, 1, 0, 52, 13, 29, 1, 25, 25 | 22, 7, 35, 9, 36, 7 | 52:Primordial:36.737:valid_but_not_selected, 52:Caçador:41.031:selected_best_candidate | board_advantage |
| Jogador 3 | 5-4 | 177–180 | 4 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 0, 0, 52, 13, 29, 21, 25, 25 | 7, 35, 9, 36, 7 | 52:Primordial:38.253:valid_but_not_selected, 52:Caçador:38.539:selected_best_candidate | board_advantage |
| Jogador 3 | 5-5 | 182–183 | 2 | Devastador | KEEP | Devastador | 47 | 0.950 | 0.667 | 0, 0, 52, 13, 29, 21, 25, 25 | 7, 33, 35, 9, 36, 7 | 47:Espinhos Negros:38.761:selected_best_candidate, 47:Monólito:34.313:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 5-5 | 184–185 | 2 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 0, 0, 52, 13, 29, 21, 25, 25 | 7, 33, 47, 35, 9, 7 | 52:Primordial:38.148:valid_but_not_selected, 52:Caçador:40.217:selected_best_candidate | board_advantage |
| Jogador 4 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 4 | 1-1 | 2–4 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7 |  |  | insufficient_evidence |
| Jogador 4 | 1-2 | 13–21 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 1, 7, 13 |  |  | insufficient_evidence |
| Jogador 4 | 1-3 | 23–27 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13 | 3, 6 |  | insufficient_evidence |
| Jogador 4 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1 | 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-1 | 43–50 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1, 13 | 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-2 | 52–59 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1, 13 | 3, 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-3 | 61–68 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 13, 13, 33 | 3, 0, 0, 3 |  | insufficient_evidence |
| Jogador 4 | 2-4 | 70–71 | 2 | — | INITIAL_SELECTION | Fumegante | 43 | 0.950 | 1.000 | 7, 13, 13, 43, 33 | 0, 3, 0, 3 | 43:Lunar:40.704:valid_but_not_selected, 43:Fumegante:40.929:selected_best_candidate | anchor_opportunity |
| Jogador 4 | 2-4 | 72–72 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 13, 13, 33 | 0, 3, 0, 3 |  | insufficient_evidence |
| Jogador 4 | 2-5 | 74–74 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 13, 13, 33 | 0, 3, 0, 3 |  | insufficient_evidence |
| Jogador 4 | 2-5 | 75–75 | 1 | Florescer | ABANDON | — | -1 | 0.650 | 0.000 | 13 | 7, 0, 13, 3, 30, 33, 0, 3 |  | board_deficit |
| Jogador 4 | 2-5 | 76–80 | 5 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 7, 0, 13, 3, 13, 0, 3 |  |  | board_advantage |
| Jogador 4 | 2-6 | 82–87 | 6 | Florescer | KEEP | Florescer | 49 | 0.950 | 0.545 | 7, 0, 3, 13, 13, 7, 0 |  | 49:Primordial:31.696:valid_but_not_selected, 49:Adaptador:37.535:selected_best_candidate | board_advantage |
| Jogador 4 | 2-7 | 89–90 | 2 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 0, 13, 13, 7, 0 | 3 |  | board_advantage |
| Jogador 4 | 3-1 | 92–97 | 6 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 0, 13, 13, 7, 0 | 36, 3, 18 |  | board_advantage |
| Jogador 4 | 3-2 | 99–100 | 2 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 0, 7, 0, 13 | 36, 3, 26, 18 |  | board_advantage |
| Jogador 4 | 3-3 | 102–107 | 6 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 7, 13, 0, 13, 40 | 3, 26, 18, 26, 36 |  | board_advantage |
| Jogador 4 | 3-4 | 109–110 | 2 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 7, 0, 13, 13, 40 | 3, 36, 26, 18, 26, 36 |  | board_advantage |
| Jogador 4 | 3-5 | 112–117 | 6 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 13, 0, 7, 22, 13, 40, 0 | 3, 36, 28, 18, 36, 26 |  | board_advantage |
| Jogador 4 | 3-6 | 119–120 | 2 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 7, 0, 7, 22, 13, 40, 0 | 3, 36, 28, 18, 28, 36, 26 |  | board_advantage |
| Jogador 4 | 3-7 | 122–126 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 0, 7, 13, 22, 15, 13, 40, 0 | 3, 28, 18, 28, 36 |  | board_advantage |
| Jogador 4 | 4-1 | 128–130 | 3 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 0, 22, 7, 13, 15, 13, 40, 0 | 3, 28, 18, 28, 36 |  | board_advantage |
| Jogador 4 | 4-2 | 132–136 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 0, 7, 7, 22, 7, 15, 13, 40, 0 | 3, 28, 18, 28, 35 |  | board_advantage |
| Jogador 4 | 4-3 | 138–140 | 3 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 0, 7, 7, 22, 7, 15, 40, 40, 0 | 3, 28, 18, 28, 35 |  | board_advantage |
| Jogador 4 | 4-4 | 142–146 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 13, 0, 7, 22, 7, 15, 40, 40 | 3, 28, 18, 28, 26, 35 |  | board_advantage |
| Jogador 4 | 4-5 | 148–150 | 3 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 13, 0, 7, 22, 7, 15, 40, 40 | 3, 18, 28, 18, 35 |  | board_advantage |
| Jogador 4 | 4-6 | 152–156 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 13, 0, 7, 22, 7, 15, 40, 40 | 3, 33, 18, 32, 18, 35 |  | board_advantage |
| Jogador 4 | 4-7 | 158–160 | 3 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 13, 0, 7, 22, 7, 22, 15, 40, 40 | 3, 33, 18, 18, 35 |  | board_advantage |
| Jogador 4 | 5-1 | 162–166 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 13, 0, 7, 22, 7, 22, 40, 40 | 3, 33, 18, 25, 18, 35 |  | board_advantage |
| Jogador 4 | 5-2 | 168–170 | 3 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 13, 0, 7, 7, 22, 22, 40, 40 | 3, 35, 33, 18, 18, 35 |  | board_advantage |
| Jogador 5 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 5 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13 |  |  | insufficient_evidence |
| Jogador 5 | 1-2 | 13–21 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 11 |  |  | insufficient_evidence |
| Jogador 5 | 1-3 | 23–24 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13 | 26 |  | insufficient_evidence |
| Jogador 5 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13 | 26, 7, 22 |  | insufficient_evidence |
| Jogador 5 | 2-1 | 43–48 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 7, 26, 28, 22 |  | insufficient_evidence |
| Jogador 5 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 7, 26, 28, 22, 7 |  | insufficient_evidence |
| Jogador 5 | 2-3 | 61–68 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 26, 1, 22, 7 |  | insufficient_evidence |
| Jogador 5 | 2-4 | 70–72 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 26, 1, 22, 33, 20 |  | insufficient_evidence |
| Jogador 5 | 2-5 | 74–74 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 26, 22, 33, 20 |  | insufficient_evidence |
| Jogador 5 | 2-5 | 75–75 | 1 | Enfeitiçador | ABANDON | — | -1 | 0.650 | 0.000 | 13 | 28, 8, 11, 4, 26, 37, 22, 8, 33, 20 |  | board_deficit |
| Jogador 5 | 2-5 | 76–80 | 5 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 8, 11, 13, 28, 8, 20, 3 | 37, 4, 22, 33 |  | board_advantage |
| Jogador 5 | 2-6 | 82–87 | 6 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 8, 11, 13, 28, 8, 20, 3 | 37, 4 |  | board_advantage |
| Jogador 5 | 2-7 | 89–90 | 2 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 11, 13, 8, 28, 20 | 37, 4 |  | board_advantage |
| Jogador 5 | 3-1 | 92–97 | 6 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 11, 8, 13, 28, 13, 20 | 37, 4, 39, 26 |  | board_advantage |
| Jogador 5 | 3-2 | 99–100 | 2 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 11, 8, 13, 28, 13, 20 | 37, 39, 4, 39, 26 |  | board_advantage |
| Jogador 5 | 3-3 | 102–107 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 41 | 0.950 | 0.222 | 8, 11, 13, 28, 13, 20, 41 | 37, 39, 4, 39, 37 | 41:Florescer:43.504:valid_but_not_selected, 41:Enfeitiçador:44.041:selected_best_candidate | board_advantage |
| Jogador 5 | 3-3 | 103–103 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 41 | 0.950 | 0.667 | 11, 8, 13, 28, 13, 20 | 37, 39, 4, 39, 26, 26, 37 | 41:Florescer:45.005:selected_best_candidate, 41:Enfeitiçador:44.217:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 3-3 | 104–106 | 3 | Enfeitiçador | ADAPT | Florescer | 41 | 0.650 | 0.667 | 8, 11, 13, 13, 41, 26 | 37, 39, 4, 39, 28, 20, 37 | 41:Florescer:45.132:selected_best_candidate, 41:Enfeitiçador:44.040:not_best_scoring_candidate | transition_cost |
| Jogador 5 | 3-4 | 109–110 | 2 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 8, 11, 13, 28, 13, 3, 20 | 37, 39, 4, 39, 37 |  | board_advantage |
| Jogador 5 | 3-5 | 112–117 | 6 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 8, 11, 13, 28, 13, 3, 3, 20, 8 | 37, 39, 4, 39, 37 |  | board_advantage |
| Jogador 5 | 3-6 | 119–120 | 2 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 8, 11, 13, 28, 13, 3, 3, 20 | 37, 39, 4, 39, 37, 24 |  | board_advantage |
| Jogador 5 | 3-7 | 122–126 | 5 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 8, 11, 13, 28, 13, 3, 3, 20, 20 | 37, 39, 4, 39, 37, 40 |  | board_advantage |
| Jogador 5 | 4-1 | 128–130 | 3 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 8, 11, 13, 28, 13, 3, 3, 20, 30, 20 | 37, 39, 4, 39, 37 |  | board_advantage |
| Jogador 5 | 4-2 | 132–136 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.545 | 8, 11, 13, 13, 3, 3, 20, 30, 20 | 37, 39, 4, 39, 53, 37 | 53:Flora Fatalis:36.740:valid_but_not_selected, 53:Carrasco:37.324:selected_best_candidate | board_advantage |
| Jogador 5 | 4-3 | 138–140 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.545 | 3, 8, 11, 13, 13, 3, 20, 30, 20 | 39, 4, 27, 53, 37, 37 | 53:Flora Fatalis:40.046:valid_but_not_selected, 53:Carrasco:41.678:selected_best_candidate | board_advantage |
| Jogador 5 | 4-4 | 142–146 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.545 | 3, 37, 11, 13, 53, 13, 3, 20, 30, 20 | 39, 4, 27, 8, 37 | 53:Flora Fatalis:40.251:valid_but_not_selected, 53:Carrasco:41.671:selected_best_candidate | board_advantage |
| Jogador 5 | 4-5 | 148–150 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 53, 37, 11, 13, 3, 13, 20, 30, 20 | 39, 4, 8, 37 | 53:Flora Fatalis:38.398:valid_but_not_selected, 53:Carrasco:40.421:selected_best_candidate | board_advantage |
| Jogador 5 | 4-6 | 152–156 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.545 | 53, 37, 11, 13, 13, 30, 20, 30, 20 | 39, 4, 12, 8, 37 | 53:Flora Fatalis:36.492:valid_but_not_selected, 53:Carrasco:37.525:selected_best_candidate | board_advantage |
| Jogador 5 | 4-7 | 158–159 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 43 | 0.950 | 0.222 | 53, 37, 11, 13, 13, 30, 20, 30, 20 | 39, 4, 12, 34, 37 | 43:Lunar:42.370:selected_best_candidate, 43:Fumegante:41.783:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 4-7 | 160–160 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.769 | 53, 37, 11, 13, 13, 30, 20, 30, 20 | 39, 4, 12, 34, 43, 37 | 53:Flora Fatalis:36.830:valid_but_not_selected, 53:Carrasco:38.190:selected_best_candidate | board_advantage |
| Jogador 5 | 5-1 | 162–166 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.545 | 53, 37, 11, 13, 13, 30, 20, 30, 20 | 39, 4, 12, 43, 37 | 53:Flora Fatalis:36.656:valid_but_not_selected, 53:Carrasco:37.689:selected_best_candidate | board_advantage |
| Jogador 5 | 5-2 | 168–170 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.769 | 53, 37, 11, 13, 13, 30, 20, 30, 20 | 39, 4, 12, 4, 43, 37 | 53:Flora Fatalis:36.972:valid_but_not_selected, 53:Carrasco:38.332:selected_best_candidate | board_advantage |
| Jogador 5 | 5-3 | 172–175 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.769 | 53, 37, 11, 13, 20, 13, 30, 30 | 39, 4, 12, 43, 24, 37, 26 | 53:Flora Fatalis:37.270:valid_but_not_selected, 53:Carrasco:39.452:selected_best_candidate | board_advantage |
| Jogador 5 | 5-4 | 177–177 | 1 | Enfeitiçador | ADAPT | Florescer | 41 | 0.650 | 0.667 | 53, 37, 11, 13, 13, 26 | 39, 4, 12, 20, 30, 43, 24, 37, 30 | 41:Florescer:47.028:selected_best_candidate, 41:Enfeitiçador:46.128:not_best_scoring_candidate | transition_cost |
| Jogador 5 | 5-4 | 178–178 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 41 | 0.950 | 0.769 | 53, 37, 11, 13, 13, 30, 30 | 39, 4, 12, 43, 24, 37, 26 | 41:Florescer:45.650:selected_best_candidate, 41:Enfeitiçador:45.590:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 5-4 | 179–180 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.545 | 53, 37, 11, 13, 41, 13, 30, 30 | 39, 4, 12, 43, 24, 37 | 53:Flora Fatalis:36.479:valid_but_not_selected, 53:Carrasco:37.513:selected_best_candidate | board_advantage |
| Jogador 5 | 5-5 | 182–185 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 53, 37, 11, 41, 13, 13, 30, 30 | 39, 4, 12, 43, 24, 37, 35 | 53:Flora Fatalis:38.371:valid_but_not_selected, 53:Carrasco:39.344:selected_best_candidate | board_advantage |
| Jogador 5 | 5-6 | 187–190 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 53, 37, 11, 41, 13, 13, 30, 30 | 39, 4, 12, 43, 12, 37, 35 | 53:Flora Fatalis:37.156:valid_but_not_selected, 53:Carrasco:38.384:selected_best_candidate | board_advantage |
| Jogador 5 | 5-7 | 192–195 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 42 | 0.950 | 0.667 | 53, 37, 11, 41, 13, 13, 30, 30 | 39, 4, 12, 43, 12, 37, 35 | 42:Inferno:37.953:valid_but_not_selected, 42:Colosso:38.951:selected_best_candidate | board_advantage |
| Jogador 5 | 6-1 | 197–200 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 46 | 0.950 | 0.222 | 53, 37, 11, 41, 13, 13, 30, 30 | 39, 4, 12, 42, 43, 12, 37, 43 | 46:Feérico:39.298:valid_but_not_selected, 46:Defendente:39.828:selected_best_candidate | board_advantage |
| Jogador 5 | 6-2 | 202–205 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 71 | 0.950 | 0.222 | 53, 37, 11, 41, 13, 13, 30, 30 | 39, 4, 12, 54, 43, 12, 37, 43 | 71:Solar:34.815:valid_but_not_selected, 71:Avatar:36.065:selected_best_candidate | board_advantage |
| Jogador 6 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 6 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 2 |  |  | insufficient_evidence |
| Jogador 6 | 1-2 | 13–21 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 2, 12, 13 |  |  | insufficient_evidence |
| Jogador 6 | 1-3 | 23–31 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 2, 12, 13 | 4 |  | insufficient_evidence |
| Jogador 6 | 1-4 | 34–35 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 4 |  | insufficient_evidence |
| Jogador 6 | 2-1 | 43–50 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 4, 7 |  | insufficient_evidence |
| Jogador 6 | 2-2 | 52–56 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 7, 19 |  | insufficient_evidence |
| Jogador 6 | 2-3 | 61–66 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 19, 15, 18 |  | insufficient_evidence |
| Jogador 6 | 2-4 | 70–72 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 31, 19, 7, 15, 18 |  | insufficient_evidence |
| Jogador 6 | 2-5 | 74–74 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 31, 19, 7, 15, 18 |  | insufficient_evidence |
| Jogador 6 | 2-5 | 75–75 | 1 | Feérico | ABANDON | — | -1 | 0.650 | 0.000 | 2 | 12, 12, 2, 39, 18, 13, 23, 31, 19, 7, 15, 18 |  | board_deficit |
| Jogador 6 | 2-5 | 76–80 | 5 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 39, 2, 13, 7, 13 | 31, 19 |  | board_advantage |
| Jogador 6 | 2-6 | 82–87 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 39, 2, 13, 13 | 19, 31, 19 |  | board_advantage |
| Jogador 6 | 2-7 | 89–90 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 39, 2, 13, 13 | 19, 33, 19 |  | board_advantage |
| Jogador 6 | 3-1 | 92–97 | 6 | Feérico | KEEP | Feérico | 41 | 0.950 | 0.769 | 12, 12, 13, 39, 2, 2, 13 | 19, 33, 19 | 41:Florescer:38.694:selected_best_candidate, 41:Enfeitiçador:37.915:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-2 | 99–100 | 2 | Fumegante | KEEP | Fumegante | -1 | 0.000 | 0.000 | 12, 12, 13, 19, 2, 19, 13 | 39, 33 |  | board_advantage |
| Jogador 6 | 3-3 | 102–107 | 6 | Fumegante | KEEP | Fumegante | -1 | 0.000 | 0.000 | 12, 12, 13, 39, 33, 19, 39, 19, 13 | 24 |  | board_advantage |
| Jogador 6 | 3-4 | 109–110 | 2 | Fumegante | KEEP | Fumegante | 46 | 0.950 | 0.400 | 12, 12, 13, 39, 33, 19, 39, 35, 19, 13 | 24 | 46:Feérico:39.676:selected_best_candidate, 46:Defendente:36.363:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-5 | 112–117 | 6 | Fumegante | KEEP | Fumegante | -1 | 0.000 | 0.000 | 12, 12, 13, 39, 33, 19, 39, 35, 35, 19, 13 |  |  | board_advantage |
| Jogador 6 | 3-6 | 119–120 | 2 | Fumegante | KEEP | Fumegante | -1 | 0.000 | 0.000 | 12, 12, 13, 39, 33, 19, 39, 35, 35, 19, 13 | 27 |  | board_advantage |
| Jogador 6 | 3-7 | 122–122 | 1 | Fumegante | ADAPT | Vivaz | 59 | 0.650 | 0.667 | 12, 13, 12, 39, 33, 39, 13 | 19, 27, 35, 35, 19 | 59:Sabugueiro:40.253:valid_but_not_selected, 59:Vivaz:42.401:selected_best_candidate | transition_cost |
| Jogador 6 | 3-7 | 123–126 | 4 | Fumegante | KEEP | Fumegante | 54 | 0.950 | 0.545 | 12, 13, 12, 39, 33, 19, 39, 35, 35, 19 |  | 54:Dama de Espinhos:32.901:valid_but_not_selected, 54:Invocador:39.417:selected_best_candidate | board_advantage |
| Jogador 6 | 4-1 | 128–130 | 3 | Fumegante | KEEP | Fumegante | 54 | 0.950 | 0.222 | 12, 13, 12, 39, 33, 19, 39, 35, 35, 19 | 54, 30 | 54:Dama de Espinhos:33.479:valid_but_not_selected, 54:Invocador:40.181:selected_best_candidate | board_advantage |
| Jogador 6 | 4-2 | 132–136 | 5 | Fumegante | KEEP | Fumegante | 53 | 0.950 | 0.400 | 12, 13, 12, 39, 33, 19, 39, 35, 35, 19 |  | 53:Flora Fatalis:32.848:valid_but_not_selected, 53:Carrasco:36.562:selected_best_candidate | board_advantage |
| Jogador 6 | 4-3 | 138–140 | 3 | Fumegante | KEEP | Fumegante | 42 | 0.950 | 0.222 | 12, 13, 12, 39, 33, 19, 39, 19, 35, 35 | 42 | 42:Inferno:39.499:valid_but_not_selected, 42:Colosso:40.716:selected_best_candidate | board_advantage |
| Jogador 6 | 4-4 | 142–146 | 5 | Fumegante | KEEP | Fumegante | 42 | 0.950 | 0.545 | 12, 33, 12, 39, 39, 19, 13, 19, 35, 35 | 42, 40, 7, 38 | 42:Inferno:39.560:valid_but_not_selected, 42:Colosso:43.793:selected_best_candidate | board_advantage |
| Jogador 6 | 4-5 | 148–150 | 3 | Fumegante | ADAPT | Colosso | 42 | 0.650 | 0.545 | 12, 33, 12, 39, 39, 13, 42, 40, 7 | 19, 19, 35, 35, 38, 10, 24 | 42:Inferno:41.960:valid_but_not_selected, 42:Colosso:46.368:selected_best_candidate | anchor_opportunity |
| Jogador 6 | 4-6 | 152–156 | 5 | Fumegante | KEEP | Fumegante | 46 | 0.950 | 0.400 | 12, 33, 12, 39, 19, 39, 13, 19, 35, 35, 10 | 42, 40, 36, 38 | 46:Feérico:42.451:selected_best_candidate, 46:Defendente:39.914:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-7 | 158–160 | 3 | Fumegante | KEEP | Fumegante | 42 | 0.950 | 0.000 | 12, 33, 12, 19, 13, 19, 35, 35, 39, 10 | 42, 40, 36, 46 | 42:Inferno:42.375:valid_but_not_selected, 42:Colosso:44.154:selected_best_candidate | board_advantage |
| Jogador 6 | 5-1 | 162–166 | 5 | Fumegante | KEEP | Fumegante | 43 | 0.950 | 0.000 | 12, 33, 12, 35, 13, 19, 43, 35, 39, 10 | 42, 40, 36, 46 | 43:Lunar:45.389:valid_but_not_selected, 43:Fumegante:49.903:selected_best_candidate | board_advantage |
| Jogador 6 | 5-2 | 168–170 | 3 | Fumegante | KEEP | Fumegante | 43 | 0.950 | 0.000 | 12, 33, 12, 35, 19, 13, 43, 35, 39, 10 | 40, 31, 42, 36, 46 | 43:Lunar:43.853:valid_but_not_selected, 43:Fumegante:49.862:selected_best_candidate | board_advantage |
| Jogador 6 | 5-3 | 172–175 | 4 | Fumegante | KEEP | Fumegante | 43 | 0.950 | 0.000 | 43, 33, 19, 13, 12, 35, 39, 10 | 31, 40, 42, 36, 46 | 43:Lunar:46.168:valid_but_not_selected, 43:Fumegante:50.705:selected_best_candidate | board_advantage |
| Jogador 6 | 5-4 | 177–177 | 1 | Fumegante | KEEP | Fumegante | 54 | 0.950 | 0.000 | 43, 33, 19, 13, 12, 35, 39, 10 | 31, 40, 42, 36, 46 | 54:Dama de Espinhos:38.112:valid_but_not_selected, 54:Invocador:45.978:selected_best_candidate | board_advantage |
| Jogador 6 | 5-4 | 178–180 | 3 | Fumegante | KEEP | Fumegante | 41 | 0.950 | 0.545 | 33, 35, 19, 13, 12, 43, 39, 10 | 31, 54, 40, 42, 36, 46 | 41:Florescer:44.153:selected_best_candidate, 41:Enfeitiçador:43.182:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 5-5 | 182–185 | 4 | Fumegante | KEEP | Fumegante | 43 | 0.950 | 0.000 | 33, 43, 19, 54, 13, 12, 35, 10 | 31, 34, 40, 42, 36, 34, 46 | 43:Lunar:45.585:valid_but_not_selected, 43:Fumegante:50.894:selected_best_candidate | board_advantage |
| Jogador 7 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 7 | 1-1 | 2–2 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0 |  |  | insufficient_evidence |
| Jogador 7 | 1-2 | 13–21 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 10 |  |  | insufficient_evidence |
| Jogador 7 | 1-3 | 23–28 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 10, 0 | 13 |  | insufficient_evidence |
| Jogador 7 | 1-4 | 34–38 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 0, 7, 0, 10 | 13, 1 |  | insufficient_evidence |
| Jogador 7 | 2-1 | 43–50 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 0, 7, 0, 10 | 13, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-2 | 52–59 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 7, 31, 10 | 13, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-3 | 61–68 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 31, 10 | 13, 1, 28, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-4 | 70–72 | 3 | — | INITIAL_SELECTION | Fera do Rift | 44 | 0.950 | 1.000 | 7, 31, 10, 44 | 13, 33, 1, 28, 1, 13, 23 | 44:Fera do Rift:40.042:selected_best_candidate, 44:Vanguarda:37.421:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-5 | 74–74 | 1 | — | INITIAL_SELECTION | Fera do Rift | 44 | 0.950 | 1.000 | 7, 31, 10, 44 | 33, 13, 1, 28, 1, 13, 23 | 44:Fera do Rift:44.523:selected_best_candidate, 44:Vanguarda:40.254:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-5 | 75–75 | 1 | Colosso | PIVOT | Fera do Rift | 44 | 0.950 | 0.222 | 7, 35, 44 | 31, 10, 33, 13, 1, 28, 1, 13, 23 | 44:Fera do Rift:46.408:selected_best_candidate, 44:Vanguarda:42.202:not_best_scoring_candidate | board_deficit |
| Jogador 7 | 2-5 | 76–80 | 5 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.222 | 7, 31, 10, 35, 44 | 33, 13, 1, 12, 1, 13 | 44:Fera do Rift:46.946:selected_best_candidate, 44:Vanguarda:42.725:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-6 | 82–87 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.222 | 7, 10, 31, 35, 7, 44 | 33, 13, 12, 13, 33 | 44:Fera do Rift:47.534:selected_best_candidate, 44:Vanguarda:43.321:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-7 | 89–90 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 7, 10, 31, 35, 7, 44 | 33, 13, 37, 13, 33 | 44:Fera do Rift:45.562:selected_best_candidate, 44:Vanguarda:37.572:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-1 | 92–97 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.222 | 7, 10, 31, 35, 21, 15, 7, 44 | 37, 33, 13, 29, 13, 33 | 44:Fera do Rift:46.429:selected_best_candidate, 44:Vanguarda:38.259:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-2 | 99–100 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 7, 31, 10, 35, 21, 15, 7, 44, 35 | 37, 33, 13, 29, 13, 33 | 44:Fera do Rift:47.935:selected_best_candidate, 44:Vanguarda:39.792:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-3 | 102–107 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 7, 31, 10, 35, 15, 7, 44, 35 | 37, 33, 13, 30, 12, 13, 33 | 44:Fera do Rift:49.003:selected_best_candidate, 44:Vanguarda:44.797:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-4 | 109–110 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 7, 31, 10, 35, 15, 7, 44, 35 | 37, 13, 33, 12, 13, 33 | 44:Fera do Rift:48.995:selected_best_candidate, 44:Vanguarda:44.788:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-5 | 112–117 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.222 | 7, 31, 10, 35, 15, 15, 7, 44, 35 | 37, 33, 13, 29, 13, 33 | 44:Fera do Rift:46.959:selected_best_candidate, 44:Vanguarda:38.957:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-6 | 119–120 | 2 | Colosso | KEEP | Colosso | 43 | 0.950 | 0.400 | 7, 31, 10, 13, 15, 15, 13, 7 | 37, 33, 35, 44, 33, 35 | 43:Lunar:42.615:valid_but_not_selected, 43:Fumegante:45.485:selected_best_candidate | board_advantage |
| Jogador 7 | 3-7 | 122–122 | 1 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 7, 31, 10, 35, 15, 31, 15, 7, 44, 35 | 37, 33, 13, 13, 33 | 44:Fera do Rift:50.010:selected_best_candidate, 44:Vanguarda:40.245:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-7 | 123–126 | 4 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 31, 10, 13, 15, 31, 15, 13, 7 | 37, 33, 35, 33, 35 |  | board_advantage |
| Jogador 7 | 4-1 | 128–130 | 3 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 31, 13, 10, 15, 31, 15, 13, 7 | 33, 37, 35, 33, 35 |  | board_advantage |
| Jogador 7 | 4-2 | 132–136 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 7, 10, 31, 13, 15, 31, 15, 13, 7, 22 | 33, 37, 35, 33, 35 |  | board_advantage |
| Jogador 7 | 4-3 | 138–140 | 3 | Colosso | KEEP | Colosso | 53 | 0.950 | 0.400 | 7, 10, 31, 13, 15, 31, 15, 13, 7 | 33, 37, 35, 53, 33, 35 | 53:Flora Fatalis:31.021:valid_but_not_selected, 53:Carrasco:34.666:selected_best_candidate | board_advantage |
| Jogador 7 | 4-4 | 142–146 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 15, 7, 10, 31, 13, 31, 15, 13, 7 | 33, 37, 30, 36, 35, 33 |  | board_advantage |
| Jogador 7 | 4-5 | 148–150 | 3 | Colosso | KEEP | Colosso | 45 | 0.950 | 0.769 | 7, 10, 15, 13, 31, 31, 15, 13, 7 | 37, 33, 30, 36, 35, 33, 29 | 45:Sabugueiro:41.082:selected_best_candidate, 45:Carrasco:36.497:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-6 | 152–156 | 5 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 10, 15, 15, 13, 7, 31 | 37, 30, 36, 33, 29 |  | board_advantage |
| Jogador 7 | 4-7 | 158–160 | 3 | Colosso | KEEP | Colosso | 51 | 0.950 | 0.545 | 10, 15, 13, 13, 7, 31 | 36, 30, 37, 33, 29 | 51:Florescer:37.551:selected_best_candidate, 51:Lutador:34.188:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 5-1 | 162–166 | 5 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.667 | 36, 13, 10, 15, 56, 13, 7, 31 | 30, 37, 18, 38, 33, 29 | 56:Florescer:42.992:selected_best_candidate, 56:Caçador:41.783:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 5-2 | 168–170 | 3 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.769 | 36, 13, 10, 15, 56, 36, 13, 7, 31 | 30, 37, 18, 38, 18, 33, 29 | 56:Florescer:45.156:selected_best_candidate, 56:Caçador:41.798:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 5-3 | 172–175 | 4 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.400 | 36, 13, 10, 15, 56, 36, 13, 33, 7 | 30, 37, 18, 38, 18, 29 | 56:Florescer:44.762:selected_best_candidate, 56:Caçador:42.469:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-4 | 177–180 | 4 | Colosso | ADAPT | Fera do Rift | 50 | 0.650 | 0.667 | 36, 10, 15, 56, 18, 18, 33, 15 | 13, 30, 37, 36, 38, 13, 11, 29 | 50:Fera do Rift:44.673:selected_best_candidate, 50:Devastador:38.924:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 5-5 | 182–185 | 4 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.667 | 36, 13, 10, 15, 56, 36, 13, 15 | 30, 37, 18, 38, 18, 37, 11, 29 | 56:Florescer:42.503:selected_best_candidate, 56:Caçador:38.763:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 5-6 | 187–190 | 4 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.545 | 13, 10, 15, 56, 13, 15, 36 | 30, 37, 39, 18, 38, 18, 37, 29 | 56:Florescer:42.016:selected_best_candidate, 56:Caçador:38.877:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-7 | 192–195 | 4 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.667 | 13, 10, 15, 56, 36, 13, 15 | 30, 39, 18, 38, 18, 37, 29 | 56:Florescer:42.105:selected_best_candidate, 56:Caçador:38.052:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 6-1 | 197–200 | 4 | Colosso | KEEP | Colosso | 45 | 0.950 | 0.667 | 13, 10, 15, 56, 13, 15 | 30, 39, 36, 18, 39, 38, 26, 35, 37, 29 | 45:Sabugueiro:34.839:valid_but_not_selected, 45:Carrasco:37.355:selected_best_candidate | board_advantage |
| Jogador 7 | 6-2 | 202–205 | 4 | Colosso | ADAPT | Caçador | 56 | 0.650 | 0.857 | 10, 15, 39, 56, 36, 39, 15 | 13, 30, 18, 38, 26, 13, 35, 37, 29 | 56:Florescer:41.869:valid_but_not_selected, 56:Caçador:44.095:selected_best_candidate | transition_cost |
| Jogador 7 | 6-3 | 207–210 | 4 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.667 | 13, 10, 15, 56, 36, 26, 13, 15, 36 | 30, 39, 39, 38, 35, 29 | 56:Florescer:42.218:selected_best_candidate, 56:Caçador:39.498:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 6-4 | 212–215 | 4 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.667 | 13, 10, 15, 56, 36, 13, 15 | 30, 39, 30, 39, 38, 35, 33, 29 | 56:Florescer:44.215:selected_best_candidate, 56:Caçador:40.360:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 6-5 | 217–218 | 2 | Colosso | ADAPT | Florescer | 56 | 0.650 | 0.667 | 13, 10, 15, 56, 36, 13, 15 | 30, 39, 30, 22, 39, 38, 35, 33, 29 | 56:Florescer:44.198:selected_best_candidate, 56:Caçador:40.363:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 6-5 | 219–220 | 2 | Colosso | KEEP | Colosso | 56 | 0.950 | 0.769 | 13, 10, 15, 56, 22, 13, 15 | 30, 39, 30, 39, 38, 32, 35, 33, 29 | 56:Florescer:40.858:selected_best_candidate, 56:Caçador:39.285:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 6-6 | 222–225 | 4 | Colosso | ADAPT | Florescer | 41 | 0.650 | 0.769 | 13, 10, 15, 56, 30, 13, 15 | 30, 39, 22, 39, 32, 35, 33, 29 | 41:Florescer:43.507:selected_best_candidate, 41:Enfeitiçador:40.756:not_best_scoring_candidate | transition_cost |
| Jogador 8 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 8 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7 |  |  | insufficient_evidence |
| Jogador 8 | 1-2 | 13–21 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 7, 11 |  |  | insufficient_evidence |
| Jogador 8 | 1-3 | 23–25 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7, 3 | 13 |  | insufficient_evidence |
| Jogador 8 | 1-4 | 34–39 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7, 3 | 12, 12 |  | insufficient_evidence |
| Jogador 8 | 2-1 | 43–50 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7 | 12, 24, 5 |  | insufficient_evidence |
| Jogador 8 | 2-2 | 52–59 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 11, 7, 3 | 24, 12, 25, 34, 0, 4 |  | insufficient_evidence |
| Jogador 8 | 2-3 | 61–68 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 3, 3, 11 | 24, 28, 25, 12, 34, 0, 4 |  | insufficient_evidence |
| Jogador 8 | 2-4 | 70–72 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 3, 3, 11 | 4, 28, 25, 12, 34, 0, 24, 4, 32 |  | insufficient_evidence |
| Jogador 8 | 2-5 | 74–74 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 3, 3, 11 | 4, 28, 25, 34, 0, 24, 4, 32 |  | insufficient_evidence |
| Jogador 8 | 2-5 | 75–75 | 1 | Enfeitiçador | ABANDON | — | -1 | 0.650 | 0.000 | 7 | 4, 28, 3, 25, 3, 34, 0, 24, 3, 11, 4, 32 |  | board_deficit |
| Jogador 8 | 2-5 | 76–80 | 5 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 3, 28, 7, 3, 3 | 25, 34, 0, 4, 25, 32 |  | board_advantage |
| Jogador 8 | 2-6 | 82–87 | 6 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 7, 3, 3, 3, 7 | 37, 4, 25, 34, 0, 39, 25, 32 |  | board_advantage |
| Jogador 8 | 2-7 | 89–90 | 2 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 7, 3, 3, 3, 7 | 37, 4, 25, 34, 0, 39, 25, 39 |  | board_advantage |
| Jogador 8 | 3-1 | 92–94 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 46 | 0.950 | 0.545 | 28, 7, 3, 3, 3, 7 | 37, 4, 25, 46, 0, 39, 25, 39 | 46:Feérico:35.073:valid_but_not_selected, 46:Defendente:38.828:selected_best_candidate | board_advantage |
| Jogador 8 | 3-1 | 95–97 | 3 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 7, 3, 3, 3, 7 | 37, 4, 25, 0, 39, 25, 39 |  | board_advantage |
| Jogador 8 | 3-2 | 99–100 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 0.769 | 28, 7, 3, 3, 3, 7 | 37, 4, 25, 0, 39, 25, 39 | 50:Fera do Rift:36.404:selected_best_candidate, 50:Devastador:35.046:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-3 | 102–107 | 6 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 7, 3, 3, 20, 3, 7 | 37, 4, 25, 12, 25, 39 |  | board_advantage |
| Jogador 8 | 3-4 | 109–110 | 2 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 7, 3, 3, 20, 3, 7 | 37, 4, 25, 32, 25, 39 |  | board_advantage |
| Jogador 8 | 3-5 | 112–117 | 6 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 7, 3, 28, 20, 7 | 37, 4, 25, 26, 32, 25, 39 |  | board_advantage |
| Jogador 8 | 3-6 | 119–120 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 47 | 0.950 | 0.222 | 28, 7, 3, 28, 7 | 37, 4, 25, 26, 32, 9, 25, 39 | 47:Espinhos Negros:36.212:selected_best_candidate, 47:Monólito:30.910:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-7 | 122–126 | 5 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 4, 3, 28 | 37, 25, 14, 26, 32, 9, 25, 24, 39 |  | board_advantage |
| Jogador 8 | 4-1 | 128–130 | 3 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 28, 4, 3, 28, 11 | 37, 14, 26, 25, 32, 9, 24, 39 |  | board_advantage |
| Jogador 8 | 4-2 | 132–136 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.769 | 37, 28, 4, 3, 28, 11 | 14, 32, 52, 26, 25, 9, 24, 39 | 52:Primordial:37.613:valid_but_not_selected, 52:Caçador:39.127:selected_best_candidate | board_advantage |
| Jogador 8 | 4-3 | 138–140 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.545 | 37, 28, 4, 3, 28, 11 | 14, 32, 52, 26, 39, 40, 9, 24, 39 | 52:Primordial:37.295:valid_but_not_selected, 52:Caçador:40.806:selected_best_candidate | board_advantage |
| Jogador 8 | 4-4 | 142–146 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.545 | 37, 28, 4, 3, 28, 20, 30, 11 | 14, 32, 52, 39, 40, 39 | 52:Primordial:40.340:valid_but_not_selected, 52:Caçador:41.081:selected_best_candidate | board_advantage |
| Jogador 8 | 4-5 | 148–150 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.545 | 37, 28, 4, 3, 28, 20, 30, 11, 20 | 14, 32, 52, 39, 40, 39 | 52:Primordial:40.185:valid_but_not_selected, 52:Caçador:41.019:selected_best_candidate | board_advantage |
| Jogador 8 | 4-6 | 152–156 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.667 | 37, 4, 3, 52, 20, 30, 11, 20 | 14, 32, 6, 39, 16, 39 | 52:Primordial:37.415:valid_but_not_selected, 52:Caçador:42.228:selected_best_candidate | board_advantage |
| Jogador 8 | 4-7 | 158–160 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.667 | 37, 4, 52, 3, 20, 30, 11, 20 | 14, 32, 31, 39, 16, 39 | 52:Primordial:39.286:valid_but_not_selected, 52:Caçador:42.314:selected_best_candidate | board_advantage |
| Jogador 8 | 5-1 | 162–166 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.667 | 37, 4, 52, 3, 20, 30, 11, 20 | 14, 32, 31, 23, 39, 37, 39 | 52:Primordial:40.899:valid_but_not_selected, 52:Caçador:41.331:selected_best_candidate | board_advantage |
| Jogador 8 | 5-2 | 168–170 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.667 | 37, 4, 52, 3, 30, 20, 30, 11, 20 | 14, 32, 39, 37, 39 | 52:Primordial:39.651:valid_but_not_selected, 52:Caçador:42.680:selected_best_candidate | board_advantage |
| Jogador 8 | 5-3 | 172–175 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.667 | 37, 4, 52, 3, 30, 20, 30, 11, 20 | 14, 32, 39, 37, 39 | 52:Primordial:39.653:valid_but_not_selected, 52:Caçador:42.682:selected_best_candidate | board_advantage |
| Jogador 8 | 5-4 | 177–180 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.545 | 37, 4, 52, 3, 28, 30, 30, 11, 20 | 14, 32, 39, 37, 39 | 52:Primordial:39.293:valid_but_not_selected, 52:Caçador:42.925:selected_best_candidate | board_advantage |
| Jogador 8 | 5-5 | 182–185 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.545 | 37, 4, 52, 3, 28, 30, 11, 30, 11 | 14, 32, 39, 37, 39 | 52:Primordial:40.205:valid_but_not_selected, 52:Caçador:42.123:selected_best_candidate | board_advantage |
| Jogador 8 | 5-6 | 187–190 | 4 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.545 | 37, 4, 52, 3, 28, 30, 11, 30, 11 | 14, 32, 39, 37, 39 | 52:Primordial:40.670:valid_but_not_selected, 52:Caçador:43.045:selected_best_candidate | board_advantage |

### Frequência das decisões

- ABANDON: 7
- ADAPT: 28
- INITIAL_SELECTION: 3
- INSUFFICIENT_EVIDENCE: 78
- KEEP: 178
- PIVOT: 1

Revisões estratégicas únicas: **295**.
Snapshots estratégicos observados: **1093** (inclui repetições por ação).
Candidatos de âncora avaliados: **268**.


### Auditoria de KEEP — continuidade fundamentada versus persistência

- KEEP auditados: **178**
- Confiança da direção atual: positive=178
- Motivos/path: current_direction_viable_without_alternative=76; alternative_below_minimum_adapt_advantage=92; best_anchor_matches_current_direction=10

| Jogador | Round | Step | Direção | Score atual | Conf. direção atual | Conf. alternativa | Score alternativa | Vantagem | Viável | Motivo | Lock | Candidato pendente | Streak | Limite PIVOT |
|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|
| Jogador 1 | 2-5 | 80 | Inferno | 40.737 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.147 |
| Jogador 1 | 2-6 | 87 | Feérico | 39.554 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 7.911 |
| Jogador 1 | 2-7 | 90 | Inferno | 40.805 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.161 |
| Jogador 1 | 3-1 | 97 | Inferno | 40.445 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.089 |
| Jogador 1 | 3-3 | 105 | Inferno | 42.256 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.451 |
| Jogador 1 | 3-4 | 110 | Inferno | 42.275 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.455 |
| Jogador 1 | 3-5 | 117 | Inferno | 43.169 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.634 |
| Jogador 1 | 3-6 | 120 | Inferno | 43.727 | 0.950 | 0.950 | 36.095 | -7.632 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.745 |
| Jogador 1 | 3-7 | 126 | Inferno | 42.885 | 0.950 | 0.950 | 35.755 | -7.130 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.577 |
| Jogador 1 | 4-1 | 130 | Inferno | 43.065 | 0.950 | 0.950 | 35.584 | -7.481 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.613 |
| Jogador 1 | 4-2 | 136 | Inferno | 38.712 | 0.950 | 0.950 | 34.038 | -4.673 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.742 |
| Jogador 1 | 4-3 | 140 | Inferno | 39.542 | 0.950 | 0.950 | 34.383 | -5.159 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.908 |
| Jogador 1 | 4-4 | 146 | Inferno | 39.402 | 0.950 | 0.950 | 37.095 | -2.306 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.880 |
| Jogador 1 | 4-5 | 150 | Inferno | 39.567 | 0.950 | 0.950 | 36.309 | -3.258 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.913 |
| Jogador 1 | 4-5 | 149 | Inferno | 39.558 | 0.950 | 0.950 | 39.334 | -0.224 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.912 |
| Jogador 1 | 4-6 | 156 | Inferno | 40.235 | 0.950 | 0.950 | 38.259 | -1.976 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.047 |
| Jogador 1 | 4-7 | 158 | Inferno | 39.808 | 0.950 | 0.950 | 37.338 | -2.469 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.962 |
| Jogador 1 | 4-7 | 160 | Inferno | 39.805 | 0.950 | 0.950 | 37.365 | -2.440 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.961 |
| Jogador 1 | 5-1 | 166 | Inferno | 40.394 | 0.950 | 0.950 | 37.863 | -2.531 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.079 |
| Jogador 1 | 5-3 | 175 | Inferno | 42.765 | 0.950 | 0.950 | 43.335 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.553 |
| Jogador 1 | 5-4 | 180 | Inferno | 44.248 | 0.950 | 0.950 | 39.511 | -4.736 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 5-4 | 178 | Inferno | 44.248 | 0.950 | 0.950 | 42.644 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.850 |
| Jogador 1 | 5-5 | 185 | Inferno | 44.248 | 0.950 | 0.950 | 39.984 | -4.263 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 5-6 | 189 | Inferno | 44.248 | 0.950 | 0.950 | 38.718 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.850 |
| Jogador 1 | 5-6 | 190 | Inferno | 44.248 | 0.950 | 0.950 | 39.409 | -4.839 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 5-7 | 194 | Inferno | 44.248 | 0.950 | 0.950 | 38.663 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.850 |
| Jogador 1 | 5-7 | 195 | Inferno | 44.248 | 0.950 | 0.950 | 39.388 | -4.859 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 6-1 | 200 | Inferno | 44.248 | 0.950 | 0.950 | 39.192 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.850 |
| Jogador 1 | 6-1 | 198 | Inferno | 44.248 | 0.950 | 0.950 | 39.746 | -4.502 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 6-2 | 205 | Inferno | 44.248 | 0.950 | 0.950 | 40.351 | -3.896 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 6-3 | 210 | Inferno | 44.248 | 0.950 | 0.950 | 43.301 | -0.947 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 6-4 | 215 | Inferno | 44.248 | 0.950 | 0.950 | 43.651 | -0.596 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 6-5 | 220 | Inferno | 44.248 | 0.950 | 0.950 | 38.323 | -5.925 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 6-5 | 218 | Inferno | 44.248 | 0.950 | 0.950 | 37.041 | -7.206 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 1 | 6-6 | 225 | Inferno | 44.248 | 0.950 | 0.950 | 36.566 | -7.681 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.850 |
| Jogador 2 | 2-5 | 80 | Feérico | 44.270 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.854 |
| Jogador 2 | 2-6 | 87 | Feérico | 44.218 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.844 |
| Jogador 2 | 2-7 | 90 | Feérico | 44.554 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.911 |
| Jogador 2 | 3-1 | 97 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 3-2 | 100 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 3-3 | 107 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 3-4 | 110 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 3-5 | 117 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 3-6 | 120 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 3-7 | 126 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 4-1 | 130 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 4-2 | 136 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 4-3 | 140 | Feérico | 44.285 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.857 |
| Jogador 2 | 4-4 | 146 | Feérico | 43.215 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.643 |
| Jogador 2 | 4-5 | 150 | Feérico | 44.055 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.811 |
| Jogador 3 | 2-5 | 80 | Colosso | 42.136 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.427 |
| Jogador 3 | 2-6 | 87 | Colosso | 42.642 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.528 |
| Jogador 3 | 2-7 | 90 | Colosso | 43.134 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.627 |
| Jogador 3 | 3-1 | 97 | Devastador | 44.358 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.872 |
| Jogador 3 | 3-2 | 100 | Devastador | 44.343 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.869 |
| Jogador 3 | 3-3 | 107 | Devastador | 45.302 | 0.950 | 0.950 | 39.604 | -5.698 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.060 |
| Jogador 3 | 3-4 | 110 | Devastador | 45.363 | 0.950 | 0.950 | 39.532 | -5.831 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.073 |
| Jogador 3 | 3-5 | 117 | Devastador | 45.590 | 0.950 | 0.950 | 41.989 | -3.601 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.118 |
| Jogador 3 | 3-6 | 120 | Devastador | 44.045 | 0.950 | 0.950 | 39.654 | -4.391 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.809 |
| Jogador 3 | 3-7 | 126 | Devastador | 44.329 | 0.950 | 0.950 | 38.286 | -6.042 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.866 |
| Jogador 3 | 4-1 | 130 | Devastador | 44.279 | 0.950 | 0.950 | 34.501 | -9.778 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.856 |
| Jogador 3 | 4-2 | 136 | Devastador | 45.062 | 0.950 | 0.950 | 40.239 | -4.823 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.012 |
| Jogador 3 | 4-3 | 140 | Devastador | 45.027 | 0.950 | 0.950 | 38.138 | -6.889 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.005 |
| Jogador 3 | 4-4 | 146 | Devastador | 45.067 | 0.950 | 0.950 | 38.515 | -6.551 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.013 |
| Jogador 3 | 4-5 | 150 | Devastador | 45.067 | 0.950 | 0.950 | 39.972 | -5.094 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.013 |
| Jogador 3 | 4-6 | 156 | Devastador | 45.771 | 0.950 | 0.950 | 38.794 | -6.978 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.154 |
| Jogador 3 | 4-7 | 160 | Devastador | 46.076 | 0.950 | 0.950 | 39.451 | -6.624 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.215 |
| Jogador 3 | 5-1 | 166 | Devastador | 46.402 | 0.950 | 0.950 | 41.874 | -4.528 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.280 |
| Jogador 3 | 5-2 | 170 | Devastador | 43.210 | 0.950 | 0.950 | 39.239 | -3.971 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.642 |
| Jogador 3 | 5-3 | 175 | Devastador | 43.210 | 0.950 | 0.950 | 41.031 | -2.178 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.642 |
| Jogador 3 | 5-4 | 180 | Devastador | 43.210 | 0.950 | 0.950 | 38.539 | -4.671 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.642 |
| Jogador 3 | 5-5 | 183 | Devastador | 43.210 | 0.950 | 0.950 | 38.761 | -4.448 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.642 |
| Jogador 3 | 5-5 | 185 | Devastador | 43.210 | 0.950 | 0.950 | 40.217 | -2.993 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.642 |
| Jogador 4 | 2-5 | 80 | Florescer | 41.911 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.382 |
| Jogador 4 | 2-6 | 87 | Florescer | 41.911 | 0.950 | 0.950 | 37.535 | -4.376 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 8.382 |
| Jogador 4 | 2-7 | 90 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 7.422 |
| Jogador 4 | 3-1 | 97 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 3-2 | 100 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 3-3 | 107 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 3-4 | 110 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 3-5 | 117 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 3-6 | 120 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 3-7 | 126 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 4-1 | 130 | Colosso | 37.111 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.422 |
| Jogador 4 | 4-2 | 136 | Colosso | 46.094 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.219 |
| Jogador 4 | 4-3 | 140 | Colosso | 45.846 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.169 |
| Jogador 4 | 4-4 | 146 | Colosso | 45.502 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.100 |
| Jogador 4 | 4-5 | 150 | Colosso | 45.834 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.167 |
| Jogador 4 | 4-6 | 156 | Colosso | 46.090 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.218 |
| Jogador 4 | 4-7 | 160 | Colosso | 46.422 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.284 |
| Jogador 4 | 5-1 | 166 | Colosso | 46.447 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.289 |
| Jogador 4 | 5-2 | 170 | Colosso | 45.405 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.081 |
| Jogador 5 | 2-5 | 80 | Enfeitiçador | 43.751 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.750 |
| Jogador 5 | 2-6 | 87 | Enfeitiçador | 43.841 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.768 |
| Jogador 5 | 2-7 | 90 | Enfeitiçador | 43.690 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.738 |
| Jogador 5 | 3-1 | 97 | Enfeitiçador | 44.682 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.936 |
| Jogador 5 | 3-2 | 100 | Enfeitiçador | 44.788 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.958 |
| Jogador 5 | 3-3 | 107 | Enfeitiçador | 45.300 | 0.950 | 0.950 | 44.041 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 9.060 |
| Jogador 5 | 3-3 | 103 | Enfeitiçador | 45.297 | 0.950 | 0.950 | 45.005 | -0.292 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.059 |
| Jogador 5 | 3-4 | 110 | Enfeitiçador | 45.717 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.143 |
| Jogador 5 | 3-5 | 117 | Enfeitiçador | 47.584 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.517 |
| Jogador 5 | 3-6 | 120 | Enfeitiçador | 46.166 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.233 |
| Jogador 5 | 3-7 | 126 | Enfeitiçador | 46.512 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.302 |
| Jogador 5 | 4-1 | 130 | Enfeitiçador | 48.311 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.662 |
| Jogador 5 | 4-2 | 136 | Enfeitiçador | 48.254 | 0.950 | 0.950 | 37.324 | -10.930 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.651 |
| Jogador 5 | 4-3 | 140 | Enfeitiçador | 47.514 | 0.950 | 0.950 | 41.678 | -5.837 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.503 |
| Jogador 5 | 4-4 | 146 | Enfeitiçador | 47.813 | 0.950 | 0.950 | 41.671 | -6.143 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.563 |
| Jogador 5 | 4-5 | 150 | Enfeitiçador | 47.040 | 0.950 | 0.950 | 40.421 | -6.619 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.408 |
| Jogador 5 | 4-6 | 156 | Enfeitiçador | 45.250 | 0.950 | 0.950 | 37.525 | -7.724 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.050 |
| Jogador 5 | 4-7 | 159 | Enfeitiçador | 46.519 | 0.950 | 0.950 | 42.370 | -4.148 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.304 |
| Jogador 5 | 4-7 | 160 | Enfeitiçador | 46.748 | 0.950 | 0.950 | 38.190 | -8.558 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.350 |
| Jogador 5 | 5-1 | 166 | Enfeitiçador | 46.862 | 0.950 | 0.950 | 37.689 | -9.173 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.372 |
| Jogador 5 | 5-2 | 170 | Enfeitiçador | 46.862 | 0.950 | 0.950 | 38.332 | -8.530 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.372 |
| Jogador 5 | 5-3 | 175 | Enfeitiçador | 47.163 | 0.950 | 0.950 | 39.452 | -7.711 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.433 |
| Jogador 5 | 5-4 | 178 | Enfeitiçador | 45.918 | 0.950 | 0.950 | 45.650 | -0.268 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.184 |
| Jogador 5 | 5-4 | 180 | Enfeitiçador | 46.192 | 0.950 | 0.950 | 37.513 | -8.679 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.238 |
| Jogador 5 | 5-5 | 185 | Enfeitiçador | 45.810 | 0.950 | 0.950 | 39.344 | -6.466 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.162 |
| Jogador 5 | 5-6 | 190 | Enfeitiçador | 46.083 | 0.950 | 0.950 | 38.384 | -7.699 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.217 |
| Jogador 5 | 5-7 | 195 | Enfeitiçador | 46.073 | 0.950 | 0.950 | 38.951 | -7.121 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.215 |
| Jogador 5 | 6-1 | 200 | Enfeitiçador | 46.419 | 0.950 | 0.950 | 39.828 | -6.591 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.284 |
| Jogador 5 | 6-2 | 205 | Enfeitiçador | 46.422 | 0.950 | 0.950 | 36.065 | -10.357 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.284 |
| Jogador 6 | 2-5 | 80 | Feérico | 41.464 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.293 |
| Jogador 6 | 2-6 | 87 | Feérico | 39.338 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 7.868 |
| Jogador 6 | 2-7 | 90 | Feérico | 39.063 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 7.813 |
| Jogador 6 | 3-1 | 97 | Feérico | 39.041 | 0.950 | 0.950 | 38.694 | -0.347 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 7.808 |
| Jogador 6 | 3-2 | 100 | Fumegante | 42.026 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.405 |
| Jogador 6 | 3-3 | 107 | Fumegante | 42.026 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.405 |
| Jogador 6 | 3-4 | 110 | Fumegante | 42.026 | 0.950 | 0.950 | 39.676 | -2.350 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.405 |
| Jogador 6 | 3-5 | 117 | Fumegante | 42.026 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.405 |
| Jogador 6 | 3-6 | 120 | Fumegante | 42.026 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.405 |
| Jogador 6 | 3-7 | 126 | Fumegante | 42.026 | 0.950 | 0.950 | 39.417 | -2.609 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.405 |
| Jogador 6 | 4-1 | 130 | Fumegante | 45.128 | 0.950 | 0.950 | 40.181 | -4.947 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.026 |
| Jogador 6 | 4-2 | 136 | Fumegante | 44.964 | 0.950 | 0.950 | 36.562 | -8.402 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.993 |
| Jogador 6 | 4-3 | 140 | Fumegante | 44.964 | 0.950 | 0.950 | 40.716 | -4.248 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.993 |
| Jogador 6 | 4-4 | 146 | Fumegante | 44.964 | 0.950 | 0.950 | 43.793 | -1.171 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.993 |
| Jogador 6 | 4-6 | 156 | Fumegante | 44.964 | 0.950 | 0.950 | 42.451 | -2.513 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.993 |
| Jogador 6 | 4-7 | 160 | Fumegante | 48.534 | 0.950 | 0.950 | 44.154 | -4.380 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.707 |
| Jogador 6 | 5-1 | 166 | Fumegante | 51.410 | 0.950 | 0.950 | 49.903 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 10.282 |
| Jogador 6 | 5-2 | 170 | Fumegante | 51.369 | 0.950 | 0.950 | 49.862 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 10.274 |
| Jogador 6 | 5-3 | 175 | Fumegante | 52.042 | 0.950 | 0.950 | 50.705 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 10.408 |
| Jogador 6 | 5-4 | 177 | Fumegante | 51.758 | 0.950 | 0.950 | 45.978 | -5.779 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.352 |
| Jogador 6 | 5-4 | 180 | Fumegante | 52.166 | 0.950 | 0.950 | 44.153 | -8.013 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.433 |
| Jogador 6 | 5-5 | 185 | Fumegante | 52.230 | 0.950 | 0.950 | 50.894 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 10.446 |
| Jogador 7 | 3-6 | 120 | Colosso | 45.873 | 0.950 | 0.950 | 45.485 | -0.388 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.175 |
| Jogador 7 | 3-7 | 126 | Colosso | 41.789 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.358 |
| Jogador 7 | 4-1 | 130 | Colosso | 41.758 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.352 |
| Jogador 7 | 4-2 | 136 | Colosso | 43.416 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.683 |
| Jogador 7 | 4-3 | 140 | Colosso | 41.655 | 0.950 | 0.950 | 34.666 | -6.988 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.331 |
| Jogador 7 | 4-4 | 146 | Colosso | 41.904 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.381 |
| Jogador 7 | 4-5 | 150 | Colosso | 42.071 | 0.950 | 0.950 | 41.082 | -0.989 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.414 |
| Jogador 7 | 4-6 | 156 | Colosso | 40.454 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.091 |
| Jogador 7 | 4-7 | 160 | Colosso | 40.830 | 0.950 | 0.950 | 37.551 | -3.279 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.166 |
| Jogador 7 | 6-1 | 200 | Colosso | 41.142 | 0.950 | 0.950 | 37.355 | -3.787 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.228 |
| Jogador 7 | 6-5 | 220 | Colosso | 41.142 | 0.950 | 0.950 | 40.858 | -0.284 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.228 |
| Jogador 8 | 2-5 | 80 | Enfeitiçador | 43.226 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.645 |
| Jogador 8 | 2-6 | 87 | Enfeitiçador | 43.226 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.645 |
| Jogador 8 | 2-7 | 90 | Enfeitiçador | 42.932 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.586 |
| Jogador 8 | 3-1 | 94 | Enfeitiçador | 42.889 | 0.950 | 0.950 | 38.828 | -4.061 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.578 |
| Jogador 8 | 3-1 | 97 | Enfeitiçador | 42.656 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.531 |
| Jogador 8 | 3-2 | 100 | Enfeitiçador | 42.699 | 0.950 | 0.950 | 36.404 | -6.294 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.540 |
| Jogador 8 | 3-3 | 107 | Enfeitiçador | 43.033 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.607 |
| Jogador 8 | 3-4 | 110 | Enfeitiçador | 43.033 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.607 |
| Jogador 8 | 3-5 | 117 | Enfeitiçador | 43.033 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.607 |
| Jogador 8 | 3-6 | 120 | Enfeitiçador | 43.033 | 0.950 | 0.950 | 36.212 | -6.821 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.607 |
| Jogador 8 | 3-7 | 126 | Enfeitiçador | 42.217 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.443 |
| Jogador 8 | 4-1 | 130 | Enfeitiçador | 44.206 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.841 |
| Jogador 8 | 4-2 | 136 | Enfeitiçador | 44.579 | 0.950 | 0.950 | 39.127 | -5.452 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.916 |
| Jogador 8 | 4-3 | 140 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 40.806 | -3.770 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 4-4 | 146 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 41.081 | -3.495 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 4-5 | 150 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 41.019 | -3.557 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 4-6 | 156 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 42.228 | -2.348 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 4-7 | 160 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 42.314 | -2.262 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 5-1 | 166 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 41.331 | -3.245 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 5-2 | 170 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 42.680 | -1.896 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 5-3 | 175 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 42.682 | -1.895 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 5-4 | 180 | Enfeitiçador | 44.576 | 0.950 | 0.950 | 42.925 | -1.651 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.915 |
| Jogador 8 | 5-5 | 185 | Enfeitiçador | 46.021 | 0.950 | 0.950 | 42.123 | -3.898 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.204 |
| Jogador 8 | 5-6 | 190 | Enfeitiçador | 46.034 | 0.950 | 0.950 | 43.045 | -2.989 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.207 |

### Unidades preservadas — sinais estratégicos versus investimento

| Jogador | Round | Unidade | Área | Estrelas | Classificação | Sinais estratégicos | Indicadores de investimento |
|---|---|---|---|---:|---|---|---|
| Jogador 1 | 2-5 | Akali | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 2-5 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 2-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 2-6 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 2-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 2-7 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-7 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-7 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 2-7 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-7 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 1 | 2-7 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-1 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-1 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-1 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-1 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-1 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-3 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-3 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-3 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-3 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-3 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-4 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-4 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-4 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-4 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-4 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-5 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-5 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-5 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 3-6 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-6 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-6 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 3-7 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-7 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 3-7 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-7 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-1 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-1 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-1 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-1 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-2 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 4-2 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-2 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 4-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-3 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 4-3 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-3 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-3 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-3 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 4-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-4 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 4-4 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-4 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-4 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-4 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 4-5 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-5 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 4-5 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 4-5 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-5 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 4-5 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 4-6 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 4-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-6 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 4-6 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-6 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-6 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 4-7 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-7 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 4-7 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 4-7 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-7 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 4-7 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-1 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 5-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-1 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-1 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-1 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-3 | Hecarim | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-3 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-3 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 5-3 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-3 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-3 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-4 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-4 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 5-4 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-4 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-4 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-4 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-4 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-4 | Hecarim | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-4 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-4 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-4 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-4 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-4 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-5 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-5 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 5-5 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-5 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-5 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-5 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-6 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-6 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 5-6 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-6 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-6 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-6 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-6 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-6 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-6 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 5-6 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-6 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-6 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-6 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-6 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-7 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-7 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 5-7 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-7 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-7 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-7 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 5-7 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-7 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 5-7 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 5-7 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-7 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-7 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 6-1 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-1 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-1 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-1 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-1 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 6-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-1 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 6-1 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-1 | Ornn | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-1 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 6-1 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-2 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-2 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-2 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-2 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-2 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-2 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-2 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-2 | Nidalee | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 1 | 6-2 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-3 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-3 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-3 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-3 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-3 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-3 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-3 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-3 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-4 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-4 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-4 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-4 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-4 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-4 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-4 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-4 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-4 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-5 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-5 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-5 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-5 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-5 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-6 | Hecarim | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-6 | Shen | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 6-6 | Ornn | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-6 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-6 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-6 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-6 | Amumu | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 6-6 | Nidalee | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 1 | 6-6 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-5 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-5 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-6 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-6 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-7 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-1 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-2 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-2 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-2 | Xayah | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-3 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-3 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-4 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-4 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-4 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-5 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-6 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-6 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 3-6 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-6 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-7 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-7 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 3-7 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-7 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-1 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-1 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-1 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-1 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-1 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-2 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 4-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-2 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-2 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-2 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-2 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-2 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-3 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 4-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-3 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-3 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-3 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-3 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-3 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-4 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 4-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-4 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-4 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-4 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-4 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-4 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 4-5 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-5 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-5 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-5 | Xayah | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-5 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 2 | 4-5 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-5 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-5 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-5 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-5 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 2-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 2-6 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-6 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-6 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-6 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 2-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 2-7 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-7 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-7 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-7 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-1 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-1 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-1 | Camille | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-1 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-1 | Rek'Sai | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 3 | 3-2 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-2 | Camille | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-2 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-2 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 3-2 | Rek'Sai | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 3-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-3 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-3 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-3 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-3 | Rek'Sai | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 3 | 3-3 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-4 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-4 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-4 | Akali | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 3 | 3-4 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-4 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-4 | Rek'Sai | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 3 | 3-4 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-5 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-5 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Rek'Sai | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 3 | 3-5 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-6 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-6 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-6 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-6 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-6 | Rek'Sai | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 3 | 3-6 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-7 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 3-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-7 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 3-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-7 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-7 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-7 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-1 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 4-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-1 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-1 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-1 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 4-1 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-1 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-2 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 4-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-2 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-2 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 4-2 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-2 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 4-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-3 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-3 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 4-3 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-3 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 4-4 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-4 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 4-4 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-4 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-5 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-5 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 4-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-5 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 4-5 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 4-6 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-6 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 4-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-6 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 4-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 4-7 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 4-7 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 4-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-7 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 4-7 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-7 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-7 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 4-7 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-7 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-1 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-1 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-1 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 5-1 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-1 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 5-1 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-1 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 5-1 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-1 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-2 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-2 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-2 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 5-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-2 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 5-2 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 5-2 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-3 | Camille | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-3 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-3 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 5-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-3 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 5-3 | Camille | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-3 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-3 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-4 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-4 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 5-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-4 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 5-4 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 5-4 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-4 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-5 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-5 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 5-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-5 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 5-5 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 5-5 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 3 | 5-5 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-5 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 3 | 5-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-5 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 5-5 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 5-5 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-5 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-5 | Rakan | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-5 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-5 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-5 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Akali | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Karma | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 4 | 2-7 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-7 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 2-7 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-1 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-1 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-1 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-2 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-2 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-2 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 4 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-3 | Akali | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 3-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-3 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 3-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-4 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-5 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-6 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-6 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 3-7 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-7 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-7 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-7 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-1 | Sejuani | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-1 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-1 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-1 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-1 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 4-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-2 | Sejuani | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-2 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-2 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-2 | Akali | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 4 | 4-3 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-3 | Sejuani | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-3 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-3 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-4 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 4-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-4 | Sejuani | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-4 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-4 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-5 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-5 | Sejuani | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-5 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 4-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-6 | Sejuani | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-6 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-6 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-6 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 4-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-7 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-7 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-7 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-7 | Aronguejo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-7 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-7 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 5-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 5-1 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 5-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 5-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 5-1 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 5-1 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 5-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 5-1 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 5-1 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 5-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 5-2 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 4 | 5-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 4 | 5-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 5-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 4 | 5-2 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 5-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 5-2 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 5-2 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-5 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-5 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 2-5 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-5 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 2-5 | Karma | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 2-6 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-6 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 2-6 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-6 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 2-6 | Karma | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 2-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-7 | Rek'Sai | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 5 | 2-7 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 2-7 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-1 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 5 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-1 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-1 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 5 | 3-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-2 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-2 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-3 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 5 | 3-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-3 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-3 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-3 | Ahri | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-3 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 5 | 3-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-3 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-3 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-4 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 5 | 3-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-4 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-4 | Karma | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-4 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-5 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 5 | 3-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-5 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-5 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-5 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-5 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-5 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 3-6 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 5 | 3-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-6 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-7 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 5 | 3-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-7 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 5 | 4-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-1 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-1 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-1 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 5 | 4-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-2 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-2 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-3 | Rek'Sai | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 5 | 4-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-3 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-4 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-4 | Soraka | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 5 | 4-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-4 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-5 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 4-5 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-5 | Karma | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 5 | 4-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-5 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-5 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-5 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-5 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-6 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 4-6 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-6 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-6 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-6 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-6 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-6 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 4-7 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-7 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 5 | 4-7 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 4-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 4-7 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-1 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-1 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-2 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-2 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | LeBlanc | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 5 | 5-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-3 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-4 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-4 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-4 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-4 | Ahri | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-4 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-5 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-5 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-5 | Ahri | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-5 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-5 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-5 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-6 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-6 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-6 | Ahri | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-6 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-6 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-6 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-7 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-7 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-7 | Ahri | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 5-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 5-7 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-7 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-7 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 6-1 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 6-1 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 6-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 6-1 | Ahri | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 6-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 6-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 6-1 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 6-1 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 6-1 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 6-2 | Soraka | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 6-2 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 6-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 6-2 | Ahri | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 6-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 6-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 5 | 6-2 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 6-2 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 6-2 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 2-5 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 2-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 3-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-1 | Cascalho | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 3-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Cascalho | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 6 | 3-2 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 3-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 3-3 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-3 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-3 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 6 | 3-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 3-4 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-4 | Mamãe Bicuda | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-4 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-4 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 3-5 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-5 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 3-6 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-6 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-7 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 3-7 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-7 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-1 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 4-1 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-1 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-2 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 4-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 4-2 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-2 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-2 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-3 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 4-3 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-4 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 4-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 4-4 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-4 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-4 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-6 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 4-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-6 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-6 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 4-6 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-7 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 4-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-7 | Kayle | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-7 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 4-7 | Kayle | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 4-7 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 5-1 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-1 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-1 | Kayle | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-1 | Aphelios | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-1 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-1 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 5-2 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-2 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-2 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-2 | Aphelios | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-2 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-2 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-2 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-3 | Aphelios | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 5-3 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-3 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-3 | Xayah | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 6 | 5-3 | Mamãe Bicuda | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-3 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-3 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-4 | Aphelios | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 5-4 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-4 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-4 | Xayah | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 6 | 5-4 | Mamãe Bicuda | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-4 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-4 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-4 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-4 | Mamãe Bicuda | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-4 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-4 | Xayah | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 6 | 5-4 | Aphelios | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-4 | Tristana | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit |
| Jogador 6 | 5-4 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-5 | Kog'Maw | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-5 | Aphelios | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 5-5 | Kayle | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-5 | Zyra | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 5-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 6 | 5-5 | Xayah | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 6 | 5-5 | Mamãe Bicuda | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 6 | 5-5 | Varus | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 3-6 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-6 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 3-6 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 3-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-6 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 3-7 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 3-7 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 3-7 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 3-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-7 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-7 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-7 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-1 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-1 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-1 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-2 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-2 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-2 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-3 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-3 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-3 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-4 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-4 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-4 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-4 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-5 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-5 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-5 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-5 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-5 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-6 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-6 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-6 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-6 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-6 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 7 | 4-6 | Hecarim | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 7 | 4-7 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-7 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 7 | 4-7 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-7 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-7 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 7 | 4-7 | Hecarim | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 7 | 6-1 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 6-1 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 6-1 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 7 | 6-1 | Ashe | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-1 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-5 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 6-5 | Varus | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 6-5 | Aronguejo | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 7 | 6-5 | Ashe | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-5 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 6-5 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-5 | Karma | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 2-5 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 2-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 2-5 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 2-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 2-6 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 2-7 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 2-7 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-2 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-3 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-3 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 3-3 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-4 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-4 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 8 | 3-4 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-4 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 3-4 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-4 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-5 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 3-5 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-5 | LeBlanc | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 8 | 3-5 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-6 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 3-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 3-6 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-6 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-7 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-7 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 3-7 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 3-7 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-1 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-1 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-1 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-1 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-2 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-2 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-2 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-3 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-3 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-3 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-3 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-4 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-4 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-4 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-4 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-4 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-4 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-4 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-5 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-5 | Cassiopeia | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-5 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-5 | Cassiopeia | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-5 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-5 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-5 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-5 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-6 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-6 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-6 | Sivir | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 4-6 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-6 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-6 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-6 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-7 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-7 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-7 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-7 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-7 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-7 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-7 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-1 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 5-1 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-1 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-1 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-1 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-1 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-1 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-1 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-1 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-2 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 5-2 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-2 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-2 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-2 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-2 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-2 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-2 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-2 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-2 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-3 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 5-3 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-3 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-3 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-3 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-3 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-3 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-3 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-3 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-3 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-4 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 5-4 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-4 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-4 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-4 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-4 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-4 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-4 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-4 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-4 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-5 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 5-5 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-5 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-5 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-5 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-5 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-5 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-5 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-5 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-5 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-6 | Rammus | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 5-6 | Kobuko | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-6 | Sivir | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-6 | Karma | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-6 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-6 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-6 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-6 | Rammus | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-6 | Fiddlesticks | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-6 | Veigar | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |

Unidades preservadas com evidência observável: **1402**.
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
| Jogador 1 | 2-5 | 80 | 2-6 | 0.000 | 1.000 | 6.000 | 0.0 / 6.0 / 4.0 | — |
| Jogador 1 | 2-6 | 87 | 2-7 | 0.000 | 5.000 | -2.000 | 0.0 / 4.0 / 2.0 | — |
| Jogador 1 | 2-7 | 90 | 3-1 | 0.000 | -1.000 | 4.000 | 0.0 / 4.0 / 4.0 | — |
| Jogador 1 | 3-1 | 97 | 3-2 | 0.000 | 5.000 | 0.000 | 0.0 / 11.0 / 0.0 | — |
| Jogador 1 | 3-3 | 105 | 3-4 | 0.000 | 7.000 | 0.000 | 0.0 / 15.0 / 2.0 | — |
| Jogador 1 | 3-4 | 110 | 3-5 | 0.000 | 8.000 | 2.000 | -10.0 / 13.0 / 2.0 | — |
| Jogador 1 | 3-5 | 117 | 3-6 | -10.000 | 5.000 | 0.000 | -10.0 / 13.0 / 0.0 | — |
| Jogador 1 | 3-6 | 120 | 3-7 | 0.000 | 8.000 | 0.000 | -11.0 / 17.0 / 0.0 | — |
| Jogador 1 | 3-7 | 126 | 4-1 | -11.000 | 9.000 | 0.000 | -23.0 / 20.0 / 4.0 | — |
| Jogador 1 | 4-1 | 130 | 4-2 | -12.000 | 11.000 | 4.000 | -12.0 / 19.0 / 4.0 | — |
| Jogador 1 | 4-2 | 136 | 4-3 | 0.000 | 8.000 | 0.000 | 0.0 / 19.0 / 4.0 | — |
| Jogador 1 | 4-3 | 140 | 4-4 | 0.000 | 11.000 | 4.000 | 0.0 / 15.0 / 4.0 | — |
| Jogador 1 | 4-4 | 146 | 4-5 | 0.000 | 4.000 | 0.000 | 0.0 / 16.0 / 0.0 | — |
| Jogador 1 | 4-5 | 150 | 4-6 | 0.000 | 12.000 | 0.000 | 0.0 / 27.0 / 0.0 | — |
| Jogador 1 | 4-5 | 149 | 4-6 | 0.000 | 12.000 | 0.000 | 0.0 / 27.0 / 0.0 | — |
| Jogador 1 | 4-6 | 156 | 4-7 | 0.000 | 15.000 | 0.000 | 0.0 / 20.0 / 6.0 | — |
| Jogador 1 | 4-7 | 158 | 5-1 | 0.000 | 5.000 | 6.000 | -13.0 / 12.0 / 6.0 | — |
| Jogador 1 | 4-7 | 160 | 5-1 | 0.000 | 5.000 | 6.000 | -13.0 / 12.0 / 6.0 | — |
| Jogador 1 | 5-1 | 166 | 5-2 | -13.000 | 7.000 | 0.000 | -13.0 / 15.0 / 4.0 | — |
| Jogador 1 | 5-3 | 175 | 5-4 | 0.000 | 8.000 | 2.000 | 0.0 / 19.0 / 2.0 | — |
| Jogador 1 | 5-4 | 180 | 5-5 | 0.000 | 11.000 | 0.000 | 0.0 / 23.0 / 0.0 | — |
| Jogador 1 | 5-4 | 178 | 5-5 | 0.000 | 11.000 | 0.000 | 0.0 / 23.0 / 0.0 | — |
| Jogador 1 | 5-5 | 185 | 5-6 | 0.000 | 12.000 | 0.000 | 0.0 / 23.0 / 0.0 | — |
| Jogador 1 | 5-6 | 189 | 5-7 | 0.000 | 11.000 | 0.000 | 0.0 / 23.0 / 6.0 | — |
| Jogador 1 | 5-6 | 190 | 5-7 | 0.000 | 11.000 | 0.000 | 0.0 / 23.0 / 6.0 | — |
| Jogador 1 | 5-7 | 194 | 6-1 | 0.000 | 12.000 | 6.000 | 0.0 / 21.0 / 6.0 | — |
| Jogador 1 | 5-7 | 195 | 6-1 | 0.000 | 12.000 | 6.000 | 0.0 / 21.0 / 6.0 | — |
| Jogador 1 | 6-1 | 200 | 6-2 | 0.000 | 9.000 | 0.000 | -18.0 / 16.0 / 0.0 | — |
| Jogador 1 | 6-1 | 198 | 6-2 | 0.000 | 9.000 | 0.000 | -18.0 / 16.0 / 0.0 | — |
| Jogador 1 | 6-2 | 205 | 6-3 | -18.000 | 7.000 | 0.000 | -18.0 / 15.0 / 0.0 | — |
| Jogador 1 | 6-3 | 210 | 6-4 | 0.000 | 8.000 | 0.000 | -18.0 / 17.0 / 0.0 | — |
| Jogador 1 | 6-4 | 215 | 6-5 | -18.000 | 9.000 | 0.000 | None / None / None | — |
| Jogador 1 | 6-5 | 220 | — | — | — | — | None / None / None | — |
| Jogador 1 | 6-5 | 218 | — | — | — | — | None / None / None | — |
| Jogador 1 | 6-6 | 225 | — | — | — | — | None / None / None | — |
| Jogador 2 | 2-5 | 80 | 2-6 | -5.000 | 9.000 | 0.000 | -5.0 / 17.0 / 0.0 | 8 |
| Jogador 2 | 2-6 | 87 | 2-7 | 0.000 | 8.000 | 0.000 | -11.0 / 24.0 / 0.0 | 8 |
| Jogador 2 | 2-7 | 90 | 3-1 | -11.000 | 16.000 | 0.000 | -20.0 / 24.0 / 0.0 | 8 |
| Jogador 2 | 3-1 | 97 | 3-2 | -9.000 | 8.000 | 0.000 | -9.0 / 16.0 / 0.0 | 8 |
| Jogador 2 | 3-2 | 100 | 3-3 | 0.000 | 8.000 | 0.000 | 0.0 / 15.0 / 0.0 | 8 |
| Jogador 2 | 3-3 | 107 | 3-4 | 0.000 | 7.000 | 0.000 | 0.0 / 21.0 / 6.0 | 8 |
| Jogador 2 | 3-4 | 110 | 3-5 | 0.000 | 14.000 | 6.000 | -11.0 / 20.0 / 6.0 | 8 |
| Jogador 2 | 3-5 | 117 | 3-6 | -11.000 | 6.000 | 0.000 | -11.0 / 3.0 / 0.0 | 8 |
| Jogador 2 | 3-6 | 120 | 3-7 | 0.000 | -3.000 | 0.000 | -12.0 / 10.0 / 0.0 | 8 |
| Jogador 2 | 3-7 | 126 | 4-1 | -12.000 | 13.000 | 0.000 | -23.0 / 22.0 / 0.0 | 8 |
| Jogador 2 | 4-1 | 130 | 4-2 | -11.000 | 9.000 | 0.000 | -24.0 / 22.0 / 0.0 | 8 |
| Jogador 2 | 4-2 | 136 | 4-3 | -13.000 | 13.000 | 0.000 | -13.0 / 26.0 / 0.0 | 8 |
| Jogador 2 | 4-3 | 140 | 4-4 | 0.000 | 13.000 | 0.000 | -11.0 / 11.0 / -18.0 | 8 |
| Jogador 2 | 4-4 | 146 | 4-5 | -11.000 | -2.000 | -18.000 | None / None / None | 8 |
| Jogador 2 | 4-5 | 150 | — | — | — | — | None / None / None | 8 |
| Jogador 3 | 2-5 | 80 | 2-6 | 0.000 | 2.000 | 2.000 | 0.0 / 12.0 / 2.0 | 6 |
| Jogador 3 | 2-6 | 87 | 2-7 | 0.000 | 10.000 | 0.000 | -10.0 / 12.0 / 0.0 | 6 |
| Jogador 3 | 2-7 | 90 | 3-1 | -10.000 | 2.000 | 0.000 | -21.0 / 9.0 / 0.0 | 6 |
| Jogador 3 | 3-1 | 97 | 3-2 | -11.000 | 7.000 | 0.000 | -21.0 / 14.0 / 4.0 | 6 |
| Jogador 3 | 3-2 | 100 | 3-3 | -10.000 | 7.000 | 4.000 | -10.0 / 16.0 / 6.0 | 6 |
| Jogador 3 | 3-3 | 107 | 3-4 | 0.000 | 9.000 | 2.000 | 0.0 / 15.0 / 8.0 | 6 |
| Jogador 3 | 3-4 | 110 | 3-5 | 0.000 | 6.000 | 6.000 | -9.0 / 18.0 / 6.0 | 6 |
| Jogador 3 | 3-5 | 117 | 3-6 | -9.000 | 12.000 | 0.000 | -9.0 / 16.0 / -4.0 | 6 |
| Jogador 3 | 3-6 | 120 | 3-7 | 0.000 | 4.000 | -4.000 | 0.0 / 23.0 / -4.0 | 6 |
| Jogador 3 | 3-7 | 126 | 4-1 | 0.000 | 19.000 | 0.000 | 0.0 / 28.0 / 0.0 | 6 |
| Jogador 3 | 4-1 | 130 | 4-2 | 0.000 | 9.000 | 0.000 | 0.0 / 24.0 / 0.0 | 6 |
| Jogador 3 | 4-2 | 136 | 4-3 | 0.000 | 15.000 | 0.000 | 0.0 / 24.0 / 0.0 | 6 |
| Jogador 3 | 4-3 | 140 | 4-4 | 0.000 | 9.000 | 0.000 | 0.0 / 23.0 / 0.0 | 6 |
| Jogador 3 | 4-4 | 146 | 4-5 | 0.000 | 14.000 | 0.000 | -13.0 / 22.0 / 0.0 | 6 |
| Jogador 3 | 4-5 | 150 | 4-6 | -13.000 | 8.000 | 0.000 | -13.0 / 17.0 / -2.0 | 6 |
| Jogador 3 | 4-6 | 156 | 4-7 | 0.000 | 9.000 | -2.000 | -13.0 / 16.0 / -2.0 | 6 |
| Jogador 3 | 4-7 | 160 | 5-1 | -13.000 | 7.000 | 0.000 | -13.0 / 27.0 / 0.0 | 6 |
| Jogador 3 | 5-1 | 166 | 5-2 | 0.000 | 20.000 | 0.000 | -16.0 / 27.0 / 0.0 | 6 |
| Jogador 3 | 5-2 | 170 | 5-3 | -16.000 | 7.000 | 0.000 | -16.0 / 17.0 / 0.0 | 6 |
| Jogador 3 | 5-3 | 175 | 5-4 | 0.000 | 10.000 | 0.000 | -13.0 / 4.0 / -26.0 | 6 |
| Jogador 3 | 5-4 | 180 | 5-5 | -13.000 | -6.000 | -26.000 | None / None / None | 6 |
| Jogador 3 | 5-5 | 183 | — | — | — | — | None / None / None | 6 |
| Jogador 3 | 5-5 | 185 | — | — | — | — | None / None / None | 6 |
| Jogador 4 | 2-5 | 80 | 2-6 | -7.000 | 2.000 | 2.000 | -7.0 / 5.0 / 2.0 | 7 |
| Jogador 4 | 2-6 | 87 | 2-7 | 0.000 | 3.000 | 0.000 | 0.0 / 5.0 / 6.0 | 7 |
| Jogador 4 | 2-7 | 90 | 3-1 | 0.000 | 2.000 | 6.000 | -11.0 / 6.0 / 4.0 | 7 |
| Jogador 4 | 3-1 | 97 | 3-2 | -11.000 | 4.000 | -2.000 | -21.0 / 5.0 / -2.0 | 7 |
| Jogador 4 | 3-2 | 100 | 3-3 | -10.000 | 1.000 | 0.000 | -10.0 / 5.0 / 6.0 | 7 |
| Jogador 4 | 3-3 | 107 | 3-4 | 0.000 | 4.000 | 6.000 | -10.0 / 5.0 / 6.0 | 7 |
| Jogador 4 | 3-4 | 110 | 3-5 | -10.000 | 1.000 | 0.000 | -10.0 / 12.0 / 0.0 | 7 |
| Jogador 4 | 3-5 | 117 | 3-6 | 0.000 | 11.000 | 0.000 | 0.0 / 14.0 / -2.0 | 7 |
| Jogador 4 | 3-6 | 120 | 3-7 | 0.000 | 3.000 | -2.000 | 0.0 / 13.0 / -2.0 | 7 |
| Jogador 4 | 3-7 | 126 | 4-1 | 0.000 | 10.000 | 0.000 | -10.0 / 25.0 / 0.0 | 7 |
| Jogador 4 | 4-1 | 130 | 4-2 | -10.000 | 15.000 | 0.000 | -22.0 / 24.0 / 0.0 | 7 |
| Jogador 4 | 4-2 | 136 | 4-3 | -12.000 | 9.000 | 0.000 | -12.0 / 21.0 / 0.0 | 7 |
| Jogador 4 | 4-3 | 140 | 4-4 | 0.000 | 12.000 | 0.000 | -10.0 / 22.0 / 0.0 | 7 |
| Jogador 4 | 4-4 | 146 | 4-5 | -10.000 | 10.000 | 0.000 | -21.0 / 18.0 / 0.0 | 7 |
| Jogador 4 | 4-5 | 150 | 4-6 | -11.000 | 8.000 | 0.000 | -11.0 / 18.0 / 0.0 | 7 |
| Jogador 4 | 4-6 | 156 | 4-7 | 0.000 | 10.000 | 0.000 | 0.0 / 21.0 / 2.0 | 7 |
| Jogador 4 | 4-7 | 160 | 5-1 | 0.000 | 11.000 | 2.000 | -3.0 / 7.0 / -20.0 | 7 |
| Jogador 4 | 5-1 | 166 | 5-2 | -3.000 | -4.000 | -22.000 | None / None / None | 7 |
| Jogador 4 | 5-2 | 170 | — | — | — | — | None / None / None | 7 |
| Jogador 5 | 2-5 | 80 | 2-6 | -5.000 | 10.000 | 0.000 | -5.0 / 15.0 / 2.0 | 3 |
| Jogador 5 | 2-6 | 87 | 2-7 | 0.000 | 5.000 | 2.000 | 0.0 / 8.0 / 8.0 | 3 |
| Jogador 5 | 2-7 | 90 | 3-1 | 0.000 | 3.000 | 6.000 | 0.0 / 7.0 / 6.0 | 3 |
| Jogador 5 | 3-1 | 97 | 3-2 | 0.000 | 4.000 | 0.000 | 0.0 / 14.0 / 0.0 | 3 |
| Jogador 5 | 3-2 | 100 | 3-3 | 0.000 | 10.000 | 0.000 | 0.0 / 18.0 / 0.0 | 3 |
| Jogador 5 | 3-3 | 107 | 3-4 | 0.000 | 8.000 | 0.000 | -11.0 / 18.0 / 0.0 | 3 |
| Jogador 5 | 3-3 | 103 | 3-4 | 0.000 | 8.000 | 0.000 | -11.0 / 18.0 / 0.0 | 3 |
| Jogador 5 | 3-4 | 110 | 3-5 | -11.000 | 10.000 | 0.000 | -11.0 / 18.0 / 0.0 | 3 |
| Jogador 5 | 3-5 | 117 | 3-6 | 0.000 | 8.000 | 0.000 | 0.0 / 19.0 / 0.0 | 3 |
| Jogador 5 | 3-6 | 120 | 3-7 | 0.000 | 11.000 | 0.000 | 0.0 / 20.0 / 0.0 | 3 |
| Jogador 5 | 3-7 | 126 | 4-1 | 0.000 | 9.000 | 0.000 | 0.0 / 20.0 / -4.0 | 3 |
| Jogador 5 | 4-1 | 130 | 4-2 | 0.000 | 11.000 | -4.000 | -11.0 / 21.0 / -2.0 | 3 |
| Jogador 5 | 4-2 | 136 | 4-3 | -11.000 | 10.000 | 2.000 | -11.0 / 25.0 / 2.0 | 3 |
| Jogador 5 | 4-3 | 140 | 4-4 | 0.000 | 15.000 | 0.000 | -12.0 / 24.0 / 6.0 | 3 |
| Jogador 5 | 4-4 | 146 | 4-5 | -12.000 | 9.000 | 6.000 | -22.0 / 17.0 / 6.0 | 3 |
| Jogador 5 | 4-5 | 150 | 4-6 | -10.000 | 8.000 | 0.000 | -10.0 / 19.0 / 0.0 | 3 |
| Jogador 5 | 4-6 | 156 | 4-7 | 0.000 | 11.000 | 0.000 | 0.0 / 20.0 / 0.0 | 3 |
| Jogador 5 | 4-7 | 159 | 5-1 | 0.000 | 9.000 | 0.000 | 0.0 / 21.0 / 0.0 | 3 |
| Jogador 5 | 4-7 | 160 | 5-1 | 0.000 | 9.000 | 0.000 | 0.0 / 21.0 / 0.0 | 3 |
| Jogador 5 | 5-1 | 166 | 5-2 | 0.000 | 12.000 | 0.000 | 0.0 / 16.0 / 0.0 | 3 |
| Jogador 5 | 5-2 | 170 | 5-3 | 0.000 | 4.000 | 0.000 | 0.0 / 15.0 / 0.0 | 3 |
| Jogador 5 | 5-3 | 175 | 5-4 | 0.000 | 11.000 | 0.000 | -17.0 / 19.0 / 8.0 | 3 |
| Jogador 5 | 5-4 | 178 | 5-5 | -17.000 | 8.000 | 8.000 | -32.0 / 19.0 / 8.0 | 3 |
| Jogador 5 | 5-4 | 180 | 5-5 | -17.000 | 8.000 | 8.000 | -32.0 / 19.0 / 8.0 | 3 |
| Jogador 5 | 5-5 | 185 | 5-6 | -15.000 | 11.000 | 0.000 | -15.0 / 21.0 / 0.0 | 3 |
| Jogador 5 | 5-6 | 190 | 5-7 | 0.000 | 10.000 | 0.000 | -16.0 / 24.0 / 0.0 | 3 |
| Jogador 5 | 5-7 | 195 | 6-1 | -16.000 | 14.000 | 0.000 | -19.0 / 14.0 / -34.0 | 3 |
| Jogador 5 | 6-1 | 200 | 6-2 | -3.000 | 0.000 | -34.000 | None / None / None | 3 |
| Jogador 5 | 6-2 | 205 | — | — | — | — | None / None / None | 3 |
| Jogador 6 | 2-5 | 80 | 2-6 | -5.000 | 6.000 | 0.000 | -5.0 / 7.0 / 0.0 | 5 |
| Jogador 6 | 2-6 | 87 | 2-7 | 0.000 | 1.000 | 0.000 | 0.0 / -4.0 / 4.0 | 5 |
| Jogador 6 | 2-7 | 90 | 3-1 | 0.000 | -5.000 | 4.000 | 0.0 / 6.0 / 8.0 | 5 |
| Jogador 6 | 3-1 | 97 | 3-2 | 0.000 | 11.000 | 4.000 | -9.0 / 4.0 / 4.0 | 5 |
| Jogador 6 | 3-2 | 100 | 3-3 | -9.000 | -7.000 | 0.000 | -9.0 / -1.0 / 0.0 | 5 |
| Jogador 6 | 3-3 | 107 | 3-4 | 0.000 | 6.000 | 0.000 | 0.0 / -6.0 / 6.0 | 5 |
| Jogador 6 | 3-4 | 110 | 3-5 | 0.000 | -12.000 | 6.000 | 0.0 / -7.0 / 6.0 | 5 |
| Jogador 6 | 3-5 | 117 | 3-6 | 0.000 | 5.000 | 0.000 | 0.0 / 13.0 / 0.0 | 5 |
| Jogador 6 | 3-6 | 120 | 3-7 | 0.000 | 8.000 | 0.000 | 0.0 / 15.0 / 0.0 | 5 |
| Jogador 6 | 3-7 | 126 | 4-1 | 0.000 | 7.000 | 0.000 | 0.0 / 27.0 / 0.0 | 5 |
| Jogador 6 | 4-1 | 130 | 4-2 | 0.000 | 20.000 | 0.000 | 0.0 / 27.0 / 0.0 | 5 |
| Jogador 6 | 4-2 | 136 | 4-3 | 0.000 | 7.000 | 0.000 | 0.0 / 12.0 / 0.0 | 5 |
| Jogador 6 | 4-3 | 140 | 4-4 | 0.000 | 5.000 | 0.000 | -11.0 / 13.0 / 0.0 | 5 |
| Jogador 6 | 4-4 | 146 | 4-5 | -11.000 | 8.000 | 0.000 | -11.0 / 14.0 / 0.0 | 5 |
| Jogador 6 | 4-6 | 156 | 4-7 | 0.000 | 10.000 | -2.000 | -13.0 / 14.0 / -2.0 | 5 |
| Jogador 6 | 4-7 | 160 | 5-1 | -13.000 | 4.000 | 0.000 | -27.0 / 12.0 / 6.0 | 5 |
| Jogador 6 | 5-1 | 166 | 5-2 | -14.000 | 8.000 | 6.000 | -30.0 / 15.0 / 4.0 | 5 |
| Jogador 6 | 5-2 | 170 | 5-3 | -16.000 | 7.000 | -2.000 | -16.0 / 14.0 / 6.0 | 5 |
| Jogador 6 | 5-3 | 175 | 5-4 | 0.000 | 7.000 | 8.000 | -10.0 / 9.0 / -30.0 | 5 |
| Jogador 6 | 5-4 | 177 | 5-5 | -10.000 | 2.000 | -38.000 | None / None / None | 5 |
| Jogador 6 | 5-4 | 180 | 5-5 | -10.000 | 2.000 | -38.000 | None / None / None | 5 |
| Jogador 6 | 5-5 | 185 | — | — | — | — | None / None / None | 5 |
| Jogador 7 | 3-6 | 120 | 3-7 | 0.000 | 11.000 | 0.000 | -11.0 / 16.0 / 0.0 | — |
| Jogador 7 | 3-7 | 126 | 4-1 | -11.000 | 5.000 | 0.000 | -22.0 / 14.0 / 0.0 | — |
| Jogador 7 | 4-1 | 130 | 4-2 | -11.000 | 9.000 | 0.000 | -23.0 / 21.0 / 0.0 | — |
| Jogador 7 | 4-2 | 136 | 4-3 | -12.000 | 12.000 | 0.000 | -12.0 / 13.0 / 4.0 | — |
| Jogador 7 | 4-3 | 140 | 4-4 | 0.000 | 1.000 | 4.000 | 0.0 / 9.0 / 4.0 | — |
| Jogador 7 | 4-4 | 146 | 4-5 | 0.000 | 8.000 | 0.000 | 0.0 / 19.0 / -8.0 | — |
| Jogador 7 | 4-5 | 150 | 4-6 | 0.000 | 11.000 | -8.000 | 0.0 / 19.0 / 2.0 | — |
| Jogador 7 | 4-6 | 156 | 4-7 | 0.000 | 8.000 | 10.000 | 0.0 / 10.0 / 20.0 | — |
| Jogador 7 | 4-7 | 160 | 5-1 | 0.000 | 2.000 | 10.000 | 0.0 / 9.0 / 10.0 | — |
| Jogador 7 | 6-1 | 200 | 6-2 | 0.000 | 21.000 | 0.000 | 0.0 / 34.0 / 0.0 | — |
| Jogador 7 | 6-5 | 220 | — | — | — | — | None / None / None | — |
| Jogador 8 | 2-5 | 80 | 2-6 | 0.000 | 6.000 | 8.000 | 0.0 / 12.0 / 8.0 | 4 |
| Jogador 8 | 2-6 | 87 | 2-7 | 0.000 | 6.000 | 0.000 | -12.0 / 11.0 / 0.0 | 4 |
| Jogador 8 | 2-7 | 90 | 3-1 | -12.000 | 5.000 | 0.000 | -12.0 / 15.0 / 0.0 | 4 |
| Jogador 8 | 3-1 | 94 | 3-2 | 0.000 | 10.000 | 0.000 | -9.0 / 17.0 / 0.0 | 4 |
| Jogador 8 | 3-1 | 97 | 3-2 | 0.000 | 10.000 | 0.000 | -9.0 / 17.0 / 0.0 | 4 |
| Jogador 8 | 3-2 | 100 | 3-3 | -9.000 | 7.000 | 0.000 | -9.0 / 16.0 / 0.0 | 4 |
| Jogador 8 | 3-3 | 107 | 3-4 | 0.000 | 9.000 | 0.000 | -9.0 / 12.0 / 0.0 | 4 |
| Jogador 8 | 3-4 | 110 | 3-5 | -9.000 | 3.000 | 0.000 | -19.0 / 18.0 / 2.0 | 4 |
| Jogador 8 | 3-5 | 117 | 3-6 | -10.000 | 15.000 | 2.000 | -10.0 / 25.0 / 2.0 | 4 |
| Jogador 8 | 3-6 | 120 | 3-7 | 0.000 | 10.000 | 0.000 | -11.0 / 18.0 / 0.0 | 4 |
| Jogador 8 | 3-7 | 126 | 4-1 | -11.000 | 8.000 | 0.000 | -11.0 / 12.0 / 6.0 | 4 |
| Jogador 8 | 4-1 | 130 | 4-2 | 0.000 | 4.000 | 6.000 | 0.0 / 19.0 / 6.0 | 4 |
| Jogador 8 | 4-2 | 136 | 4-3 | 0.000 | 15.000 | 0.000 | 0.0 / 24.0 / 0.0 | 4 |
| Jogador 8 | 4-3 | 140 | 4-4 | 0.000 | 9.000 | 0.000 | 0.0 / 23.0 / 0.0 | 4 |
| Jogador 8 | 4-4 | 146 | 4-5 | 0.000 | 14.000 | 0.000 | 0.0 / 28.0 / 2.0 | 4 |
| Jogador 8 | 4-5 | 150 | 4-6 | 0.000 | 14.000 | 2.000 | 0.0 / 21.0 / 2.0 | 4 |
| Jogador 8 | 4-6 | 156 | 4-7 | 0.000 | 7.000 | 0.000 | -14.0 / 18.0 / 0.0 | 4 |
| Jogador 8 | 4-7 | 160 | 5-1 | -14.000 | 11.000 | 0.000 | -14.0 / 20.0 / 0.0 | 4 |
| Jogador 8 | 5-1 | 166 | 5-2 | 0.000 | 9.000 | 0.000 | -15.0 / 19.0 / 0.0 | 4 |
| Jogador 8 | 5-2 | 170 | 5-3 | -15.000 | 10.000 | 0.000 | -15.0 / 19.0 / 0.0 | 4 |
| Jogador 8 | 5-3 | 175 | 5-4 | 0.000 | 9.000 | 0.000 | 0.0 / 22.0 / 0.0 | 4 |
| Jogador 8 | 5-4 | 180 | 5-5 | 0.000 | 13.000 | 0.000 | -3.0 / 10.0 / -32.0 | 4 |
| Jogador 8 | 5-5 | 185 | 5-6 | -3.000 | -3.000 | -32.000 | None / None / None | 4 |
| Jogador 8 | 5-6 | 190 | — | — | — | — | None / None / None | 4 |

A evolução posterior é associação temporal, não atribuição causal à recomendação shadow.


### Auditoria de INSUFFICIENT_EVIDENCE

| Jogador | Round | Step | Motivo específico | Geração de candidatos | Direção atual | Viável atual | Score atual | Score âncora | Vantagem | Mín. ADAPT | Limite PIVOT | Conf. âncora | Conf. direção atual | Âncora disponível | Filtros (considerados/gerados/catálogo ausente/planos vazios/âncora ausente) |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Jogador 1 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-3 | 27 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-2 | 59 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-3 | 67 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-4 | 72 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-5 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-3 | 31 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-4 | 40 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-2 | 59 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-3 | 68 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-4 | 72 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-5 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 16 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-1 | 4 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-3 | 31 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-4 | 38 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-3 | 64 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-4 | 72 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 16 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-5 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 17 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-1 | 4 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-3 | 27 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-2 | 59 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-3 | 68 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-4 | 72 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-5 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-3 | 24 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 9 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-1 | 48 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-3 | 68 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-4 | 72 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-5 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 15 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-3 | 31 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-4 | 35 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-2 | 56 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-3 | 66 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-4 | 72 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 15 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-5 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 17 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-1 | 2 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-3 | 28 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-4 | 38 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-2 | 59 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-3 | 68 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-2 | 21 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-3 | 25 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-4 | 39 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 7 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-2 | 59 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-3 | 68 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-4 | 72 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 16 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-5 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 17 / 0 / 0 / 0 / 0 |

**Motivos agregados:** unavailable=8; no_initial_anchor_available=70
**Motivos de geração agregados:** unavailable=8; no_cost_four_or_five_anchor=70
**Viabilidade da direção atual:** not_viable=78

Confiança da âncora e confiança da direção atual são derivadas de score e não são probabilidades calibradas. Snapshots por ação podem repetir a mesma revisão; não devem ser contados como revisões independentes.
