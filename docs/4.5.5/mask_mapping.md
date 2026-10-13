# Auditoria de Máscaras de Ações — TFT AI

## 1. Objetivo

Mapear todas as funções de geração e validação de máscaras em `ai/ActionMaskManager.py`, identificar seus consumidores e definir o contrato que deverá ser preservado durante a migração para C++.

**Escopo desta etapa:** auditoria e documentação. Não inclui implementação, alteração de arquivos ou commits.

## 2. Arquivos envolvidos

| Arquivo                                     | Responsabilidade                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `ai/ActionMaskManager.py`                   | Implementa as regras de geração e validação das máscaras em Python.                                       |
| `lobby/TFTLobby.py`                         | Calcula as máscaras por jogador, consolida os resultados e monta o dicionário consumido pelo treinamento. |
| `env.py`                                    | Encaminha a solicitação de máscaras ao `ActionMaskManager`.                                               |
| `policy.py`                                 | Aplica as máscaras às distribuições categóricas da política PPO.                                          |
| `trainer.py`                                | Agrupa, valida e converte as máscaras para tensores PyTorch.                                              |
| `cpp/include/decision/ActionMaskEngine.hpp` | Arquivo destinado à interface da engine C++; vazio na versão `main` auditada.                             |
| `cpp/src/decision/ActionMaskEngine.cpp`     | Arquivo destinado à implementação da engine C++; vazio na versão `main` auditada.                         |
| `cpp/src/decision/AntiLoopEngine.cpp`       | Implementação C++ existente das regras anti-loop que devem ser reutilizadas.                              |

## 3. Contrato das ações

As dimensões categóricas definidas pela política são:

| Índice | Ação                          |                                 Dimensão |
| -----: | ----------------------------- | ---------------------------------------: |
|      0 | `BUY`                         |                          7 tipos de ação |
|      1 | `REROLL`                      |                          5 slots da loja |
|      2 | `BUY_XP`                      | 9 slots do banco na cabeça compartilhada |
|      3 | `MOVE_BENCH`                  |                 28 destinos do tabuleiro |
|      4 | `MOVE_BOARD`                  |                  28 origens do tabuleiro |
|      5 | `SELL` / destino condicionado |     28 categorias na cabeça condicionada |

As dimensões da política são `[7, 5, 9, 28, 28, 28]`. Os índices representam cabeças de ação e não devem ser interpretados isoladamente como permissões completas: a validade de uma ação também depende do tipo de ação selecionado e, em movimentos, da origem escolhida.

### Máscaras nomeadas consumidas pelo treinamento

O `TFTLobby` transforma os resultados em um dicionário com oito entradas:

| Chave                         | Shape      | Finalidade                                                 |
| ----------------------------- | ---------- | ---------------------------------------------------------- |
| `type_mask`                   | `(7,)`     | Tipos de ação permitidos.                                  |
| `shop_mask`                   | `(5,)`     | Slots de compra disponíveis.                               |
| `bench_source_mask`           | `(9,)`     | Unidades existentes no banco; utilizada também para venda. |
| `board_target_mask`           | `(28,)`    | Máscara genérica de destino, mantida por compatibilidade.  |
| `board_source_mask`           | `(28,)`    | Origens do tabuleiro com pelo menos um movimento válido.   |
| `board_move_target_masks`     | `(28, 28)` | Destinos válidos condicionados a cada origem do tabuleiro. |
| `bench_move_source_mask`      | `(9,)`     | Unidades do banco que podem entrar no tabuleiro.           |
| `bench_to_board_target_masks` | `(9, 28)`  | Destinos válidos condicionados a cada slot do banco.       |

O contrato externo da engine C++ deve ser compatível com essas chaves, dimensões e semânticas.

## 4. Mapeamento de todas as funções do `ActionMaskManager`

### 4.1. API principal e tipos de ação

| Função             | Responsabilidade                                                                                                                                               | Categoria     |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `__init__`         | Recebe os managers de tabuleiro, banco, loja, economia, composição, posicionamento, anti-loop e unidades; define os tamanhos e o contador de falhas anti-loop. | Inicialização |
| `get_action_masks` | Gera a lista principal de seis máscaras e aceita máscaras de origem e disponibilidade previamente calculadas.                                                  | API pública   |
| `get_type_mask`    | Habilita ou desabilita os sete tipos de ação, incluindo `PASS`, de acordo com a disponibilidade real.                                                          | Geração       |
| `debug_print`      | Exibe as máscaras calculadas para diagnóstico.                                                                                                                 | Diagnóstico   |

