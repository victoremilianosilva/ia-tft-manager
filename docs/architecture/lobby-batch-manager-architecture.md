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

#### Snapshot nativo lazy e compartilhável
- `_NativeSnapshotMapping` mantém o handle nativo `const` como autoridade, materializa o dicionário base apenas na primeira leitura e congela recursivamente o resultado.
- Eventos de combate continuam em caches separados e lazy; quando solicitados, também são congelados.
- `deepcopy` do envelope de snapshot reutiliza o mesmo mapping imutável e pinado, em vez de clonar a árvore materializada.
- A superfície de leitura continua compatível com `Mapping`/`dict` e `list`; mutações são rejeitadas explicitamente.

#### Problema anterior
A expansão do snapshot da lobby copiava profundamente cada registro de jogador para criar as linhas do rollout. Em seguida, o `RolloutBuffer` copiava novamente esses subtrees ao assumir ownership e voltava a copiá-los ao expor metadados. O conteúdo nativo é evidência de auditoria associada a uma identidade de snapshot e não deve ser mutável pelo Trainer ou por consumidores do buffer.

#### Racional técnico
O estado nativo por jogador é um valor JSON-like que pode ser copiado uma vez na fronteira de ownership e congelado. Containers congelados compatíveis com `dict` e `list` preservam os contratos de leitura existentes, mas implementam `__deepcopy__` por identidade: cópias posteriores de envelopes de rollout compartilham o mesmo subtree imutável, em vez de reconstruí-lo.

#### Fronteira de masks no caminho quente do PPO
- O wrapper mantém o buffer nativo `[8, 1280]` como fonte de verdade e valida dtype/shape no momento de consumir o resultado, sem expandi-lo em mappings.
- `get_packed_action_masks_for_training()` empresta a matriz contígua e somente leitura ao Trainer.
- `Trainer._flatten_masks` reconhece buffers compactos, valida o layout completo e cria os tensores por campo diretamente a partir das fatias do buffer; o caminho antigo de mappings permanece apenas para fixtures/adapters.
- A ablação explícita de ações de item copia o buffer somente quando precisa alterar os nove bits de tipo; sem ablação, não há cópia no wrapper.
- A API pública estruturada e `get_action_masks_for_training()` permanecem disponíveis para compatibilidade.

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


### Fase C — validação semântica sem materialização duplicada

#### Problema anterior
O wrapper convertia seis blocos de features de itens de cada jogador em arrays NumPy temporários para verificar shape e finitude. No fluxo nativo do Trainer, a projeção semântica executa novamente a validação desses mesmos blocos e ainda aplica a faixa canônica `[0, 1]`. A conversão intermediária não alimentava nenhum consumidor: era uma materialização descartável antes da projeção.

#### Racional técnico
A validação estrutural do envelope e das identidades do snapshot continua no wrapper. Para snapshots nativos pinados, a validação semântica dos blocos de features fica concentrada em `project_native_player_state`, que já é a autoridade antes da criação dos tensores PPO e verifica tipo numérico, dimensões, finitude e faixa. Fixtures e snapshots construídos em Python não possuem a mesma fronteira de produtor nativo e mantêm a validação defensiva integral no wrapper.

#### Responsabilidade nova
- `CppTFTLobbyWrapper._copy_native_state_snapshot` preserva validações de contrato, identidade, ownership e integridade estrutural.
- `project_native_player_state` é a autoridade única para validar os seis blocos numéricos semânticos consumidos pelo PPO.
- O wrapper não cria arrays NumPy temporários desses blocos quando recebe `_NativeSnapshotMapping`.
- O caminho dict-backed mantém a validação de shape e finitude para fixtures e adapters.

