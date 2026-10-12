# Análise de Identidade das Unidades e Equivalência de Movimentos

## 1. Objetivo

O `AntiLoopManager` precisa determinar se uma unidade já realizou determinado movimento, se uma ação é a reversão de outra e se duas configurações representam o mesmo estado de posicionamento.

Essas comparações não utilizam todas os mesmos critérios. A identidade da unidade é combinada com o tipo do movimento, as posições de origem e destino, o histórico recente e, em certos casos, a assinatura completa do tabuleiro e do banco.

## 2. Identidade das unidades

### 2.1. Método `_unit_identity(unit)`

O método é estático e define a identidade usada nos registros e nas comparações.

A regra atual é:

| Condição | Identidade produzida |
|---|---|
| A unidade não é um dicionário | `None` |
| Existe um campo `uuid` diferente de `None` | `("uuid", uuid)` |
| Não existe UUID válido segundo essa condição | `("unit", id, star)` |

Na identidade alternativa, `star` assume o valor padrão `1` quando o campo está ausente.

### 2.2. Consequências

**Unidades com UUID:** são diferenciadas pelo UUID. Campos como `id` e `star` não participam da identidade quando existe UUID.

**Unidades sem UUID:** são identificadas pela combinação de `id` e `star`. Duas unidades com o mesmo identificador e a mesma estrela serão consideradas equivalentes, mesmo que sejam instâncias diferentes.

**Unidades que não são dicionários:** recebem identidade `None`. Isso significa que não possuem uma identidade individual rastreável por esse método. Como consequência, comparações baseadas em igualdade de identidade podem tratar essas unidades como equivalentes entre si.

O método não valida se o UUID é único, se o `id` existe ou se a estrela é válida. Ele utiliza os valores disponíveis.

## 3. Onde a identidade é utilizada

A identidade produzida por `_unit_identity()` aparece em quatro estruturas principais:

1. **Histórico de movimentos:** `register_move()` armazena a identidade junto ao tipo, à origem e ao destino.
2. **Chave de bloqueio explícito:** `make_move_key()` inclui a identidade na chave.
3. **Assinatura do estado:** `make_board_signature()` registra a identidade de cada unidade em sua posição.
4. **Detecção de reversões, oscilações e ciclos:** as regras filtram ou comparam movimentos com base na identidade, exceto nas situações especiais descritas adiante.

Essa reutilização mantém um critério de identidade comum entre diferentes proteções, mas também faz com que qualquer limitação de `_unit_identity()` afete várias regras simultaneamente.

## 4. Equivalência de movimentos

### 4.1. Chave de movimento

O método `make_move_key()` cria a chave:

`(move_type, source, target, unit_identity)`

Dois movimentos possuem a mesma chave quando os quatro componentes são iguais.

A chave é utilizada por `block_move()` e `is_move_blocked()` para registrar e consultar bloqueios explícitos.

Nessa comparação:

- O tipo precisa ser igual.
- A origem precisa ser igual.
- O destino precisa ser igual.
- A identidade da unidade precisa ser igual.

A chave não normaliza automaticamente aliases de tipos nem inverte a ordem das posições. Portanto, movimentos equivalentes segundo outras regras podem ter chaves diferentes.

### 4.2. Movimento reverso

O método `is_reverse_move()` utiliza critérios diferentes para movimentos normais e trocas.

**Para movimentos normais**, considera a ação uma reversão quando:

- A identidade da unidade é igual à do último movimento.
- O tipo é igual ao tipo anterior.
- A origem atual corresponde ao destino anterior.
- O destino atual corresponde à origem anterior.

**Para `board_swap`**, quando o último movimento também é `board_swap`, a regra ignora a identidade e compara o conjunto das duas posições.

Assim, trocar as posições 3 e 10 é equivalente à troca entre 10 e 3, independentemente de qual unidade está em cada extremidade.

Essa exceção é intencional: uma troca altera a unidade que ocupa cada posição, mas continua representando a mesma operação inversa sobre o par de posições.

## 5. Equivalência durante a detecção de oscilações

O método `is_oscillating()` seleciona os movimentos recentes associados à identidade da unidade candidata.

A janela examinada contém até seis registros recentes de `move_history`.

Para `board_move`, somente movimentos desse tipo entram na cadeia relevante. Para `board_swap`, entram tanto `board_swap` quanto `board_move` associados à mesma identidade.

A equivalência depende de:

1. Identidade igual.
2. Tipo de movimento incluído no filtro aplicável.
3. Continuidade entre as posições dos movimentos.
4. Último destino registrado igual à origem atual do candidato.
5. Repetição do destino candidato pelo menos duas vezes na cadeia reconstruída, desconsiderando a posição final.

Essa regra não compara apenas a chave exata do movimento. Ela procura um padrão de posicionamento repetido na trajetória da unidade.

## 6. Equivalência em ciclos entre banco e tabuleiro

O método `is_bench_board_loop()` utiliza identidade, tipos normalizados e posições.

Ele reconhece estes aliases:

| Tipo recebido | Tipo normalizado |
|---|---|
| `MOVE_BENCH_TO_BOARD` | `bench_to_board` |
| `bench_to_board` | `bench_to_board` |
| `MOVE_BOARD_TO_BENCH` | `board_to_bench` |
| `board_to_bench` | `board_to_bench` |

A regra filtra o histórico para a identidade da unidade candidata. Os dois últimos movimentos relevantes precisam representar transições de tipos diferentes, entre as mesmas posições, em sentidos opostos.

