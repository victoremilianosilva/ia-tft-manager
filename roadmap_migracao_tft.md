# 🚀 2. Roadmap — Migração do ambiente TFT para C++

## 🎯 Objetivo

Migrar gradualmente a lógica do ambiente TFT de Python para C++, mantendo compatibilidade com o Gymnasium e com o treinamento PPO existente.

A migração deve priorizar a correção dos contratos da API, a equivalência de comportamento com o ambiente Python e a redução do custo de simulação. O PPO continuará sendo responsável pela política e pelo treinamento, enquanto o C++ executará as partes mais custosas do ambiente.

### Princípios da migração

- [ ] Manter a compatibilidade com o pipeline atual de treinamento PPO.
- [ ] Definir contratos estáveis entre C++, bindings Python e ambiente Gymnasium.
- [ ] Preservar as regras de jogo e o comportamento esperado do ambiente Python.
- [ ] Migrar em etapas pequenas, com testes de regressão.
- [ ] Evitar duplicação de regras entre Python e C++.
- [ ] Medir o desempenho antes e depois de cada etapa.
- [ ] Manter uma implementação Python de referência durante a validação.
- [ ] Não integrar definitivamente uma etapa ao PPO enquanto seus contratos e testes não estiverem validados.

---

# 📌 Etapa 1 — Contratos do binding

**Objetivo:** estabelecer uma API C++/Python consistente, previsível e compatível com o ambiente de treinamento.

**Status:** 🟡 Em andamento — requer correções e validação.

## 1.1. Padronização dos contratos públicos

- [ ] Definir o contrato de `reset()`, incluindo observações e informações auxiliares.
- [ ] Definir o contrato de `step()`, incluindo observações, recompensas, encerramentos, truncamentos e informações auxiliares.
- [ ] Padronizar os tipos retornados pelos bindings para cada método público.
- [ ] Definir explicitamente as dimensões e os tipos dos arrays retornados.
- [ ] Padronizar os identificadores dos jogadores e das unidades.
- [ ] Garantir que os contratos estejam documentados e cobertos por testes automatizados.

## 1.2. Estado público do ambiente

- [ ] Alinhar `get_public_state()` ao formato esperado pelo ambiente Python.
- [ ] Incluir os dados globais necessários, como estágio, rodada, índice da rodada, estado de encerramento, vencedor, classificação e jogadores vivos.
- [ ] Definir o formato dos dados individuais de cada jogador.
- [ ] Garantir que o estado público não exponha referências mutáveis internas do C++.
- [ ] Validar a conversão dos tipos C++ para os tipos Python.

## 1.3. Estratégias e metadados

- [ ] Definir se `get_strategies()` deve retornar uma lista plana de estratégias ou uma estrutura agrupada por jogador.
- [ ] Padronizar a estrutura retornada conforme o contrato escolhido.
- [ ] Incluir os metadados necessários para identificar jogador, estratégia e estado da estratégia.
- [ ] Garantir consistência entre o retorno do binding e o consumo em Python.
- [ ] Adicionar testes para ambientes com diferentes quantidades de jogadores e estratégias.

## 1.4. Métricas anti-loop

- [ ] Definir o contrato de `get_anti_loop_metrics()`.
- [ ] Decidir se o retorno será uma lista de métricas por jogador ou um dicionário agregado.
- [ ] Padronizar nomes, tipos e significado de cada métrica.
- [ ] Garantir que as métricas possam ser consumidas pelo logger e pelos sistemas de diagnóstico.
- [ ] Criar testes para métricas zeradas, atualizadas e reinicializadas após `reset()`.

## 1.5. Implementação e compilação dos bindings

- [ ] Revisar `cpp/include/lobby/TftEngine.hpp`.
- [ ] Revisar `cpp/bindings/tft_engine_bindings.cpp`.
- [ ] Implementar ou completar `cpp/src/lobby/TftEngine.cpp`.
- [ ] Verificar se todos os métodos declarados possuem implementação correspondente.
- [ ] Garantir que os bindings exponham somente os métodos necessários à integração.
- [ ] Compilar o módulo C++ e corrigir erros de compilação e linkedição.

## 1.6. Testes de contrato