#### Contratos e invariantes
- Nenhum campo, dimensão, regra semântica ou validação de identidade é removido do fluxo PPO.
- A projeção semântica continua rejeitando shape incorreto, valores não finitos e valores fora de `[0, 1]`.
- Snapshots dict-backed continuam sendo validados integralmente pelo wrapper.
- Nenhum snapshot é aceito pelo Trainer para PPO sem passar pela projeção semântica.
- A validação de pool, eventos, UUIDs, ownership de itens, estado de bigorna e provenance permanece no wrapper.
- A mudança não altera rewards, masks, observações, checkpoints ou a semântica das ações.

#### Impactos e limites
Para snapshots nativos, deixa de haver a conversão de seis matrizes/listas por jogador em arrays NumPy descartáveis durante a validação do wrapper. O custo da validação semântica permanece no estágio de projeção, onde os dados são efetivamente convertidos para a representação PPO. A melhoria esperada é redução de alocações temporárias e trabalho duplicado; não é declarada uma redução de latência end-to-end sem novo benchmark.

#### Fronteira de confiança e consumidores
O snapshot nativo pinado pode ser lido por consumidores de auditoria/proveniência antes da projeção; isso não significa que seus seis blocos semânticos estejam validados para uso neural. Esses consumidores usam fatos estruturais/ownership/eventos e não podem alimentar tensores ou decisões da policy diretamente. A única entrada dos campos semânticos no PPO é `build_semantic_batch`, que projeta cada linha por `project_native_player_state` antes da criação dos tensores.

O Trainer usa `build_semantic_batch` tanto para o snapshot da decisão atual quanto para o snapshot da próxima observação. O cache semântico só pode ser reutilizado quando a identidade imutável do snapshot coincide com a identidade da projeção já construída; a validade do cache depende do contrato nativo de que o conteúdo não muda sem avançar a sequência. Snapshots de resultado usados apenas para eventos factuais/auditoria não são considerados entradas PPO.

#### Validação
- confirmar que o wrapper continua rejeitando blocos inválidos em snapshots dict-backed;
- confirmar que snapshots nativos passam pelo wrapper sem materialização NumPy redundante;
- confirmar que `build_semantic_batch` rejeita blocos inválidos no mesmo caminho usado para snapshots atuais e próximos antes da criação dos tensores PPO;
- confirmar que o projetor individual permanece a autoridade de shape, tipo numérico, finitude e faixa [0, 1];
- executar testes de snapshot binding, projeção semântica, paridade nativa e smoke PPO.


### Fase C — ownership único dos envelopes canônicos de identidade

#### Problema anterior
Durante _expand_lobby_snapshot_metadata, cada envelope canônico de identidade era copiado profundamente para o registro do jogador. Na sequência, RolloutBuffer.add fazia outra cópia profunda do conjunto completo de metadados para assumir ownership. O primeiro clone era redundante: o buffer já é a fronteira definitiva de ownership, e o envelope não é alterado entre expansão, validação semântica e armazenamento.

#### Racional técnico
Os envelopes são dados JSON-like usados como evidência imutável de correlação. freeze_snapshot cria uma cópia recursivamente imutável compatível com dict/list e cujo __deepcopy__ reutiliza a mesma referência. Assim, a expansão continua isolando o envelope da origem, mas o deepcopy agregado do RolloutBuffer não duplica novamente sua árvore. O restante dos metadados continua atravessando a cópia defensiva de ownership existente.

#### Responsabilidade nova
- Trainer._expand_lobby_snapshot_metadata congela o envelope canônico uma única vez ao anexá-lo à linha do jogador.
- RolloutBuffer.add continua sendo a fronteira de ownership para os metadados completos da transição; sua cópia agregada compartilha o envelope congelado.
- RolloutBuffer.get_batches(include_metadata=True) continua expondo referências do buffer sob contrato read-only; o envelope agora também impede mutações acidentais em profundidade.

