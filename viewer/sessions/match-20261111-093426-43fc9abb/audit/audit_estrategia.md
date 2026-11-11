# Strategic Planner — recomendações

Direção atual e recomendação do planner são mantidas separadas. O planner não altera o compromisso ativo nesta fase.

> Recomendações em shadow mode são diagnósticos heurísticos. Elas não foram executadas nem alteraram a ação do PPO.

| Jogador | Round | Steps observados | Observações | Direção ativa | Decisão | Direção alvo | Âncora | Confiança | Custo de transição | Preservadas | Substituíveis | Candidatos avaliados (ID/direção/score/resultado) | Motivo |
|---|---|---|---:|---|---|---:|---:|---:|---:|---|---|---|---|
| Jogador 1 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 1 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 6 |  |  | insufficient_evidence |
| Jogador 1 | 1-2 | 12–17 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 6, 0 |  |  | insufficient_evidence |
| Jogador 1 | 1-3 | 22–26 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 0, 6 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 2-1 | 43–47 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 0, 6, 7 | 12, 5 |  | insufficient_evidence |
| Jogador 1 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 0, 6 | 12, 14 |  | insufficient_evidence |
| Jogador 1 | 2-3 | 62–68 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0, 6, 7, 7, 0, 6 | 12, 23 |  | insufficient_evidence |
| Jogador 1 | 2-4 | 72–80 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 7, 6, 0 | 23, 12, 19, 33 |  | insufficient_evidence |
| Jogador 1 | 2-5 | 82–82 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 7, 6, 0 | 23, 12, 19, 33 |  | insufficient_evidence |
| Jogador 1 | 2-5 | 83–83 | 1 | Inferno | ABANDON | — | -1 | 0.650 | 0.000 | 7 | 7, 0, 23, 12, 6, 19, 0, 33, 23 |  | board_deficit |
| Jogador 1 | 2-5 | 84–90 | 7 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 0, 23, 23, 7, 0, 33 | 12, 18 |  | board_advantage |
| Jogador 1 | 2-6 | 92–98 | 7 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 7, 23, 23, 0, 33 | 12, 34, 28, 18 |  | board_advantage |
| Jogador 1 | 2-7 | 101–109 | 9 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 23, 23, 34, 33 | 12, 21, 28, 18, 18, 2, 16 |  | board_advantage |
| Jogador 1 | 3-1 | 111–115 | 5 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 23, 23, 34, 33 | 12, 21, 15, 14, 28, 18, 18, 2, 16, 36 |  | board_advantage |
| Jogador 1 | 3-2 | 120–120 | 1 | Inferno | KEEP | Inferno | 45 | 0.950 | 0.545 | 7, 23, 23, 34, 33 | 12, 21, 15, 14, 28, 18, 18, 2, 16, 36 | 45:Sabugueiro:36.404:selected_best_candidate, 45:Carrasco:30.407:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 3-3 | 122–127 | 6 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 23, 23, 34, 33 | 12, 21, 15, 14, 28, 18, 18, 14, 16, 36 |  | board_advantage |
| Jogador 1 | 3-4 | 129–130 | 2 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 23, 23, 34, 33 | 12, 21, 15, 14, 28, 18, 18, 14, 36 |  | board_advantage |
| Jogador 1 | 3-5 | 132–138 | 7 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 34, 33, 23 | 14, 12, 21, 40, 15, 28, 18, 18, 14, 36 |  | board_advantage |
| Jogador 1 | 3-6 | 140–140 | 1 | Inferno | KEEP | Inferno | 49 | 0.950 | 0.933 | 7, 34, 33, 23 | 14, 12, 21, 40, 15, 28, 18, 18, 14, 36 | 49:Primordial:26.735:selected_best_candidate, 49:Adaptador:26.735:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 3-7 | 142–145 | 4 | Inferno | KEEP | Inferno | 65 | 0.950 | 0.545 | 34, 7, 23, 33, 33, 23 | 40, 14, 12, 21, 15, 28, 18, 18, 14, 36 | 65:Feérico:35.921:selected_best_candidate, 65:Avatar:32.501:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-1 | 151–156 | 6 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 40, 34, 7, 23, 33, 33 | 14, 12, 21, 15, 28, 18, 18, 14, 40, 36 |  | board_advantage |
| Jogador 1 | 4-2 | 158–160 | 3 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 40, 34, 7, 23, 33, 0, 33 | 12, 14, 21, 15, 18, 18, 14, 40, 36 |  | board_advantage |
| Jogador 1 | 4-3 | 162–168 | 7 | Inferno | KEEP | Inferno | 51 | 0.950 | 0.933 | 34, 40, 7, 23, 33, 0, 33 | 14, 21, 15, 12, 18, 18, 14, 40, 36 | 51:Florescer:25.086:selected_best_candidate, 51:Lutador:25.086:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-4 | 170–170 | 1 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 34, 40, 7, 23, 33, 0, 33 | 14, 21, 12, 15, 18, 18, 14, 40, 36 |  | board_advantage |
| Jogador 1 | 4-5 | 172–174 | 3 | Inferno | KEEP | Inferno | 47 | 0.950 | 0.667 | 34, 40, 7, 23, 33, 0, 33 | 14, 21, 12, 15, 18, 18, 14, 40 | 47:Espinhos Negros:34.717:selected_best_candidate, 47:Monólito:34.520:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-5 | 175–178 | 4 | Inferno | KEEP | Inferno | 53 | 0.950 | 0.400 | 34, 7, 40, 23, 33, 0, 33 | 14, 21, 15, 12, 18, 18, 14, 40, 53 | 53:Flora Fatalis:34.067:selected_best_candidate, 53:Carrasco:32.951:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 4-6 | 180–180 | 1 | Inferno | KEEP | Inferno | 53 | 0.950 | 0.545 | 7, 34, 40, 23, 33, 0, 33 | 14, 21, 15, 12, 18, 18, 14, 40, 53 | 53:Flora Fatalis:34.595:valid_but_not_selected, 53:Carrasco:36.117:selected_best_candidate | board_advantage |
| Jogador 1 | 4-7 | 182–187 | 6 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 34, 40, 23, 0, 33 | 14, 12, 21, 15, 25, 38, 18, 18, 14, 40 |  | board_advantage |
| Jogador 1 | 5-1 | 189–190 | 2 | Inferno | KEEP | Inferno | 51 | 0.950 | 0.933 | 7, 34, 40, 23, 0, 33 | 14, 12, 15, 21, 25, 38, 18, 18, 14, 40 | 51:Florescer:30.206:selected_best_candidate, 51:Lutador:30.206:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-2 | 192–198 | 5 | Inferno | KEEP | Inferno | 41 | 0.950 | 0.222 | 7, 34, 15, 40, 23, 0, 40 | 14, 12, 21, 30, 29, 18, 18, 14, 12 | 41:Florescer:40.189:valid_but_not_selected, 41:Enfeitiçador:41.953:selected_best_candidate | board_advantage |
| Jogador 1 | 5-2 | 193–194 | 2 | Inferno | ADAPT | Enfeitiçador | 41 | 0.650 | 0.222 | 7, 34, 15, 40, 40 | 14, 12, 21, 23, 25, 0, 38, 18, 18, 14, 12 | 41:Florescer:40.122:valid_but_not_selected, 41:Enfeitiçador:41.777:selected_best_candidate | anchor_opportunity |
| Jogador 1 | 5-3 | 200–200 | 1 | Inferno | KEEP | Inferno | 42 | 0.950 | 0.000 | 7, 34, 15, 40, 23, 0, 40 | 14, 12, 21, 30, 18, 18, 14, 12 | 42:Inferno:43.517:selected_best_candidate, 42:Colosso:42.906:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 5-4 | 202–208 | 7 | Inferno | KEEP | Inferno | -1 | 0.000 | 0.000 | 7, 34, 15, 40, 0, 0, 40 | 14, 21, 21, 12, 18, 18, 15 |  | board_advantage |
| Jogador 1 | 5-5 | 210–210 | 1 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.222 | 7, 34, 21, 15, 40, 21, 18, 18, 15, 40 | 14, 12, 0, 0 | 62:Avatar:38.686:selected_best_candidate | board_advantage |
| Jogador 1 | 5-6 | 212–217 | 6 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.545 | 7, 18, 34, 15, 40, 15, 21 | 14, 62, 0, 0 | 62:Avatar:37.788:selected_best_candidate | board_advantage |
| Jogador 1 | 5-7 | 219–220 | 2 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.545 | 7, 18, 34, 62, 15, 40, 15, 21 | 14, 29, 0, 0 | 62:Avatar:38.098:selected_best_candidate | board_advantage |
| Jogador 1 | 6-1 | 222–226 | 5 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.400 | 7, 18, 34, 62, 15, 34, 40, 35, 15, 35, 21 | 14, 29, 32, 0, 0 | 62:Avatar:38.328:selected_best_candidate | board_advantage |
| Jogador 1 | 6-2 | 228–230 | 3 | Fera do Rift | KEEP | Fera do Rift | 53 | 0.950 | 0.400 | 7, 18, 62, 15, 34, 35, 15, 35, 21 | 14, 29, 32, 0, 0 | 53:Flora Fatalis:36.505:valid_but_not_selected, 53:Carrasco:39.088:selected_best_candidate | board_advantage |
| Jogador 1 | 6-3 | 232–233 | 2 | Fera do Rift | KEEP | Fera do Rift | 49 | 0.950 | 0.222 | 7, 18, 62, 15, 34, 34, 35, 15, 35, 21 | 14, 29, 0, 32 | 49:Primordial:39.307:valid_but_not_selected, 49:Adaptador:46.588:selected_best_candidate | board_advantage |
| Jogador 1 | 6-3 | 234–237 | 4 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.400 | 7, 18, 62, 15, 34, 34, 35, 15, 35, 21 | 14, 29, 0, 32, 49, 8 | 62:Avatar:39.659:selected_best_candidate, 49:Primordial:39.104:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 6-4 | 239–240 | 2 | Fera do Rift | KEEP | Fera do Rift | 51 | 0.950 | 0.400 | 7, 18, 62, 15, 34, 35, 15, 35, 21 | 14, 29, 0, 32, 49, 8 | 51:Florescer:41.025:valid_but_not_selected, 51:Lutador:42.075:selected_best_candidate | board_advantage |
| Jogador 1 | 6-5 | 242–243 | 2 | Fera do Rift | KEEP | Fera do Rift | 54 | 0.950 | 0.400 | 7, 18, 62, 15, 34, 35, 15, 35 | 14, 29, 0, 32, 49, 8, 33 | 54:Dama de Espinhos:36.731:valid_but_not_selected, 54:Invocador:42.331:selected_best_candidate | board_advantage |
| Jogador 1 | 6-5 | 244–245 | 2 | Fera do Rift | KEEP | Fera do Rift | 53 | 0.950 | 0.667 | 7, 18, 62, 15, 34, 35, 15, 35 | 14, 29, 0, 32, 49, 33, 54 | 53:Flora Fatalis:35.806:valid_but_not_selected, 53:Carrasco:37.326:selected_best_candidate | board_advantage |
| Jogador 1 | 6-5 | 246–248 | 3 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.400 | 7, 18, 62, 15, 34, 35, 15, 35 | 14, 29, 0, 22, 49, 53, 33, 54 | 62:Avatar:40.414:selected_best_candidate, 49:Primordial:37.925:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 6-6 | 250–250 | 1 | Fera do Rift | KEEP | Fera do Rift | 51 | 0.950 | 0.545 | 7, 18, 62, 15, 34, 35, 15, 35 | 14, 0, 29, 22, 49, 53, 33, 54 | 51:Florescer:38.820:valid_but_not_selected, 51:Lutador:38.970:selected_best_candidate | board_advantage |
| Jogador 1 | 6-7 | 252–258 | 7 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.222 | 7, 18, 62, 15, 34, 35, 15, 35 | 14, 0, 29, 33, 49, 14, 33, 37 | 62:Avatar:41.443:selected_best_candidate, 49:Primordial:37.184:not_best_scoring_candidate | board_advantage |
| Jogador 1 | 7-1 | 260–260 | 1 | Fera do Rift | KEEP | Fera do Rift | 62 | 0.950 | 0.222 | 7, 18, 62, 15, 34, 35, 15, 35 | 14, 0, 29, 33, 49, 14, 33 | 62:Avatar:41.800:selected_best_candidate, 49:Primordial:38.907:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 2 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 11 |  |  | insufficient_evidence |
| Jogador 2 | 1-2 | 12–15 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 11, 11 |  |  | insufficient_evidence |
| Jogador 2 | 1-3 | 22–31 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 11, 4 |  |  | insufficient_evidence |
| Jogador 2 | 1-4 | 34–40 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 11, 11, 11 | 13 |  | insufficient_evidence |
| Jogador 2 | 2-1 | 43–50 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11, 11, 11 | 0, 40 |  | insufficient_evidence |
| Jogador 2 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 0, 22, 40 |  | insufficient_evidence |
| Jogador 2 | 2-3 | 62–66 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 22, 8, 40, 36, 16 |  | insufficient_evidence |
| Jogador 2 | 2-4 | 72–80 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 4, 7, 11 | 12, 12, 10, 22, 40, 36, 30, 32 |  | insufficient_evidence |
| Jogador 2 | 2-5 | 82–82 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 11, 7, 4 | 12, 12, 10, 22, 40, 36, 30, 32 |  | insufficient_evidence |
| Jogador 2 | 2-5 | 83–83 | 1 | Feérico | ABANDON | — | -1 | 0.650 | 0.000 |  | 7, 12, 11, 7, 4, 12, 10, 22, 39, 40, 36, 30, 32 |  | board_deficit |
| Jogador 2 | 2-5 | 84–90 | 7 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 12, 11, 7, 4, 12, 39 | 38, 40, 27, 30, 32 |  | board_advantage |
| Jogador 2 | 2-6 | 92–99 | 8 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 12, 11, 7, 4, 12, 39 | 40, 27, 30 |  | board_advantage |
| Jogador 2 | 2-7 | 101–109 | 9 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 12, 11, 7, 4, 12, 39 | 32, 30 |  | board_advantage |
| Jogador 2 | 3-1 | 111–118 | 8 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 12, 11, 7, 4, 12, 39 | 32, 37, 30 |  | board_advantage |
| Jogador 2 | 3-2 | 120–120 | 1 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 7, 12, 11, 7, 4, 12, 39 | 37, 30 |  | board_advantage |
| Jogador 2 | 3-3 | 122–127 | 6 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.545 | 11, 7, 12, 7, 4, 39, 39 | 37, 28, 49, 30 | 49:Primordial:35.783:selected_best_candidate, 49:Adaptador:33.554:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 3-4 | 129–130 | 2 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.545 | 11, 7, 12, 7, 4, 39, 39 | 37, 28, 49, 23, 30 | 49:Primordial:35.916:selected_best_candidate, 49:Adaptador:35.413:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 3-5 | 132–138 | 7 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.545 | 7, 11, 12, 7, 4, 39, 39 | 37, 28, 49, 23, 25, 37, 30, 10 | 49:Primordial:36.314:selected_best_candidate, 49:Adaptador:35.045:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 3-6 | 140–140 | 1 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.545 | 7, 11, 12, 7, 4, 39, 39 | 37, 28, 49, 23, 25, 37, 30 | 49:Primordial:37.745:selected_best_candidate, 49:Adaptador:34.167:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 3-7 | 142–149 | 8 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.667 | 7, 11, 12, 7, 4, 11 | 37, 34, 28, 49, 32, 25, 37, 30 | 49:Primordial:33.089:valid_but_not_selected, 49:Adaptador:35.688:selected_best_candidate | board_advantage |
| Jogador 2 | 4-1 | 151–156 | 5 | Feérico | KEEP | Feérico | 45 | 0.950 | 0.545 | 7, 11, 12, 7, 4, 4, 11 | 37, 34, 28, 49, 32, 37, 30 | 45:Sabugueiro:43.019:selected_best_candidate | board_advantage |
| Jogador 2 | 4-1 | 155–155 | 1 | Feérico | ADAPT | Sabugueiro | 45 | 0.650 | 0.545 | 7, 11, 12, 7, 4, 4, 11 | 37, 34, 28, 49, 32, 25, 37, 30 | 45:Sabugueiro:43.447:selected_best_candidate | anchor_opportunity |
| Jogador 2 | 4-2 | 158–160 | 3 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.545 | 11, 12, 4, 4, 7, 11 | 37, 34, 28, 49, 45, 37, 30 | 49:Primordial:34.743:selected_best_candidate, 49:Adaptador:34.695:not_best_scoring_candidate | board_advantage |
| Jogador 2 | 4-3 | 162–168 | 7 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.667 | 11, 12, 4, 39, 4, 11 | 28, 34, 37, 18, 49, 45, 37, 30 | 49:Primordial:34.745:valid_but_not_selected, 49:Adaptador:36.973:selected_best_candidate | board_advantage |
| Jogador 2 | 4-4 | 170–170 | 1 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.857 | 11, 12, 4, 39, 4, 11 | 28, 34, 37, 18, 49, 21, 45, 37, 30 | 49:Primordial:34.973:valid_but_not_selected, 49:Adaptador:37.248:selected_best_candidate | board_advantage |
| Jogador 2 | 4-5 | 172–178 | 7 | Feérico | KEEP | Feérico | 49 | 0.950 | 0.545 | 11, 12, 4, 39, 39, 4, 11 | 28, 34, 37, 49, 8, 37, 30 | 49:Primordial:35.338:valid_but_not_selected, 49:Adaptador:36.093:selected_best_candidate | board_advantage |
| Jogador 3 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 3 | 1-1 | 2–4 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0 |  |  | insufficient_evidence |
| Jogador 3 | 1-2 | 12–16 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 0, 13 |  |  | insufficient_evidence |
| Jogador 3 | 1-3 | 22–31 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 8, 0 |  |  | insufficient_evidence |
| Jogador 3 | 1-4 | 34–38 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 0 | 18, 1 |  | insufficient_evidence |
| Jogador 3 | 2-1 | 43–50 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 8, 0 | 15, 18, 1, 23 |  | insufficient_evidence |
| Jogador 3 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8 | 15, 18, 1, 23, 15, 29 |  | insufficient_evidence |
| Jogador 3 | 2-3 | 62–65 | 4 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8 | 15, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-4 | 72–74 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8, 8 | 15, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-5 | 82–82 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13, 0, 8, 8 | 15, 18, 1, 23, 15, 29, 21, 7 |  | insufficient_evidence |
| Jogador 3 | 2-5 | 83–83 | 1 | Colosso | ABANDON | — | -1 | 0.650 | 0.000 | 0 | 15, 13, 18, 8, 13, 1, 23, 15, 29, 21, 7, 8 |  | board_deficit |
| Jogador 3 | 2-5 | 84–90 | 7 | Colosso | KEEP | Colosso | -1 | 0.000 | 0.000 | 13, 8, 0, 13, 7, 8 | 29, 18, 23, 1, 21 |  | board_advantage |
| Jogador 3 | 2-6 | 92–98 | 7 | Devastador | KEEP | Devastador | -1 | 0.000 | 0.000 | 13, 8, 0, 29, 1, 21, 8 | 18, 15, 26, 23, 7 |  | board_advantage |
| Jogador 3 | 2-7 | 101–107 | 7 | Devastador | KEEP | Devastador | -1 | 0.000 | 0.000 | 8, 29, 0, 13, 13, 29, 1, 21, 8 | 18, 15, 23, 7, 15 |  | board_advantage |
| Jogador 3 | 3-1 | 111–118 | 8 | Devastador | KEEP | Devastador | -1 | 0.000 | 0.000 | 1, 29, 0, 13, 29, 21 | 18, 23, 15, 7, 15 |  | board_advantage |
| Jogador 3 | 3-2 | 120–120 | 1 | Devastador | KEEP | Devastador | -1 | 0.000 | 0.000 | 1, 29, 0, 15, 29, 21, 15 | 18, 23, 7 |  | board_advantage |
| Jogador 3 | 3-3 | 122–127 | 6 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.400 | 52, 1, 29, 0, 15, 29, 21, 15 | 18, 23, 38, 17, 39, 7 | 52:Primordial:39.102:valid_but_not_selected, 52:Caçador:40.118:selected_best_candidate | board_advantage |
| Jogador 3 | 3-4 | 129–130 | 2 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 52, 29, 0, 15, 1, 29, 21, 15 | 38, 18, 23, 17, 39, 7, 30 | 52:Primordial:42.292:selected_best_candidate, 52:Caçador:40.482:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-5 | 132–135 | 4 | Devastador | KEEP | Devastador | 49 | 0.950 | 0.545 | 52, 29, 0, 15, 1, 29, 21, 15 | 38, 18, 23, 33, 7, 30 | 49:Primordial:37.991:valid_but_not_selected, 49:Adaptador:42.200:selected_best_candidate | board_advantage |
| Jogador 3 | 3-5 | 136–138 | 3 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.769 | 0, 52, 29, 15, 1, 29, 21, 15 | 18, 23, 38, 33, 49, 7, 30 | 52:Primordial:42.333:selected_best_candidate, 52:Caçador:41.294:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-6 | 140–140 | 1 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 0, 52, 29, 15, 1, 29, 21, 15 | 18, 23, 38, 33, 49, 7, 30 | 52:Primordial:41.804:selected_best_candidate, 52:Caçador:41.097:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 3-7 | 142–149 | 8 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 0, 52, 29, 15, 1, 29, 21, 15 | 18, 23, 38, 33, 49, 7 | 52:Primordial:41.712:selected_best_candidate, 52:Caçador:41.295:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-1 | 151–156 | 6 | Devastador | KEEP | Devastador | 53 | 0.950 | 0.667 | 0, 52, 29, 15, 1, 29, 21, 15 | 18, 23, 38, 33, 7, 33 | 53:Flora Fatalis:32.471:valid_but_not_selected, 53:Carrasco:34.003:selected_best_candidate | board_advantage |
| Jogador 3 | 4-2 | 158–160 | 3 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 0, 52, 29, 15, 1, 29, 21, 15 | 18, 23, 38, 33, 18, 7, 33 | 52:Primordial:41.944:selected_best_candidate, 52:Caçador:41.766:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-3 | 162–168 | 7 | Devastador | KEEP | Devastador | 51 | 0.950 | 0.545 | 0, 52, 29, 15, 1, 29, 21, 15 | 18, 23, 38, 33, 18, 33 | 51:Florescer:34.693:valid_but_not_selected, 51:Lutador:37.022:selected_best_candidate | board_advantage |
| Jogador 3 | 4-4 | 170–170 | 1 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.667 | 0, 52, 29, 15, 1, 29, 21, 15 | 18, 23, 38, 33, 18, 51, 33 | 52:Primordial:37.838:valid_but_not_selected, 52:Caçador:38.117:selected_best_candidate | board_advantage |
| Jogador 3 | 4-5 | 172–178 | 7 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 52, 29, 15, 25, 29, 0, 21, 21, 15 | 18, 18, 23, 38, 33, 35 | 52:Primordial:40.666:selected_best_candidate, 52:Caçador:39.678:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 4-6 | 180–180 | 1 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.769 | 0, 29, 15, 25, 29, 21, 21, 15 | 18, 18, 23, 38, 33, 52, 35 | 52:Primordial:40.277:valid_but_not_selected, 52:Caçador:41.248:selected_best_candidate | board_advantage |
| Jogador 3 | 4-7 | 182–187 | 6 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 21, 0, 29, 15, 25, 29, 15 | 23, 38, 39, 52, 18, 40, 35 | 52:Primordial:40.332:selected_best_candidate, 52:Caçador:38.195:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 5-1 | 189–190 | 2 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 21, 0, 15, 29, 25, 29, 15 | 23, 38, 22, 39, 52, 18, 40, 35 | 52:Primordial:40.365:selected_best_candidate, 52:Caçador:39.368:not_best_scoring_candidate | board_advantage |
| Jogador 3 | 5-2 | 192–198 | 7 | Devastador | KEEP | Devastador | 52 | 0.950 | 0.545 | 21, 0, 29, 15, 25, 29, 25 | 23, 38, 39, 52, 40, 35, 7 | 52:Primordial:41.430:selected_best_candidate, 52:Caçador:41.235:not_best_scoring_candidate | board_advantage |
| Jogador 4 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 4 | 1-1 | 2–4 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7 |  |  | insufficient_evidence |
| Jogador 4 | 1-2 | 12–16 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 1, 7, 13 |  |  | insufficient_evidence |
| Jogador 4 | 1-3 | 22–26 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13 | 3, 6 |  | insufficient_evidence |
| Jogador 4 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1 | 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-1 | 43–47 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1, 13 | 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 1, 13, 1, 13 | 3, 3, 6, 0 |  | insufficient_evidence |
| Jogador 4 | 2-3 | 62–70 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 13, 13, 33 | 3, 0, 3 |  | insufficient_evidence |
| Jogador 4 | 2-4 | 72–78 | 5 | — | INITIAL_SELECTION | Lunar | 43 | 0.950 | 1.000 | 7, 33, 13, 13, 43 | 3, 3 | 43:Lunar:38.942:selected_best_candidate | anchor_opportunity |
| Jogador 4 | 2-4 | 73–74 | 2 | — | INITIAL_SELECTION | Fumegante | 43 | 0.950 | 1.000 | 7, 33, 13, 13, 43 | 3, 18, 0, 3 | 43:Lunar:40.489:valid_but_not_selected, 43:Fumegante:40.740:selected_best_candidate | anchor_opportunity |
| Jogador 4 | 2-4 | 79–80 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 33, 13, 13 | 3, 12, 3 |  | insufficient_evidence |
| Jogador 4 | 2-5 | 82–82 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 33, 13, 13 | 3, 12, 12, 3 |  | insufficient_evidence |
| Jogador 4 | 2-5 | 83–83 | 1 | Florescer | ABANDON | — | -1 | 0.650 | 0.000 | 13 | 7, 33, 3, 13, 12, 3 |  | board_deficit |
| Jogador 4 | 2-5 | 84–90 | 7 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 29, 33, 3, 13, 13, 26, 3 |  |  | board_advantage |
| Jogador 4 | 2-6 | 92–93 | 2 | Florescer | KEEP | Florescer | 49 | 0.950 | 0.933 | 29, 33, 3, 3, 13, 13, 26 | 22 | 49:Primordial:13.083:selected_best_candidate, 49:Adaptador:13.083:not_best_scoring_candidate | board_advantage |
| Jogador 4 | 2-6 | 94–97 | 4 | Florescer | ADAPT | Adaptador | 49 | 0.650 | 0.857 | 13, 29, 33, 13 | 3, 3, 26, 22, 7 | 49:Primordial:13.117:valid_but_not_selected, 49:Adaptador:36.572:selected_best_candidate | transition_cost |
| Jogador 4 | 2-7 | 101–109 | 9 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 29, 33, 3, 13, 3, 26, 13 | 22, 25 |  | board_advantage |
| Jogador 4 | 3-1 | 111–118 | 8 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 29, 3, 3, 13, 33, 26, 13, 26 | 22, 32 |  | board_advantage |
| Jogador 4 | 3-2 | 120–120 | 1 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 29, 3, 3, 13, 33, 26, 13, 26 | 22 |  | board_advantage |
| Jogador 4 | 3-3 | 122–127 | 6 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 29, 3, 3, 33, 26, 13 | 40, 22, 20 |  | board_advantage |
| Jogador 4 | 3-4 | 129–130 | 2 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 29, 3, 3, 33, 26, 13, 26 | 22, 40, 20 |  | board_advantage |
| Jogador 4 | 3-5 | 132–136 | 5 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 3, 3, 33, 26, 13, 26, 29, 26 | 22, 40, 20, 20, 22 |  | board_advantage |
| Jogador 4 | 3-6 | 140–140 | 1 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 3, 3, 33, 26, 13, 26, 29, 26 | 22, 40, 20, 20, 22 |  | board_advantage |
| Jogador 4 | 3-7 | 142–149 | 8 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 22, 29, 3, 3, 33, 26, 36, 26 | 40, 20, 25, 20, 22 |  | board_advantage |
| Jogador 4 | 4-1 | 151–156 | 6 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 22, 29, 3, 3, 33, 36, 26 | 40, 20, 25, 20, 25, 22, 7 |  | board_advantage |
| Jogador 4 | 4-2 | 158–160 | 3 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 22, 29, 3, 3, 33, 40, 26, 36 | 20, 25, 20, 25, 22, 5, 7 |  | board_advantage |
| Jogador 4 | 4-3 | 162–168 | 7 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 22, 3, 3, 33, 40, 26, 29, 26 | 20, 20, 35, 27, 25, 22, 5 |  | board_advantage |
| Jogador 4 | 4-4 | 170–170 | 1 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 22, 3, 3, 33, 29, 26, 40, 26 | 20, 20, 35, 27, 25, 22, 5 |  | board_advantage |
| Jogador 4 | 4-5 | 172–178 | 4 | Florescer | ADAPT | Flora Fatalis | 53 | 0.650 | 0.545 | 22, 33, 29, 40, 33, 40, 53 | 20, 3, 26, 3, 20, 27, 22, 5, 26 | 53:Flora Fatalis:33.421:selected_best_candidate | anchor_opportunity |
| Jogador 4 | 4-5 | 175–177 | 3 | Florescer | KEEP | Florescer | -1 | 0.000 | 0.000 | 22, 3, 26, 3, 33, 29, 40, 33, 40, 26 | 20, 20, 27, 53, 22, 5 |  | board_advantage |
| Jogador 5 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 5 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 13 |  |  | insufficient_evidence |
| Jogador 5 | 1-2 | 12–17 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 13, 11 |  |  | insufficient_evidence |
| Jogador 5 | 1-3 | 22–23 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13 | 26 |  | insufficient_evidence |
| Jogador 5 | 1-4 | 34–36 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13 | 26, 7, 22 |  | insufficient_evidence |
| Jogador 5 | 2-1 | 43–48 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 7, 26, 28, 22 |  | insufficient_evidence |
| Jogador 5 | 2-2 | 52–54 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 7, 26, 28, 22, 7 |  | insufficient_evidence |
| Jogador 5 | 2-3 | 62–70 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 26, 1, 22 |  | insufficient_evidence |
| Jogador 5 | 2-4 | 72–80 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 16, 33 |  | insufficient_evidence |
| Jogador 5 | 2-5 | 82–82 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 28, 4, 16, 10, 33 |  | insufficient_evidence |
| Jogador 5 | 2-5 | 83–83 | 1 | Espinhos Negros | ABANDON | — | -1 | 0.650 | 0.000 | 13 | 28, 8, 11, 4, 16, 10, 37, 8, 33 |  | board_deficit |
| Jogador 5 | 2-5 | 84–90 | 7 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 33, 4, 37, 28 |  | board_advantage |
| Jogador 5 | 2-6 | 92–99 | 8 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 8, 11, 13, 8 | 33, 28, 4, 1, 37 |  | board_advantage |
| Jogador 5 | 2-7 | 101–109 | 9 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 8, 13, 11, 8 | 15, 4, 28, 7, 33, 37 |  | board_advantage |
| Jogador 5 | 3-1 | 111–118 | 8 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 13, 8, 11, 8 | 15, 4, 28, 33, 37, 39 |  | board_advantage |
| Jogador 5 | 3-2 | 120–120 | 1 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 13, 8, 11, 8 | 15, 4, 28, 33, 37, 39 |  | board_advantage |
| Jogador 5 | 3-3 | 122–127 | 6 | Espinhos Negros | ADAPT | Florescer | 41 | 0.650 | 0.545 | 13, 8, 11, 8 | 15, 4, 28, 39, 25, 37, 39, 37, 27 | 41:Florescer:43.892:selected_best_candidate, 41:Enfeitiçador:41.733:not_best_scoring_candidate | anchor_opportunity |
| Jogador 5 | 3-4 | 129–130 | 2 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 13, 8, 11, 25, 8, 27 | 15, 4, 28, 39, 37, 39, 37 |  | board_advantage |
| Jogador 5 | 3-5 | 132–138 | 7 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 13, 39, 11, 39, 27 | 15, 4, 28, 35, 37, 34, 37 |  | board_advantage |
| Jogador 5 | 3-6 | 140–140 | 1 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 13, 39, 11, 39, 27 | 15, 4, 28, 35, 37, 34, 37 |  | board_advantage |
| Jogador 5 | 3-7 | 142–145 | 4 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 39, 13, 39, 11, 27 | 15, 4, 28, 28, 35, 37, 34, 35, 37 |  | board_advantage |
| Jogador 5 | 4-1 | 151–156 | 6 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 4, 39, 13, 39, 11, 27 | 15, 28, 28, 35, 37, 34, 35, 37, 34 |  | board_advantage |
| Jogador 5 | 4-2 | 158–160 | 3 | Espinhos Negros | KEEP | Espinhos Negros | 53 | 0.950 | 0.545 | 4, 39, 13, 39, 11, 27 | 15, 28, 37, 35, 37, 34, 35, 34 | 53:Flora Fatalis:37.268:valid_but_not_selected, 53:Carrasco:38.279:selected_best_candidate | board_advantage |
| Jogador 5 | 4-3 | 162–168 | 7 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 4, 39, 13, 39, 11, 8, 8, 27, 27 | 15, 28, 35, 35 |  | board_advantage |
| Jogador 5 | 4-4 | 170–170 | 1 | Espinhos Negros | KEEP | Espinhos Negros | -1 | 0.000 | 0.000 | 4, 39, 13, 39, 11, 8, 8, 27, 27 | 15, 28, 35, 33, 35 |  | board_advantage |
| Jogador 5 | 4-5 | 172–177 | 6 | Vivaz | KEEP | Vivaz | -1 | 0.000 | 0.000 | 4, 13, 11, 39, 39 | 15, 28, 0, 35, 33, 8, 35, 3, 27, 27 |  | board_advantage |
| Jogador 5 | 4-6 | 180–180 | 1 | Vivaz | KEEP | Vivaz | 44 | 0.950 | 0.933 | 4, 13, 11, 39, 39 | 15, 28, 0, 35, 33, 8, 35, 3, 27, 27 | 44:Fera do Rift:41.319:selected_best_candidate, 44:Vanguarda:36.283:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 4-7 | 182–185 | 4 | Vivaz | KEEP | Vivaz | 43 | 0.950 | 0.667 | 4, 13, 11, 39, 39 | 15, 28, 0, 8, 33, 8, 43, 3, 27, 27 | 43:Lunar:39.218:selected_best_candidate | board_advantage |
| Jogador 5 | 4-7 | 186–187 | 2 | Vivaz | KEEP | Vivaz | 50 | 0.950 | 0.400 | 4, 13, 11, 39, 39, 11 | 15, 28, 0, 8, 33, 8, 43, 3, 27, 27 | 50:Fera do Rift:38.317:valid_but_not_selected, 50:Devastador:38.500:selected_best_candidate | board_advantage |
| Jogador 5 | 5-1 | 189–190 | 2 | Vivaz | KEEP | Vivaz | 43 | 0.950 | 0.545 | 4, 13, 11, 39, 39, 4, 11 | 15, 28, 0, 8, 33, 43, 3, 27, 27 | 43:Lunar:37.405:valid_but_not_selected, 43:Fumegante:39.145:selected_best_candidate | board_advantage |
| Jogador 5 | 5-2 | 192–198 | 7 | Vivaz | KEEP | Vivaz | 43 | 0.950 | 0.667 | 4, 13, 11, 39, 39, 4, 24, 11 | 15, 28, 34, 8, 33, 43, 27, 27 | 43:Lunar:37.238:valid_but_not_selected, 43:Fumegante:38.697:selected_best_candidate | board_advantage |
| Jogador 5 | 5-3 | 200–200 | 1 | Vivaz | KEEP | Vivaz | 55 | 0.950 | 0.769 | 4, 13, 11, 39, 39, 4, 24, 11 | 15, 28, 8, 33, 43, 27, 27 | 55:Comunhão:34.135:valid_but_not_selected, 55:Lunar:36.663:selected_best_candidate | board_advantage |
| Jogador 5 | 5-4 | 202–208 | 7 | Vivaz | KEEP | Vivaz | 55 | 0.950 | 0.222 | 4, 13, 11, 39, 39, 4, 24, 11 | 15, 28, 55, 8, 33, 27, 27 | 55:Comunhão:33.911:selected_best_candidate, 55:Lunar:33.429:not_best_scoring_candidate | board_advantage |
| Jogador 5 | 5-5 | 210–210 | 1 | Vivaz | KEEP | Vivaz | 42 | 0.950 | 0.667 | 4, 13, 11, 39, 39, 4, 24, 11 | 15, 28, 55, 8, 33, 35, 27, 27 | 42:Inferno:35.951:valid_but_not_selected, 42:Colosso:37.745:selected_best_candidate | board_advantage |
| Jogador 6 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 6 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 2 |  |  | insufficient_evidence |
| Jogador 6 | 1-2 | 12–14 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 2, 12, 13 |  |  | insufficient_evidence |
| Jogador 6 | 1-3 | 22–31 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 2, 12, 13 | 4 |  | insufficient_evidence |
| Jogador 6 | 1-4 | 34–35 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 4 |  | insufficient_evidence |
| Jogador 6 | 2-1 | 43–47 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 4, 7 |  | insufficient_evidence |
| Jogador 6 | 2-2 | 52–56 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 7, 19 |  | insufficient_evidence |
| Jogador 6 | 2-3 | 62–67 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 23, 19, 15, 18 |  | insufficient_evidence |
| Jogador 6 | 2-4 | 72–80 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 31, 7, 15, 7 |  | insufficient_evidence |
| Jogador 6 | 2-5 | 82–82 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 13 | 39, 31, 7, 7 |  | insufficient_evidence |
| Jogador 6 | 2-5 | 83–83 | 1 | Feérico | ABANDON | — | -1 | 0.650 | 0.000 | 2 | 12, 12, 2, 39, 13, 13, 31, 7, 7 |  | board_deficit |
| Jogador 6 | 2-5 | 84–90 | 7 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 13, 12, 12, 2, 2, 39, 13, 7, 7 |  |  | board_advantage |
| Jogador 6 | 2-6 | 92–99 | 8 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 13, 12, 12, 7, 2, 2, 7 |  |  | board_advantage |
| Jogador 6 | 2-7 | 101–109 | 9 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 13, 12, 12, 7, 2, 2, 7 | 40, 10 |  | board_advantage |
| Jogador 6 | 3-1 | 111–116 | 6 | Feérico | ADAPT | Florescer | 41 | 0.650 | 0.545 | 13, 12, 12, 2, 2, 41 | 7, 30, 10, 7 | 41:Florescer:41.711:selected_best_candidate, 41:Enfeitiçador:40.471:not_best_scoring_candidate | anchor_opportunity |
| Jogador 6 | 3-1 | 117–118 | 2 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 13, 12, 12, 2, 2, 7, 7 | 30, 10 |  | board_advantage |
| Jogador 6 | 3-2 | 120–120 | 1 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 7, 13, 7 | 30, 10 |  | board_advantage |
| Jogador 6 | 3-3 | 122–127 | 6 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 7, 2, 2, 12, 39, 13 | 30, 10, 37, 18 |  | board_advantage |
| Jogador 6 | 3-4 | 129–130 | 2 | Feérico | KEEP | Feérico | 45 | 0.950 | 0.545 | 12, 7, 2, 2, 12, 39, 13 | 30, 10, 37, 30 | 45:Sabugueiro:40.395:selected_best_candidate, 45:Carrasco:37.993:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-5 | 132–138 | 7 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 7, 39, 13 | 30, 30, 10, 37, 35, 35, 37 |  | board_advantage |
| Jogador 6 | 3-6 | 140–140 | 1 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 12, 2, 2, 7, 39, 13 | 30, 30, 10, 37, 29, 35, 35, 37 |  | board_advantage |
| Jogador 6 | 3-7 | 142–143 | 2 | Feérico | KEEP | Feérico | 59 | 0.950 | 0.545 | 12, 12, 2, 2, 7, 39, 13 | 30, 30, 37, 29, 35, 35, 37, 29 | 59:Sabugueiro:43.285:selected_best_candidate, 59:Vivaz:42.900:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 3-7 | 144–148 | 5 | Feérico | KEEP | Feérico | 54 | 0.950 | 0.400 | 12, 2, 2, 7, 12, 39, 13 | 30, 30, 54, 37, 29, 35, 35, 37, 29 | 54:Dama de Espinhos:36.065:valid_but_not_selected, 54:Invocador:41.218:selected_best_candidate | board_advantage |
| Jogador 6 | 4-1 | 151–153 | 3 | Feérico | KEEP | Feérico | 54 | 0.950 | 0.400 | 12, 2, 2, 7, 12, 39, 13 | 30, 30, 54, 37, 29, 35, 35, 37, 29 | 54:Dama de Espinhos:36.061:valid_but_not_selected, 54:Invocador:41.214:selected_best_candidate | board_advantage |
| Jogador 6 | 4-1 | 154–156 | 3 | Feérico | KEEP | Feérico | -1 | 0.000 | 0.000 | 12, 2, 2, 7, 12, 39, 13 | 30, 30, 37, 31, 29, 35, 35, 29 |  | board_advantage |
| Jogador 6 | 4-2 | 158–160 | 3 | Feérico | KEEP | Feérico | 53 | 0.950 | 0.400 | 12, 2, 2, 7, 12, 39, 13 | 30, 30, 33, 31, 29, 35, 35, 9, 29 | 53:Flora Fatalis:36.040:valid_but_not_selected, 53:Carrasco:38.323:selected_best_candidate | board_advantage |
| Jogador 6 | 4-3 | 162–168 | 7 | Feérico | KEEP | Feérico | 42 | 0.950 | 0.400 | 12, 2, 2, 7, 12, 39, 13, 7 | 30, 30, 33, 29, 35, 35, 42, 29 | 42:Inferno:38.690:valid_but_not_selected, 42:Colosso:41.990:selected_best_candidate | board_advantage |
| Jogador 6 | 4-4 | 170–170 | 1 | Feérico | KEEP | Feérico | 42 | 0.950 | 0.400 | 12, 2, 2, 7, 12, 39, 13, 7 | 30, 30, 29, 35, 35, 42, 29 | 42:Inferno:41.015:valid_but_not_selected, 42:Colosso:43.027:selected_best_candidate | board_advantage |
| Jogador 6 | 4-5 | 172–178 | 7 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.000 | 12, 7, 12, 39, 13, 46, 7, 2 | 30, 29, 30, 35, 35, 29 | 46:Feérico:45.993:selected_best_candidate, 46:Defendente:40.743:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-6 | 180–180 | 1 | Feérico | KEEP | Feérico | 46 | 0.950 | 0.000 | 12, 39, 7, 12, 13, 46, 7, 2 | 30, 29, 30, 35, 35, 29 | 46:Feérico:45.951:selected_best_candidate, 46:Defendente:40.701:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 4-7 | 182–187 | 6 | Feérico | KEEP | Feérico | 43 | 0.950 | 0.222 | 29, 12, 39, 13, 7, 12, 39, 46, 7, 2 | 43, 35, 35, 30 | 43:Lunar:48.569:selected_best_candidate, 43:Fumegante:48.254:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 5-1 | 189–190 | 2 | Feérico | KEEP | Feérico | 43 | 0.950 | 0.222 | 29, 12, 39, 13, 39, 7, 12, 46, 7, 2 | 43, 35, 35, 30 | 43:Lunar:48.605:selected_best_candidate, 43:Fumegante:48.440:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 5-2 | 192–198 | 7 | Feérico | KEEP | Feérico | 43 | 0.950 | 0.400 | 13, 39, 29, 39, 7, 12, 46, 7, 2 | 43, 35, 30 | 43:Lunar:49.435:selected_best_candidate, 43:Fumegante:49.094:not_best_scoring_candidate | board_advantage |
| Jogador 6 | 5-3 | 200–200 | 1 | Feérico | KEEP | Feérico | 54 | 0.950 | 0.400 | 13, 39, 29, 39, 12, 7, 46, 7, 2 | 43, 35, 30 | 54:Dama de Espinhos:39.442:valid_but_not_selected, 54:Invocador:44.598:selected_best_candidate | board_advantage |
| Jogador 7 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 7 | 1-1 | 2–2 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 0 |  |  | insufficient_evidence |
| Jogador 7 | 1-2 | 12–18 | 7 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 10 |  |  | insufficient_evidence |
| Jogador 7 | 1-3 | 22–27 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7, 0, 10, 0 | 13 |  | insufficient_evidence |
| Jogador 7 | 1-4 | 34–38 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 0, 7, 0, 10 | 13, 1 |  | insufficient_evidence |
| Jogador 7 | 2-1 | 43–47 | 5 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 0, 7, 0, 10 | 13, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 10, 7, 31, 10 | 13, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-3 | 62–69 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 31, 7, 28 | 13, 1, 1, 13, 23 |  | insufficient_evidence |
| Jogador 7 | 2-4 | 72–74 | 3 | — | INITIAL_SELECTION | Fera do Rift | 44 | 0.950 | 1.000 | 31, 7, 28, 44 | 13, 33, 1, 1, 13, 23 | 44:Fera do Rift:38.543:selected_best_candidate, 44:Vanguarda:32.311:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-5 | 82–82 | 1 | — | INITIAL_SELECTION | Fera do Rift | 44 | 0.950 | 1.000 | 31, 7, 28, 44 | 33, 13, 1, 1, 13, 23 | 44:Fera do Rift:42.639:selected_best_candidate, 44:Vanguarda:38.432:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-5 | 83–83 | 1 | Colosso | PIVOT | Fera do Rift | 44 | 0.950 | 0.400 | 7, 35, 44 | 31, 28, 33, 13, 1, 1, 13, 23 | 44:Fera do Rift:44.416:selected_best_candidate, 44:Vanguarda:40.298:not_best_scoring_candidate | board_deficit |
| Jogador 7 | 2-5 | 84–86 | 3 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 31, 28, 7, 35, 44 | 33, 13, 1, 1, 13, 23, 12 | 44:Fera do Rift:44.791:selected_best_candidate, 44:Vanguarda:40.902:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-6 | 92–99 | 8 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 31, 28, 7, 35, 44, 7 | 13, 33, 1, 13, 12, 33 | 44:Fera do Rift:46.127:selected_best_candidate, 44:Vanguarda:42.370:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-7 | 101–102 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 31, 28, 7, 35, 44, 7 | 13, 33, 37, 13, 12, 33 | 44:Fera do Rift:45.372:selected_best_candidate, 44:Vanguarda:41.534:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 2-7 | 103–106 | 4 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 31, 28, 7, 13, 13, 7 | 33, 35, 37, 12, 33 | 44:Fera do Rift:44.741:selected_best_candidate, 44:Vanguarda:40.993:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 3-1 | 111–116 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 7, 28, 35, 15, 7 | 33, 13, 37, 13, 12, 33 | 44:Fera do Rift:47.924:selected_best_candidate, 44:Vanguarda:44.172:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-2 | 120–120 | 1 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 7, 28, 35, 15, 7 | 33, 13, 37, 13, 12, 33 | 44:Fera do Rift:49.078:selected_best_candidate, 44:Vanguarda:45.325:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-3 | 122–127 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 7, 28, 15, 35, 7 | 33, 37, 40, 13, 12, 33 | 44:Fera do Rift:49.740:selected_best_candidate, 44:Vanguarda:45.987:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-4 | 129–130 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 28, 15, 35, 7 | 33, 37, 40, 13, 12, 33 | 44:Fera do Rift:50.111:selected_best_candidate, 44:Vanguarda:46.358:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-5 | 132–138 | 7 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.000 | 44, 31, 28, 35, 15, 33 | 12, 20, 37, 40, 13, 12, 30 | 44:Fera do Rift:47.929:selected_best_candidate, 44:Vanguarda:44.133:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-6 | 140–140 | 1 | Colosso | KEEP | Colosso | 43 | 0.950 | 0.222 | 44, 31, 28, 15, 40, 33, 13 | 35, 12, 20, 37, 12, 30 | 43:Lunar:40.736:valid_but_not_selected, 43:Fumegante:45.595:selected_best_candidate | board_advantage |
| Jogador 7 | 3-7 | 142–149 | 7 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 44, 31, 35, 28, 15, 31, 2 | 12, 20, 40, 12, 30, 30 | 44:Fera do Rift:43.691:selected_best_candidate, 44:Vanguarda:38.204:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 3-7 | 146–146 | 1 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 31, 28, 15, 31, 40 | 35, 12, 20, 37, 12, 30, 30 | 44:Fera do Rift:15.731:valid_but_not_selected, 44:Vanguarda:38.064:selected_best_candidate | board_advantage |
| Jogador 7 | 4-1 | 151–156 | 6 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.933 | 44, 31, 35, 28, 15, 31, 22, 40 | 12, 2, 14, 12, 30, 30 | 44:Fera do Rift:19.822:selected_best_candidate, 44:Vanguarda:19.822:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-2 | 158–160 | 3 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.222 | 44, 31, 35, 28, 15, 31, 40, 22 | 12, 14, 12, 30, 30 | 44:Fera do Rift:41.026:selected_best_candidate, 44:Vanguarda:38.131:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 4-3 | 162–163 | 2 | Colosso | KEEP | Colosso | 53 | 0.950 | 0.769 | 44, 31, 35, 28, 31, 15, 15, 40, 22 | 12, 14, 12, 30, 30 | 53:Flora Fatalis:30.258:valid_but_not_selected, 53:Carrasco:30.610:selected_best_candidate | board_advantage |
| Jogador 7 | 4-3 | 164–167 | 4 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 31, 31, 28, 15, 35, 15, 40, 22 | 12, 53, 20, 14, 12, 30, 30 | 44:Fera do Rift:20.180:valid_but_not_selected, 44:Vanguarda:39.023:selected_best_candidate | board_advantage |
| Jogador 7 | 4-4 | 170–170 | 1 | Colosso | KEEP | Colosso | 44 | 0.950 | 0.400 | 44, 31, 31, 28, 15, 35, 15, 40, 22 | 12, 53, 20, 14, 12, 30, 30 | 44:Fera do Rift:22.842:valid_but_not_selected, 44:Vanguarda:39.024:selected_best_candidate | board_advantage |
| Jogador 7 | 4-5 | 172–178 | 6 | Colosso | KEEP | Colosso | 45 | 0.950 | 0.667 | 44, 31, 28, 31, 35, 15, 15, 40 | 12, 53, 29, 20, 12, 30, 30 | 45:Carrasco:37.212:selected_best_candidate | board_advantage |
| Jogador 7 | 4-5 | 177–177 | 1 | Colosso | ADAPT | Sabugueiro | 45 | 0.650 | 0.769 | 44, 31, 31, 28, 12, 35, 15, 20, 12 | 15, 53, 29, 40, 30, 30 | 45:Sabugueiro:40.781:selected_best_candidate, 45:Carrasco:37.326:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 4-6 | 180–180 | 1 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 44, 31, 28, 35, 31, 15, 15 | 12, 53, 29, 40, 20, 12, 30, 30 | 44:Fera do Rift:45.189:selected_best_candidate, 44:Vanguarda:42.335:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 4-7 | 182–187 | 6 | Colosso | KEEP | Colosso | 51 | 0.950 | 0.667 | 44, 20, 53, 28, 35, 31, 15, 40, 31 | 12, 29, 12, 30, 30 | 51:Florescer:30.664:valid_but_not_selected, 51:Lutador:33.674:selected_best_candidate | board_advantage |
| Jogador 7 | 5-1 | 189–190 | 2 | Colosso | KEEP | Colosso | 56 | 0.950 | 0.769 | 44, 20, 53, 28, 35, 31, 15, 40, 31 | 12, 18, 29, 12, 30, 30 | 56:Florescer:33.783:valid_but_not_selected, 56:Caçador:36.225:selected_best_candidate | board_advantage |
| Jogador 7 | 5-2 | 192–198 | 7 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.545 | 44, 53, 31, 20, 35, 28, 15, 18, 18 | 12, 29, 40, 12, 30, 30 | 44:Fera do Rift:42.643:selected_best_candidate, 44:Vanguarda:39.765:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-3 | 200–200 | 1 | Colosso | ADAPT | Vanguarda | 44 | 0.650 | 0.400 | 44, 53, 31, 20, 35, 28, 15, 29 | 12, 18, 40, 18, 39, 12, 30, 30 | 44:Fera do Rift:19.633:valid_but_not_selected, 44:Vanguarda:40.980:selected_best_candidate | anchor_opportunity |
| Jogador 7 | 5-4 | 202–208 | 7 | Colosso | ADAPT | Fera do Rift | 50 | 0.650 | 0.545 | 44, 53, 31, 20, 35, 12, 28, 15, 18, 18 | 33, 40, 39, 12, 30, 30 | 50:Fera do Rift:44.418:selected_best_candidate, 50:Devastador:35.410:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-5 | 210–210 | 1 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.545 | 44, 53, 31, 20, 35, 12, 28, 15, 18, 18 | 33, 40, 12, 30, 30 | 44:Fera do Rift:42.743:selected_best_candidate, 44:Vanguarda:42.452:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-6 | 212–217 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.545 | 44, 53, 31, 20, 35, 12, 28, 15, 18, 18 | 33, 40, 12, 30, 30 | 44:Fera do Rift:42.661:selected_best_candidate, 44:Vanguarda:42.452:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 5-7 | 219–220 | 2 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.667 | 44, 53, 31, 20, 35, 12, 28, 15, 18, 18 | 33, 40, 12, 30, 30 | 44:Fera do Rift:44.987:selected_best_candidate, 44:Vanguarda:42.452:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 6-1 | 222–225 | 4 | Colosso | ADAPT | Sabugueiro | 45 | 0.650 | 0.769 | 44, 53, 31, 20, 35, 12, 28, 12 | 15, 18, 40, 35, 30, 30 | 45:Sabugueiro:43.487:selected_best_candidate, 45:Carrasco:41.179:not_best_scoring_candidate | transition_cost |
| Jogador 7 | 6-1 | 226–226 | 1 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.545 | 44, 53, 31, 20, 35, 12, 28, 15, 18, 35 | 45, 40, 12, 30, 30 | 44:Fera do Rift:42.097:selected_best_candidate, 44:Vanguarda:40.296:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 6-2 | 228–230 | 3 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 44, 53, 31, 20, 35, 12, 28, 15, 15, 35 | 45, 40, 39, 12, 30, 30 | 44:Fera do Rift:41.703:selected_best_candidate, 44:Vanguarda:41.030:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 6-3 | 232–237 | 6 | Colosso | ADAPT | Fera do Rift | 44 | 0.650 | 0.400 | 44, 53, 31, 20, 45, 12, 28, 15, 15, 35 | 37, 40, 30, 12, 23 | 44:Fera do Rift:42.748:selected_best_candidate, 44:Vanguarda:41.681:not_best_scoring_candidate | anchor_opportunity |
| Jogador 7 | 6-4 | 239–240 | 2 | Sabugueiro | KEEP | Sabugueiro | 44 | 0.950 | 0.545 | 44, 53, 31, 20, 45, 12, 28, 12 | 15, 37, 15, 40, 30, 23, 1 | 44:Fera do Rift:39.866:valid_but_not_selected, 44:Vanguarda:41.716:selected_best_candidate | board_advantage |
| Jogador 7 | 6-5 | 242–248 | 7 | Sabugueiro | KEEP | Sabugueiro | 44 | 0.950 | 0.667 | 44, 53, 31, 20, 45, 12, 28, 12 | 15, 37, 15, 40, 33, 32, 23, 2 | 44:Fera do Rift:38.687:valid_but_not_selected, 44:Vanguarda:39.756:selected_best_candidate | board_advantage |
| Jogador 7 | 6-6 | 250–250 | 1 | Sabugueiro | KEEP | Sabugueiro | 41 | 0.950 | 0.545 | 44, 53, 31, 20, 45, 12, 28, 12 | 15, 37, 15, 40, 33, 32, 23 | 41:Florescer:40.119:selected_best_candidate, 41:Enfeitiçador:39.650:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 6-7 | 252–258 | 7 | Sabugueiro | KEEP | Sabugueiro | 44 | 0.950 | 0.857 | 44, 53, 31, 20, 45, 12, 28, 12 | 15, 29, 15, 26, 33, 32, 32, 27 | 44:Fera do Rift:18.755:selected_best_candidate, 44:Vanguarda:18.755:not_best_scoring_candidate | board_advantage |
| Jogador 7 | 7-1 | 260–260 | 1 | Sabugueiro | KEEP | Sabugueiro | 46 | 0.950 | 0.400 | 44, 53, 31, 20, 45, 12, 28, 12 | 15, 29, 15, 33, 32, 32, 27 | 46:Feérico:39.316:valid_but_not_selected, 46:Defendente:40.617:selected_best_candidate | board_advantage |
| Jogador 8 | 1-1 | 1–1 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 |  |  |  | — |
| Jogador 8 | 1-1 | 2–3 | 2 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 7 |  |  | insufficient_evidence |
| Jogador 8 | 1-2 | 12–17 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 7, 11 |  |  | insufficient_evidence |
| Jogador 8 | 1-3 | 22–24 | 3 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7, 3 | 13 |  | insufficient_evidence |
| Jogador 8 | 1-4 | 34–39 | 6 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7, 3 | 12, 12 |  | insufficient_evidence |
| Jogador 8 | 2-1 | 43–50 | 8 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7 | 12, 24, 5 |  | insufficient_evidence |
| Jogador 8 | 2-2 | 52–60 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7 | 24, 2, 25, 4, 0 |  | insufficient_evidence |
| Jogador 8 | 2-3 | 62–70 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 3, 11, 7, 11, 3 | 24 |  | insufficient_evidence |
| Jogador 8 | 2-4 | 72–80 | 9 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 11, 11, 7, 3, 3 | 36, 24, 32, 4 |  | insufficient_evidence |
| Jogador 8 | 2-5 | 82–82 | 1 | — | INSUFFICIENT_EVIDENCE | — | -1 | 0.000 | 0.000 | 11, 11, 7, 3 | 36, 24, 32, 4 |  | insufficient_evidence |
| Jogador 8 | 2-5 | 83–83 | 1 | Enfeitiçador | ABANDON | — | -1 | 0.650 | 0.000 | 7 | 11, 36, 11, 24, 32, 4, 3, 3 |  | board_deficit |
| Jogador 8 | 2-5 | 84–90 | 7 | Enfeitiçador | KEEP | Enfeitiçador | -1 | 0.000 | 0.000 | 11, 11, 7, 3, 3 | 36, 24, 37 |  | board_advantage |
| Jogador 8 | 2-6 | 92–99 | 8 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 53, 11, 7, 11, 3, 3 | 36, 24, 29, 15, 37 | 53:Flora Fatalis:20.039:selected_best_candidate, 53:Carrasco:20.039:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 2-7 | 101–107 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 53, 11, 7, 11, 3, 3 | 29, 36, 24, 15, 37, 39, 0, 40 | 53:Flora Fatalis:20.422:selected_best_candidate, 53:Carrasco:20.422:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-1 | 111–111 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 46 | 0.950 | 0.769 | 53, 11, 7, 11, 3, 3 | 29, 36, 24, 15, 37, 39, 0, 40 | 46:Feérico:36.964:selected_best_candidate | board_advantage |
| Jogador 8 | 3-1 | 112–118 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 53, 11, 11, 3, 3 | 36, 24, 29, 15, 37, 39, 21, 40, 46 | 53:Flora Fatalis:20.054:selected_best_candidate, 53:Carrasco:20.054:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-2 | 120–120 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 50 | 0.950 | 1.000 | 7, 11, 53, 11, 3, 3 | 36, 24, 29, 15, 37, 39, 21, 40, 46 | 50:Fera do Rift:36.949:selected_best_candidate, 50:Devastador:33.989:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-3 | 122–127 | 6 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 11, 53, 20, 11, 3, 3 | 36, 24, 29, 37, 39, 32, 0, 46 | 53:Flora Fatalis:20.324:selected_best_candidate, 53:Carrasco:20.324:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-4 | 129–130 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 11, 53, 20, 11, 3 | 36, 24, 29, 37, 39, 32, 46 | 53:Flora Fatalis:20.091:selected_best_candidate, 53:Carrasco:20.091:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-5 | 132–138 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 11, 53, 28, 11 | 36, 24, 29, 4, 37, 39, 40, 32, 46 | 53:Flora Fatalis:20.125:selected_best_candidate, 53:Carrasco:20.125:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 3-6 | 140–140 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 47 | 0.950 | 0.769 | 7, 11, 53, 28, 11 | 36, 24, 29, 37, 39, 40, 32, 46 | 47:Monólito:31.409:selected_best_candidate | board_advantage |
| Jogador 8 | 3-7 | 142–149 | 8 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 53, 28, 28, 46 | 36, 24, 29, 27, 37, 39, 40, 32, 38 | 53:Flora Fatalis:19.639:selected_best_candidate, 53:Carrasco:19.639:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-1 | 151–156 | 6 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 53, 28, 24, 11, 28, 46 | 36, 29, 27, 37, 39, 40, 32, 25 | 53:Flora Fatalis:25.031:selected_best_candidate, 53:Carrasco:25.031:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-2 | 158–160 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 52 | 0.950 | 0.769 | 7, 53, 28, 24, 11, 28, 7, 46 | 36, 29, 27, 37, 39, 32 | 52:Primordial:38.483:selected_best_candidate, 52:Caçador:37.373:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-3 | 162–168 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 53, 28, 24, 11, 28, 20, 7, 46 | 36, 29, 29, 37, 24, 32 | 53:Flora Fatalis:19.704:selected_best_candidate, 53:Carrasco:19.704:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-4 | 170–170 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 7, 53, 28, 24, 11, 28, 20, 7, 46 | 36, 29, 37, 24, 32 | 53:Flora Fatalis:24.599:selected_best_candidate, 53:Carrasco:24.599:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-5 | 172–178 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 20, 28, 53, 11, 24, 20, 28, 7, 46 | 36, 39, 29, 37, 32 | 53:Flora Fatalis:20.376:selected_best_candidate, 53:Carrasco:20.376:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-6 | 180–180 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 20, 53, 28, 11, 24, 20, 28, 7, 46 | 36, 39, 29, 37, 32 | 53:Flora Fatalis:24.742:selected_best_candidate, 53:Carrasco:24.742:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 4-7 | 182–187 | 6 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 28, 11, 24, 28, 20, 7, 46 | 39, 29, 31, 17, 37, 32 | 53:Flora Fatalis:20.965:selected_best_candidate, 53:Carrasco:20.965:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 5-1 | 189–190 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 49 | 0.950 | 0.769 | 36, 53, 28, 11, 24, 28, 20, 7, 46 | 39, 29, 31, 17, 37, 32, 5 | 49:Primordial:17.222:valid_but_not_selected, 49:Adaptador:36.813:selected_best_candidate | board_advantage |
| Jogador 8 | 5-2 | 192–198 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 28, 11, 24, 28, 46 | 39, 29, 31, 17, 37, 31, 29, 32, 5 | 53:Flora Fatalis:20.817:selected_best_candidate, 53:Carrasco:20.817:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 5-3 | 200–200 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 11, 24, 28, 28, 46 | 39, 29, 31, 17, 37, 31, 29, 32, 5 | 53:Flora Fatalis:24.901:selected_best_candidate, 53:Carrasco:24.901:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 5-4 | 202–208 | 7 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 11, 24, 30, 36, 46 | 39, 29, 31, 37, 31, 29, 32 | 53:Flora Fatalis:25.669:selected_best_candidate, 53:Carrasco:25.669:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 5-5 | 210–210 | 1 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 11, 24, 30, 36, 46 | 39, 29, 31, 37, 31, 29, 32 | 53:Flora Fatalis:35.089:selected_best_candidate, 53:Carrasco:35.089:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 5-6 | 212–217 | 6 | Enfeitiçador | ADAPT | Lunar | 43 | 0.650 | 0.667 | 36, 53, 29, 24, 29, 46 | 39, 11, 31, 11, 37, 30, 37, 31, 32, 24 | 43:Lunar:42.235:selected_best_candidate, 43:Fumegante:38.728:not_best_scoring_candidate | transition_cost |
| Jogador 8 | 5-7 | 219–220 | 2 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 11, 24, 11, 30, 46 | 39, 29, 31, 37, 37, 31, 29, 32, 39 | 53:Flora Fatalis:26.393:selected_best_candidate, 53:Carrasco:26.393:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 6-1 | 222–226 | 5 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 11, 24, 11, 30, 3, 46 | 39, 29, 31, 37, 37, 25, 32, 39 | 53:Flora Fatalis:26.468:selected_best_candidate, 53:Carrasco:26.468:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 6-2 | 228–230 | 3 | Enfeitiçador | KEEP | Enfeitiçador | 53 | 0.950 | 0.667 | 36, 53, 11, 24, 11, 30, 3, 46 | 39, 29, 31, 37, 37, 32, 39 | 53:Flora Fatalis:26.393:selected_best_candidate, 53:Carrasco:26.393:not_best_scoring_candidate | board_advantage |
| Jogador 8 | 6-3 | 232–237 | 6 | Enfeitiçador | ADAPT | Florescer | 51 | 0.650 | 0.545 | 36, 53, 24, 3, 46 | 39, 29, 11, 31, 11, 37, 30, 37, 30, 32 | 51:Florescer:42.574:selected_best_candidate, 51:Lutador:37.430:not_best_scoring_candidate | anchor_opportunity |

