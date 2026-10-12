# Documentação Geral — Migração da Engine de Decisão da IA TFT para C++

## 1. Objetivo

Migrar para C++ os componentes responsáveis pela geração das Action Masks, validação de movimentos e gerenciamento de AntiLoop da IA TFT, preservando o comportamento atual do ambiente e a compatibilidade com a política PPO existente.

A migração tem como objetivos principais:

- Reduzir o custo computacional da geração e validação de ações.
- Reduzir o overhead das chamadas repetidas entre Python e C++.
- Preservar as regras de validade de movimentos e prevenção de loops.
- Manter a compatibilidade com a política PPO, os ambientes e o treinamento.
- Validar a equivalência funcional antes de ativar a implementação nativa como caminho principal.
- Evitar alterações desnecessárias nos testes unitários existentes.

## 2. Escopo

### 2.1. Componentes que serão migrados

- Geração das Action Masks.
- Validação de ações e movimentos.
- Regras de AntiLoop.
- Validação de movimentos entre banco e tabuleiro.
- Validação de movimentos dentro do tabuleiro.
- Integração entre as regras de decisão e a geração das máscaras condicionais.

### 2.2. Componentes que permanecerão em Python

- Política PPO e rede neural.
- Treinamento e atualização dos parâmetros.
- Ambientes de treinamento e orquestração das lobbies.
- Execução das ações no ambiente.
- Sistema de recompensas.
- Economia, progressão e demais regras do jogo fora do escopo da migração.

A engine C++ será responsável pelo processamento nativo das regras de decisão, enquanto Python continuará coordenando o ambiente e o treinamento.

## 3. Arquitetura proposta

A migração utilizará a infraestrutura C++ existente no projeto, estendendo-a com um módulo específico chamado `decision_engine`.

Não será criado um projeto C++ independente nem será duplicada a infraestrutura genérica de compilação e bindings já existente.

A arquitetura lógica será composta por:

1. **Interface Python:** recebe os dados do ambiente e disponibiliza os resultados para os componentes existentes.
2. **Decision Engine C++:** executa as regras migradas de validação, AntiLoop e geração das máscaras.
3. **Bindings via pybind11:** conectam a implementação nativa ao Python.
4. **Seleção de backend:** permite escolher a implementação Python ou C++ durante a validação.
5. **Testes e diagnósticos:** verificam compatibilidade, equivalência funcional, regressões e desempenho.

O módulo de decisão deverá possuir contratos de entrada e saída explícitos, independentes das estruturas específicas utilizadas pelo motor de combate.

A transferência de dados entre Python e C++ deverá ocorrer preferencialmente em lote, evitando chamadas nativas individuais para cada candidato de movimento.

## 4. Estratégia de versionamento

A migração será desenvolvida em uma branch exclusiva, separada da linha principal de desenvolvimento.

Essa branch permitirá revisar as alterações de forma isolada, comparar versões e recuperar o estado anterior por meio do controle de versão.

O versionamento não elimina a necessidade de validação funcional. Os commits devem representar etapas verificáveis da migração, facilitando a identificação de regressões e a revisão das mudanças.

Nenhuma alteração na arquitetura da política PPO, nas dimensões do espaço de ações ou nas regras de recompensa faz parte desta migração.

## 5. Estratégia para os testes unitários existentes

### 5.1. Princípio fundamental

Os testes unitários existentes deverão ser preservados, sem modificações desnecessárias nas asserções, nos cenários ou nas expectativas de comportamento.

O objetivo é testar a implementação C++ por meio dos mesmos contratos já utilizados para validar a implementação Python.

A troca deve acontecer na implementação selecionada pelo código de integração, não na lógica interna dos testes.

### 5.2. Seleção de backend

Será implementado um mecanismo explícito de seleção da engine utilizada na execução.

Os modos previstos são:

- **Python:** utiliza a implementação atual como referência.
- **C++:** utiliza a implementação nativa.
- **Shadow:** calcula as saídas das duas implementações para o mesmo estado, utilizando Python como resultado efetivo durante a comparação.