#### Contratos e invariantes
- O envelope armazenado permanece isolado do envelope fornecido pelo produtor.
- A identidade canônica conserva exatamente os mesmos campos, namespaces, valores e vínculos de Engine/episódio/jogador/sequência.
- O envelope é compatível com os consumidores existentes que verificam dict/list e com validate_player_identity_envelope.
- deepcopy posterior do envelope retorna a mesma referência imutável.
- Metadados mutáveis fora do envelope continuam protegidos pela cópia agregada do RolloutBuffer.
- Nenhuma identidade, provenance, evento, snapshot ou validação é removida.

#### Impactos e limites
São eliminadas as cópias profundas duplicadas dos envelopes canônicos no caminho de coleta. A expansão ainda faz uma cópia para estabelecer ownership imutável; a cópia agregada posterior do rollout reutiliza esse subtree. Não há alegação de ganho end-to-end até repetir o profiler com PPO ativo e comparar alocações/tempo do caminho completo.

#### Validação
- provar que o envelope expandido é FrozenDict compatível e preserva igualdade com a origem;
- provar que deepcopy do envelope congelado reutiliza a identidade;
- provar que mutações no envelope congelado são rejeitadas;
- manter a cobertura existente de isolamento da entrada no RolloutBuffer, identidade de transição e auto-reset terminal;
- executar testes de identidade do rollout, snapshot nativo, semantic alignment e smoke PPO.


### Fase C — compartilhamento do estado nativo entre resultado e próxima observação

#### Problema anterior
Após cada step, o Trainer expande separadamente o snapshot de resultado da Engine e o snapshot da próxima observação. Em transições não terminais, ambos podem representar a mesma revisão nativa. A expansão congelava novamente o subtree do jogador em cada passagem, duplicando alocações e retenção de uma estrutura grande antes mesmo do RolloutBuffer.

#### Racional técnico
A identidade nativa composta por Engine, episódio, sequência do snapshot, round, sequência individual e jogador identifica uma revisão imutável. O Trainer agora mantém um cache local à transição e reutiliza o subtree congelado quando a segunda expansão apresenta exatamente essa mesma identidade. O cache também verifica a identidade do contrato/produtor; divergência contratual para a mesma chave falha explicitamente. O escopo local impede compartilhamento entre transições distintas.

#### Responsabilidade nova
- Trainer cria um cache efêmero por resultado de step.
- _expand_lobby_snapshot_metadata valida os campos do snapshot e consulta o cache antes de congelar novamente o estado do jogador.
- O cache é descartado após a expansão de resultado/próxima observação e não se torna estado persistente do Trainer ou da Engine.

#### Contratos e invariantes
- Apenas revisões com lobby, Engine, episódio, sequência, round, jogador e sequência individual idênticos podem compartilhar o subtree; a partição por lobby impede alias mesmo diante de identificadores de Engine duplicados em fixtures ou entradas inválidas.
- Contrato, versão, produtor e namespace de origem precisam coincidir para reutilização.
- Episódios auto-reset e revisões posteriores nunca compartilham estado por coincidência de jogador.
- O subtree continua recursivamente imutável e isolado da origem.
- Identidade canônica, action trace, provenance, eventos, rewards, masks e semântica PPO permanecem inalterados.
- Não há cache entre chamadas de step nem entre lobbies/episódios.

#### Impactos e limites
Elimina uma segunda materialização do subtree nativo quando resultado e próxima observação apontam para a mesma revisão. O benefício efetivo depende da frequência dessas transições e será quantificado pelo profiler end-to-end; não se declara ganho de throughput sem essa medição.

#### Validação
- duas mappings independentes da mesma revisão reutilizam a mesma referência congelada por jogador;
- episódio ou round diferente não reutiliza o subtree;
- divergência de contrato para a mesma chave falha explicitamente;
- linhas de lobby distintas nunca compartilham subtrees;
- manter testes existentes de auto-reset, alinhamento de snapshots, identidade e PPO smoke;
- executar CI Python/nativo e comparar métricas de alocação/tempo após merge.


### Fase C — comparação estrutural com curto-circuito de subtrees compartilhados

