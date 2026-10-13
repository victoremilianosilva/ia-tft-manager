# Testes do Decision State Adapter

## Objetivo

Validar a conversão dos managers Python para `decision_engine.PlayerState`, usando a extensão C++ compilada.

## Arquivo de testes

`tests/test_decision_state_adapter.py`

## Executar

Na raiz do projeto, com o ambiente virtual ativado:

```powershell
python -m pytest -q tests/test_decision_state_adapter.py
```

Se a extensão `decision_engine` não estiver compilada ou não estiver disponível no `PYTHONPATH`, os testes que dependem dela serão ignorados pelo `pytest.importorskip`.

Para validar a integração nativa, confirme que a extensão está disponível no mesmo ambiente Python usado para executar os testes.

## Cobertura

* Dimensões de tabuleiro, banco e loja.
* Conversão dos campos de economia.
* Identidade, estrelas e custo das unidades.
* Slots vazios.
* Unidade indisponível na loja.
* IDs textuais sem UUID.
* Dimensões inválidas.
* Valores econômicos inválidos.
* Unidades em formato incorreto.
* Ausência de mutações nos managers durante a conversão.

## Critérios de aceitação

1. Os testes passam com a extensão C++ compilada.
2. Os dados convertidos correspondem aos dados Python de origem.
3. Estados inválidos são rejeitados com `ValueError`.
4. A conversão não altera tabuleiro, banco, loja ou economia.
5. A extensão real é utilizada nos testes, sem substituir os tipos nativos por mocks.

## Limitação

Esses testes validam a conversão isoladamente. Não comprovam ainda a equivalência das máscaras Python e C++, nem a integração com `TFTLobby` ou PPO.
