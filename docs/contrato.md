# Contrato de Entrada e Saída do Módulo Nativo — Action Masks e AntiLoop

## 1. Objetivo e responsabilidades

O módulo nativo será uma extensão C++ acessível pelo Python por meio do `pybind11`. Sua responsabilidade será calcular a validade das ações e aplicar as proteções AntiLoop de acordo com o estado recebido.

A arquitetura manterá as responsabilidades separadas:

- **Python:** ambiente, estado oficial da partida, gestores do jogo, execução das ações, recompensas, PPO e treinamento.
- **C++:** geração das máscaras, validação dos candidatos e consultas às regras AntiLoop.
- **pybind11:** conversão dos dados entre Python e C++.

O módulo nativo não executará compras, vendas, movimentações, trocas ou qualquer outra ação. Também não calculará logits, probabilidades, gradientes ou atualizações do PPO.

A implementação Python continuará sendo a referência de comportamento durante a validação.

## 2. Interface pública proposta

O módulo existente chama-se `combat_engine` e atende à simulação de combate. Para evitar misturar responsabilidades, a decisão de projeto é expor a nova funcionalidade por uma interface própria dentro da infraestrutura C++ existente.

Interface lógica proposta:

```python
import decision_engine

result = decision_engine.generate_action_masks(snapshot)
```

O nome `decision_engine` é uma proposta para a interface de decisão, não uma afirmação de que esse módulo já existe.

A chamada deve ser síncrona, determinística para uma mesma entrada e sem modificar o estado Python recebido.

A interface deve oferecer duas operações lógicas:

1. `generate_action_masks(snapshot)`: calcula todas as máscaras e os indicadores de disponibilidade.
2. `evaluate_move(snapshot, move)`: consulta a validade e, quando aplicável, o motivo de bloqueio de um movimento específico.

A segunda operação pode ser usada por testes de equivalência e diagnósticos. A geração de máscaras deve reutilizar a mesma lógica de validação, evitando regras duplicadas.

## 3. Contrato de entrada

A entrada será um snapshot explícito do estado relevante de um jogador. Não será passado o objeto inteiro `MiniTFTEnv`, nem referências a gestores Python.

### 3.1. Estado do jogador

| Campo | Tipo lógico | Significado |
|---|---|---|
| `is_alive` | `bool` | Indica se o jogador pode agir |
| `gold` | inteiro | Ouro disponível |
| `level` | inteiro | Nível atual, caso seja necessário para regras de compra de XP |
| `xp` | inteiro | XP atual, caso seja necessário para regras de compra de XP |

Campos adicionais só devem entrar no contrato se a auditoria das regras confirmar que são necessários para calcular a validade das ações.

O C++ não deve recalcular regras econômicas por conta própria quando a regra oficial já estiver encapsulada no `EconomyManager`. Os custos e critérios relevantes precisam ser fornecidos ou formalizados explicitamente no contrato.

### 3.2. Tabuleiro e banco

| Campo | Dimensão | Significado |
|---|---:|---|
| `board` | 28 posições | Estado ordenado das posições do tabuleiro |
| `bench` | 9 posições | Estado ordenado das posições do banco |

Cada posição será representada por uma unidade ou por um valor explícito de ausência de unidade.

Para uma unidade, o contrato de identidade deverá incluir:

- `uuid`, quando existente;
- `id`;
- `star`, com padrão atual igual a `1` quando ausente.

A identidade deverá respeitar a regra Python vigente: UUID tem precedência; sem UUID, a identidade é composta por `id` e `star`; objetos que não sejam dicionários produzem identidade `None` na implementação atual.

Os dados necessários para decidir se uma posição está ocupada e para identificar a unidade devem ser separados dos atributos de combate que não influenciam a validade do movimento.

### 3.3. Loja e economia

| Campo | Dimensão | Significado |
|---|---:|---|
| `shop` | 5 posições | Unidades oferecidas na loja |
| `shop[i].available` | booleano lógico | Indica se há uma oferta real no slot |
| `shop[i].cost` | inteiro | Custo da unidade oferecida |
| `gold` | inteiro | Saldo disponível para operações |

O C++ precisa distinguir uma oferta real de um slot vazio. O fallback técnico da máscara da loja nunca poderá ser interpretado como compra disponível.

A validade de `REROLL` e `BUY_XP` deverá seguir os critérios atuais de `EconomyManager`, incluindo eventuais regras além do saldo de ouro. Esses critérios devem ser definidos como parte do contrato funcional antes de sua implementação nativa.

### 3.4. Histórico AntiLoop

O snapshot deverá conter os dados necessários para reproduzir as consultas da implementação atual:

