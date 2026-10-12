# Casos de Referência para Comparação entre Python e C++ — Action Masks e AntiLoop

## 1. Objetivo

Definir casos representativos e extremos para comparar as implementações Python e C++ usando os mesmos estados, parâmetros e históricos.

Os testes devem verificar quatro aspectos:

1. **Equivalência das máscaras:** mesmas dimensões e mesmos valores em todas as posições.
2. **Equivalência das decisões AntiLoop:** mesmos resultados e motivos de bloqueio para cada candidato.
3. **Equivalência dos efeitos colaterais:** consultas não modificam o estado; execuções atualizam o histórico no momento correto.
4. **Robustez:** estados extremos e entradas-limite não causam divergências, exceções inesperadas ou máscaras inválidas.

A implementação Python é a referência inicial. A implementação C++ deve reproduzir seu comportamento atual, incluindo fallbacks e peculiaridades existentes, antes de qualquer mudança deliberada de regra.

## 2. Contrato comum de cada caso de teste

Cada caso deve definir:

- Identificador e descrição.
- Estado do tabuleiro, com 28 posições.
- Estado do banco, com nove posições.
- Estado da loja, com cinco posições, quando relevante.
- Dados econômicos e estado ativo/eliminado do jogador, quando relevantes.
- Identidade das unidades.
- Parâmetros do AntiLoop.
- Histórico de estados, movimentos, bloqueios e visitas.
- Operação a testar.
- Resultado esperado.
- Estado histórico esperado após a operação, quando houver efeitos colaterais.

O mesmo cenário deve ser carregado nas duas implementações. Não se deve executar uma sequência de ações em Python e reutilizar o estado já modificado para iniciar a execução equivalente em C++.

## 3. Casos representativos de Action Masks

### AM-01 — Estado inicial com banco ocupado e tabuleiro vazio

**Preparação:** tabuleiro vazio, pelo menos uma unidade no banco e estado econômico válido.

**Verificar:**
- Formatos e dimensões das oito máscaras.
- `bench_move_source_mask` habilita a origem que possui destino válido.
- `bench_to_board_target_masks` habilita os destinos permitidos para essa origem.
- `board_source_mask` não identifica origens inexistentes.
- `MOVE_BENCH` só é permitido quando existe uma combinação real de origem e destino.
- A máscara de venda diferencia uma unidade real de um fallback.

**Resultado esperado:** máscaras idênticas entre Python e C++, inclusive nas posições não habilitadas.

### AM-02 — Tabuleiro parcialmente ocupado

**Preparação:** unidades em posições conhecidas e pelo menos uma posição vazia.

**Verificar:**
- Origens ocupadas com destinos válidos.
- Destinos vazios.
- Destinos ocupados que permitem uma troca, conforme as regras atuais.
- Rejeição de movimentos da posição para ela mesma.
- Correspondência entre cada linha da matriz de destino e sua origem.

**Resultado esperado:** igualdade de `board_source_mask` e `board_move_target_masks`.

### AM-03 — Tabuleiro cheio

**Preparação:** todas as 28 posições ocupadas.

**Verificar:**
- Nenhum movimento banco → tabuleiro pode ser considerado válido apenas pela existência de unidades no banco.
- As máscaras condicionais do banco utilizam o fallback apropriado.
- Movimentos entre unidades no tabuleiro continuam sujeitos às regras atuais.
- A disponibilidade de `MOVE_BENCH` não é habilitada pelo fallback.

**Resultado esperado:** mesmas máscaras e mesmos indicadores de disponibilidade real.

### AM-04 — Banco vazio

**Preparação:** nove posições vazias no banco.

**Verificar:**
- Nenhuma unidade pode ser vendida ou movida a partir do banco.
- `bench_source_mask` e `bench_move_source_mask` mantêm as dimensões corretas.
- As máscaras de destino condicionais seguem o comportamento de fallback atual.
- `SELL` e `MOVE_BENCH` não são habilitados somente pelo fallback.

### AM-05 — Loja sem compras possíveis

**Preparação:** loja vazia, ou unidades cujo custo não pode ser pago, ou banco sem espaço.

**Verificar:**
- `shop_mask` tem cinco categorias.
- O fallback da loja não é confundido com compra disponível.
- `BUY` permanece desabilitado quando não existe compra real.
- A disponibilidade das demais ações continua sendo calculada independentemente.

### AM-06 — Economia em valores-limite

