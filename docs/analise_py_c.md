# Análise de Dados entre Python e C++ — Action Masks e AntiLoop

## 1. Objetivo

A migração do gerador de Action Masks e das validações AntiLoop para C++ exige definir quais dados o Python precisa enviar, quais informações o C++ deve calcular e o que precisa retornar para a política PPO.

A separação fundamental é:

- **Python:** continua responsável pelo ambiente, pelos gerenciadores do jogo, pela execução das ações, pelo PPO e pelo treinamento.
- **C++:** recebe uma representação explícita do estado relevante para as decisões, calcula as máscaras e avalia as proteções AntiLoop.
- **Python:** recebe os resultados e os entrega ao fluxo atual de `TFTLobby`, `trainer.py` e `TFTPolicy`.

A proposta é transferir um **snapshot dos dados necessários à decisão**, em vez de tentar compartilhar diretamente objetos Python ou instâncias inteiras dos gerenciadores.

## 2. Dados que precisam ser enviados do Python para o C++

### 2.1. Estado do tabuleiro

O tabuleiro possui 28 posições, indexadas de `0` a `27`.

Para cada posição, o C++ precisa saber:

- Índice da posição.
- Se está vazia ou ocupada.
- Identidade da unidade, conforme as regras atuais do AntiLoop.
- `id` da unidade, quando disponível.
- `star` da unidade, quando disponível.
- UUID, quando disponível.

Esses dados são necessários para:

- Identificar origens válidas.
- Identificar destinos ocupados e vazios.
- Distinguir `board_move` de `board_swap`.
- Gerar `board_source_mask`.
- Gerar `board_move_target_masks`.
- Construir assinaturas equivalentes às atuais.

A posição da unidade precisa ser representada explicitamente. Não basta enviar somente a lista de unidades, porque a localização de cada uma influencia diretamente a validade das ações.

### 2.2. Estado do banco

O banco possui nove posições, indexadas de `0` a `8`.

Para cada posição, o C++ precisa receber:

- Se está vazia ou ocupada.
- Identidade da unidade.
- `id`, `star` e UUID, conforme disponíveis.

Essas informações permitem gerar:

- `bench_source_mask`, para venda.
- `bench_move_source_mask`, para movimentação.
- `bench_to_board_target_masks`, para destinos condicionados à origem.
- Assinaturas do estado conjunto de tabuleiro e banco.

### 2.3. Estado da loja

A loja possui cinco posições, indexadas de `0` a `4`.

O snapshot precisa incluir os dados efetivamente utilizados pelas regras atuais de compra, como:

- Se o slot contém uma unidade disponível.
- Custo da unidade, quando necessário para a validação.
- Saldo de ouro disponível para a compra.

Se as regras atuais utilizarem outros critérios para determinar a disponibilidade de compra, esses critérios também precisam fazer parte do contrato.

A lista deve preservar a posição original de cada unidade na loja. O C++ não deve reorganizar os slots.

### 2.4. Estado econômico e disponibilidade de ações

A máscara de tipos depende de mais informações do que o posicionamento das unidades.

O C++ precisa receber os valores necessários para reproduzir as regras atuais de:

- Compra.
- Atualização da loja (`REROLL`).
- Compra de XP (`BUY_XP`).
- Venda (`SELL`).
- Movimentos do banco e do tabuleiro.
- `PASS`.
- Estado ativo ou eliminado do jogador.

Para economia, devem ser enviados os valores efetivamente consultados pelas regras, como ouro e custo das operações. Se a validade depender de nível, XP ou outro estado, esses campos também deverão ser incluídos.

Não é necessário enviar todo o objeto `EconomyManager`: basta transmitir os dados necessários para reproduzir suas decisões de disponibilidade.

### 2.5. Estado e histórico do AntiLoop

O AntiLoop não depende somente do estado atual. Algumas decisões dependem dos movimentos anteriores e dos bloqueios registrados.

O snapshot precisa representar:

| Dado | Conteúdo necessário |
|---|---|
| Histórico de posições | Assinaturas anteriores do tabuleiro e banco |
| Histórico de movimentos | Tipo, origem, destino e identidade da unidade |
| Último movimento | Registro usado para detectar reversões |
| Bloqueios explícitos | Chaves de movimentos bloqueados |
| Estado associado ao bloqueio | Assinatura que contextualiza cada bloqueio |
| Contagem de visitas | Quantidade de vezes que cada assinatura foi registrada |
| Última assinatura | Estado usado como referência para bloqueios explícitos |

A implementação atual utiliza limites configuráveis de histórico, com `history_size=20`, `blocked_move_size=10` e `loop_threshold=2`.

