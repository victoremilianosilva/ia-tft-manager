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
Esta entrega adiciona a API e ownership nativos sequenciais, mas ainda não substitui o caminho do `Trainer`: integrar os wrappers e `LobbyVectorEnv` à API batch será uma etapa própria, com comparação old/new para seeds e ações idênticas. Nenhum ganho de throughput é alegado nesta fase. A API converte resultados para os mesmos dicionários/arrays já usados pelo binding atual; a fronteira compacta é escopo da Fase C.

## Validação
- rejeitar zero lobbies, seed inválida/overflow e batches com dimensões inválidas;
- confirmar IDs distintos e estáveis;
- comparar reset/step batch com execução direta por Engine para seeds e ações idênticas;
- confirmar falha de lifecycle antes do reset e após close;
- executar suíte C++ e testes Python com o módulo `tft_engine` compilado.