- [ ] Executar `tests/test_tft_engine_api.py`.
- [ ] Validar o formato de retorno de `reset()` e `step()`.
- [ ] Validar as dimensões das observações e das máscaras de ação.
- [ ] Validar recompensas, encerramentos e informações auxiliares.
- [ ] Validar os métodos de estado público, estratégias e métricas anti-loop.
- [ ] Garantir que os testes falhem quando um contrato for alterado indevidamente.

### Critério de conclusão

A etapa estará concluída quando o módulo C++ compilar, todos os métodos públicos estiverem implementados e os testes de contrato passarem sem incompatibilidades com o consumidor Python.

---

# 📌 Etapa 2 — Catálogo nativo e pool compartilhado

**Objetivo:** migrar para C++ a representação e o gerenciamento das unidades, mantendo consistência entre catálogo, pool, jogadores, loja, banco e tabuleiro.

## 2.1. Modelo nativo das unidades

- [ ] Definir a estrutura nativa da unidade.
- [ ] Representar identificador, nome, custo, atributos e demais propriedades necessárias ao jogo.
- [ ] Representar características e informações utilizadas em sinergias.
- [ ] Representar nível de estrela e demais estados relevantes da unidade.
- [ ] Definir quais dados são imutáveis e quais podem ser alterados durante a partida.
- [ ] Padronizar a conversão entre as estruturas C++ e Python.

## 2.2. Carregamento do catálogo

- [ ] Identificar a fonte oficial dos dados das unidades.
- [ ] Validar o formato e a integridade do catálogo.
- [ ] Implementar o carregamento do catálogo em C++.
- [ ] Garantir que todas as unidades esperadas sejam carregadas.
- [ ] Tratar identificadores inexistentes e dados inválidos.
- [ ] Comparar o catálogo carregado em C++ com o utilizado pelo ambiente Python.
- [ ] Evitar carregamentos repetidos e desnecessários durante cada passo do ambiente.

## 2.3. Pool compartilhado

- [ ] Implementar o pool compartilhado de unidades.
- [ ] Definir as quantidades disponíveis por unidade e por nível de estrela, conforme as regras adotadas.
- [ ] Implementar retirada e devolução de unidades ao pool.
- [ ] Integrar o pool às compras, vendas e demais operações que alterem a disponibilidade.
- [ ] Garantir que dois jogadores não obtenham cópias além das quantidades permitidas.
- [ ] Definir o comportamento do pool quando uma unidade não estiver mais disponível.
- [ ] Implementar reinicialização determinística do pool quando aplicável.

## 2.4. Estado das unidades por jogador

- [ ] Integrar o catálogo ao estado dos jogadores.
- [ ] Representar corretamente as unidades na loja, no banco e no tabuleiro.
- [ ] Garantir consistência entre identificadores de unidades e dados do catálogo.
- [ ] Validar a movimentação de unidades entre áreas.
- [ ] Garantir que compras, vendas e combinações atualizem o pool corretamente.
- [ ] Impedir referências inválidas e duplicações acidentais no estado.

## 2.5. Testes de catálogo e pool

- [ ] Testar carregamento completo do catálogo.
- [ ] Testar unidades inexistentes e dados inválidos.
- [ ] Testar retirada e devolução de unidades.
- [ ] Testar disponibilidade compartilhada entre jogadores.
- [ ] Testar reinicialização do pool.
- [ ] Comparar os resultados com a implementação Python de referência.

### Critério de conclusão

A etapa estará concluída quando o catálogo e o pool forem gerenciados de forma consistente em C++, sem divergências relevantes em relação às regras do ambiente Python.

---

# 📌 Etapa 3 — Loja, economia e ações

**Objetivo:** transferir para C++ as operações de loja, economia e manipulação do tabuleiro, garantindo que cada ação produza os mesmos efeitos esperados no ambiente de referência.

## 3.1. Economia

- [ ] Implementar o gerenciamento de ouro.
- [ ] Implementar a renda por rodada conforme as regras atuais.
- [ ] Implementar juros, limites e demais regras econômicas utilizadas pelo ambiente.
- [ ] Implementar recompensas econômicas relacionadas a vitórias, derrotas e sequências, caso façam parte das regras adotadas.
- [ ] Implementar compra de experiência e progressão de nível.
- [ ] Validar os custos e os efeitos de cada operação econômica.
- [ ] Garantir que nenhuma operação permita saldo ou estado inválido.

