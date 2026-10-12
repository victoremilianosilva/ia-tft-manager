# Validação e Equivalência Python/C++

## Objetivo

Definir como verificar que a engine C++ reproduz as regras atuais de Action Masks e AntiLoop antes de ser ativada como caminho principal.

## Princípio de referência

A implementação Python é a referência inicial. Observações documentadas podem refletir uma versão anterior do código; quando houver conflito, verificar o código e os testes atuais antes de alterar o contrato.

## Preparação de cada cenário

Cada cenário deve conter, conforme necessário:

- Tabuleiro com 28 posições, banco com 9 posições e loja com 5 posições.
- Estado econômico e estado ativo/eliminado do jogador.
- Identidade das unidades e posições ocupadas/vazias.
- Parâmetros AntiLoop.
- Histórico de estados, movimentos, bloqueios e visitas.
- Operação, resultado esperado e efeitos colaterais esperados.

As duas implementações devem receber snapshots equivalentes e históricos independentes. Não se deve executar o cenário em Python e reutilizar o estado já mutado como entrada do teste C++.

## Comparações obrigatórias

| Área | Critério |
|---|---|
| Dimensões das máscaras | Igualdade exata |
| Valores das máscaras | Igualdade elemento a elemento |
| Disponibilidade real | Mesmo resultado, separada do fallback categórico |
| Motivo AntiLoop | Mesmo motivo ou ausência de bloqueio |
| Identidade e assinatura | Mesmo conteúdo e mesma ordenação |
| Histórico | Mesmos registros e sequência |
| Bloqueios | Mesmas chaves e associações ao estado |
| Métricas | Mesmos deltas para a mesma operação |
| Consultas | Sem mutações inesperadas |
| Execução e rollback | Estado final e histórico equivalentes |
| Reset | Mesma limpeza e mesmas métricas persistentes |
| Erros e fallback | Resultado conforme o contrato explícito |

Para máscaras booleanas, comparar todas as posições. A mesma contagem de bits habilitados não prova equivalência: uma única posição diferente pode permitir uma ação inválida.

## Cenários de referência

A suíte deve cobrir pelo menos:

1. Estado inicial, banco ocupado e tabuleiro vazio.
2. Tabuleiro parcialmente ocupado e tabuleiro cheio.
3. Banco vazio.
4. Loja sem compras possíveis e limites de ouro.
5. Jogador eliminado.
6. Nenhum movimento válido e uso de fallback.
7. Histórico AntiLoop vazio.
8. Reversão normal e reversão de troca.
9. Oscilação, ciclo banco ↔ tabuleiro e ciclo geral.
10. Bloqueios explícitos com e sem mudança de estado.
11. Identidade com UUID, sem UUID e campos ausentes.
12. Índices inválidos e limites de capacidade do histórico.
13. Consultas repetidas sem efeitos colaterais.
14. Tentativa bloqueada, movimento concluído, falha, rollback e reset.
15. Falha controlada em consulta AntiLoop.

A lista detalhada de fixtures e verificações continua em `casos_referencia.md`.

## Relatório de divergências

Para cada cenário, registrar:

- Identificador do caso e entrada usada.
- Resultado Python e resultado C++.
- Primeira máscara, índice ou campo divergente.
- Motivo de bloqueio retornado por cada implementação.
- Estado e métricas antes/depois, quando aplicável.
- Erro ou fallback acionado.
- Resultado `PASS` ou `FAIL`.

O caso deve ser reproduzível isoladamente. Não usar somente uma contagem agregada de divergências.

## Critérios para declarar equivalência

A equivalência funcional só pode ser declarada quando todos os cenários obrigatórios executados passarem, todas as máscaras e motivos coincidirem, as mutações autorizadas forem equivalentes e não houver divergências conhecidas sem decisão explícita.

O desempenho deve ser medido separadamente, com os mesmos cenários e incluindo conversão de dados e custo total do fluxo. Ganho de velocidade não compensa falha de equivalência.

## Referências

- `contrato_atual.md`: referência do comportamento observado.
- `casos_referencia.md`: fixtures e casos detalhados.
- `criterios_objetivos.md`: critérios objetivos de aceitação.
- `base_desemplenho.md`: metodologia e resultados de desempenho.
- `4.5.2/`: contratos e instruções de build/testes nativos.