#### Problema anterior
Ao armazenar uma transição, RolloutBuffer.add compara os metadados de resultado e próxima observação para internar envelopes iguais. A comparação genérica left == right percorre recursivamente estruturas grandes mesmo quando native_player_state já é a mesma referência congelada, compartilhada pela otimização anterior. Esse trabalho não cria informação nova e pode consumir CPU proporcional ao tamanho do snapshot em cada jogador/transição.

#### Racional técnico
A comparação passa a ser estrutural e recursiva para mappings e sequências JSON-like. A identidade de objeto é verificada primeiro: referências idênticas são iguais sem percorrer seus descendentes. Valores não compartilhados continuam comparados recursivamente; tipos/valores incompatíveis continuam resultando em desigualdade. Resultados de igualdade não escalares e exceções continuam sendo tratados defensivamente como não iguais.

#### Responsabilidade nova
- RolloutBuffer._metadata_values_equal compara estruturas JSON-like e interrompe a recursão em qualquer subtree já compartilhado por identidade.
- A rotina de armazenamento continua responsável por internar apenas envelopes integralmente iguais antes da cópia defensiva de ownership.

#### Contratos e invariantes
- Igualdade estrutural preserva a semântica para dicts, listas e tuplas; listas e tuplas são comparadas por conteúdo e comprimento, conforme o comportamento de igualdade Python.
- Uma referência idêntica pode ser reutilizada sem inspecionar seus descendentes porque não houve alteração de objeto entre os dois envelopes.
- Diferenças em qualquer campo mutável continuam impedindo o interning.
- Valores cuja igualdade gere resultado ambíguo ou exceção continuam sendo tratados como diferentes.
- A cópia defensiva agregada do RolloutBuffer e o isolamento de metadados mutáveis permanecem inalterados.

#### Impactos e limites
Evita percorrer novamente subtrees nativos congelados que já foram compartilhados entre resultado e próxima observação. O custo restante depende dos metadados mutáveis e da estrutura de cada envelope. Não há alegação de ganho end-to-end antes da repetição do profiler com PPO ativo.

#### Validação
- provar que subtrees compartilhados por identidade não invocam igualdade profunda;
- provar que diferenças em campos aninhados são detectadas;
- provar tratamento defensivo de igualdade não escalar;
- manter testes de isolamento, imutabilidade, identidade, auto-reset e paridade do rollout;
- executar CI Python/nativo e comparar o tempo de rollout.add e alocações no profiler completo.


#### Correção de equivalência entre sequências
A comparação estrutural não mistura listas e tuplas: cada família é comparada recursivamente apenas com a mesma família, preservando a semântica nativa do Python (`[1] != (1,)`). `FrozenList` continua compatível com listas por herança, sem perder o short-circuit por identidade.


### Fase C — contexto compartilhado da projeção semântica

#### Problema anterior
build_semantic_batch projetava cada jogador de forma independente. Cada chamada recriava o dicionário do catálogo de campeões, reconstruía o conjunto de IDs conhecidos e calculava novamente SHA-256 para traits estáveis repetidos entre jogadores do mesmo batch. Esses dados são invariantes durante a projeção de um batch e não exigem recomputação por jogador.

A auditoria também identificou validações estruturais no wrapper e validações semânticas no projetor que observam alguns campos relacionados. A sobreposição aparente, por si só, não prova que as verificações sejam redundantes: o wrapper protege a fronteira do snapshot e o projetor protege a entrada do PPO.

#### Racional técnico
O batch cria um contexto efêmero contendo uma única cópia normalizada do catálogo, o conjunto imutável de IDs conhecidos e um cache de hashes de traits. O contexto é compartilhado somente pelas projeções daquela chamada. Os hashes continuam sendo SHA-256 e produzem exatamente os mesmos buckets do contrato semântico v8.

