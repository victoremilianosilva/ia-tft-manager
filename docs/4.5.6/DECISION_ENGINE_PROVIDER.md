# Decision Engine Provider

## Objetivo

Centralizar a seleção entre a implementação Python e a extensão C++ `decision_engine`, permitindo migrar gradualmente o cálculo das máscaras sem alterar imediatamente o fluxo do treinamento PPO.

## Configuração

A seleção pode ser feita pela variável de ambiente `TFT_DECISION_ENGINE` ou pelo argumento de `get_decision_engine_backend()`.

| Valor       | Comportamento                                                |
| ----------- | ------------------------------------------------------------ |
| `python`    | Seleciona a implementação Python. É o padrão.                |
| `cpp`       | Importa a extensão nativa e valida a API pública necessária. |
| Outro valor | Gera `ValueError`.                                           |

Quando C++ é solicitado e a extensão não está disponível, o provider gera `RuntimeError`. Não há fallback silencioso.

## API pública

* `get_decision_engine_backend(backend=None)`: resolve a implementação selecionada.
* `DecisionEngineBackend.name`: identifica o backend ativo.
* `DecisionEngineBackend.is_python`: informa se Python foi selecionado.
* `DecisionEngineBackend.is_cpp`: informa se C++ foi selecionado.
* `DecisionEngineBackend.require_native_module()`: retorna a extensão nativa ou gera um erro claro.

## Integração atual

O provider verifica a disponibilidade de `ActionMaskEngine`, `AntiLoopEngine` e `PlayerState` no módulo nativo.

Nesta etapa, ele não converte os managers Python em `PlayerState`, não gera máscaras e não modifica o histórico anti-loop.

## Próximas etapas

1. Implementar a conversão do estado real para os tipos nativos.
2. Integrar o provider ao `ActionMaskManager` e ao `TFTLobby`.
3. Compartilhar o histórico anti-loop persistente do jogador.
4. Validar a equivalência das máscaras Python e C++.

## Compilação e importação

A extensão deve ser compilada pelo CMake usando o mesmo ambiente Python que será utilizado pelo projeto. O teste `decision_engine_import` já está configurado no CMake; sua execução ainda precisa ser confirmada após a integração.

## Critério de conclusão

A etapa estará validada quando o provider selecionar corretamente os dois backends, a extensão C++ compilar e importar no ambiente-alvo e a configuração Python continuar funcionando sem exigir a extensão nativa.
