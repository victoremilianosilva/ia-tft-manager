# Decision Engine — Contrato de Tratamento de Erros

## 1. Objetivo

Padronizar a identificação e o tratamento de erros no `decision_engine`, garantindo que os componentes C++ utilizem códigos consistentes e que a integração com Python possa distinguir entradas inválidas de falhas técnicas.

O módulo deve permanecer independente do `combat_engine`.

## 2. Códigos de erro

Os códigos são definidos em `decision/DecisionError.hpp`, por meio do enum `DecisionErrorCode`.

| Código | Valor | Significado |
|---|---:|---|
| `NONE` | 0 | Operação sem erro |
| `INVALID_INPUT` | 1 | Entrada inválida ou malformada |
| `INVALID_STATE` | 2 | Estado incompatível com a operação |
| `INVALID_CONFIGURATION` | 3 | Configuração inconsistente |
| `DEPENDENCY_FAILURE` | 4 | Falha em uma dependência |
| `INTERNAL_ERROR` | 5 | Falha interna inesperada |

Os valores numéricos fazem parte do contrato e não devem ser alterados sem atualizar os consumidores correspondentes.

## 3. Estrutura de diagnóstico

`DecisionError` contém:

- `code`: código padronizado do erro.
- `message`: descrição destinada a diagnóstico e logs.
- `has_error()`: indica se existe erro.
- conversão explícita para `bool`: permite verificar a presença de erro.

A mensagem não deve ser utilizada como identificador de controle. A lógica deve depender do código.

## 4. Responsabilidades

### C++

- Validar entradas antes de utilizá-las.
- Retornar códigos consistentes para falhas conhecidas.
- Preservar a distinção entre entrada inválida e falha técnica.
- Não permitir que exceções atravessem a fronteira do `pybind11` sem tratamento definido.
- Registrar informações úteis para diagnóstico, sem introduzir efeitos colaterais nas consultas de candidatos ou máscaras.

### Python

- Interpretar os resultados da integração nativa.
- Decidir quando uma operação deve ser rejeitada, repetida ou encaminhada ao backend alternativo.
- Não interpretar todo erro como motivo para fallback.
- Preservar o comportamento do ambiente e o fluxo de treinamento PPO.

## 5. Política de fallback

O fallback deve ser controlado pela camada de integração.

- `INVALID_INPUT`: rejeitar a entrada; não repetir automaticamente a mesma operação no backend alternativo.
- `INVALID_STATE`: interromper a operação incompatível e permitir correção ou recuperação explícita.
- `INVALID_CONFIGURATION`: registrar a falha de configuração; não ocultá-la com fallback silencioso.
- `DEPENDENCY_FAILURE`: permitir fallback quando a operação alternativa for segura e estiver configurada.
- `INTERNAL_ERROR`: registrar o diagnóstico e aplicar a política de recuperação definida pela integração.
- `NONE`: continuar o fluxo normal.

O fallback não deve misturar parcialmente resultados de diferentes backends na mesma máscara. A política de seleção do backend deve ser consistente durante cada operação.

## 6. Integração com os resultados de decisão

`DecisionError` descreve falhas técnicas e de validação. Ele não substitui `ValidationStatus`, `BlockReason` ou o resultado de decisão.

- `ValidationStatus`: informa se uma operação é válida, inválida ou apresentou erro.
- `BlockReason`: informa por que um movimento foi bloqueado pelo AntiLoop.
- `DecisionErrorCode`: identifica a categoria de erro ocorrido.

Um movimento bloqueado pelo AntiLoop não deve ser classificado automaticamente como erro técnico.

## 7. Critérios de aceitação

- Os códigos possuem valores estáveis e verificáveis em compilação.
- O header compila com C++20.
- Os nomes dos códigos são estáveis para logs e integração.
- Entradas inválidas são diferenciadas de falhas internas.
- O módulo não depende de tipos do `combat_engine`.
- A integração Python define explicitamente como tratar cada categoria.
- Nenhuma alteração automática de comportamento do PPO é introduzida apenas pela criação deste contrato.