A validação estrutural do wrapper e a validação semântica do projetor permanecem intactas nesta entrega. Remover verificações entre fronteiras sem uma prova de autoridade equivalente poderia aceitar snapshots malformados antes de chegarem ao PPO.

#### Responsabilidade nova
- build_semantic_batch prepara o contexto uma vez e o fornece às projeções individuais.
- project_native_player_state continua sendo a autoridade semântica e mantém o mesmo comportamento quando chamado isoladamente.
- O cache de traits é local ao batch e não é retornado, persistido no Trainer ou compartilhado entre batches.
- CppTFTLobbyWrapper._copy_native_state_snapshot continua responsável pela integridade estrutural, identidade, ownership e provenance do snapshot.

#### Contratos e invariantes
- O catálogo normalizado representa exatamente os mesmos pares nome/ID fornecidos ao projetor.
- O conjunto de IDs conhecidos é derivado da mesma cópia normalizada e não pode ser alterado durante a projeção.
- Cada trait mantém o bucket SHA-256(UTF-8(trait)) módulo SEMANTIC_TRAIT_VOCAB_SIZE, com o deslocamento canônico de padding.
- Cache de hash não cruza chamadas de batch nem altera hashes de projeção, identidade, champion IDs ou features numéricas.
- O projetor individual continua aceitando chamadas sem contexto compartilhado.
- Nenhuma validação estrutural ou semântica, contrato, provenance ou regra de aceitação de snapshot é removida.
- O contrato semântico v8, dimensões, pesos, rewards, masks e checkpoints permanecem inalterados.

#### Impactos e limites
Elimina a cópia do catálogo e a reconstrução do conjunto de IDs para cada jogador, além de evitar SHA-256 repetido para o mesmo trait dentro do batch. Não elimina o percurso dos slots nem a validação semântica individual, que continuam necessárias para produzir e autenticar cada linha do PPO. A economia end-to-end precisa ser confirmada pelo profiler com PPO ativo.

#### Validação
- Comparar features numéricas, champion IDs e hashes entre projeção individual e batch.
- Provar que cada trait repetido é hasheado uma única vez dentro do batch.
- Provar que batches independentes não compartilham cache.
- Manter os testes de rejeição de contratos, sequências, ownership, features de itens e provenance.
- Executar testes de projeção semântica, alinhamento de rollout, snapshot binding e smoke PPO.
- Repetir o profiler completo e comparar semantic.build_batch, semantic.project_player, alocações e tempo end-to-end.


## Snapshot validation profiling findings and cleanup

**Prior problem.** The end-to-end profiler showed a material
`wrapper.snapshot_validation` cost, but the wrapper exposed only one aggregate
measurement. Temporary per-stage timers were added to identify where that time
was concentrated.

**Observed evidence.** In the four-lobby run (32 players), the measured stage
totals were approximately 50.95 seconds: 32.26 seconds in the envelope /
identity / provenance interval (63.3%), 12.14 seconds in player units and slots
(23.8%), 4.51 seconds in strategic-owner checks (8.8%), 1.77 seconds in item
ownership (3.5%), and 0.21 seconds in shared pool and events (0.4%).

**Measurement limitation.** The envelope interval begins before the first
non-combat field access on `_NativeSnapshotMapping`. That first access lazily
materializes the native snapshot through `to_dict()` and `freeze_snapshot()`.
Consequently, the 32.26-second bucket is not pure envelope validation; it also
includes first-touch materialization. The result identifies lazy materialization
as the next investigation target, but does not prove that the identity checks
themselves are expensive or redundant.

**Technical rationale and cleanup.** The temporary timers served their
diagnostic purpose and have been removed from the wrapper and end-to-end
profiler. The metrics-only accessor and its metrics-specific test were removed
as well. This cleanup does not change the snapshot mapping, materialization,
validation order, or validation rules.

