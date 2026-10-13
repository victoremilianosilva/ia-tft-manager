# Equivalência das Máscaras de Ação — Python × C++

## Objetivo

Garantir que o motor nativo C++ reproduza o comportamento do `ActionMaskManager.py`. Durante a migração, o Python é a referência funcional: diferenças de comportamento devem ser corrigidas no C++ ou registradas antes de avançar.

## Máscaras comparadas

| Índice | Máscara                              | Dimensão |
| -----: | ------------------------------------ | -------: |
|      0 | Tipo de ação                         |        7 |
|      1 | Slots da loja                        |        5 |
|      2 | Unidades do banco para venda         |        9 |
|      3 | Destinos de unidades do banco        |       28 |
|      4 | Origens de movimentação no tabuleiro |       28 |
|      5 | Destinos condicionais do tabuleiro   |       28 |

Os fallbacks categóricos são comparados, mas não devem ser confundidos com disponibilidade real de uma ação.

## Cenários cobertos

* Estado vazio.
* Unidades compráveis e custos diferentes.
* Unidade da loja com `available=False`.
* Movimentação do banco para o tabuleiro.
* Movimentação e troca de unidades no tabuleiro.
* Economia insuficiente e seleção de unidades para venda.

Os testes utilizam um anti-loop sem bloqueios para isolar as regras básicas das máscaras. A equivalência do histórico real de anti-loop será testada separadamente.

## Regra de compatibilidade

A máscara Python da loja considera presença da unidade, espaço no banco e saldo. Ela não filtra o campo `available`. O motor C++ deve reproduzir essa regra, mesmo que outra regra pareça preferível.

Nenhuma regra deve ser modificada apenas para fazer os testes passarem.

## Execução

Com a extensão `decision_engine` compilada e disponível no ambiente Python:

```bash
python -m pytest tests/test_action_mask_equivalence.py -v
```

Para executar também os testes do adapter:

```bash
python -m pytest tests/test_decision_state_adapter.py tests/test_action_mask_equivalence.py -v
```

## Critério de aceite

* As seis máscaras têm as dimensões esperadas.
* Os valores das máscaras Python e C++ são idênticos nos cenários cobertos.
* A disponibilidade real das ações corresponde à máscara de tipos Python.
* Nenhuma divergência é corrigida alterando silenciosamente o comportamento Python.

Os resultados devem ser registrados após a execução local. Criar os testes não equivale a confirmar que passaram.
