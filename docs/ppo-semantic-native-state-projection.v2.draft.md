# PPO semantic native-state projection v2 — draft

## Purpose

Provide PPO with a structured, versioned projection of native game-state facts without treating the legacy flat observation offsets as the definition of those facts. The projection is an independent side input to the shared Actor/Critic latent. It is not a replacement for the legacy tensor yet.

## Source contract

- Contract: `tft.native-state-snapshot`, version 4.
- Producer: `TFTEngine::get_audit_snapshot`.
- Namespace: `tft.engine.observation-snapshot`.
- Correlation: Engine instance, episode, snapshot sequence, player decision sequence and player ID are validated before projection.
- Champion identities are resolved through the active native catalog map (`apiName -> champion_internal_id`). The catalog fingerprint and vocabulary size are bound into the checkpoint contract.

## Projected feature layout

The numeric block has 525 float32 features in v2. The original 269 factual features retain their order and meaning; strategic owner and copy-progress features are appended through an explicit v1-to-v2 mapping.

| Block | Width | Meaning |
|---|---:|---|
| Global facts | 21 | Existing 17 facts plus active-composition, direction, pivot and opportunity-cost availability |
| Board | 28 × 12 | Existing six facts plus composition/core membership, direction/pivot references and copy/upgrade progress |
| Bench | 9 × 12 | Same slot-local facts |
| Shop | 5 × 12 | Candidate slot facts plus owned-copy and upgrade context |

Champion IDs are a separate int64 tensor with 42 stable slots and a shared 16-dimensional embedding. ID zero is reserved for empty or unknown identities. Unknown catalog names are not mapped to a guessed ID; the slot's validity feature remains false. The trait count is derived from the snapshot's static catalog `trait_names` only; as documented by the native producer, it does not include item-granted traits.

Normalizations are explicit in `semantic_observation.py` and versioned by this contract. Missing optional placement/opponent values have separate validity/presence features. Invalid required source fields, non-finite values, identity mismatch, wrong slot counts, or incompatible producers fail closed.

## Strategic owner source

The existing AuditSnapshot carries one strategic_state object per player, produced by TFTEngine::get_audit_snapshot from the existing ActiveCompositionManager and StrategicCommitment, plus the unified state machine direction/pivot anchors. PPO training enables the native owner pipeline; the optional JSONL audit sidecar is not required for state updates. Its independent contract is tft.strategic-owner-observation v2 and repeats episode, player, round and player-decision sequence so stale or cross-player state is rejected.

The semantic tensor receives only membership/reference features, not recommendation scores or confidence. Pair and upgrade progress is produced once by the existing C++ UnitCopyProgress helpers from the exact board/bench units and carried in the same strategic_state snapshot. Python only projects that native result; it does not reimplement copy/upgrade rules. Shop offers are not counted as owned copies. Four global validity values distinguish unavailable owners from valid empty membership.

Opportunity cost remains explicitly unavailable in this snapshot: PR2 found no validated per-action producer published here. The availability flag is false and no numeric cost is fabricated. This remains an integration gap for the full #286 acceptance criteria.

## Exclusions

The semantic projection does not consume:
- Legacy Strategy ID or strategy one-hot.
- Legacy composition direction/focus/lock.
- Shadow recommendation, score or confidence.
- Unverified action-candidate rankings.
- Legacy flat observation offsets.

No strategy score or confidence is promoted to a PPO target or feature.

## PPO integration

- Trainer projects the exact native player rows for the decision observation and the next observation.
- Actor and Critic share the semantic encoder output; Critic still receives the exact action-mask side input independently.
- RolloutBuffer stores the numeric and categorical semantic rows alongside the same transition; PPO minibatches and final bootstrap use the matching semantic row.
- Per-player projection hashes and the full semantic identity (Engine, episode, snapshot sequence, player decision sequence, player, round and lobby) are attached to decision/next-snapshot metadata and validated against the exact native snapshot before sampling/bootstrap.
- RolloutBuffer rejects identified transitions whose semantic row identity, projection hash or contract lineage is missing/divergent; minibatch replay carries the same identity/hash alongside the indexed semantic tensors.
- Checkpoints carry `semantic_state_contract`, including source identity, catalog fingerprint, feature order, dimensions, normalizations and missing-value policy.
- The semantic encoder's final layer is zero-initialized. Historical checkpoints without semantic weights migrate through this neutral additive path, preserving old logits/value estimates at load while allowing PPO to train the new branch.
- Viewer validates the semantic contract/catalog and reconstructs the same projection for live policy inference.

## Current delivery boundary

This is an additive semantic state path, not yet a complete replacement of the historical observation schema. The legacy flat observation remains present for checkpoint compatibility and still supplies the existing item-state sub-block. The v2 projection now exposes active-composition membership/core, direction and pivot references, plus native copy/upgrade progress. Opportunity-cost attribution remains unavailable because no validated per-action producer is published.