## 3.2. Loja

- [ ] Implementar a geração de ofertas da loja.
- [ ] Implementar as probabilidades de aparição por nível.
- [ ] Integrar a geração de ofertas ao catálogo e ao pool compartilhado.
- [ ] Implementar a atualização da loja.
- [ ] Implementar a compra de unidades.
- [ ] Validar o consumo de ouro e a disponibilidade de espaço no banco.
- [ ] Definir o comportamento quando não houver unidades disponíveis no pool.
- [ ] Garantir que as operações respeitem o estado atual da partida.

## 3.3. Manipulação do banco e do tabuleiro

- [ ] Implementar a movimentação de unidades entre banco e tabuleiro.
- [ ] Implementar a movimentação entre posições do tabuleiro.
- [ ] Implementar a troca de posições entre unidades.
- [ ] Implementar a venda de unidades.
- [ ] Implementar a combinação de unidades e a evolução de estrelas.
- [ ] Garantir que posições de origem e destino sejam válidas.
- [ ] Impedir movimentações que deixem o estado inconsistente.
- [ ] Atualizar corretamente o pool e a economia quando necessário.

## 3.4. Execução de ações

- [ ] Definir um contrato único para as ações recebidas pelo ambiente.
- [ ] Validar tipo de ação e parâmetros antes da execução.
- [ ] Implementar a aplicação de ações válidas.
- [ ] Definir o comportamento para ações inválidas ou mascaradas.
- [ ] Garantir que ações inválidas não provoquem corrupção do estado.
- [ ] Padronizar os resultados das ações para uso no binding Python.

## 3.5. Máscaras de ação

- [ ] Integrar o `ActionMaskEngine` ao estado real do ambiente.
- [ ] Implementar máscaras para tipos de ação.
- [ ] Implementar máscaras para posições da loja.
- [ ] Implementar máscaras para unidades no banco.
- [ ] Implementar máscaras para posições de origem e destino no tabuleiro.
- [ ] Validar as dimensões esperadas: `[7, 5, 9, 28, 28, 28]`.
- [ ] Garantir que cada máscara reflita as restrições reais da ação correspondente.
- [ ] Garantir que exista uma ação válida de fallback quando necessário.
- [ ] Testar a consistência entre máscaras geradas e ações aceitas.

## 3.6. Anti-loop e movimentos inúteis

- [ ] Integrar o `AntiLoopEngine` ao estado atual do jogador.
- [ ] Detectar movimentos repetidos entre banco e tabuleiro.
- [ ] Detectar trocas repetidas entre posições.
- [ ] Detectar ciclos de movimentação que não alterem o estado estratégico.
- [ ] Bloquear ações comprovadamente inúteis por meio das máscaras, quando seguro.
- [ ] Evitar bloquear movimentos legítimos que produzam uma melhoria real.
- [ ] Validar a interação entre máscaras, movimentos condicionais e trocas.
- [ ] Adicionar testes para sequências repetitivas conhecidas.
- [ ] Garantir que a política ainda possa vender unidades de baixo valor e reorganizar o tabuleiro quando necessário.

## 3.7. Testes de loja, economia e ações

- [ ] Testar compra, venda e atualização da loja.
- [ ] Testar compra de experiência e progressão de nível.
- [ ] Testar juros, renda e limites econômicos.
- [ ] Testar movimentações entre banco e tabuleiro.
- [ ] Testar combinações de unidades.
- [ ] Testar ações inválidas e limites de posições.
- [ ] Testar máscaras em estados válidos e inválidos.
- [ ] Testar prevenção de loops sem bloquear ações úteis.
- [ ] Comparar as transições de estado com a implementação Python.

### Critério de conclusão

A etapa estará concluída quando loja, economia, ações e máscaras estiverem integradas e os testes demonstrarem que as operações respeitam as regras do ambiente.

---

# 📌 Etapa 4 — Combate, recompensas e observações

**Objetivo:** concluir a lógica de simulação necessária para que o ambiente C++ produza transições, observações e recompensas compatíveis com o treinamento.

## 4.1. Preparação do combate

