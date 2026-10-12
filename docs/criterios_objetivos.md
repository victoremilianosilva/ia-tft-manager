# Critérios Objetivos de Equivalência — Implementações Python e C++ de Action Masks e AntiLoop

## 1. Objetivo

Definir critérios verificáveis para demonstrar que a implementação nativa em C++ reproduz o comportamento da implementação Python na geração de máscaras, validação de movimentos e detecção de bloqueios AntiLoop.

A equivalência deve cobrir quatro dimensões independentes:

1. **Equivalência de saída:** máscaras, indicadores e motivos de bloqueio iguais.
2. **Equivalência de estado:** nenhuma mutação inesperada e mesmas atualizações após operações mutáveis.
3. **Equivalência comportamental:** mesmos movimentos aceitos, bloqueados ou rejeitados nos mesmos cenários.
4. **Equivalência de integração:** mesmas dimensões, tipos, fallbacks e tratamento de erros na interface Python/C++.

A comparação deve usar a implementação Python atual como referência. Uma divergência não deve ser considerada aceitável apenas porque o resultado parece estrategicamente razoável.

## 2. Estratégia de comparação

Cada caso de teste deve ser executado em duas instâncias independentes:

- Instância Python de referência.
- Instância C++ em avaliação, acessada pela interface nativa.

Ambas recebem snapshots equivalentes de estado inicial. Nenhuma implementação deve compartilhar objetos mutáveis com a outra.

O fluxo de comparação é:

1. Construir o cenário de teste.
2. Serializar ou copiar o estado inicial.
3. Executar a operação na implementação Python.
4. Executar a mesma operação na implementação C++.
5. Comparar os resultados.
6. Comparar o estado antes e depois da operação.
7. Registrar a primeira divergência encontrada.
8. Repetir o caso para verificar estabilidade.

Os testes devem começar com operações isoladas e avançar para sequências de movimentos, resets e casos de integração.

## 3. Critérios para comparar as máscaras

### 3.1. Formatos obrigatórios

As duas implementações devem retornar as oito máscaras com estas dimensões:

| Máscara | Dimensão |
|---|---|
| `type_mask` | `(7,)` |
| `shop_mask` | `(5,)` |
| `bench_source_mask` | `(9,)` |
| `board_target_mask` | `(28,)` |
| `board_source_mask` | `(28,)` |
| `board_move_target_masks` | `(28, 28)` |
| `bench_move_source_mask` | `(9,)` |
| `bench_to_board_target_masks` | `(9, 28)` |

Critérios objetivos:

- Todas as máscaras obrigatórias estão presentes.
- Nenhuma dimensão difere da especificação.
- Nenhuma máscara contém `NaN`, infinito ou valores diferentes de zero e um.
- Cada posição habilitada em Python também está habilitada em C++.
- Cada posição desabilitada em Python também está desabilitada em C++.

### 3.2. Igualdade exata

As máscaras são estruturas discretas de validade. Portanto, o critério de aceitação é **igualdade exata elemento a elemento**, não uma tolerância percentual.

Para cada máscara \(M\):

\[
M_{\text{Python}} = M_{\text{C++}}
\]

A comparação deve identificar:

- Nome da máscara.
- Índices divergentes.
- Valor Python.
- Valor C++.
- Snapshot e caso de teste que produziram a diferença.

Uma diferença de um único bit é uma divergência funcional, mesmo que represente apenas uma posição do tabuleiro.

### 3.3. Indicadores auxiliares

Quando o contrato incluir indicadores como `buy_available`, `sell_available`, `has_valid_board_move` e `has_valid_bench_move`, eles também devem ser idênticos.

O teste precisa distinguir uma opção real de um fallback técnico. Uma posição habilitada para evitar uma distribuição categórica vazia não pode ser interpretada como prova de que existe um movimento válido.

### 3.4. Coerência entre máscaras

Além da igualdade com Python, devem ser verificadas as relações internas:

- `type_mask` só habilita `MOVE_BOARD` quando existe um movimento real de tabuleiro.
- `type_mask` só habilita `MOVE_BENCH` quando existe um movimento real do banco para o tabuleiro.
- Uma origem real habilitada deve possuir pelo menos um destino real válido.
- Destinos diagonais (`source == target`) não podem ser movimentos reais de tabuleiro.
- Uma origem vazia não pode ser habilitada como origem real de movimento.
- As máscaras de destino condicionais devem corresponder à origem selecionada.
- Um jogador eliminado deve manter a semântica oficial de ações permitidas, incluindo o `PASS` e os fallbacks técnicos das demais dimensões.

Essas verificações complementam a comparação; não substituem a implementação Python como referência.

## 4. Critérios para motivos de bloqueio

### 4.1. Comparação exata

Para cada candidato, comparar:

- Resultado booleano de `should_block_move()`.
- Resultado textual de `get_block_reason()`.
- Tipo de movimento avaliado.
- Origem e destino.
- Identidade da unidade.
- Estado e histórico usados na consulta.

Os motivos devem coincidir exatamente, incluindo `None` quando não há bloqueio.

### 4.2. Precedência obrigatória

A ordem de referência é:

1. `explicit`
2. `reverse`
3. `oscillation`
4. `bench_board_loop`
5. `cycle`
6. `None`

Nos casos em que várias regras reconheçam o mesmo candidato, o C++ deve retornar o primeiro motivo segundo essa ordem.

Não basta que ambas as implementações bloqueiem o movimento: o motivo também precisa ser igual, pois influencia diagnósticos e contadores específicos.

### 4.3. Casos de conflito

A suíte deve incluir pelo menos:

- Bloqueio explícito combinado com reversão.
- Bloqueio explícito combinado com oscilação.
- Reversão combinada com oscilação.
- Oscilação combinada com ciclo.
- Ciclo banco ↔ tabuleiro combinado com outra proteção aplicável.
- Ciclo geral isolado.
- Candidato sem nenhuma proteção aplicável.
- Bloqueio explícito associado a um estado diferente do atual.

O resultado esperado deve ser definido antes de executar a implementação C++, para evitar adaptar a expectativa ao resultado obtido.

## 5. Critérios de identidade e equivalência de movimentos

Os testes devem preservar as regras de identidade atuais:

- UUID presente: identidade baseada em UUID.
- UUID ausente: identidade baseada em `id` e `star`, com `star` padrão igual a 1.
- Objeto que não seja um dicionário: identidade `None`.

Devem ser comparados separadamente:

- Chave exata de movimento.
- Reversão de movimento normal.
- Reversão de `board_swap`.
- Oscilação da mesma unidade.
- Ciclo banco ↔ tabuleiro.
- Ciclo geral no tabuleiro.
- Assinatura ordenada do tabuleiro e banco.

Unidades distintas com o mesmo `id` e `star`, mas sem UUID, devem seguir a equivalência atual do Python. O C++ não pode introduzir identidade por endereço de memória, ponteiro ou outra regra diferente.

## 6. Critérios de equivalência do estado

Comparar snapshots completos antes e depois de cada operação.

### 6.1. Consultas

Para geração de máscaras e consultas AntiLoop, o estado mutável deve permanecer inalterado.

Comparar, no mínimo:

- `position_history`.
- `move_history`.
- `blocked_moves`.
- `state_visits`.
- `last_board_signature`.
- `blocked_move_states`.
- `last_move`.
- `execution_metrics`.
- Tabuleiro e banco.
- Economia e loja, quando presentes no snapshot.

Critério: nenhuma diferença em campos mutáveis que a operação não esteja autorizada a alterar.

Logs de diagnóstico e estatísticas internas de cache podem ser excluídos dessa comparação somente se forem explicitamente classificados como telemetria que não influencia as decisões. Se a existência de cache puder alterar saídas futuras, seu estado também precisa ser testado.

### 6.2. Operações mutáveis

Para `register_state()`, `register_move()`, `block_move()`, registros de métricas, execução e reset, comparar:

- Retorno da operação.
- Conteúdo de cada estrutura alterada.
- Ordem dos registros.
- Tamanho dos históricos após aplicar limites.
- Valores de contadores.
- Estado final do jogo, quando aplicável.

