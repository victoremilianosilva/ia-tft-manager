# PPO Architecture and Checkpoint Contract v1

**Status:** approved documentary specification; loader migration and executable acceptance remain blocked until Gate 8 and explicit authorization  
**Contract ID:** `tft.ppo-checkpoint.v1`  
**Target architecture:** `new-arquiteture`  
**Related issues:** #286, #288, #287, #294, #295  
**Depends on:** approved Observation Schema v1, Action / Mask Contract v1, and Reward Contract v1 documentary specifications

> This document records the proposed architecture identity, checkpoint metadata, compatibility classes, and migration policy for the new PPO lineage. It does not change policy, training, rollout, Engine, action legality, reward formulas, or existing checkpoint files.

## 1. Purpose and non-goals

A checkpoint is not semantically identified by tensor shapes alone. The same shape can encode different feature meanings, ordering, normalization, action meanings, catalog identities, reward attribution, or encoder/head behavior.

This contract separates four questions:

1. **Structural loadability:** can tensors and serialized state be read into a compatible module shape?
2. **Inference-semantic compatibility:** does the consumer interpret every input feature and output action exactly as the producer did?
3. **Training-resume compatibility:** can policy, optimizer, scheduler, update counter, rollout assumptions, and training configuration be resumed without silently changing the optimization process?
4. **Historical evaluability:** can a legacy artifact be retained and evaluated as a baseline without claiming semantic compatibility with the new lineage?

Non-goals:
- No automatic semantic migration is approved here.
- No existing checkpoint may be rewritten, upgraded in place, or deleted.
- No change to PPO clipping, GAE, masks, action dimensions, reward values, or Engine rules is authorized.
- Shadow recommendations, confidence, or planner outputs are not imitation targets and do not become PPO labels by inclusion in metadata.

## 2. Audited current architecture (baseline, not normative v1)

The current `policy.py` defines:
- six action dimensions: `[9, 5, 9, 28, 28, 28]`;
- a spatial board slice of `4 × 7 × 5 = 140` values beginning at offset 22;
- a convolutional board encoder (5 input channels, 32 then 64 channels);
- a global MLP with 256-wide layers and a 512-wide fusion representation by default;
- conditional/autoregressive action heads for action type, shop, sell, bench, board movement, and item operations;
- a value head over the fused representation;
- an explicit candidate tail and item semantic/compatibility blocks;
- five policy-derived economic context features currently computed from the legacy observation's HP, gold, level, round, and strategy one-hot.

The current `TFTPolicy.load_compatible_state_dict()` supports selected shape migrations (including action-head expansion and input-column insertion/shift). Its return value indicates that a shape migration occurred; it does **not** prove that source and target feature semantics, action meanings, catalogs, or reward lineage are compatible.

The current trainer checkpoint payload contains `policy`, `optimizer`, `scheduler`, `update`, `training_config`, and `scheduler_type`. The loader currently restores policy weights first, conditionally restores Adam state when the shape loader reports no migration, and restores the scheduler only when scheduler type and selected LR schedule values match. These are observed legacy mechanics, not the approved v1 compatibility policy.

## 3. Architecture identity

Every new policy lineage must have an explicit, immutable architecture identity. At minimum it records:

| Identity | Required metadata |
|---|---|
| Policy implementation | architecture ID and version; source revision |
| Encoder | encoder ID/version, board layout, global feature projection, fusion width |
| Action heads | head-layout ID/version, action argument order, per-head dimensions |
| Value head | value-head ID/version and output semantics |
| Observation input | schema ID/version, tensor projection ID/version, dimension, ordered feature manifest hash |
| Derived features | formula IDs/versions, source paths, units, normalization and missing-value policy |
| Action output | Action Contract ID/version/hash and exact dimensions |
| Catalogs/rules | stable catalog IDs, versions, content hashes, ruleset identity where relevant |

An architecture ID must change when a change can alter the meaning of model inputs/outputs or the computation performed by the model, even if parameter names and tensor shapes remain unchanged.

A source commit alone is not a substitute for semantic IDs: the manifest must state the contract identities that the commit implements.

## 4. Checkpoint manifest v1 (proposed)

New checkpoints should carry a versioned `contract_manifest` alongside weights and training state. The following is a conceptual shape, not a committed runtime schema or an instruction to write these keys into current checkpoints:

```json
{
  "checkpoint_format": "tft.checkpoint.v1",
  "artifact": {
    "lineage_id": "required-stable-lineage",
    "created_at": "UTC timestamp",
    "source_revision": "git commit",
    "engine_revision": "git commit or immutable build identity"
  },
  "policy": {
    "architecture_id": "tft.policy.<id>",
    "architecture_version": "semver-or-contract-version",
    "encoder_id": "tft.encoder.<id>",
    "encoder_version": "version",
    "action_heads_id": "tft.action-heads.<id>",
    "action_heads_version": "version",
    "value_head_id": "tft.value-head.<id>",
    "obs_dim": 0,
    "action_dims": []
  },
  "observation": {
    "schema_id": "tft.observation.v1",
    "schema_hash": "sha256:<64-hex>",
    "projection_id": "tft.observation-tensor.v1",
    "projection_hash": "sha256:<64-hex>",
    "ordered_features_hash": "sha256:<64-hex>",
    "normalization_manifest_hash": "sha256:<64-hex>",
    "derived_formula_manifest_hash": "sha256:<64-hex>"
  },
  "action": {
    "contract_id": "tft.action.v1",
    "contract_hash": "sha256:<64-hex>"
  },
  "reward": {
    "contract_id": "tft.reward.v1",
    "contract_hash": "sha256:<64-hex>",
    "temporal_attribution_id": "tft.reward-attribution.v1",
    "temporal_attribution_hash": "sha256:<64-hex>"
  },
  "catalogs": [
    {
      "catalog_id": "stable-id",
      "version": "version",
      "content_hash": "sha256:<64-hex>"
    }
  ],
  "training": {
    "algorithm": "PPO",
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "rollout_contract_id": "tft.rollout.<version>",
    "optimizer": "Adam",
    "optimizer_config_hash": "sha256:<64-hex>",
    "scheduler_id": "cosine_clamped",
    "scheduler_config_hash": "sha256:<64-hex>",
    "training_config_hash": "sha256:<64-hex>"
  }
}
```

The values above are placeholders/examples, not approved production IDs or numeric defaults. Actual manifests must use exact immutable IDs and hashes produced from the corresponding versioned artifacts. Do not put credentials, local paths, private tokens, or player-identifying data in the manifest.

The manifest must distinguish:
- **required identity** from optional diagnostics;
- **observed facts** from derived/estimated/inferred values;
- **unknown/missing** from a valid numeric zero;
- **contract version** from source commit;
- **structural dimensions** from semantic feature identity.

## 5. Compatibility classification

Compatibility must be computed and reported in separate dimensions. A single boolean named `compatible` is insufficient.

| Class | Meaning | Permitted behavior |
|---|---|---|
| Exact semantic + structural | All required IDs/hashes and tensor shapes match | Inference; training resume only if training-state checks also pass |
| Structural-only | Tensors fit, but one or more semantic identities are missing/different | No silent inference as current policy; no training resume |
| Explicitly migrated | A reviewed migration map covers every changed identity and has validation evidence | Only the migration operation explicitly authorized by that map; output is a new artifact |
| Legacy-unverified | Artifact predates manifest or has incomplete provenance | Preserve as historical baseline; evaluation only in a clearly labeled legacy environment |
| Incompatible | Known contract, architecture, catalog, or action mismatch without an approved migration | Reject load for the requested purpose with field-level reasons |

Loader/report output must identify each compared field, source value, target value, and result. It must never infer semantic compatibility from matching dimensions, tensor keys, parameter counts, or a successful `load_state_dict`.

## 6. Training-resume policy

Restoring model weights and resuming optimization are different operations.

A training resume requires all of the following:
- exact or explicitly migrated policy architecture identity;
- exact observation schema, projection, feature order, formulas, and normalization identity;
- exact Action Contract and action-head dimensions/order;
- exact reward and temporal-attribution contract identity;
- compatible catalog/rules identity;
- optimizer algorithm and parameter-group compatibility;
- scheduler type and schedule identity;
- compatible rollout/GAE semantics and training configuration;
- explicit update/step continuity and provenance.

Optimizer state must not be restored merely because parameter tensor shapes happen to match. If architecture or parameter mapping changes, optimizer moments are not presumed meaningful. A migration must explicitly say whether optimizer state is preserved, transformed, or reset, and why. Scheduler state must follow the same explicit policy.

