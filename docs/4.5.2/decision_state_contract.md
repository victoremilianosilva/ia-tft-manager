# Decision Engine — Contrato de Estado, Histórico e Resultados

## 1. Objetivo

Definir estruturas explícitas para representar o estado do jogador, as unidades, as posições, o histórico de movimentos e os resultados produzidos pelo `decision_engine`.

As estruturas devem permitir que os componentes nativos compartilhem dados sem depender diretamente de objetos Python ou das estruturas internas do motor de combate.

## 2. Organização dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `DecisionState.hpp` | Identidade das unidades, snapshots, economia e estado do jogador |
| `DecisionHistory.hpp` | Assinaturas de posicionamento, visitas, movimentos, bloqueios e métricas |
| `DecisionResult.hpp` | Máscaras, status de validação e resultados de operações |

Todos os tipos pertencem ao namespace `tft::decision` e utilizam os tipos fundamentais definidos em `DecisionTypes.hpp`.

## 3. Estado do jogador

`PlayerState` representa os dados necessários às futuras validações de ações.

Contém:

- Identificador do jogador e estado de vida.
- Economia: ouro, nível, XP e custos de referência.
- Tabuleiro com 28 slots.
- Banco com 9 slots.
- Loja com 5 slots.

Slots vazios são representados por `std::nullopt`, distinguindo ausência de unidade de uma unidade real.

A estrutura fornece consultas simples para verificar se existem espaços livres no tabuleiro ou no banco. As demais regras de validação ficam fora dela.

## 4. Identidade das unidades

`UnitIdentity` representa a identidade utilizada nas comparações históricas.

A ordem de preferência é:

1. `uuid`, quando disponível.
2. Combinação de `id` e `star`, quando não houver UUID.

Se nenhum identificador estiver disponível, a conversão do estado não deve inventar uma identidade.

`UnitSnapshot` contém a identidade e os atributos mínimos necessários às decisões atuais. Novos campos devem ser adicionados quando houver uma necessidade identificada no contrato do motor.

## 5. Posições e assinaturas

`PositionSignature` registra as identidades presentes em cada slot do tabuleiro e do banco.

A assinatura deve ser comparável por valor, possibilitando detectar se um estado já foi visitado.

A posição faz parte da assinatura: unidades iguais em slots diferentes representam estados de posicionamento distintos.

A assinatura não inclui a loja nem a economia nesta etapa, preservando o escopo do histórico de posicionamento existente no AntiLoop.

## 6. Histórico do AntiLoop

`AntiLoopHistory` reúne:

- Histórico de assinaturas de posicionamento.
- Histórico de movimentos.
- Movimentos bloqueados e seus estados associados.
- Contagem de visitas aos estados.
- Último estado e último movimento registrados.
- Métricas acumuladas de execução.

Os vetores não aplicam limites de retenção automaticamente. O componente responsável deverá respeitar as configurações de tamanho dos históricos.

As consultas usadas durante a geração de máscaras devem ser somente de leitura. A geração de candidatos não deve registrar movimentos, modificar visitas ou incrementar métricas.

O reset dos históricos e a persistência das métricas serão definidos na implementação do AntiLoop.

## 7. Resultados

`ValidationResult` distingue:

- `VALID`: entrada aceita pela validação.
- `INVALID`: operação inválida.
- `ERROR`: falha interna.

`BlockReason` identifica o motivo de bloqueio quando aplicável.

`ActionMasks` representa as máscaras da política, incluindo dimensões principais e máscaras condicionadas pela origem selecionada.

As dimensões principais permanecem compatíveis com o contrato existente:

`[7, 5, 9, 28, 28, 28]`

Também são representadas as máscaras condicionadas de tabuleiro e de banco para tabuleiro.

`DecisionResult` reúne as máscaras, o resultado da validação e informações de erro. A implementação deverá padronizar como `success` e `validation.status` serão preenchidos, evitando estados contraditórios.

## 8. Dependências e limites

As estruturas utilizam tipos da biblioteca padrão do C++.

Esta etapa não implementa:

- Conversão completa dos objetos Python para os snapshots nativos.
- Geração de máscaras.
- Regras de validação de movimentos.
- Detecção de loops.
- Política PPO, recompensas ou execução de ações.
- Serialização e hashing de assinaturas.

Essas responsabilidades pertencem às etapas seguintes.

## 9. Critérios de aceitação

- Os headers compilam com C++20.
- Os tipos estão no namespace `tft::decision`.
- O estado representa corretamente as dimensões do tabuleiro, banco e loja.
- Slots vazios são distintos de unidades presentes.
- As assinaturas podem ser comparadas por valor.
- O histórico representa movimentos e bloqueios sem depender de objetos Python.
- As dimensões das máscaras permanecem compatíveis com a política existente.
