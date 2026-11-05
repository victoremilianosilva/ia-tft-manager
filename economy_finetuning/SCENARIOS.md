# Catálogo completo de cenários econômicos

Os cenários abaixo são detectados em observações reais da engine C++. Eles não
são estados sintéticos injetados: a API atual não possui setter público para
ouro, HP, nível, estágio, lobby ou composição. Cada execução seleciona um único
cenário treinável; todos os demais ficam apenas em monitoramento.

| ID | Condições | Estratégia | Tipo | Objetivo |
|---|---|---|---|---|
| `s4_fast8_lvl6_gold60_hp_ok` | Estágio 4 (4-1 a 4-7), nível 6, ouro 60+, HP acima de 40 | FAST8 | Treinável — reward nativo | Aprender a escolher BUY_XP versus compra útil/PASS/ROLL sem recompensa sintética |
| `s4_fast8_lvl6_gold80` | Estágio 4 (4-1 a 4-7), nível 6, ouro 80+, HP acima de 40 | FAST8 | Treinável — reward nativo | Aprender conversão do excedente sem bônus artificial para XP |
| `s4_fast8_lvl7_gold60` | Estágio 4 (4-1 a 4-7), nível 7, ouro 60+, HP acima de 30 | FAST8 | Treinável — reward nativo | Aprender timing de nível 8 sem forçar 9/10 |
| `late_game_high_gold_underleveled` | Estágio 4–5, nível até 7, ouro 60+, HP acima de 30 | ECON, STABILIZE, FAST8, ALL_IN, WINSTREAK, LOSS_STREAK | Treinável — reward nativo | Aprender a converter reserva em força na fase tardia |
| `critical_hp_high_gold` | Estágio 3–7, HP até 30, ouro 50+ | ECON, STABILIZE, FAST8, ALL_IN, WINSTREAK, LOSS_STREAK | Treinável — reward nativo | Aprender quando comprar unidade, XP, roll ou passar sem presumir que XP é sempre correto |
| `low_hp_fast8_high_gold` | Estágio 3–7, FAST8, HP até 40, ouro 50+ | FAST8 | Monitor-only | Verificar trade-off entre XP e estabilização |
| `slowroll_gold_reserve` | Estágio 3–4, nível 6, ouro 50+, HP acima de 50 | SLOWROLL | Treinável/proteção | Penalizar BUY_XP para preservar a lógica de slowroll |
| `all_in_gold_hoarding` | Estágio 3–7, ouro 50+ | ALL_IN | Monitor-only | Investigar reservas incompatíveis com ALL_IN sem criar reward especulativo |
| `player8_all_in_gold_hoarding` | Estágio 3–7, jogador 8 (player_id 7), ouro 50+ | ALL_IN | Monitor-only | Isolar o caso específico do oitavo jogador observado na auditoria |
| `gold_above_50_any_strategy` | Qualquer estágio/nível/estratégia, ouro acima de 50 | Todas | Monitor-only | Medir BUY, BUY_XP, ROLL e PASS por contexto |
| `useful_shop_opportunity` | Ouro acima de 50 e candidatos de loja | Todas | Monitor-only | Aguardar contrato semântico confiável para identificar compra realmente útil |

| `core_sale_retention` | Estágio 3+, com banco e histórico de candidatos disponíveis na observação nativa | Todas | Treinável — reward nativo | Ajustar `sell_head` e `type_head` sem bloquear substituições legítimas |
| `bench_deployment_quality` | Estágio 2+, estado real do tabuleiro/banco | Todas | Treinável — reward nativo | Ajustar `bench_head` e `bench_to_board_head` |
| `carry_protection_positioning` | Estágio 3+, tabuleiro real e sinais de carry/frontline | Todas | Treinável — reward nativo | Ajustar `board_source_head` e `board_move_target_head` após unificação dos roles |
| `movement_no_progress` | Estágio 2+, movimentos de banco/tabuleiro avaliados pelo reward nativo | Todas | Treinável — reward nativo | Reduzir movimentos sem ganho sem punir reposicionamentos úteis |

## O que é treinado

O script seleciona um único cohort por execução. FAST8, economia tardia e HP
crítico usam exclusivamente o reward nativo da engine; o PPO apenas concentra
as atualizações nas transições daquele cenário. Não adicionamos um bônus
artificial de BUY_XP que pudesse fazer a IA ignorar uma oferta útil.

A única exceção é a proteção de SLOWROLL: recebe uma penalidade pequena e
contextual para BUY_XP no nível 6, com HP preservado e reserva acima de 50,
pois a estratégia deve continuar priorizando seus alvos de 3 estrelas.

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

## Sequência obrigatória de execução

1. `critical_hp_high_gold`
2. `late_game_high_gold_underleveled`
3. `s4_fast8_lvl6_gold60_hp_ok`
4. `s4_fast8_lvl6_gold80`
5. `s4_fast8_lvl7_gold60`
6. `slowroll_gold_reserve`
7. `core_sale_retention`
8. `bench_deployment_quality`
9. `carry_protection_positioning`
10. `movement_no_progress`

O arquivo local `chain_state.json` registra hashes de checkpoint, origem,
relatório e avaliação. Treino concluído fica com status `trained`, não libera
o próximo. Para liberar, a avaliação revisada deve ser salva em JSON com
`approved: true` e `checkpoint_sha256` igual ao hash do checkpoint treinado,
e então executada:

```powershell
.\\economy_finetuning\\approve_scenario.ps1 -Scenario critical_hp_high_gold -Evaluation .\\evaluation_critical_hp.json
```

Para cenários 2–10, o runner resolve automaticamente o checkpoint aprovado
do predecessor e ignora o checkpoint-base fornecido. Alterar um checkpoint
aprovado invalida a cadeia. Reexecutar um cenário também invalida todas as
aprovações posteriores.
