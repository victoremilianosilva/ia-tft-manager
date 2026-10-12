# Roadmap oficial consolidado — IA TFT

> Este arquivo usa o roadmap fornecido pelo usuário como fonte oficial. As tarefas complementares foram incluídas somente quando acrescentam algo que ainda não estava coberto, evitando duplicações. Itens sem evidência suficiente permanecem pendentes.

## Fase 1 — Arquitetura e responsabilidades

**Objetivo:** estabelecer uma base modular para o ambiente de treinamento.

- [x] Definir as responsabilidades do `MiniTFTEnv`.
- [x] Estruturar o `TFTLobby` e a lógica global da partida.
- [x] Separar `SHOP`, `ECONOMY`, `UNITS` e `STRATEGY`.
- [x] Integrar `UnitManager` e `UnitPool` compartilhados.
- [x] Conferir contratos de observação, ação, recompensa e reset.

## Fase 2 — Lobby completo com 8 jogadores

- [x] Criar o lobby com oito jogadores.
- [x] Manter o estado de cada jogador e o estado global da partida.
- [x] Estruturar pareamento de jogadores e avanço de rounds.
- [x] Validar partidas completas, incluindo reset e eliminação.
- [x] Garantir que nenhum jogador eliminado continue influenciando o fluxo da partida.
- [x] Testar diferentes sequências de pareamento e situações-limite.

## Fase 3 — Combate PvP e motor C++

- [x] Implementar a extensão `combat_engine` em C++ com bindings via pybind11.
- [x] Configurar a compilação com CMake no Windows.
- [x] Confirmar que o Python importa o módulo compilado.
- [x] Passar o teste `tests/teste_integracao_combate_cpp.py`.
- [x] Validar o combate integrado ao `TFTLobby`.
- [x] Validar dano ao jogador, vitória, derrota, empate e eliminação.
- [x] Testar timeout, movimentação, dano e resultados individuais.
- [x] Confirmar que a simulação é determinística quando configurada para isso.
- [x] Medir tempo médio de combate e eventos processados.

## Fase 4 — Máscaras de ação, anti-loop e desempenho

### 4.1 — Auditoria das máscaras

- [x] Implementar correções no `ActionMaskManager.py`.
- [x] Validar dimensões e tipos das máscaras.
- [x] Validar máscaras condicionais de movimento no tabuleiro.
- [x] Validar movimentação banco → tabuleiro e tabuleiro → tabuleiro.
- [x] Garantir que sempre exista uma ação válida para o PPO.
- [x] Confirmar que a máscara usada na coleta é compatível com a usada na atualização do PPO.

### 4.2 — Anti-loop e regressões

- [x] Corrigir o `AntiLoopManager` e comitar a alteração.
- [x] Executar testes de regressão anteriores reportados como aprovados.
- [x] Reexecutar as regressões na configuração atual da máquina.
- [x] Confirmar que o anti-loop não bloqueia ações realmente úteis.
- [x] Instrumentar métricas de execução e bloqueios no TensorBoard.
- [ ] Validar os contadores em cenários controlados com bloqueios reais.
- [ ] Confirmar que as métricas representam contagens e taxas com a interpretação correta.

### 4.2.1 — Alinhar o anti-loop ao aprendizado

- [x] Auditar as regras atuais do `AntiLoopManager.py`.
- [x] Auditar a aplicação das regras no `ActionMaskManager.py`.
- [x] Validar se `is_bench_board_loop()` bloqueia apenas movimentos que efetivamente perpetuam o ciclo, sem impedir outras ações úteis da unidade.
- [x] Revisar `is_cycle_move()` para garantir que a detecção respeite a sequência cronológica dos movimentos e não identifique ciclos a partir de transições desconexas.
- [x] Validar a detecção de oscilações envolvendo `board_swap`, garantindo que trocas úteis não sejam bloqueadas apenas pelo histórico de outras unidades.
- [x] Investigar e corrigir o possível bloqueio de `MOVE_BOARD` quando há apenas uma unidade no tabuleiro e existem destinos vazios válidos.
- [x] Revisar o tratamento de exceções nas consultas ao `AntiLoopManager` dentro do `ActionMaskManager`, garantindo que falhas sejam diagnosticáveis sem comprometer a validade das máscaras.
- [x] Adicionar testes de regressão para os bloqueios indevidos identificados na auditoria, preservando os testes existentes.
- [x] Confirmar que movimentos válidos continuam disponíveis após um bloqueio, inclusive quando o estado do jogo muda e o movimento anteriormente bloqueado passa a ser útil.
- [x] Bloquear ciclos persistentes sem impedir movimentos para estados novos.
- [x] Verificar o tratamento de ciclos envolvendo swaps, nos quais duas unidades trocam de posição.
- [x] Garantir que consultas de máscara não alterem contadores de execução.
- [x] Reutilizar os testes de regressão existentes.
- [x] Adicionar testes apenas para comportamentos relevantes ainda não cobertos.

