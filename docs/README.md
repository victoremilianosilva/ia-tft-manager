# Documentação técnica

Esta documentação descreve o código presente no repositório, separando arquitetura, contratos e funcionalidades. Os diagramas do viewer foram movidos para [assets](assets/).

### Gate 8 — Stage 0 projection design

- [Stage 0 Observation Projection Design v1](stage0-observation-projection-design.v1.draft.md) — initial semantic projection groups, Actor/Critic boundaries, identity and review criteria.
- [Observation Projection Manifest v1 (machine-readable)](../spec/observation-projection-manifest.v1.draft.json) — 77-field inventory derived from the approved semantic consumer matrix; not yet a frozen tensor layout.
- [Implementation Issue Roadmap v1](implementation-issue-roadmap.v1.draft.md) — ordered issue dependencies and staged execution plan.

## Fonte normativa da arquitetura canônica

Para decisões de arquitetura e implementação da nova linhagem, use primeiro os contratos aprovados e os artefatos versionados abaixo. Os documentos de comportamento atual/legado continuam úteis como evidência histórica, mas não substituem esses contratos.

- [Observation Schema v1 (machine-readable)](../spec/observation-schema.v1.draft.json), histórico imutável da linhagem v1, com mapas de origem, migração e disponibilidade.
- [Observation Schema v2 (machine-readable proposal)](../spec/observation-schema.v2.draft.json) — proposta de identidade tipada; ainda não aprovada para runtime.
- [Sequence Namespace Registry v2](../spec/sequence-namespace-registry.v2.draft.json) — namespaces observados versus propostos, owners, escopos e disponibilidade.
- [Decision Identity v2 hash vectors](../spec/decision-identity-v2-hash-vectors.draft.json) — vetores RFC 8785/SHA-256 sintéticos para validação determinística.
- [Observation identity v1→v2 crosswalk](observation-identity-v1-v2-crosswalk.md) — migração sem reinterpretar hashes ou artefatos históricos.
- [Observation Tensor Projection Contract v1 — Design Requirements](observation-tensor-projection-contract.v1.draft.md)
- [Observation Projection Consumer Matrix v1 — Draft](observation-projection-consumer-matrix.v1.draft.md)
- [Structured Entity and Temporal Evidence Contract v1 — Draft](observation-structured-entity-temporal-contract.v1.draft.md) — entity identity, ownership, collection completeness, temporal scope and schema gaps before tensor encoding.
- [Structured Entity Producer Evidence Audit — Identity Slice v1 — Draft](observation-structured-entity-producer-audit.v1.draft.md) — native UnitInstance UUID generation is implemented; canonical cross-episode identity and full lifecycle acceptance remain unverified.
- [Native State Snapshot Contract v1 — Draft](native-state-snapshot-contract.v1.draft.md) — binds existing board/bench/shop, economy and item-inventory facts to the exact native observation/mask snapshot and carries per-player records into rollout sidecar metadata; not an Actor/Critic tensor contract.
- [Shared Champion Pool Snapshot Contract v1 — Draft](shared-champion-pool-snapshot-contract.v1.draft.md) — publishes catalog-ordered shared-pool counts with the same Engine/episode/decision identity; remains non-tensor audit metadata.
- [Structured Item Ownership Snapshot Contract v1 — Draft](structured-item-ownership-snapshot-contract.v1.draft.md) — preserves component/inventory multiplicity and active unit equipment ownership without fabricating physical item-instance IDs.
- [Observation Schema v2 Identity Field Semantics Reconciliation](observation-schema-v2-identity-field-semantics-reconciliation.v1.draft.md) — separates authoritative game match, Engine episode scope, Viewer session, native episode counter and player seat.
- [Engine Identity Scope Reconciliation](engine-identity-scope-reconciliation.v1.draft.md) — defines the semantic need for Engine-instance scope plus episode without choosing a runtime ID algorithm.
- [Structured Entity Audit Coverage Status](observation-structured-entity-audit-coverage-status.v1.draft.md) — consolidated status for 17 entity kinds and 31 field-family rows; unavailable fields remain unavailable.
- [Elimination Item Terminal Policy — Decision Proposal v1](elimination-item-terminal-policy-proposal.v1.draft.md) — decisão de domínio aceita: aposentadoria/descarte terminal, sem transferência ou redistribuição; implementação e testes continuam bloqueados até Gate 8.
- [Gates 1–7 Integrated Readiness Review](gates-1-7-integrated-readiness-review.v1.draft.md) — evidência documental versus aceitação runtime e bloqueios da Gate 8.
- [Identity and GEP Six-Workstream Closeout](identity-and-gep-six-workstream-closeout.v1.draft.md) — fechamento documental dos seis itens de identidade, call sites, correlação GEP, Schema v2 e issue #346; não equivale a aceitação runtime.
- [Final Documentary Reconciliation — Gates 1–7 v1](gates-1-7-final-documentary-reconciliation.v1.draft.md) — consolidated closeout for identity/lifecycle, GEP-to-PPO correlation, 17 structured entity kinds, elimination item policy, CSV traceability and final Gate 1–7 status.
- [Python Identity/Test-Hook Call-Site Inventory](python-identity-test-hook-callsite-inventory.v1.draft.md) and [C++ Identity/Test-Hook Caller Audit](cpp-identity-test-hook-caller-audit.v1.draft.md) — tracked source/test call-site inventories and explicit scope limitations.
- [Decision Identity and Mask Correlation Contract v1 — Design Proposal](decision-identity-mask-correlation-contract.v1.draft.md) — rationale e invariantes de correlação entre observação, masks, critic, rollout e replay.
- [Decision Identity Schema v2 — Versioning Boundary and Migration Design](decision-identity-schema-v2-design.v1.draft.md) — proposta para versionar namespaces tipados sem alterar o schema v1 histórico; ainda aguarda revisão/aprovação documental.
- [Action / Mask Contract v1](action-mask-contract.v1.draft.md) — especificação documental aprovada; execução/aceitação runtime pendente.
- [Reward Contract v1](reward-contract.v1.draft.md) — especificação documental aprovada; migração runtime pendente.
- [PPO Architecture and Checkpoint Contract v1](ppo-checkpoint-contract.v1.draft.md) — especificação documental aprovada; loader/migração runtime pendentes.
- [Strategic Ownership and Integration Contract v1](strategic-ownership-integration.v1.draft.md) — ownership canônico aprovado; integração executável pendente.
- [Economic Evidence and Progression Contract v1](economic-evidence-and-progression-contract.v1.draft.md), [Strategic Action Candidate Contract v1](strategic-action-candidate-contract.v1.draft.md), [Unit Ownership and Star Progress Contract v1](unit-ownership-and-star-progress-contract.v1.draft.md) e [Strategic Shadow Integrated Replay Contract v1](strategic-shadow-integrated-replay-contract.v1.draft.md) — especificações documentais aprovadas; execução pendente.
- [PPO Evaluation Protocol v1](ppo-evaluation-protocol.v1.draft.md) — protocolo documental aprovado; avaliação executável pendente.
- [Legacy strategic consumer and shutdown matrix](legacy-strategic-consumer-migration-matrix.md) — inventário estático consolidado, destinos por consumidor, ordem de migração e critérios de desligamento; não autoriza remoção do legado.