`get_action_masks` retorna uma **lista com seis elementos**, e não o dicionário de oito máscaras consumido pelo `Trainer`. A montagem do dicionário acontece em `TFTLobby.get_action_masks`.

### 4.2. Compra, loja, reroll e experiência

| Função                            | Responsabilidade                                                                                      |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `_get_shop_mask_and_availability` | Calcula a máscara dos cinco slots da loja e informa separadamente se existe uma compra real possível. |
| `get_shop_mask`                   | Expõe a máscara da loja sem retornar a disponibilidade separadamente.                                 |
| `_has_valid_buy`                  | Consulta se há alguma compra real disponível.                                                         |
| `_has_valid_reroll`               | Verifica se a economia permite pagar pelo reroll; retorna `False` em caso de exceção.                 |
| `_has_valid_buy_xp`               | Verifica se a economia permite comprar XP; retorna `False` em caso de exceção.                        |

**Regras importantes:**

* A compra exige espaço livre no banco, uma unidade disponível na loja e saldo suficiente.
* O fallback técnico do slot zero não deve habilitar `BUY` quando não existe compra real.
* Reroll e compra de XP são avaliados separadamente da máscara de compra.

### 4.3. Banco, venda e movimentos para o tabuleiro

| Função                                         | Responsabilidade                                                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `_get_bench_source_mask_and_sell_availability` | Gera a máscara dos slots ocupados do banco e calcula a disponibilidade real de venda em uma única passagem.      |
| `get_bench_source_mask`                        | Retorna os slots ocupados do banco.                                                                              |
| `_has_valid_sell`                              | Informa se existe uma unidade real que pode ser vendida.                                                         |
| `get_board_target_mask`                        | Calcula a união dos destinos vazios válidos para unidades do banco.                                              |
| `get_bench_to_board_target_mask`               | Calcula os destinos válidos para um slot específico do banco.                                                    |
| `_has_valid_bench_move`                        | Verifica se alguma unidade do banco pode entrar no tabuleiro.                                                    |
| `_is_valid_bench_board_move`                   | Valida origem ocupada, destino dentro do tabuleiro e bloqueios anti-loop para um movimento banco → tabuleiro.    |
| `get_bench_move_source_mask`                   | Marca as unidades do banco que possuem pelo menos um destino válido para entrar no tabuleiro.                    |
| `get_bench_move_masks`                         | Calcula conjuntamente a máscara de origens, a matriz de destinos condicionados e a disponibilidade de movimento. |

**Distinção obrigatória:** `bench_source_mask` e `bench_move_source_mask` não são equivalentes. A primeira identifica unidades no banco, inclusive para venda; a segunda identifica unidades que podem ser movidas para o tabuleiro.

A máscara de destinos banco → tabuleiro considera posições vazias. Ela não deve ser confundida com a máscara de movimentos entre duas posições do tabuleiro, que também pode permitir trocas entre unidades.

### 4.4. Movimentos dentro do tabuleiro

| Função                              | Responsabilidade                                                                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `get_board_source_mask`             | Marca origens ocupadas que possuem pelo menos um destino válido diferente da origem.                                                                   |
| `get_conditioned_board_target_mask` | Calcula a união dos destinos válidos considerando as origens ocupadas.                                                                                 |
| `_is_valid_board_move`              | Valida limites, origem ocupada, diferença entre origem e destino e bloqueios anti-loop. Distingue movimento para espaço vazio de troca entre unidades. |
| `_has_valid_board_move`             | Verifica se existe pelo menos um movimento válido no tabuleiro.                                                                                        |
| `get_board_move_target_mask`        | Gera os destinos válidos para uma origem específica do tabuleiro.                                                                                      |
| `get_board_move_masks`              | Calcula em uma única passagem a máscara de origens, a matriz de destinos `(28, 28)` e a disponibilidade real de movimento.                             |

A validação de movimentos no tabuleiro possui dois casos:

* **Espaço vazio:** o movimento é validado com o tipo `board_move`.
* **Posição ocupada:** a operação é tratada como troca, validada com o tipo `board_swap`.