### Frequência das decisões

- ABANDON: 7
- ADAPT: 29
- INITIAL_SELECTION: 4
- INSUFFICIENT_EVIDENCE: 78
- KEEP: 172
- PIVOT: 1

Revisões estratégicas únicas: **291**.
Snapshots estratégicos observados: **1221** (inclui repetições por ação).
Candidatos de âncora avaliados: **282**.


### Auditoria de KEEP — continuidade fundamentada versus persistência

- KEEP auditados: **172**
- Confiança da direção atual: positive=172
- Motivos/path: current_direction_viable_without_alternative=59; alternative_below_minimum_adapt_advantage=110; best_anchor_matches_current_direction=3

| Jogador | Round | Step | Direção | Score atual | Conf. direção atual | Conf. alternativa | Score alternativa | Vantagem | Viável | Motivo | Lock | Candidato pendente | Streak | Limite PIVOT |
|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|
| Jogador 1 | 2-5 | 90 | Inferno | 41.894 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.379 |
| Jogador 1 | 2-6 | 98 | Inferno | 42.531 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.506 |
| Jogador 1 | 2-7 | 109 | Inferno | 40.160 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.032 |
| Jogador 1 | 3-1 | 115 | Inferno | 39.916 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.983 |
| Jogador 1 | 3-2 | 120 | Inferno | 39.941 | 0.950 | 0.950 | 36.404 | -3.537 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.988 |
| Jogador 1 | 3-3 | 127 | Inferno | 39.945 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.989 |
| Jogador 1 | 3-4 | 130 | Inferno | 39.942 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.988 |
| Jogador 1 | 3-5 | 138 | Inferno | 39.259 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.852 |
| Jogador 1 | 3-6 | 140 | Inferno | 39.201 | 0.950 | 0.950 | 26.735 | -12.465 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.840 |
| Jogador 1 | 3-7 | 145 | Inferno | 39.201 | 0.950 | 0.950 | 35.921 | -3.280 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 7.840 |
| Jogador 1 | 4-1 | 156 | Inferno | 39.201 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.840 |
| Jogador 1 | 4-2 | 160 | Inferno | 42.383 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.477 |
| Jogador 1 | 4-3 | 168 | Inferno | 41.971 | 0.950 | 0.950 | 25.086 | -16.885 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.394 |
| Jogador 1 | 4-4 | 170 | Inferno | 43.875 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.775 |
| Jogador 1 | 4-5 | 174 | Inferno | 41.969 | 0.950 | 0.950 | 34.717 | -7.252 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.394 |
| Jogador 1 | 4-5 | 178 | Inferno | 41.969 | 0.950 | 0.950 | 34.067 | -7.902 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.394 |
| Jogador 1 | 4-6 | 180 | Inferno | 42.379 | 0.950 | 0.950 | 36.117 | -6.262 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.476 |
| Jogador 1 | 4-7 | 187 | Inferno | 42.602 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.520 |
| Jogador 1 | 5-1 | 190 | Inferno | 42.573 | 0.950 | 0.950 | 30.206 | -12.367 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.515 |
| Jogador 1 | 5-2 | 198 | Inferno | 41.873 | 0.950 | 0.950 | 41.953 | 0.080 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.375 |
| Jogador 1 | 5-3 | 200 | Inferno | 42.811 | 0.950 | 0.950 | 43.517 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 8.562 |
| Jogador 1 | 5-4 | 208 | Inferno | 41.925 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | Fera do Rift | 1 | 8.385 |
| Jogador 1 | 5-5 | 210 | Fera do Rift | 49.146 | 0.950 | 0.950 | 38.686 | -10.460 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 9.829 |
| Jogador 1 | 5-6 | 217 | Fera do Rift | 50.029 | 0.950 | 0.950 | 37.788 | -12.240 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.006 |
| Jogador 1 | 5-7 | 220 | Fera do Rift | 50.029 | 0.950 | 0.950 | 38.098 | -11.931 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.006 |
| Jogador 1 | 6-1 | 226 | Fera do Rift | 50.273 | 0.950 | 0.950 | 38.328 | -11.945 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.055 |
| Jogador 1 | 6-2 | 230 | Fera do Rift | 50.849 | 0.950 | 0.950 | 39.088 | -11.761 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.170 |
| Jogador 1 | 6-3 | 233 | Fera do Rift | 51.716 | 0.950 | 0.950 | 46.588 | -5.127 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.343 |
| Jogador 1 | 6-3 | 237 | Fera do Rift | 51.711 | 0.950 | 0.950 | 39.659 | -12.052 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.342 |
| Jogador 1 | 6-4 | 240 | Fera do Rift | 50.825 | 0.950 | 0.950 | 42.075 | -8.749 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.165 |
| Jogador 1 | 6-5 | 243 | Fera do Rift | 51.090 | 0.950 | 0.950 | 42.331 | -8.758 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.218 |
| Jogador 1 | 6-5 | 245 | Fera do Rift | 51.090 | 0.950 | 0.950 | 37.326 | -13.763 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.218 |
| Jogador 1 | 6-5 | 248 | Fera do Rift | 51.090 | 0.950 | 0.950 | 40.414 | -10.676 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.218 |
| Jogador 1 | 6-6 | 250 | Fera do Rift | 51.090 | 0.950 | 0.950 | 38.970 | -12.119 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.218 |
| Jogador 1 | 6-7 | 258 | Fera do Rift | 49.823 | 0.950 | 0.950 | 41.443 | -8.380 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.965 |
| Jogador 1 | 7-1 | 260 | Fera do Rift | 51.248 | 0.950 | 0.950 | 41.800 | -9.448 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.250 |
| Jogador 2 | 2-5 | 90 | Feérico | 42.846 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.569 |
| Jogador 2 | 2-6 | 99 | Feérico | 42.830 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.566 |
| Jogador 2 | 2-7 | 109 | Feérico | 43.148 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.630 |
| Jogador 2 | 3-1 | 118 | Feérico | 43.139 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.628 |
| Jogador 2 | 3-2 | 120 | Feérico | 43.139 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.628 |
| Jogador 2 | 3-3 | 127 | Feérico | 43.139 | 0.950 | 0.950 | 35.783 | -7.356 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 3-4 | 130 | Feérico | 43.139 | 0.950 | 0.950 | 35.916 | -7.224 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 3-5 | 138 | Feérico | 43.139 | 0.950 | 0.950 | 36.314 | -6.826 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 3-6 | 140 | Feérico | 43.139 | 0.950 | 0.950 | 37.745 | -5.395 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 3-7 | 149 | Feérico | 43.139 | 0.950 | 0.950 | 35.688 | -7.451 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 4-1 | 156 | Feérico | 43.139 | 0.950 | 0.950 | 43.019 | -0.120 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 4-2 | 160 | Feérico | 43.139 | 0.950 | 0.950 | 34.743 | -8.396 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 4-3 | 168 | Feérico | 43.139 | 0.950 | 0.950 | 36.973 | -6.166 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 4-4 | 170 | Feérico | 43.139 | 0.950 | 0.950 | 37.248 | -5.892 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.628 |
| Jogador 2 | 4-5 | 178 | Feérico | 44.145 | 0.950 | 0.950 | 36.093 | -8.052 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.829 |
| Jogador 3 | 2-5 | 90 | Colosso | 41.884 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.377 |
| Jogador 3 | 2-6 | 98 | Devastador | 44.780 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.956 |
| Jogador 3 | 2-7 | 107 | Devastador | 45.541 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 9.108 |
| Jogador 3 | 3-1 | 118 | Devastador | 44.726 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.945 |
| Jogador 3 | 3-2 | 120 | Devastador | 44.675 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.935 |
| Jogador 3 | 3-3 | 127 | Devastador | 44.649 | 0.950 | 0.950 | 40.118 | -4.531 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.930 |
| Jogador 3 | 3-4 | 130 | Devastador | 44.660 | 0.950 | 0.950 | 42.292 | -2.367 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 3-5 | 135 | Devastador | 44.660 | 0.950 | 0.950 | 42.200 | -2.460 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 3-5 | 138 | Devastador | 44.660 | 0.950 | 0.950 | 42.333 | -2.327 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 3-6 | 140 | Devastador | 44.660 | 0.950 | 0.950 | 41.804 | -2.856 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 3-7 | 149 | Devastador | 44.660 | 0.950 | 0.950 | 41.712 | -2.948 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 4-1 | 156 | Devastador | 44.660 | 0.950 | 0.950 | 34.003 | -10.657 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 4-2 | 160 | Devastador | 44.660 | 0.950 | 0.950 | 41.944 | -2.716 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 4-3 | 168 | Devastador | 44.660 | 0.950 | 0.950 | 37.022 | -7.638 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 4-4 | 170 | Devastador | 44.660 | 0.950 | 0.950 | 38.117 | -6.543 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 4-5 | 178 | Devastador | 44.660 | 0.950 | 0.950 | 40.666 | -3.994 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 4-6 | 180 | Devastador | 44.660 | 0.950 | 0.950 | 41.248 | -3.412 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 4-7 | 187 | Devastador | 44.660 | 0.950 | 0.950 | 40.332 | -4.328 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 5-1 | 190 | Devastador | 44.660 | 0.950 | 0.950 | 40.365 | -4.295 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.932 |
| Jogador 3 | 5-2 | 198 | Devastador | 46.274 | 0.950 | 0.950 | 41.430 | -4.844 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.255 |
| Jogador 4 | 2-5 | 90 | Florescer | 18.405 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 3.681 |
| Jogador 4 | 2-6 | 93 | Florescer | 23.373 | 0.950 | 0.950 | 13.083 | -10.290 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 4.675 |
| Jogador 4 | 2-7 | 109 | Florescer | 23.763 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 4.753 |
| Jogador 4 | 3-1 | 118 | Florescer | 23.857 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 4.771 |
| Jogador 4 | 3-2 | 120 | Florescer | 26.741 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 5.348 |
| Jogador 4 | 3-3 | 127 | Florescer | 28.825 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 5.765 |
| Jogador 4 | 3-4 | 130 | Florescer | 32.144 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 6.429 |
| Jogador 4 | 3-5 | 136 | Florescer | 30.302 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 6.060 |
| Jogador 4 | 3-6 | 140 | Florescer | 33.125 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 6.625 |
| Jogador 4 | 3-7 | 149 | Florescer | 24.899 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 4.980 |
| Jogador 4 | 4-1 | 156 | Florescer | 23.846 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 4.769 |
| Jogador 4 | 4-2 | 160 | Florescer | 31.126 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 6.225 |
| Jogador 4 | 4-3 | 168 | Florescer | 33.555 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 6.711 |
| Jogador 4 | 4-4 | 170 | Florescer | 35.490 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.098 |
| Jogador 4 | 4-5 | 177 | Florescer | 32.483 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 6.497 |
| Jogador 5 | 2-5 | 90 | Espinhos Negros | 40.961 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.192 |
| Jogador 5 | 2-6 | 99 | Espinhos Negros | 41.002 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.200 |
| Jogador 5 | 2-7 | 109 | Espinhos Negros | 41.951 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.390 |
| Jogador 5 | 3-1 | 118 | Espinhos Negros | 41.953 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.391 |
| Jogador 5 | 3-2 | 120 | Espinhos Negros | 41.953 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.391 |
| Jogador 5 | 3-4 | 130 | Espinhos Negros | 41.953 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.391 |
| Jogador 5 | 3-5 | 138 | Espinhos Negros | 41.953 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.391 |
| Jogador 5 | 3-6 | 140 | Espinhos Negros | 41.953 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.391 |
| Jogador 5 | 3-7 | 145 | Espinhos Negros | 41.953 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.391 |
| Jogador 5 | 4-1 | 156 | Espinhos Negros | 41.953 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.391 |
| Jogador 5 | 4-2 | 160 | Espinhos Negros | 41.953 | 0.950 | 0.950 | 38.279 | -3.674 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.391 |
| Jogador 5 | 4-3 | 168 | Espinhos Negros | 44.214 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.843 |
| Jogador 5 | 4-4 | 170 | Espinhos Negros | 43.618 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | Vivaz | 2 | 8.724 |
| Jogador 5 | 4-5 | 177 | Vivaz | 47.350 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.470 |
| Jogador 5 | 4-6 | 180 | Vivaz | 47.334 | 0.950 | 0.950 | 41.319 | -6.015 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.467 |
| Jogador 5 | 4-7 | 185 | Vivaz | 48.096 | 0.950 | 0.950 | 39.218 | -8.878 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.619 |
| Jogador 5 | 4-7 | 187 | Vivaz | 48.468 | 0.950 | 0.950 | 38.500 | -9.969 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.694 |
| Jogador 5 | 5-1 | 190 | Vivaz | 51.279 | 0.950 | 0.950 | 39.145 | -12.135 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.256 |
| Jogador 5 | 5-2 | 198 | Vivaz | 51.486 | 0.950 | 0.950 | 38.697 | -12.789 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.297 |
| Jogador 5 | 5-3 | 200 | Vivaz | 51.429 | 0.950 | 0.950 | 36.663 | -14.766 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.286 |
| Jogador 5 | 5-4 | 208 | Vivaz | 48.835 | 0.950 | 0.950 | 33.911 | -14.924 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.767 |
| Jogador 5 | 5-5 | 210 | Vivaz | 48.825 | 0.950 | 0.950 | 37.745 | -11.080 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.765 |
| Jogador 6 | 2-5 | 90 | Feérico | 41.074 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.215 |
| Jogador 6 | 2-6 | 99 | Feérico | 39.397 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 7.879 |
| Jogador 6 | 2-7 | 109 | Feérico | 39.397 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 7.879 |
| Jogador 6 | 3-1 | 118 | Feérico | 39.741 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.948 |
| Jogador 6 | 3-2 | 120 | Feérico | 39.648 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 7.930 |
| Jogador 6 | 3-3 | 127 | Feérico | 42.988 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 8.598 |
| Jogador 6 | 3-4 | 130 | Feérico | 44.781 | 0.950 | 0.950 | 40.395 | -4.385 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.956 |
| Jogador 6 | 3-5 | 138 | Feérico | 46.553 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.311 |
| Jogador 6 | 3-6 | 140 | Feérico | 46.255 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.251 |
| Jogador 6 | 3-7 | 143 | Feérico | 46.440 | 0.950 | 0.950 | 43.285 | -3.155 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.288 |
| Jogador 6 | 3-7 | 148 | Feérico | 46.664 | 0.950 | 0.950 | 41.218 | -5.446 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.333 |
| Jogador 6 | 4-1 | 153 | Feérico | 46.677 | 0.950 | 0.950 | 41.214 | -5.463 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.335 |
| Jogador 6 | 4-1 | 156 | Feérico | 46.430 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | True | — | 0 | 9.286 |
| Jogador 6 | 4-2 | 160 | Feérico | 46.744 | 0.950 | 0.950 | 38.323 | -8.421 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.349 |
| Jogador 6 | 4-3 | 168 | Feérico | 46.786 | 0.950 | 0.950 | 41.990 | -4.796 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.357 |
| Jogador 6 | 4-4 | 170 | Feérico | 46.999 | 0.950 | 0.950 | 43.027 | -3.972 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.400 |
| Jogador 6 | 4-5 | 178 | Feérico | 49.386 | 0.950 | 0.950 | 45.993 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 9.877 |
| Jogador 6 | 4-6 | 180 | Feérico | 49.339 | 0.950 | 0.950 | 45.951 | 0.000 | True | best_anchor_matches_current_direction | True | — | 0 | 9.868 |
| Jogador 6 | 4-7 | 187 | Feérico | 50.377 | 0.950 | 0.950 | 48.569 | -1.807 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.075 |
| Jogador 6 | 5-1 | 190 | Feérico | 50.405 | 0.950 | 0.950 | 48.605 | -1.800 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.081 |
| Jogador 6 | 5-2 | 198 | Feérico | 50.556 | 0.950 | 0.950 | 49.435 | -1.121 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.111 |
| Jogador 6 | 5-3 | 200 | Feérico | 50.541 | 0.950 | 0.950 | 44.598 | -5.942 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 10.108 |
| Jogador 7 | 2-7 | 106 | Colosso | 44.652 | 0.950 | 0.950 | 44.741 | 0.088 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.930 |
| Jogador 7 | 3-6 | 140 | Colosso | 47.020 | 0.950 | 0.950 | 45.595 | -1.425 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.404 |
| Jogador 7 | 3-7 | 146 | Colosso | 41.535 | 0.950 | 0.950 | 38.064 | -3.471 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.307 |
| Jogador 7 | 4-1 | 156 | Colosso | 42.200 | 0.950 | 0.950 | 19.822 | -22.378 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.440 |
| Jogador 7 | 4-2 | 160 | Colosso | 41.434 | 0.950 | 0.950 | 41.026 | -0.407 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.287 |
| Jogador 7 | 4-3 | 163 | Colosso | 41.380 | 0.950 | 0.950 | 30.610 | -10.770 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.276 |
| Jogador 7 | 4-3 | 167 | Colosso | 41.379 | 0.950 | 0.950 | 39.023 | -2.356 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.276 |
| Jogador 7 | 4-4 | 170 | Colosso | 41.373 | 0.950 | 0.950 | 39.024 | -2.349 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.275 |
| Jogador 7 | 4-5 | 178 | Colosso | 41.117 | 0.950 | 0.950 | 37.212 | -3.905 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.223 |
| Jogador 7 | 4-7 | 187 | Colosso | 41.520 | 0.950 | 0.950 | 33.674 | -7.845 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.304 |
| Jogador 7 | 5-1 | 190 | Colosso | 40.833 | 0.950 | 0.950 | 36.225 | -4.608 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.167 |
| Jogador 7 | 6-4 | 240 | Sabugueiro | 46.828 | 0.950 | 0.950 | 41.716 | -5.112 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 9.366 |
| Jogador 7 | 6-5 | 248 | Sabugueiro | 44.139 | 0.950 | 0.950 | 39.756 | -4.383 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.828 |
| Jogador 7 | 6-6 | 250 | Sabugueiro | 44.204 | 0.950 | 0.950 | 40.119 | -4.086 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.841 |
| Jogador 7 | 6-7 | 258 | Sabugueiro | 44.204 | 0.950 | 0.950 | 18.755 | -25.449 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.841 |
| Jogador 7 | 7-1 | 260 | Sabugueiro | 44.204 | 0.950 | 0.950 | 40.617 | -3.587 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.841 |
| Jogador 8 | 2-5 | 90 | Enfeitiçador | 40.429 | 0.950 | 0.000 | 0.000 | 0.000 | True | current_direction_viable_without_alternative | False | — | 0 | 8.086 |
| Jogador 8 | 2-6 | 99 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.039 | -20.390 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 8.086 |
| Jogador 8 | 2-7 | 107 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.422 | -20.008 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 8.086 |
| Jogador 8 | 3-1 | 111 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 36.964 | -3.465 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 8.086 |
| Jogador 8 | 3-1 | 118 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.054 | -20.375 | True | alternative_below_minimum_adapt_advantage | False | — | 0 | 8.086 |
| Jogador 8 | 3-2 | 120 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 36.949 | -3.480 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 3-3 | 127 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.324 | -20.105 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 3-4 | 130 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.091 | -20.338 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 3-5 | 138 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.125 | -20.304 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 3-6 | 140 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 31.409 | -9.020 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 3-7 | 149 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 19.639 | -20.791 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 4-1 | 156 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 25.031 | -15.398 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 4-2 | 160 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 38.483 | -1.946 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 4-3 | 168 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 19.704 | -20.725 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 4-4 | 170 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 24.599 | -15.830 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 4-5 | 178 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.376 | -20.053 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 4-6 | 180 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 24.742 | -15.687 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 4-7 | 187 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.965 | -19.465 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 5-1 | 190 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 36.813 | -3.616 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 5-2 | 198 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 20.817 | -19.613 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 5-3 | 200 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 24.901 | -15.528 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 5-4 | 208 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 25.669 | -14.760 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 5-5 | 210 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 35.089 | -5.340 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 5-7 | 220 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 26.393 | -14.036 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 6-1 | 226 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 26.468 | -13.962 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |
| Jogador 8 | 6-2 | 230 | Enfeitiçador | 40.429 | 0.950 | 0.950 | 26.393 | -14.036 | True | alternative_below_minimum_adapt_advantage | True | — | 0 | 8.086 |

