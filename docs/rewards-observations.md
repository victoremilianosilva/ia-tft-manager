# Recompensas e observações

## Recompensas

A engine retorna uma recompensa total por jogador e mantém componentes separados para auditoria: recompensa da ação, combate e colocação. A estrutura `RewardState` guarda referências anteriores (poder do tabuleiro, posicionamento, sinergia, nível e ouro), além da recompensa de combate/rodada/acumulada.

`RewardManager` reúne sinais como resultado do combate, mudanças de poder, sinergias, posicionamento, nível, economia, sequência, preenchimento do tabuleiro e sucesso da ação. `RewardModel.hpp` contém funções-modelo adicionais usadas pela implementação. A fórmula exata e os pesos devem ser consultados no código C++ antes de alterar o sinal de treino.

## Observações

A engine gera observações por jogador e informa `observation_dim()`; o wrapper converte o vetor de retorno para `numpy.float32`. O treinador verifica a forma `(num_lobbies, 8, obs_dim)` antes de achatar o batch para `(num_lobbies * 8, obs_dim)`.

A observação de treino não é igual ao snapshot de auditoria. O snapshot pode conter tabuleiro, banco, loja, máscaras e informações de diagnóstico que não fazem parte do vetor observado pela policy.

A observação PPO inclui, após os campos anteriores:
- um vetor one-hot da direção atual da composição, na ordem fixa de traits do catálogo;
- um vetor binário indicando as core traits;
- um score de compatibilidade normalizado para cada slot do tabuleiro, banco e loja. O score considera unidade principal, direção da composição, core traits, estrelas e custo.

Esses campos tornam a direção e a compatibilidade visíveis à policy, em vez de mantê-las apenas como metadados de diagnóstico. A implantação/substituição no tabuleiro recebe sinais pequenos e limitados relativos ao estado anterior: mudança de posicionamento, progresso de sinergia e diferença de compatibilidade em relação à unidade substituída ou à média do tabuleiro. O bônus por preencher uma vaga só é concedido quando há melhora de composição, sinergia ou posicionamento (ou quando a primeira unidade é implantada). Assim, uma ação que apenas ocupa uma vaga sem melhorar o estado não recebe um bônus automático, deixando espaço para o PPO aprender quando PASS é preferível. Esses sinais não substituem as recompensas de combate e colocação.

### Sinais econômicos e features por candidato

- A recompensa de cada ação inclui a diferença da potencialização do ouro antes/depois. O potencial combina um valor pequeno por ouro líquido com bônus nos patamares de 10 em 10 até 50, aproximando o benefício dos juros. É uma diferença entre estados, não um bônus repetido por ficar parado.
- Comprar recebe um sinal adicional pela melhoria marginal de compatibilidade quando já existe uma composição no tabuleiro, e por completar um upgrade quando há duas cópias compatíveis.
- Vender é avaliado pelo score de compatibilidade da unidade, se ela é core, se sua venda destrói uma possibilidade próxima de upgrade e se libera espaço no banco.
- Cada slot do banco e da loja agora expõe oito features próprias: compatibilidade, custo, estrelas, função, core, cópias existentes, traits compartilhadas e valor de venda/possibilidade de compra. Cabeças compartilhadas da policy pontuam cada slot com suas features locais.

A dimensão da observação e a arquitetura da policy mudaram. Checkpoints anteriores não são compatíveis: é necessário treinar um checkpoint novo antes de usar o auditor estratégico.

**Compatibilidade de checkpoints:** a dimensão da observação mudou. Checkpoints treinados antes desta alteração têm uma primeira camada com dimensão incompatível e não devem ser carregados como se fossem compatíveis. Inicie um novo treinamento ou implemente uma migração explícita de pesos antes de reutilizar checkpoints antigos.

## Terminação

A engine expõe dones individuais e `lobby_done`. Um jogador eliminado pode terminar seu episódio individual antes de a lobby inteira acabar. Quando a lobby termina, `LobbyVectorEnv` captura o estado terminal/ranking antes de reiniciar o ambiente, para não perder o resultado.

## Validação

- Confirmar shape e valores finitos das observações.
- Comparar recompensas totais com a soma/semântica dos componentes.
- Verificar sinais terminais e colocação final.
- Ao mudar qualquer campo, revisar dimensões de policy, rollout e checkpoints.

Testes relacionados: `tests/test_action_dimensions.py`, `tests/test_full_match_terminal_ranking.py`, `tests/test_lobby_end_to_end.py` e testes C++ de reward.