### 4.3 — Integração com PPO

- [x] Auditar as seis dimensões da ação: `[7, 5, 9, 28, 28, 28]`.
- [x] Otimizar Maks
- [x] Conferir as máscaras condicionais para cada cabeça da política.
- [x] Verificar cálculo de probabilidades e log-probabilidades com máscaras.
- [x] Testar a consistência das máscaras entre `get_action_and_value` e `evaluate_actions` para os tipos de ação cobertos pelos testes reportados.
- [x] Testar `evaluate_actions` durante a atualização do PPO em treinamento.
- [x] Confirmar que não há NaN, distribuições inválidas ou ações impossíveis.

### 4.4 — Desempenho e avaliação controlada

- [x] Medir o custo de `get_action_masks()` por jogador.
- [x] Medir tempo de `env.step()` e de cada combate.
- [x] Medir throughput de steps por segundo.
- [x] Identificar gargalos antes de otimizar.

### 4.5 — Migração das Masks e dos Gargalos de Decisão para C++

**Objetivo:** Migrar a geração das Action Masks, a validação de movimentos e o AntiLoop para um módulo nativo em C++, mantendo o PPO, a política neural, o treinamento e a orquestração do ambiente em Python.

A migração deverá preservar o comportamento atual da IA, incluindo todas as regras, correções, proteções anti-loop, máscaras condicionais e melhorias implementadas anteriormente.

**Princípio fundamental:** o código Python atual não será removido nem deixará de funcionar durante a migração. A implementação C++ será validada em paralelo e somente assumirá o fluxo principal após cumprir todos os critérios de equivalência, integração, estabilidade e desempenho.

**Escopo da migração:**
- Geração das Action Masks.
- Validação de ações e movimentos.
- AntiLoop e gerenciamento dos bloqueios de movimentos.
- Validação de movimentos do tabuleiro e do banco.
- Interface Python/C++ e transferência eficiente de dados.
- Testes de equivalência, integração, regressão e desempenho.

**Fora do escopo:**
- Migração da política PPO ou da rede neural para C++.
- Alteração da arquitetura de ações aprendida pela política.
- Reescrita da economia, recompensas, combate ou progressão do jogo.
- Remoção antecipada do código Python de referência.

---

##### Fase 1 — Auditoria do código atual e definição do contrato

**Objetivo:** documentar o comportamento atual antes de implementar a versão nativa.

**Tarefas:**
- [x] Inspecionar `ai/ActionMaskManager.py`.
- [x] Inspecionar `ai/AntiLoopManager.py`.
- [x] Inspecionar `lobby/TFTLobby.py`.
- [x] Inspecionar `env.py` e os pontos de integração com as máscaras.
- [x] Inspecionar `trainer.py`, `policy.py` e os testes relacionados à consistência das ações.
- [ ] Mapear todas as funções responsáveis por gerar, validar e bloquear ações.
- [ ] Identificar todas as dependências entre Action Masks, AntiLoop, estado do jogador, unidades, posições e histórico de movimentos.
- [ ] Documentar todas as regras atuais de validação de movimentos do tabuleiro e do banco.
- [ ] Documentar regras de bloqueio de reversões, oscilações, ciclos, movimentos repetidos e demais proteções existentes.
- [ ] Mapear a identidade das unidades e os critérios usados para detectar movimentos equivalentes.
- [ ] Documentar a ordem de geração e aplicação das máscaras condicionais da política autoregressiva.
- [ ] Confirmar o formato, as dimensões e os significados dos índices das máscaras atuais.
- [ ] Identificar os estados que precisam ser transferidos do Python para o C++ e os dados que precisam retornar.
- [ ] Identificar os efeitos colaterais e as atualizações de histórico que não podem ser perdidos durante a migração.
- [ ] Registrar casos representativos e casos extremos para comparação entre as implementações.
- [ ] Definir o contrato de entrada e saída do módulo nativo.
- [ ] Definir a estratégia de fallback e ativação controlada.
-[ ] Mapear todas as regras de precedência e conflitos: determinar o que acontece quando diferentes regras de bloqueio se aplicam simultaneamente e qual motivo de bloqueio prevalece.
-[ ] Documentar determinismo e estado mutável: identificar quais funções apenas consultam o estado e quais modificam históricos, caches, contadores ou outras estruturas.
-[ ] Definir critérios objetivos de equivalência: especificar como comparar as saídas Python/C++, incluindo máscaras, motivos de bloqueio, atualizações de estado e resultados em casos extremos.
-[ ] Registrar a linha de base de desempenho e o ambiente de referência: guardar as medições atuais, configurações, versões e metodologia para comparar o ganho após a migração.