- [ ] Definir a estrutura de entrada do combate.
- [ ] Representar as unidades participantes, suas posições e seus atributos relevantes.
- [ ] Integrar informações de nível de estrela, características e habilidades utilizadas na simulação.
- [ ] Validar a composição dos times antes do combate.
- [ ] Garantir que o combate utilize um estado consistente do tabuleiro.

## 4.2. Motor de combate

- [ ] Revisar o `CombatEngine` existente.
- [ ] Definir o contrato de `CombatInput` e `CombatResult`.
- [ ] Implementar ou completar as regras de resolução do combate.
- [ ] Garantir que atributos e modificadores sejam aplicados corretamente.
- [ ] Implementar a resolução de vitória, derrota e empate, conforme as regras adotadas.
- [ ] Definir o tratamento de combates sem unidades válidas.
- [ ] Garantir que a resolução seja reproduzível quando a mesma semente e as mesmas condições forem utilizadas.
- [ ] Comparar resultados representativos com a implementação Python de referência.

## 4.3. Ciclo de rodadas

- [ ] Integrar o combate ao ciclo principal da partida.
- [ ] Implementar a transição entre preparação e combate.
- [ ] Atualizar rodada, estágio e demais contadores.
- [ ] Aplicar os efeitos de vitória e derrota.
- [ ] Integrar renda, juros, experiência e progressão ao ciclo correto.
- [ ] Implementar a condição de término da partida.
- [ ] Garantir a atualização consistente da classificação e dos jogadores restantes.

## 4.4. Observações

- [ ] Definir o contrato definitivo das observações.
- [ ] Migrar para C++ o cálculo das observações que forem parte do caminho crítico.
- [ ] Preservar a ordem dos atributos e a semântica de cada dimensão.
- [ ] Garantir que as observações tenham formato e tipo compatíveis com a política PPO.
- [ ] Validar a ausência de valores inválidos, como `NaN` e infinitos.
- [ ] Garantir consistência entre observações, estado público e máscaras de ação.
- [ ] Comparar as observações C++ e Python para estados equivalentes.

## 4.5. Recompensas

- [ ] Definir o contrato da função de recompensa.
- [ ] Migrar para C++ os componentes de recompensa que precisem ser executados no ambiente nativo.
- [ ] Preservar a semântica das recompensas existentes.
- [ ] Validar recompensas por evolução, sinergias, economia e composição, quando aplicáveis.
- [ ] Validar recompensas relacionadas a vitórias, derrotas e progresso na partida.
- [ ] Evitar duplicação de recompensas entre C++ e Python.
- [ ] Comparar as recompensas produzidas pelos dois ambientes para transições equivalentes.
- [ ] Documentar diferenças intencionais.

## 4.6. Encerramentos e informações auxiliares

- [ ] Padronizar `terminated` e `truncated` conforme o contrato do Gymnasium.
- [ ] Garantir que o encerramento natural da partida seja identificado corretamente.
- [ ] Garantir que limites externos de execução sejam tratados de forma apropriada.
- [ ] Padronizar as informações auxiliares retornadas por `step()`.
- [ ] Validar o estado terminal e o resultado final da partida.
- [ ] Garantir que `reset()` reinicialize todos os estados relevantes.

## 4.7. Testes de equivalência

- [ ] Criar cenários fixos para comparar os ambientes Python e C++.
- [ ] Comparar transições de estado.
- [ ] Comparar observações.
- [ ] Comparar recompensas.
- [ ] Comparar máscaras de ação.
- [ ] Comparar encerramentos e informações auxiliares.
- [ ] Investigar e documentar divergências.
- [ ] Garantir que todas as diferenças aceitas tenham justificativa explícita.

### Critério de conclusão

A etapa estará concluída quando o ambiente C++ executar o ciclo de jogo completo e produzir resultados compatíveis com a referência Python nos cenários cobertos pelos testes.

---

# 📌 Etapa 5 — Integração com o PPO

**Objetivo:** conectar o ambiente C++ ao pipeline PPO existente e validar estabilidade, desempenho e qualidade do treinamento.

## 5.1. Wrapper Gymnasium

