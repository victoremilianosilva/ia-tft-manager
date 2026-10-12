# Mapeamento de `_is_valid_board_move()`

## 1. Objetivo

Documentar as condições utilizadas por `ActionMaskManager._is_valid_board_move()` para determinar se um movimento dentro do tabuleiro pode ser considerado válido durante a geração das Action Masks.

O método verifica os índices, a existência de uma unidade na origem e as regras AntiLoop. O tipo de movimento depende de o destino estar vazio ou ocupado.

**Arquivo:** `ai/ActionMaskManager.py`

## 2. Implementação analisada

```python
def _is_valid_board_move(self, source, target, board=None):
    if board is None:
        board = self._get_board()

    if source < 0 or source >= len(board):
        return False

    if target < 0 or target >= len(board):
        return False

    if source == target:
        return False

    source_unit = board[source]

    if source_unit is None:
        return False

    target_unit = board[target]

    if target_unit is not None:
        if self._should_block_anti_loop(
            move_type="board_swap",
            source=source,
            target=target,
            unit=source_unit,
        ):
            return False

        return True

    if self._should_block_anti_loop(
        move_type="board_move",
        source=source,
        target=target,
        unit=source_unit,
    ):
        return False

    return True
```

## 3. Condições de validação

As condições são avaliadas na seguinte ordem.

### 3.1. Obtenção do tabuleiro

Se o argumento `board` não for informado, o método utiliza `self._get_board()` para obter o tabuleiro atual.

Se um tabuleiro for fornecido, ele será utilizado diretamente.

O método não valida explicitamente o tipo ou a estrutura completa desse objeto.

### 3.2. Índice de origem válido

```python
if source < 0 or source >= len(board):
    return False
```

A origem precisa estar dentro dos limites da lista do tabuleiro.

O movimento é rejeitado quando:

- O índice de origem é negativo.
- O índice de origem é igual ou superior ao tamanho do tabuleiro.

### 3.3. Índice de destino válido

```python
if target < 0 or target >= len(board):
    return False
```

O destino também precisa estar dentro dos limites da lista.

O movimento é rejeitado quando:

- O índice de destino é negativo.
- O índice de destino é igual ou superior ao tamanho do tabuleiro.

O método utiliza `len(board)` como limite, não uma constante fixa de 28 posições.

### 3.4. Origem diferente do destino

```python
if source == target:
    return False
```

Uma unidade não pode ser movimentada para a mesma posição em que já se encontra.

Essa condição é verificada antes de consultar o conteúdo das posições e o AntiLoop.

### 3.5. Origem ocupada

```python
source_unit = board[source]

if source_unit is None:
    return False
```

A posição de origem precisa conter uma unidade.

Se a origem estiver vazia, o candidato é rejeitado sem consultar o AntiLoop.

O método considera `None` como indicação de posição vazia. Ele não valida, por conta própria, se um objeto diferente de `None` representa uma unidade válida segundo todas as regras do jogo.

## 4. Classificação do movimento

Depois das validações básicas, o método verifica o conteúdo do destino.

### 4.1. Destino ocupado: `board_swap`

```python
target_unit = board[target]

if target_unit is not None:
    ...
```

Quando o destino contém um valor diferente de `None`, o candidato é tratado como uma troca de posições.

O método consulta o AntiLoop com os seguintes argumentos:

- `move_type="board_swap"`
- `source`: índice de origem.
- `target`: índice de destino.
- `unit`: unidade localizada na origem.

Se o AntiLoop bloquear o movimento, o método retorna `False`.

Caso contrário, retorna `True`.

**Observação:** o método não verifica diretamente se a troca melhora o posicionamento, a composição ou o poder do tabuleiro. Também não executa a troca; apenas avalia o candidato.

### 4.2. Destino vazio: `board_move`

Quando o destino contém `None`, o candidato é tratado como uma movimentação para uma posição vazia.

A consulta AntiLoop utiliza:

- `move_type="board_move"`
- `source`: índice de origem.
- `target`: índice de destino.
- `unit`: unidade localizada na origem.

Se o AntiLoop bloquear o movimento, o resultado será `False`. Caso contrário, será `True`.

**Observação:** o método não executa a movimentação nem altera as posições das unidades.

## 5. Comportamento do AntiLoop

A validação AntiLoop ocorre somente depois de os índices serem considerados válidos, a origem estar ocupada e a origem ser diferente do destino.