**Entregáveis:**
- Mapa de dependências.
- Especificação do contrato Python/C++.
- Inventário das regras que precisam ser preservadas.
- Conjunto inicial de cenários de referência.

**Critério de conclusão:** todas as responsabilidades, dependências e regras necessárias para reproduzir o comportamento atual estão identificadas. Nenhuma implementação nativa começa com dependências críticas desconhecidas.

##### Fase 2 — Preparação da infraestrutura C++

**Objetivo:** criar uma base nativa independente, compilável e integrável ao projeto Python.

**Tarefas:**
- [ ] Definir a estrutura de diretórios do módulo `decision_engine`.
- [x] Configurar o sistema de build com CMake.
- [x] Selecionar e configurar uma versão compatível do C++.
- [x] Configurar os bindings Python/C++ com pybind11, caso confirmada a compatibilidade com o ambiente do projeto.
- [x] Configurar a compilação para os sistemas operacionais utilizados no desenvolvimento e treinamento.
- [ ] Definir os tipos compartilhados entre os componentes nativos.
- [ ] Definir estruturas explícitas para estado do jogador, unidades, posições, histórico e resultado.
- [ ] Definir convenções para índices, enums, valores ausentes e dimensões das máscaras.
- [ ] Definir tratamento de erros, validação de entradas e retorno de diagnósticos.
- [ ] Evitar dependências externas desnecessárias.
- [ ] Configurar testes nativos automatizados.
- [ ] Configurar a compilação do módulo a partir do ambiente Python utilizado pelo projeto.
- [ ] Documentar como compilar, importar e executar os testes do módulo.

**Entregáveis:**
- Estrutura inicial do módulo C++.
- Configuração de build reproduzível.
- Bindings iniciais funcionais.
- Testes básicos de compilação e importação.

**Critério de conclusão:** o módulo compila no ambiente-alvo, pode ser importado pelo Python e executa seus testes básicos sem alterar o funcionamento do projeto existente.

##### Fase 3 — Migração do validador de movimentos

**Objetivo:** reproduzir em C++ as regras de validade de movimentos utilizadas pela geração das máscaras.

**Tarefas:**
- [ ] Mapear as condições de `_is_valid_board_move()`.
- [ ] Mapear as condições de `_is_valid_bench_board_move()`.
- [ ] Migrar as regras de origem e destino no tabuleiro.
- [ ] Migrar as regras de ocupação e disponibilidade de posições.
- [ ] Migrar as restrições de movimentação entre banco e tabuleiro.
- [ ] Preservar as condições especiais e as exceções existentes.
- [ ] Preservar as regras relacionadas à identidade e à posição das unidades.
- [ ] Reproduzir a interação entre validação de movimentos e AntiLoop.
- [ ] Garantir que a validação não altere o estado real do jogo.
- [ ] Criar testes unitários para movimentos válidos e inválidos.
- [ ] Criar testes para posições ocupadas, posições vazias e unidades ausentes.
- [ ] Comparar os resultados do validador C++ com os resultados da implementação Python.
- [ ] Corrigir todas as divergências encontradas antes de avançar.

**Entregáveis:**
- Validador nativo de movimentos.
- Testes unitários e comparativos.
- Documentação das regras reproduzidas.

**Critério de conclusão:** o validador C++ produz os mesmos resultados que o Python para os cenários de referência, sem modificar o estado do ambiente.

##### Fase 4 — Migração do AntiLoop

**Objetivo:** reproduzir em C++ o comportamento completo das proteções contra movimentos repetitivos, reversões, oscilações e ciclos.