A origem e o destino devem ser diferentes. A existência de uma unidade no tabuleiro, isoladamente, não torna `MOVE_BOARD` válido.

### 4.5. Helpers de estado e legalidade

| Função                     | Responsabilidade                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `_get_board`               | Obtém o tabuleiro do manager ou retorna um tabuleiro vazio de tamanho padrão quando não há estado disponível. |
| `_get_bench`               | Obtém o banco do manager ou retorna uma lista vazia de tamanho padrão.                                        |
| `_get_shop`                | Consulta a loja; em caso de exceção, tenta o atributo local e, como último fallback, retorna slots vazios.    |
| `_has_free_board_slot`     | Verifica se há posição vazia usando o manager, com fallback para inspeção direta do tabuleiro.                |
| `_is_valid_board_position` | Valida uma posição por meio do manager, usando limites fixos como fallback.                                   |
| `_should_block_anti_loop`  | Consulta o `AntiLoopManager`, registra falhas de diagnóstico e decide se o candidato deve ser bloqueado.      |

Esses helpers não são detalhes descartáveis: eles definem o comportamento de contingência da geração das máscaras quando um manager falha ou não possui estado disponível.

### 4.6. Integração anti-loop

`_should_block_anti_loop` consulta `should_block_move`, passando:

* tipo do movimento;
* origem;
* destino;
* unidade envolvida.

Se a consulta anti-loop lançar uma exceção, a implementação Python atual permite o candidato nessa camada e registra a falha. A primeira falha é registrada com traceback; ocorrências posteriores são contabilizadas e avisos são emitidos periodicamente.

**Esse comportamento de tolerância a falhas precisa ser tratado explicitamente na migração.** Não se deve converter silenciosamente uma falha de consulta em bloqueio total de movimentos, nem duplicar a lógica do `AntiLoopEngine`.

## 5. Fallbacks e invariantes

As máscaras categóricas usam o valor `1` no índice zero como fallback quando não há opções reais. Esse fallback evita distribuições categóricas vazias, mas **não representa necessariamente uma ação válida**.

A disponibilidade real deve ser calculada separadamente e refletida em `type_mask`. Por exemplo:

* não há compras reais → `BUY` desabilitado, mesmo que `shop_mask[0]` esteja marcado;
* não há unidades vendáveis → `SELL` desabilitado, mesmo que `bench_source_mask[0]` esteja marcado;
* não há movimentos reais → `MOVE_BENCH` ou `MOVE_BOARD` desabilitado, mesmo que uma origem dummy esteja marcada.

Outros invariantes a preservar:

1. Os tamanhos são fixos: loja 5, banco 9 e tabuleiro 28.
2. Todas as máscaras consumidas pela política devem conter somente `0` e `1`.
3. Cada distribuição categórica deve ter pelo menos uma categoria habilitada.
4. A máscara de tipo deve representar a disponibilidade real, não os fallbacks técnicos das cabeças auxiliares.
5. Jogadores eliminados devem receber uma máscara que permita somente `PASS`.
6. Consultar máscaras não deve atualizar indevidamente o histórico anti-loop.
7. A matriz de destinos precisa permanecer condicionada à origem escolhida.

## 6. Fluxo atual de geração

O fluxo de máscaras usado pelo treinamento é:

1. `TFTLobby.get_action_masks` identifica cada jogador.
2. Jogadores eliminados recebem máscaras dummy, com somente `PASS` permitido.
3. Para jogadores ativos, o lobby chama `get_board_move_masks`.
4. Em seguida, chama `get_bench_move_masks`.
5. Os resultados são reutilizados na chamada de `env.get_action_masks`, evitando recalcular disponibilidade de movimentos.
6. O lobby converte as seis máscaras retornadas em parte de um dicionário de oito chaves.
7. `Trainer._flatten_masks` valida as formas, os valores e os tipos, agrupando as máscaras em tensores booleanos.
8. `TFTPolicy` aplica as máscaras às cabeças de ação e aos destinos condicionados.

As funções `get_board_target_mask`, `get_conditioned_board_target_mask`, `get_bench_to_board_target_mask`, `get_board_source_mask` e os métodos individuais de disponibilidade também fazem parte da API de `ActionMaskManager`, ainda que o fluxo principal do lobby prefira os métodos que calculam as máscaras em lote.