**Regra de leitura:** contratos aprovados definem semântica e autoridade futuras; documentação de código descreve o comportamento observado no snapshot auditado; issues registram lacunas e trabalho de aceitação. Nenhuma aprovação documental libera implementação antes do Gate 8 e autorização explícita.

## Comece por aqui

- [Limite de integração live Overwolf/GEP](overwolf-live-state-integration-boundary.md) — ownership entre captura GEP, estado canônico, importação nativa, inferência PPO e evidência necessária para declarar integração live.
- [GEP Match ID Source Path and Lifecycle Audit](gep-match-id-source-path-and-lifecycle-audit.v1.draft.md) — path exato do match ID, normalização, sessão/revisão do snapshot manager e evidência ainda pendente de captura real.

- [Arquitetura geral](architecture.md) — componentes e fluxo de dados.
- [Engine de lobby](lobby-engine.md) — ciclo de partida e estado dos oito jogadores.
- [Catálogo e instâncias de unidades](units-catalog.md) — definições estáticas, cópias, estrelas e pool.
- [Economia e loja](economy-shop.md) — ouro, XP, juros, reroll e ofertas.
- [Ações, máscaras e anti-loop (histórico)](decisions-masks-antiloop.md) — snapshot do catálogo antigo de sete ações; não normativo. Para a nova linhagem, consulte o [Action / Mask Contract v1](action-mask-contract.v1.draft.md).
- [Combate](combat.md) — entradas, simulação e eventos.
- [Recompensas e observações](rewards-observations.md) — sinais de treino e estado observado.
- [Estratégia, sinergias e posicionamento](strategy-synergies-positioning.md).
- [Treinamento PPO](rl-training.md) — coleta, rollout, otimização e checkpoints.
- [Ambientes Python e bindings](python-environments.md).
- [Viewer desktop](viewer.md) — interface de avaliação e limites reais.
- [Logs, sessões e replay](sessions-logs-replay.md).
- [Avaliação e ferramentas](evaluation-tooling.md).
- [Build, testes e CI](build-and-tests.md).
- [Contratos e dados](contracts-and-data.md).

