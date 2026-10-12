# Roadmap oficial consolidado — IA TFT

> Este arquivo usa o roadmap fornecido pelo usuário como fonte oficial. As tarefas complementares foram incluídas somente quando acrescentam algo que ainda não estava coberto, evitando duplicações. Itens sem evidência suficiente permanecem pendentes.

## Fase 1 — Arquitetura e responsabilidades

**Objetivo:** estabelecer uma base modular para o ambiente de treinamento.

- [x] Definir as responsabilidades do `MiniTFTEnv`.
- [x] Estruturar o `TFTLobby` e a lógica global da partida.
- [x] Separar `SHOP`, `ECONOMY`, `UNITS` e `STRATEGY`.
- [x] Integrar `UnitManager` e `UnitPool` compartilhados.
- [x] Conferir contratos de observação, ação, recompensa e reset.

**Estado:** componentes principais existentes; alguns contratos ainda precisam de revisão integrada.

## Fase 2 — Lobby completo com 8 jogadores

- [x] Criar o lobby com oito jogadores.
- [x] Manter o estado de cada jogador e o estado global da partida.
- [x] Estruturar pareamento de jogadores e avanço de rounds.
- [x] Validar partidas completas, incluindo reset e eliminação.
- [x] Garantir que nenhum jogador eliminado continue influenciando o fluxo da partida.
- [x] Testar diferentes sequências de pareamento e situações-limite.

**Status:** implementação principal existente; validação ponta a ponta pendente.

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

**Status:** integração direta Python → C++ confirmada; regressão completa e desempenho ainda precisam ser validados.

## Fase 4 — Máscaras de ação, anti-loop e desempenho

### 4.1 — Auditoria das máscaras

- [x] Implementar correções no `ActionMaskManager.py`.
- [x] Validar dimensões e tipos das máscaras.
- [x] Validar máscaras condicionais de movimento no tabuleiro.
- [x] Validar movimentação banco → tabuleiro e tabuleiro → tabuleiro.
- [x] Garantir que sempre exista uma ação válida para o PPO.
- [x] Confirmar que a máscara usada na coleta é compatível com a usada na atualização do PPO.

**Status:** concluída conforme os testes reportados.

### 4.2 — Anti-loop e regressões

- [x] Corrigir o `AntiLoopManager` e comitar a alteração.
- [x] Executar testes de regressão anteriores reportados como aprovados.
- [x] Reexecutar as regressões na configuração atual da máquina.
- [x] Confirmar que o anti-loop não bloqueia ações realmente úteis.
- [x] Instrumentar métricas de execução e bloqueios no TensorBoard.
- [ ] Validar os contadores em cenários controlados com bloqueios reais.
- [ ] Confirmar que as métricas representam contagens e taxas com a interpretação correta.

**Status:** testes de regressão aprovados; os itens pendentes continuam abertos.

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

**Critério de conclusão:** o anti-loop impede repetições indesejadas sem assumir o papel do agente na escolha estratégica das ações.

### 4.3 — Integração com PPO

- [x] Auditar as seis dimensões da ação: `[7, 5, 9, 28, 28, 28]`.
- [x] Otimizar Maks
- [ ] Conferir as máscaras condicionais para cada cabeça da política.
- [ ] Verificar cálculo de probabilidades e log-probabilidades com máscaras.
- [x] Testar a consistência das máscaras entre `get_action_and_value` e `evaluate_actions` para os tipos de ação cobertos pelos testes reportados.
- [ ] Testar `evaluate_actions` durante a atualização do PPO em treinamento.
- [ ] Confirmar que não há NaN, distribuições inválidas ou ações impossíveis.

**Observação:** a consistência básica já foi testada. Os itens restantes são validações mais abrangentes.

### 4.4 — Desempenho e avaliação controlada

- [ ] Medir o custo de `get_action_masks()` por jogador.
- [ ] Medir tempo de `env.step()` e de cada combate.
- [ ] Medir throughput de steps por segundo.
- [ ] Identificar gargalos antes de otimizar.
- [ ] Comparar resultados antes e depois das otimizações.

### 4.5 — Decisão sobre C++ adicional

- [ ] Avaliar se vale migrar outras rotinas para C++, e se migra so mask, ou o antiloop tb.
- [ ] Só implementar novas migrações depois de medir o gargalo real.
- [ ] Preservar a lógica Python quando a migração não oferecer ganho comprovado.

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

**Atualização:** um treino curto foi executado, retomando do update 41 e chegando ao update 42. O carregamento do checkpoint foi confirmado. Salvamento e demais contratos ainda precisam de validação própria.

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
**Status:** fora do escopo atual; não bloqueia a Fase 4.2.

## Próximo passo oficial

O foco imediato é a **Fase 4.2.1**: auditar `AntiLoopManager.py` e `ActionMaskManager.py`, distinguir restrições de legalidade de heurísticas estratégicas e preservar a exploração do PPO. Os testes de regressão já aprovados não precisam ser repetidos sem motivo.