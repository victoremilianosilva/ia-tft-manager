# Documentação — Engine de Decisão TFT

## Objetivo

Reduzir o custo de geração das Action Masks e das consultas AntiLoop com uma migração gradual para C++, sem transferir PPO, treinamento, estado oficial ou execução das ações para o módulo nativo.

## Limites de responsabilidade

**Python:** estado oficial da partida, ambiente, execução de ações, recompensas, política PPO e treinamento.

**C++:** cálculo de máscaras e avaliação de candidatos/consultas AntiLoop, usando snapshots explícitos e sem mutações indevidas.

**Regra principal:** a implementação Python é a referência até testes automatizados demonstrarem equivalência. Ganho de desempenho não compensa divergência funcional.

## Fluxo

1. Python prepara snapshot e histórico.
2. Implementação de decisão calcula máscaras e diagnósticos.
3. Política PPO seleciona a ação.
4. Ambiente Python valida e executa a ação.
5. Histórico oficial e métricas são atualizados conforme o resultado real.

## Critérios mínimos

- Dimensões e valores das máscaras idênticos.
- Disponibilidade real separada de fallback técnico.
- Mesmos resultados e motivos de bloqueio AntiLoop.
- Identidade de unidades e assinaturas de estado equivalentes.
- Sem efeitos colaterais indevidos em consultas.
- Atualização equivalente de histórico, reset, erros e fallback.
- Benchmark separado da verificação funcional e incluindo conversão de dados.

## Navegação

Comece por [`README.md`](README.md). Consulte `contrato_atual.md` para o formato vigente, `contrato.md` para a interface nativa, `anti_loop.md` para regras AntiLoop, `casos_referencia.md` para cenários, `validacao_e_equivalencia.md` para o processo de validação, `base_desemplenho.md` para desempenho e `estrategia_faallback.md` para ativação gradual e rollback.

A pasta `4.5.2/` contém contratos e instruções específicas do módulo nativo e não deve ser alterada por esta limpeza.