| Campo | Tipo lógico | Uso |
|---|---|---|
| `position_history` | sequência ordenada de assinaturas | Histórico recente de estados espaciais |
| `move_history` | sequência ordenada de movimentos | Reversões, oscilações e ciclos |
| `last_move` | movimento ou ausência | Detecção de reversão |
| `blocked_moves` | sequência de chaves de movimento | Bloqueios explícitos |
| `blocked_move_states` | mapa de chave para assinatura | Verificar se o bloqueio vale no estado atual |
| `state_visits` | mapa de assinatura para contagem | Contabilizar visitas a estados |
| `last_board_signature` | assinatura ou ausência | Estado usado nas consultas de bloqueio |
| `history_size` | inteiro | Limite de histórico |
| `blocked_move_size` | inteiro | Limite de bloqueios explícitos |
| `loop_threshold` | inteiro | Limiar de repetição de estado |

Um registro de movimento deverá preservar, no mínimo:

```text
move_type
source
target
unit_identity
```

A assinatura do estado deve manter a ordem das 28 posições do tabuleiro e das nove posições do banco. Não deve incluir ouro, XP, loja ou HP se o objetivo for reproduzir a assinatura espacial atual.

As janelas e os limites devem reproduzir a implementação Python, inclusive as janelas específicas usadas por cada proteção.

### 3.5. Parâmetros da chamada

O contrato deve identificar a versão funcional das regras, por exemplo, por uma constante de versão de contrato. Isso permitirá detectar incompatibilidades quando os formatos ou as regras forem alterados.

A versão do contrato não substitui a comparação de comportamento entre Python e C++.

## 4. Contrato de saída

A operação `generate_action_masks(snapshot)` deverá retornar as oito máscaras atuais e os indicadores auxiliares.

### 4.1. Máscaras obrigatórias

| Campo | Dimensão | Significado |
|---|---:|---|
| `type_mask` | `(7,)` | Tipos de ação disponíveis |
| `shop_mask` | `(5,)` | Slots selecionáveis da loja |
| `bench_source_mask` | `(9,)` | Slots selecionáveis para venda |
| `board_target_mask` | `(28,)` | Máscara geral auxiliar de destinos do tabuleiro |
| `board_source_mask` | `(28,)` | Origens válidas para movimentos no tabuleiro |
| `board_move_target_masks` | `(28, 28)` | Destinos condicionados à origem do tabuleiro |
| `bench_move_source_mask` | `(9,)` | Origens válidas no banco para movimentação |
| `bench_to_board_target_masks` | `(9, 28)` | Destinos condicionados à origem no banco |

As dimensões são parte obrigatória do contrato e devem ser preservadas para compatibilidade com `trainer.py` e `policy.py`.

### 4.2. Índices de `type_mask`

| Índice | Ação |
|---:|---|
| 0 | `BUY` |
| 1 | `REROLL` |
| 2 | `BUY_XP` |
| 3 | `MOVE_BENCH` |
| 4 | `MOVE_BOARD` |
| 5 | `SELL` |
| 6 | `PASS` |

### 4.3. Indicadores auxiliares

A saída também deverá conter indicadores booleanos explícitos:

- `buy_available`: existe uma compra real disponível.
- `sell_available`: existe uma unidade real que pode ser vendida.
- `has_board_move`: existe um movimento real válido no tabuleiro.
- `has_bench_move`: existe uma movimentação real válida do banco para o tabuleiro.

Esses indicadores não podem ser inferidos apenas pela presença de valores habilitados nas máscaras, pois algumas máscaras utilizam um fallback técnico para evitar distribuições categóricas vazias.

### 4.4. Diagnóstico de movimentos

A operação `evaluate_move(snapshot, move)` deverá retornar:

- `valid`: se o candidato é permitido pelas regras consultadas;
- `block_reason`: motivo correspondente à regra atual, ou ausência de motivo;
- `move_type`: tipo de movimento avaliado.

Os motivos devem ser valores estáveis, documentados e comparáveis entre Python e C++. A ordem de precedência atual deve ser mantida.

A saída de diagnóstico não deverá alterar o histórico ou as métricas de execução.

## 5. Representação dos dados e regras de validação

1. As dimensões do tabuleiro, banco e loja são fixas no contrato inicial: 28, nove e cinco posições.
2. As posições devem usar índices inteiros zero-based.
3. Posições vazias devem possuir representação explícita e não ser confundidas com uma unidade de identidade nula.
4. A identidade da unidade deve ser normalizada de maneira idêntica nos dois lados.
5. Os tipos de movimento devem ser representados por valores documentados e estáveis. Os aliases reconhecidos por regras específicas do Python não devem ser normalizados globalmente sem comprovação de equivalência.
6. A entrada deve ser validada antes do cálculo. Dimensões incompatíveis, tipos desconhecidos e índices inválidos devem produzir um erro definido, e não acesso fora dos limites.
7. A implementação não deve modificar o snapshot recebido.
8. Os fallbacks atuais devem ser preservados exatamente, sem confundi-los com disponibilidade real de ação.