A equivalência exige o mesmo estado final, não apenas o mesmo número de entradas.

### 6.3. Semântica de reset

Após reset:

- Históricos de posição e movimentos devem seguir a mesma política de limpeza.
- Bloqueios explícitos e assinaturas associadas devem ser tratados de forma idêntica.
- Contagem de visitas e último movimento devem coincidir.
- Métricas acumuladas devem manter a semântica atual: o reset do AntiLoop não apaga os contadores de execução.

O teste deve verificar o estado imediatamente após o reset e também se o episódio seguinte é influenciado indevidamente pelo histórico anterior.

## 7. Critérios para resultados de execução

Para movimentos de banco e tabuleiro, a comparação deve incluir:

- Se a ação foi concluída.
- Se o tabuleiro e banco foram alterados.
- Se houve bloqueio AntiLoop.
- Motivo registrado em `info`.
- Recompensa retornada.
- Tentativas, bloqueios e sucessos registrados.
- Histórico de movimento após a operação.
- Estado após falhas e rollbacks.

### 7.1. Movimento bloqueado

Critérios:

- O movimento não altera o tabuleiro nem o banco.
- O motivo registrado coincide.
- A tentativa e o bloqueio são contabilizados conforme o caminho Python.
- Não há registro de movimento bem-sucedido.
- A recompensa e os campos de `info` coincidem.

### 7.2. Movimento bem-sucedido

Critérios:

- As unidades ocupam as mesmas posições finais.
- O mesmo tipo de movimento é registrado.
- A identidade da unidade registrada coincide.
- `last_move` e `move_history` são atualizados de forma equivalente.
- Os contadores de sucesso coincidem.
- Recompensa e informações de retorno coincidem, quando o teste inclui o fluxo completo do ambiente.

### 7.3. Movimento inválido ou falho

Testar índice fora dos limites, origem vazia, origem igual ao destino, destino ocupado no caso banco → tabuleiro e falha de movimentação.

As duas implementações devem preservar a mesma separação entre:

- Rejeição por validação básica.
- Bloqueio AntiLoop.
- Falha operacional após a validação.
- Sucesso.

A ordem das validações deve ser mantida quando ela afeta as métricas ou o conteúdo de `info`.

## 8. Casos extremos obrigatórios

A suíte de equivalência deve cobrir:

1. Tabuleiro vazio.
2. Tabuleiro cheio.
3. Banco vazio.
4. Banco cheio.
5. Ausência de movimentos válidos.
6. Ausência de compras válidas.
7. Ouro exatamente igual ao custo e insuficiente por uma unidade.
8. Jogador eliminado.
9. Históricos vazios.
10. Históricos no limite de capacidade.
11. Estado visitado exatamente até o limiar de repetição.
12. Bloqueio explícito com assinatura correspondente e divergente.
13. Identidades com e sem UUID.
14. Identidade `None`.
15. Índices negativos e acima dos limites.
16. Destinos ocupados e vazios.
17. Mais de uma regra de bloqueio aplicável.
18. Exceção durante consulta AntiLoop na geração das máscaras.
19. Falha na operação de movimentação e rollback.
20. Reset seguido de nova geração de máscaras.
21. Chamadas repetidas de consulta sobre o mesmo snapshot.
22. Snapshots de jogadores diferentes processados em sequência.
23. Estado espacial igual com economia diferente.
24. Histórico igual com uma identidade ou ordem de movimentos diferente.

Os casos devem ser determinísticos e não depender de sorteio de unidades, relógio ou estado global aleatório, salvo quando esses fatores forem o próprio objeto do teste.

## 9. Critérios de determinismo

Para um snapshot idêntico, parâmetros idênticos e histórico idêntico:

- A mesma implementação deve produzir a mesma saída em chamadas repetidas.
- Python e C++ devem produzir saídas idênticas.
- Consultas repetidas não podem mudar o resultado pela própria execução da consulta.
- A ordem dos testes não pode contaminar os resultados.
- Um reset deve restaurar o comportamento esperado para um novo episódio, respeitando métricas que são intencionalmente cumulativas.