**Tarefas:**
- [ ] Mapear as funções públicas e privadas de `AntiLoopManager`.
- [ ] Migrar a geração das chaves de movimentos.
- [ ] Migrar a identificação das unidades.
- [ ] Migrar a detecção de movimentos inversos.
- [ ] Migrar a detecção de oscilações.
- [ ] Migrar a detecção de ciclos.
- [ ] Migrar as regras de bloqueio e os motivos associados.
- [ ] Preservar os critérios de comparação entre movimentos.
- [ ] Preservar o uso do histórico e das assinaturas de estado.
- [ ] Preservar os mecanismos de prevenção de loops entre banco e tabuleiro.
- [ ] Preservar todas as regras adicionais de bloqueio implementadas anteriormente.
- [ ] Reproduzir a ordem de avaliação das condições quando ela afetar o resultado.
- [ ] Garantir que verificações de bloqueio não atualizem o histórico indevidamente.
- [ ] Garantir que as atualizações legítimas do histórico ocorram no momento correto.
- [ ] Criar testes para reversões, oscilações, ciclos e movimentos repetidos.
- [ ] Criar testes para movimentos semelhantes executados por unidades diferentes.
- [ ] Criar testes para mudanças de estado que devem permitir novamente um movimento.
- [ ] Comparar decisões e motivos de bloqueio entre Python e C++.
- [ ] Corrigir todas as divergências identificadas.

**Entregáveis:**
- Núcleo AntiLoop nativo.
- Testes de equivalência do AntiLoop.
- Contrato documentado para estado e histórico.

**Critério de conclusão:** o AntiLoop C++ reproduz as decisões de bloqueio da implementação Python nos cenários de referência, preservando as regras e a evolução do histórico.

##### Fase 5 — Migração do gerador de Action Masks

**Objetivo:** migrar a construção das máscaras para C++, integrando o validador de movimentos e o AntiLoop nativos.

**Tarefas:**
- [ ] Mapear todas as funções de geração das máscaras em `ActionMaskManager`.
- [ ] Migrar a geração das máscaras de tipos de ação.
- [ ] Migrar a geração das máscaras de seleção da loja.
- [ ] Migrar a geração das máscaras do banco.
- [ ] Migrar a geração das máscaras de origem no tabuleiro.
- [ ] Migrar a geração das máscaras de destino no tabuleiro.
- [ ] Migrar a geração das máscaras de movimentação entre banco e tabuleiro.
- [ ] Migrar a geração das máscaras condicionais.
- [ ] Preservar a dependência entre as etapas autoregressivas da política.
- [ ] Preservar todas as restrições econômicas e de estado que influenciem as máscaras.
- [ ] Preservar as regras especiais e os casos de borda existentes.
- [ ] Integrar o validador de movimentos e o AntiLoop sem duplicar verificações desnecessárias.
- [ ] Evitar chamadas individuais entre Python e C++ para cada candidato de movimento.
- [ ] Processar os candidatos internamente em C++ e retornar os resultados em lote.
- [ ] Definir o formato exato de saída esperado pela política atual.
- [ ] Garantir dimensões, tipos, ordem dos índices e semântica idênticos aos atuais.
- [ ] Tratar estados inválidos ou inconsistentes sem produzir máscaras incorretas silenciosamente.
- [ ] Comparar cada componente da saída C++ com a saída Python.
- [ ] Corrigir todas as divergências antes de integrar o módulo ao fluxo principal.

**Entregáveis:**
- Gerador nativo de Action Masks.
- Integração interna com validador e AntiLoop.
- Testes de equivalência para todas as máscaras.

**Critério de conclusão:** o módulo C++ gera máscaras equivalentes às máscaras Python para os cenários de referência, preservando dimensões, índices, dependências condicionais e restrições de ações.

##### Fase 6 — Integração Python/C++ e execução paralela de validação

**Objetivo:** integrar o módulo nativo sem remover nem desativar o caminho Python existente.