**Preparação:** repetir o caso de compra com ouro exatamente igual ao custo, um valor abaixo do custo e um valor acima do custo.

**Verificar:**
- A máscara segue o resultado de `EconomyManager.can_spend()` para cada valor.
- `REROLL` e `BUY_XP` seguem suas próprias regras.
- A disponibilidade de compra não depende somente de a loja conter uma unidade.

**Resultado esperado:** equivalência para cada valor de entrada, sem assumir que todas as operações utilizam o mesmo custo.

### AM-07 — Jogador eliminado

**Preparação:** jogador marcado como eliminado.

**Verificar:**
- `type_mask` permite somente `PASS`.
- As demais máscaras possuem os formatos esperados.
- As categorias dummy não habilitam ações adicionais.
- A política consegue processar as máscaras sem distribuição categórica vazia.

### AM-08 — Nenhum movimento válido

**Preparação:** estados nos quais todas as origens candidatas estão bloqueadas pelo AntiLoop ou não possuem destinos válidos.

**Verificar:**
- Máscaras condicionais não ficam vazias quando o código atual prevê fallback.
- A disponibilidade real de movimento continua falsa.
- O fallback não habilita `MOVE_BOARD` ou `MOVE_BENCH`.
- A geração das máscaras não registra movimentos executados.

## 4. Casos representativos do AntiLoop

### AL-01 — Histórico vazio

**Preparação:** AntiLoop recém-inicializado, sem estados ou movimentos registrados.

**Verificar:**
- Não há reversão sem um movimento anterior.
- Não há oscilação ou ciclo detectado a partir de histórico inexistente.
- Não há bloqueio explícito.
- `get_block_reason()` retorna `None` para um movimento legal que não encontre nenhuma proteção aplicável.

### AL-02 — Reversão de movimento normal

**Preparação:** registrar `board_move` de A para B por uma unidade e consultar o movimento inverso B para A da mesma unidade.

**Verificar:**
- A ação inversa é identificada como reversão.
- O motivo retornado respeita a precedência das regras.
- A consulta não altera `last_move` nem `move_history`.

### AL-03 — Reversão de troca

**Preparação:** registrar `board_swap` entre duas posições e consultar novamente a troca com origem e destino invertidos.

**Verificar:**
- A regra especial de troca considera o mesmo par de posições.
- A detecção não depende da identidade da unidade como na reversão normal.
- O motivo final respeita a ordem de avaliação das proteções.

### AL-04 — Oscilação repetida

**Preparação:** criar uma sequência de movimentos da mesma unidade que repita destinos na cadeia recente.

**Verificar:**
- A regra utiliza a janela de histórico prevista.
- A identidade da unidade é aplicada corretamente.
- A sequência de posições é reconstruída com continuidade.
- O mesmo candidato recebe o mesmo resultado nas duas implementações.

### AL-05 — Ida e volta entre banco e tabuleiro

**Preparação:** registrar movimentos correspondentes de banco para tabuleiro e de tabuleiro para banco para a mesma unidade.

**Verificar:**
- Os tipos reconhecidos pela regra são normalizados conforme os aliases atuais.
- A unidade e as posições correspondem à sequência registrada.
- Um movimento sem correspondência de unidade ou posições não é bloqueado por essa regra isoladamente.

### AL-06 — Fechamento de ciclo no tabuleiro

**Preparação:** criar uma sequência contínua de movimentos que feche um ciclo de posições.

**Verificar:**
- A primeira conclusão do ciclo segue a regra atual.
- A repetição posterior é avaliada conforme o histórico.
- O filtro por identidade e tipo de movimento é preservado.
- O resultado não depende de movimentos fora da janela considerada pela regra.

### AL-07 — Bloqueio explícito no mesmo estado

**Preparação:** registrar uma assinatura de estado, bloquear explicitamente um movimento e consultar o mesmo movimento sem alterar a assinatura.

**Verificar:**
- O movimento é bloqueado como `explicit`.
- A chave inclui tipo, origem, destino e identidade.
- A assinatura associada ao bloqueio coincide com a assinatura atual.

### AL-08 — Bloqueio explícito após mudança de estado

**Preparação:** registrar um bloqueio e, em seguida, registrar uma assinatura de estado diferente.

**Verificar:**
- O bloqueio deixa de ser aplicável quando a assinatura atual muda.
- O resultado é idêntico nas duas implementações.
- O histórico e o mapeamento de assinaturas não ficam inconsistentes.

### AL-09 — Precedência dos motivos

