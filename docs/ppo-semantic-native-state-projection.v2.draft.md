# PPO semantic native-state projection v2 — draft

## Purpose

Provide PPO with a structured, versioned projection of native game-state facts without treating the legacy flat observation offsets as the definition of those facts. The projection is an independent side input to the shared Actor/Critic latent. It is not a replacement for the legacy tensor yet.

## Source contract

- Contract: `tft.native-state-snapshot`, version 3.
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

The existing AuditSnapshot carries one strategic_state object per player, produced by TFTEngine::get_audit_snapshot from the existing ActiveCompositionManager and StrategicCommitment, plus the unified state machine direction/pivot anchors. PPO training enables the native owner pipeline; the optional JSONL audit sidecar is not required for state updates. Its independent contract is tft.strategic-owner-observation v1 and repeats episode, player, round and player-decision sequence so stale or cross-player state is rejected.

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
- Per-player projection hashes are attached to decision/next-snapshot metadata.
- Checkpoints carry `semantic_state_contract`, including source identity, catalog fingerprint, feature order, dimensions, normalizations and missing-value policy.
- The semantic encoder's final layer is zero-initialized. Historical checkpoints without semantic weights migrate through this neutral additive path, preserving old logits/value estimates at load while allowing PPO to train the new branch.
- Viewer validates the semantic contract/catalog and reconstructs the same projection for live policy inference.

## Current delivery boundary

This is an additive semantic state path, not yet a complete replacement of the historical observation schema. The legacy flat observation remains present for checkpoint compatibility and still supplies the existing item-state sub-block. In particular, this projection currently does not yet expose native strategic-owner evidence for composition direction, pairs/upgrades, pivot transitions or opportunity-cost attribution.

Therefore:
- Semantic native state is now consumed by PPO and persisted in rollouts/checkpoints.
- The full legacy-independent replay gate remains open.
- The item-state/legacy-profile migration remains open.
- A future projection version must add strategic-owner facts only after their producers, provenance, validity and synchronization contracts are explicitly published.

## Legacy producer replay gate

Trainer collection no longer calls the legacy `get_strategies()` compatibility API. That removes a Python-side diagnostic dependency, but it does not satisfy the producer-disabled replay gate: native `update_strategy()` still co-locates the economic Strategy ID selector, legacy composition-direction/focus maintenance, native composition generation, and the isolated Shadow evaluation pipeline. Disabling that entire function would also disable native generation and would invalidate the evidence needed by the current strategic path. The next safe step is to separate those responsibilities and publish their own owner snapshots before a replay can disable only the legacy producers without disabling the native owners.

## PR3 — retirada das features estratégicas legadas do caminho PPO

**Problema anterior:** o tensor plano ainda consumia StrategyInfo para one-hot ECON/FAST8/SLOWROLL, direção, core traits, fit, focus, lock, strength e sinais core/planned por candidato. A policy ainda derivava target level e reserva econômica desse one-hot, convertendo ausência em ECON por `argmax`.

**Justificativa técnica:** esses campos eram saídas de produtores estratégicos legados, não fatos observados. Mantê-los no encoder fazia a policy aprender uma política nominal fixa e mascarava a ausência de evidência. A recomendação Shadow também não pode virar rótulo de imitação.

**Responsabilidade nova:** o caminho PPO plano preserva somente os slots físicos por compatibilidade estrutural; slots estratégicos legados são tombstones zero. O side input semântico nativo continua responsável pelos fatos verificáveis. O perfil de item compartilhado usa `semantic_item_unit_profiles`, construído a partir do classificador factual e da composição ativa nativa, sem carry/core traits de StrategyInfo.

**Contrato e invariantes:** zero nesses slots significa feature descontinuada, não postura neutra; StrategyInfo não é lido por `build_observations()`; action masks e legalidade continuam independentes; recomendações, scores e confiança Shadow não são inputs nem targets PPO; ausência de composição não fabrica fit.

**Impactos:** TftEngine, Policy encoder, candidatos de compra/venda, item-target profiles, testes C++ e testes de entrada semântica. A dimensão física do vetor é preservada nesta etapa para evitar desalinhamento acidental com os leitores existentes; a semântica passa a exigir nova linhagem de treino.

**Validação:** regressões verificam que o one-hot e todos os blocos estratégicos legados são zero, enquanto custo/estrela/papel/cópias e estado factual de itens permanecem disponíveis; testes Python verificam invariância às colunas antigas de estratégia. Esta entrega não declara completa a projeção dos owners estratégicos nativos no schema PPO.
