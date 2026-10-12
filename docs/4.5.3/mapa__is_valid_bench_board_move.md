# Mapeamento de `_is_valid_bench_board_move()`

## 1. Objetivo

O método `_is_valid_bench_board_move()` verifica se uma unidade do banco (`bench`) pode ser movida para uma posição do tabuleiro (`board`).

Além das condições básicas de origem e destino, ele consulta o `AntiLoopManager` para impedir movimentos bloqueados pelas regras anti-loop.

**Assinatura atual:**

```python
def _is_valid_bench_board_move(self, bench_slot, target, bench=None):
```

Parâmetros:

- `bench_slot`: índice da unidade no banco.
- `target`: posição de destino no tabuleiro.
- `bench`: banco opcional recebido pelo chamador. Quando não informado, o método obtém o banco atual por meio de `_get_bench()`.

## 2. Implementação atual

```python
def _is_valid_bench_board_move(self, bench_slot, target, bench=None):
    if bench is None:
        bench = self._get_bench()

    if bench_slot < 0 or bench_slot >= len(bench):
        return False

    unit = bench[bench_slot]

    if unit is None:
        return False

    if not self._is_valid_board_position(target):
        return False

    if self._should_block_anti_loop(
        move_type="bench_to_board",
        source=bench_slot,
        target=target,
        unit=unit,
    ):
        return False

    return True
```

## 3. Condições de validação

| Ordem | Condição | Resultado |
|---|---|---|
| 1 | `bench` não foi informado | Obtém o banco atual por `_get_bench()`. |
| 2 | `bench_slot < 0` ou `bench_slot >= len(bench)` | Retorna `False`. |
| 3 | A posição de origem contém `None` | Retorna `False`. |
| 4 | `_is_valid_board_position(target)` retorna `False` | Retorna `False`. |
| 5 | `_should_block_anti_loop(...)` retorna `True` | Retorna `False`. |
| 6 | Nenhuma condição anterior bloqueou o movimento | Retorna `True`. |

### 3.1. Banco de origem

Se o argumento `bench` não for fornecido, o método usa `_get_bench()`. Esse helper retorna `bench_manager.bench` ou uma lista de nove posições vazias quando o atributo não está disponível.

O índice é validado contra `len(bench)`, e não diretamente contra `self.bench_size`.

Isso significa que o método aceita qualquer índice válido na lista recebida, mesmo que ela tenha mais de nove posições. Os métodos chamadores normalmente limitam a análise às nove posições previstas para o banco.

### 3.2. Existência da unidade

A posição selecionada precisa conter uma unidade:

```python
unit = bench[bench_slot]

if unit is None:
    return False
```

O método não valida outras propriedades da unidade, como custo, nível, composição ou força. A condição necessária nessa etapa é apenas que a referência não seja `None`.

### 3.3. Validade do destino

A posição de destino é verificada por `_is_valid_board_position(target)`.

Esse helper tenta delegar a validação para `board_manager.is_valid_position(position)`. Se ocorrer uma exceção, utiliza como fallback o intervalo:

```python
0 <= position < self.board_size
```

O tamanho configurado do tabuleiro é 28 posições.

**Importante:** `_is_valid_bench_board_move()` não verifica diretamente se o destino está vazio. A ausência de ocupação é garantida pelos chamadores que obtêm os destinos por `board_manager.get_empty_positions()`.

### 3.4. Bloqueio anti-loop

O método consulta o anti-loop com os seguintes dados:

```python
self._should_block_anti_loop(
    move_type="bench_to_board",
    source=bench_slot,
    target=target,
    unit=unit,
)
```

A consulta identifica o movimento como `bench_to_board` e informa a origem, o destino e a unidade envolvida.

Se a consulta retornar `True`, o movimento é considerado inválido nessa camada.

O helper `_should_block_anti_loop()` chama `anti_loop_manager.should_block_move(...)`. Caso essa chamada gere uma exceção, registra a falha e retorna `False`, permitindo o candidato nessa camada. Portanto, uma falha do mecanismo anti-loop não bloqueia automaticamente o movimento.

## 4. O que o método não verifica diretamente

O método não verifica diretamente:

- Se o tabuleiro possui alguma posição vazia.
- Se o destino está efetivamente vazio.
- Se a origem está dentro do limite fixo de nove posições, independentemente do tamanho da lista recebida.
- Se o movimento aumenta a força da equipe ou melhora a composição.
- Se a unidade pode entrar no tabuleiro segundo regras de nível ou limite de unidades.
- Se o ambiente de jogo autorizará a execução final da ação.

As condições de existência de espaço livre e de seleção de destinos vazios são tratadas principalmente pelos métodos que chamam essa validação. As regras definitivas de execução devem ser conferidas no fluxo responsável por aplicar a ação ao estado do jogo.

## 5. Relação com a geração das máscaras

O método é utilizado por diferentes rotinas do `ActionMaskManager`:

- `get_board_target_mask()`: agrega destinos possíveis para unidades do banco.
- `get_bench_to_board_target_mask(bench_slot)`: gera destinos para uma origem específica.
- `_has_valid_bench_move()`: verifica se existe pelo menos um movimento possível.
- `get_bench_move_source_mask()`: identifica unidades do banco com pelo menos um destino válido.
- `get_bench_move_masks()`: calcula as máscaras de origem e destino em uma única passagem.

Esses chamadores podem verificar previamente se existem posições vazias no tabuleiro. Alguns também aplicam limites de tamanho ao banco antes de selecionar as unidades.

As máscaras possuem fallback técnico para evitar distribuições categóricas vazias. Esse fallback não significa, por si só, que exista um movimento real válido.

## 6. Casos de teste relevantes

| Cenário | Resultado esperado |
|---|---|
| Banco não informado e unidade válida disponível | Usa o banco atual e continua a validação. |
| Índice de origem negativo | `False`. |
| Índice de origem fora do tamanho da lista | `False`. |
| Origem contém `None` | `False`. |
| Destino inválido segundo o helper de posição | `False`. |
| Anti-loop bloqueia o movimento | `False`. |
| Origem e destino válidos, unidade presente e anti-loop não bloqueia | `True`. |
| Consulta ao anti-loop gera exceção | O helper retorna `False`; o candidato não é bloqueado por essa consulta. |
| Destino ocupado, mas informado diretamente ao método | Não há verificação explícita de ocupação neste método; o resultado depende das demais condições. |

## 7. Requisitos para uma futura migração

Uma implementação equivalente deve preservar:

1. O uso do banco fornecido ou a obtenção do banco atual quando o argumento for `None`.
2. A validação do índice em relação a `len(bench)`.
3. A rejeição de origens vazias.
4. A delegação da validação do destino para `_is_valid_board_position()`.
5. O tipo de movimento `bench_to_board` na consulta anti-loop.
6. O comportamento de tolerância a exceções implementado por `_should_block_anti_loop()`.
7. A distinção entre um candidato individual válido e a existência de pelo menos um movimento real nas máscaras agregadas.

## 8. Conclusão

`_is_valid_bench_board_move()` é uma validação de candidato: verifica a origem, a existência de uma unidade, a validade do destino e o bloqueio anti-loop. A disponibilidade de espaço e a seleção de destinos vazios são responsabilidades dos chamadores, não condições verificadas diretamente por esse método.

A principal atenção para uma migração é não adicionar silenciosamente verificações de ocupação, limite fixo do banco ou regras estratégicas que não existem na implementação atual.
