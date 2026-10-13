# 🚀 Roadmap — Migração completa do ambiente TFT para C++

**Projeto:** TFT AI  
**Objetivo:** Migrar a simulação do ambiente de jogo de Python para C++, preservando as regras, o comportamento, as recompensas e a compatibilidade com o treinamento PPO.

**Status:** Planejado — não iniciado.

## 1. 🎯 Objetivos da migração

- Migrar o núcleo de simulação do ambiente para C++.
- Reduzir o custo computacional de cada passo do ambiente.
- Eliminar cópias profundas redundantes e processamento repetitivo.
- Manter a geração de máscaras e a lógica anti-loop no C++.
- Preservar a compatibilidade com Gymnasium e o Trainer PPO.
- Manter o ambiente Python como referência para testes de equivalência.
- Permitir alternar entre os ambientes Python e C++ por configuração.
- Medir o ganho real de throughput antes de alterar o backend padrão.

### Fora do escopo inicial

- Reescrever a rede neural PPO em C++.
- Reescrever o Trainer, o RolloutBuffer ou o otimizador.
- Alterar as regras do jogo para facilitar a migração.
- Modificar recompensas ou máscaras para favorecer artificialmente o novo backend.
- Remover a implementação Python antes da validação completa.

---

## 2. 🏗️ Arquitetura de destino

**Python continuará responsável pelo treinamento; C++ será responsável pela simulação.**

```text
Python
├── Trainer PPO
├── Policy / Value Network
├── RolloutBuffer
├── Coleta de experiências
├── Avaliação e logging
└── Wrapper Gymnasium
        │
        ▼
Binding Python ↔ C++
        │
        ▼
Motor C++
├── Estado do jogo
├── Unidades e identidades
├── Tabuleiro e banco
├── Loja e pool de unidades
├── Ouro, XP e economia
├── Compra, venda e movimentação
├── Rodadas e progressão
├── Combate
├── Recompensas
├── Observações
├── Máscaras de ações
└── Histórico anti-loop
```

### Tecnologias previstas

- **C++17 ou C++20:** implementação do motor, escolhendo a versão conforme a compatibilidade das dependências.
- **pybind11:** comunicação entre Python e C++.
- **CMake:** compilação e organização do código nativo.
- **Gymnasium:** interface de ambiente mantida no lado Python.
- **pytest:** testes de regressão, integração e equivalência.
- **Benchmark próprio:** medição de throughput sem depender exclusivamente do profiler.

A escolha final das versões será feita quando a migração começar, considerando o ambiente Windows, a versão do Python e as dependências atuais.

---

## 3. 🗺️ Etapas da migração

### Etapa 0 — Congelar a referência Python

**Objetivo:** estabelecer uma referência confiável antes de modificar a implementação.

Tarefas:
- Registrar o commit de referência do ambiente Python.
- Documentar as regras, recompensas, transições e condições de término.
- Registrar as dimensões das observações e das máscaras.
- Criar cenários determinísticos com seeds controladas.
- Salvar estados de referência para compra, venda, movimentação, loja, combate e término de partida.
- Executar a suíte atual de testes e registrar os resultados.

**Critério de conclusão:** existe uma referência Python reproduzível e uma suíte de testes capaz de detectar mudanças de comportamento.

### Etapa 1 — Infraestrutura C++ e bindings

**Objetivo:** criar a fundação técnica do novo ambiente.

Tarefas:
- Organizar o código nativo em `cpp/`.
- Configurar CMake e pybind11.
- Criar o módulo Python importável.
- Definir as estruturas básicas de estado, ação, observação e resultado.
- Padronizar a conversão de erros e exceções.
- Implementar um ambiente mínimo com `reset()` e `step()`.
- Validar a compilação e a importação no Windows.

**Critério de conclusão:** o módulo C++ compila, é importado pelo Python e executa um ciclo mínimo de reset e step.