**Tarefas:**
- [ ] Implementar a interface pública do `decision_engine`.
- [ ] Integrar os bindings ao ambiente Python.
- [ ] Implementar a conversão dos dados de entrada para os tipos nativos.
- [ ] Implementar a conversão da saída para o formato esperado pelo projeto.
- [ ] Validar o estado recebido antes de executar o cálculo.
- [ ] Evitar cópias desnecessárias de estruturas e dados entre linguagens.
- [ ] Preservar a ordem de execução e os pontos de atualização do histórico.
- [ ] Criar uma opção de configuração para selecionar a implementação Python ou C++.
- [ ] Manter Python como caminho padrão durante a validação inicial.
- [ ] Implementar um modo de comparação que calcule as duas saídas para o mesmo estado.
- [ ] Comparar as máscaras elemento por elemento.
- [ ] Comparar os resultados de validação e os bloqueios do AntiLoop.
- [ ] Registrar divergências com contexto suficiente para reproduzir o problema.
- [ ] Garantir que o caminho de comparação não altere duas vezes o histórico nem modifique o estado do jogo.
- [ ] Garantir que o resultado C++ ainda não substitua o resultado Python antes da aprovação.
- [ ] Testar a integração com `TFTLobby`, `MiniTFTEnv`, `TFTGymEnv` e `Trainer`, conforme aplicável.
- [ ] Testar o comportamento com múltiplos jogadores e múltiplas lobbies.
- [ ] Testar erros de importação, compilação, entrada inválida e falhas da interface.
- [ ] Validar que o fallback Python continua funcional.

**Entregáveis:**
- Integração nativa com seleção de backend.
- Modo de comparação Python/C++.
- Relatórios de divergência.
- Fallback funcional.

**Critério de conclusão:** o C++ pode ser executado em paralelo para validação sem alterar o comportamento do fluxo Python, sem efeitos colaterais duplicados e sem comprometer o estado do ambiente.

##### Fase 7 — Equivalência comportamental e regressão completa

**Objetivo:** demonstrar que a implementação nativa preserva o comportamento esperado antes de ativá-la no fluxo principal.

**Tarefas:**
- [ ] Executar os testes existentes de consistência das máscaras da PPO.
- [ ] Executar os testes de máscaras condicionais.
- [ ] Executar os testes existentes de AntiLoop e validação de movimentos.
- [ ] Criar testes diferenciais automatizados entre Python e C++.
- [ ] Comparar todas as dimensões e todos os valores das máscaras.
- [ ] Comparar as decisões de bloqueio e seus motivos.
- [ ] Testar estados iniciais, estados intermediários e estados de borda.
- [ ] Testar tabuleiro vazio, banco cheio, posições ocupadas e combinações de unidades.
- [ ] Testar ciclos e reversões que envolvam múltiplas ações consecutivas.
- [ ] Testar mudanças de estado que alterem a validade de movimentos anteriores.
- [ ] Testar a persistência e a atualização correta do histórico anti-loop.
- [ ] Testar a consistência entre amostragem, máscaras condicionais e avaliação das ações pela PPO.
- [ ] Testar estados com diferentes quantidades de jogadores e unidades.
- [ ] Testar sequências reais de jogo registradas durante a execução Python.
- [ ] Reproduzir as mesmas sequências nas duas implementações.
- [ ] Investigar todas as divergências, sem ignorar diferenças consideradas raras.
- [ ] Corrigir regressões antes de avançar.
- [ ] Registrar os resultados dos testes e os cenários cobertos.

**Entregáveis:**
- Relatório de equivalência comportamental.
- Testes diferenciais automatizados.
- Relatório de regressão.
- Lista documentada de cenários validados.

**Critério de conclusão:** todos os testes obrigatórios passam, todas as divergências observadas são explicadas e corrigidas, e os cenários de referência apresentam equivalência de resultados.

##### Fase 8 — Benchmark e otimização de desempenho

**Objetivo:** comprovar o ganho real de desempenho e identificar os custos remanescentes da integração.

**Tarefas:**
- [ ] Repetir o benchmark de geração das máscaras com o mesmo ambiente de referência.
- [ ] Medir separadamente o tempo de geração das máscaras Python.
- [ ] Medir separadamente o tempo de geração das máscaras C++.
- [ ] Medir o custo de conversão e transferência de dados entre linguagens.
- [ ] Medir o custo de `_flatten_masks()` e verificar se continua necessário no formato atual.
- [ ] Medir o tempo total do fluxo de decisão da PPO.
- [ ] Medir o tempo de `env.step()` separadamente.
- [ ] Medir o throughput de decisões por segundo e de steps por segundo.
- [ ] Registrar média, mediana, P95 e variabilidade dos tempos.
- [ ] Repetir os testes com múltiplas lobbies e múltiplos jogadores.
- [ ] Separar os resultados com e sem o overhead de diagnóstico.
- [ ] Comparar os resultados usando a mesma máquina, configuração e cenário.
- [ ] Verificar se a geração em lote reduz a quantidade de chamadas Python/C++.
- [ ] Investigar alocações, cópias e estruturas que ainda representem custos relevantes.
- [ ] Evitar otimizações que alterem as regras de validade ou o comportamento do AntiLoop.
- [ ] Reexecutar os testes de equivalência após cada otimização.
- [ ] Documentar o ganho medido e os gargalos remanescentes.