**Contract and invariants.** Snapshot contract/version, geometry, provenance,
engine/episode/round identity, decision sequences, shared-pool/event contracts,
player and slot ownership, UUID uniqueness, item ownership, strategic-owner
contracts, and planner invariants remain enforced by the existing validation
path. No validation is skipped, weakened, cached, or moved.

**Impact and validation criteria.** Runtime validation no longer performs the
temporary per-stage timer bookkeeping or maintains per-wrapper timing counters.
Existing snapshot rejection and semantic-projection tests remain the validation
gate. Any future optimization of lazy materialization must preserve the exact
snapshot values, immutability, identity correlation, and all existing rejection
behavior.


## Lazy native snapshot materialization findings

**Prior problem.** The previous snapshot-validation profile grouped the first
non-combat field access on `_NativeSnapshotMapping` with envelope validation.
That first access lazily performs native `to_dict()` conversion followed by
`freeze_snapshot()`, so the aggregate could not distinguish those costs.

**Observed evidence.** The isolated PPO-enabled profile on 25 November 2026
recorded 34, 68, and 136 actual materializations for 1, 2, and 4 lobbies
respectively. In the four-lobby run, `to_dict()` took 7.59 s total (55.8 ms
per materialization) and `freeze_snapshot()` took 27.71 s (203.7 ms per
materialization). Together they account for approximately 35.30 s, or
259.6 ms per first materialization. The measured `base_dict_total` wrapper
was called 24,672 times because it also includes cache-hit accesses; its
35.66 s aggregate must not be interpreted as 24,672 materializations.

**Technical conclusion.** Within the measured first-touch work, recursive
freezing is the larger component (about 78.5%) and native conversion accounts
for about 21.5%. This identifies `freeze_snapshot()` as the first candidate
for a focused investigation, not as proof that freezing can be skipped or
replaced. The semantic projection remains the largest measured stage at
87.51 s for four lobbies (1,088 player projections, about 80.4 ms each).

**Responsibility and contracts.** `_NativeSnapshotMapping` remains responsible
for lazy materialization and stable cached access. At this measurement point,
the native handle supplied the canonical snapshot and Python
`freeze_snapshot()` supplied the immutable representation. The follow-up
implementation is recorded below. No validation, identity, provenance,
sequence, ownership, or snapshot acceptance rule is changed by these findings.

**Profiling cleanup and limits.** The temporary monkeypatch and timing metrics
have been removed from `scripts/profile_training_pipeline.py`; only the
durable findings remain here. Timings are profiler-instrumented and inclusive
where documented; nested durations must not be added to wrapper validation.
The measurement does not decompose internal C++ work or fully capture native
allocator memory. It is diagnostic evidence, not a performance guarantee.

**Next validation criteria.** Any proposed optimization must preserve lazy
cache behavior, exact snapshot values, immutability, identity correlation, and
all existing rejection behavior. Compare the end-to-end PPO profile and run
snapshot binding, semantic projection, rollout alignment, and PPO smoke tests
before accepting a functional change.

## Safe native snapshot materialization

**Prior problem.** The lazy native snapshot handle previously serialized the
same pinned `AuditSnapshot` into a new mutable Python tree on repeated field
access. The benchmark showed that first-touch serialization and recursive
freezing were a material part of snapshot validation cost.

**Technical rationale.** A native snapshot is immutable and pinned by
`shared_ptr<const AuditSnapshot>`. The handle can therefore cache one frozen
Python view for its lifetime. This removes repeated serialization/freezing
for subsequent reads without changing the established, tested conversion
boundary.

**Rejected implementation.** An attempted optimization built `FrozenDict`
and `FrozenList` directly with CPython C-API container operations. The
native integration workflow reproducibly terminated with a segmentation
fault while reading the snapshot. That builder path was removed rather than
treating a process crash as an acceptable trade-off.