### Etapa 2 — Estado, unidades e identidade

**Objetivo:** representar o estado do jogo sem depender de objetos Python.

Tarefas:
- Implementar as estruturas de unidades e campeões.
- Definir a identidade persistente de cada unidade.
- Separar dados estáticos dos campeões do estado mutável de cada instância.
- Implementar tabuleiro de 28 posições, banco de 9 posições e loja de 5 espaços.
- Implementar nível, XP, ouro, juros, rodada, estágio e streak.
- Definir regras de propriedade e cópia dos objetos.
- Evitar cópias profundas de catálogos estáticos.

**Critério de conclusão:** os estados equivalentes em Python e C++ apresentam os mesmos valores relevantes e preservam a identidade das unidades.

### Etapa 3 — Pool de unidades e loja

**Objetivo:** migrar a parte que o profiling identificou como principal gargalo.

Tarefas:
- Migrar o pool de unidades disponíveis.
- Migrar retirada e devolução de unidades.
- Migrar a geração da loja e os sorteios de custo.
- Preservar as probabilidades e regras de disponibilidade.
- Preservar a independência das unidades instanciadas.
- Evitar reconstruir e copiar o catálogo completo em cada sorteio.
- Definir como seeds e estado do gerador aleatório serão controlados.

**Critério de conclusão:** os testes de distribuição, disponibilidade e estado do pool passam, e o benchmark demonstra o custo dessa etapa isoladamente.

### Etapa 4 — Operações de jogo

**Objetivo:** migrar todas as ações que alteram o estado do jogador.

Tarefas:
- Compra de unidades.
- Venda de unidades.
- Movimentação entre banco e tabuleiro.
- Movimentação e troca de posições no tabuleiro.
- Compra de XP e evolução de nível.
- Atualização e bloqueio da loja.
- Aplicação dos custos e recompensas econômicas.
- Atualização de estrelas e combinações de unidades.
- Validação de ações inválidas e limites de recursos.

**Critério de conclusão:** para sequências de ações controladas, Python e C++ produzem estados finais equivalentes, com as mesmas recompensas e regras de validade.

### Etapa 5 — Composição, sinergias e estratégia

**Objetivo:** migrar a lógica que interpreta a composição do jogador.

Tarefas:
- Atualizar contagens de unidades e características.
- Calcular sinergias ativas, parciais e níveis.
- Migrar a avaliação de composição.
- Preservar identificação de papéis e avaliação posicional.
- Migrar a lógica de foco de composição, caso pertença ao ambiente.
- Preservar as regras usadas na avaliação de recompensas.

**Critério de conclusão:** composições de referência produzem as mesmas contagens, sinergias e resultados estratégicos.

### Etapa 6 — Rodadas, combate e progressão

**Objetivo:** migrar o ciclo completo de partida.

Tarefas:
- Migrar a resolução de rodadas.
- Migrar a lógica de combate.
- Migrar a determinação de vitória, derrota e empate.
- Migrar dano ao jogador, eliminações e ranking.
- Migrar progressão de estágio e rodada.
- Migrar streaks, recompensas e condições de encerramento.
- Preservar a ordem em que os eventos são processados.

**Critério de conclusão:** cenários de combate e sequências de rodadas produzem resultados equivalentes aos da referência Python.

### Etapa 7 — Máscaras de ações e anti-loop

**Objetivo:** integrar o motor de máscaras existente ao novo ambiente, evitando duplicação da lógica.

Tarefas:
- Integrar a geração C++ das seis dimensões de ação.
- Preservar as matrizes de movimentação de tabuleiro e banco.
- Integrar o histórico anti-loop.
- Preservar as condições que impedem movimentos inúteis e ciclos.
- Garantir que a geração das máscaras no backend C++ não invoque geradores de máscaras em Python.
- Testar estados inválidos, posições ocupadas e ações condicionais.