**Entregáveis:**
- Relatório de benchmark antes/depois.
- Comparação de throughput.
- Análise do custo da interface Python/C++.
- Lista de otimizações adicionais justificadas por medições.

**Critério de conclusão:** o desempenho está medido de ponta a ponta, com resultados reproduzíveis, e o ganho ou a ausência de ganho está documentado. Nenhuma otimização aprovada pode introduzir divergências comportamentais.

##### Fase 9 — Ativação controlada do C++

**Objetivo:** permitir que a implementação nativa assuma o fluxo principal de decisão com possibilidade de retorno imediato ao Python.

**Tarefas:**
- [ ] Adicionar uma configuração explícita para selecionar o backend.
- [ ] Manter Python como implementação de referência e fallback.
- [ ] Ativar C++ inicialmente em execuções de teste controladas.
- [ ] Monitorar erros, divergências e tempos de execução.
- [ ] Verificar a estabilidade em múltiplas lobbies e múltiplos jogadores.
- [ ] Confirmar que o estado e o histórico são atualizados uma única vez.
- [ ] Confirmar que a política PPO recebe máscaras no formato original.
- [ ] Testar o retorno ao backend Python após uma falha simulada.
- [ ] Validar o comportamento em reinicializações do ambiente.
- [ ] Validar o comportamento em treinamento contínuo a partir de checkpoints existentes.
- [ ] Documentar o procedimento de ativação e reversão.
- [ ] Não alterar os pesos da política, as dimensões das ações ou a lógica de recompensas como parte desta migração.

**Entregáveis:**
- Seleção controlada do backend.
- Procedimento de rollback.
- Relatório de estabilidade da execução nativa.

**Critério de conclusão:** o módulo C++ executa o fluxo de decisão de forma estável e controlada, com fallback testado e sem regressões conhecidas.

##### Fase 10 — Retirada do caminho Python do fluxo principal

**Objetivo:** deixar de executar as implementações Python de AntiLoop e Action Masks no caminho normal somente após a aprovação integral da migração.

**Tarefas:**
- [ ] Confirmar o cumprimento de todos os critérios da seção 8.
- [ ] Confirmar a aprovação dos testes de equivalência, regressão, integração e desempenho.
- [ ] Alterar o caminho principal para usar o módulo C++ por padrão.
- [ ] Manter as implementações Python preservadas como referência e fallback.
- [ ] Garantir que a seleção do backend Python continue disponível para diagnóstico e recuperação.
- [ ] Garantir que o caminho padrão não execute simultaneamente os cálculos Python e C++ sem necessidade.
- [ ] Confirmar que não há chamadas residuais às implementações Python no fluxo normal.
- [ ] Repetir os testes essenciais após a alteração do backend padrão.
- [ ] Repetir o benchmark de throughput com o C++ no caminho principal.
- [ ] Documentar a arquitetura final, os comandos de compilação e os procedimentos de recuperação.
- [ ] Atualizar o roadmap com os resultados medidos e as limitações conhecidas.
- [ ] Não excluir os arquivos Python nesta etapa.

**Entregáveis:**
- Módulo C++ como backend padrão de decisão.
- Implementações Python preservadas.
- Documentação operacional atualizada.
- Relatório final de equivalência e desempenho.

**Critério de conclusão:** o fluxo principal utiliza C++ para gerar as máscaras e aplicar as regras de AntiLoop, enquanto Python mantém a política PPO e o restante da orquestração. O fallback continua funcional e todos os critérios de aceitação estão cumpridos.

---

#### 8. Critérios de aceitação da migração

A migração somente será considerada concluída quando todos os critérios obrigatórios abaixo forem atendidos.

##### 8.1 — Equivalência funcional

- [ ] A implementação C++ reproduz as regras de validade de movimentos da implementação Python.
- [ ] A implementação C++ reproduz os bloqueios do AntiLoop para os mesmos estados e históricos.
- [ ] Todas as máscaras preservam dimensões, tipos, índices e significados.
- [ ] Todas as máscaras condicionais mantêm a dependência correta entre as etapas autoregressivas.
- [ ] A geração das máscaras não altera indevidamente o estado do ambiente.
- [ ] O histórico anti-loop é atualizado nos mesmos pontos e segundo as mesmas regras.
- [ ] Não existem divergências inexplicadas nos cenários de referência.
- [ ] Os casos de borda relevantes estão cobertos pelos testes.