### Unidades preservadas — sinais estratégicos versus investimento

| Jogador | Round | Unidade | Área | Estrelas | Classificação | Sinais estratégicos | Indicadores de investimento |
|---|---|---|---|---:|---|---|---|
| Jogador 1 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Akali | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 2-5 | Akali | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 2-5 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 2-6 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-6 | Akali | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 2-6 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 2-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 2-7 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-7 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 2-7 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 2-7 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-1 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-1 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-1 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-1 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-2 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-2 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-2 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-2 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-3 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-3 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-3 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-3 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-4 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 3-4 | Shen | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 3-4 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-4 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-5 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-5 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-5 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 1 | 3-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-6 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-6 | Kog'Maw | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 3-6 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 1 | 3-7 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 3-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 3-7 | Shen | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-7 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-7 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 3-7 | Shen | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 1 | 4-1 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-1 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-1 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-1 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-1 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-1 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-2 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-2 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-2 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-2 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-2 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-2 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-2 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-3 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-3 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-3 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-3 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-3 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-3 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-3 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-4 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-4 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-4 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-4 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-4 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-4 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-4 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-5 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-5 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-5 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-5 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-5 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-5 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-5 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-5 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-6 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-6 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-6 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-6 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-6 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-6 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-6 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 4-7 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 4-7 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 4-7 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-7 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 4-7 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 4-7 | Kog'Maw | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 5-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-1 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 5-1 | Vi | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-1 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-1 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-1 | Vi | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-1 | Kog'Maw | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 5-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-2 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 5-2 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 1 | 5-2 | Vi | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-2 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-2 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-2 | Vi | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-3 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 5-3 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 1 | 5-3 | Vi | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-3 | Shen | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-3 | Akali | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 1 | 5-3 | Vi | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-4 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 5-4 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-4 | Vi | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-4 | Akali | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-4 | Akali | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-4 | Vi | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-5 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 5-5 | Lobo Trevoguari | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 5-5 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-5 | Vi | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-5 | Lobo Trevoguari | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 5-5 | Grompe | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-5 | Grompe | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-5 | Vi | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-6 | Grompe | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-6 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 5-6 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-6 | Vi | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 1 | 5-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-6 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 5-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 5-7 | Grompe | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 5-7 | Krugue | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 1 | 5-7 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 5-7 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 5-7 | Vi | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 1 | 5-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 5-7 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 6-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-1 | Grompe | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-1 | Krugue | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 1 | 6-1 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-1 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-1 | Krugue | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Vi | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 1 | 6-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-1 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 6-2 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-2 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-2 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-2 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-2 | Krugue | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 6-2 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-2 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-2 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 6-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-3 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 1 | 6-3 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-3 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-3 | Krugue | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Krugue | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 6-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 6-3 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-3 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-3 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-3 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-3 | Krugue | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Krugue | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 1 | 6-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-3 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 6-4 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-4 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-4 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-4 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-4 | Krugue | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 6-4 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-4 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-4 | Lobo Trevoguari | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 1 | 6-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-5 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-5 | Krugue | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 6-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-5 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-5 | Krugue | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 6-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-5 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-5 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-5 | Krugue | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 6-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-5 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-6 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-6 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-6 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-6 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-6 | Krugue | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 6-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-6 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-7 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-7 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 6-7 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 6-7 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 6-7 | Krugue | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 6-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 6-7 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 7-1 | Rakan | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 7-1 | Grompe | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 1 | 7-1 | Lux | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 1 | 7-1 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 1 | 7-1 | Krugue | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 1 | 7-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 7-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 1 | 7-1 | Mamãe Bicuda | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-5 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-5 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-6 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-6 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-6 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 2-7 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 2-7 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 2-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-1 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 3-1 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-1 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-1 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-2 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-2 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 3-2 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-2 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-2 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 3-3 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-3 | Xayah | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 3-3 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-3 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-3 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-4 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-4 | Xayah | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 3-4 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-4 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-4 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-5 | Xayah | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 3-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-5 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-5 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-6 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 2 | 3-6 | Xayah | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 3-6 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-6 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-6 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 3-7 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 3-7 | Xayah | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 3-7 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 2 | 3-7 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 2 | 4-1 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-1 | Xayah | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-1 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-1 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-1 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-2 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-2 | Xayah | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-2 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-2 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-2 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 2 | 4-2 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-3 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-3 | Xayah | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-3 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-3 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-3 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-3 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-4 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-4 | Xayah | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-4 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-4 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 2 | 4-4 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-4 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-5 | Veigar | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 2 | 4-5 | Xayah | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 2 | 4-5 | Kobuko | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 2 | 4-5 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-5 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-5 | Kobuko | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 2 | 4-5 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-5 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-5 | Rakan | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-5 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-6 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 2-6 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-6 | Diana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 2-6 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-6 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-6 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 2-7 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-7 | Diana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 2-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 2-7 | Yorick | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 3 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-7 | Diana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 2-7 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-7 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 2-7 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 3 | 3-1 | Camille | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-1 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-1 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 3-1 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-1 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-2 | Camille | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-2 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-2 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-2 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-3 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-3 | Camille | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 3 | 3-3 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-3 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-3 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-4 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-4 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-4 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-4 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-4 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-5 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-5 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-5 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-5 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-6 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-6 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-6 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-6 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-6 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 3-7 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 3-7 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 3-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-7 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 3-7 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 3-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-1 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 4-1 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-1 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-1 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-2 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 4-2 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-2 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-2 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-2 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-3 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 4-3 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-3 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-3 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-4 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 4-4 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Camille | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-4 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-4 | Lobo Trevoguari | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Sivir | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 3 | 4-5 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-5 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Akali | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 3 | 4-5 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-6 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-6 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Lobo Trevoguari | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-6 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-7 | Lobo Trevoguari | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 4-7 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 4-7 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 4-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-7 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 4-7 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 4-7 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-1 | Lobo Trevoguari | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 3 | 5-1 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-1 | Aronguejo | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 3 | 5-1 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-1 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 3 | 5-1 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-1 | Aronguejo | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Lobo Trevoguari | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-2 | Akali | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 3 | 5-2 | Diana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 3 | 5-2 | Aronguejo | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 3 | 5-2 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Diana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 3 | 5-2 | Warwick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-5 | Diana | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 2-5 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 2-5 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-5 | Yunara | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 2-5 | Karma | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 2-6 | Diana | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 2-6 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 2-6 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-6 | Yunara | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 2-7 | Diana | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 2-7 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 2-7 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 2-7 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 2-7 | Yunara | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-1 | Diana | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-1 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-1 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 3-1 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-1 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-1 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-1 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-2 | Diana | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-2 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-2 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 3-2 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-2 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-2 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-2 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-3 | Diana | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-3 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-3 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-3 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-3 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 3-3 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 4 | 3-4 | Diana | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-4 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-4 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-4 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-4 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-4 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 4 | 3-4 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-5 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-5 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-5 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-5 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 4 | 3-5 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-5 | Diana | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 4 | 3-5 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-6 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-6 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-6 | Yunara | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-6 | Yorick | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 4 | 3-6 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-6 | Diana | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 4 | 3-6 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-7 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 3-7 | Diana | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-7 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-7 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 3-7 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 3-7 | Yunara | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 3-7 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 3-7 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 3-7 | Yunara | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 4 | 4-1 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-1 | Diana | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 4 | 4-1 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-1 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-1 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 4-1 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-1 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-1 | Yunara | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 4 | 4-2 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-2 | Diana | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 4 | 4-2 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-2 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-2 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 4-2 | Vi | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 4 | 4-2 | Yunara | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-2 | Master Yi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 4 | 4-2 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-3 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-3 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-3 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 4-3 | Vi | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 4-3 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Diana | bench | 1 | strategic_and_investment_signals | core_unit | equipped_items |
| Jogador 4 | 4-3 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-3 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-4 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-4 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-4 | Kog'Maw | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 4 | 4-4 | Diana | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 4 | 4-4 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Vi | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 4 | 4-4 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-4 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Sejuani | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 4 | 4-5 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-5 | Yunara | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-5 | Karma | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-5 | Kog'Maw | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 4 | 4-5 | Diana | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 4 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Kog'Maw | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 4 | 4-5 | Vi | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Sejuani | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 4 | 4-5 | Yunara | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-5 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-5 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-6 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-6 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 2-7 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 2-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 2-7 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 3-1 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-1 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 3-2 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-2 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 3-4 | Rek'Sai | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 3-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-4 | Warwick | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-4 | Rek'Sai | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-4 | Azir | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 3-5 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-5 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-5 | Azir | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 3-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-6 | Tristana | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 3-6 | Azir | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 3-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 3-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 3-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 3-7 | Azir | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-1 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-1 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-1 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-1 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-1 | Azir | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-2 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-2 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-2 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-2 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-2 | Azir | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 4-3 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-3 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-3 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-3 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-3 | Rek'Sai | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Rek'Sai | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Azir | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-3 | Azir | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-4 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-4 | Rek'Sai | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Rek'Sai | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Azir | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-4 | Azir | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 4-5 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-5 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-5 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-5 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-6 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-6 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-6 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-6 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-7 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-7 | Veigar | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 5 | 4-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-7 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-7 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 4-7 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-7 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 4-7 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-1 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-1 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-1 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-1 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-1 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-1 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-2 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-2 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-2 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-2 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-2 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-2 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-2 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-3 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-3 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-3 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-3 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-3 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-3 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-4 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-4 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-4 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-4 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-4 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-4 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-5 | Kobuko | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 5 | 5-5 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-5 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 5 | 5-5 | Tristana | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 5 | 5-5 | Kobuko | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 5 | 5-5 | Teemo | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 5 | 5-5 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Yorick | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-5 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 2-5 | Yorick | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-5 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-6 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-6 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 2-7 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 2-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 2-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-1 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-2 | Yorick | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 6 | 3-2 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 3-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 3-3 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-3 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-3 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 3-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 3-4 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-4 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-4 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 3-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-5 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-5 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 3-5 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-5 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 3-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-6 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-6 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 3-6 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-6 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-7 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 3-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-7 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 3-7 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 3-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 3-7 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 3-7 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-1 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-1 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 4-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-1 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-1 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-2 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-2 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 4-2 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-2 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-2 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-3 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-3 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 4-3 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-3 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-3 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-3 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-4 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-4 | Cascalho | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 4-4 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-4 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-4 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-4 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-5 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 4-5 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-5 | Tristana | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-5 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-5 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-5 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-5 | Cascalho | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 6 | 4-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-6 | Tristana | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 4-6 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 4-6 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-6 | Yorick | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 6 | 4-6 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-6 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-6 | Cascalho | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 6 | 4-7 | Diana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 4-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 4-7 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-7 | Yorick | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 6 | 4-7 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 4-7 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 4-7 | Tristana | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 4-7 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 4-7 | Cascalho | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 6 | 5-1 | Diana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 6 | 5-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 6 | 5-1 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-1 | Yorick | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 6 | 5-1 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-1 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 5-1 | Xayah | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-1 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-1 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-1 | Cascalho | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 6 | 5-2 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 5-2 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-2 | Diana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 5-2 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-2 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 5-2 | Xayah | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 6 | 5-2 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-2 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-2 | Cascalho | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 6 | 5-3 | Yorick | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 6 | 5-3 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-3 | Diana | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 5-3 | Tristana | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 6 | 5-3 | Xayah | board | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 6 | 5-3 | Rakan | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, multiple_owned_copies |
| Jogador 6 | 5-3 | Lillia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 6 | 5-3 | Rakan | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 6 | 5-3 | Cascalho | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 7 | 2-7 | Azuporã | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 2-7 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 2-7 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 2-7 | Yorick | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 2-7 | Yorick | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 2-7 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-6 | Azuporã | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-6 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-6 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-6 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 3-6 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 3-6 | Kog'Maw | bench | 2 | strategic_and_investment_signals | core_unit | upgraded_unit, equipped_items |
| Jogador 7 | 3-6 | Yorick | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 7 | 3-7 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-7 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 3-7 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 3-7 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 3-7 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 3-7 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-1 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-1 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-1 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-1 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 4-1 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-1 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-1 | Sejuani | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-1 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-2 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-2 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-2 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-2 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 4-2 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-2 | Hecarim | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-2 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-2 | Sejuani | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 7 | 4-3 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-3 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-3 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-3 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-3 | Sejuani | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 7 | 4-3 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-3 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-3 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-3 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-3 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-3 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-3 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-3 | Sejuani | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 7 | 4-4 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-4 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-4 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-4 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-4 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-4 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-4 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-4 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-4 | Sejuani | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 7 | 4-5 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-5 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-5 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 4-5 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-5 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-5 | Aronguejo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 4-5 | Aronguejo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 4-5 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-7 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-7 | LeBlanc | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 4-7 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 7 | 4-7 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 4-7 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 7 | 4-7 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 4-7 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 7 | 4-7 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 4-7 | Hecarim | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 7 | 5-1 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 5-1 | LeBlanc | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit |
| Jogador 7 | 5-1 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 7 | 5-1 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 5-1 | Mamãe Bicuda | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 5-1 | Hecarim | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 7 | 5-1 | Aronguejo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 7 | 5-1 | Vi | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 7 | 5-1 | Hecarim | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, multiple_owned_copies |
| Jogador 7 | 6-4 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-4 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 7 | 6-4 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-4 | LeBlanc | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 7 | 6-4 | Ezreal | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-4 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-4 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-4 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-5 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-5 | Soraka | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-5 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-5 | LeBlanc | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 7 | 6-5 | Ezreal | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-5 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-5 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 6-5 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-6 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-6 | Soraka | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-6 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-6 | LeBlanc | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 7 | 6-6 | Ezreal | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-6 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-6 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 6-6 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 6-7 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-7 | Soraka | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 7 | 6-7 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-7 | LeBlanc | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 7 | 6-7 | Ezreal | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 6-7 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 6-7 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 6-7 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 7 | 7-1 | Azuporã | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 7-1 | Soraka | board | 1 | strategic_and_investment_signals | currently_contributes_to_board | equipped_items |
| Jogador 7 | 7-1 | Hecarim | board | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 7-1 | LeBlanc | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 7 | 7-1 | Ezreal | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 7 | 7-1 | Xayah | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 7 | 7-1 | Cassiopeia | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 7 | 7-1 | Xayah | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-5 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 2-5 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 2-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 2-5 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-5 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 8 | 2-6 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 2-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 2-6 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-6 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 8 | 2-7 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 2-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 2-7 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 2-7 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 8 | 3-1 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-1 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-1 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 8 | 3-1 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-1 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-1 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-2 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-2 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 8 | 3-2 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-2 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-3 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-3 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 8 | 3-3 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 3-3 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-3 | Karma | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-4 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-4 | Soraka | board | 1 | observable_strategic_signals | currently_contributes_to_board |  |
| Jogador 8 | 3-4 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 3-4 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-4 | Karma | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit |
| Jogador 8 | 3-5 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-5 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-5 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 3-5 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 3-5 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-6 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-6 | Veigar | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 3-6 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 3-6 | Cassiopeia | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 3-6 | Veigar | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-7 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 3-7 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 3-7 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-7 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 3-7 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-1 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-1 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-1 | Teemo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-1 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-1 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-1 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-2 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-2 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-2 | Teemo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items |
| Jogador 8 | 4-2 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-2 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-2 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-2 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-3 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-3 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-3 | Teemo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-3 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-3 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-3 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-3 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-3 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-3 | Lillia | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 4-4 | Rakan | board | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-4 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-4 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-4 | Teemo | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 4-4 | Veigar | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-4 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | LeBlanc | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 4-4 | Teemo | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | Rakan | bench | 1 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-4 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-5 | LeBlanc | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-5 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-5 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-5 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 4-5 | Teemo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 8 | 4-5 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-5 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-5 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 8 | 4-5 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-6 | LeBlanc | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-6 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-6 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-6 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 4-6 | Teemo | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 8 | 4-6 | LeBlanc | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-6 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-6 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 8 | 4-6 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 4-7 | Master Yi | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 4-7 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 4-7 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 4-7 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 4-7 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 4-7 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 4-7 | LeBlanc | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 8 | 4-7 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 8 | 4-7 | Lillia | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 5-1 | Master Yi | board | 2 | strategic_and_investment_signals | currently_contributes_to_board | upgraded_unit |
| Jogador 8 | 5-1 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-1 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 5-1 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 5-1 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-1 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-1 | LeBlanc | bench | 2 | strategic_and_investment_signals | current_direction_or_core_trait | upgraded_unit |
| Jogador 8 | 5-1 | Rakan | bench | 2 | strategic_and_investment_signals | core_unit, current_direction_or_core_trait | upgraded_unit, equipped_items |
| Jogador 8 | 5-1 | Lillia | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 5-2 | Master Yi | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-2 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-2 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 5-2 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 5-2 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-2 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-2 | Lillia | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 5-3 | Master Yi | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-3 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-3 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 5-3 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-3 | Cassiopeia | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 5-3 | Cassiopeia | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-3 | Lillia | bench | 1 | observable_strategic_signals | core_unit |  |
| Jogador 8 | 5-4 | Master Yi | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 5-4 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-4 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 5-4 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-4 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-4 | Master Yi | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 8 | 5-4 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 5-5 | Master Yi | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items, multiple_owned_copies |
| Jogador 8 | 5-5 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-5 | Veigar | board | 1 | observable_strategic_signals | current_direction_or_core_trait, currently_contributes_to_board |  |
| Jogador 8 | 5-5 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-5 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-5 | Master Yi | bench | 1 | strategic_and_investment_signals | core_unit | multiple_owned_copies |
| Jogador 8 | 5-5 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 5-7 | Master Yi | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-7 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 5-7 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | multiple_owned_copies |
| Jogador 8 | 5-7 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 5-7 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 5-7 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 5-7 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 6-1 | Master Yi | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 6-1 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 6-1 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 6-1 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 6-1 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 6-1 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 6-1 | Karma | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 6-1 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |
| Jogador 8 | 6-2 | Master Yi | board | 2 | strategic_and_investment_signals | core_unit, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 6-2 | Soraka | board | 1 | observable_strategic_signals | core_unit, currently_contributes_to_board |  |
| Jogador 8 | 6-2 | Veigar | board | 1 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | equipped_items, multiple_owned_copies |
| Jogador 8 | 6-2 | Teemo | board | 2 | strategic_and_investment_signals | current_direction_or_core_trait, currently_contributes_to_board | upgraded_unit, equipped_items |
| Jogador 8 | 6-2 | Veigar | bench | 1 | strategic_and_investment_signals | current_direction_or_core_trait | multiple_owned_copies |
| Jogador 8 | 6-2 | Fiddlesticks | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 6-2 | Karma | bench | 1 | observable_strategic_signals | current_direction_or_core_trait |  |
| Jogador 8 | 6-2 | Lillia | bench | 1 | observable_strategic_signals | core_unit, current_direction_or_core_trait |  |

