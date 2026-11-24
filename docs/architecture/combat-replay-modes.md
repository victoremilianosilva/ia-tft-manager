# Combat replay and event-retention modes

## Problema anterior

O caminho de combate da lobby sempre habilitava `record_damage` e `record_events`, montava os documentos `COMBAT_SNAPSHOT_V2` e `COMBAT_SIMULATION_REPLAY_V1`, serializava os payloads em JSON e os anexava a `StepResult.events`. O Trainer não consome esses eventos detalhados no caminho de decisão PPO.

Além disso, a preparação de cada unidade fazia uma cópia intermediária necessária para aplicar emblemas e stats efetivos, seguida de outra cópia ao construir `RuntimeUnit`. A busca por posição copiava toda a `CombatUnit` apenas para substituir duas coordenadas.

## Justificativa técnica

Eventos detalhados, JSONs de replay e cópias integrais de estruturas com vetores e strings aumentam alocações e trabalho por combate. O simulador, entretanto, precisa manter o mesmo resultado determinístico e as estatísticas agregadas por unidade que alimentam evidências estratégicas.

## Responsabilidade nova

- O modo normal de treinamento deve omitir coleta/retensão de eventos detalhados e serialização de artefatos JSON sem consumidor.
- O modo de auditoria deve continuar produzindo os documentos e eventos completos.
- O simulador continua calculando dano agregado, sobrevivência, mortes, cura, ataques, conjurações e posição final em `CombatUnitResult`, independentemente da coleta de eventos detalhados.
- A preparação de unidade deve transferir a estrutura efetiva para `RuntimeUnit` por move semantics, preservando a cópia inicial que protege a entrada.
- Distâncias de movimento devem ser calculadas diretamente das coordenadas candidatas, sem copiar `CombatUnit`.

## Configuração

Variável de ambiente `TFT_COMBAT_REPLAY_MODE`:

| Valor | Comportamento |
|---|---|
| `off` (padrão) | Não coleta eventos detalhados nem constrói/serializa `COMBAT_SNAPSHOT_V2` e `COMBAT_SIMULATION_REPLAY_V1`. |
| `audit` | Mantém eventos detalhados, snapshots e replay para auditoria. |
| `debug` | Mesmo conjunto de artefatos detalhados do modo `audit`, reservado a depuração. |

Valores diferentes são rejeitados explicitamente. O modo é lido durante a resolução de combate; portanto, a configuração deve ser definida antes do step que executa o combate.

## Contratos e invariantes

- A mesma entrada e seed produzem o mesmo vencedor, duração, sobreviventes, dano agregado e estatísticas finais por unidade nos modos `off` e `audit`.
- `CombatUnitResult` permanece disponível em todos os modos; `record_damage` e `record_events` controlam somente coleções de eventos detalhados.
- Dano agregado por unidade continua alimentando `strategic_board_contribution_evidence`.
- Identidade, sequência e proveniência dos eventos continuam preservadas no modo `audit`.
- A entrada original permanece imutável: a cópia `effective_unit` é mantida durante a aplicação de emblemas/stats, e somente essa cópia preparada é movida para o runtime.
- Ordem de eventos, regras de movimento, valores de combate, reward, masks e contexto estratégico não podem mudar por causa do modo de retenção.

## Impactos

- `cpp/src/lobby/TftEngine.cpp`: configuração do modo, opt-in dos eventos, snapshots e replay JSON; preserva builders/validadores de evidência e agregações.
- `cpp/src/combat/CombatEngine.cpp`: move da unidade preparada e cálculo de distância sem cópia de probe.
- `cpp/tests/test_combat_engine.cpp`: equivalência de resultado e evidência agregada com eventos ligados/desligados.
- `tests/test_tft_engine_api.py`: teste de proveniência de eventos configura explicitamente o modo `audit`.

## Critérios de validação

- Teste nativo compara vencedor, duração, sobreviventes, dano e métricas por unidade entre os modos com e sem eventos.
- Modo normal não retém vetores de eventos detalhados.
- Modo `audit` continua publicando eventos tipados com sequência e UUIDs de origem/destino.
- Build e testes nativos/Python passam.
- Sanitizers e medição de alocações podem ser executados posteriormente; não são substituídos por estimativas de performance.
