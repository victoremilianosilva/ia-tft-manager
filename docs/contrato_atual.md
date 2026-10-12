# Contrato Atual das Action Masks — Formatos, Dimensões e Índices

## 1. Visão geral

O sistema utiliza oito máscaras nomeadas para restringir as ações disponíveis para cada jogador. Elas são geradas pelos componentes de decisão do ambiente, organizadas por `TFTLobby` e consolidadas pelo `trainer.py` antes de serem consumidas pela política PPO.

O contrato atual usa estas dimensões por jogador:

| Máscara | Formato | Significado |
|---|---:|---|
| `type_mask` | `(7,)` | Tipos de ação permitidos |
| `shop_mask` | `(5,)` | Posições da loja permitidas para compra |
| `bench_source_mask` | `(9,)` | Posições do banco permitidas para venda |
| `board_target_mask` | `(28,)` | Máscara geral de destino do tabuleiro |
| `board_source_mask` | `(28,)` | Posições de origem válidas no tabuleiro |
| `board_move_target_masks` | `(28, 28)` | Destinos válidos condicionados à origem no tabuleiro |
| `bench_move_source_mask` | `(9,)` | Posições de origem válidas no banco para mover ao tabuleiro |
| `bench_to_board_target_masks` | `(9, 28)` | Destinos válidos condicionados à origem no banco |

Essas dimensões correspondem ao contrato definido em `trainer.py`, na constante `MASK_SHAPES`.

## 2. Convenção de valores

Na geração individual do `ActionMaskManager`, as máscaras são normalmente vetores e matrizes `numpy` com tipo `float32`:

- `1.0`: categoria habilitada.
- `0.0`: categoria desabilitada.

Na montagem do dicionário de `TFTLobby.get_action_masks()`, as máscaras são convertidas para `numpy.bool_`:

- `True`: categoria habilitada.
- `False`: categoria desabilitada.

No treinador, `_flatten_masks()` consolida as máscaras e as converte para tensores booleanos, preservando os formatos definidos.

A política utiliza esses valores para restringir os logits antes de criar as distribuições categóricas.

## 3. Significado dos índices

### 3.1. `type_mask` — 7 categorias

| Índice | Tipo de ação |
|---:|---|
| `0` | `BUY` |
| `1` | `REROLL` |
| `2` | `BUY_XP` |
| `3` | `MOVE_BENCH` |
| `4` | `MOVE_BOARD` |
| `5` | `SELL` |
| `6` | `PASS` |

A máscara define quais tipos de ação podem ser selecionados. Os tipos de movimento só devem ser habilitados quando existir pelo menos uma combinação real de origem e destino válida.

### 3.2. `shop_mask` — 5 categorias

Cada índice representa uma posição da loja:

- `0` a `4`: slots da loja.

O índice identifica a posição, não o identificador do campeão que está nela. A validade depende da disponibilidade do slot e das regras de compra.

### 3.3. `bench_source_mask` — 9 categorias

Cada índice representa uma posição do banco:

- `0` a `8`: slots do banco.

Essa máscara é utilizada para a decisão `SELL`. Não deve ser confundida com `bench_move_source_mask`, que controla as origens permitidas para movimentar uma unidade ao tabuleiro.

### 3.4. `board_target_mask` — 28 categorias

Cada índice representa uma posição do tabuleiro:

- `0` a `27`: posições lineares do tabuleiro de 4 × 7.

Na chamada atual de `TFTLobby.get_action_masks()`, a geração dessa máscara geral é desativada e o índice `0` é habilitado como fallback técnico. A política atual utiliza as matrizes condicionais para os movimentos, portanto essa máscara geral não substitui as máscaras específicas por origem.

### 3.5. `board_source_mask` — 28 categorias

Cada índice representa uma posição candidata a origem de um movimento no tabuleiro.

- `0` a `27`: posições do tabuleiro.
- Uma posição é habilitada quando a unidade nela possui pelo menos um destino válido segundo a geração das máscaras.

A validade da origem não significa que todos os destinos sejam válidos. A máscara de destino deve ser consultada depois da seleção da origem.

### 3.6. `board_move_target_masks` — matriz de 28 × 28

Essa matriz relaciona origem e destino:

`board_move_target_masks[origem, destino]`

- Primeiro índice: origem, de `0` a `27`.
- Segundo índice: destino, de `0` a `27`.
- Valor habilitado: movimento ou troca permitido para aquele par segundo a validação das máscaras.

A diagonal, na qual origem e destino são iguais, não representa um movimento válido. Destinos inválidos são desabilitados, embora linhas sem destinos reais possam receber o fallback técnico no índice `0`.

A matriz permite que a política selecione a linha correspondente à origem escolhida, sem precisar reconstruir as regras de validade durante a amostragem.

### 3.7. `bench_move_source_mask` — 9 categorias

Cada índice representa uma posição do banco que pode servir de origem para mover uma unidade ao tabuleiro:

- `0` a `8`: slots do banco.

A máscara considera a existência de uma unidade e de pelo menos um destino válido no tabuleiro, incluindo as proteções AntiLoop.

Ela é diferente de `bench_source_mask`, que é destinada à venda.

### 3.8. `bench_to_board_target_masks` — matriz de 9 × 28

Essa matriz relaciona a origem no banco ao destino no tabuleiro:

`bench_to_board_target_masks[slot_banco, destino_tabuleiro]`

- Primeiro índice: slot de origem no banco, de `0` a `8`.
- Segundo índice: destino no tabuleiro, de `0` a `27`.
- Valor habilitado: destino permitido para aquela origem segundo a geração das máscaras.

Na implementação atual, a geração considera as posições vazias do tabuleiro e as proteções AntiLoop. Linhas sem destinos reais podem receber o fallback no índice `0`.

## 4. Contrato do vetor de ação

O método `env.py::_sanitize_action()` interpreta a ação como um vetor de seis posições:

| Índice do vetor | Campo | Significado |
|---:|---|---|
| `0` | `type` | Tipo de ação |
| `1` | `shop_slot` | Slot da loja |
| `2` | `bench_slot` | Slot do banco |
| `3` | `board_target` | Destino usado pelo movimento do banco para o tabuleiro |
| `4` | `board_source` | Origem de um movimento no tabuleiro |
| `5` | `conditioned_board_target` | Destino condicionado à origem no tabuleiro |

A mesma posição do vetor pode ser irrelevante para determinados tipos de ação. Por exemplo, `shop_slot` é utilizado por `BUY`, enquanto `board_source` e `conditioned_board_target` são utilizados por `MOVE_BOARD`.

As dimensões das cabeças da política seguem a ordem:

`[7, 5, 9, 28, 28, 28]`

Essa ordem corresponde aos campos de ação acima, não à ordem das oito máscaras nomeadas. Algumas máscaras controlam dimensões que são usadas somente em ramos específicos da política.

## 5. Como as máscaras se relacionam com a política

A política utiliza as máscaras na seguinte ordem lógica:

1. `type_mask` restringe a escolha do tipo.
2. Para `BUY`, `shop_mask` restringe o slot da loja.
3. Para `SELL`, `bench_source_mask` restringe o slot do banco.
4. Para `MOVE_BENCH`, `bench_move_source_mask` restringe a origem; depois, `bench_to_board_target_masks` fornece a linha correspondente à origem selecionada.
5. Para `MOVE_BOARD`, `board_source_mask` restringe a origem; depois, `board_move_target_masks` fornece a linha correspondente à origem selecionada.

`REROLL`, `BUY_XP` e `PASS` não possuem uma decisão categórica adicional no fluxo atual de `get_action_and_value()`.

A máscara geral `board_target_mask` permanece no contrato para compatibilidade e outros usos, mas não substitui o condicionamento por origem das matrizes atuais.

## 6. Formatos depois de consolidar os agentes

Se `N` for o número total de agentes consolidados pelo treinador, os formatos passam a ser:

| Máscara | Formato por batch |
|---|---:|
| `type_mask` | `(N, 7)` |
| `shop_mask` | `(N, 5)` |
| `bench_source_mask` | `(N, 9)` |
| `board_target_mask` | `(N, 28)` |
| `board_source_mask` | `(N, 28)` |
| `board_move_target_masks` | `(N, 28, 28)` |
| `bench_move_source_mask` | `(N, 9)` |
| `bench_to_board_target_masks` | `(N, 9, 28)` |

Com quatro lobbies de oito jogadores, `N = 32`.

O primeiro índice de cada tensor identifica o agente dentro do batch. Nas matrizes condicionais, o segundo índice identifica a origem e o terceiro identifica o destino.

## 7. Fallbacks e jogadores eliminados

### Fallbacks

O índice `0` pode ser habilitado tecnicamente quando uma máscara ou linha condicional não contém opções reais. Isso impede que uma distribuição categórica receba uma máscara inteiramente vazia.

Esse valor, isoladamente, não prova que o movimento seja válido. A disponibilidade real é determinada durante a geração das máscaras e utilizada para habilitar ou desabilitar os tipos de movimento.

### Jogadores eliminados

`TFTLobby._dead_player_mask()` retorna máscaras especiais:

- Somente `PASS` é permitido em `type_mask`.
- As demais dimensões habilitam o índice `0` como categoria dummy.
- As matrizes condicionais também habilitam uma combinação dummy no índice zero.

Isso mantém as distribuições utilizáveis sem permitir que um jogador eliminado selecione outro tipo de ação.

## 8. Contrato a preservar em uma implementação equivalente

Uma implementação alternativa deve manter:

1. As oito chaves nomeadas e suas dimensões.
2. A ordem e o significado dos seis campos do vetor de ação.
3. A distinção entre slots do banco usados para venda e para movimentação.
4. A interpretação das linhas das matrizes condicionais como origens.
5. A interpretação das colunas como destinos.
6. A conversão entre máscaras numéricas, booleanas e tensores.
7. A semântica dos fallbacks e das máscaras de jogadores eliminados.
8. A correspondência entre as máscaras geradas, as ações amostradas e as máscaras armazenadas para a avaliação PPO.

## 9. Conclusão

O contrato atual utiliza oito máscaras, mas a política não escolhe diretamente entre oito componentes de ação. Ela escolhe entre seis dimensões, enquanto as máscaras condicionais fornecem as restrições necessárias para cada ramo autoregressivo.

O formato, a ordem dos índices e a diferença entre máscaras gerais e condicionais são essenciais para manter compatibilidade entre o ambiente, a política e o treinador.