A interface de seleção ainda deverá ser implementada. Uma variável de ambiente, como `DECISION_ENGINE`, poderá ser utilizada para definir o backend.

Os nomes e comandos definitivos serão confirmados durante a implementação.

### 5.3. Execução da mesma suíte

A validação deverá executar os testes existentes separadamente para cada backend, utilizando as mesmas condições e expectativas sempre que aplicável.

Exemplo ilustrativo de comandos PowerShell:

```powershell
# Testes com a implementação Python
$env:DECISION_ENGINE = "python"
pytest

# Testes com a implementação C++
$env:DECISION_ENGINE = "cpp"
pytest
```

Esses comandos representam a estratégia pretendida, não uma interface já implementada ou validada. O comando correto de execução deverá respeitar a configuração real do projeto.

Caso um teste dependa diretamente de uma classe concreta da implementação Python, e não de sua interface pública, poderá ser necessário adaptar a forma de integração ou criar uma camada de compatibilidade. A prioridade será preservar o teste e seu objetivo original, evitando alterações desnecessárias em seu conteúdo.

### 5.4. Testes adicionais

Novos testes serão adicionados somente quando necessários para cobrir comportamentos relevantes que não estejam suficientemente verificados pela suíte existente.

Também serão criados testes diferenciais automatizados para comparar os resultados Python e C++ em estados equivalentes.

Esses testes complementares não substituirão nem invalidarão os testes unitários existentes.

## 6. Equivalência comportamental

A implementação C++ deverá reproduzir as regras atuais, incluindo correções, exceções e proteções desenvolvidas anteriormente.

A equivalência será avaliada considerando:

- Dimensões e tipos das máscaras.
- Significado e ordem dos índices.
- Validade das ações e dos movimentos.
- Regras de ocupação e disponibilidade de posições.
- Restrições de movimentação entre banco e tabuleiro.
- Bloqueios de reversões, oscilações, ciclos e movimentos repetitivos.
- Motivos de bloqueio e precedência entre regras.
- Identidade das unidades e critérios de equivalência entre movimentos.
- Dependências entre as etapas condicionais da política autoregressiva.
- Atualizações de histórico, caches e contadores.
- Ausência de efeitos colaterais em consultas que deveriam ser somente leitura.

O espaço de ações atual, com dimensões `[7, 5, 9, 28, 28, 28]`, deverá permanecer inalterado.

A geração das máscaras deverá preservar também seus formatos condicionais, incluindo as máscaras bidimensionais de movimentos entre posições do tabuleiro e entre banco e tabuleiro.

A validação não se limitará à comparação das dimensões: os valores e a semântica das saídas também deverão ser equivalentes.

## 7. Estado e histórico do AntiLoop

O AntiLoop possui regras dependentes do histórico, portanto a equivalência não poderá ser avaliada somente com estados isolados.

Os testes deverão considerar sequências de movimentos, mudanças de estado e atualizações de histórico.

Será necessário preservar:

- A geração das chaves de movimento.
- A identificação das unidades.
- A ordem de avaliação dos motivos de bloqueio.
- A detecção de reversões, oscilações e ciclos.
- As regras para movimentos entre banco e tabuleiro.
- O momento em que movimentos bem-sucedidos são registrados.
- A separação entre consultas e operações que alteram o estado.

Durante a execução em modo de comparação, as duas implementações não poderão atualizar o histórico de maneira duplicada. O resultado de uma consulta comparativa também não poderá alterar indevidamente o estado real do ambiente.

## 8. Fallback e ativação controlada

Durante o desenvolvimento, a implementação Python continuará disponível como referência e mecanismo de recuperação.

A implementação C++ não assumirá o fluxo principal antes da validação dos contratos, da integração e da equivalência comportamental.

A estratégia de ativação prevê:

1. Execução inicial com Python.
2. Comparação paralela entre Python e C++.
3. Execução dos testes existentes com C++ selecionado.
4. Correção das divergências encontradas.
5. Validação da integração com os ambientes e múltiplas lobbies.
6. Avaliação de desempenho.
7. Ativação controlada da implementação C++.
8. Consideração da retirada do caminho Python do fluxo principal após a aprovação dos critérios de aceitação.

A implementação Python não precisará continuar sendo executada no caminho normal depois que o C++ estiver validado. Entretanto, sua remoção definitiva será uma decisão posterior, tomada após a conclusão dos critérios de equivalência e reversibilidade.

## 9. Diagnóstico e classificação de falhas

Os resultados dos testes deverão distinguir três situações:

**Regressão:** um comportamento que passava na implementação Python deixa de passar na implementação C++.

**Falha preexistente:** o teste já falhava antes da migração e continua falhando, sem evidência de que a mudança tenha causado o problema.

**Divergência comportamental:** as duas implementações produzem resultados diferentes para entradas equivalentes, mesmo que os testes unitários existentes não detectem a diferença.

Todas as divergências relevantes deverão ser investigadas. Não será suficiente considerar a migração correta apenas porque a suíte atual terminou sem falhas.

## 10. Desempenho

A implementação C++ deverá ser avaliada com os mesmos cenários e condições de referência utilizados para medir o código Python.

As medições deverão incluir:

- Tempo de geração das máscaras.
- Tempo de validação dos movimentos.
- Tempo de execução do AntiLoop.
- Custo da conversão e transferência de dados.
- Tempo total do fluxo de decisão.
- Throughput de decisões e steps.
- Média, mediana, P95 e variabilidade.

As otimizações deverão preservar as regras de comportamento. Caso uma alteração de desempenho introduza divergências, ela deverá ser corrigida antes de ser aprovada.

## 11. Critérios para considerar a migração concluída

A migração somente será considerada concluída quando:

- O módulo nativo compilar e puder ser importado no ambiente do projeto.
- Os testes unitários existentes forem executados com o backend C++.
- As falhas preexistentes estiverem identificadas e separadas das regressões.
- Os testes de equivalência confirmarem os resultados esperados.
- As divergências relevantes estiverem corrigidas ou formalmente identificadas como bloqueios.
- A integração com os ambientes, a política PPO e múltiplas lobbies estiver validada.
- O estado e o histórico do AntiLoop forem preservados corretamente.
- O fallback Python estiver funcional e tiver sido testado.
- Os benchmarks comparativos estiverem documentados.
- O procedimento de ativação e retorno ao backend Python estiver definido e validado.

## 12. Estado atual do planejamento

A auditoria do comportamento Python e a definição dos contratos necessários para a migração foram documentadas.

A infraestrutura C++ existente será reutilizada. A criação e configuração específica do módulo `decision_engine`, assim como a definição completa de seus tipos compartilhados, ainda fazem parte das próximas etapas de implementação.

A seleção de backend, a execução da suíte de testes com C++ e os testes diferenciais também permanecem como trabalho futuro.

Nenhuma conclusão sobre equivalência funcional, compilação da nova engine ou ganho de desempenho deverá ser registrada antes da execução e verificação dos respectivos testes.

## 13. Princípios de desenvolvimento

A migração seguirá estes princípios:

1. Preservar o comportamento antes de otimizar.
2. Manter os testes existentes sempre que possível.
3. Trocar a implementação por meio de uma interface de seleção, sem reescrever as expectativas dos testes.
4. Comparar as implementações com entradas equivalentes.
5. Evitar efeitos colaterais duplicados durante a validação.
6. Preservar a compatibilidade com PPO e com os checkpoints existentes.
7. Medir o desempenho com cenários reproduzíveis.
8. Manter a possibilidade de retorno ao Python durante a validação.
9. Executar a migração de forma incremental, validando cada etapa antes de avançar.
10. Não considerar a migração concluída enquanto os critérios de aceitação obrigatórios não forem atendidos.