- [ ] Implementar ou finalizar o wrapper Python para o ambiente C++.
- [ ] Garantir compatibilidade com a interface do Gymnasium.
- [ ] Expor corretamente os espaços de observação e ação.
- [ ] Validar os formatos retornados por `reset()` e `step()`.
- [ ] Integrar as máscaras de ação ao formato esperado pela política.
- [ ] Garantir que o wrapper trate encerramentos e reinicializações corretamente.
- [ ] Implementar tratamento de erros sem ocultar falhas do motor nativo.

## 5.2. Integração com os ambientes vetorizados

- [ ] Integrar o wrapper ao `DummyVecEnv`.
- [ ] Integrar o wrapper ao `SubprocVecEnv`, quando aplicável.
- [ ] Validar o funcionamento com múltiplos ambientes simultâneos.
- [ ] Garantir que cada ambiente mantenha estado independente.
- [ ] Validar sementes e reprodutibilidade por ambiente.
- [ ] Verificar o custo de serialização e comunicação entre processos.
- [ ] Confirmar que o uso de subprocessos não provoque deadlocks ou encerramentos inesperados.

## 5.3. Integração com a política e o PPO

- [ ] Integrar as observações ao `TFTPolicy`.
- [ ] Integrar as máscaras de ação ao mecanismo de amostragem da política.
- [ ] Garantir que as ações produzidas respeitem o contrato do ambiente.
- [ ] Integrar recompensas, encerramentos e informações auxiliares ao buffer de rollout.
- [ ] Validar o armazenamento das transições no `RolloutBuffer`.
- [ ] Validar o cálculo de vantagens e retornos.
- [ ] Validar a avaliação de ações e probabilidades da política.
- [ ] Garantir compatibilidade com checkpoints existentes, quando aplicável.
- [ ] Confirmar que a migração não exige alterações indevidas na lógica central do PPO.

## 5.4. Testes de treinamento

- [ ] Executar um episódio completo com o ambiente C++.
- [ ] Executar vários episódios consecutivos.
- [ ] Executar um smoke test de treinamento PPO.
- [ ] Validar que o buffer recebe transições corretas.
- [ ] Validar que a atualização da política termina sem erros.
- [ ] Validar que não há recompensas ou observações inválidas.
- [ ] Validar reinicializações e encerramentos de episódios.
- [ ] Validar treinamento com um ambiente e com múltiplos ambientes.
- [ ] Comparar os logs de treinamento com os da implementação Python.

## 5.5. Benchmark de desempenho

- [ ] Medir o desempenho do ambiente Python antes da migração completa.
- [ ] Medir o desempenho do ambiente C++ em condições equivalentes.
- [ ] Medir o tempo de `reset()` e `step()`.
- [ ] Medir o throughput em passos por segundo.
- [ ] Medir o throughput com diferentes quantidades de ambientes.
- [ ] Medir o custo do wrapper e dos bindings.
- [ ] Medir o uso de CPU e memória.
- [ ] Comparar execução sequencial e vetorizada.
- [ ] Identificar gargalos remanescentes.
- [ ] Registrar os resultados em um relatório reproduzível.

**Metas iniciais de desempenho — hipóteses a validar, não resultados medidos:**

- [ ] Estabelecer uma baseline confiável do ambiente Python.
- [ ] Buscar ganho de aproximadamente 2x como primeiro objetivo.
- [ ] Avaliar ganhos de 3x a 5x como objetivo intermediário.
- [ ] Investigar ganhos superiores a 5x somente após medir e eliminar os principais gargalos.

## 5.6. Estabilidade e regressão

- [ ] Executar a suíte completa de testes.
- [ ] Executar partidas com diferentes sementes.
- [ ] Executar partidas com diferentes quantidades de jogadores.
- [ ] Verificar a ausência de vazamentos de memória.
- [ ] Verificar falhas de estado entre episódios.
- [ ] Verificar comportamento com ações inválidas.
- [ ] Verificar comportamento em estados terminais.
- [ ] Garantir que o ambiente Python de referência continue disponível durante a validação.
- [ ] Documentar diferenças conhecidas e limitações restantes.

### Critério de conclusão

A etapa estará concluída quando o ambiente C++ estiver integrado ao PPO, passar pelos testes de treinamento e demonstrar um ganho de desempenho medido sem divergências de comportamento não justificadas.

---