O C++ precisa respeitar esses limites e a ordem dos registros. Transferir somente o último movimento não reproduziria todas as proteções atuais.

As métricas acumuladas de execução são importantes para diagnóstico, mas não devem ser confundidas com o estado mínimo necessário para decidir se uma ação é válida. Elas podem ser tratadas como um canal adicional de telemetria.

## 3. Resumo do snapshot de entrada

O contrato de entrada pode ser organizado em cinco grupos lógicos:

| Grupo | Dados principais | Utilização |
|---|---|---|
| Tabuleiro | 28 posições e identidades das unidades | Movimentos e trocas |
| Banco | 9 posições e identidades das unidades | Venda e movimentação |
| Loja | 5 slots e dados relevantes para compra | `BUY` |
| Jogador e economia | Estado ativo, ouro e valores exigidos pelas regras | Máscara de tipos e disponibilidade |
| AntiLoop | Históricos, assinaturas, bloqueios e visitas | Proteções contra repetição |

Esse agrupamento é conceitual. Não exige que o transporte use cinco objetos independentes. A estrutura final pode ser um único DTO de entrada, desde que o contrato seja explícito.

## 4. Dados que precisam retornar do C++ para o Python

### 4.1. Máscaras finais

O C++ precisa retornar as oito máscaras do contrato atual:

| Campo | Dimensão por jogador |
|---|---:|
| `type_mask` | `(7,)` |
| `shop_mask` | `(5,)` |
| `bench_source_mask` | `(9,)` |
| `board_target_mask` | `(28,)` |
| `board_source_mask` | `(28,)` |
| `board_move_target_masks` | `(28, 28)` |
| `bench_move_source_mask` | `(9,)` |
| `bench_to_board_target_masks` | `(9, 28)` |

O contrato deve preservar nomes, dimensões, ordem dos índices e significado de cada categoria. A camada Python deve conseguir entregar esses resultados ao treinador sem mudar o contrato consumido pela política.

### 4.2. Indicadores de disponibilidade real

Além das máscaras, o gerador precisa fornecer internamente ou devolver os indicadores de disponibilidade utilizados para calcular a máscara de tipos:

- `buy_available`.
- `sell_available`.
- `has_board_move`.
- `has_bench_move`.

Esses indicadores são importantes porque uma máscara pode conter um fallback técnico habilitado no índice zero sem representar uma ação real disponível.

O C++ deve manter essa distinção. Uma categoria dummy não pode habilitar `MOVE_BOARD` ou `MOVE_BENCH` por engano.

Os indicadores podem ser incluídos em uma estrutura de resultado para facilitar diagnóstico e testes, embora o contrato atual de oito máscaras não exija que todos sejam entregues à política.

### 4.3. Motivo de bloqueio, quando solicitado

Para a geração normal de máscaras, o resultado principal é a máscara de validade.

Para diagnóstico ou validação paralela, é útil que o C++ possa informar, para um candidato específico, o motivo do bloqueio, por exemplo:

- Bloqueio explícito.
- Reversão.
- Oscilação.
- Ciclo banco ↔ tabuleiro.
- Ciclo geral.

Essa informação não precisa ser calculada e transportada para cada par de posições durante toda execução. Pode ser exposta por uma consulta de diagnóstico ou ativada em modo de comparação.

### 4.4. Telemetria opcional

Para comparar a implementação Python com a C++, pode ser útil registrar:

- Quantidade de pares de movimentos examinados.
- Quantidade de candidatos bloqueados por categoria.
- Tempo de geração das máscaras.
- Tempo gasto nas consultas AntiLoop.
- Diferenças encontradas durante a comparação entre implementações.

Esses dados são auxiliares. Não fazem parte das oito máscaras consumidas pela política.

## 5. O que não deve retornar do C++

A política PPO continua sendo executada em Python. Portanto, o módulo C++ não precisa retornar:

- Logits da política.
- Probabilidades das ações.
- Ação amostrada pelo PPO.
- Log-probabilidade.
- Entropia.
- Gradientes.
- Tensores de treinamento.
- Atualizações dos pesos da rede neural.

O C++ determina quais opções são permitidas. A política continua determinando qual das opções permitidas será selecionada.

Da mesma forma, o C++ não deve executar a compra, a venda ou a movimentação só porque calculou uma máscara válida. A execução continua no ambiente Python, que pode validar a ação novamente antes de modificar o estado.

## 6. Estado persistente e estado transitório

É importante separar os dados que mudam a cada consulta dos dados históricos que precisam sobreviver entre consultas.

### Estado transitório