## 7. Pontos de atenção identificados

### 7.1. Cálculo duplicado

Os métodos individuais de disponibilidade e os métodos em lote podem percorrer repetidamente as mesmas origens e destinos. O fluxo do lobby já reduz essa repetição usando `get_board_move_masks` e `get_bench_move_masks`.

A engine C++ deve preservar esse caminho otimizado, evitando recalcular os mesmos pares de posições dentro de uma única geração.

### 7.2. Máscaras genéricas versus condicionadas

`board_target_mask` não substitui `board_move_target_masks`. A matriz `(28, 28)` é necessária para filtrar destinos de acordo com a origem efetivamente selecionada pela política.

Da mesma forma, `bench_to_board_target_masks` não substitui `bench_move_source_mask`: uma representa destinos por origem, e a outra representa quais origens têm algum movimento válido.

### 7.3. Tratamento de exceções

Os helpers possuem políticas de fallback diferentes. Algumas consultas retornam `False`; outras usam estado local ou valores padrão; falhas anti-loop permitem o candidato e geram logs.

A migração deve documentar e reproduzir essas diferenças de forma intencional, evitando substituir todas as exceções por um único comportamento genérico.

### 7.4. Dependências armazenadas

`composition_manager`, `positioning_manager` e `unit_manager` são recebidos e armazenados pelo `ActionMaskManager`, mas não são utilizados diretamente pelas funções de geração identificadas nesta auditoria. Não há necessidade de incorporá-los automaticamente à primeira versão da engine C++.

### 7.5. Validação dos dados

`get_action_masks` converte uma máscara de origem externa para `float32`, mas não valida explicitamente seu tamanho. A validação posterior feita pelo `Trainer` verifica as formas e os valores antes de criar os tensores.

Na migração, o contrato de entrada deve ser definido claramente. Melhorias de validação podem ser introduzidas, mas devem ser separadas da reprodução inicial do comportamento para facilitar a comparação Python/C++.

## 8. Organização sugerida para a engine C++

A implementação pode ser organizada em grupos funcionais, sem exigir uma correspondência artificial de um método C++ para cada método Python:

1. **API e tipos:** tipos de ação, dimensões e estrutura de saída das máscaras.
2. **Economia e loja:** compra, reroll, XP e disponibilidade de venda.
3. **Banco → tabuleiro:** origens, destinos e disponibilidade de movimentos.
4. **Tabuleiro → tabuleiro:** movimentos, trocas, origens e destinos condicionados.
5. **Integração anti-loop:** reutilização do `AntiLoopEngine`.
6. **Adaptação Python:** bindings pybind11 e compatibilidade com o dicionário esperado pelo lobby e pelo treinamento.

A implementação pode compartilhar cálculos internos entre máscaras relacionadas, desde que preserve o contrato público e os resultados esperados.

## 9. Checklist da auditoria

* [x] Mapear as funções de geração das máscaras.
* [x] Mapear as funções auxiliares de legalidade e disponibilidade.
* [x] Identificar os consumidores das máscaras no lobby, no ambiente e na política.
* [x] Registrar as dimensões e os nomes das máscaras consumidas pelo treinamento.
* [x] Identificar a integração com o anti-loop.
* [x] Documentar os fallbacks técnicos e as diferenças entre máscaras de origem e de destino.
* [x] Identificar os arquivos C++ destinados à engine de máscaras.
* [ ] Implementar a engine C++.
* [ ] Expor a API via pybind11.
* [ ] Integrar a engine ao fluxo do lobby.
* [ ] Criar testes C++ equivalentes aos cenários Python.
* [ ] Validar equivalência comportamental entre Python e C++.
* [ ] Avaliar desempenho e remoção do caminho Python somente após a validação.

## 10. Critério de conclusão

A auditoria está concluída quando todas as funções, dependências, consumidores, formatos e regras de fallback estão documentados.

A migração estará concluída somente depois que a implementação C++ reproduzir os resultados esperados das máscaras, integrar-se ao `AntiLoopEngine`, passar pelos testes automatizados e demonstrar compatibilidade com o fluxo de treinamento PPO.

A implementação Python deve permanecer como referência e fallback durante essa validação.
