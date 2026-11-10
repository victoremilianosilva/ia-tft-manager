# Plano de fine-tuning por problema da auditoria 8b4be77

Este plano separa o que a policy consegue aprender do que precisa ser corrigido
na engine. Cada execução seleciona **um único cenário**. Não misturar cenários
econômicos, vendas e posicionamento no mesmo update PPO.

## Ordem proposta

| Ordem | Cenário | Evidência da auditoria | Cabeças a treinar | Fonte de recompensa | Situação |
|---:|---|---|---|---|---|
| 1 | `critical_hp_high_gold` | P4: 21→10 HP com 125→158 ouro e nível 6; P6: 22→5 HP, 91→113 ouro e nível 7; P7: 28 HP e 101+ ouro | `type_head` + `value_head` | Reward nativo | Selecionável no PS1 |
| 2 | `late_game_high_gold_underleveled` | P7: 5-1, nível 7, 94 ouro e 45 HP; continua abaixo do alvo de fase | `type_head` + `value_head` | Reward nativo | Selecionável no PS1 |
| 3 | `s4_fast8_lvl6_gold60_hp_ok` | FAST8 no estágio 4, nível 6, 60+ ouro e HP preservado | `type_head` + `value_head` | Reward nativo | Selecionável no PS1 |
| 4 | `s4_fast8_lvl6_gold80` | Caso de excedente mais severo no nível 6 | `type_head` + `value_head` | Reward nativo | Selecionável no PS1 |
| 5 | `s4_fast8_lvl7_gold60` | FAST8 no nível 7, com reserva suficiente para avaliar a progressão ao 8 | `type_head` + `value_head` | Reward nativo | Selecionável no PS1 |
| 6 | `slowroll_gold_reserve` | Proteção contra a correção de XP contaminar a janela de SLOWROLL | `type_head` + `value_head` | Shaping negativo pequeno apenas para BUY_XP | Selecionável no PS1 |
| 7 | `core_sale_retention` | 23 vendas core HIGH e 13 vendas de cópias de pares; P6 vende Master Yi/Kog'Maw em ALL_IN | `type_head` + `sell_head` + `value_head` | Reward nativo de venda | Implementado; aguarda experimento e aprovação |
| 8 | `bench_deployment_quality` | Tabuleiros subocupados/estruturalmente fracos e unidades úteis não implantadas | `type_head` + `bench_head` + `bench_to_board_head` + `value_head` | Reward nativo de implantação e melhoria estrutural | Implementado; aguarda experimento e aprovação |
| 9 | `carry_protection_positioning` | Carry exposto, frontline frágil/isolada e warnings de posicionamento | `type_head` + `board_source_head` + `board_move_target_head` + `value_head` | Reward nativo de BoardEvaluation | Implementado após alinhar classificação de roles; aguarda experimento |
| 10 | `movement_no_progress` | P4: 76 movimentos (MOVE_BENCH -0,042; MOVE_BOARD -0,008); P6: 76; P7: 87 | `type_head` + heads condicionais de movimento | Reward nativo de movimento/BoardEvaluation | Implementado; aguarda experimento e aprovação |

Os dez cenários são opções do runner PowerShell. A cadeia exige aprovação explícita após cada avaliação; a simples conclusão do treino não libera a etapa seguinte. Os quatro cenários estratégicos usam rewards nativos e liberam somente as cabeças condicionais pertinentes.

## Por que a economia pode ser aprendida sem alterar a engine

O caminho atual já contém os sinais necessários:

- `ActionMaskEngine` habilita `BUY_XP` quando o nível está abaixo do máximo e
  existe ouro suficiente. Portanto, a legalidade não explica o caso P4.
- A observação contém HP, ouro, nível, round e estratégia.
- `policy.py::_economic_context_features` deriva alvo de nível, déficit,
  reserva, ouro disponível e pressão de fase.
- `TftEngine.cpp` calcula reward de XP por transição de nível, progresso de
  fase, excedente, estratégia e oportunidade de compra útil.
- `PASS` recebe penalidade quando há oportunidade de XP ou compra útil; o
  reward é entregue à transição nativa.

Por isso, nos cenários FAST8, late game e HP crítico, a proposta é **não somar
outro bônus artificial para XP**. O PPO será treinado somente com transições
do cenário selecionado e usará o reward nativo, que já distingue compra útil,
XP, roll e PASS. Isso evita ensinar XP quando a loja contém uma peça melhor.

O cenário SLOWROLL é a exceção: tem uma penalidade pequena e restrita a BUY_XP
no nível 6, com HP preservado e reserva acima de 50, pois a estratégia deve
continuar priorizando seus alvos de 3 estrelas.

## Core e pares: treinável, mas precisa de outra cabeça

A policy tem um `sell_head` separado. O vetor de cada unidade do banco já
inclui composição-fit, custo, estrelas, role, flag core/planned, cópias,
força do caminho de upgrade e valor de venda. Isso dá ao modelo informação
suficiente para aprender qual unidade não deve ser vendida.

A engine também já aplica `sale_quality`, `critical_all_in_sale_penalty` e
penalidade de caminho de upgrade. O problema não é ausência de sinal de reward:
a máscara ainda permite vender qualquer unidade ocupada do banco e o fine-tuning
econômico atual não treina `sell_head`.

