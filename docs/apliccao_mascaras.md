# Análise da Geração e Aplicação das Máscaras Condicionais na Política Autoregressiva

## 1. Objetivo

A política `TFTPolicy` utiliza seis componentes de ação:

`[action_type, shop_slot, bench_slot, board_target, board_source, board_move_target]`

As dimensões são fixadas em:

`[7, 5, 9, 28, 28, 28]`

A política é autoregressiva porque a escolha de uma ação anterior condiciona as decisões seguintes. O tipo de ação define qual sequência será executada; nos movimentos, a origem escolhida determina quais destinos podem ser selecionados.

As máscaras restringem as opções permitidas em cada etapa, evitando que a distribuição categórica atribua probabilidade a ações proibidas.

## 2. Componentes responsáveis

- **`ai/ActionMaskManager.py`**: calcula a validade das ações e gera máscaras de origem, destino e tipo.
- **`lobby/TFTLobby.py`**: coordena a geração das máscaras dos jogadores e monta o dicionário consumido pelo treinador e pela política.
- **`trainer.py`**: obtém as máscaras das lobbies, organiza os dados em um batch e os envia à política.
- **`policy.py`**: aplica as máscaras aos logits e escolhe as ações de forma autoregressiva. Durante a avaliação do PPO, também valida se as ações armazenadas respeitam as máscaras.
- **`env.py`**: executa as ações e mantém o estado do jogo, que será usado na próxima geração de máscaras.

## 3. Ordem de geração das máscaras

### 3.1. Etapa 1 — Gerar máscaras condicionais de movimento

Em `TFTLobby.get_action_masks()`, cada jogador ativo tem seu `ActionMaskManager` consultado.

Primeiro, é chamada a geração conjunta das máscaras de movimentos no tabuleiro:

`get_board_move_masks()`

Ela retorna:

- `board_source_mask`: vetor de 28 posições, indicando quais origens possuem pelo menos um destino válido.
- `move_target_masks`: matriz de 28 × 28, em que cada linha corresponde a uma origem e cada coluna a um destino.
- `has_board_move`: indica se existe ao menos um movimento real válido.

Depois, é chamada a geração conjunta dos movimentos do banco para o tabuleiro:

`get_bench_move_masks()`

Ela retorna:

- `bench_move_source_mask`: vetor de 9 posições para as unidades do banco que podem ser movidas.
- `bench_to_board_target_masks`: matriz de 9 × 28, em que cada linha corresponde a uma posição do banco e cada coluna a uma posição do tabuleiro.
- `has_bench_move`: indica se existe ao menos um movimento real válido.

Essas matrizes são calculadas antes de a política escolher o tipo de ação. Isso permite preparar todas as opções condicionais em uma única consulta ao ambiente.

### 3.2. Etapa 2 — Gerar as máscaras gerais

O método `TFTLobby.get_action_masks()` chama `env.get_action_masks()` com os resultados anteriores.

Nessa chamada, as máscaras condicionais são desativadas para evitar que sejam calculadas novamente. A máscara de origem do tabuleiro já calculada é reutilizada, assim como os indicadores de disponibilidade dos movimentos.

O `ActionMaskManager.get_action_masks()` calcula, nessa ordem:

1. Máscara da loja e disponibilidade de compra.
2. Máscara do banco e disponibilidade de venda.
3. Máscara dos tipos de ação, usando os indicadores de disponibilidade.
4. Máscara geral de destino do tabuleiro, desativada nessa chamada específica.
5. Reutilização da máscara de origem do tabuleiro.
6. Máscara geral de destino condicionado, também desativada nessa chamada específica.

As máscaras desativadas recebem um fallback técnico no índice zero. Elas não substituem as matrizes condicionais calculadas anteriormente.

### 3.3. Etapa 3 — Montar o dicionário final

Para cada jogador ativo, `TFTLobby.get_action_masks()` monta o seguinte contrato:

| Chave | Formato por jogador | Função |
|---|---:|---|
| `type_mask` | `(7,)` | Restringe os tipos de ação |
| `shop_mask` | `(5,)` | Restringe as posições da loja |
| `bench_source_mask` | `(9,)` | Restringe as unidades que podem ser vendidas |
| `board_target_mask` | `(28,)` | Máscara geral de destino, com fallback nesta chamada |
| `board_source_mask` | `(28,)` | Restringe as origens válidas do tabuleiro |
| `board_move_target_masks` | `(28, 28)` | Destinos condicionados à origem no tabuleiro |
| `bench_move_source_mask` | `(9,)` | Restringe as origens válidas do banco |
| `bench_to_board_target_masks` | `(9, 28)` | Destinos condicionados à origem no banco |

Jogadores eliminados recebem máscaras especiais: somente `PASS` é permitido como tipo de ação, e as demais dimensões mantêm uma categoria dummy válida no índice zero.

## 4. Transporte das máscaras até a política

No `trainer.py`, o fluxo é:

1. Chamar `vec_env.env_method("get_action_masks")`.
2. Receber as máscaras agrupadas por lobby e jogador.
3. Chamar `_flatten_masks()` para consolidar os jogadores em um único batch.
4. Converter as máscaras para tensores booleanos.
5. Enviar o dicionário à `TFTPolicy.get_action()`.

Com quatro lobbies e oito jogadores por lobby, por exemplo, as máscaras passam a representar 32 agentes.

A consolidação preserva as dimensões condicionais. Em particular, as máscaras do tabuleiro passam a ter formato `(agentes, 28, 28)`, e as do banco para o tabuleiro, `(agentes, 9, 28)`.

## 5. Ordem de aplicação na política autoregressiva

O método `TFTPolicy.get_action_and_value()` começa codificando a observação em `features`. Em seguida, executa as etapas abaixo.

### 5.1. Etapa 1 — Escolher o tipo de ação

A política calcula os logits com `type_head(features)` e aplica `type_mask` usando `_mask_logits()`.

Depois, seleciona o tipo de ação permitido, por amostragem ou por `argmax` quando o modo determinístico está ativo.

A escolha do tipo determina qual ramo será executado:

| Índice | Tipo de ação | Decisões subsequentes |
|---:|---|---|
| 0 | BUY | Posição da loja |
| 1 | REROLL | Nenhuma dimensão adicional |
| 2 | BUY_XP | Nenhuma dimensão adicional |
| 3 | MOVE_BENCH | Origem no banco e destino no tabuleiro |
| 4 | MOVE_BOARD | Origem e destino no tabuleiro |
| 5 | SELL | Posição do banco |
| 6 | PASS | Nenhuma dimensão adicional |

A política transforma o tipo selecionado em um vetor one-hot e o concatena às features. Esse contexto é utilizado pelas cabeças de decisão seguintes.

### 5.2. Etapa 2 — BUY

Quando `action_type == 0`:

1. `shop_head` gera os logits das cinco posições da loja.
2. `shop_mask` remove as opções inválidas.
3. A política escolhe `shop_slot`.
4. A log-probabilidade e a entropia dessa decisão são adicionadas aos totais.

Não há uma segunda decisão condicional dentro do ramo BUY.

### 5.3. Etapa 3 — MOVE_BENCH

Quando `action_type == 3`, a ordem é:

1. **Escolher a origem:** `bench_head` produz os logits das nove posições do banco.
2. **Aplicar a máscara de origem:** utiliza `bench_move_source_mask`. Se essa chave não existir, a política usa `bench_source_mask` como compatibilidade com máscaras antigas.
3. **Selecionar a origem:** a política escolhe `bench_slot`.
4. **Obter a máscara de destino correspondente:** usa `bench_to_board_target_masks[agente, bench_slot, :]`.
5. **Aplicar a máscara de destino:** `bench_to_board_head` produz os logits das 28 posições e `_mask_logits()` remove os destinos inválidos.
6. **Selecionar o destino:** a política escolhe `board_target`.
7. **Acumular log-probabilidade e entropia** das duas decisões.

O ponto fundamental é que a máscara do destino não é aplicada antes de se conhecer a origem escolhida pela política. A matriz inteira já foi calculada pelo ambiente, mas a política seleciona somente a linha correspondente ao slot escolhido.

Se `bench_to_board_target_masks` não existir, `get_action_and_value()` usa `board_target_mask` como fallback de compatibilidade. Esse fallback não oferece o mesmo nível de condicionamento por origem.

### 5.4. Etapa 4 — MOVE_BOARD

Quando `action_type == 4`, a ordem é:

1. `board_source_head` gera os logits das 28 posições de origem.
2. `board_source_mask` restringe as origens permitidas.
3. A política escolhe `board_source`.
4. A origem selecionada é convertida em one-hot.
5. Esse vetor é concatenado ao contexto da política.
6. `board_move_target_head` calcula os logits dos 28 destinos.
7. A política seleciona `board_move_target_masks[agente, board_source, :]`.
8. A máscara selecionada é aplicada aos logits do destino.
9. A política escolhe `board_move_target`.
10. A log-probabilidade e a entropia das decisões de origem e destino são adicionadas aos totais.

O destino depende tanto do contexto da ação quanto da origem selecionada. A máscara condicional garante que a política não escolha um destino que tenha sido considerado inválido para aquela origem na geração das máscaras.

### 5.5. Etapa 5 — SELL

Quando `action_type == 5`:

1. `bench_head` gera os logits das posições do banco.
2. `bench_source_mask` restringe as posições que podem ser vendidas.
3. A política escolhe `bench_slot`.
4. A decisão é adicionada aos totais de log-probabilidade e entropia.

Essa máscara é diferente de `bench_move_source_mask`: a primeira é usada para vender unidades; a segunda, para mover unidades do banco para o tabuleiro.

### 5.6. REROLL, BUY_XP e PASS

Esses tipos não geram outra escolha categórica dentro de `get_action_and_value()`. Seus índices auxiliares permanecem nos tensores inicializados com zero.