Depois disso, o candidato é comparado com a transição anterior em termos de tipo normalizado, origem e destino.

Portanto, nesse caso, a equivalência não depende apenas da identidade: também depende da sequência de ida e volta e da correspondência exata das posições.

## 7. Equivalência em ciclos gerais

O método `is_cycle_move()` considera apenas `board_move` e `board_swap`.

Ele filtra os movimentos por identidade e tipo, selecionando até os oito registros relevantes mais recentes. Em seguida, procura uma sequência contínua de posições e verifica se o histórico já fechou o ciclo associado ao destino candidato.

O critério é diferente da chave exata de movimento:

- A identidade precisa corresponder.
- Os tipos registrados precisam estar entre os tipos aceitos.
- A sequência precisa ser contínua.
- O ciclo precisa ter sido fechado anteriormente.
- O estado final da sequência precisa corresponder à origem atual do candidato.

O primeiro fechamento do ciclo é permitido. A repetição posterior pode ser bloqueada quando satisfaz essas condições.

## 8. Equivalência de estados

O método `make_board_signature(board, bench)` representa o posicionamento completo das unidades no tabuleiro e no banco.

Cada posição é representada por seu índice e pela identidade da unidade, ou por `None` quando está vazia. A assinatura final contém duas tuplas: uma para o tabuleiro e outra para o banco.

Dois estados têm assinaturas iguais quando:

- As listas de posições possuem a mesma estrutura e ordem.
- Cada posição está vazia nos dois estados ou contém a mesma identidade.
- A distribuição das unidades entre tabuleiro e banco é igual.

A assinatura não considera ouro, XP, loja, vida ou outros atributos.

Consequentemente, dois estados com recursos diferentes podem ser considerados iguais para as proteções que dependem dessa assinatura, desde que a disposição das unidades seja a mesma.

## 9. Equivalências que não devem ser confundidas

| Comparação | Critério principal |
|---|---|
| Chave de movimento | Tipo, origem, destino e identidade |
| Reversão normal | Mesmo tipo e unidade, com origem e destino invertidos |
| Reversão de troca | Mesmo par de posições, independentemente da ordem |
| Oscilação | Identidade e cadeia recente de posições |
| Ciclo banco ↔ tabuleiro | Identidade, tipos normalizados e ida e volta pelas mesmas posições |
| Ciclo geral | Identidade e sequência contínua de movimentos de tabuleiro |
| Assinatura de estado | Identidade de cada unidade em cada posição do tabuleiro e banco |

Um mesmo par de movimentos pode ser diferente segundo a chave exata e, ainda assim, ser equivalente segundo a regra de reversão ou de ciclo.

## 10. Limitações e pontos de atenção

### 10.1. Unidades sem UUID

A combinação `id + star` não distingue cópias da mesma unidade. Se for necessário acompanhar instâncias individualmente, a identidade alternativa pode ser insuficiente.

### 10.2. Unidades não representadas por dicionários

Retornar `None` como identidade reduz a capacidade de distinguir essas unidades. As regras que exigem uma identidade válida, como `is_oscillating()` e `is_bench_board_loop()`, não detectam seus padrões normalmente.

### 10.3. Tipos de movimento

A chave de movimento e as regras de reversão normal dependem do tipo exato. Os aliases são normalizados explicitamente em `is_bench_board_loop()`, mas não há uma normalização geral aplicada a todas as proteções.

### 10.4. Trocas de posições

A equivalência especial de `board_swap` compara o par de posições sem depender da identidade. Esse comportamento é mais amplo do que a comparação normal e precisa ser preservado se a intenção for manter a mesma semântica de bloqueio.

### 10.5. Assinatura de estado

A assinatura registra somente o posicionamento e a identidade das unidades. Ela não distingue estados com o mesmo tabuleiro e banco, mas com recursos ou atributos diferentes.

### 10.6. Dependência do histórico

As regras de reversão, oscilação e ciclo dependem dos movimentos efetivamente registrados. Um histórico incompleto ou identidades inconsistentes podem alterar a equivalência detectada.

## 11. Critérios a preservar em uma implementação equivalente

Uma implementação alternativa deve manter:

1. A precedência do UUID sobre `id + star`.
2. O tratamento atual de unidades sem UUID e de objetos que não são dicionários.
3. A estrutura exata da chave de movimento.
4. A comparação de movimentos normais por identidade, tipo e posições invertidas.
5. A comparação especial de trocas pelo par de posições.
6. Os filtros de tipo e identidade de cada regra.
7. Os aliases explicitamente reconhecidos na detecção banco ↔ tabuleiro.
8. A estrutura da assinatura, incluindo posições vazias e separação entre tabuleiro e banco.
9. As janelas de histórico e os requisitos de continuidade das sequências.
10. A diferença entre equivalência de movimento e equivalência de estado.

## 12. Conclusão

A identidade das unidades é central para o anti-loop, mas não é o único fator de equivalência. O código combina identidade, tipo, origem, destino, sequência histórica e assinatura de posicionamento conforme a proteção consultada.

A exceção mais importante é `board_swap`, cuja reversão é identificada pelo par de posições, sem depender da identidade da unidade. Já as demais regras utilizam a identidade para acompanhar movimentos e trajetórias, enquanto os bloqueios explícitos dependem de uma chave exata associada ao estado registrado.

Essa distinção deve ser mantida para evitar tanto falsos bloqueios quanto movimentos repetitivos que deixem de ser detectados.