O treino 7 deve usar o reward nativo e atualizar `sell_head`; `type_head`
entra para aprender a evitar SELL quando não existe descarte seguro. Se ainda
houver vendas core após esse experimento, aí implementaremos uma proteção
condicional no gerador de máscaras e na validação de execução. Não quero
bloquear vendas legítimas de substituição.

## Composição/foco: precisa de código novo, não PPO

A direção da composição possui `CompositionDirectionPolicy` com lock,
vantagem mínima e persistência de candidato. O foco não possui a mesma proteção:

- `update_strategy()` limpa e recalcula `composition_focus` a cada atualização;
- os pesos de foco sofrem decay e recebem ganhos novamente a cada atualização;
- `core_unit_ids` são reconstruídos a partir dos três maiores `focus_scores`
  sem uma política de candidato/confirmado equivalente à da direção.

O plano de composição já tem alguma histerese via
`should_replace_composition_plan()`. Esta PR agora preserva o foco enquanto a
unidade continua owned/viável e só troca quando uma alternativa supera o score
anterior por pelo menos 20% + 0,5 ponto. Os core IDs anteriores são retidos e
preenchem primeiro as vagas; unidades novas só entram para preencher vagas
livres. Isso reduz churn sem impedir substituições quando a peça sai do banco/tabuleiro.

## Posicionamento: precisa alinhar a representação antes do PPO

Há um descompasso concreto:

- `board_evaluation()` classifica unidades com
  `UnitCombatClassifier::classify()`, usando range, stats, habilidade, itens e
  carry planejado.
- A observação do PPO e o vetor de candidatos usam
  `def.combat_profile.role` diretamente.
- Os perfis do banco enviados ao `BoardEvaluation` também usam o role base.

Assim, o avaliador/reward pode tratar uma unidade como carry enquanto a policy
recebe a feature de fighter (ou outra role base). O modelo pode ser penalizado
por uma formação que, segundo a própria entrada, parecia correta.

A observação de tabuleiro, banco, loja e candidatos agora usa o mesmo
`UnitCombatClassifier` do `BoardEvaluation`; os perfis de banco enviados ao
avaliador também usam a classificação efetiva. O cenário de carry/posicionamento
pode, portanto, ser treinado com representação consistente. O cenário 8 deve vir antes:
um tabuleiro com poucos campeões ou sem unidades úteis implantadas não se
resolve movendo posições. O cenário 10 mede eficiência de movimento: não
penaliza uma troca isolada útil, mas ensina a policy a evitar sequências cujo
delta líquido de estrutura/posição não melhora o tabuleiro.

Também é necessário separar na auditoria `positional_score`,
`structural_score`, `exposed_main_carry_count`,
`missing_frontline_count`, `missing_backline_count` e
`isolated_frontline_count`. Hoje o snapshot público expõe só parte dessas
contagens. Além disso, `board_power()` é apenas
`sum(cost * star * 2)`, uma proxy de investimento/qualidade, não poder real de
combate. E `positioning_score()` retorna `BoardEvaluation.total_score`
(posicional + estrutural), não apenas posicionamento puro. Os 255 warnings
textuais não são 255 decisões independentes.

## Auditoria: correção de ferramenta, não treinamento

- Rotular como registros os 3.886 eventos ativos, e contar decisões apenas
  quando há uma ação estruturada válida.
- Mostrar cobertura de validação completa: 1.436/1.524 = **94,2%**; 88 ações
  ficam explicitamente como não verificadas. Zero falhas não significa 100%
  de cobertura.
- Entregar sidecars ou um pacote reproduzível com checksums; não depender de
  arquivos locais ausentes do commit.
- Registrar checkpoint SHA, commit da engine, commit do trainer, run ID,
  configuração PPO, versão/hash do reward e versão do catálogo.
- Separar mudanças de direção, foco de trait, foco de unidade, core IDs,
  main carry e plano de oito unidades.

## Regras comuns de aprovação

1. Executar shadow comparison no mesmo estado e mesmas máscaras.
2. Exigir amostra mínima do cenário; zero ocorrências ou zero optimizer steps
   significa **não treinado**, nunca sucesso.
3. Comparar distribuição e argumentos das cabeças realmente treinadas.
4. Auditar todas as estratégias fora do cohort-alvo.
5. Executar partidas completas pareadas em seeds de validação não usadas no
   treino, comparar colocação, HP, nível, ouro, força/estrutura e decisões.
6. Não promover nem encadear o próximo fine-tuning sem aprovação explícita do
   cenário atual.


## Implementação nesta revisão

- Cadeia de 10 cenários em `chain_manager.py`: predecessor aprovado obrigatório,
  hash SHA-256 do checkpoint, hash de origem, relatório de treino e avaliação
  vinculada ao checkpoint. Reexecução invalida as etapas posteriores.
- `approve_scenario.ps1` libera explicitamente a próxima etapa depois que a
  avaliação revisada fornece `approved: true` e o hash correto.
- Fine-tuning libera apenas as cabeças do cenário selecionado; encoder e heads
  não relacionados permanecem congelados.
- `-Device auto|cpu|cuda` agora é respeitado; CUDA solicitado sem suporte falha
  explicitamente em vez de cair silenciosamente para CPU.
- Engine C++ estabiliza foco/core e alinha roles de observação com
  `UnitCombatClassifier`/BoardEvaluation.
- A implementação ainda precisa passar pela CI/build C++ e pelos testes Python
  completos antes de qualquer treino experimental.
