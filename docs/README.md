# Documentação técnica

Esta documentação descreve o código presente no repositório, separando arquitetura, contratos e funcionalidades. Os diagramas do viewer foram movidos para [assets](assets/).

## Fonte normativa da arquitetura canônica

Para decisões de arquitetura e implementação da nova linhagem, use primeiro os contratos aprovados e os artefatos versionados abaixo. Os documentos de comportamento atual/legado continuam úteis como evidência histórica, mas não substituem esses contratos.

- [Observation Schema v1 (machine-readable)](../spec/observation-schema.v1.draft.json), com mapas de origem, migração e disponibilidade.
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
