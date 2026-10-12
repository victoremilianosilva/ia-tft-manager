# Linha de Base de Desempenho — Migração de Action Masks e AntiLoop para C++

## 1. Objetivo

Registrar as medições da implementação Python antes da migração para permitir uma comparação reproduzível com a implementação C++.

A linha de base deve responder a quatro perguntas:

1. Quanto tempo custa gerar as máscaras?
2. Quais funções concentram o custo computacional?
3. Qual é o impacto das máscaras no ciclo completo de decisão do PPO?
4. Qual foi o ganho real após a migração, considerando também conversões e comunicação entre Python e C++?

As medições históricas disponíveis são registradas abaixo. Elas não devem ser confundidas com um benchmark único e totalmente controlado: foram executadas em cenários diferentes e devem ser comparadas somente com medições futuras equivalentes.

## 2. Ambiente de referência

### 2.1. Configuração identificada no código

| Item | Configuração |
|---|---|
| Linguagem da implementação de referência | Python |
| Framework de aprendizado | PyTorch |
| Algoritmo | PPO |
| Dispositivo configurado para treinamento | CPU |
| Lobbies paralelos no benchmark de treinamento | 4 |
| Jogadores por lobby | 8 |
| Agentes por iteração | 32 |
| Dimensões da ação | `[7, 5, 9, 28, 28, 28]` |
| Versão C++ configurada no projeto | C++20 |
| Integração nativa existente | pybind11 |
| Motor C++ existente | `combat_engine` |

O `trainer.py` configura explicitamente `self.device = torch.device("cpu")`. A configuração de GPU disponível no equipamento é impressa pelo programa, mas não significa que o treinamento esteja utilizando a GPU.

O `cpp/CMakeLists.txt` declara C++20 e localiza Python e pybind11. Também contém um caminho absoluto para uma instalação local de pybind11, detalhe relevante para reproduzir a compilação.

### 2.2. Dados de ambiente ainda não confirmados

Os seguintes dados precisam ser registrados na próxima execução de referência:

- Versão exata do Python.
- Versão do PyTorch e NumPy.
- Versão do sistema operacional e compilação.
- Processador, número de núcleos e memória RAM.
- Versão do compilador C++ e configuração de otimização.
- Versões do CMake e pybind11.
- Commit Git usado no benchmark.
- Configuração real de `use_subprocess`.
- Estado de outros processos que possam disputar CPU e memória.

Esses valores não são inferidos a partir das medições anteriores.

## 3. Linha de base histórica

### 3.1. Geração de máscaras por jogador

<text color="secondary" size="sm">500 amostras por jogador ativo; 8 jogadores ativos.</text>

| Métrica | Resultado |
|---|---:|
| Média por jogador | 0,1860 ms |
| Mediana por jogador | 0,1755 ms |
| P95 por jogador | 0,3248 ms |
| Média mínima observada entre jogadores | 0,1765 ms |
| Média máxima observada entre jogadores | 0,1999 ms |
| Custo estimado para 8 jogadores | 1,4881 ms |

O custo para oito jogadores foi estimado multiplicando a média por oito. Não corresponde necessariamente ao tempo de uma chamada completa da lobby, porque montagem, conversão e coordenação não estão incluídas de forma garantida.

### 3.2. `MiniTFTEnv.step()` e combate

<text color="secondary" size="sm">500 amostras; ação PASS; HP restaurado antes de cada combate.</text>

| Métrica | `MiniTFTEnv.step()` | `TFTLobby.resolve_combat()` |
|---|---:|---:|
| Média | 0,2877 ms | 0,1005 ms |
| Mediana | 0,2821 ms | 0,0978 ms |
| P95 | 0,3080 ms | 0,1173 ms |
| Mínimo | 0,2769 ms | 0,0958 ms |
| Máximo | 0,6114 ms | 0,2246 ms |

O cenário de combate utilizava uma unidade por lado. A medição de `resolve_combat()` representa o caminho completo da função, não apenas o tempo interno do motor C++.

Portanto, não deve ser usada isoladamente para estimar o ganho da migração das máscaras e do AntiLoop.

### 3.3. Throughput inicial do ambiente

<text color="secondary" size="sm">Ação PASS; 4 lobbies × 8 jogadores; 500 chamadas vetorizadas.</text>

