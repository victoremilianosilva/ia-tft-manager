# Fase 3 — Migração das regras de origem e destino no tabuleiro

## 1. Objetivo

Migrar para C++ as regras de validação de origem e destino dos movimentos entre posições do tabuleiro, preservando o comportamento da implementação Python existente em `ai/ActionMaskManager.py`.

A migração deve preparar o validador nativo para ser utilizado futuramente pelo módulo `decision_engine`, sem alterar o formato das ações, a arquitetura da política PPO ou o fluxo atual de treinamento.

## 2. Implementação de referência

Arquivo Python: `ai/ActionMaskManager.py`

Método principal: `_is_valid_board_move(source, target, board=None)`.

O método recebe os índices da posição de origem e de destino e, opcionalmente, o estado do tabuleiro.

Quando o tabuleiro não é fornecido explicitamente, o método utiliza o estado retornado por `_get_board()`.

## 3. Regras de validação identificadas

### 3.1. Validação dos limites

A origem e o destino precisam estar dentro dos limites do tabuleiro recebido.

- Origem negativa: movimento inválido.
- Origem fora dos limites: movimento inválido.
- Destino negativo: movimento inválido.
- Destino fora dos limites: movimento inválido.

A implementação deve considerar o tamanho real do tabuleiro utilizado na validação, sem depender exclusivamente da constante de 28 posições.

### 3.2. Origem e destino iguais

Um movimento cuja origem e destino sejam a mesma posição deve ser rejeitado.

Essa regra impede que a ação seja considerada uma movimentação real quando nenhuma posição seria alterada.

### 3.3. Origem vazia

A origem precisa conter uma unidade.

Se a posição de origem estiver vazia, o movimento será inválido, independentemente da ocupação do destino.

### 3.4. Destino ocupado

Quando o destino contém uma unidade, o movimento é classificado como uma troca entre unidades (`board_swap`).

A troca é permitida pelo validador básico, desde que não seja bloqueada pelo `AntiLoopManager`.

### 3.5. Destino vazio

Quando o destino está vazio, o movimento é classificado como uma movimentação para uma posição vazia (`board_move`).

O movimento é permitido pelo validador básico, desde que não seja bloqueado pelo `AntiLoopManager`.

## 4. Integração com o AntiLoop

A validação de movimentos está integrada ao método `_should_block_anti_loop()`.

O método encaminha ao `AntiLoopManager`:

- Tipo do movimento (`board_move` ou `board_swap`).
- Índice de origem.
- Índice de destino.
- Unidade movimentada.

A identidade da unidade deve ser preservada na migração. Não basta enviar somente os índices das posições, pois o histórico anti-loop pode utilizar informações da unidade para distinguir movimentos.

Na implementação Python atual, uma exceção durante a consulta ao AntiLoop é registrada e o candidato não é bloqueado por essa consulta. A implementação nativa deve preservar a semântica acordada para falhas, com diagnóstico adequado.

A migração das regras internas do AntiLoop é uma etapa separada e não faz parte do escopo desta tarefa.

## 5. Proposta de implementação em C++

O validador nativo deverá receber:

- Origem do movimento.
- Destino do movimento.
- Representação do tabuleiro.
- Informações suficientes para identificar a unidade de origem.
- Uma interface de consulta ao AntiLoop, ou uma integração equivalente definida pelo contrato do `decision_engine`.

O resultado deverá indicar se o movimento é válido e, quando aplicável, distinguir uma movimentação para posição vazia de uma troca entre unidades.

A interface final deverá seguir as estruturas e convenções já existentes no módulo C++, evitando criar tipos duplicados ou incompatíveis.

## 6. Restrições de implementação

A implementação deverá:

1. Preservar a semântica das verificações do Python.
2. Não modificar o estado real do tabuleiro durante a validação.
3. Não movimentar, remover ou trocar unidades.
4. Não atualizar indevidamente o histórico do AntiLoop.
5. Preservar a identidade da unidade consultada.
6. Não alterar as dimensões ou a semântica do espaço de ações da PPO.
7. Manter a implementação Python disponível como referência e fallback.
8. Respeitar a estrutura real do projeto e as convenções do módulo `decision_engine`.

## 7. Plano de testes

### Casos básicos

- Origem negativa.
- Origem fora dos limites.
- Destino negativo.
- Destino fora dos limites.
- Origem igual ao destino.
- Origem vazia.
- Origem ocupada e destino vazio.
- Origem ocupada e destino ocupado.

### Casos envolvendo AntiLoop

- Movimento para posição vazia não bloqueado.
- Movimento para posição vazia bloqueado.
- Troca entre unidades não bloqueada.
- Troca entre unidades bloqueada.
- Identidade da unidade encaminhada corretamente.
- Falha na consulta ao AntiLoop tratada conforme o contrato definido.

### Testes de equivalência

Para cada cenário, executar o validador Python e o C++ com estados equivalentes e comparar os resultados.

Qualquer divergência deve ser investigada antes da integração ao fluxo principal.

### Teste de ausência de efeitos colaterais

Registrar o estado do tabuleiro e do histórico antes da validação e verificar que a consulta não introduziu alterações indevidas.

## 8. Critérios de conclusão

A tarefa somente poderá ser marcada como concluída quando:

- [ ] A implementação nativa estiver integrada à estrutura real do projeto.
- [ ] As regras de origem e destino estiverem reproduzidas.
- [ ] A identidade da unidade estiver preservada.
- [ ] A interação com o AntiLoop estiver definida e validada.
- [ ] Os testes unitários de casos válidos e inválidos estiverem implementados.
- [ ] Os testes diferenciais Python/C++ estiverem aprovados.
- [ ] A validação não alterar indevidamente o estado do jogo.
- [ ] Os testes de regressão relevantes estiverem aprovados.
- [ ] A implementação Python continuar disponível.

## 9. Situação atual

**Status: pendente de implementação e validação.**

As regras da implementação Python foram identificadas e documentadas. A estrutura definitiva do código C++ e sua integração ainda precisam ser confirmadas no repositório.

Esta documentação não representa uma declaração de conclusão da tarefa. O item do roadmap deverá permanecer pendente até que os critérios de aceitação sejam cumpridos.
