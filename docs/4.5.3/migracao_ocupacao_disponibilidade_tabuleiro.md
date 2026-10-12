# Fase 3 — Migração das regras de ocupação e disponibilidade de posições

## 1. Objetivo

Migrar para C++ as regras estruturais de ocupação e disponibilidade de posições do tabuleiro, mantendo o comportamento do ambiente Python e a compatibilidade com o contrato atual de ações do PPO.

A implementação deve permitir consultar a disponibilidade de uma posição e validar movimentos sem modificar o estado do jogo.

## 2. Arquivos envolvidos

- `cpp/include/decision/MoveValidator.hpp`
- `cpp/src/decision/MoveValidator.cpp`
- `cpp/tests/test_move_validator.cpp`
- `cpp/CMakeLists.txt`

## 3. Regras de validação

### 3.1. Disponibilidade de posição

Uma posição está disponível quando:

- Seu índice pertence ao intervalo válido da sequência recebida.
- A posição não contém uma unidade.

Índices negativos e índices iguais ou superiores ao tamanho real da sequência são inválidos.

### 3.2. Movimento dentro do tabuleiro

Um movimento é estruturalmente válido quando:

- A origem e o destino são válidos.
- Origem e destino são diferentes.
- A origem contém uma unidade.

O tipo de movimento é determinado pela ocupação do destino:

- `BOARD_MOVE`: destino vazio.
- `BOARD_SWAP`: destino ocupado.

A validação não executa o movimento nem realiza a troca.

### 3.3. Movimento do banco para o tabuleiro

Um movimento é estruturalmente válido quando:

- O slot do banco existe e contém uma unidade.
- O destino pertence ao tabuleiro recebido.
- O destino está vazio.

Diferentemente de um movimento dentro do tabuleiro, uma posição ocupada não pode ser aceita como destino de uma movimentação do banco.

### 3.4. Tabuleiro cheio

A consulta de disponibilidade deve retornar falso quando todas as posições estão ocupadas.

Um tabuleiro vazio ou parcialmente ocupado deve ser avaliado conforme seu estado real, sem pressupor que toda entrada contém exatamente 28 posições.

## 4. Integração com o AntiLoop

O validador estrutural não substitui o `AntiLoopManager`.

A validação estrutural determina se o movimento respeita as regras de origem, destino e ocupação. O AntiLoop continua responsável por avaliar se o movimento deve ser bloqueado devido ao histórico.

A integração completa deverá preservar a distinção entre:

1. Movimento estruturalmente inválido.
2. Movimento estruturalmente válido, mas bloqueado pelo AntiLoop.
3. Movimento liberado para execução.

## 5. Imutabilidade do estado

As funções de validação devem ser somente de leitura.

Elas não podem:

- Mover unidades.
- Trocar unidades de posição.
- Remover ou adicionar unidades.
- Alterar a identidade das unidades.
- Atualizar o histórico de movimentos.
- Alterar contadores de execução.

## 6. Testes previstos

O teste nativo deve verificar:

- Posição vazia e disponível.
- Posição ocupada e indisponível.
- Tabuleiro completamente ocupado.
- Índices negativos e fora dos limites.
- Origem vazia.
- Origem e destino iguais.
- Movimento para destino vazio.
- Troca com destino ocupado.
- Movimento do banco para destino vazio.
- Rejeição de destino ocupado no movimento banco → tabuleiro.
- Preservação das unidades e do estado durante a validação.

Após a implementação, os resultados deverão ser comparados com o comportamento de referência do Python nos mesmos cenários.

## 7. Critérios de aceitação

- [ ] Implementação nativa compilada.
- [ ] Testes nativos executados com sucesso.
- [ ] Semântica comparada com o Python.
- [ ] Identidade das unidades preservada.
- [ ] Nenhuma alteração de estado durante a validação.
- [ ] Integração com AntiLoop verificada.
- [ ] Testes de regressão executados.
- [ ] Compatibilidade com as dimensões de ação do PPO preservada.

## 8. Status

**Pendente de aplicação, compilação e validação.**

A implementação proposta e os testes foram preparados para revisão, mas ainda não foram aplicados ao repositório nem executados no ambiente do projeto. A equivalência com o Python e a integração com o AntiLoop também precisam ser confirmadas antes de considerar a tarefa concluída.