| Métrica | Resultado |
|---|---:|
| Média por chamada vetorizada | 341,8654 ms |
| Mediana por chamada vetorizada | 343,4781 ms |
| P95 por chamada vetorizada | 364,1867 ms |
| Tempo total | 170,933 s |
| Chamadas vetorizadas | 500 |
| Passos de lobby | 2.000 |
| Passos de jogador | 16.000 |
| Chamadas vetorizadas por segundo | 2,93 |
| Passos de lobby por segundo | 11,70 |
| Passos de jogador por segundo | 93,60 |

Este benchmark utilizava PASS e não representava integralmente o fluxo real de decisões com geração de máscaras, política e movimentações. É uma referência histórica do ambiente, não a métrica principal para avaliar a migração.

### 3.4. Fluxo real do PPO

<text color="secondary" size="sm">Checkpoint carregado; 500 iterações.</text>

| Etapa | Média | P95 |
|---|---:|---:|
| Obtenção e montagem das máscaras (`masks`) | 69,602 ms | 103,353 ms |
| Inferência da política (`policy`) | 5,305 ms | 6,338 ms |
| Conversão (`conversion`) | 0,057 ms | 0,074 ms |
| Execução dos ambientes (`env_step`) | 46,140 ms | 126,949 ms |
| Fluxo total (`total`) | 121,137 ms | 217,930 ms |

Resultados gerais:

- 500 iterações em 60,57 segundos.
- Aproximadamente 8,26 iterações por segundo.
- Aproximadamente 264,16 decisões de agente por segundo, considerando 32 agentes por iteração.

Os valores das etapas são medições separadas e não devem ser somados mecanicamente para exigir que coincidam com o tempo total. Instrumentação, coordenação, sobreposição de intervalos e outros custos podem explicar diferenças.

Este é o benchmark histórico mais relevante para observar o impacto da migração no fluxo completo de treinamento.

### 3.5. Perfil dos gargalos de máscaras

<text color="secondary" size="sm">Perfil de 100 chamadas a `env_method` distribuídas por 4 lobbies; 400 chamadas a `TFTLobby.get_action_masks()`.</text>

| Métrica | Média | Mediana | P95 |
|---|---:|---:|---:|
| Obtenção das máscaras das lobbies | 34,993 ms | 34,461 ms | 38,056 ms |
| `_flatten_masks()` | 2,330 ms | 2,232 ms | 2,624 ms |
| Fluxo combinado de máscaras | 37,323 ms | 36,714 ms | 41,970 ms |

Tempo acumulado reportado pelo `cProfile`:

| Função | Tempo cumulativo |
|---|---:|
| `ActionMaskManager.get_board_move_masks()` | 6,831 s |
| `_is_valid_board_move()` | 6,345 s |
| `_should_block_anti_loop()` | 6,345 s |
| `AntiLoopManager.should_block_move()` | 6,036 s |
| `AntiLoopManager.get_block_reason()` | 5,812 s |
| `_unit_identity()` | 1,676 s |
| `is_cycle_move()` | 1,660 s |
| `is_oscillating()` | 1,427 s |
| `ShopManager.get_shop()` | 0,832 s |
| Operações de `deepcopy` associadas | 0,823 s |
| `get_bench_move_masks()` | 0,793 s |
| `_is_valid_bench_board_move()` | 0,724 s |

Os tempos cumulativos das funções se sobrepõem: uma função pode incluir o tempo gasto nas funções que chama. **Não se deve somar esses valores para calcular o tempo total.**

O perfil indica que a avaliação repetida de candidatos do tabuleiro e as consultas AntiLoop são os principais alvos para investigação. A cópia da loja aparece como um alvo secundário, enquanto a conversão final das máscaras tem custo relativamente menor nesse perfil.

## 4. Metodologia oficial para o próximo benchmark

As medições históricas acima devem ser preservadas, mas a comparação oficial antes/depois precisa seguir um protocolo controlado.

### 4.1. Preparação

1. Fixar o commit Python usado como referência.
2. Registrar versões de Python, bibliotecas, compilador e sistema.
3. Usar os mesmos snapshots determinísticos para Python e C++.
4. Incluir tabuleiros, bancos, lojas e históricos AntiLoop representativos.
5. Separar o tempo de preparação dos snapshots do tempo de geração das máscaras.
6. Executar aquecimento antes das medições.
7. Realizar pelo menos 1.000 medições por cenário, quando o custo permitir.
8. Repetir cada cenário em pelo menos três execuções independentes.
9. Reportar média, mediana, P95, desvio-padrão e número de amostras.
10. Registrar o custo da instrumentação e evitar profiling pesado no benchmark de latência final.