# 📊 Resumo do roadmap

| Etapa | Descrição | Status |
|---|---|---|
| 1 | Contratos do binding | 🟡 Em andamento |
| 2 | Catálogo nativo e pool compartilhado | ⬜ Pendente |
| 3 | Loja, economia e ações | ⬜ Pendente |
| 4 | Combate, recompensas e observações | ⬜ Pendente |
| 5 | Integração com o PPO | ⬜ Pendente |

---

# ✅ Critérios globais de aceite

- [ ] O módulo C++ compila e pode ser importado pelo Python.
- [ ] Todos os métodos públicos possuem contratos documentados.
- [ ] Os testes de contrato passam.
- [ ] Catálogo e pool compartilhado respeitam as regras definidas.
- [ ] Loja, economia e ações mantêm o estado consistente.
- [ ] As máscaras de ação correspondem às restrições reais do ambiente.
- [ ] Os mecanismos anti-loop bloqueiam ciclos inúteis sem impedir ações legítimas.
- [ ] Combate, recompensas e observações são validados contra a referência Python.
- [ ] O wrapper funciona com o Gymnasium e os ambientes vetorizados.
- [ ] O PPO consegue coletar rollouts e atualizar a política.
- [ ] O benchmark comprova o ganho de desempenho alcançado.
- [ ] As diferenças intencionais em relação ao ambiente Python estão documentadas.
- [ ] Existe um procedimento de fallback para a implementação Python durante a validação.

---

# ⚠️ Observações sobre a implementação atual

Antes de considerar a Etapa 1 concluída, validar especialmente:

- [ ] `get_public_state()` retorna a estrutura pública completa esperada pelo ambiente Python.
- [ ] `get_strategies()` segue o contrato definido, sem divergência entre listas agrupadas e listas planas.
- [ ] `get_anti_loop_metrics()` segue o contrato definido para métricas por jogador ou agregadas.
- [ ] `cpp/src/lobby/TftEngine.cpp` contém as implementações necessárias.
- [ ] `tests/test_tft_engine_api.py` é executado com sucesso.
- [ ] A compilação e a linkedição do módulo nativo foram verificadas.

**Importante:** a presença dos métodos nos bindings não comprova que suas implementações estejam completas nem que a API compile. A etapa deve ser considerada concluída somente após a compilação e a execução dos testes.

Etapa 1 — Contratos do binding
Objetivo: alinhar a API Python/C++ antes de conectar o motor nativo à lógica real do jogo.
Arquivos principais:
- cpp/include/lobby/TftEngine.hpp
- cpp/bindings/tft_engine_bindings.cpp
- cpp/src/lobby/TftEngine.cpp
- tests/test_tft_engine_api.py
- lobby/TFTLobby.py
Tarefas
- [x] Corrigir o retorno de get_strategies() para uma lista plana, com uma estratégia por jogador.
- [x] Corrigir o retorno de get_anti_loop_metrics() para um dicionário com métricas agregadas.
- [ ] Alinhar get_public_state() ao contrato Python, incluindo estado global da lobby e lista de jogadores.
- [ ] Documentar o formato de entrada e saída de reset().
- [ ] Documentar o formato de entrada e saída de step().
- [ ] Validar as seis dimensões da ação: [7, 5, 9, 28, 28, 28].
- [ ] Validar os formatos das observações, recompensas, dones e máscaras.
- [ ] Padronizar o tratamento de valores ausentes, índices inválidos e exceções.
- [ ] Implementar ou concluir a estrutura mínima de TFTEngine necessária para cumprir o contrato.
- [ ] Compilar o módulo tft_engine.
- [ ] Executar os testes de importação e tests/test_tft_engine_api.py.
- [ ] Comparar os contratos públicos do motor C++ com os métodos correspondentes da implementação Python.
Critério de conclusão: o módulo compila e pode ser utilizado pelo Python com contratos consistentes para reset, step, observações, máscaras, estratégias, métricas e estado público.

