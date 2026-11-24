# LobbyBatchManager — decisão de arquitetura e contrato (Fase B)

## Problema anterior
O `LobbyVectorEnv` executa cada `CppTFTLobbyWrapper` em loops Python separados. A propriedade das lobbies fica distribuída entre wrappers e não existe uma fronteira nativa explícita para coordenar várias simulações independentes.

## Racional técnico
A `TFTEngine` já representa uma lobby completa de oito jogadores. O manager deve possuir várias Engines completas, sem dividir jogadores de uma mesma partida e sem alterar regras, RNG interno, recompensas ou contratos de snapshot. A primeira implementação é sequencial para estabelecer ownership e semântica batch antes de qualquer paralelismo ou liberação do GIL.

## Responsabilidade nova
`tft_engine.LobbyBatchManager`:
- cria e possui exatamente N instâncias independentes de `TFTEngine`;
- atribui seeds independentes por offset determinístico (`base_seed + lobby_index`);
- expõe `reset(seed)` e `step(actions)` em lote, preservando a ordem dos índices;
- expõe IDs de Engine para correlação;
- possui lifecycle explícito e `close()` idempotente;
- rejeita dimensões incorretas de lote, jogadores e componentes de ação.

## Contratos e invariantes
- Uma Engine continua sendo dona de uma lobby inteira (8 jogadores).
- Cada índice do lote identifica a mesma Engine durante toda a vida do manager.
- Seeds fornecidas no reset são derivadas deterministicamente por índice; overflow é rejeitado antes de iniciar resets.
- Cada step recebe N lobbies, cada uma com oito ações de seis componentes.
- O manager executa sequencialmente e não libera o GIL nesta fase.
- A saída mantém um resultado nativo independente por lobby, incluindo observações, rewards, dones, masks, jogadores e snapshot nativo.
- Falha durante reset/step invalida a fronteira batch; o chamador deve executar reset completo antes de continuar. Não há rollback implícito.
- PPO, policy, reward shaping, GAE, loss, optimizer, estratégia e action masks permanecem fora do manager.

## Impactos e limites desta entrega
Esta entrega integra a API batch ao caminho real do `Trainer`: `LobbyVectorEnv` envia reset/step como uma única chamada nativa por lote, enquanto cada `CppTFTLobbyWrapper` continua responsável pela projeção de snapshots, máscaras, auditoria de rewards e eventos factuais. O manager empresta referências estáveis às Engines que possui; wrappers não encerram individualmente Engines compartilhadas. O caminho legado por factories continua disponível para testes e consumidores que não fornecem manager. Não há paralelismo, liberação do GIL ou alegação de ganho de throughput nesta fase. A API ainda materializa os dicionários/arrays atuais; a fronteira compacta é escopo da Fase C.

## Validação
- rejeitar zero lobbies, seed inválida/overflow e batches com dimensões inválidas;
- confirmar IDs distintos e estáveis;
- comparar reset/step batch com execução direta por Engine para seeds e ações idênticas;
- confirmar falha de lifecycle antes do reset e após close;
- executar suíte C++ e testes Python com o módulo `tft_engine` compilado.


## Integração Fase B — fluxo batch do Trainer
- `Trainer` instancia um único `LobbyBatchManager` para o conjunto de lobbies e injeta cada referência de Engine no wrapper correspondente.
- `LobbyVectorEnv.reset` chama `manager.reset(seed)` uma vez e entrega cada resultado ao processamento de snapshot do wrapper.
- `LobbyVectorEnv.step` normaliza as ações por wrapper, envia o lote em uma única chamada `manager.step(actions)` e processa cada resultado com o mesmo pipeline de auditoria/proveniência já existente.
- Auto-reset de uma lobby terminal continua individual, preservando a identidade do snapshot terminal e a observação do novo episódio.
- O manager é o único proprietário do lifecycle das Engines compartilhadas; `close()` é executado uma vez no fechamento do vetor.
- A API batch permanece sequencial em C++; o ganho desta etapa é a fronteira de ownership e chamada, não paralelismo.

## Evidências adicionais de integração e recuperação — Fase B

A conclusão da fase exige validar não apenas a chamada batch, mas também a fronteira de estado observável pelo Trainer:

- falha em reset invalida máscaras e metadados antigos em todos os wrappers antes que qualquer Engine possa avançar parcialmente;
- após falha de reset/step, LobbyVectorEnv bloqueia novas decisões até um reset completo;
- a trajetória de uma lobby deve permanecer idêntica quando outra lobby recebe uma sequência de ações diferente, demonstrando isolamento de estado/RNG;
- paridade batch vs. wrappers individuais inclui rewards por componente, eventos, action traces, eventos factuais, auditoria e identidades/seqüências dos snapshots terminal e seguinte;
- o smoke test nativo de treinamento deve completar com PPO ativo e validar o contrato de checkpoint; uma execução que não chega a essa etapa não é evidência de integração end-to-end.

A fase permanece aberta até que o CI execute também o smoke test PPO e todas as verificações acima passem. Não se declara ganho de throughput: a execução continua sequencial e a fronteira compacta permanece na Fase C.
