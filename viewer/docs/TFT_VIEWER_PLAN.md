# Planejamento do visualizador TFT — 8 agentes PPO

> **Status:** implementação inicial em andamento; validação de execução local e aceite final ainda pendentes.  
> **Repositório:** victoremilianosilva/teste-ia  
> **Pasta de documentação visual:** `viewer/docs/`.  
> **Última revisão:** 2026-10-15.

Este documento é a fonte de referência do projeto de visualização. Toda decisão futura sobre arquitetura, eventos, logs, replay, inferência ou interface deve ser refletida aqui para evitar que o plano fique espalhado em conversas.

## 1. Objetivo

Construir um visualizador desktop para observar um lobby real do projeto TFT-like, com **oito agentes PPO jogando a mesma partida**, incluindo:

- Visão geral dos oito jogadores, com tabuleiros e indicadores.
- Ampliação de qualquer jogador sem perder o contexto do lobby.
- Execução ao vivo, pausa, avanço controlado e velocidade de apresentação.
- Reprodução de partidas gravadas, com navegação na linha do tempo.
- Log detalhado das decisões de cada agente.
- Debug de probabilidades, valor estimado, máscaras, ações inválidas, loops e diagnósticos.
- Comparação de sessões e checkpoints treinados por quantidades diferentes de atualizações.

**Princípio central:** treinar e visualizar são atividades separadas. Primeiro treinamos por X atualizações e salvamos o checkpoint; depois carregamos esse checkpoint para executar uma avaliação sem atualizar os pesos.

## 2. Fluxo de trabalho

1. Treinar o PPO por uma quantidade escolhida de atualizações.
2. Salvar e identificar o checkpoint resultante.
3. Abrir o visualizador e selecionar o checkpoint.
4. Configurar inferência, seed e parâmetros da sessão.
5. Executar um lobby com oito jogadores controlados pela política selecionada.
6. Observar os jogadores, inspecionar decisões e gravar a sessão.
7. Reabrir o replay e investigar decisões específicas.
8. Comparar sessões de checkpoints diferentes sob condições controladas.

Podemos, por exemplo, avaliar checkpoints após 10, 50 ou 200 atualizações. Esses números são exemplos, não parâmetros fixos.

## 3. Arquitetura proposta

![Diagrama de arquitetura do TFT Viewer](architecture.svg)

A arquitetura tem cinco responsabilidades:

1. **Política PPO (Python/PyTorch):** carrega o checkpoint e calcula ações.
2. **Controlador de avaliação:** coordena ritmo, seed, pausa, avanço e sequência de ações.
3. **Engine C++ existente:** continua sendo a autoridade sobre regras, economia, loja, unidades, combate, recompensas e resultado.
4. **Camada de eventos/replay:** converte decisões e resultados em registros versionados e persistíveis.
5. **Interface:** apresenta lobby, logs, detalhes e replays sem interferir na lógica do jogo.

A interface não deve acessar estruturas internas da engine diretamente. Uma camada adaptadora estável reduz o acoplamento e permite mudar a tecnologia de interface sem reescrever as regras.

### 3.1 Regras de arquitetura

- A engine C++ continua sendo a fonte da verdade sobre estado e execução.
- A política permanece em Python/PyTorch.
- A interface é observadora; comandos de pausa e avanço são enviados ao controlador.
- Não duplicar regras do jogo no frontend.
- Não alterar observações, máscaras ou recompensas consumidas pelo PPO para acomodar a interface.
- Consumir snapshots e eventos públicos por uma API explícita.
- Registrar versão da engine, checkpoint e configuração da sessão.
- A velocidade de animação não pode mudar a lógica nem a recompensa da partida.

## 4. Carregamento do modelo e inferência

### 4.1 O modelo já treinado é suficiente?

Sim, para avaliação, desde que o checkpoint seja compatível com a arquitetura da política, o ambiente e as dimensões atuais das observações e ações. **O visualizador é exclusivamente de inferência: não treina, não retreina e não atualiza os pesos.** O treinamento continua sendo um processo separado, executado antes da abertura do visualizador.

Regras obrigatórias da sessão:

