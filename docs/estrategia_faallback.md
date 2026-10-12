# Estratégia de Fallback e Ativação Controlada — Action Masks e AntiLoop em C++

## 1. Objetivo

Introduzir a implementação nativa gradualmente, garantindo que a implementação Python continue disponível como referência e alternativa operacional.

A migração não deve exigir a substituição imediata do código Python. O módulo C++ só poderá assumir a geração das máscaras no fluxo normal depois de demonstrar equivalência funcional, estabilidade e ganho de desempenho mensurável.

Princípios obrigatórios:

- Python continua sendo a referência funcional.
- A ativação do C++ é explícita e configurável.
- Uma falha nativa não pode deixar o treinamento sem máscaras válidas.
- Não se aceita divergência silenciosa entre as implementações.
- O rollback não pode exigir alterações nos pesos ou no checkpoint do PPO.
- O código Python não será removido enquanto o C++ não estiver validado e a estratégia de fallback não estiver comprovada.

## 2. Modos de operação

A integração deve possuir modos explícitos, selecionados por configuração.

| Modo | Comportamento | Finalidade |
|---|---|---|
| `python` | Somente a implementação Python gera as máscaras | Referência e rollback |
| `shadow` | Python gera as máscaras utilizadas; C++ calcula em paralelo para comparação | Validar equivalência sem afetar as ações |
| `native` | C++ gera as máscaras utilizadas; Python permanece disponível para fallback | Operação controlada |
| `native_strict` | C++ é obrigatório; qualquer falha nativa interrompe a operação com erro explícito | Diagnóstico e testes de integração |

O modo `python` deve ser o padrão inicial. Durante a validação, `shadow` é o modo preferencial. `native` só deve ser habilitado depois dos critérios de aceitação. `native_strict` serve principalmente para revelar problemas que o fallback poderia ocultar.

A configuração deve ser centralizada e registrada no início da execução, sem depender de alterações no código da política PPO.

## 3. Estratégia de fallback

### 3.1. Quando acionar

O fallback para Python deve ocorrer quando:

- O módulo nativo não puder ser importado no modo `native`.
- A chamada C++ lançar uma exceção.
- A resposta possuir dimensões inesperadas.
- Alguma máscara obrigatória estiver ausente.
- Os valores retornados forem incompatíveis com o contrato.
- A resposta não puder ser convertida para o formato consumido pelo treinador.
- Uma verificação de consistência obrigatória falhar.

Em `native_strict`, esses casos devem produzir erro explícito, sem substituição silenciosa por Python.

### 3.2. Fluxo do fallback

No modo `native`, o fluxo será:

1. Criar um snapshot consistente do jogador.
2. Invocar o módulo C++.
3. Validar o resultado antes de utilizá-lo.
4. Se o resultado for válido, utilizar as máscaras nativas.
5. Se ocorrer uma falha, registrar o erro e calcular as máscaras com Python.
6. Entregar ao PPO somente um conjunto completo e validado de máscaras.

O fallback deve substituir o resultado inteiro da chamada. Não se deve misturar, por exemplo, `type_mask` do Python com `board_move_target_masks` do C++ sem um contrato explícito que garanta consistência entre elas.

### 3.3. Falha do fallback Python

Se o próprio cálculo Python também falhar, a exceção deve ser propagada de forma clara. O sistema não deve criar máscaras arbitrárias para esconder uma falha dupla.

Uma máscara dummy de jogador eliminado não é um mecanismo genérico de recuperação. Ela só deve ser usada quando o estado oficial realmente indicar que o jogador está eliminado.

## 4. Validação da resposta nativa

Antes de entregar a resposta ao PPO, validar:

- Presença das oito máscaras obrigatórias.
- Dimensões exatas: `(7,)`, `(5,)`, `(9,)`, `(28,)`, `(28,)`, `(28, 28)`, `(9,)` e `(9, 28)`.
- Valores booleanos ou valores numéricos estritamente equivalentes a habilitado/desabilitado, conforme o contrato.
- Ausência de categorias inteiramente inválidas onde o contrato exige fallback.
- Disponibilidade real de ações coerente com os indicadores auxiliares.
- Correspondência entre origens habilitadas e destinos condicionais válidos.
- Disponibilidade de `PASS` para jogadores ativos, de acordo com a regra atual.
- Somente `PASS` como tipo de ação para jogadores eliminados.

Uma resposta com formato correto não garante equivalência funcional. Por isso, a validação estrutural deve ser complementada por testes de equivalência no modo `shadow`.

## 5. Modo shadow

O modo `shadow` é a principal proteção antes da ativação.

Para cada snapshot:

1. Python calcula as máscaras de referência.
2. C++ calcula suas máscaras.
3. As duas respostas são normalizadas para um formato comparável.
4. O resultado Python é utilizado pela política.
5. A divergência é registrada para análise.

A comparação deve incluir as oito máscaras completas, os indicadores de disponibilidade e, nos testes específicos, os motivos de bloqueio AntiLoop.

A execução shadow não deve aplicar ações, registrar movimentos ou alterar o histórico. A consulta nativa precisa ser somente leitura.

### Divergências

Cada divergência deve registrar, sempre que possível:

- modo de execução;
- versão do contrato;
- identificação do cenário ou snapshot;
- máscara e índice divergentes;
- valor Python;
- valor C++;
- dimensões recebidas;
- erro ou motivo de bloqueio, quando aplicável.

Não é necessário guardar snapshots completos de todas as iterações indefinidamente. Os registros devem ser suficientes para reproduzir os casos problemáticos sem gerar um volume excessivo de dados.

**Regra de segurança:** divergências funcionais não podem ser ignoradas apenas porque a maioria das máscaras coincide.

## 6. Ativação progressiva

A ativação deve ocorrer por etapas, com critérios objetivos de avanço.

### Etapa A — Python como referência

- Todas as chamadas utilizam Python.
- O contrato nativo é definido.
- A suíte de testes de referência é preparada.
- Nenhuma alteração no comportamento da IA é atribuída à migração.

### Etapa B — Shadow em testes controlados

- C++ recebe snapshots equivalentes aos usados pelo Python.
- Todas as máscaras são comparadas.
- Casos representativos e extremos são executados.
- Divergências bloqueiam a promoção para a próxima etapa.

### Etapa C — Shadow em treinamento controlado

- Python continua fornecendo as máscaras efetivamente utilizadas.
- C++ é exercitado em estados reais do treinamento.
- São coletados erros, divergências, latências médias e percentis.
- O desempenho é comparado com uma referência Python medida nas mesmas condições.

### Etapa D — Native em ambiente controlado

- C++ passa a fornecer as máscaras.
- O fallback Python permanece ativo.
- Erros e acionamentos de fallback são monitorados.
- A execução pode retornar ao modo Python sem alterar os pesos ou o formato dos checkpoints.

### Etapa E — Native como padrão operacional

Só pode ocorrer após os critérios de aceitação serem atendidos. Mesmo nessa etapa, a implementação Python deve permanecer disponível até que a remoção do caminho Python seja autorizada e planejada separadamente.

## 7. Critérios para avançar de etapa

A promoção de uma etapa para outra exige:

1. Todos os casos obrigatórios de equivalência aprovados.
2. Nenhuma divergência funcional sem explicação e resolução.
3. Nenhum erro de memória, acesso inválido ou corrupção de dados.
4. Comportamento correto em reset, falhas de execução e histórico no limite.
5. Fallback validado por testes que provoquem falhas nativas deliberadamente.
6. Medições de desempenho comparáveis e reproduzíveis.
7. Ausência de regressões relevantes no treinamento controlado.

Não se deve definir um ganho percentual mínimo de desempenho sem antes estabelecer uma referência comparável e o custo real da conversão dos snapshots. O ganho deve ser medido no fluxo completo, não apenas dentro de uma função C++ isolada.

## 8. Rollback

O rollback deve ser uma mudança de configuração para `python`, seguida de uma nova execução controlada.

Procedimento:

1. Interromper ou encerrar ordenadamente a execução nativa afetada.
2. Registrar o erro e o último contexto reproduzível.
3. Desabilitar o modo nativo.
4. Reiniciar o treinamento ou ambiente no modo Python.
5. Reutilizar o checkpoint somente se o estado salvo for compatível com o estado de treinamento desejado.
6. Confirmar que o módulo C++ não é mais usado para gerar máscaras.

O rollback não deve depender de recompilar o projeto ou remover arquivos nativos.

Como as máscaras influenciam as ações amostradas e as transições subsequentes, não se deve presumir que é seguro continuar exatamente a mesma trajetória após uma divergência funcional. A retomada precisa respeitar a consistência do estado do ambiente e do rollout PPO.

## 9. Métricas operacionais

A integração deve acompanhar pelo menos:

- número de chamadas nativas;
- número de falhas nativas;
- número de acionamentos do fallback;
- número de divergências shadow;
- latência média e P95 da geração de máscaras;
- latência de conversão do snapshot;
- latência total do caminho de máscaras;
- distribuição de motivos de falha.

As métricas de execução de movimentos do AntiLoop devem continuar separadas das métricas operacionais da integração. Uma consulta de máscara não pode aumentar contadores de movimentos executados.

## 10. Critérios de aceitação

A estratégia estará pronta quando:

- Os quatro modos estiverem definidos e documentados.
- O modo Python funcionar sem depender do módulo de decisão nativo.
- O modo shadow comparar as respostas sem influenciar as ações.
- O modo native validar as respostas antes de utilizá-las.
- Falhas nativas acionarem o fallback corretamente.
- Falhas duplas forem propagadas de forma explícita.
- O rollback puder ser executado por configuração.
- Os critérios para ativação progressiva forem verificáveis.
- O desempenho for medido no fluxo completo.
- A implementação Python continuar disponível como referência e alternativa.

## Conclusão

A ativação do C++ deve ser gradual: primeiro comparar, depois observar em treinamento, e somente então utilizar a implementação nativa como fonte das máscaras. O fallback deve ser explícito, monitorado e testado; não pode esconder divergências nem transformar falhas internas em ações aparentemente válidas.

A implementação Python permanece como referência e caminho de recuperação até que a migração tenha demonstrado equivalência funcional e estabilidade.