A quantidade de amostras deve ser igual entre as implementações comparadas, salvo se houver uma justificativa documentada.

### 4.2. Cenários obrigatórios

- Máscaras de um jogador com estado simples.
- Máscaras de um jogador com tabuleiro parcialmente ocupado.
- Tabuleiro com muitos candidatos a movimento.
- Histórico AntiLoop vazio.
- Histórico AntiLoop com oscilações e ciclos.
- Quatro lobbies com oito jogadores.
- Fluxo real do PPO com checkpoint fixo.
- Caminho completo Python → snapshot → C++ → máscaras Python.
- Fallback Python quando a implementação nativa falhar.

O benchmark de fallback deve ser identificado separadamente e não contabilizado como desempenho nativo.

### 4.3. Medições separadas

Registrar, no mínimo:

| Métrica | Finalidade |
|---|---|
| `mask_generation_python_ms` | Referência de geração Python |
| `mask_generation_cpp_ms` | Cálculo nativo isolado |
| `snapshot_conversion_ms` | Custo de preparar a entrada |
| `binding_transfer_ms` | Custo de atravessar a interface Python/C++ |
| `full_mask_pipeline_ms` | Custo total de geração e integração |
| `env_step_ms` | Impacto no passo completo do ambiente |
| `ppo_iteration_ms` | Impacto no fluxo de treinamento |
| `native_fallback_count` | Quantidade de chamadas que retornaram ao Python |
| `shadow_divergence_count` | Divergências entre implementações |

O cálculo isolado em C++ é útil para diagnóstico, mas o critério de desempenho deve considerar principalmente o pipeline completo. Um motor muito rápido pode não gerar ganho relevante se conversões e cópias dominarem o custo.

## 5. Fórmulas para avaliar o ganho

Para uma métrica de latência comparável:

\[
\text{Speedup} =
\frac{T_{\text{Python}}}{T_{\text{C++ integrado}}}
\]

\[
\text{Redução de latência (\%)} =
100\left(1-\frac{T_{\text{C++ integrado}}}{T_{\text{Python}}}\right)
\]

Para throughput:

\[
\text{Ganho de throughput (\%)} =
100\left(\frac{Q_{\text{C++}}}{Q_{\text{Python}}}-1\right)
\]

Onde:

- \(T\) é a latência da mesma operação e cenário.
- \(Q\) é o throughput medido com a mesma unidade de trabalho.

A redução de latência e o ganho de throughput não são necessariamente iguais, especialmente quando existe paralelismo ou sobreposição de operações.

## 6. Critérios para aceitar a comparação

A medição pós-migração só deve ser considerada válida quando:

- Os cenários de entrada são equivalentes.
- As máscaras e os resultados passam nos testes de equivalência.
- A quantidade de trabalho é igual.
- As versões e configurações são registradas.
- O custo de conversão e integração está incluído no resultado principal.
- O P95 é reportado junto da média.
- Os resultados de profiling não são misturados com benchmarks sem instrumentação.
- Os casos que usaram fallback são contabilizados separadamente.

A equivalência funcional é pré-requisito: desempenho melhor com divergência de comportamento não constitui sucesso da migração.

## 7. Registro da execução futura

Para cada benchmark, registrar:

- Identificador e data.
- Commit Git.
- Implementação ativa (`python`, `shadow` ou `native`).
- Sistema operacional e hardware.
- Versões das ferramentas.
- Configuração do ambiente.
- Cenário e quantidade de amostras.
- Métricas de latência e throughput.
- Quantidade de fallbacks e divergências.
- Resultado dos testes de equivalência.

## 8. Conclusão

A linha de base histórica indica que a obtenção das máscaras e o fluxo de execução dos ambientes são custos relevantes no treinamento. O perfil aponta a geração de movimentos do tabuleiro e as consultas AntiLoop como os alvos prioritários para otimização.

As medições históricas ficam registradas como referências preliminares. Antes de declarar um ganho percentual definitivo, será necessário confirmar o ambiente de execução e realizar uma comparação controlada, com os mesmos snapshots e a mesma metodologia para Python e C++.