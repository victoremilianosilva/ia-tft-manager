# Testes nativos da AntiLoopEngine

## Objetivo

Criar uma suíte de testes em C++ para validar os principais comportamentos da `AntiLoopEngine`, usando a implementação nativa e sem depender da execução dos testes Python.

## Cobertura

* **Reversões:** movimentos de retorno e reversões de troca entre duas posições.
* **Movimentos repetidos:** bloqueios explícitos de movimentos já registrados.
* **Oscilações:** alternância recorrente entre posições e movimentação repetida entre banco e tabuleiro.
* **Ciclos:** permissão do primeiro fechamento, bloqueio da repetição persistente e permissão de um destino novo.
* **Identidade das unidades:** movimentos semelhantes de unidades diferentes não devem compartilhar indevidamente o histórico.
* **Mudança de estado:** um bloqueio associado a uma assinatura anterior deixa de valer quando um novo estado é registrado.
* **Histórico:** consultas de bloqueio não devem alterar os históricos.
* **Reset:** limpeza dos históricos e do último movimento.

## Arquivos

* `cpp/tests/test_anti_loop_engine.cpp`: testes nativos da engine.
* `cpp/CMakeLists.txt`: configuração do executável e registro no CTest.

## Execução

Na pasta `cpp`, configure e compile o projeto:

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

## Critério de conclusão

A suíte deve compilar e passar no CTest. A equivalência completa com o comportamento Python deve ser confirmada na validação integrada do projeto, incluindo eventuais diferenças na ordem dos motivos de bloqueio.