As regras de economia que dependem de gestores Python precisam ser formalizadas antes da migração definitiva. Não se deve presumir que `gold`, isoladamente, reproduz todas as condições de `can_spend()` ou `can_buy_xp()`.

## 6. Semântica de erros

O contrato deverá distinguir:

- **Entrada inválida:** dimensões ou tipos incompatíveis; a chamada deve falhar de forma explícita.
- **Candidato inválido:** movimento que não satisfaz as regras; retorna resultado inválido, sem tratar isso como falha interna.
- **Bloqueio AntiLoop:** candidato rejeitado por uma proteção específica; retorna o motivo correspondente.
- **Falha interna do módulo:** erro de implementação ou condição inesperada; deve ser comunicada ao Python.

Uma falha interna não pode ser convertida silenciosamente em máscaras permissivas. Durante a fase de validação, a integração deverá registrar o erro e recorrer à implementação Python de referência conforme a política de fallback definida.

O comportamento atual de tolerância a exceções na geração de máscaras Python deve ser tratado como uma regra específica de compatibilidade, e não reproduzido por acidente. O comportamento de produção e o comportamento de diagnóstico podem precisar de políticas distintas, desde que isso seja explícito.

## 7. Propriedade do estado e sincronização

O contrato inicial recomenda que **Python seja o proprietário do estado oficial e do histórico AntiLoop**.

Em cada chamada:

1. Python cria um snapshot consistente.
2. O módulo nativo recebe o snapshot.
3. C++ calcula as máscaras ou consulta um candidato.
4. C++ devolve o resultado.
5. Python usa as máscaras na política PPO.
6. Python executa a ação selecionada.
7. Após o resultado real da execução, Python atualiza o estado e o histórico oficial.

Essa abordagem evita manter dois históricos mutáveis independentes durante a primeira etapa de migração.

As consultas de geração de máscaras e de motivos de bloqueio são operações de leitura. Elas não podem registrar movimentos, alterar `last_move`, incrementar contadores de execução ou modificar os bloqueios.

A decisão de manter futuramente um AntiLoop persistente dentro do C++ deverá ser tratada como uma evolução separada do contrato, depois de comprovada a equivalência do modelo baseado em snapshots.

## 8. Compatibilidade com Python, PPO e `pybind11`

O contrato nativo deve ser independente da arquitetura neural.

O módulo não deve receber:

- pesos da `TFTPolicy`;
- logits ou probabilidades;
- ações amostradas pelo PPO;
- gradientes;
- buffer de rollout;
- recompensas;
- observações completas que não sejam necessárias à validade das ações.

O módulo deve devolver dados que Python consiga converter diretamente para os formatos utilizados pelo treinador. A integração precisa preservar as dimensões das máscaras e o mapeamento dos índices esperados por `policy.py`.

A API C++ interna pode utilizar structs tipadas e vetores. A camada `pybind11` deve expor os campos de maneira previsível e validar as conversões. Não é necessário reutilizar `CombatInput` ou `CombatResult`: esses tipos representam o domínio de combate e não o estado de decisão/AntiLoop.

## 9. Critérios de aceitação do contrato

O contrato estará definido quando:

- A entrada de cada operação estiver documentada campo a campo.
- As oito máscaras, seus formatos e seus índices estiverem especificados.
- Os indicadores de disponibilidade real estiverem separados dos fallbacks.
- A identidade das unidades e os formatos do histórico estiverem definidos.
- Os motivos de bloqueio e sua precedência estiverem especificados.
- A política de erros e fallback estiver documentada.
- Estiver explícito que consultas não mutam o histórico.
- Estiver explícito que Python continua responsável pela execução e pelas atualizações de estado.
- A interface não depender de estruturas exclusivas do PPO nem reutilizar indevidamente estruturas de combate.
- O contrato permitir testes determinísticos de equivalência com a implementação Python.

## 10. Decisões ainda necessárias antes da implementação

Há três pontos que exigem confirmação a partir das regras existentes e dos testes:

1. **Economia:** quais valores precisam ser enviados para reproduzir exatamente `can_spend()` e `can_buy_xp()`?
2. **Histórico:** o snapshot completo será enviado em cada chamada ou haverá, numa etapa futura, estado persistente no C++?
3. **Falhas da implementação nativa:** qual será a política exata de fallback em treinamento e em testes de equivalência?

Essas questões não impedem a definição do contrato básico, mas devem ser resolvidas antes de considerar a interface pronta para produção.

## Conclusão

O contrato proposto mantém o Python como fonte oficial do estado e da execução, enquanto o C++ atua como um calculador determinístico de validade de ações. A saída permanece compatível com as oito máscaras existentes e inclui indicadores explícitos para evitar que fallbacks técnicos sejam interpretados como ações válidas.

A equivalência será medida contra a implementação Python atual, preservando identidade, histórico, precedência de bloqueios, limites e semântica de erro.