**New responsibility.** `NativeAuditSnapshotHandle.to_dict()` now creates
the established mutable serialization once, freezes it through
`immutable_snapshot.freeze_snapshot()`, and caches the immutable result.
`_NativeSnapshotMapping` continues to cache field access and lazily
materialize combat-event rows. The public `get_audit_snapshot()` serializer
remains unchanged.

**Contracts and invariants.**
- The handle continues to pin `shared_ptr<const AuditSnapshot>`.
- The cached view remains recursively immutable and compatible with
  `dict`/`list` consumers through `FrozenDict`/`FrozenList`.
- Repeated reads reuse the same frozen view; no repeated full-tree
  serialization or freezing occurs for the same handle.
- Combat event access remains lazy and separately cached.
- Snapshot identity, provenance, sequence validation, schema, and
  `deepcopy` sharing remain unchanged.

**Impact.** This restores the safe conversion path while retaining the
per-handle cache. It does not claim the larger direct-construction speedup:
the mutable intermediate tree and initial Python freezing pass remain.
The A/B benchmark must measure whether caching alone provides a worthwhile
end-to-end improvement before another native construction strategy is tried.

**Validation criteria.** CI must compile the binding and pass the native
engine integration, snapshot binding, semantic projection, rollout alignment,
and PPO contract tests. Tests verify one freeze per handle, stable cached
identity, structural parity with the public getter, immutability, and lazy
combat access. Benchmark comparison remains a separate user-run step.


## Native player snapshot views

**Prior problem.** The native handle materialized all eight player subtrees into one Python dictionary tree before the training pipeline could select a player. Recursive freezing then traversed every player subtree together, even though training expands and consumes players individually.

**Technical rationale.** Player records are independently addressable inside the pinned immutable `AuditSnapshot`. The binding can serialize one requested player at a time while retaining the same native snapshot owner. Python exposes that access as a read-only sequence, preserving indexing and iteration for consumers without requiring an eager list of all eight player dictionaries.

**New responsibility.** `NativeAuditSnapshotHandle` owns the native player sequence and exposes bounded `player_count()` / `player(index)` access. Its dedicated `to_envelope_dict()` excludes the player collection, while the established public `to_dict()` remains complete and includes all players. `_NativeSnapshotPlayers` caches and freezes each player only on first access. `_NativeSnapshotMapping` combines the envelope with this lazy sequence. Python-backed fixture handles keep the legacy complete-dictionary fallback. `Trainer` consumes the sequence protocol and reuses an already-frozen player record rather than freezing it again.

**Contracts and invariants.**
- The handle continues to pin `shared_ptr<const AuditSnapshot>`; the Python sequence retains the handle for the lifetime of its player views.
- Player count remains exactly the native lobby cardinality (eight); indices are bounds-checked.
- Player identity, strategic owner context, board/bench/shop slots, item ownership, and all snapshot fields retain their existing serialized names and values.
- The public eager `get_audit_snapshot()` and `NativeAuditSnapshotHandle.to_dict()` APIs remain complete and unchanged in shape, including the diagnostic masks exposed by `get_audit_snapshot()`.
- Training receives no action-mask copy through the player snapshot; masks remain available through the dedicated packed-mask API.
- Fixture-backed mappings remain supported during migration.

**Impact.** The training adapter requests the dedicated native envelope and does not build or freeze the player collection as part of that read. Each player subtree is exposed by index and frozen on first Python access, with repeated reads reusing the same immutable object. The public `to_dict()` path remains intentionally eager for callers that request the complete snapshot. This is an incremental lazy-materialization boundary, not yet a zero-copy typed C++ view; it does not claim that the per-player conversion/freeze cost has disappeared.

**Validation criteria.** Native binding tests verify envelope caching, lazy per-player materialization, per-player cache identity, structural parity with the public getter after excluding its diagnostic-only action masks, bounds behavior, and immutable nested player data. Wrapper validation, semantic projection, rollout alignment, and PPO contract tests must remain green. End-to-end performance claims require a separate PPO-enabled benchmark.