Etapa 2 — Catálogo e pool de unidades em C++
Objetivo: migrar o catálogo real de campeões e o estoque compartilhado, garantindo que os oito jogadores utilizem o mesmo pool global.
Arquivos principais:
- units/UnitManager.py
- units/UnitPool.py
- cpp/include/lobby/
- cpp/src/lobby/
- units_gerado.json
Tarefas
- [ ] Auditar o formato real de units_gerado.json e os dados consumidos pelo UnitManager.
- [ ] Definir estruturas C++ para os dados estáticos dos campeões.
- [ ] Separar os dados do catálogo do estado mutável de cada unidade.
- [ ] Preservar IDs, UUIDs, estrelas, custo e demais atributos necessários.
- [ ] Migrar a carga e a validação do catálogo para C++.
- [ ] Implementar a criação de instâncias individuais de unidades.
- [ ] Implementar o estoque global com quantidades disponíveis por campeão ou custo, conforme as regras atuais.
- [ ] Implementar retirada de cópias do estoque.
- [ ] Implementar devolução de cópias ao estoque.
- [ ] Implementar o reset do pool sem duplicar ou perder unidades.
- [ ] Garantir que os oito jogadores compartilhem uma única instância do pool.
- [ ] Preservar as regras de disponibilidade e as quantidades definidas pela configuração atual.
- [ ] Definir como o gerador aleatório e as seeds serão controlados.
- [ ] Criar testes de disponibilidade, retirada, devolução, reset e compartilhamento.
- [ ] Comparar os resultados com o UnitPool e o UnitManager Python.
Critério de conclusão: o catálogo é carregado em C++, as instâncias preservam sua identidade e o estoque compartilhado mantém as quantidades corretas ao longo da partida.

Etapa 3 — Loja, economia e ações
Objetivo: migrar as operações que modificam o estado dos jogadores, reutilizando os componentes C++ de decisão já existentes.
Arquivos principais:
- shop/ShopManager.py
- economy/
- env.py
- cpp/include/decision/ActionMaskEngine.hpp
- cpp/src/decision/ActionMaskEngine.cpp
- cpp/include/decision/AntiLoopEngine.hpp
- cpp/src/decision/AntiLoopEngine.cpp
- cpp/src/lobby/TftEngine.cpp
Tarefas
- [ ] Migrar o estado econômico do jogador: ouro, nível, XP e custos.
- [ ] Migrar a geração da loja com as probabilidades e regras atuais.
- [ ] Implementar bloqueio e desbloqueio da loja, se aplicável às regras atuais.
- [ ] Implementar compra de unidades com validação de saldo e espaço no banco.
- [ ] Implementar reroll e devolução das ofertas substituídas ao pool.
- [ ] Implementar compra de XP e evolução de nível.
- [ ] Implementar venda de unidades e devolução ao pool.
- [ ] Implementar movimentação entre banco e tabuleiro.
- [ ] Implementar movimentação e troca de posições no tabuleiro.
- [ ] Preservar upgrades de estrelas e combinações de unidades.
- [ ] Migrar custos, renda, juros, streaks e progressão econômica.
- [ ] Integrar ActionMaskEngine ao estado real do jogador.
- [ ] Integrar AntiLoopEngine às validações e execuções de movimentos.
- [ ] Garantir que consultar máscaras não modifique o histórico anti-loop.
- [ ] Impedir ações inválidas sem corromper o estado.
- [ ] Criar testes unitários para cada operação e para sequências de ações.
- [ ] Comparar estados finais e efeitos econômicos com o ambiente Python.
Critério de conclusão: as ações são executadas integralmente no C++, com estado consistente, máscaras corretas e regras econômicas equivalentes às da implementação Python.