## Princípios usados nesta documentação

1. A engine C++ é a fonte de verdade para as regras da partida e os resultados das ações.
2. Python/PyTorch controla treinamento, coleta de experiências, inferência e ferramentas de avaliação.
3. As dimensões de ações, observações e máscaras são contratos entre policy e engine; mudanças precisam ser validadas em conjunto.
4. Diagramas de interface são wireframes, não evidência de que todos os dados ilustrados já são fornecidos pela engine.
5. Uma funcionalidade descrita aqui não é considerada testada só por estar documentada. Veja os comandos e limitações em [build e testes](build-and-tests.md).

## Entradas principais

- Treinamento: `trainer.py`
- Policy: `policy.py`
- PPO: `ppo.py`
- Buffer: `rollout.py`
- Adaptador nativo: `cpp_lobby_env.py`
- Engine: `cpp/include/lobby/TftEngine.hpp` e implementações em `cpp/src/`
- Viewer: `viewer/main.py`, `viewer/session.py` e `viewer/player_logs.py`

- [Remaining Identity, Ownership, Rollout and Gate Reconciliation](remaining-identity-rollout-gate-reconciliation.v1.draft.md) — current consolidated source evidence for Engine scope, UnitInstance value semantics, wrapper/RolloutBuffer correlation, Schema v2 dispositions, GEP deferral and Gates 1–7 readiness.

- [Gate 8 Preflight and Staged Implementation Plan](gate8-preflight-and-staged-implementation-plan.v1.draft.md) — integrated authorization checklist, closed design decisions, accepted runtime gaps and dependency-ordered implementation stages; does not grant authorization.

- `observation-schema-v2-identity-boundary.v1.draft.md` — Stage 1 executable identity/provenance/cardinality contract for Observation Schema v2.

- [Stage 1 — Structured Entity Producer Audit Reconciliation](stage1-structured-entity-producer-audit-reconciliation.v1.draft.md) — consolidated Stage 1 item-D source audit across 17 entity kinds, 31 field families and the 223-path Schema v2 crosswalk; paired with the bounded native-state sidecar producer in PR #455.

- [Stage 1 — Integrated Contract and Runtime Evidence Gate](stage1-integrated-contract-runtime-evidence-gate.v1.draft.md) — consolidated acceptance ledger for PRs #425–#452, separating merged boundary evidence from outstanding replay, producer, identity, checkpoint and evaluation gates.
