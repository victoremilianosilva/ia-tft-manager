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


## Fase C — primeira fatia da fronteira compacta: action masks

### Problema anterior
O binding materializava as máscaras de cada jogador como doze arrays NumPy separados, agrupados em oito dicionários Python por lobby. Esse formato cria muitos objetos Python no limite C++/Python antes mesmo de o Trainer transformar os valores em tensores.

### Racional técnico
As máscaras já possuem um contrato fixo de campos, dimensões e ordem em `action_contract.MASK_SHAPES`. Portanto, a fronteira nativa pode transportar os mesmos bits em um único buffer booleano contíguo por lobby, sem alterar semântica, legalidade ou o contrato de checkpoint. A camada wrapper mantém a visão compatível por meio de slices/reshapes que compartilham a memória do buffer.

### Responsabilidade nova
- O binding publica `action_masks` como um array NumPy `bool` contíguo com shape `[8, 1280]`.
- A ordem dos segmentos é idêntica à ordem canônica de `MASK_SHAPES`.
- `CppTFTLobbyWrapper` valida dtype e dimensões e cria views por jogador/campo, sem cópia na ingestão.
- A API pública de leitura continua entregando cópias defensivas; a API de treinamento continua expondo buffers somente leitura.

### Contratos e invariantes
- Nenhum bit, dimensão, nome de campo ou regra condicional de máscara é alterado.
- A largura do buffer é a soma das dimensões do contrato atual (1280 booleanos por jogador).
- Views internas permanecem ancoradas no array NumPy proprietário; nenhuma view pode sobreviver ao ciclo de vida do snapshot por referência solta.
- Payloads legados em lista de mappings continuam aceitos pelo wrapper para fixtures e consumidores de teste.
- Máscaras públicas continuam isoladas de mutações do consumidor; máscaras de treinamento continuam somente leitura.
- A Engine continua sendo a autoridade final de legalidade; o buffer é apenas um formato de transporte.

### Impactos e limites
A conversão C++ deixa de alocar 96 arrays e 8 dicionários de máscaras por lobby/resultado e passa a alocar um único array contíguo. O wrapper ainda reconstrói mappings leves com views para preservar os contratos atuais do Trainer e da policy; remover esses mappings do hot path é uma etapa posterior e separada da Fase C. Observações, rewards e dones já atravessam o binding como arrays NumPy contíguos. Snapshots de auditoria/replay permanecem imutáveis e lazy, sem redução de campos ou validações nesta entrega.

### Fase C — ownership imutável de estado por jogador

#### Problema anterior
A expansão do snapshot da lobby copiava profundamente cada registro de jogador para criar as linhas do rollout. Em seguida, o `RolloutBuffer` copiava novamente esses subtrees ao assumir ownership e voltava a copiá-los ao expor metadados. O conteúdo nativo é evidência de auditoria associada a uma identidade de snapshot e não deve ser mutável pelo Trainer ou por consumidores do buffer.

#### Racional técnico
O estado nativo por jogador é um valor JSON-like que pode ser copiado uma vez na fronteira de ownership e congelado. Containers congelados compatíveis com `dict` e `list` preservam os contratos de leitura existentes, mas implementam `__deepcopy__` por identidade: cópias posteriores de envelopes de rollout compartilham o mesmo subtree imutável, em vez de reconstruí-lo.

#### Responsabilidade nova
- `freeze_snapshot` cria uma cópia recursivamente imutável do subtree nativo do jogador.
- `Trainer._expand_lobby_snapshot_metadata` transfere o subtree congelado para a linha do jogador.
- `RolloutBuffer` pode continuar usando sua fronteira defensiva de `deepcopy` para metadados mutáveis; subtrees congelados são compartilhados com segurança.
- Leitores continuam recebendo envelopes mutáveis isolados nas partes que não são snapshot nativo.

#### Contratos e invariantes
- O snapshot de origem não é compartilhado mutavelmente com o rollout.
- Dicts e listas mantêm compatibilidade de leitura e os tipos reconhecidos por consumidores existentes.
- Qualquer tentativa de mutação em qualquer nível do subtree congelado falha explicitamente.
- `deepcopy` de um subtree congelado retorna a mesma referência imutável; isso preserva aliases sem duplicar conteúdo.
- Identidade de Engine, episódio, sequência, jogador, contrato e hashes continuam validados como antes.
- Não são removidos campos, validações, eventos, provenance ou snapshots de auditoria.

#### Impactos e limites
A primeira cópia continua ocorrendo na fronteira de ownership, mas as cópias profundas subsequentes feitas pelo armazenamento e leitura de metadados do rollout deixam de duplicar o estado nativo do jogador. Metadados mutáveis e envelopes continuam isolados por cópia. Esta otimização não substitui a compactação dos demais payloads nem declara a Fase C concluída.

#### Validação
- provar isolamento em relação à fonte mutável;
- provar imutabilidade recursiva de dicts e listas;
- provar identidade compartilhada após `deepcopy`;
- executar testes de identidade do rollout e toda a suíte de integração nativa/Python.
 
### Validação
- testar layout completo e ordem de todos os campos;
- provar que as views internas compartilham memória com o buffer e que cópias públicas não compartilham;
- rejeitar dtype/shape incompatíveis;
- executar a suíte de paridade nativa e Python com o módulo compilado;
- comparar paridade funcional das máscaras antes/depois para todas as famílias de ação cobertas pela suíte.
