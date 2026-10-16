# Recompensas e observações

## Recompensas

A engine retorna uma recompensa total por jogador e mantém componentes separados para auditoria: recompensa da ação, combate e colocação. A estrutura `RewardState` guarda referências anteriores (poder do tabuleiro, posicionamento, sinergia, nível e ouro), além da recompensa de combate/rodada/acumulada.

`RewardManager` reúne sinais como resultado do combate, mudanças de poder, sinergias, posicionamento, nível, economia, sequência, preenchimento do tabuleiro e sucesso da ação. `RewardModel.hpp` contém funções-modelo adicionais usadas pela implementação. A fórmula exata e os pesos devem ser consultados no código C++ antes de alterar o sinal de treino.

## Observações

A engine gera observações por jogador e informa `observation_dim()`; o wrapper converte o vetor de retorno para `numpy.float32`. O treinador verifica a forma `(num_lobbies, 8, obs_dim)` antes de achatar o batch para `(num_lobbies * 8, obs_dim)`.

A observação de treino não é igual ao snapshot de auditoria. O snapshot pode conter tabuleiro, banco, loja, máscaras e informações de diagnóstico que não fazem parte do vetor observado pela policy. Não usar dados de auditoria como entrada da policy sem uma mudança intencional do contrato e dos checkpoints.

## Terminação

A engine expõe dones individuais e `lobby_done`. Um jogador eliminado pode terminar seu episódio individual antes de a lobby inteira acabar. Quando a lobby termina, `LobbyVectorEnv` captura o estado terminal/ranking antes de reiniciar o ambiente, para não perder o resultado.

## Validação

- Confirmar shape e valores finitos das observações.
- Comparar recompensas totais com a soma/semântica dos componentes.
- Verificar sinais terminais e colocação final.
- Ao mudar qualquer campo, revisar dimensões de policy, rollout e checkpoints.

Testes relacionados: `tests/test_action_dimensions.py`, `tests/test_full_match_terminal_ranking.py`, `tests/test_lobby_end_to_end.py` e testes C++ de reward.
