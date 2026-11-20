# Observation Projection — Semantic Decision v1

**Status:** approved semantic contract; concrete tensor layout and model implementation remain assigned to PR 3.
**Canonical architecture:** TFT Strategic Engine + PPO.
**Related:** `spec/observation-projection-manifest.v1.draft.json`, `spec/observation-schema.v2.draft.json`, issues #293 and #286.

## 1. Prior problem

The Schema v2 inventory identified candidate fields but did not settle which information is semantic model input, which is control metadata, which is diagnostic-only, and how the Actor and Critic must receive missingness and legality. This left the first new PPO lineage without an authoritative semantic projection decision.

## 2. Technical rationale

Flattening heterogeneous game state into a single undifferentiated vector loses entity identity, spatial relations, temporal scope, provenance and missingness. Treating TFT Strategic Engine recommendations as labels would also turn PPO into an imitation of the strategic evaluator rather than a policy that learns from state and outcomes.

## 3. Approved semantic projection

The projection is a deterministic, versioned transformation from one validated Schema v2 player snapshot into typed semantic blocks. It is not a direct copy of the legacy observation vector.

| Semantic block | Authoritative content | Consumer disposition |
|---|---|---|
| Player and lifecycle | HP, alive/eliminated state, placement when observed, stage/round, level, XP, gold, streaks | Shared Actor/Critic state |
| Board and bench entities | Stable slots, occupancy, champion identity, star tier, physical UUID scoped by `engine_match_id`, equipped items | Shared entity/set encoder |
| Shop candidates | Current offers, slot/revision identity, cost and native availability | Shared candidate encoder; no invented offer identity |
| Item state | Components, completed-item inventory, equipped-item ownership, pending anvil and explicit options | Shared entity/set encoder and action conditioning |
| Spatial/positioning state | Board geometry, occupied coordinates, frontline/backline relations and validated positional evidence | Shared spatial encoder |
| TFT Strategic Engine context | Direction/commitment, active composition, owned pairs/upgrades, pivot feasibility, marginal opportunity cost, economic posture and uncertainty, only when their native owners publish valid evidence | Shared semantic context encoder with per-field validity/provenance |
| Exact action masks | Native legal-action masks correlated to the same decision identity | Separate Actor and Critic side inputs; never observation features |
| Decision identity and provenance | Engine episode scope, player/round, typed decision/snapshot references, hashes, source and validity metadata | Control plane only; never scalarized into neural features |
| Strategic recommendations and diagnostics | Candidate rankings, recommendation scores, confidence, evaluator explanations and executor diagnostics | Replay/Viewer diagnostics only; excluded from Actor, Critic, reward targets and imitation labels |

## 4. Encoding and validity invariants

1. Entity collections preserve stable identity and deterministic ordering. Fixed native slots remain fixed; variable collections carry explicit length/presence semantics.
2. Missing, unavailable, not-produced, stale, conflicting and invalid are distinct states. Numeric zero is a valid value and is never a generic missing sentinel.
3. Every derived or estimated field carries its formula/version, source inputs, units and confidence/uncertainty where meaningful.
4. A field is eligible only when its owner, provenance, validity and decision identity are validated. Schema declaration or diagnostic serialization alone does not prove availability.
5. Board/bench physical identity is `(engine_match_id, unit.uuid)`; player ownership is mutable metadata and is not part of physical identity.
6. Observation, action masks, sampled action, value estimate and rollout row must share the exact decision identity. A mismatch is rejected before policy/value evaluation.
7. Actor and Critic consume the same validated state and exact masks through separate side inputs. Their heads and objectives remain distinct; no strategic recommendation is used as a target.
8. Unavailable sources remain explicitly unavailable. In particular, future income, expected incoming damage and elimination risk are not populated with guessed values.
9. PPO remains the learning algorithm. TFT Strategic Engine contributes validated state/evidence, not a replacement policy.

## 5. Explicitly deferred to PR 3

This decision approves semantic ownership and consumer disposition, not a premature tensor shape. PR 3 must define and freeze block dimensions, categorical vocabularies, normalization identities, padding/truncation, encoder topology, Actor/Critic heads, projection hash and checkpoint lineage together. The current 77-field inventory and its dispositions remain traceable; fields classified unavailable or diagnostic-only are not silently promoted.

PR 3 must also prove the path through sampling, value estimation, rollout storage, replay and inference before removing the legacy tensor tombstones. Until then, the old tensor layout remains only for compatibility and is not a source of strategic meaning.

## 6. Reconstruction review

1. **Prior problem:** semantic candidates lacked a binding decision for model-input versus control/diagnostic use.
2. **Technical rationale:** entity, spatial, temporal and evidence semantics cannot be safely represented as an untyped flat vector.
3. **New responsibility:** this decision owns semantic grouping and Actor/Critic disposition; Schema v2 owns field semantics; native Engine and TFT Strategic Engine owners remain authoritative producers; PPO owns learning.
4. **Contract/invariants:** no synthetic values, no zero-as-missing, no recommendation imitation, no identity conflation, and no mask substitution.
5. **Cross-component impacts:** Schema v2, projection manifest, native snapshot adapter, semantic encoder, Actor/Critic, action masks, rollout, replay and checkpoint lineage.
6. **Objective validation:** the existing machine-readable inventory remains the source for field-level traceability; implementation acceptance is deferred to the executable tests and artifacts in PR 3.