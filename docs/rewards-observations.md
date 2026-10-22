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
- um score de compatibilidade normalizado para cada slot do tabuleiro, banco e loja. O score considera unidade principal, direção da composição, core traits, estrelas e custo;
- os pesos de foco de composição, alinhados à mesma ordem fixa de traits e normalizados para [0, 1];
- o estado de bloqueio da composição (`composition_locked`), codificado como 0/1;
- a força da composição normalizada para [0, 1] a partir da escala nativa [0, 10].

Esses campos tornam a direção e a compatibilidade visíveis à policy, em vez de mantê-las apenas como metadados de diagnóstico. A implantação/substituição no tabuleiro recebe sinais pequenos e limitados relativos ao estado anterior: mudança de posicionamento, progresso de sinergia e diferença de compatibilidade em relação à unidade substituída ou à média do tabuleiro. O bônus por preencher uma vaga só é concedido quando há melhora de composição, sinergia ou posicionamento (ou quando a primeira unidade é implantada). Assim, uma ação que apenas ocupa uma vaga sem melhorar o estado não recebe um bônus automático, deixando espaço para o PPO aprender quando PASS é preferível. Esses sinais não substituem as recompensas de combate e colocação.

### Sinais econômicos e features por candidato

- A recompensa de cada ação inclui a diferença da potencialização do ouro antes/depois. O potencial combina um valor pequeno por ouro líquido com bônus nos patamares de 10 em 10 até 50, aproximando o benefício dos juros. É uma diferença entre estados, não um bônus repetido por ficar parado.
- Comprar recebe um sinal adicional pela melhoria marginal de compatibilidade quando já existe uma composição no tabuleiro, e por completar um upgrade quando há duas cópias compatíveis.
- Vender é avaliado pelo score de compatibilidade da unidade, se ela é core, se sua venda destrói uma possibilidade próxima de upgrade e se libera espaço no banco.
- Cada slot do banco e da loja agora expõe oito features próprias: compatibilidade, custo, estrelas, função, core, cópias existentes, traits compartilhadas e valor de venda/possibilidade de compra. Cabeças compartilhadas da policy pontuam cada slot com suas features locais.

A dimensão da observação mudou novamente com os pesos de foco, o bloqueio e a força da composição. O carregador atual pode migrar checkpoints compatíveis: as colunas novas do encoder global são inicializadas em zero e a cauda de candidatos é deslocada sem perder alinhamento. Isso preserva o comportamento inicial, mas **não significa que o checkpoint já aprendeu a usar as novas features**. Para validar o efeito, faça fine-tuning com o carregador de migração ou treine do zero; não compare métricas como se a arquitetura/observação fossem idênticas.

**Compatibilidade de checkpoints:** a dimensão mudou, mas `TFTPolicy.load_compatible_state_dict()` migra checkpoints que compartilham os mesmos nomes de parâmetros e diferem apenas pela inserção de features globais antes da cauda de candidatos. As novas colunas são inicializadas em zero; o checkpoint carrega, mas precisa de fine-tuning ou treinamento novo para aprender os sinais recém-adicionados.

## Terminação

A engine expõe dones individuais e `lobby_done`. Um jogador eliminado pode terminar seu episódio individual antes de a lobby inteira acabar. Quando a lobby termina, `LobbyVectorEnv` captura o estado terminal/ranking antes de reiniciar o ambiente, para não perder o resultado.

## Validação

- Confirmar shape e valores finitos das observações.
- Verificar a ordem de traits compartilhada por direção, core traits e pesos de foco.
- Verificar que `composition_locked` é 0/1 e a força está normalizada.
- Confirmar que as features por candidato continuam na cauda da observação.
- Comparar recompensas totais com a soma/semântica dos componentes.
- Verificar sinais terminais e colocação final.
- Ao mudar qualquer campo, revisar dimensões de policy, rollout e checkpoints.

Testes relacionados: `tests/test_action_dimensions.py`, `tests/test_full_match_terminal_ranking.py`, `tests/test_lobby_end_to_end.py` e testes C++ de reward.
