# Catálogo completo de cenários econômicos

Os cenários abaixo são detectados em observações reais da engine C++. Eles não
são estados sintéticos injetados: a API atual não possui setter público para
ouro, HP, nível, estágio, lobby ou composição.

| ID | Condições | Estratégia | Tipo | Objetivo |
|---|---|---|---|---|
| `s4_fast8_lvl6_gold60_hp_ok` | Estágio 4-1, nível 1–6, ouro 60+, HP acima de 40 | FAST8 | Treinável | Incentivo pequeno para BUY_XP; desincentivo leve a PASS/ROLL |
| `s4_fast8_lvl6_gold80` | Estágio 4-1, nível 1–6, ouro 80+, HP acima de 20 | FAST8 | Treinável | Caso severo de acúmulo; maior incentivo contextual para BUY_XP |
| `s4_fast8_lvl7_gold60` | Estágio 4-1, nível 7, ouro 60+, HP acima de 30 | FAST8 | Treinável | Avaliar progressão para nível 8, sem forçar 9/10 |
| `late_game_high_gold_underleveled` | Estágio 4–5, nível até 7, ouro 60+, HP acima de 30 | ECON, STABILIZE, FAST8, ALL_IN, WINSTREAK, LOSS_STREAK | Treinável | Reduzir passividade econômica fora de SLOWROLL |
| `critical_hp_high_gold` | Estágio 3–7, HP até 30, ouro 50+ | Todas | Monitor-only | Investigar acúmulo com risco de eliminação; não forçar XP |
| `low_hp_fast8_high_gold` | Estágio 3–7, FAST8, HP até 40, ouro 50+ | FAST8 | Monitor-only | Verificar trade-off entre XP e estabilização |
| `slowroll_gold_reserve` | Estágio 2–5, nível 5–7, ouro 50+, HP 20+ | SLOWROLL | Treinável/proteção | Penalizar BUY_XP para preservar a lógica de slowroll |
| `all_in_gold_hoarding` | Estágio 3–7, ouro 50+ | ALL_IN | Monitor-only | Investigar reservas incompatíveis com ALL_IN sem criar reward especulativo |
| `player8_all_in_gold_hoarding` | Estágio 3–7, jogador 8 (player_id 7), ouro 50+ | ALL_IN | Monitor-only | Isolar o caso específico do oitavo jogador observado na auditoria |
| `gold_above_50_any_strategy` | Qualquer estágio/nível/estratégia, ouro acima de 50 | Todas | Monitor-only | Medir BUY, BUY_XP, ROLL e PASS por contexto |
| `useful_shop_opportunity` | Ouro acima de 50 e candidatos de loja | Todas | Monitor-only | Aguardar contrato semântico confiável para identificar compra realmente útil |

## O que é treinado

O script usa o reward nativo da engine e adiciona shaping pequeno somente nos
estados que correspondem a cenários treináveis. O shaping incide sobre a
decisão de tipo:

- BUY_XP: incentivo contextual nos cenários FAST8/atraso de nível.
- PASS e REROLL: penalidades pequenas nos cenários específicos de acúmulo.
- SLOWROLL: penalidade contextual para BUY_XP, evitando que a correção de
  economia se transforme em gasto indiscriminado de XP.
- HP crítico: BUY_XP nunca recebe shaping positivo.

Não existe bônus genérico para qualquer compra ou qualquer gasto de ouro. A
observação disponível não comprova, por si só, que cada unidade na loja é útil,
que o tabuleiro está estabilizado ou que uma compra é superior a XP/roll.
Esses cenários ficam visíveis para auditoria, mas sem rótulos artificiais.

## Limitações de cobertura

A observação do agente fornece HP, ouro, nível, round/estágio e estratégia.
Esta versão não presume que a observação individual revele o nível médio dos
sete oponentes. Portanto, "nível abaixo do lobby" é aproximado pelos alvos de
nível por estágio/estratégia da própria política. Um gap real contra o lobby
só poderá ser adicionado quando existir um campo público e documentado no
snapshot da engine.

O número de ocorrências de cada cenário é reportado. Zero ocorrências significa
**não coberto**, não sucesso.
