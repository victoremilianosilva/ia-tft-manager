# Documentação da migração da engine de decisão

Esta documentação descreve a migração gradual das operações de Action Masks e AntiLoop para C++, mantendo PPO, treinamento e execução real das ações em Python.

## Mapa dos documentos

- `doc_geral.md`: visão geral e limites arquiteturais.
- `contexto.md`: contexto técnico e arquitetura identificada.
- `contrato_atual.md`: comportamento atual observado.
- `contrato.md`: contrato de integração Python/C++.
- `analise_dependencias.md`: dependências e fluxo de chamadas.
- `anti_loop.md`: regras, precedência, identidade, histórico e efeitos colaterais AntiLoop.
- `validacao_e_equivalencia.md`: método de comparação e critérios de equivalência.
- `casos_referencia.md`: cenários detalhados para testes comparativos.
- `criterios_objetivos.md`: critérios objetivos de aceitação.
- `base_desemplenho.md`: medições e metodologia de desempenho.
- `estrategia_faallback.md`: fallback e rollback.
- `4.5.2/`: contratos específicos do módulo nativo, convenções, testes e instruções de build.

## Regra de segurança da migração

A implementação Python continua sendo a referência até que testes comparativos demonstrem equivalência. Não declarar equivalência nem ganho de desempenho sem executar e verificar os testes correspondentes.