- Carregar o checkpoint selecionado e instanciar a arquitetura de política compatível.
- Usar `model.eval()` e `torch.inference_mode()` (ou `torch.no_grad()` quando necessário), de acordo com a implementação real da política.
- Não criar nem executar otimizador PPO no visualizador; não chamar `optimizer.step()`, rotinas de atualização de política, backpropagation ou coleta de rollout destinada a treinamento.
- Não salvar checkpoints modificados pela sessão. Salvar logs, snapshots e replays é permitido e independente do treinamento.
- Preservar exatamente o contrato de observações, máscaras, ações e recompensas da engine.
- Registrar identificador/hash do checkpoint, versão da política, seed e configuração da sessão.
- Verificar antes da partida que os pesos carregados permanecem inalterados durante toda a avaliação.

`model.eval()` por si só não torna a escolha de ação determinística. O modo determinístico/estocástico deve ser controlado explicitamente pela API de inferência já existente.

### 4.2 Modos selecionáveis

A interface deve oferecer os dois modos:

- **Determinístico:** seleciona a ação preferida pela política segundo a implementação existente. Útil para avaliações mais repetíveis.
- **Estocástico:** amostra a ação segundo a distribuição da política. Útil para observar a variabilidade do comportamento.

Mesmo com modo determinístico, não se deve prometer resultados idênticos se mudarem seed, estado inicial, engine, ordem de execução ou configuração. No modo estocástico, registrar seed e configuração de amostragem é especialmente importante.

### 4.3 Uma política ou oito?

A configuração inicial recomendada é **um checkpoint compartilhado pelos oito agentes**, mantendo observações, estado de jogo, seed/fluxo de amostragem e histórico de decisões independentes por jogador. Não é necessário carregar oito cópias dos mesmos pesos se a API atual permitir compartilhar o modelo com segurança.

A arquitetura deve permitir futuramente associar checkpoints diferentes a assentos específicos para comparação, mas isso não é requisito da primeira versão. Se houver apenas um checkpoint, os oito agentes usam a mesma política; isso não significa que tomarão necessariamente as mesmas decisões, pois os estados observados e as amostragens podem ser diferentes.

## 5. Interface: visão geral e foco individual

![Wireframe da visão geral com oito jogadores e tabuleiros completos](dashboard-wireframe.svg)

A tela principal deve mostrar os oito jogadores ao mesmo tempo. **Cada cartão de jogador contém o tabuleiro completo daquele jogador, em uma grade de 7 colunas × 4 linhas (28 posições), com cada peça desenhada na posição ocupada correta.** Não basta mostrar uma composição resumida ou apenas as unidades da primeira fileira.

Cada cartão deve incluir, quando os dados estiverem disponíveis:

- Identificador do jogador e estado no lobby.
- Tabuleiro 7×4 completo, com as posições livres e ocupadas visíveis.
- Identificação compacta de cada peça; estrelas/nível de estrela quando disponível.
- Indicadores resumidos de vida, ouro, nível e XP.
- Fase/rodada e última ação relevante.
- Realce do jogador selecionado e de mudanças recentes no tabuleiro.

Ao selecionar um jogador, o painel de inspeção mostra o seu tabuleiro em tamanho ampliado, com coordenadas das casas e informações da peça selecionada, além de banco, loja, sinergias e logs. As coordenadas devem seguir o mesmo padrão usado pela engine, sem criar uma segunda convenção que confunda a depuração.

### 5.1 Controles de espectador

- Iniciar/retomar e pausar.
- Avançar uma decisão/etapa, quando compatível com a granularidade real do controlador.
- Avançar uma fase ou rodada.
- Ajustar a velocidade visual.
- Selecionar um dos oito agentes.
- Filtrar eventos por agente, tipo, rodada ou gravidade.
- Alternar entre sessão ao vivo e replay.
- Entrar e sair da visualização detalhada de combate sem perder o contexto da partida.

A API nativa `TftEngine::step` recebe um array de ações dos oito assentos e executa um passo conjunto do lobby. Portanto, **o avanço unitário da primeira versão será um passo conjunto**, com uma ação proposta para cada jogador vivo (e `PASS` para assentos que não atuam, conforme as regras da engine), não uma ação isolada de um único jogador. A UI poderá pausar entre esses passos conjuntos. A linha do tempo interna de combate será navegável separadamente por eventos gravados. Não vamos fingir que é possível pausar a engine no meio de um passo conjunto se a API não oferece esse controle.

### 5.2 Combate detalhado ao clicar em um jogador

![Wireframe da batalha detalhada com as duas equipes e painel de eventos](combat-view.svg)

Durante a fase de combate, clicar no cartão de um jogador abre uma **visão de batalha dedicada** para o confronto dele. Essa tela deve mostrar todas as peças participantes dos dois lados — as unidades do jogador selecionado e todas as unidades inimigas —, e não apenas o campeão selecionado ou um resumo do combate.