**Preparação:** construir um histórico no qual mais de uma regra possa reconhecer o mesmo candidato.

**Verificar:**
- O motivo retornado é o da primeira regra correspondente.
- A ordem é: explícito, reversão, oscilação, ciclo banco ↔ tabuleiro quando aplicável e ciclo geral.
- As métricas de execução não são incrementadas apenas por consultar o motivo.

## 5. Casos extremos de identidade e estrutura

### EX-01 — Unidade com UUID

**Preparação:** duas unidades com UUIDs diferentes, mesmo `id` e mesma estrela.

**Verificar:** são identidades distintas.

### EX-02 — Unidade sem UUID

**Preparação:** unidades sem UUID com o mesmo `id` e mesma estrela.

**Verificar:** a implementação atual as considera equivalentes pela combinação `id + star`.

### EX-03 — Estrela ausente

**Preparação:** unidade sem UUID e sem o campo `star`.

**Verificar:** a identidade utiliza o valor padrão `1`.

### EX-04 — Objeto que não é dicionário

**Preparação:** fornecer uma unidade em formato diferente de dicionário.

**Verificar:** `_unit_identity()` retorna `None` no Python. O C++ deve reproduzir a semântica definida para esse caso, sem inventar uma identidade alternativa.

### EX-05 — Posição vazia

**Preparação:** tabuleiro e banco contendo posições vazias intercaladas com unidades.

**Verificar:**
- Assinaturas incluem todas as posições na ordem correta.
- `None` é representado de forma consistente.
- Posições vazias e posições ocupadas não são confundidas.

### EX-06 — Índices nos limites

**Preparação:** consultar origens e destinos nos índices mínimo e máximo, além de índices fora dos limites.

**Verificar:**
- Índices válidos permanecem válidos conforme o estado.
- Índices inválidos são tratados conforme o contrato atual.
- Não ocorrem acessos fora dos limites nem conversões silenciosas para outra posição.

### EX-07 — Histórico no limite de capacidade

**Preparação:** preencher `position_history`, `move_history` e `blocked_moves` até seus limites e adicionar novos registros.

**Verificar:**
- Os registros mais antigos são removidos conforme o comportamento das estruturas atuais.
- As assinaturas associadas a bloqueios expirados são removidas corretamente.
- Os movimentos ainda presentes na janela continuam sendo avaliados.
- A ordem e o conteúdo do histórico são equivalentes.

### EX-08 — Contagem de visitas no limiar

**Preparação:** registrar a mesma assinatura até atingir e ultrapassar `loop_threshold`.

**Verificar:**
- O valor de `visits` aumenta corretamente.
- `repeated` muda no limiar configurado.
- `state_visits` e `position_history` são atualizados de acordo com suas regras distintas.

### EX-09 — Histórico com tipos diferentes

**Preparação:** intercalar `board_move`, `board_swap`, `bench_to_board` e outros tipos aceitos pelas regras.

**Verificar:**
- Cada proteção filtra os tipos conforme sua implementação.
- Aliases não são normalizados globalmente sem previsão no contrato.
- A sequência não é interpretada como um ciclo apenas por conter posições repetidas.

### EX-10 — Estado espacial igual, economia diferente

**Preparação:** manter tabuleiro e banco idênticos, alterando ouro, XP ou loja.

**Verificar:**
- A assinatura espacial do AntiLoop permanece igual.
- As máscaras de economia podem mudar.
- A implementação não inclui acidentalmente dados econômicos na assinatura do posicionamento.

## 6. Casos de efeitos colaterais e sincronização

### FX-01 — Consultas repetidas

**Preparação:** consultar várias vezes as mesmas máscaras e o mesmo motivo de bloqueio, sem executar ações.

**Verificar:** históricos, bloqueios e métricas de execução permanecem inalterados, exceto por registros de diagnóstico que o comportamento atual já preveja.

### FX-02 — Movimento bloqueado na execução

**Preparação:** tentar executar um movimento que o AntiLoop bloqueia.

**Verificar:**
- A ação é rejeitada.
- `execution_attempts` e `execution_blocks` são atualizados conforme o fluxo atual.
- O contador específico do motivo é incrementado uma vez.
- Nenhum movimento bem-sucedido é registrado.

### FX-03 — Movimento concluído

**Preparação:** executar um movimento válido até sua conclusão.