Unidades preservadas com evidência observável: **1255**.
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
| Jogador 1 | 2-5 | 90 | 2-6 | 0.000 | 1.000 | 4.000 | 0.0 / 3.0 / 8.0 | — |
| Jogador 1 | 2-6 | 98 | 2-7 | 0.000 | 2.000 | 4.000 | 0.0 / 4.0 / 4.0 | — |
| Jogador 1 | 2-7 | 109 | 3-1 | 0.000 | 2.000 | 0.000 | 0.0 / 13.0 / 0.0 | — |
| Jogador 1 | 3-1 | 115 | 3-2 | 0.000 | 11.000 | 0.000 | -10.0 / -6.0 / 0.0 | — |
| Jogador 1 | 3-2 | 120 | 3-3 | -10.000 | -17.000 | 0.000 | -10.0 / -11.0 / 0.0 | — |
| Jogador 1 | 3-3 | 127 | 3-4 | 0.000 | 6.000 | 0.000 | 0.0 / 8.0 / 6.0 | — |
| Jogador 1 | 3-4 | 130 | 3-5 | 0.000 | 2.000 | 6.000 | -9.0 / 6.0 / 6.0 | — |
| Jogador 1 | 3-5 | 138 | 3-6 | -9.000 | 4.000 | 0.000 | -9.0 / 7.0 / 0.0 | — |
| Jogador 1 | 3-6 | 140 | 3-7 | 0.000 | 3.000 | 0.000 | 0.0 / 13.0 / 0.0 | — |
| Jogador 1 | 3-7 | 145 | 4-1 | 0.000 | 10.000 | 0.000 | 0.0 / 25.0 / 0.0 | — |
| Jogador 1 | 4-1 | 156 | 4-2 | 0.000 | 15.000 | 0.000 | 0.0 / 23.0 / 0.0 | — |
| Jogador 1 | 4-2 | 160 | 4-3 | 0.000 | 8.000 | 0.000 | 0.0 / 22.0 / 0.0 | — |
| Jogador 1 | 4-3 | 168 | 4-4 | 0.000 | 14.000 | 0.000 | 0.0 / 22.0 / 0.0 | — |
| Jogador 1 | 4-4 | 170 | 4-5 | 0.000 | 8.000 | 0.000 | 0.0 / 25.0 / 0.0 | — |
| Jogador 1 | 4-5 | 174 | 4-6 | 0.000 | 17.000 | 0.000 | 0.0 / 21.0 / 0.0 | — |
| Jogador 1 | 4-5 | 178 | 4-6 | 0.000 | 17.000 | 0.000 | 0.0 / 21.0 / 0.0 | — |
| Jogador 1 | 4-6 | 180 | 4-7 | 0.000 | 4.000 | 0.000 | 0.0 / 18.0 / 0.0 | — |
| Jogador 1 | 4-7 | 187 | 5-1 | 0.000 | 14.000 | 0.000 | 0.0 / 37.0 / 0.0 | — |
| Jogador 1 | 5-1 | 190 | 5-2 | 0.000 | 23.000 | 0.000 | 0.0 / 36.0 / 0.0 | — |
| Jogador 1 | 5-2 | 198 | 5-3 | 0.000 | 13.000 | 0.000 | 0.0 / 28.0 / 2.0 | — |
| Jogador 1 | 5-3 | 200 | 5-4 | 0.000 | 15.000 | 2.000 | 0.0 / 24.0 / 2.0 | — |
| Jogador 1 | 5-4 | 208 | 5-5 | 0.000 | 9.000 | 0.000 | -16.0 / 15.0 / 4.0 | — |
| Jogador 1 | 5-5 | 210 | 5-6 | -16.000 | 6.000 | 4.000 | -16.0 / 10.0 / 10.0 | — |
| Jogador 1 | 5-6 | 217 | 5-7 | 0.000 | 4.000 | 6.000 | 0.0 / 6.0 / 6.0 | — |
| Jogador 1 | 5-7 | 220 | 6-1 | 0.000 | 2.000 | 0.000 | -17.0 / 16.0 / -2.0 | — |
| Jogador 1 | 6-1 | 226 | 6-2 | -17.000 | 14.000 | -2.000 | -17.0 / 17.0 / -2.0 | — |
| Jogador 1 | 6-2 | 230 | 6-3 | 0.000 | 3.000 | 0.000 | 0.0 / 18.0 / 0.0 | — |
| Jogador 1 | 6-3 | 233 | 6-4 | 0.000 | 15.000 | 0.000 | -18.0 / 24.0 / 0.0 | — |
| Jogador 1 | 6-3 | 237 | 6-4 | 0.000 | 15.000 | 0.000 | -18.0 / 24.0 / 0.0 | — |
| Jogador 1 | 6-4 | 240 | 6-5 | -18.000 | 9.000 | 0.000 | -36.0 / 22.0 / 0.0 | — |
| Jogador 1 | 6-5 | 243 | 6-6 | -18.000 | 13.000 | 0.000 | -18.0 / 27.0 / 0.0 | — |
| Jogador 1 | 6-5 | 245 | 6-6 | -18.000 | 13.000 | 0.000 | -18.0 / 27.0 / 0.0 | — |
| Jogador 1 | 6-5 | 248 | 6-6 | -18.000 | 13.000 | 0.000 | -18.0 / 27.0 / 0.0 | — |
| Jogador 1 | 6-6 | 250 | 6-7 | 0.000 | 14.000 | 0.000 | None / None / None | — |
| Jogador 1 | 6-7 | 258 | — | — | — | — | None / None / None | — |
| Jogador 1 | 7-1 | 260 | — | — | — | — | None / None / None | — |
| Jogador 2 | 2-5 | 90 | 2-6 | 0.000 | 7.000 | 0.000 | 0.0 / 15.0 / 0.0 | 8 |
| Jogador 2 | 2-6 | 99 | 2-7 | 0.000 | 8.000 | 0.000 | -12.0 / 17.0 / 0.0 | 8 |
| Jogador 2 | 2-7 | 109 | 3-1 | -12.000 | 9.000 | 0.000 | -23.0 / 17.0 / 2.0 | 8 |
| Jogador 2 | 3-1 | 118 | 3-2 | -11.000 | 8.000 | 2.000 | -11.0 / 7.0 / 8.0 | 8 |
| Jogador 2 | 3-2 | 120 | 3-3 | 0.000 | -1.000 | 6.000 | 0.0 / 3.0 / 6.0 | 8 |
| Jogador 2 | 3-3 | 127 | 3-4 | 0.000 | 4.000 | 0.000 | -11.0 / 9.0 / 0.0 | 8 |
| Jogador 2 | 3-4 | 130 | 3-5 | -11.000 | 5.000 | 0.000 | -21.0 / 14.0 / 0.0 | 8 |
| Jogador 2 | 3-5 | 138 | 3-6 | -10.000 | 9.000 | 0.000 | -10.0 / 20.0 / 0.0 | 8 |
| Jogador 2 | 3-6 | 140 | 3-7 | 0.000 | 11.000 | 0.000 | -10.0 / 20.0 / 0.0 | 8 |
| Jogador 2 | 3-7 | 149 | 4-1 | -10.000 | 9.000 | 0.000 | -21.0 / 22.0 / 8.0 | 8 |
| Jogador 2 | 4-1 | 156 | 4-2 | -11.000 | 13.000 | 8.000 | -22.0 / 21.0 / 8.0 | 8 |
| Jogador 2 | 4-2 | 160 | 4-3 | -11.000 | 8.000 | 0.000 | -11.0 / 22.0 / 0.0 | 8 |
| Jogador 2 | 4-3 | 168 | 4-4 | 0.000 | 14.000 | 0.000 | -3.0 / 15.0 / -28.0 | 8 |
| Jogador 2 | 4-4 | 170 | 4-5 | -3.000 | 1.000 | -28.000 | None / None / None | 8 |
| Jogador 2 | 4-5 | 178 | — | — | — | — | None / None / None | 8 |
| Jogador 3 | 2-5 | 90 | 2-6 | -5.000 | 1.000 | 2.000 | -5.0 / 3.0 / 2.0 | 6 |
| Jogador 3 | 2-6 | 98 | 2-7 | 0.000 | 2.000 | 0.000 | -10.0 / 15.0 / 0.0 | 6 |
| Jogador 3 | 2-7 | 107 | 3-1 | -10.000 | 13.000 | 0.000 | -21.0 / 19.0 / 0.0 | 6 |
| Jogador 3 | 3-1 | 118 | 3-2 | -11.000 | 6.000 | 0.000 | -11.0 / 5.0 / 12.0 | 6 |
| Jogador 3 | 3-2 | 120 | 3-3 | 0.000 | -1.000 | 12.000 | 0.0 / 3.0 / 12.0 | 6 |
| Jogador 3 | 3-3 | 127 | 3-4 | 0.000 | 4.000 | 0.000 | -9.0 / 10.0 / 0.0 | 6 |
| Jogador 3 | 3-4 | 130 | 3-5 | -9.000 | 6.000 | 0.000 | -19.0 / 19.0 / 0.0 | 6 |
| Jogador 3 | 3-5 | 135 | 3-6 | -10.000 | 13.000 | 0.000 | -10.0 / 23.0 / 0.0 | 6 |
| Jogador 3 | 3-5 | 138 | 3-6 | -10.000 | 13.000 | 0.000 | -10.0 / 23.0 / 0.0 | 6 |
| Jogador 3 | 3-6 | 140 | 3-7 | 0.000 | 10.000 | 0.000 | 0.0 / 19.0 / 0.0 | 6 |
| Jogador 3 | 3-7 | 149 | 4-1 | 0.000 | 9.000 | 0.000 | 0.0 / 24.0 / 0.0 | 6 |
| Jogador 3 | 4-1 | 156 | 4-2 | 0.000 | 15.000 | 0.000 | -12.0 / 21.0 / 0.0 | 6 |
| Jogador 3 | 4-2 | 160 | 4-3 | -12.000 | 6.000 | 0.000 | -12.0 / 20.0 / 0.0 | 6 |
| Jogador 3 | 4-3 | 168 | 4-4 | 0.000 | 14.000 | 0.000 | 0.0 / 16.0 / -4.0 | 6 |
| Jogador 3 | 4-4 | 170 | 4-5 | 0.000 | 2.000 | -4.000 | -12.0 / 20.0 / -4.0 | 6 |
| Jogador 3 | 4-5 | 178 | 4-6 | -12.000 | 18.000 | 0.000 | -12.0 / 18.0 / 4.0 | 6 |
| Jogador 3 | 4-6 | 180 | 4-7 | 0.000 | 0.000 | 4.000 | -16.0 / 9.0 / 4.0 | 6 |
| Jogador 3 | 4-7 | 187 | 5-1 | -16.000 | 9.000 | 0.000 | -20.0 / 11.0 / -32.0 | 6 |
| Jogador 3 | 5-1 | 190 | 5-2 | -4.000 | 2.000 | -32.000 | None / None / None | 6 |
| Jogador 3 | 5-2 | 198 | — | — | — | — | None / None / None | 6 |
| Jogador 4 | 2-5 | 90 | 2-6 | -6.000 | 3.000 | 0.000 | -6.0 / 4.0 / 2.0 | 7 |
| Jogador 4 | 2-6 | 93 | 2-7 | 0.000 | 1.000 | 2.000 | 0.0 / 3.0 / 2.0 | 7 |
| Jogador 4 | 2-7 | 109 | 3-1 | 0.000 | 2.000 | 0.000 | -11.0 / 7.0 / 2.0 | 7 |
| Jogador 4 | 3-1 | 118 | 3-2 | -11.000 | 5.000 | 2.000 | -20.0 / 4.0 / 4.0 | 7 |
| Jogador 4 | 3-2 | 120 | 3-3 | -9.000 | -1.000 | 2.000 | -9.0 / 2.0 / 2.0 | 7 |
| Jogador 4 | 3-3 | 127 | 3-4 | 0.000 | 3.000 | 0.000 | -12.0 / 6.0 / -2.0 | 7 |
| Jogador 4 | 3-4 | 130 | 3-5 | -12.000 | 3.000 | -2.000 | -22.0 / 8.0 / -2.0 | 7 |
| Jogador 4 | 3-5 | 136 | 3-6 | -10.000 | 5.000 | 0.000 | -10.0 / 11.0 / 2.0 | 7 |
| Jogador 4 | 3-6 | 140 | 3-7 | 0.000 | 6.000 | 2.000 | -11.0 / 23.0 / 2.0 | 7 |
| Jogador 4 | 3-7 | 149 | 4-1 | -11.000 | 17.000 | 0.000 | -23.0 / 27.0 / 0.0 | 7 |
| Jogador 4 | 4-1 | 156 | 4-2 | -12.000 | 10.000 | 0.000 | -24.0 / 20.0 / -2.0 | 7 |
| Jogador 4 | 4-2 | 160 | 4-3 | -12.000 | 10.000 | -2.000 | -12.0 / 25.0 / 2.0 | 7 |
| Jogador 4 | 4-3 | 168 | 4-4 | 0.000 | 15.000 | 4.000 | -7.0 / 8.0 / -24.0 | 7 |
| Jogador 4 | 4-4 | 170 | 4-5 | -7.000 | -7.000 | -28.000 | None / None / None | 7 |
| Jogador 4 | 4-5 | 177 | — | — | — | — | None / None / None | 7 |
| Jogador 5 | 2-5 | 90 | 2-6 | -6.000 | 1.000 | 0.000 | -6.0 / -1.0 / -2.0 | 4 |
| Jogador 5 | 2-6 | 99 | 2-7 | 0.000 | -2.000 | -2.000 | -10.0 / -2.0 / -2.0 | 4 |
| Jogador 5 | 2-7 | 109 | 3-1 | -10.000 | 0.000 | 0.000 | -10.0 / 3.0 / 0.0 | 4 |
| Jogador 5 | 3-1 | 118 | 3-2 | 0.000 | 3.000 | 0.000 | -9.0 / 1.0 / 0.0 | 4 |
| Jogador 5 | 3-2 | 120 | 3-3 | -9.000 | -2.000 | 0.000 | -9.0 / 3.0 / 0.0 | 4 |
| Jogador 5 | 3-4 | 130 | 3-5 | -11.000 | -2.000 | 4.000 | -11.0 / 1.0 / 10.0 | 4 |
| Jogador 5 | 3-5 | 138 | 3-6 | 0.000 | 3.000 | 6.000 | 0.0 / 6.0 / 6.0 | 4 |
| Jogador 5 | 3-6 | 140 | 3-7 | 0.000 | 3.000 | 0.000 | -12.0 / 9.0 / 0.0 | 4 |
| Jogador 5 | 3-7 | 145 | 4-1 | -12.000 | 6.000 | 0.000 | -12.0 / 6.0 / 0.0 | 4 |
| Jogador 5 | 4-1 | 156 | 4-2 | 0.000 | 0.000 | 0.000 | 0.0 / 20.0 / 0.0 | 4 |
| Jogador 5 | 4-2 | 160 | 4-3 | 0.000 | 20.000 | 0.000 | 0.0 / 29.0 / 0.0 | 4 |
| Jogador 5 | 4-3 | 168 | 4-4 | 0.000 | 9.000 | 0.000 | -14.0 / 16.0 / 0.0 | 4 |
| Jogador 5 | 4-4 | 170 | 4-5 | -14.000 | 7.000 | 0.000 | -24.0 / 15.0 / 0.0 | 4 |
| Jogador 5 | 4-5 | 177 | 4-6 | -10.000 | 8.000 | 0.000 | -10.0 / 22.0 / 0.0 | 4 |
| Jogador 5 | 4-6 | 180 | 4-7 | 0.000 | 14.000 | 0.000 | 0.0 / 24.0 / 0.0 | 4 |
| Jogador 5 | 4-7 | 185 | 5-1 | 0.000 | 10.000 | 0.000 | 0.0 / 20.0 / 0.0 | 4 |
| Jogador 5 | 4-7 | 187 | 5-1 | 0.000 | 10.000 | 0.000 | 0.0 / 20.0 / 0.0 | 4 |
| Jogador 5 | 5-1 | 190 | 5-2 | 0.000 | 10.000 | 0.000 | -15.0 / 15.0 / 0.0 | 4 |
| Jogador 5 | 5-2 | 198 | 5-3 | -15.000 | 5.000 | 0.000 | -15.0 / 14.0 / 0.0 | 4 |
| Jogador 5 | 5-3 | 200 | 5-4 | 0.000 | 9.000 | 0.000 | -13.0 / 12.0 / -28.0 | 4 |
| Jogador 5 | 5-4 | 208 | 5-5 | -13.000 | 3.000 | -28.000 | None / None / None | 4 |
| Jogador 5 | 5-5 | 210 | — | — | — | — | None / None / None | 4 |
| Jogador 6 | 2-5 | 90 | 2-6 | -6.000 | -2.000 | 2.000 | -6.0 / -1.0 / 2.0 | 5 |
| Jogador 6 | 2-6 | 99 | 2-7 | 0.000 | 1.000 | 0.000 | 0.0 / -1.0 / 4.0 | 5 |
| Jogador 6 | 2-7 | 109 | 3-1 | 0.000 | -2.000 | 4.000 | -10.0 / 2.0 / 6.0 | 5 |
| Jogador 6 | 3-1 | 118 | 3-2 | -10.000 | 4.000 | 2.000 | -10.0 / 4.0 / 2.0 | 5 |
| Jogador 6 | 3-2 | 120 | 3-3 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 / 0.0 | 5 |
| Jogador 6 | 3-3 | 127 | 3-4 | 0.000 | -1.000 | 0.000 | 0.0 / -3.0 / 6.0 | 5 |
| Jogador 6 | 3-4 | 130 | 3-5 | 0.000 | -2.000 | 6.000 | 0.0 / 2.0 / 6.0 | 5 |
| Jogador 6 | 3-5 | 138 | 3-6 | 0.000 | 4.000 | 0.000 | 0.0 / 7.0 / 0.0 | 5 |
| Jogador 6 | 3-6 | 140 | 3-7 | 0.000 | 3.000 | 0.000 | -11.0 / 6.0 / 0.0 | 5 |
| Jogador 6 | 3-7 | 143 | 4-1 | -11.000 | 3.000 | 0.000 | -22.0 / 17.0 / 0.0 | 5 |
| Jogador 6 | 3-7 | 148 | 4-1 | -11.000 | 3.000 | 0.000 | -22.0 / 17.0 / 0.0 | 5 |
| Jogador 6 | 4-1 | 153 | 4-2 | -11.000 | 14.000 | 0.000 | -11.0 / 22.0 / 0.0 | 5 |
| Jogador 6 | 4-1 | 156 | 4-2 | -11.000 | 14.000 | 0.000 | -11.0 / 22.0 / 0.0 | 5 |
| Jogador 6 | 4-2 | 160 | 4-3 | 0.000 | 8.000 | 0.000 | 0.0 / 14.0 / 0.0 | 5 |
| Jogador 6 | 4-3 | 168 | 4-4 | 0.000 | 6.000 | 0.000 | 0.0 / 18.0 / 8.0 | 5 |
| Jogador 6 | 4-4 | 170 | 4-5 | 0.000 | 12.000 | 8.000 | 0.0 / 21.0 / 8.0 | 5 |
| Jogador 6 | 4-5 | 178 | 4-6 | 0.000 | 9.000 | 0.000 | 0.0 / 10.0 / 2.0 | 5 |
| Jogador 6 | 4-6 | 180 | 4-7 | 0.000 | 1.000 | 2.000 | -14.0 / 11.0 / 2.0 | 5 |
| Jogador 6 | 4-7 | 187 | 5-1 | -14.000 | 10.000 | 0.000 | -28.0 / 17.0 / 0.0 | 5 |
| Jogador 6 | 5-1 | 190 | 5-2 | -14.000 | 7.000 | 0.000 | -24.0 / 3.0 / -34.0 | 5 |
| Jogador 6 | 5-2 | 198 | 5-3 | -10.000 | -4.000 | -34.000 | None / None / None | 5 |
| Jogador 6 | 5-3 | 200 | — | — | — | — | None / None / None | 5 |
| Jogador 7 | 2-7 | 106 | 3-1 | -10.000 | -1.000 | 0.000 | -10.0 / 2.0 / 0.0 | — |
| Jogador 7 | 3-6 | 140 | 3-7 | 0.000 | 20.000 | 0.000 | 0.0 / 22.0 / 0.0 | — |
| Jogador 7 | 3-7 | 146 | 4-1 | 0.000 | 2.000 | 0.000 | 0.0 / 3.0 / 6.0 | — |
| Jogador 7 | 4-1 | 156 | 4-2 | 0.000 | 1.000 | 6.000 | 0.0 / 3.0 / 6.0 | — |
| Jogador 7 | 4-2 | 160 | 4-3 | 0.000 | 2.000 | 0.000 | 0.0 / 18.0 / 0.0 | — |
| Jogador 7 | 4-3 | 163 | 4-4 | 0.000 | 16.000 | 0.000 | 0.0 / 25.0 / 0.0 | — |
| Jogador 7 | 4-3 | 167 | 4-4 | 0.000 | 16.000 | 0.000 | 0.0 / 25.0 / 0.0 | — |
| Jogador 7 | 4-4 | 170 | 4-5 | 0.000 | 9.000 | 0.000 | 0.0 / 20.0 / -8.0 | — |
| Jogador 7 | 4-5 | 178 | 4-6 | 0.000 | 11.000 | -8.000 | 0.0 / 19.0 / 6.0 | — |
| Jogador 7 | 4-7 | 187 | 5-1 | 0.000 | 12.000 | 0.000 | -15.0 / 25.0 / 0.0 | — |
| Jogador 7 | 5-1 | 190 | 5-2 | -15.000 | 13.000 | 0.000 | -15.0 / 29.0 / 0.0 | — |
| Jogador 7 | 6-4 | 240 | 6-5 | 0.000 | 17.000 | 0.000 | 0.0 / 26.0 / 0.0 | — |
| Jogador 7 | 6-5 | 248 | 6-6 | 0.000 | 9.000 | 0.000 | 0.0 / 22.0 / 0.0 | — |
| Jogador 7 | 6-6 | 250 | 6-7 | 0.000 | 13.000 | 0.000 | None / None / None | — |
| Jogador 7 | 6-7 | 258 | — | — | — | — | None / None / None | — |
| Jogador 7 | 7-1 | 260 | — | — | — | — | None / None / None | — |
| Jogador 8 | 2-5 | 90 | 2-6 | 0.000 | 0.000 | 12.000 | 0.0 / -1.0 / 12.0 | 3 |
| Jogador 8 | 2-6 | 99 | 2-7 | 0.000 | -1.000 | 0.000 | 0.0 / 1.0 / 0.0 | 3 |
| Jogador 8 | 2-7 | 107 | 3-1 | 0.000 | 2.000 | 0.000 | 0.0 / 12.0 / 0.0 | 3 |
| Jogador 8 | 3-1 | 111 | 3-2 | 0.000 | 10.000 | 0.000 | 0.0 / 19.0 / 0.0 | 3 |
| Jogador 8 | 3-1 | 118 | 3-2 | 0.000 | 10.000 | 0.000 | 0.0 / 19.0 / 0.0 | 3 |
| Jogador 8 | 3-2 | 120 | 3-3 | 0.000 | 9.000 | 0.000 | 0.0 / 16.0 / 0.0 | 3 |
| Jogador 8 | 3-3 | 127 | 3-4 | 0.000 | 7.000 | 0.000 | 0.0 / 18.0 / 0.0 | 3 |
| Jogador 8 | 3-4 | 130 | 3-5 | 0.000 | 11.000 | 0.000 | 0.0 / 21.0 / 0.0 | 3 |
| Jogador 8 | 3-5 | 138 | 3-6 | 0.000 | 10.000 | 0.000 | 0.0 / 5.0 / 4.0 | 3 |
| Jogador 8 | 3-6 | 140 | 3-7 | 0.000 | -5.000 | 4.000 | 0.0 / 11.0 / 4.0 | 3 |
| Jogador 8 | 3-7 | 149 | 4-1 | 0.000 | 16.000 | 0.000 | -11.0 / 25.0 / 0.0 | 3 |
| Jogador 8 | 4-1 | 156 | 4-2 | -11.000 | 9.000 | 0.000 | -23.0 / 25.0 / 0.0 | 3 |
| Jogador 8 | 4-2 | 160 | 4-3 | -12.000 | 16.000 | 0.000 | -12.0 / 25.0 / 2.0 | 3 |
| Jogador 8 | 4-3 | 168 | 4-4 | 0.000 | 9.000 | 2.000 | -11.0 / 14.0 / 6.0 | 3 |
| Jogador 8 | 4-4 | 170 | 4-5 | -11.000 | 5.000 | 4.000 | -22.0 / 14.0 / 8.0 | 3 |
| Jogador 8 | 4-5 | 178 | 4-6 | -11.000 | 9.000 | 4.000 | -11.0 / 8.0 / 10.0 | 3 |
| Jogador 8 | 4-6 | 180 | 4-7 | 0.000 | -1.000 | 6.000 | -14.0 / 11.0 / 6.0 | 3 |
| Jogador 8 | 4-7 | 187 | 5-1 | -14.000 | 12.000 | 0.000 | -14.0 / 25.0 / 0.0 | 3 |
| Jogador 8 | 5-1 | 190 | 5-2 | 0.000 | 13.000 | 0.000 | 0.0 / 24.0 / 0.0 | 3 |
| Jogador 8 | 5-2 | 198 | 5-3 | 0.000 | 11.000 | 0.000 | 0.0 / 20.0 / 0.0 | 3 |
| Jogador 8 | 5-3 | 200 | 5-4 | 0.000 | 9.000 | 0.000 | 0.0 / 20.0 / 0.0 | 3 |
| Jogador 8 | 5-4 | 208 | 5-5 | 0.000 | 11.000 | 0.000 | 0.0 / 23.0 / 0.0 | 3 |
| Jogador 8 | 5-5 | 210 | 5-6 | 0.000 | 12.000 | 0.000 | 0.0 / 23.0 / 0.0 | 3 |
| Jogador 8 | 5-7 | 220 | 6-1 | -18.000 | 12.000 | 0.000 | -18.0 / 20.0 / 0.0 | 3 |
| Jogador 8 | 6-1 | 226 | 6-2 | 0.000 | 8.000 | 0.000 | -6.0 / 7.0 / -48.0 | 3 |
| Jogador 8 | 6-2 | 230 | 6-3 | -6.000 | -1.000 | -48.000 | None / None / None | 3 |

