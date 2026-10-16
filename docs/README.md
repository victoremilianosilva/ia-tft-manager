# Status atual da migração C++ (2026-10-15)

O escopo do projeto evoluiu além da migração inicial de Action Masks/AntiLoop: agora existe também uma lobby nativa `tft_engine`, integração com `CombatEngine`, observações e recompensas. Isso **não** significa paridade total. A referência Python e os critérios de equivalência continuam valendo; a auditoria atual está em `CPP_STAGE4_COMBAT_REWARD_OBSERVATION_AUDIT.md`.

O replay cruzado é executado com bindings nativos obrigatórios no CI. Ele compara estado público, recompensas e campos estáveis das observações, mas ainda não cobre um snapshot inicial integralmente controlado, combate real comparável, loja/traits idênticos ou todas as recompensas terminais. A regra de fallback descrita neste documento era válida durante a migração; em 2026-10-16 o backend Python de jogo foi removido. Isso não constitui, por si só, prova de paridade integral.

---

# Documentação da Engine de Decisão TFT

Os documentos abaixo foram escritos durante a fase inicial da migração de Action Masks/AntiLoop e alguns descrevem a arquitetura planejada naquela época. Para a arquitetura executada atualmente, consulte também `cpp/include/lobby/TftEngine.hpp`, `cpp/src/lobby/TftEngine.cpp`, `cpp/bindings/tft_engine_bindings.cpp` e a auditoria da Etapa 4. Quando houver divergência entre documento histórico e código atual, confirme o comportamento nos testes e atualize o contrato antes de declarar paridade.

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

- A referência de regras Python foi removida; a suíte atual valida a implementação C++ diretamente, sem declarar por isso paridade integral com todos os estados históricos.
- Fallback técnico não deve ser interpretado como ação disponível.
- Consultas não podem duplicar mutações de histórico.
- Não declarar teste, benchmark ou equivalência sem execução verificável.
- Não alterar `4.5.2/` como parte desta consolidação.


## Atualização de paridade controlada — 2026-10-15

O replay Python/C++ agora controla a formação das unidades para comparar uma luta real e seus componentes de recompensa. A execução atual corrige a observação de jogadores eliminados e o score de posicionamento do ambiente Python. A paridade integral ainda depende de fixtures adicionais de empate, eliminações/ranking terminal e de uma decisão explícita sobre sincronização dos RNGs. Consulte CPP_STAGE4_COMBAT_REWARD_OBSERVATION_AUDIT.md.


## Atualização de arquitetura — 2026-10-16

A engine de jogo ativa é exclusivamente C++ (cpp/src/lobby/TftEngine.cpp). O arquivo
cpp_lobby_env.py é um adaptador de interface usado pelo PPO; não contém as regras
de jogo. Foram removidos a factory engine_backend.py, a variável de seleção
TFT_ENGINE_BACKEND e os módulos Python de regras que já tinham APIs/implementações
nativas correspondentes.

O PPO, a policy, o rollout, o treinamento, a avaliação de checkpoints e o visualizador
continuam em Python por serem infraestrutura de aplicação, não um segundo backend
de jogo. Os testes de unidade nativos continuam em cpp/tests/; testes Python que
cobriam contratos de aplicação agora utilizam os bindings C++ quando aplicável.
Testes sem substituto executável adequado foram removidos em vez de manter imports
da engine de jogo eliminada.

Esta remoção não encerra, por si só, as lacunas de paridade histórica descritas nas
auditorias abaixo. Os documentos e análises arquivados são mantidos para rastreabilidade;
onde citem a antiga engine Python, devem ser lidos como evidência histórica.