**Critério de conclusão:** equivalência de máscaras e anti-loop comprovada, com geração realizada integralmente no motor C++.

### Etapa 8 — Observações, recompensas e API Gymnasium

**Objetivo:** tornar o motor C++ compatível com o pipeline de treinamento.

Tarefas:
- Migrar a construção das observações.
- Preservar shapes, tipos, índices e normalização.
- Migrar o cálculo das recompensas e o respectivo detalhamento.
- Implementar `reset()` e `step()` com contratos compatíveis.
- Preservar os indicadores de término de episódio e truncamento.
- Retornar informações auxiliares necessárias ao logging.
- Minimizar conversões de estruturas grandes entre C++ e Python.

**Critério de conclusão:** o wrapper passa nos testes do Gymnasium e o Trainer consegue interagir com o novo ambiente.

### Etapa 9 — Integração com o Trainer PPO

**Objetivo:** substituir o ambiente utilizado pelo treinamento sem reescrever o algoritmo.

Tarefas:
- Integrar o novo wrapper ao Trainer existente.
- Testar `DummyVecEnv` e `SubprocVecEnv`.
- Validar reset automático, encerramento e reinício de episódios.
- Validar serialização e transferência dos dados necessários.
- Preservar a interface das observações, máscaras e ações.
- Testar checkpoint, retomada de treinamento e logging.
- Comparar o comportamento com a versão Python.

**Critério de conclusão:** o PPO consegue treinar, salvar checkpoints e retomar o treinamento utilizando o ambiente C++.

### Etapa 10 — Equivalência e regressão completa

**Objetivo:** garantir que a migração não alterou silenciosamente as regras do jogo.

Tarefas:
- Executar testes unitários de todos os componentes.
- Executar sequências determinísticas nos dois ambientes.
- Comparar estados, observações, máscaras, recompensas e resultados.
- Comparar a economia e a disponibilidade de unidades.
- Testar partidas completas e casos de eliminação.
- Testar seeds e sequências de ações variadas.
- Investigar diferenças legítimas causadas pela implementação do RNG.
- Corrigir divergências no C++, mantendo Python como referência.

**Critério de conclusão:** todos os testes críticos passam e qualquer divergência restante está documentada e aprovada explicitamente.

### Etapa 11 — Benchmark e otimização

**Objetivo:** medir o ganho real da migração.

Tarefas:
- Repetir benchmarks sem `cProfile`.
- Alternar a ordem dos testes Python e C++ para reduzir viés.
- Medir o custo de `reset()`, `step()`, máscaras, observações e combate.
- Medir throughput com um e vários ambientes.
- Medir o throughput real de decisões e atualizações PPO.
- Comparar uso de CPU, memória e custo de conversões.
- Executar partidas longas e verificar estabilidade.
- Identificar gargalos restantes antes de otimizações adicionais.

**Critério de conclusão:** relatório reproduzível com métricas comparáveis, estabilidade confirmada e ganho de desempenho suficiente para justificar a migração.

### Etapa 12 — Ativação gradual do backend C++

**Objetivo:** disponibilizar a nova implementação sem remover a possibilidade de retorno.

Tarefas:
- Manter a configuração explícita do backend.
- Fazer testes de integração em CI, se disponível.
- Executar sessões de treinamento de validação.
- Comparar métricas e comportamento com o backend Python.
- Definir critérios de rollback.
- Tornar C++ o backend padrão somente após aprovação.
- Manter Python disponível como referência e alternativa.

**Critério de conclusão:** backend C++ aprovado para uso regular, com caminho de retorno funcional e documentação atualizada.

---

## 4. 🧪 Estratégia obrigatória de testes

A migração deve preservar os contratos observáveis do ambiente, não necessariamente o mesmo consumo interno de memória.

