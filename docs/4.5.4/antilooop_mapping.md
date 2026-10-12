# Mapeamento do AntiLoopManager

**Projeto:** TFT AI  
**Arquivo de referência:** `ai/AntiLoopManager.py`  
**Objetivo:** documentar a API, as responsabilidades, o estado interno e as dependências da implementação Python antes da migração para C++.

## 1. Inventário de métodos

### 1.1. Inicialização e histórico

| Método | Responsabilidade |
|---|---|
| `__init__(history_size=20, blocked_move_size=10, loop_threshold=2)` | Inicializa configurações, métricas e histórico. |
| `reset()` | Limpa o histórico e os estados rastreados sem zerar as métricas acumuladas. |
| `register_state(board, bench=None)` | Registra a assinatura do estado e contabiliza visitas. |
| `register_move(move_type, source, target, unit=None)` | Registra um movimento e atualiza `last_move`. |

### 1.2. Identidade e assinaturas

| Método | Responsabilidade |
|---|---|
| `make_board_signature(board, bench=None)` | Gera uma assinatura do tabuleiro e do banco. |
| `_unit_identity(unit)` | Retorna a identidade estável da unidade, priorizando UUID e usando `id` e `star` como alternativa. |
| `make_move_key(move_type, source, target, unit=None)` | Gera uma chave de identificação do movimento. |

### 1.3. Bloqueios e detecção de ciclos

| Método | Responsabilidade |
|---|---|
| `block_move(move_type, source, target, unit=None)` | Registra o bloqueio de um movimento no estado atual. |
| `is_move_blocked(move_type, source, target, unit=None)` | Verifica se o movimento continua bloqueado na assinatura de estado atual. |
| `is_reverse_move(move_type, source, target, unit=None)` | Detecta movimentos inversos, com tratamento específico para `board_swap`. |
| `is_oscillating(unit, source, target, move_type=None)` | Detecta oscilações na sequência recente de movimentos. |
| `is_bench_board_loop(unit, move_type=None, source=None, target=None)` | Detecta repetição de transições entre banco e tabuleiro. |
| `is_cycle_move(move_type, source, target, unit=None)` | Detecta ciclos persistentes de movimentação no tabuleiro. |
| `get_block_reason(move_type, source, target, unit=None)` | Retorna o motivo do bloqueio ou `None`. |
| `should_block_move(move_type, source, target, unit=None, board=None, bench=None)` | Retorna se o movimento deve ser bloqueado. |
| `evaluate_move_risk(move_type, source, target, unit=None)` | Calcula um risco entre `0.0` e `1.0`. |

### 1.4. Consulta de estados e manutenção

| Método | Responsabilidade |
|---|---|
| `was_state_seen(board, bench=None)` | Verifica se o estado já foi registrado. |
| `get_state_visits(board, bench=None)` | Retorna o número de visitas ao estado. |
| `clear_old_blocks()` | Remove bloqueios antigos caso o limite seja excedido. |
| `get_state()` | Retorna um resumo do histórico e do último movimento. |

### 1.5. Métricas e depuração

| Método | Responsabilidade |
|---|---|
| `record_execution_attempt()` | Incrementa o contador de tentativas reais. |
| `record_execution_block(reason)` | Registra um bloqueio ocorrido durante a execução. |
| `record_successful_move(move_type)` | Conta movimentos executados com sucesso. |
| `get_metrics()` | Retorna uma cópia das métricas. |
| `debug_print()` | Exibe informações internas para depuração. |

## 2. Estado interno

| Atributo | Finalidade |
|---|---|
| `history_size` | Limite dos históricos de estados e movimentos. |
| `blocked_move_size` | Limite do histórico de bloqueios. |
| `loop_threshold` | Quantidade de visitas necessária para marcar um estado como repetido. |
| `execution_metrics` | Contadores acumulados de tentativas, bloqueios e movimentos executados. |
| `position_history` | Histórico limitado de assinaturas dos estados. |
| `move_history` | Histórico limitado de movimentos. |
| `blocked_moves` | Coleção limitada de movimentos bloqueados. |
| `blocked_move_states` | Associação entre cada movimento bloqueado e a assinatura de estado correspondente. |
| `state_visits` | Contagem de visitas por assinatura. |
| `last_board_signature` | Última assinatura registrada. |
| `last_move` | Último movimento registrado. |

## 3. Dependências lógicas

A sequência principal de decisões é:

1. `_unit_identity()` fornece a identidade usada pelas assinaturas e chaves.
2. `make_board_signature()` representa o estado do tabuleiro e do banco.
3. `register_state()` registra estados e contabiliza visitas.
4. `register_move()` mantém o histórico de movimentos.
5. `is_move_blocked()`, `is_reverse_move()`, `is_oscillating()`, `is_bench_board_loop()` e `is_cycle_move()` analisam candidatos.
6. `get_block_reason()` consolida os detectores.
7. `should_block_move()` transforma a existência de um motivo em uma decisão booleana.
8. `evaluate_move_risk()` calcula uma pontuação usando bloqueios e detectores.

## 4. Regras que precisam ser preservadas em C++

- A identidade deve priorizar UUID e usar `id` e `star` quando não houver UUID.
- As assinaturas precisam considerar tanto o tabuleiro quanto o banco.
- Os históricos limitados devem reproduzir o comportamento dos `deque` com `maxlen`.
- Os bloqueios devem estar vinculados à assinatura de estado na qual foram registrados.
- `board_swap` possui regras próprias para detectar movimentos inversos e oscilações.
- Os movimentos entre banco e tabuleiro aceitam aliases diferentes para o tipo de movimento.
- `get_block_reason()` e `should_block_move()` devem continuar sendo consultas sem efeitos colaterais.
- `reset()` deve limpar o histórico sem zerar `execution_metrics`.
- A ordem e os critérios dos detectores devem ser preservados, pois determinam o motivo retornado.
- A pontuação de `evaluate_move_risk()` deve manter os pesos e o limite de `1.0`.

## 5. Observações de implementação

- `should_block_move()` recebe `board` e `bench`, mas atualmente não os utiliza diretamente.
- `clear_old_blocks()` trabalha em conjunto com uma coleção que já tem limite automático; seu comportamento deve ser preservado e testado.
- `get_metrics()` retorna uma cópia do dicionário para evitar que o chamador altere diretamente os contadores internos.
- O inventário identifica a API por convenção de nomenclatura Python; não significa que todos os métodos precisem ser expostos publicamente na interface C++.

## 6. Critério de conclusão do mapeamento

Considera-se concluído quando os métodos, seus parâmetros, suas responsabilidades, os atributos internos e as dependências relevantes estiverem documentados para orientar a migração.

**Status:** concluído — documentação de referência para a próxima etapa.

**Próxima tarefa sugerida:** mapear os atributos de estado e as estruturas de dados C++ equivalentes antes de iniciar a implementação.