A visão de combate deve incluir:

- Campo de batalha com as peças dos dois times e sua posição atual, diferenciadas visualmente por equipe.
- Nome/identificador de cada unidade e, quando disponível, estrelas, vida atual/máxima, barra de HP, mana e estado (viva, eliminada, alvo/atacando).
- Atualização temporal da posição e dos atributos durante o combate, conforme os eventos ou snapshots realmente emitidos pela engine.
- Linha do tempo de combate com eventos como movimento, ataque, habilidade, dano, eliminação e fim de combate, apenas quando esses dados forem fornecidos.
- Controles de pausa, velocidade, avanço de evento e retorno à visão geral.
- Seleção de uma unidade para inspecionar seus dados sem esconder as demais peças.
- Resultado final e resumo do confronto após a engine concluir a batalha.

**Resultado da inspeção estática:** a engine C++ já define `CombatResult` com eventos tipados de dano, ataque, posição, morte e eventos genéricos, além de HP inicial/final e estatísticas por unidade. `CombatConfig` também tem flags para registrar eventos, dano, alvos, posições, mana e habilidades. Isso indica que existe uma base no motor de combate para construir a linha do tempo. Ainda precisamos confirmar se a configuração é ativada no fluxo normal do lobby e se esses dados chegam ao binding Python e ao adaptador `cpp_lobby_env.py`.

**Decisão para a primeira versão:** registrar e reproduzir a linha do tempo real emitida pelo motor; não exigir que a simulação de combate seja pausável internamente. Se o motor resolve a batalha inteira numa chamada, a UI pode animar os eventos gravados depois que a chamada retornar, respeitando seus timestamps, mas deve identificar isso como reprodução da linha do tempo, não como combate simulado em tempo real. Se eventos intermediários não chegarem à camada Python, implementar a passagem explícita desses eventos/snapshots pela API do lobby. Não fabricar HP, mana, trajetórias ou habilidades. O comentário atual do `CombatEngine` indica que o loop ativo resolve movimento e ataques básicos; habilidades, itens e traits ainda não são mecânicas ativas do loop e não devem ser animadas como se fossem.

## 6. Logs de decisão: requisito central

O visualizador precisa responder, para cada jogador: **o que recebeu, o que escolheu, quais alternativas eram permitidas, o que a engine executou, qual foi o resultado e quais diagnósticos surgiram?**

### 6.1 Categorias de eventos propostas

- match_started / match_finished
- phase_changed / round_started / round_finished
- decision_started
- policy_output
- action_proposed
- action_validated / action_rejected
- action_executed / action_failed
- state_changed
- combat_started / combat_finished
- reward_emitted
- player_eliminated
- anti_loop_detected / anti_loop_blocked
- strategy_changed
- diagnostic_warning / diagnostic_error

Esses nomes são propostas para um esquema de eventos tipado; não significam que todas essas categorias já sejam emitidas pela engine.

### 6.2 Campos mínimos de cada evento

| Campo | Significado |
|---|---|
| schema_version | Versão do esquema de eventos. |
| match_id | Identificador único da sessão/partida. |
| sequence_id | Ordem monotônica global do evento. |
| decision_id | Agrupa registros pertencentes à mesma decisão. |
| round, stage, phase | Contexto do jogo, quando aplicável. |
| player_id | Identificador do assento/jogador de 1 a 8. |
| checkpoint_id | Identidade do modelo utilizado. |
| event_type | Tipo de evento. |
| timestamp | Tempo de parede para diagnóstico; a ordem oficial é sequence_id. |
| observation_ref | Referência à observação exata usada na inferência. |
| action_proposed | Componentes da ação selecionada. |
| action_validation | Estado da validação e motivo explícito. |
| action_result | Resultado real confirmado pela engine, quando existir. |
| policy_diagnostics | Log-probabilidade, entropia, valor estimado e distribuições expostas. |
| reward_components | Recompensas relevantes, mantendo a semântica atual. |
| state_before_ref, state_after_ref | Referências a snapshots antes/depois. |
| diagnostics | Ciclos, bloqueios, anomalias e explicações derivadas. |

Os eventos devem ser estruturados, não apenas strings livres. Mensagens humanas podem ser adicionadas para legibilidade, mas não substituem campos tipados.

### 6.3 Ação proposta não é ação executada

O log deve distinguir rigorosamente:

1. Ação escolhida pela política.
2. Ação validada ou rejeitada.
3. Ação enviada à engine.
4. Resultado real após a execução.
5. Mudança observada no estado.

Se uma validação rejeitar um lote, não registrar a ação como executada. Se a engine não fornecer confirmação granular por jogador, essa limitação deve ser registrada e corrigida na integração, não escondida na interface.

## 7. Debug da política PPO

A política atual usa uma ação estruturada em seis componentes: tipo, slot da loja, slot do banco, alvo do tabuleiro, origem do tabuleiro e alvo condicionado do movimento. A ordem exata e a semântica devem ser confirmadas no código da política antes de implementar o logger.

### 7.1 Dados a registrar

A inspeção de `TFTPolicy` confirma que `get_action_and_value()` retorna quatro saídas: ação, log-probabilidade total, entropia total e valor estimado. **A distribuição completa/logits de cada cabeça não é retornada atualmente.** A ação é autorregressiva e já aplica máscaras às cabeças condicionais.

Decisão de implementação: preservar o contrato atual de quatro retornos usado pelo trainer e criar uma API de diagnóstico opt-in que devolva, além das saídas normais, os logits/probabilidades após máscara de cada cabeça realmente visitada, a máscara aplicada, a ação selecionada e a probabilidade condicional correspondente. Essa API deve compartilhar o mesmo caminho de inferência para não amostrar uma segunda ação nem avançar o RNG de novo. Não alterar pesos, observações, máscaras, ações ou recompensas. Testes devem garantir que, com a mesma seed e modo de inferência, ativar diagnósticos não altera a ação produzida.

Dados a registrar:

- Ação final selecionada.
- Log-probabilidade total, entropia total e valor estimado V(s), já disponíveis na saída atual.
- Distribuição/probabilidades após máscara em cada cabeça visitada, via API de diagnóstico nova.
- Alternativas de maior probabilidade, calculadas a partir dessas distribuições.
- Máscara aplicada em cada etapa.
- Dependências condicionais entre componentes da ação.
- Modo determinístico/estocástico e seed de sessão.

### 7.2 Probabilidades condicionais

As probabilidades dos componentes não devem ser apresentadas como seis escolhas independentes quando uma etapa depende da anterior. Por exemplo, a distribuição do destino de um movimento pode depender da origem escolhida e da máscara correspondente.

O painel deve mostrar probabilidades condicionadas à decisão anterior e à máscara aplicada. A probabilidade de uma ação completa, se apresentada, deve ser calculada corretamente segundo a distribuição autorregressiva implementada.

### 7.3 Fato, diagnóstico e interpretação

O visualizador deve separar três níveis:

- **Fato:** o movimento ocorreu da posição A para B.
- **Diagnóstico derivado:** o movimento não alterou o estado ou repetiu uma assinatura anterior.
- **Interpretação:** hipótese de que o agente tentava proteger um carregador, caso existam evidências suficientes.

Não atribuir ao modelo uma justificativa em linguagem natural que ele não produziu. Diagnósticos derivados precisam indicar a regra que os originou.

## 8. Máscaras, ações inválidas e anti-loop

A auditoria inicial identificou infraestrutura nativa para snapshot de auditoria e métricas anti-loop, mas a trilha individual de tentativa/causa/resultado precisa ser completada.

Para cada ação inválida ou bloqueada, registrar:

- Jogador e decisão.
- Componentes da ação.
- Máscara vigente e regra de validação aplicada.
- Motivo explícito da rejeição.
- Se a rejeição ocorreu antes do lote ou durante a execução.
- Estado anterior e confirmação de que não houve alteração indevida.
- Contador/métrica anti-loop relacionada, quando aplicável.

Para movimentos repetitivos, registrar assinatura do estado relevante, origem/destino, ação anterior equivalente, número de repetições e regra que detectou o ciclo. Evitar armazenar apenas um contador agregado: ele não basta para investigar um caso individual.

A instrumentação não deve mudar silenciosamente a política nem substituir a máscara usada no treinamento. Qualquer bloqueio operacional deve estar explícito, auditável e consistente com as regras atuais.

## 9. Snapshots e contrato de integração

Estruturas conceituais propostas:

- **LobbySnapshot:** estado público de todos os oito jogadores em um instante.
- **PlayerSnapshot:** economia, nível, XP, banco, loja, tabuleiro, vida e estado do jogador.
- **DecisionRecord:** observação, máscaras, saída da política e ação proposta.
- **ActionExecutionRecord:** validação, execução e resultado confirmado.
- **GameEvent:** combate, rodada, eliminação, recompensa e mudança de fase.
- **DiagnosticEvent:** ação inválida, loop, bloqueio e anomalia.
- **MatchMetadata:** checkpoint, seed, versão da engine, configuração e modo de inferência.
- **ReplayIndex:** índice de snapshots e sequência de eventos para navegação.

Esses nomes são conceitos do contrato, não classes já existentes.

### 9.1 APIs existentes a reaproveitar

Na auditoria estática inicial da branch main, foram identificados estes pontos relevantes:

- TFTPolicy em policy.py, com inferência determinística/estocástica e saídas de diagnóstico como log-probabilidade, entropia e valor.
- get_audit_snapshot() na engine C++ e seus bindings nativos.
- get_action_masks() e APIs de estado do lobby.
- cpp_lobby_env.py, adaptador Python para o backend nativo.
- Métricas de anti-loop e recompensas existentes.
- scripts/evaluate_checkpoints.py, referência para carregar checkpoints e executar avaliação.