##### 8.2 — Compatibilidade com a PPO

- [ ] `TFTPolicy` continua recebendo máscaras no formato esperado.
- [ ] A amostragem das ações continua respeitando as máscaras.
- [ ] A avaliação posterior das ações utiliza máscaras consistentes com as utilizadas durante a amostragem.
- [ ] Os testes de consistência de máscaras e ações passam.
- [ ] As dimensões e a semântica do espaço de ações não são alteradas.
- [ ] O treinamento, os buffers e os checkpoints continuam compatíveis com a arquitetura atual.

##### 8.3 — Integração e estabilidade

- [ ] O módulo compila e pode ser importado no ambiente de treinamento.
- [ ] A integração funciona com os ambientes e as lobbies utilizados pelo projeto.
- [ ] A execução com múltiplos jogadores e lobbies está validada.
- [ ] Erros da interface nativa são tratados de forma explícita.
- [ ] Não há atualizações duplicadas do histórico ou efeitos colaterais indevidos.
- [ ] O fallback Python funciona e foi testado.
- [ ] É possível retornar ao backend Python sem alterar os pesos da política ou corromper o estado do treinamento.

##### 8.4 — Desempenho

- [ ] O benchmark Python/C++ utiliza cenários equivalentes e condições comparáveis.
- [ ] O custo da interface e da transferência de dados foi medido.
- [ ] O tempo das máscaras, o tempo de `env.step()` e o throughput completo foram medidos separadamente.
- [ ] Média, mediana, P95 e variabilidade estão documentadas.
- [ ] Os resultados não dependem do overhead do profiler para demonstrar o ganho.
- [ ] O ganho efetivo, se houver, está documentado e não foi obtido removendo regras ou simplificando o comportamento da IA.

##### 8.5 — Preservação do código e reversibilidade

- [ ] As implementações Python originais permanecem disponíveis.
- [ ] Nenhuma implementação Python é removida antes da aprovação final.
- [ ] O backend C++ pode ser ativado e desativado por configuração.
- [ ] O procedimento de rollback foi testado.
- [ ] A ativação do C++ não exige alterar a política PPO.
- [ ] O histórico de alterações e os resultados de validação estão documentados.

##### 8.6 — Documentação e conclusão

- [ ] A estrutura e as responsabilidades do módulo C++ estão documentadas.
- [ ] Os comandos de compilação e execução dos testes estão documentados.
- [ ] O contrato Python/C++ está documentado.
- [ ] Os testes executados e os resultados obtidos estão registrados.
- [ ] As divergências encontradas durante a migração foram corrigidas ou formalmente identificadas como bloqueios pendentes.
- [ ] O roadmap registra explicitamente a conclusão de cada fase.

**Regra de aprovação final:** se qualquer critério obrigatório de equivalência, compatibilidade, estabilidade ou reversibilidade estiver pendente, a migração não será considerada 100% concluída e o caminho Python deverá continuar disponível como referência e fallback.

A conclusão desta etapa significa que C++ assumiu a geração das Action Masks, a validação de movimentos e o AntiLoop no fluxo principal, preservando o comportamento esperado da IA. Isso não implica remover imediatamente o código Python de referência, nem garante equivalência matemática para todos os estados possíveis; a aprovação depende dos testes diferenciais, dos cenários de referência e da validação operacional documentada.



## Fase 5 — Integração do ambiente vetorizado e do trainer

- [ ] Revisar `LobbyVectorEnv` e `vector_lobby_env.py`.
- [ ] Validar `DummyVecEnv` e `SubprocVecEnv`.
- [ ] Confirmar que cada ambiente possui estado e aleatoriedade adequados.
- [ ] Auditar `Trainer(num_envs=4, use_subprocess=True)`.
- [ ] Validar o fluxo de observações, ações, recompensas e término de episódio.
- [ ] Confirmar que o reset dos ambientes não perde dados necessários.
- [ ] Validar a integração entre `TFTPolicy`, `RolloutBuffer` e `PPOTrainer`.
- [ ] Confirmar salvamento e carregamento de checkpoints.
- [x] Executar um ciclo de treino completo, mesmo que curto.
- [ ] Validar o fluxo completo de término e truncamento de episódios.
- [ ] Comparar execução sequencial e subprocessos quanto à estabilidade e desempenho.


