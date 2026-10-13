# Testes de Equivalência do AntiLoop — Python × C++

## Objetivo

Validar que o motor nativo C++ reproduz o comportamento do `AntiLoopManager` Python durante a construção das máscaras de ação.

O Python continua sendo a referência de comportamento. Diferenças encontradas devem ser investigadas e corrigidas no C++, sem alterar as regras Python para forçar equivalência.

## Cenários cobertos

* Movimento inverso no tabuleiro.
* Swap repetido entre posições.
* Ciclo de movimentação entre banco e tabuleiro.
* Repetição de um ciclo de posicionamento.
* Comparação das seis máscaras com históricos sincronizados.
* Ausência de mutações no histórico durante a geração de máscaras.
* Tolerância do Python a exceções na consulta ao AntiLoop.

## Contrato de comportamento

A geração das máscaras é uma consulta: não deve registrar movimentos, alterar estados visitados, inserir bloqueios ou incrementar métricas de execução.

A identidade de uma unidade deve manter a prioridade definida pelo Python: UUID quando disponível; caso contrário, ID e estrela.

O Python captura exceções de `should_block_move` e permite o candidato nessa camada. Esse comportamento de tolerância a falhas é testado separadamente, pois não representa uma regra de bloqueio do motor C++.

## Executar os testes

Com a extensão `decision_engine` compilada e acessível no ambiente Python:

```bash
python -m pytest tests/test_action_mask_equivalence.py -v
```

## Interpretação dos resultados

* **PASS:** o cenário testado apresentou o comportamento esperado.
* **FAIL:** investigar a divergência entre Python e C++ antes de modificar qualquer expectativa.
* **SKIPPED:** verificar se a extensão nativa está compilada e disponível no ambiente de testes.

A aprovação desses testes não comprova, isoladamente, equivalência de todas as sequências possíveis de movimentos. A validação final também depende da integração com o histórico real por jogador e de testes de regressão em partidas completas.
