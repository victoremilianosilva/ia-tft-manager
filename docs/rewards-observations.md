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

### Estado semântico de itens e condicionamento de alvos

A cauda de candidatos continua reservada às features de banco/loja. Imediatamente antes dela, a engine agora expõe um bloco de itens com:
- contagem normalizada dos dez primeiros componentes do catálogo ativo;
- atributos de combate, pesos de função e indicador de emblema para cada um dos nove slots de itens completos na bag;
- atributos dos itens produzidos pelas receitas, indexados pelo par ordenado de componentes;
- perfil de cada um dos 37 alvos possíveis (28 posições do tabuleiro e nove do banco), incluindo localização, estrelas, função, linha, compatibilidade com a composição, atributos básicos e slots de item ocupados;
- matrizes de compatibilidade item/alvo para os nove itens completos na bag e para os 100 resultados de receita, cada um comparado com os 37 alvos. As receitas só recebem compatibilidade não-zero quando o par de componentes está disponível para craft naquele estado.

A policy mantém as cabeças categóricas existentes, mas soma scores compartilhados por candidato para inventário, opções de bigorna, componentes e alvo. A cabeça de inventário usa features da bag em equipagem normal e features específicas das opções quando há bigorna pendente. O score de alvo combina atributos do item/receita, perfil da unidade e a compatibilidade calculada pela engine; assim, a seleção deixa de depender apenas do índice do slot. Os scores auxiliares começam zerados para preservar os logits de checkpoints antigos durante a migração. O bloco bruto acrescenta 6.562 floats à observação nativa; 2.529 features semânticas entram no global encoder e as 4.033 compatibilidades ficam fora dele, alimentando somente o scorer autorregressivo do alvo. Checkpoints antigos carregam com colunas e cabeças auxiliares neutras, mas precisam de fine-tuning para aprender essas relações.

A compatibilidade de emblemas compara o ID estável do item com os nomes canônicos dos traits, removendo o prefixo do set, e favorece traits planejadas/ativas que o campeão ainda não possui. Não concede o mesmo bônus genérico a qualquer emblema.

A auditoria nativa também registra catálogo ordenado de componentes, estado/opções de bigorna e a última decisão de item: operação, item/receita, UUID e localização do alvo, compatibilidade estimada, força imediata estimada, alinhamento de função e reward de atribuição. A escolha de bigorna é identificada como concessão de opção, não como equipamento. Esses campos são diagnósticos e não alteram a recompensa nem a legalidade das ações.

### Sinais econômicos e features por candidato

A policy deriva cinco features econômicas determinísticas dos campos nativos já presentes na observação (ouro, HP, nível, rodada e one-hot da estratégia): nível-alvo da fase/plano, distância até o alvo, reserva mínima dinâmica, ouro disponível acima dessa reserva e pressão de progressão. Elas são inseridas no encoder global imediatamente antes da cauda de candidatos. Assim, a policy e o value head recebem explicitamente o contexto econômico; a amostragem e o replay PPO usam a mesma derivação, sem alterar o contrato do vetor C++.

A reserva deixa de ser fixa em 50: fases iniciais preservam mais liquidez, enquanto as fases 3+ reduzem progressivamente a reserva (e FAST8 pode gastar para alcançar o nível 8). SLOWROLL mantém uma reserva própria para rolagem. HP crítico e ALL_IN podem reduzir a reserva a zero. Checkpoints anteriores migram com as cinco colunas novas inicializadas em zero; fine-tuning continua necessário para aprender a utilizá-las.



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