Etapa 4 — Combate, recompensas e observações
Objetivo: completar o ciclo de jogo em C++, preservando a semântica das partidas, as recompensas e os dados consumidos pelo PPO.
Arquivos principais:
- cpp/include/combat/CombatEngine.hpp
- cpp/include/combat/CombatInput.hpp
- cpp/include/combat/CombatResult.hpp
- cpp/src/combat/CombatEngine.cpp
- lobby/TFTLobby.py
- env.py
- vector_lobby_env.py
- cpp/src/lobby/TftEngine.cpp
Tarefas
- [ ] Converter as unidades reais do estado C++ para a entrada de combate.
- [ ] Preservar atributos, posições, papéis e informações necessárias ao combate.
- [ ] Integrar o CombatEngine à resolução das partidas.
- [ ] Migrar o pareamento dos oito jogadores.
- [ ] Migrar o controle de rodada, estágio e progressão.
- [ ] Preservar as regras de vitória, derrota e empate.
- [ ] Implementar a aplicação de dano, eliminações e ranking.
- [ ] Preservar a ordem de processamento dos resultados de combate.
- [ ] Migrar o cálculo de recompensas individuais e terminais.
- [ ] Migrar a construção das observações para C++.
- [ ] Preservar a dimensão das observações, seus índices, tipos e normalização.
- [ ] Preservar as informações necessárias para estratégias e logging.
- [ ] Definir o tratamento de success, completed, timeout e erros do combate.
- [ ] Implementar as condições de término da lobby e dos episódios individuais.
- [ ] Criar testes de regressão para combate, dano, eliminação, ranking e recompensas.
- [ ] Comparar observações e recompensas entre os backends em cenários controlados.
Critério de conclusão: o motor C++ executa o ciclo de jogo necessário, produz observações e recompensas compatíveis e mantém as regras de combate e encerramento da referência Python.

Etapa 5 — Integração com o PPO
Objetivo: habilitar o motor C++ no pipeline de treinamento existente sem reescrever a policy ou o algoritmo PPO.
Arquivos principais:
- trainer.py
- policy.py
- ppo.py
- vector_lobby_env.py
- cpp/bindings/tft_engine_bindings.cpp
- tests/
- benchmark_real_throughput.py
Tarefas
- [ ] Criar ou concluir o wrapper Python para o motor C++.
- [ ] Preservar a interface esperada pelo Trainer e pelo ambiente vetorizado.
- [ ] Implementar seleção explícita entre backend Python e backend C++.
- [ ] Validar a conversão de ações da policy para o formato nativo.
- [ ] Validar as máscaras utilizadas na coleta de experiências e na atualização PPO.
- [ ] Comparar observações, máscaras, recompensas e dones entre os backends.
- [ ] Validar reinício automático de episódios e término da lobby.
- [ ] Testar a integração com DummyVecEnv e SubprocVecEnv, conforme suportado pelo wrapper.
- [ ] Validar importação do módulo e inicialização nos subprocessos.
- [ ] Executar treinamento curto de fumaça e verificar ausência de erros e valores numéricos inválidos.
- [ ] Validar salvamento e retomada de checkpoints.
- [ ] Executar testes de regressão em partidas completas.
- [ ] Medir throughput real com configurações equivalentes.
- [ ] Comparar consumo de CPU, memória e custo de conversão entre Python e C++.
- [ ] Manter Python como backend de referência e fallback durante a validação.
- [ ] Ativar C++ como backend padrão somente após aprovação dos critérios de equivalência, estabilidade e desempenho.
Critério de conclusão: o PPO treina com o backend C++, os contratos permanecem consistentes, as regressões críticas passam e o benchmark demonstra o ganho real sem comprometer a qualidade do treinamento.

🧪 Critérios globais de validação
Esses critérios bloqueiam a conclusão da migração, mesmo que todas as etapas de implementação estejam marcadas como concluídas.
- [ ] Testes unitários dos componentes C++ aprovados.
- [ ] Testes de contrato Python/C++ aprovados.
- [ ] Testes de regressão das regras do jogo aprovados.
- [ ] Testes de pool compartilhado e economia aprovados.
- [ ] Testes de máscaras e anti-loop aprovados.
- [ ] Testes de combate, recompensas e encerramento aprovados.
- [ ] Compatibilidade do wrapper com o Trainer validada.
- [ ] Treinamento PPO de fumaça concluído.
- [ ] Execução com múltiplas lobbies validada.
- [ ] Benchmark reproduzível concluído.
- [ ] Diferenças restantes documentadas e aprovadas explicitamente.
- [ ] Backend Python mantido como alternativa de rollback.
📈 Metas de desempenho
As metas abaixo são objetivos de planejamento, não resultados já medidos.
- Meta inicial: pelo menos 2× de throughput em relação à referência Python.
- Meta desejável: 3–5× após a migração e otimização dos componentes dominantes.
- Meta ambiciosa: 5× ou mais, se os gargalos atuais forem removidos e as conversões entre linguagens não se tornarem o novo limitador.