Quando houver dependência de aleatoriedade na preparação do cenário ou na política, a aleatoriedade deve ser controlada. A comparação das máscaras deve ocorrer antes da amostragem da política PPO.

## 10. Tratamento de erros

Comparar também os comportamentos de erro:

- Entrada malformada.
- Dimensão incorreta.
- Tipo de movimento desconhecido.
- Unidade com formato inválido.
- Índice inválido.
- Falha de conversão Python/C++.
- Falha de execução nativa.

A interface deve distinguir uma entrada inválida de um bloqueio AntiLoop. Uma exceção nativa não pode ser convertida silenciosamente em uma máscara permissiva, a menos que isso faça parte explícita do fallback configurado e preserve a política de segurança definida para a integração.

Se o modo de execução usar fallback Python, comparar e registrar qual implementação forneceu o resultado final. Uma saída de fallback não deve ser contabilizada como sucesso da implementação C++.

## 11. Classificação das divergências

Cada falha deve ser classificada em uma das categorias:

| Categoria | Exemplo | Severidade |
|---|---|---|
| Máscara | Um destino habilitado em apenas uma implementação | Bloqueante |
| Motivo | Ambas bloqueiam, mas retornam motivos diferentes | Bloqueante |
| Estado | Consulta altera histórico ou contadores | Bloqueante |
| Sequência | Históricos finais têm conteúdo ou ordem diferentes | Bloqueante |
| Execução | Movimento é aceito em uma implementação e rejeitado na outra | Bloqueante |
| Erro/fallback | Uma implementação falha silenciosamente ou usa fallback diferente | Bloqueante |
| Integração | Dimensão, tipo ou campo obrigatório incorreto | Bloqueante |
| Desempenho | Resultados iguais, mas latência diferente | Não funcional; avaliar separadamente |
| Telemetria auxiliar | Diferença em dado explicitamente não decisório | Avaliar impacto antes de aceitar |

Uma divergência funcional não deve ser descartada como diferença numérica irrelevante. Máscaras, motivos, índices e estruturas discretas exigem igualdade exata.

## 12. Relatório automatizado de equivalência

Cada execução deve produzir um relatório com:

- Identificador do caso.
- Semente e parâmetros, quando aplicáveis.
- Snapshot inicial.
- Operação testada.
- Resultado Python.
- Resultado C++.
- Máscaras divergentes e índices.
- Motivos de bloqueio.
- Estado mutável antes e depois.
- Métricas antes e depois.
- Erros e fallback utilizados.
- Tempo da operação em cada implementação.
- Resultado final: `PASS` ou `FAIL`.

O relatório deve registrar a primeira divergência e permitir reproduzir o caso isoladamente.

## 13. Critérios de aceitação

A equivalência funcional somente pode ser declarada quando:

1. Todos os casos obrigatórios executados passam.
2. Todas as máscaras coincidem exatamente.
3. Todos os motivos de bloqueio coincidem exatamente.
4. Todas as operações mutáveis produzem estados finais equivalentes.
5. Consultas não produzem mutações inesperadas.
6. Reset, limites de histórico e métricas seguem a mesma semântica.
7. Casos extremos e erros possuem resultados previstos.
8. Não existem divergências funcionais conhecidas sem resolução.
9. A integração não esconde falhas nativas por fallback indevido.
10. Os testes podem ser repetidos e reproduzem os mesmos resultados.

O desempenho deve ser avaliado em uma etapa separada, usando os mesmos cenários e medindo latência média, P95, custo de conversão do snapshot e custo total do caminho de máscaras. Ganho de desempenho não compensa falha de equivalência.

## 14. Conclusão

O critério objetivo é **igualdade exata das saídas discretas, equivalência das mutações autorizadas e ausência de efeitos colaterais inesperados**.

A comparação precisa abranger máscaras, motivos de bloqueio, histórico, métricas, execução e comportamento nos casos extremos. Somente depois de demonstrada essa equivalência é possível avaliar a ativação controlada da implementação C++ com confiança.