**Verificar:**
- O estado do tabuleiro ou banco é atualizado.
- O movimento é registrado uma única vez.
- `last_move` passa a refletir o movimento.
- As métricas de sucesso correspondem ao tipo executado.

### FX-04 — Falha na execução

**Preparação:** usar um candidato que passe por parte da validação, mas cuja operação de movimento falhe.

**Verificar:**
- A falha não é registrada como movimento concluído.
- Não ocorre atualização indevida de `last_move`.
- Os contadores refletem o ponto em que a falha ocorreu.

### FX-05 — Rollback de banco para tabuleiro

**Preparação:** simular uma falha na inserção da unidade no tabuleiro depois de removê-la do banco.

**Verificar:**
- O fluxo tenta restaurar a unidade ao slot original.
- A falha não é registrada como movimento bem-sucedido.
- O histórico AntiLoop permanece consistente com o resultado efetivo.

### FX-06 — Reset

**Preparação:** preencher os históricos e incrementar métricas; depois chamar `reset()`.

**Verificar:**
- Históricos, visitas, último movimento e bloqueios são limpos.
- `execution_metrics` permanece acumulado.
- A geração de máscaras após o reset não utiliza dados históricos da partida anterior.

### FX-07 — Falha em consulta AntiLoop durante geração de máscaras

**Preparação:** provocar uma exceção controlada na consulta AntiLoop.

**Verificar:**
- O caminho atual de geração registra a falha e permite o candidato nessa camada.
- A falha não cria um registro de movimento executado.
- Python e C++ seguem a política de tolerância definida para a integração.

## 7. Comparação automatizada

Para cada cenário, a comparação deve usar o mesmo snapshot e verificar:

| Elemento | Critério |
|---|---|
| Formato das máscaras | Igualdade exata de dimensões |
| Tipo dos valores | Conversão compatível com o contrato |
| Valores das máscaras | Igualdade elemento a elemento |
| Disponibilidade real | Igualdade dos indicadores |
| Motivo de bloqueio | Mesmo motivo ou `None` |
| Assinatura do estado | Mesmo conteúdo e mesma ordem |
| Histórico de movimentos | Mesmos registros e sequência |
| Bloqueios explícitos | Mesmas chaves e assinaturas associadas |
| Métricas | Mesmos deltas após a mesma operação |
| Reset | Mesmo estado histórico e mesmas métricas persistentes |

Para máscaras booleanas, a comparação deve ser exata. Não basta comparar o número total de valores habilitados: uma única posição diferente pode permitir uma ação proibida.

Para históricos, é necessário comparar tanto o conteúdo quanto a ordem, pois a ordem influencia as proteções.

## 8. Estratégia de execução dos testes

1. Preparar fixtures determinísticas com estados e históricos explícitos.
2. Executar cada fixture na implementação Python de referência.
3. Executar o mesmo caso na implementação C++.
4. Comparar todas as máscaras e indicadores.
5. Comparar os motivos de bloqueio para uma lista de candidatos.
6. Comparar o estado interno relevante antes e depois das consultas.
7. Executar os casos com efeitos colaterais e comparar os deltas de histórico e métricas.
8. Repetir os casos extremos nos limites de capacidade.
9. Registrar divergências com o identificador do caso, entrada utilizada, resultado Python e resultado C++.
10. Só considerar um caso equivalente quando todos os critérios aplicáveis forem atendidos.

A comparação deve ser determinística: nenhuma implementação deve depender de sorteios ou estados aleatórios diferentes durante o teste.

## 9. Critérios de aceitação

A base de comparação está pronta quando:

- Todos os cenários possuem entradas reproduzíveis.
- Cada cenário possui um resultado esperado ou uma referência Python registrada.
- Todas as oito máscaras são comparadas integralmente.
- As proteções AntiLoop possuem casos positivos e negativos.
- Os limites de histórico e de índices estão cobertos.
- Os efeitos colaterais e o reset são verificados.
- As divergências são identificadas por caso e não apenas por uma contagem agregada.
- Nenhuma divergência é ignorada sem explicação e decisão explícita.

## 10. Conclusão

Os casos devem cobrir tanto situações normais quanto combinações que expõem diferenças sutis de semântica: fallback versus disponibilidade real, identidade UUID versus `id + star`, reversões de troca, histórico no limite e consultas que não podem produzir efeitos colaterais.

A equivalência não deve ser declarada apenas porque as máscaras coincidem em um estado inicial. Ela precisa permanecer válida ao longo de sequências de decisões, execuções, falhas, bloqueios e resets.