A chamada é realizada por meio de:

```python
self._should_block_anti_loop(...)
```

Esse helper consulta `AntiLoopManager.should_block_move()`.

Se a consulta retornar um valor verdadeiro, o movimento será bloqueado. Se retornar um valor falso, o candidato poderá ser aceito por este método.

Se a consulta lançar uma exceção, `_should_block_anti_loop()` captura a falha, registra o erro e retorna `False`. Consequentemente, o candidato é permitido nesta camada, desde que tenha passado pelas validações básicas.

Isso não garante que a execução real seja bem-sucedida: o ambiente continua responsável por validar e executar a ação.

## 6. Ordem completa das verificações

| Ordem | Condição | Resultado quando falha |
|---|---|---|
| 1 | Obter o tabuleiro, caso não tenha sido fornecido | Depende do resultado de `_get_board()` |
| 2 | Origem dentro dos limites | `False` |
| 3 | Destino dentro dos limites | `False` |
| 4 | Origem diferente do destino | `False` |
| 5 | Origem contém uma unidade | `False` |
| 6 | Classificar o destino como ocupado ou vazio | Define o tipo do movimento |
| 7 | AntiLoop não bloqueia o candidato | `False` se bloquear; `True` caso contrário |

## 7. Condições que o método não verifica diretamente

O método não verifica diretamente:

- Se o destino é uma posição válida segundo `BoardManager.is_valid_position()`. Ele verifica apenas os limites da lista recebida.
- Se a troca ou movimentação melhora a estratégia da IA.
- Se o movimento aumenta o poder do tabuleiro.
- Se a unidade deve ocupar determinada posição por seu papel ou alcance.
- Se a execução real será bem-sucedida.
- Se a estrutura completa da unidade é válida.
- Se uma máscara técnica de fallback representa um movimento real.

Essas verificações, quando necessárias, devem ser identificadas nas demais camadas responsáveis. Não se deve presumir que sejam executadas por este método.

## 8. Casos de teste derivados

| Caso | Estado | Resultado esperado |
|---|---|---|
| Origem negativa | `source < 0` | `False` |
| Origem fora dos limites | `source >= len(board)` | `False` |
| Destino negativo | `target < 0` | `False` |
| Destino fora dos limites | `target >= len(board)` | `False` |
| Mesma posição | `source == target` | `False` |
| Origem vazia | `board[source] is None` | `False` |
| Destino ocupado e AntiLoop bloqueia | `board_swap` bloqueado | `False` |
| Destino ocupado e AntiLoop permite | `board_swap` permitido | `True` |
| Destino vazio e AntiLoop bloqueia | `board_move` bloqueado | `False` |
| Destino vazio e AntiLoop permite | `board_move` permitido | `True` |
| Falha na consulta AntiLoop | Exceção capturada pelo helper | Candidato permitido nesta camada, se as validações básicas passarem |

Os testes devem verificar também que o método não executa movimentos nem altera diretamente o tabuleiro.

## 9. Implicações para a migração Python/C++

Uma implementação equivalente em C++ deve preservar:

1. A ordem das validações.
2. A rejeição de índices inválidos.
3. A rejeição de origem igual ao destino.
4. A rejeição de origens vazias.
5. A distinção entre `board_move` e `board_swap`.
6. O envio da unidade de origem para a consulta AntiLoop.
7. A semântica de bloqueio e de falha na consulta AntiLoop.
8. A ausência de execução ou mutação do tabuleiro durante a validação.

Os testes de equivalência devem comparar os resultados de Python e C++ para os mesmos estados, índices, unidades e históricos AntiLoop.

## 10. Conclusão

`_is_valid_board_move()` é um validador de candidatos utilizado na geração das máscaras. Ele verifica os limites dos índices, impede movimentos para a própria posição, exige uma unidade na origem e consulta o AntiLoop de acordo com o tipo de movimento.

O método considera válido qualquer candidato que passe por essas condições. Ele não avalia a qualidade estratégica da ação nem executa o movimento.

A implementação C++ deverá reproduzir esse comportamento, inclusive o tratamento de falhas na consulta AntiLoop, antes de substituir a implementação Python no fluxo principal.

**Escopo:** este documento descreve o comportamento de `_is_valid_board_move()` em `ai/ActionMaskManager.py`. A validação completa da execução exige analisar separadamente o ambiente e os métodos responsáveis pela movimentação e pela troca de unidades.