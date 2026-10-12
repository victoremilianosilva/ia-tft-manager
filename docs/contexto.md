# Contexto Técnico — Migração da Engine de Decisão para C++

## Objetivo

Migrar gradualmente para C++ os gargalos de geração de Action Masks e validação AntiLoop, mantendo PPO, treinamento, estado oficial e execução das ações em Python. A implementação Python continua sendo a referência até a equivalência ser comprovada por testes automatizados.

## Arquitetura

- `ai/ActionMaskManager.py`: gera máscaras e valida candidatos.
- `ai/AntiLoopManager.py`: aplica proteções AntiLoop e mantém histórico/métricas.
- `lobby/TFTLobby.py`: integra máscaras ao fluxo de decisão.
- `env.py`: valida e executa ações e atualiza o estado oficial.
- `policy.py` e `trainer.py`: política PPO e treinamento.
- C++/pybind11: candidato para cálculo de máscaras e consultas de decisão, sem executar ações nem assumir o estado oficial.

## Contrato de ação conhecido

As dimensões compostas documentadas são `[7, 5, 9, 28, 28, 28]`: 7 tipos, 5 posições da loja, 9 posições de reserva e índices de tabuleiro de 28 posições. Máscaras condicionais e indicadores de disponibilidade devem seguir o contrato atual; fallback técnico não significa que exista uma ação real válida.

## Regras de trabalho

1. Trabalhar um item do roadmap por vez.
2. Não alterar comportamento sem evidência e teste comparativo.
3. Não declarar testes ou equivalência sem executá-los.
4. Preservar dimensões, índices, identidade de unidades, precedência AntiLoop, histórico, métricas, reset, erros e fallback.
5. Consultas de candidatos não podem ser confundidas com execução nem atualizar o histórico oficial indevidamente.
6. Medir desempenho incluindo conversão Python/C++ e custo total do fluxo.

## Fontes de referência

- Visão geral e navegação: `README.md`.
- Contrato atual das máscaras: `contrato_atual.md`.
- Interface Python/C++: `contrato.md`.
- Dependências e fluxo de chamadas: `analise_dependencias.md`.
- Aplicação das máscaras à política: `apliccao_mascaras.md`.
- Validação de movimentos: `regra_validacao_movimento.md`.
- Regras AntiLoop consolidadas: `anti_loop.md`.
- Casos de teste: `casos_referencia.md`.
- Critérios de equivalência: `criterios_objetivos.md` e `validacao_e_equivalencia.md`.
- Desempenho: `base_desemplenho.md`.
- Fallback e rollback: `estrategia_faallback.md`.
- Contratos nativos e build: `4.5.2/` (mantida sem alterações por esta rotina).

Os documentos arquivados em `archive/` são material de apoio histórico. Quando houver divergência, confirme o comportamento no código e nos testes atuais; não trate observações históricas como contrato automaticamente.