Pode ser reconstruído a partir do estado atual do jogador:

- Ocupação do tabuleiro.
- Ocupação do banco.
- Conteúdo da loja.
- Dados econômicos relevantes.
- Estado ativo ou eliminado.
- Máscaras e indicadores de disponibilidade calculados para aquela consulta.

Esses dados podem ser enviados como um snapshot atualizado.

### Estado persistente

Precisa ser mantido ou sincronizado entre decisões:

- Histórico de posições.
- Histórico de movimentos.
- Último movimento.
- Bloqueios explícitos.
- Assinaturas associadas aos bloqueios.
- Contagem de visitas por assinatura.
- Parâmetros e limites do AntiLoop.

Há duas possibilidades arquiteturais: manter esse histórico no Python e enviá-lo ao C++ em cada consulta, ou manter uma instância de estado AntiLoop no C++ e atualizá-la por eventos. A escolha precisa ser feita antes da implementação.

A segunda opção pode reduzir o volume de dados transferidos, mas exige uma sincronização rigorosa de movimentos executados, falhas, resets e mudanças de estado. Não se deve adotar essa opção sem validar primeiro a equivalência comportamental.

## 7. Regras de sincronização

Para evitar divergências entre Python e C++, o contrato deve definir:

1. **Momento do snapshot:** as máscaras são calculadas a partir de um estado consistente do jogador.
2. **Identidade:** UUID tem precedência sobre a combinação `id + star`, conforme a implementação atual.
3. **Histórico:** a ordem temporal dos movimentos deve ser preservada.
4. **Mutação:** consultar o AntiLoop para gerar uma máscara não deve registrar um movimento como executado.
5. **Execução:** o Python continua responsável por executar e validar a ação escolhida.
6. **Registro:** o histórico deve ser atualizado no momento correspondente ao movimento efetivamente executado, preservando as regras atuais.
7. **Reset:** o estado histórico do AntiLoop precisa ser sincronizado quando o ambiente reinicia, respeitando o comportamento atual das métricas.
8. **Fallbacks:** as categorias dummy devem manter o significado atual.
9. **Jogadores eliminados:** somente `PASS` deve permanecer permitido.
10. **Falhas de integração:** erros de conversão, dados inconsistentes ou respostas incompletas precisam ser detectáveis, sem produzir silenciosamente máscaras semanticamente diferentes.

## 8. Arquitetura de referência

O fluxo de dados proposto é:

1. Python coleta o estado relevante do jogador.
2. Python constrói o snapshot de entrada.
3. O binding Python–C++ converte o snapshot para os tipos nativos.
4. C++ calcula as máscaras e aplica as proteções AntiLoop.
5. C++ devolve as máscaras e, opcionalmente, informações de diagnóstico.
6. Python converte ou valida os resultados e monta o dicionário atual.
7. `trainer.py` consolida os agentes no batch.
8. `TFTPolicy` escolhe a ação.
9. `env.py` valida e executa a ação no estado Python.
10. O histórico AntiLoop é atualizado conforme o resultado da execução.

O contrato não exige transferir objetos Python arbitrários para C++. Estruturas explícitas com tipos e dimensões conhecidos facilitam o binding, os testes e a comparação entre as implementações.

## 9. Critérios para considerar o contrato definido

Antes de implementar a migração, deve ser possível confirmar:

- Quais campos do jogador entram no snapshot.
- Quais atributos da unidade são necessários para identidade e validação.
- Quais campos econômicos influenciam a máscara de tipos.
- Quais estruturas históricas do AntiLoop são transportadas ou mantidas no C++.
- Quais oito máscaras retornam e quais são suas dimensões.
- Como os indicadores de disponibilidade real são representados.
- Como bloqueios e movimentos executados sincronizam o histórico.
- Como resets e jogadores eliminados são tratados.
- Como comparar os resultados Python e C++ para o mesmo snapshot.

## 10. Conclusão

A migração precisa transferir **o estado relevante para a decisão e o histórico necessário para reproduzir as proteções AntiLoop**, não o ambiente inteiro nem os pesos da política PPO.

O retorno obrigatório é o contrato atual das oito máscaras, preservando suas dimensões e semântica. Indicadores de disponibilidade e motivos de bloqueio podem complementar esse retorno para garantir equivalência e facilitar a validação.

A decisão arquitetural ainda pendente é se o histórico AntiLoop permanecerá no Python, sendo enviado como snapshot, ou se será mantido no C++ por meio de atualizações sincronizadas. Essa escolha deve preceder a implementação porque altera o contrato de integração e o risco de divergência entre os dois ambientes.