## Fase 6 — Recompensas e qualidade das decisões

- [ ] Avaliar a recompensa de variação de poder com `tanh`.
- [ ] Revisar bônus por sinergias ativas, parciais e mudanças de nível.
- [ ] Revisar recompensas por direção de composição e foco estratégico.
- [ ] Revisar punições por vender unidades importantes.
- [ ] Revisar punições por resetar o tabuleiro sem necessidade.
- [ ] Revisar decisões de XP e economia.
- [ ] Validar bônus por upgrades de 2 e 3 estrelas.
- [ ] Revisar recompensas de estabilidade e anti-loop.
- [ ] Verificar se caches e histórico não contaminam os episódios.
- [ ] Comparar a qualidade das decisões com e sem cada componente de reward shaping.

**Objetivo:** evitar uma IA que aprenda a maximizar a recompensa artificial sem realmente jogar melhor.

## Fase 7 — Avaliação controlada e treinamento

- [ ] Criar uma avaliação com seeds fixas.
- [ ] Registrar colocação final, taxa de vitória e sobrevivência.
- [ ] Registrar economia, nível, composição e upgrades.
- [ ] Registrar ações inválidas e tentativas de movimento repetitivo.
- [ ] Comparar o agente com uma estratégia de referência.
- [ ] Separar avaliação de treinamento para evitar métricas enviesadas.
- [x] Instrumentar e observar métricas no TensorBoard.
- [ ] Validar que o agente melhora ao longo do treinamento.
- [ ] Comparar checkpoints usando os mesmos cenários.
- [ ] Avaliar a estabilidade do KL e a frequência de early stopping.
- [ ] Comparar políticas treinadas antes e depois da introdução do Self-Play.

## Fase 8 — Versionamento e evolução dos modelos

- [ ] Definir convenção de nomes para checkpoints.
- [ ] Salvar configuração e hiperparâmetros junto do modelo.
- [ ] Registrar versão do ambiente e da política.
- [ ] Manter checkpoints de referência para comparação.
- [ ] Implementar seleção de modelos com base em avaliação.
- [ ] Planejar população de agentes ou self-play controlado.
- [ ] Garantir que modelos antigos possam ser carregados ou rejeitados com erro claro se incompatíveis.
- [ ] Avaliar agentes atuais contra versões anteriores sob condições equivalentes.

## Fase 9 — Inteligência tática de combate

- [ ] Implementar mana, habilidades, buffs de sinergia, etc
- [ ] Melhorar seleção de alvos.
- [ ] Avaliar pathfinding e movimentação até alvos.
- [ ] Refinar inferência de papéis: tank, carry, support, fighter e assassin.
- [ ] Usar atributos, alcance e descrição de habilidades para inferir papéis, sem depender de nomes fixos de traits.
- [ ] Melhorar avaliação de ameaça e prioridade dos alvos.
- [ ] Evitar posicionamentos incoerentes, como carries ou assassinos colocados na linha de frente sem justificativa.
- [ ] Medir custo computacional e aproveitar caches quando comprovadamente úteis.
- [ ] Criar cenários controlados para testar comportamento tático.
- [ ] Avaliar BFS e A* para movimentação, se profiling e testes táticos justificarem.

## Fase 10 — Robustez e preparação para execução prolongada

- [ ] Rodar sessões longas de treinamento sem falhas.
- [ ] Detectar NaN, explosão de gradientes e instabilidade das recompensas.
- [ ] Validar recuperação após interrupção e carregamento de checkpoints.
- [ ] Verificar consumo de memória e estabilidade dos processos.
- [ ] Garantir que os logs sejam suficientes para diagnosticar regressões.
- [ ] Documentar instalação, compilação, testes e execução.
- [ ] Consolidar um comando reproduzível para iniciar o treinamento.

## Débito técnico — DT-01

### Retirar unidades do tabuleiro para o banco

- [ ] Implementar a ação tabuleiro → banco.
- [ ] Integrar a ação às máscaras e ao PPO.
- [ ] Testar ciclos banco ↔ tabuleiro e preservar movimentos úteis.
- [ ] Avaliar compatibilidade com dimensões de ações e checkpoints.
- [ ] Separar restrições de legalidade de heurísticas estratégicas.
- [ ] Evitar bloquear um movimento apenas por parecer estrategicamente ruim.
- [ ] Preservar a exploração da política PPO.