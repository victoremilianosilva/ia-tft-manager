

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