A evolução posterior é associação temporal, não atribuição causal à recomendação shadow.


### Auditoria de INSUFFICIENT_EVIDENCE

| Jogador | Round | Step | Motivo específico | Geração de candidatos | Direção atual | Viável atual | Score atual | Score âncora | Vantagem | Mín. ADAPT | Limite PIVOT | Conf. âncora | Conf. direção atual | Âncora disponível | Filtros (considerados/gerados/catálogo ausente/planos vazios/âncora ausente) |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Jogador 1 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-2 | 17 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-3 | 26 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 1 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-1 | 47 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-3 | 68 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-4 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 1 | 2-5 | 82 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-2 | 15 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-3 | 31 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 2 | 1-4 | 40 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-3 | 66 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-4 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 2 | 2-5 | 82 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 17 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-1 | 4 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-2 | 16 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-3 | 31 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 3 | 1-4 | 38 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-3 | 65 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-4 | 74 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 16 / 0 / 0 / 0 / 0 |
| Jogador 3 | 2-5 | 82 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 17 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-1 | 4 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-2 | 16 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-3 | 26 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 4 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-1 | 47 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-3 | 70 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 9 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-4 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 9 / 0 / 0 / 0 / 0 |
| Jogador 4 | 2-5 | 82 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-2 | 17 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-3 | 23 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 5 | 1-4 | 36 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 9 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-1 | 48 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-2 | 54 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-3 | 70 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-4 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 5 | 2-5 | 82 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-2 | 14 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-3 | 31 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 6 | 1-4 | 35 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-1 | 47 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-2 | 56 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-3 | 67 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-4 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 6 | 2-5 | 82 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 14 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-1 | 2 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-2 | 18 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-3 | 27 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 7 | 1-4 | 38 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-1 | 47 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 12 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 7 | 2-3 | 69 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 10 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-1 | 1 | — | — | — | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | False | 0 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-1 | 3 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-2 | 17 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 6 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-3 | 24 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 8 | 1-4 | 39 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-1 | 50 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 7 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-2 | 60 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 9 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-3 | 70 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 8 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-4 | 80 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 11 / 0 / 0 / 0 / 0 |
| Jogador 8 | 2-5 | 82 | no_initial_anchor_available | no_cost_four_or_five_anchor | — | False | 0.000 | 0.000 | 0.000 | 0.100 | 0.750 | 0.000 | 0.000 | False | 13 / 0 / 0 / 0 / 0 |

**Motivos agregados:** unavailable=8; no_initial_anchor_available=70
**Motivos de geração agregados:** unavailable=8; no_cost_four_or_five_anchor=70
**Viabilidade da direção atual:** not_viable=78

Confiança da âncora e confiança da direção atual são derivadas de score e não são probabilidades calibradas. Snapshots por ação podem repetir a mesma revisão; não devem ser contados como revisões independentes.