O tipo selecionado continua sendo a decisão probabilística relevante para esses ramos.

## 6. Como as máscaras são aplicadas aos logits

O método `_mask_logits(logits, mask)`:

1. Converte a máscara para o dispositivo do tensor.
2. Verifica se o formato é igual ao dos logits.
3. Se a máscara não for booleana, verifica se contém somente zero e um.
4. Rejeita linhas sem nenhuma opção permitida.
5. Rejeita logits com NaN ou infinito.
6. Substitui logits das opções proibidas pelo menor valor representável pelo tipo numérico.

Ao construir uma distribuição `Categorical` a partir desses logits, as opções proibidas deixam de ser selecionáveis em condições normais de execução.

Essa função não decide quais ações são válidas. Ela aplica a decisão de validade já calculada pelo ambiente.

## 7. Fallbacks e validade real

As matrizes condicionais utilizam o índice zero como fallback técnico quando uma linha não possui destinos válidos. As máscaras de origem também podem habilitar o índice zero quando nenhum movimento real existe.

Esses fallbacks evitam distribuições categóricas vazias, mas não significam que a ação correspondente seja realmente possível.

A distinção é mantida pelos indicadores `has_board_move` e `has_bench_move`, utilizados na geração da máscara de tipos para impedir que `MOVE_BOARD` ou `MOVE_BENCH` sejam habilitados apenas por causa do fallback.

Em outras palavras, há dois conceitos distintos:

- **Máscara tecnicamente utilizável:** possui pelo menos uma categoria para a distribuição.
- **Ação realmente disponível:** existe pelo menos uma combinação de origem e destino válida.

Essa separação é necessária para evitar que uma categoria dummy seja confundida com um movimento válido.

## 8. Reavaliação das ações durante o PPO

O método `TFTPolicy.evaluate_actions()` reproduz a sequência autoregressiva para calcular as log-probabilidades e entropias das ações já armazenadas no rollout.

Ele utiliza as ações registradas para selecionar os ramos e, no caso dos movimentos, a origem armazenada para recuperar a linha correta da máscara de destino.

Além de aplicar `_mask_logits()`, valida explicitamente várias escolhas com `_validate_selected_actions()`:

- Tipo de ação.
- Slot da loja.
- Origem do movimento do banco.
- Destino do movimento do banco.
- Origem do movimento do tabuleiro.
- Destino do movimento do tabuleiro.

A validação rejeita índices fora dos limites e ações proibidas pela máscara correspondente.

Essa reavaliação é importante para o PPO porque a log-probabilidade calculada durante o treinamento deve corresponder à ação registrada e às máscaras armazenadas com a transição, não a uma sequência de ações recém-amostrada.

## 9. Fluxo completo resumido

A ordem do sistema pode ser representada assim:

1. O ambiente consulta o estado atual do jogador.
2. `ActionMaskManager` gera as máscaras de origem e destino condicionais.
3. O ambiente gera as máscaras gerais e determina os tipos realmente disponíveis.
4. `TFTLobby` monta o dicionário nomeado de máscaras.
5. `trainer.py` consolida as máscaras dos jogadores no batch.
6. `TFTPolicy` aplica `type_mask` e escolhe o tipo.
7. Se necessário, aplica a máscara da primeira decisão, escolhe a origem e recupera a máscara de destino correspondente.
8. A política aplica a máscara condicional do destino e escolhe a ação completa.
9. O treinador armazena ação, log-probabilidade, observação e máscaras no rollout.
10. Durante a atualização do PPO, `evaluate_actions()` reavalia as ações registradas usando as máscaras armazenadas.

## 10. Pontos críticos para manter a equivalência

Uma implementação alternativa precisa preservar:

1. A ordem de decisão: tipo → origem, quando aplicável → destino condicionado.
2. As dimensões e os formatos de cada máscara.
3. A diferença entre `bench_source_mask` e `bench_move_source_mask`.
4. A seleção da linha condicional pelo slot de banco ou pela origem do tabuleiro escolhida.
5. A correspondência entre as máscaras geradas, as ações escolhidas e as máscaras guardadas no rollout.
6. O tratamento de jogadores eliminados.
7. A distinção entre fallback técnico e movimento real disponível.
8. A validação de ações durante a avaliação do PPO.
9. A compatibilidade dos fallbacks antigos de `get_action_and_value()` e `evaluate_actions()`, sem presumir que eles sejam semanticamente idênticos às máscaras condicionais atuais.

## 11. Conclusão

A geração das máscaras ocorre antes da escolha da ação, mas a aplicação das máscaras condicionais acontece durante a decisão autoregressiva, depois que a política escolhe a origem relevante.

O ambiente calcula quais combinações são permitidas; a política usa essas informações para restringir as distribuições de probabilidade em cada etapa. O PPO, por sua vez, precisa reavaliar as mesmas decisões com as máscaras associadas à transição original.

A ordem de seleção, o formato das matrizes, os fallbacks e a correspondência entre origem e destino são partes essenciais do contrato atual.