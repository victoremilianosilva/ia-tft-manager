# Contratos, enums e formatos de dados

> **Snapshot do runtime atual/legado:** os formatos descritos aqui documentam bindings e dados implementados no snapshot auditado. Eles não substituem os contratos semânticos aprovados da nova linhagem. O contrato PPO ativo usa nove tipos de ação e registro de seis inteiros com dimensões-base `[9, 5, 9, 28, 28, 28]`; ações de item usam cabeças/máscaras condicionais adicionais. Para semântica normativa, consulte [Action / Mask Contract v1](action-mask-contract.v1.draft.md) e [Observation Schema v1](../spec/observation-schema.v1.draft.json).

## Contrato de ação

engine_contracts.py mantém IDs Python estáveis para tipos de ação e estratégia. O C++ possui contratos correspondentes em DecisionTypes.hpp e TftEngine.hpp. Qualquer alteração precisa ser refletida em policy, máscaras, conversores, buffer, bindings e testes.

| Constante | Valor |
|---|---:|
| Jogadores por lobby | 8 |
| Posições de tabuleiro | 28 (4 × 7) |
| Slots de banco | 9 |
| Slots de loja | 5 |
| Componentes da ação | 6 |
| Dimensões-base do registro PPO | [9, 5, 9, 28, 28, 28] |

As dimensões-base não são o inventário completo das cabeças condicionais de item; veja o contrato Action/Mask v1 para as máscaras dedicadas e os limites condicionados por tipo.

## Máscaras

As máscaras booleanas chegam ao PyTorch e são armazenadas no rollout junto com as transições. Matrizes condicionais representam origem × destino, e o tipo da ação determina quais componentes têm significado. Policy e engine precisam compartilhar a mesma convenção de índices.

## Catálogo de unidades

units_gerado.json é uma lista de definições de campeões. A engine lê campos como apiName, name, cost, traits, stats, combat_profile, habilidade e ícones. O viewer usa aliases do catálogo para tornar snapshots legíveis.

## Logs do viewer

O schema de sessão atual é versão 1. metadata.json guarda metadados da partida; cada log de jogador contém entries e eventos com sequence_id, timestamp_iso, round, stage, event_type, text e payload. O replay valida versão e ordem dos IDs.

## Alterar contratos com segurança

1. Mude o tipo/shape na definição de origem.
2. Atualize binding e wrapper.
3. Atualize policy, flattening e armazenamento do rollout.
4. Adicione fixtures de equivalência e casos inválidos.
5. Atualize esta documentação e os documentos funcionais afetados.
6. Execute CTest e testes Python relacionados.
