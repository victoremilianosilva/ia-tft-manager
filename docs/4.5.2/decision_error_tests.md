# Decision Engine — Testes do Contrato de Erros

## Objetivo

Validar o contrato definido em `decision/DecisionError.hpp` antes de integrá-lo aos componentes de decisão.

## Cobertura

O teste `tests/test_decision_error.cpp` verifica:

- Estado padrão sem erro.
- Detecção de erro por `has_error()`.
- Conversão explícita para `bool`.
- Preservação do código e da mensagem.
- Nome estável para cada código conhecido.
- Tratamento de códigos desconhecidos.

## Execução

Compilar com C++20 e incluir `cpp/include` no caminho de headers. Executar o binário de teste após a compilação.

## Critérios de aceitação

- A compilação termina sem erros.
- Todos os testes terminam sem falhas.
- O teste não depende do Python, do `pybind11` ou do `combat_engine`.
- Nenhum componente de produção é modificado nesta etapa.

## Limites

Estes testes validam apenas o contrato de erros. Eles não comprovam o comportamento do fallback, o tratamento de exceções na integração Python ou a propagação de erros pelos resultados de decisão. Essas verificações ficam para as etapas de integração.