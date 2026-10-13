# Decision State Adapter

## Objetivo

Converter o estado dos managers Python do TFT para os tipos nativos disponibilizados pela extensão `decision_engine`.

O adaptador é responsável exclusivamente pela conversão e validação. Ele não executa ações, não gera máscaras e não modifica os managers nem o histórico anti-loop.

## Arquivo

`ai/DecisionStateAdapter.py`

Função pública:

```python
build_player_state(
    env,
    *,
    is_alive=True,
    native_module=None,
)
```

### Parâmetros

* `env`: instância do ambiente que contém os managers do jogador.
* `is_alive`: estado de vida informado pelo chamador. Deve refletir o estado atual da lobby quando usado em uma partida.
* `native_module`: módulo nativo opcional. Se não informado, o adaptador tenta importar `decision_engine`.

### Retorno

Uma instância nativa de `decision_engine.PlayerState`, contendo:

* identificação do jogador e estado de vida;
* economia atual;
* 28 posições de tabuleiro;
* 9 posições de banco;
* 5 posições de loja.

## Mapeamento de dados

| Origem Python                      | Destino C++                     |
| ---------------------------------- | ------------------------------- |
| `env.player_id`                    | `PlayerState.player_id`         |
| `is_alive`                         | `PlayerState.is_alive`          |
| `economy_manager.gold`             | `EconomyState.gold`             |
| `economy_manager.level`            | `EconomyState.level`            |
| `economy_manager.xp`               | `EconomyState.current_xp`       |
| `GameConfig.MAX_LEVEL`             | `EconomyState.max_level`        |
| `GameConfig.get_xp_to_next(level)` | `EconomyState.xp_to_next_level` |
| `GameConfig.REROLL_COST`           | `EconomyState.reroll_cost`      |
| `GameConfig.BUY_XP_COST`           | `EconomyState.xp_purchase_cost` |
| `board_manager.board`              | `PlayerState.board`             |
| `bench_manager.bench`              | `PlayerState.bench`             |
| `shop_manager.shop`                | `PlayerState.shop`              |

## Identidade das unidades

O adaptador prioriza o campo `uuid`. Quando não existe UUID, utiliza `id` somente se o valor for numérico e compatível com o tipo nativo.

O campo `star` é convertido para o tipo numérico esperado pelo C++.

Slots vazios permanecem como `None`. Unidades precisam estar representadas por dicionários, de acordo com o formato atual dos managers.

## Validação e erros

O adaptador rejeita:

* managers obrigatórios ausentes;
* listas de slots com dimensões diferentes das esperadas;
* unidades que não sejam dicionários ou `None`;
* valores econômicos negativos ou fora dos limites numéricos;
* níveis incompatíveis com `GameConfig.MAX_LEVEL`;
* falhas ao carregar a extensão nativa.

Os erros são explícitos para evitar que um estado incorreto produza máscaras aparentemente válidas.

## Integridade do estado

A conversão não deve:

* gastar ou adicionar ouro;
* mover, comprar ou vender unidades;
* atualizar o histórico anti-loop;
* registrar movimentos;
* gerar ou modificar máscaras de ações.

## Escopo desta entrega

Este adaptador é uma etapa intermediária. A integração com `ActionMaskManager`, `TFTLobby` e a seleção do backend fica para etapas posteriores.

## Validação recomendada

1. Compilar a extensão nativa.
2. Criar um ambiente e converter seu estado inicial.
3. Conferir as dimensões e os valores econômicos.
4. Testar slots vazios e ocupados nas três estruturas.
5. Testar unidades com UUID e unidades sem UUID.
6. Testar nível máximo, ouro zero e XP zero.
7. Confirmar que dados inválidos geram exceções claras.
8. Comparar o estado dos managers antes e depois da conversão para confirmar que nada foi alterado.