Therefore:
- Semantic native state is now consumed by PPO and persisted in rollouts/checkpoints.
- The full legacy-independent replay gate remains open.
- The item-state/legacy-profile migration remains open.
- The remaining semantic gaps are per-action opportunity-cost evidence and a complete producer-disabled replay. The retired zero-only slots have now been removed from the flat observation layout as a coordinated C++/Policy change. The remaining flat blocks are still live positional inputs: board geometry for the CNN, factual global/trait/capacity/action-memory features, item inventory/recipe/target records, item-target compatibility matrices, pending-anvil options and per-candidate action features. These are not tombstones and must not be deleted until each has a structured producer/consumer replacement.

## Legacy producer replay gate

Trainer collection no longer calls the legacy `get_strategies()` compatibility API. That removes a Python-side diagnostic dependency, but it does not satisfy the producer-disabled replay gate: native `update_strategy()` still co-locates the economic Strategy ID selector, legacy composition-direction/focus maintenance, native composition generation, and the isolated Shadow evaluation pipeline. Disabling that entire function would also disable native generation and would invalidate the evidence needed by the current strategic path. The next safe step is to separate those responsibilities and publish their own owner snapshots before a replay can disable only the legacy producers without disabling the native owners.

## PR3 — retirada das features estratégicas legadas do caminho PPO

**Problema anterior:** o tensor plano ainda consumia StrategyInfo para one-hot ECON/FAST8/SLOWROLL, direção, core traits, fit, focus, lock, strength e sinais core/planned por candidato. A policy ainda derivava target level e reserva econômica desse one-hot, convertendo ausência em ECON por `argmax`.

**Justificativa técnica:** esses campos eram saídas de produtores estratégicos legados, não fatos observados. Mantê-los no encoder fazia a policy aprender uma política nominal fixa e mascarava a ausência de evidência. A recomendação Shadow também não pode virar rótulo de imitação.

**Responsabilidade nova:** o caminho PPO plano preserva somente os slots físicos por compatibilidade estrutural; slots estratégicos legados são tombstones zero. O side input semântico nativo continua responsável pelos fatos verificáveis. O perfil de item compartilhado usa `semantic_item_unit_profiles`, construído a partir do classificador factual e da composição ativa nativa, sem carry/core traits de StrategyInfo.

**Contrato e invariantes:** zero nesses slots significa feature descontinuada, não postura neutra; StrategyInfo não é lido por `build_observations()`; action masks e legalidade continuam independentes; recomendações, scores e confiança Shadow não são inputs nem targets PPO; ausência de composição não fabrica fit.

**Impactos:** TftEngine, Policy encoder, candidatos de compra/venda, item-target profiles, testes C++ e testes de entrada semântica. A dimensão física do vetor é preservada nesta etapa para evitar desalinhamento acidental com os leitores existentes; a semântica passa a exigir nova linhagem de treino.

**Validação:** regressões verificam que o one-hot e todos os blocos estratégicos legados são zero, enquanto custo/estrela/papel/cópias e estado factual de itens permanecem disponíveis; testes Python verificam invariância às colunas antigas de estratégia. Esta entrega não declara completa a projeção dos owners estratégicos nativos no schema PPO.

## PR5 — alinhamento semântico de sampling, value, replay e inferência

**Problema anterior:** o Trainer gerava identidade/hash por projeção, mas o RolloutBuffer armazenava somente os tensores numéricos/categóricos. A igualdade de shape não provava que cada linha semântica pertencia à mesma decisão. O avaliador pareado de checkpoints também chamava a Policy sem o side input semântico.

**Justificativa técnica:** uma linha de estado estratégica pode ter a mesma dimensão de outra linha e ainda pertencer a outro jogador, episódio, round ou versão de owner. O Critic/bootstrap e o replay precisam avaliar a mesma decisão correlacionada que o Actor amostrou.

**Nova responsabilidade:**
- semantic_observation.py vincula o hash à identidade nativa e à proveniência dos owners, incluindo IDs/versões de composição, direção, pivot e sequência de contexto.
- Trainer valida projeção, identidade e hash tanto para o snapshot de decisão quanto para o snapshot de bootstrap.
- RolloutBuffer valida a correlação semântica antes de persistir a transição e preserva identidade/hash nos minibatches.
- Viewer e avaliação pareada usam a mesma projeção nativa v2; avaliação sem contexto semântico é rejeitada.

**Contrato e invariantes:** tft.strategic-owner-observation v2 é a origem estratégica. A sequência de decisão por jogador não é confundida com a sequência global do snapshot. Missing, unavailable e validade falsa continuam distintos de zero observado. Recomendações, scores e confiança Shadow não entram no Actor/Critic nem em reward.