If weights are intentionally imported only as an initialization for new training, classify that operation as **warm-start/fine-tuning**, not resume. The new run gets a new lineage/run identity and records the source checkpoint plus the approved migration map.

## 7. Observation and reward coordination

The observation manifest must reference both:
- the semantic Observation Schema (field identities, provenance, status, units, catalog references); and
- the tensor projection (ordered feature IDs, offsets, dimensions, normalization, missingness encoding, and consumer/head alignment).

The projection must not collapse `missing`, `unknown`, `stale`, or `incompatible` into a valid zero without an explicit field-level encoding rule.

Derived policy features must be versioned by formula and inputs. In particular, the currently audited five economic-context features are derived from legacy strategy one-hot columns; their present formulas are not approved as the new architecture's semantic definition. The new projection must reconstruct context from approved factual/evidence sources and must not reintroduce ECON/FAST8/SLOWROLL/ALL_IN nominal strategy defaults.

Reward metadata must reference the Reward Contract and temporal attribution version. The reward contract draft currently records an unresolved GAE validity concern: `valid` is applied during normalization/batch selection, but is not consulted by the backward GAE recurrence. It also requires explicit terminal-versus-truncation semantics. These must be resolved and tested before a new training lineage is declared reproducible.

## 8. Legacy checkpoint handling

- Existing checkpoint files are immutable baselines. Never overwrite them during migration or validation.
- Missing manifest means `legacy-unverified`, not “compatible by default”.
- Legacy structural loading through `load_compatible_state_dict()` is not proof of semantic compatibility.
- Any approved conversion writes a separate output artifact and includes source hash, target contract IDs, migration-map ID/version, tool revision, and validation report.
- Legacy evaluation must label the exact environment/policy semantics used and must not compare metrics as if the new observation/reward lineage were identical.
- A successful deserialization is not acceptance evidence.

## 9. Required acceptance evidence

Before runtime implementation can be considered complete, tests and reports must demonstrate:

1. Exact manifest round-trip and deterministic hash generation.
2. Exact-match checkpoint accepted for inference and resume when all training-state checks pass.
3. Same tensor shapes but changed feature order/hash rejected as semantic mismatch.
4. Same tensor shapes but changed derived formula/normalization rejected.
5. Changed observation dimension rejected unless a complete approved migration map exists.
6. Action Contract ID/hash or action-head order/dimension mismatch rejected.
7. Reward/temporal-attribution mismatch rejected for resume.
8. Catalog/rules content mismatch detected.
9. Legacy checkpoint without metadata classified legacy-unverified and preserved unchanged.
10. Structural-only load never silently becomes a semantic load.
11. Optimizer/scheduler restoration follows explicit policy and has positive and negative tests.
12. Approved migration produces a new artifact, preserves source bytes/hash, and records full provenance.
13. Manifest/report identifies all mismatched fields and remediation category.
14. Reproducibility test can identify the exact observation, action, reward, catalog, policy and training contracts for a recorded update.

## 10. Migration and rollout sequence

1. Approve Observation Schema and tensor projection, including complete feature/source/consumer maps.
2. Approve Action Contract and its relationship to action-head ordering/dimensions.
3. Approve Reward Contract and temporal attribution; resolve GAE validity and terminal/truncation gaps.
4. Freeze policy architecture identity and encoder/head manifest.
5. Define checkpoint manifest schema and compatibility classifier.
6. Implement manifest emission and validation behind tests; do not mutate historical artifacts.
7. Add explicit migration tooling only for reviewed migration maps.
8. Produce a new checkpoint lineage and retrain/fine-tune according to a reproducible plan.
9. Compare against legacy baselines without claiming semantic equivalence.

## 11. Gate status and implementation boundary

**Documentary work in this draft:** current architecture and checkpoint payload audited; proposed manifest, compatibility classes, resume policy, legacy policy, and acceptance matrix specified.

**Still pending before Gate 4 can be accepted as a complete contract:**
- final Observation Schema/projection approval and exact feature manifest/hash generation;
- final Action Contract identity/hash and head-order mapping;
- final Reward Contract approval and temporal attribution identity;
- a complete architecture manifest with stable encoder/head IDs and deterministic serialization;
- review of the migration policy against every existing checkpoint-loading path.

**Runtime work is explicitly deferred.** No policy, trainer, loader, optimizer, scheduler, rollout, PPO, Engine, action mask, reward, Viewer, or checkpoint file is changed by this document. Gate 8 approval is required before implementation begins.