Testes obrigatórios:
- Estado inicial e reset.
- Compra, venda, movimentação e XP.
- Ouro, juros e economia.
- Loja, pool e disponibilidade.
- Identidade e independência das unidades.
- Máscaras e anti-loop.
- Composição e sinergias.
- Combate, dano e eliminações.
- Recompensas e condições de término.
- Observações, shapes e tipos.
- Compatibilidade com Gymnasium.
- Treinamento PPO e multiprocessing.
- Partidas longas e retomada de checkpoints.

**Regra de ouro:** se houver divergência entre Python e C++, investigar e corrigir a implementação C++ antes de alterar o comportamento Python.

O RNG merece tratamento especial: se as duas linguagens não consumirem os números aleatórios na mesma ordem, a sequência exata de sorteios poderá diferir. Nesse caso, os testes devem verificar tanto os resultados determinísticos controlados quanto as propriedades estatísticas e as regras do jogo.

---

## 5. 📈 Metas de desempenho

As metas abaixo são objetivos de planejamento, não resultados garantidos.

- **Meta inicial:** alcançar pelo menos 2× de throughput em relação à referência Python.
- **Meta desejável:** alcançar 3–5× após migrar e otimizar os componentes dominantes.
- **Meta ambiciosa:** 5× ou mais caso o custo dominante seja efetivamente removido e o restante do pipeline não se torne o novo limitador.

O benchmark oficial deve ser feito sem profiler, em condições equivalentes, usando múltiplas execuções e registrando a variabilidade. O throughput total do PPO será a métrica principal; velocidade isolada do motor não basta.

---

## 6. ⚠️ Principais riscos

1. **Divergência de regras:** recompensas, transições ou ações podem mudar sutilmente.
2. **Identidade das unidades:** cópias e referências compartilhadas podem gerar bugs.
3. **RNG:** diferenças de consumo aleatório podem alterar a sequência das partidas.
4. **Conversões entre linguagens:** cópias de grandes estruturas podem reduzir o ganho esperado.
5. **Multiprocessing:** compilação, importação e isolamento do estado precisam funcionar nos subprocessos.
6. **Debugging:** falhas nativas podem ser mais difíceis de diagnosticar do que exceções Python.
7. **Manutenção dupla:** preservar Python e C++ exige testes e documentação consistentes.

Mitigação: migrar por módulos, comparar com a referência e exigir critérios de aprovação antes de avançar.

---

## 7. 📋 Ordem de execução resumida

| Ordem | Etapa | Prioridade |
|---|---|---|
| 0 | Congelar referência Python | Obrigatória |
| 1 | Infraestrutura e bindings | Obrigatória |
| 2 | Estado e identidade | Obrigatória |
| 3 | Pool e loja | Máxima |
| 4 | Operações de jogo | Alta |
| 5 | Composição e sinergias | Alta |
| 6 | Rodadas e combate | Alta |
| 7 | Máscaras e anti-loop | Alta |
| 8 | Observações, recompensas e Gymnasium | Obrigatória |
| 9 | Integração PPO | Obrigatória |
| 10 | Equivalência completa | Bloqueante |
| 11 | Benchmark e otimização | Bloqueante |
| 12 | Ativação gradual | Final |

## 8. ✅ Condições para considerar a migração concluída

A migração só será considerada concluída quando:

- Todas as funcionalidades necessárias do ambiente estiverem no motor C++.
- A geração de máscaras no backend C++ não depender de cálculo de máscaras em Python.
- Os contratos do ambiente e a integração PPO estiverem preservados.
- A suíte de equivalência e regressão estiver aprovada.
- Partidas longas e multiprocessing estiverem estáveis.
- O benchmark demonstrar o ganho real sem comprometer a qualidade do treinamento.
- O backend Python continuar disponível para comparação e rollback.
- A documentação de arquitetura, build, testes e execução estiver atualizada.

**Decisão final:** a migração completa para C++ será um projeto futuro e incremental. Até lá, o ambiente Python continua como referência e backend padrão; o trabalho atual de máscaras C++ permanece independente e aproveitável.