**Impactos:** semantic_observation.py, trainer.py, rollout.py, viewer/session.py, scripts/evaluate_checkpoints.py, testes de projeção/replay/inferência e a linhagem de checkpoint. O contrato semântico de checkpoint muda de hash; checkpoints anteriores continuam baselines imutáveis e exigem o fluxo explícito de warm-start.

**Validação:** testes de hash sensível à proveniência mesmo quando o tensor é idêntico; rejeição de identidade/hash cruzado; preservação da identidade/hash em minibatches; e inferência de checkpoint com o side input semântico obrigatório.

**Limites:** esta entrega não declara concluído o replay com produtores legados desligados, a atribuição de custo de oportunidade nem a remoção física dos tombstones do tensor plano. Esses pontos permanecem abertos até que o consumidor posicional remanescente seja migrado e a prova integrada seja executada.


## PR6 — migração dos cinco grupos de consumidores para estado semântico nativo

**Problema anterior:** CNN do board, encoder global, traits, candidatos, perfis de alvo, inventário, receitas, compatibilidade e anvil ainda dependiam de fatias posicionais do vetor PPO. Isso acoplava a política a offsets e deixava o snapshot nativo sem autoridade única para os dados consumidos.

**Justificativa técnica:** cada consumidor recebe campos nomeados derivados do mesmo snapshot nativo da decisão, com identidade, sequência, proveniência e hash preservados em sampling, avaliação, value/bootstrap, rollout, replay e inferência. A migração não fabrica fatos nem reconstrói dados a partir de recomendações.

**Nova responsabilidade implementada:**
- **Board/CNN:** 28 entidades semânticas em ordem row-major 4x7; a CNN recebe ocupação, custo, estrela, itens equipados e contagem de traits.
- **Encoder global:** fatos globais, identidade de campeões e identidades de traits com buckets SHA-256 estáveis e embeddings próprios.
- **Capacidade/memória:** snapshot nativo v4 publica capacidade de board/bench, ações no round e idade de movimento por slot.
- **Candidatos e alvos:** compra/venda/posicionamento consomem entidades de bench/shop; alvos de item consomem perfis nativos board/bench com role classifier, posição, AD/AS/HP/armadura/resistência mágica e contagem de itens.
- **Itens:** snapshot nativo publica componentes, inventário, features canônicas de itens/receitas e matrizes de compatibilidade por alvo, usando ItemEngine, catálogo e perfis nativos.
- **Anvil:** pendência, sequência, tipo e nove opções estruturadas são projetados a partir da Engine; o scorer recebe features de opção e flags explícitas de componente/item completo.
- **Rollout/replay:** blocos semânticos nomeados são reconstruídos da mesma linha numérica versionada; RolloutBuffer.add rejeita divergência entre blocos nomeados e a projeção persistida.
- **Inferência/avaliação:** trainer, avaliação de checkpoints e paired evaluator fornecem a mesma projeção semântica à Policy.
- **Checkpoint:** contrato semântico v6 e warm-start v2→v6 explícito. A migração preserva campos antigos compatíveis, inicializa campos novos e reinicia pesos/otimizador semânticos e colunas de consumidores reinterpretadas.

**Contrato e invariantes:**
- Projeção semântica v6: 52 fatos globais, 42 entidades com 39 features cada (12 fatos de entidade, 17 atributos de alvo e 10 IDs de trait normalizados), além de blocos item/anvil nomeados.
- Hash de cada decisão cobre identidade completa, proveniência estratégica, traits, inventário, componentes, itens equipados, fingerprint do catálogo de itens, sequência/tipo/opções de anvil e valores projetados.
- Campos ausentes, inválidos, stale ou desalinhados falham fechados.
- PPO permanece a política aprendida. GAE, RolloutBuffer, replay e action masks permanecem preservados; Engine masks continuam sendo a autoridade de legalidade.
- Recomendações estratégicas não são labels de imitação nem substituem a política aprendida.

**Validação ainda necessária antes de concluir #286/#293:**
- Executar e corrigir toda a CI C++/Python/native após a ampliação do snapshot e do contrato v6.
- Confirmar end-to-end sampling, evaluate_actions, value/bootstrap, minibatches, replay, paired evaluation e inferência com os produtores legados desligados.
- Auditar que nenhum caminho nativo de produção chama a Policy sem semantic_state v6.
- Remover os blocos posicionais aposentados do vetor PPO depois da prova end-to-end, preservando apenas o transporte factual necessário para interfaces externas.

**Status:** os cinco grupos de consumidores foram migrados no código do PR; a validação integrada e a remoção física dos blocos posicionais ainda são gates obrigatórios. Manter Draft e não fechar #286/#293 até CI verde e prova integrada.