Links:
- [policy.py](https://github.com/victoremilianosilva/teste-ia/blob/main/policy.py)
- [cpp_lobby_env.py](https://github.com/victoremilianosilva/teste-ia/blob/main/cpp_lobby_env.py)
- [scripts/evaluate_checkpoints.py](https://github.com/victoremilianosilva/teste-ia/blob/main/scripts/evaluate_checkpoints.py)
- [TftEngine.hpp](https://github.com/victoremilianosilva/teste-ia/blob/main/cpp/include/lobby/TftEngine.hpp)
- [Bindings Python](https://github.com/victoremilianosilva/teste-ia/blob/main/cpp/bindings/tft_engine_bindings.cpp)

**Limitação da auditoria:** foi uma inspeção estática dos arquivos de main; a engine não foi executada nesta etapa. Antes da implementação, validar assinaturas completas, formatos de retorno e caminhos de erro na versão local compilada.

## 10. Replay reproduzível

O replay deve reproduzir os dados gravados, não pedir à política que jogue novamente e presumir que a partida será idêntica. Isso é especialmente importante no modo estocástico. **Abrir ou reproduzir um replay nunca dispara treinamento nem precisa carregar/executar a política**: a sessão gravada deve conter os eventos e snapshots necessários para reconstruir o que foi registrado.

![Ciclo de auditoria de uma decisão](event-lifecycle.svg)

### 10.1 Persistência escolhida para a primeira versão

**Formato inicial: JSONL versionado por sessão**, com um evento JSON por linha, em ordem monotônica. A escolha prioriza simplicidade de implementação, inspeção manual, gravação incremental e facilidade para depurar arquivos sem ferramentas adicionais. A UI deve depender do contrato lógico de eventos, não de detalhes de serialização.

Cada sessão terá um arquivo de metadados e um fluxo JSONL com:

- Metadados de partida: checkpoint/hash, seed, versão da engine, configuração e modo de inferência.
- Eventos estruturados em ordem global, incluindo decisão proposta, validação, execução confirmada, estado e diagnóstico.
- Snapshots completos no início, em marcos definidos e no fim; eventos incrementais entre snapshots.
- Referências de decisão e estado anterior/posterior.
- Resultado final e classificação.

Implementar escrita incremental e buffer limitado, sem bloquear a thread da UI. Começar com logging configurável (resumo/diagnóstico detalhado) para controlar overhead. SQLite só será reconsiderado se medições reais mostrarem que consulta aleatória, volume ou tamanho de sessão tornam JSONL insuficiente; não precisamos manter dois formatos na primeira versão.

### 10.2 Integridade do replay

- Cada evento deve ter sequência estável.
- Cada referência de snapshot deve resolver para um estado gravado.
- O fim da partida deve incluir a classificação final real.
- A ausência de um campo não deve ser substituída por valores inventados.
- O esquema precisa ser versionado para permitir evolução.
- A gravação deve poder ser desativada ou ter níveis configuráveis para limitar overhead, mantendo debug completo disponível quando solicitado.

## 11. Comparação entre checkpoints

O visualizador deve facilitar avaliações após diferentes quantidades de treinamento. Para que os resultados sejam comparáveis, registrar pelo menos:

- Identificador/hash do checkpoint.
- Número de atualizações de treinamento, quando conhecido.
- Seed da partida.
- Modo de inferência.
- Versão/commit da engine e configuração relevante.
- Assento de cada política, caso existam checkpoints diferentes.
- Colocação, vitória, top 4, duração e métricas escolhidas.
- Quantidade de ações, inválidas, bloqueios e ciclos por agente.

Uma única partida serve para observar comportamento, mas não prova superioridade de um checkpoint. Avaliações comparativas precisam de várias partidas e condições controladas.

## 12. Tecnologia: recomendação e decisões pendentes

Direção técnica recomendada:

- Engine: C++ atual, como fonte da verdade.
- Modelo: Python/PyTorch, apenas carregamento de checkpoint e inferência.
- Controlador: Python, aproveitando a integração existente.
- Interface desktop: **PySide6/Qt**, recomendação inicial pela integração direta com Python/PyTorch e pelos controles necessários para lobby, inspeção, logs e replay.
- Gráficos/telemetria: avaliar pyqtgraph ou Qt Charts conforme o volume e o tipo de dados.
- Persistência: formato de replay versionado, a escolher após medir volume e requisitos de consulta.

PySide6 é a recomendação, mas a escolha deve ser confirmada antes de iniciar a implementação. Não é necessário reescrever a engine nem migrar a política para C++. A UI não deve executar inferência pesada nem simulação diretamente na thread de renderização; o controlador deve coordenar o trabalho para manter a interface responsiva.

## 13. Plano de implementação

### Fase 1 — Auditoria e contrato
- [ ] Confirmar API real do lobby e do binding C++ em execução.
- [ ] Expor `get_audit_snapshot()` pelo adaptador Python.
- [ ] Confirmar formato e semântica dos seis componentes de ação.
- [ ] Definir e versionar o esquema de eventos/snapshots.
- [ ] Confirmar como obter classificação final e resultado por jogador.
- [ ] Passar eventos de combate do `CombatResult` pelo lobby/binding até o adaptador Python, ativando somente as flags de gravação necessárias.

### Fase 2 — Avaliação com checkpoint
- [ ] Carregar checkpoint treinado sem executar otimização.
- [ ] Selecionar modo determinístico/estocástico.
- [ ] Fixar e registrar seed/configuração.
- [ ] Executar um lobby de oito jogadores pelo controlador atual.
- [ ] Verificar que a visualização não altera pesos nem recompensas.

### Fase 3 — Instrumentação de debug
- [ ] Registrar entrada da política, máscaras e ação proposta.
- [ ] Expor distribuições/probabilidades condicionais por uma API de diagnóstico opt-in sem mudar a API normal nem a sequência de amostragem.
- [ ] Registrar log-probabilidade, entropia e valor estimado.
- [ ] Registrar validação, resultado real e estados anterior/posterior.
- [ ] Instrumentar ações inválidas e bloqueios anti-loop com causa individual.
- [ ] Testar consistência e ausência de efeitos parciais em ações rejeitadas.

### Fase 4 — Primeira interface
- [ ] Renderizar os oito tabuleiros.
- [ ] Exibir vida, ouro, nível, loja, banco e unidades disponíveis.
- [ ] Selecionar e ampliar qualquer agente.
- [ ] Filtrar o log por agente, rodada, tipo e gravidade.
- [ ] Adicionar controles de pausa, avanço e velocidade.

### Fase 5 — Replay
- [ ] Persistir metadados, eventos e snapshots.
- [ ] Navegar pela linha do tempo.
- [ ] Selecionar uma decisão e inspecionar o estado associado.
- [ ] Reproduzir resultados gravados sem executar novamente a política.
- [ ] Testar sessões com versões distintas do esquema.

### Fase 6 — Análise de comportamento
- [ ] Detectar ciclos de movimentos e ações repetidas.
- [ ] Exibir métricas por agente e por partida.
- [ ] Comparar checkpoints em sessões controladas.
- [ ] Medir overhead de logging e ajustar níveis de detalhe.

## 13.1 Próximas tarefas técnicas obrigatórias

Esta é a sequência de execução acordada antes de avançar a implementação visual. **Estas tarefas estão registradas como pendentes; o registro no plano não significa que já foram executadas.**

### Tarefa 1 — Compilar e validar a passagem dos eventos de combate até Python
- [ ] Configurar/compilar a extensão C++ e executar um teste de combate real com registro de eventos ativado.
- [ ] Confirmar quais eventos são preenchidos de fato em `CombatResult` (ataque, dano, posição, morte e outros suportados).
- [ ] Rastrear o resultado pela engine do lobby, binding pybind11 e adaptador `cpp_lobby_env.py`.
- [ ] Se os eventos forem descartados em algum nível, adicionar passagem explícita dos dados sem alterar a semântica do combate.
- [ ] Criar teste automatizado que confirme que os eventos emitidos no C++ chegam ao Python com IDs, timestamps e valores consistentes.
- [ ] Registrar comandos executados, ambiente, resultado dos testes e limitações encontradas.

**Critério para encerrar:** existe um teste reproduzível que executa combate e demonstra quais dados de evento chegam ao Python. Só então decidir se a tela de combate consegue consumir a linha do tempo diretamente ou se precisa de instrumentação adicional.

### Tarefa 2 — Validar avanço conjunto e pontos seguros de pausa
- [ ] Executar um lobby real com oito assentos e confirmar o contrato de `step()`, incluindo assentos que não atuam e ações `PASS`.
- [ ] Confirmar quando cada lote de ações é validado, executado e refletido no snapshot do estado.
- [ ] Definir a pausa como controle entre chamadas de passo conjunto, sem bloquear ou interromper uma chamada nativa em andamento.
- [ ] Testar pausa, retomada e avanço unitário, verificando que nenhuma ação é executada duas vezes nem fica parcialmente aplicada.
- [ ] Documentar como o controlador distingue ação proposta, ação rejeitada e ação efetivamente executada.

**Critério para encerrar:** teste reproduzível confirma a fronteira de cada passo e a UI consegue pausar com o estado do lobby consistente.

### Tarefa 3 — Implementar e testar diagnóstico opt-in da política
- [ ] Preservar sem alteração a assinatura e o comportamento normal de `get_action_and_value()`.
- [ ] Adicionar caminho opcional para coletar logits/probabilidades após máscara das cabeças visitadas, máscaras, escolhas condicionais e probabilidades das escolhas.
- [ ] Evitar amostragem duplicada ou consumo adicional do RNG quando o diagnóstico estiver habilitado.
- [ ] Testar modo determinístico e estocástico com e sem diagnóstico, usando estados e seeds equivalentes.
- [ ] Confirmar que ações, log-probabilidade, entropia e valor continuam coerentes e que nenhum peso é alterado.
- [ ] Medir o custo adicional e permitir desativar o detalhe para sessões longas.

**Critério para encerrar:** testes automatizados demonstram que diagnóstico habilitado não altera a ação nem os pesos e que os dados registrados correspondem às distribuições usadas para escolher a ação.

### Tarefa 4 — Validar esquema e ciclo completo do replay JSONL
- [ ] Definir versão explícita do esquema, identificador de sessão, sequência monotônica de eventos e metadados de engine/checkpoint/seed.
- [ ] Registrar snapshots inicial, checkpoints de estado acordados, eventos incrementais e resultado final.
- [ ] Distinguir proposta, validação, execução confirmada e estado posterior; nunca registrar ação rejeitada como executada.
- [ ] Implementar gravação incremental e tratamento de erro de escrita sem travar a UI.
- [ ] Testar gravação, fechamento, reabertura, validação de esquema e reconstrução do estado a partir de snapshot + eventos.
- [ ] Testar arquivo truncado/corrompido e versão de esquema não suportada, apresentando erro claro em vez de inventar dados.

**Critério para encerrar:** uma sessão real pode ser gravada, fechada e reaberta, reconstruindo os dados registrados sem executar novamente a política.


## 13.2 Registro da implementação inicial (2026-10-16)

A implementação inicial foi iniciada, sem declarar concluídos os critérios de aceite que ainda não foram testados em execução:

- [x] Janela desktop PySide6 com dashboard de oito jogadores e grade completa 7×4 por jogador.
- [x] Controles de seleção de checkpoint, seed, inferência determinística/estocástica, iniciar/pausar, passo conjunto, avanço de rodada e velocidade visual.
- [x] Leitura de checkpoints salvos pelo trainer no campo `policy`, inferência em modo `eval()` e parâmetros com gradientes desativados.
- [x] API de diagnóstico opt-in para probabilidades/máscaras das cabeças visitadas, com teste para preservar ações/valores e consumo de RNG.
- [x] Gravação inicial de metadados e eventos JSONL versionados, e navegação de eventos em replay.
- [x] Passagem de snapshots públicos/auditáveis pelo adaptador Python, sem a interface acessar diretamente a engine.
- [ ] Executar a aplicação no Windows com checkpoint real e confirmar compatibilidade de formato/observações.
- [ ] Validar todas as máscaras e as oito inferências com uma partida real no motor nativo.
- [ ] Confirmar propagação dos eventos tipados de combate e implementar roster/HP/posições completos apenas com dados reais.
- [ ] Validar reconstrução visual de snapshots ao navegar replay, além da navegação dos eventos gravados.
- [ ] Executar os testes de diagnóstico em CI e confirmar ausência de regressão no trainer.

A lista acima registra estado de implementação, não uma declaração de aprovação. Campos não fornecidos pelo binding continuam explicitamente indisponíveis na UI.

## 14. Critérios de aceite

A primeira versão completa será funcional quando:

1. Carregar checkpoint treinado e executar lobby real de oito jogadores sem otimização PPO.
2. Mostrar os oito jogadores com o tabuleiro completo 7×4 e posição de cada peça, e permitir ampliar qualquer um.
3. Durante combate, abrir uma visão dedicada ao clicar no jogador, mostrando todas as unidades dos dois lados e atualizando posições/HP/mana quando a engine fornecer eventos intermediários.
4. Oferecer inferência determinística e estocástica selecionável.
5. Registrar ação proposta, máscara, validação e resultado real sem confundi-los.
6. Expor log-probabilidade, entropia, valor estimado e probabilidades relevantes, respeitando a estrutura condicional da política.
7. Registrar ações inválidas, loops e bloqueios com contexto individual.
8. Gravar e reabrir replay sem depender de executar novamente a política.
9. Preservar regras, observações, máscaras e recompensas da engine.
10. Identificar checkpoint, seed e versões necessárias para interpretar a sessão.
11. Documentar campos indisponíveis e falhas de gravação sem fabricar dados.

## 15. Registro de decisões

Decisões já alinhadas:

- [x] O lobby visualizado terá oito agentes na mesma partida.
- [x] O visualizador terá visão geral e ampliação de qualquer agente.
- [x] Haverá modo ao vivo e replay.
- [x] O modelo será treinado separadamente e depois carregado para avaliação.
- [x] Inferência determinística e estocástica será selecionável.
- [x] O log será de debug completo, incluindo probabilidades da política, valor estimado, ações inválidas, ciclos e diagnósticos.
- [x] O visualizador não deve alterar regras, recompensas nem pesos do PPO.
- [x] A engine C++ continua sendo a fonte da verdade.
- [x] A pasta de diagramas e imagens se chama ./, conforme solicitado.
- [x] PySide6/Qt definido como tecnologia inicial da interface desktop; reavaliar apenas se a validação técnica mostrar impedimento.
- [ ] O esquema final de eventos será validado contra as assinaturas reais do código.
- [x] A visão geral foi especificada para exibir o tabuleiro 7×4 completo de cada um dos oito jogadores, com posição individual das peças.
- [x] Durante combate, clicar no jogador abre uma tela separada com todas as unidades dos dois lados e atualização condicionada aos dados reais da engine.
- [ ] Confirmar em execução se os eventos de `CombatResult` são propagados pelo lobby/bindings até Python; o motor já define eventos tipados e flags de gravação, mas o caminho completo ainda precisa ser validado.
- [x] Avanço unitário definido como um passo conjunto do lobby (ações dos oito assentos), com pausa entre passos; não se promete interromper o passo internamente.
- [x] Diagnósticos PPO definidos como opt-in e sem alteração do contrato normal ou da sequência de amostragem.
- [x] JSONL versionado definido como formato inicial de replay.
- [x] A implementação inicial do visualizador começou em `viwer/main.py` e `viewer/session.py`; os critérios de aceite ainda dependem de validação em execução.

## 16. Manutenção deste documento

Toda nova decisão acordada para o visualizador deve atualizar este documento na mesma mudança que altera o planejamento ou a implementação. Atualizar, conforme necessário:

1. **Decisões do projeto:** marcar a decisão e sua justificativa.
2. **Arquitetura e contratos:** manter diagramas e nomes dos eventos alinhados com o código real.
3. **Plano de implementação:** marcar tarefas concluídas apenas após validação.
4. **Critérios de aceite:** registrar testes realizados e resultados reais.
5. **Diagramas em ./:** atualizar as imagens quando o fluxo, a interface ou a arquitetura mudar.

Não marcar tarefas como concluídas com base apenas em inspeção estática. Distinguir claramente entre planejado, implementado, testado e validado em execução.
