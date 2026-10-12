# Documentação da Engine de Decisão TFT

Esta pasta documenta a migração gradual de Action Masks e consultas AntiLoop de Python para C++. A política PPO, o treinamento, o estado oficial e a execução das ações permanecem em Python.

## Comece por aqui

1. `doc_geral.md` — visão geral e limites arquiteturais.
2. `contexto.md` — contexto técnico e mapa das fontes de verdade.
3. `contrato_atual.md` — formato, dimensões e índices das máscaras atuais.
4. `contrato.md` — interface proposta entre Python e C++.
5. `anti_loop.md` — identidade, assinaturas, precedência e histórico AntiLoop.
6. `validacao_e_equivalencia.md` — plano de comparação e critérios de aprovação.

## Referência por assunto

- Dependências e chamadas: `analise_dependencias.md`.
- Aplicação autoregressiva das máscaras: `apliccao_mascaras.md`.
- Regras de movimento e validação: `regra_validacao_movimento.md`.
- Casos reproduzíveis: `casos_referencia.md`.
- Critérios objetivos: `criterios_objetivos.md`.
- Desempenho: `base_desemplenho.md`.
- Fallback, shadow, ativação e rollback: `estrategia_faallback.md`.
- Contratos do módulo nativo e build: `4.5.2/`.
- `archive/`: análises detalhadas anteriores, preservadas para consulta e rastreabilidade.

## Regras de segurança da migração

- Python continua como referência até a equivalência automatizada ser demonstrada.
- Fallback técnico não deve ser interpretado como ação disponível.
- Consultas não podem duplicar mutações de histórico.
- Não declarar teste, benchmark ou equivalência sem execução verificável.
- Não alterar `4.5.2/` como parte desta consolidação.
