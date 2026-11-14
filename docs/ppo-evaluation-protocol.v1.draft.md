# PPO Evaluation Protocol v1

**Status:** approved documentary specification; executable evaluation and training acceptance remain blocked until Gate 8.  
**Scope:** experimental protocol for future PPO lineages after Gate 8.  
**Non-goals:** this document does not authorize training, retraining, checkpoint mutation, PPO/Engine changes, Viewer changes, or runtime migration.

## 1. Decision principles

1. Compare policies only when their observation, action/mask, reward, catalog/rules, and architecture contracts are identified and semantically compatible.
2. Keep historical checkpoints and their original manifests immutable. New experiments write to new, versioned run directories; never overwrite a baseline.
3. Prefer paired evaluation: candidate and baseline encounter the same lobby conditions and seed schedule, with seat assignment rotated to reduce seat bias.
4. Separate training, validation, and final test data by seed/episode identity. The final test set is not used for tuning, threshold selection, or repeated model selection.
5. A higher internal reward is not evidence of better match outcomes. Report outcome, behavior, legality, stability, and uncertainty separately.
6. PPO actions, baseline recommendations, contextual Shadow proposals, and Shadow executor resolutions are distinct data sources. Shadow output is not an imitation target or correctness label.

## 2. Experiment and lineage identity

Every run must emit a machine-readable manifest containing:

- experiment ID, parent/baseline run ID, purpose, and pre-registered hypothesis;
- repository commit, build/compiler identity, Engine build identity;
- catalog fingerprint, rules/patch identity, environment/opponent configuration;
- Observation Schema ID/version/hash and projection identity;
- Action Contract and mask contract ID/version/hash;
- Reward Contract ID/version/hash;
- PPO architecture/encoder/head identity and policy configuration;
- training configuration, hyperparameters, optimizer/scheduler configuration, update horizon;
- global seed, per-lobby seed derivation, Python/NumPy/Torch/Engine RNG seeds and available RNG states;
- dataset split IDs, evaluation seed list, seat-rotation schedule;
- checkpoint artifact path/hash and whether it is latest, best, or immutable baseline;
- evaluation code version and report/artifact hashes.

Evaluation must fail closed when required contract hashes are absent, malformed, or incompatible. A caller-supplied Policy object is not proof that the checkpoint was loaded under the expected semantic contracts.

### 2.1 Lineage classes

Label each experiment explicitly as one of:

- **from-scratch retraining** — new initialization and optimizer state;
- **controlled weight transfer** — only explicitly mapped compatible tensors are transferred, with a written mapping and provenance;
- **fine-tuning** — a declared parent checkpoint and compatible semantics, with optimizer/scheduler reset-or-resume policy stated;
- **evaluation-only** — no training or parameter mutation.

Do not infer transfer/resume compatibility from tensor shape alone. A new Observation Schema or Reward Contract normally creates a distinct semantic lineage. Legacy checkpoints remain immutable baselines and are not required to load into the new architecture.

## 3. Seed and paired-lobby protocol

- Define a master experiment seed and derive independent deterministic seeds for each lobby/episode and each RNG domain.
- Record the derivation algorithm and all resulting seeds. Do not silently map missing seeds to zero.
- Candidate and baseline use paired lobby seeds and identical environment/opponent settings.
- Rotate player seats across paired runs using a deterministic schedule; do not keep candidate slots fixed at {0,1,2,3}.
- Keep RNG streams independent between lobbies and record whether engines intentionally share or do not share a seed.
- Record failed, incomplete, invalid, and retried episodes; retries retain their original identity and are reported rather than silently replacing outcomes.
- Freeze the seed schedule before evaluating the final test set.

The existing paired-seed evaluator is a useful starting point, but caller-supplied fixed candidate slots are insufficient without deterministic seat rotation. Evaluation must also validate semantic contract hashes before running.

## 4. Data splits and model selection

| Split | Permitted use | Prohibited use |
|---|---|---|
| Train | Gradient updates and training diagnostics | Final performance claims |
| Validation | Hyperparameter/model selection, early stopping, ablation selection | Final promotion claim |
| Test | One-shot final comparison after choices are frozen | Tuning, repeated selection, threshold adjustment |

Split by episode/seed identity and, where relevant, by scenario family or patch/catalog identity to reduce leakage. Publish split manifests and hashes. If the environment changes materially, report a separate evaluation domain rather than pooling incompatible results.

## 5. Training and checkpoint discipline

- Record total updates and the full scheduler horizon. Reject configurations where the intended run ends before a schedule reaches its declared endpoint unless explicitly justified.
- Record optimizer, scheduler, normalization state, update count, and RNG state according to the new checkpoint contract.
- Use immutable, run-versioned checkpoint paths. Keep latest and best as pointers/copies within the run, never as the sole artifact or as a replacement for the baseline.
- Record selection criteria for best before training. Do not select by training reward alone.
- Resume only under an explicit compatible lineage and declared optimizer/scheduler policy. Otherwise start a new run or use an explicitly documented controlled transfer.
- Preserve raw episode outputs and aggregate reports; summaries alone are insufficient for reproduction.

## 6. Metrics and reporting

### 6.1 Primary outcome metrics

Report at minimum:
- mean placement and placement distribution;
- top-4 rate and win rate;
- paired candidate-minus-baseline differences;
- 95% uncertainty intervals for primary comparisons.

Do not report only a mean or a single small batch of matches.

### 6.2 Secondary behavior and decision metrics

Report:
- episode return separately from placement/outcomes;
- survival/round reached and elimination timing;
- economy trajectory, interest, spending, XP/reroll behavior, and opportunity cost where observable;
- action distribution by action family and game stage;
- legal-mask coverage, invalid actions, rejected actions, and mask/action consistency;
- PPO entropy, value error, explained variance, and relevant optimization diagnostics;
- loops, reversals, repeated buy/sell behavior, spending without measurable gain, missed opportunities, and reward-hacking indicators;
- performance segmented by stage, economic state, relative board strength, composition, opportunity type, and evidence completeness.

Every metric must declare its source, aggregation unit, missing-data handling, and whether it is an outcome, behavior, or training diagnostic.

### 6.3 Uncertainty and sample size

- Use paired resampling over independent lobby seeds for candidate-vs-baseline intervals; do not treat players within one lobby as independent samples.
- Pre-register the primary metric, practical effect threshold, confidence level, and stopping/sample-size rule before final evaluation.
- Use an initial exploratory screen of at least 30 independent paired lobby seeds; this is not automatically sufficient for promotion.
- Increase sample size when the interval is too wide to distinguish the pre-registered practical threshold. Report independent lobby count and interval width.
- Correct or clearly label multiple comparisons when many ablations, segments, or candidate checkpoints are inspected.

## 7. Ablation protocol

Ablations answer a named hypothesis, not merely produce a leaderboard. Plan separate comparisons for:
- Observation Schema blocks and derived/contextual features;
- encoder families and specialized heads;
- reward components and temporal attribution;
- action/context side inputs where contracts permit;
- training hyperparameters and schedule choices.

Change one factor family at a time when causal attribution is the goal. Include the full configuration and relevant leave-one-block-out comparisons. Keep seeds, seat rotation, opponent settings, and evaluation contracts paired across ablations. Report negative results and regressions.

Do not use Shadow recommendations, scores, confidence, candidate rankings, or executor resolutions as PPO labels. PPO-vs-Shadow divergence is diagnostic only and must be correlated to the exact same decision identity/sequence before being reported.

## 8. Promotion and rollback gates

A candidate lineage may be promoted only when:
1. Required contract hashes and checkpoint lineage validate.
2. Evaluation uses frozen, disjoint test seeds and deterministic seat rotation.
3. Primary outcome comparison meets the pre-registered practical threshold with the declared uncertainty rule.
4. No critical regression appears in legality, mask consistency, stability, or contract invariants.
5. Secondary metrics and segmented results are reviewed for material regressions; trade-offs are explicitly accepted.
6. The report is reproducible from manifests, raw episode records, and code/build identities.
7. The previous baseline remains available and immutable for rollback.

A promotion decision must state promote, hold, or reject, cite exact run IDs and report hashes, and explain uncertainty and trade-offs. If evidence is inconclusive, the result is hold, not success.

No universal numeric win-rate/placement threshold is embedded here: the practical effect threshold must be declared for the experiment before the test set is opened, based on product objective and baseline variance.

## 9. Required report artifacts

Each evaluation report must include:
- experiment and contract manifest;
- train/validation/test split manifests;
- paired seed and seat-rotation schedule;
- per-lobby raw results and failure/retry ledger;
- aggregate outcome metrics and uncertainty intervals;
- behavior, legality, stability, and optimization diagnostics;
- ablation table with hypothesis and factor changes;
- baseline/candidate artifact hashes;
- promotion decision and rollback reference.

## 10. Gate boundaries and acceptance

This document completes only the **documentary protocol draft** for #295. It does not complete Gate 7 executable acceptance.

Post-Gate-8 implementation/evidence must include:
- evaluator enforcement of contract/checkpoint manifests;
- independent per-lobby RNG seeding and deterministic seat rotation;
- immutable checkpoint/run artifact handling;
- split leakage checks and reproducible raw result capture;
- paired uncertainty calculation and report generation;
- at least one end-to-end candidate-vs-baseline evaluation plus representative ablations;
- validation that Shadow outputs are not used as PPO labels/reward targets.

The separate strategic replay contract in #315/#289 is complementary: it validates the Shadow strategic chain and temporal correlation, not PPO benchmark superiority. Runtime replay and PPO evaluation must both be exercised after Gate 8, without executing actions in the live game.

## 11. Explicit non-goals and invariants

- No live-game action execution.
- No changes to Engine rules, action masks, PPO, observations, rewards, training, checkpoints, or Viewer before Gate 8.
- No requirement to load legacy PPO checkpoints into the new architecture.
- No claim that Shadow recommendations are ground truth, causal interventions, or PPO reward targets.
- No promotion based solely on internal reward, training curves, or a small unpaired sample.
