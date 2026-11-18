# Shared Champion Pool Snapshot Contract v2 — Draft

**Status:** nested Stage 1 contract revision; implemented with Native State Snapshot Contract v3 in PR #484, pending review and CI.  
**Supersedes:** Shared Champion Pool Snapshot Contract v1.  
**Tracking:** #346, #293 and #294.

## 1. Prior problem

The v1 shared-pool child record copied Engine instance, episode, snapshot sequence, all player decision sequences and source namespace already present in the enclosing AuditSnapshot. The duplicated envelope added no independent identity and required the wrapper to compare two copies.

## 2. Technical rationale

The pool snapshot is always transported as a child of the same atomic AuditSnapshot. The parent is therefore the sole correlation authority. The pool still needs its own contract identity and producer because those describe the child payload's semantics and factual source, not the decision envelope.

## 3. New responsibility and owner

- UnitPool remains authoritative for initial and currently available copy counts.
- TFTEngine::get_audit_snapshot() owns the single Engine/episode/snapshot/player-sequence envelope.
- AuditSharedPoolSnapshot owns only its child contract, producer, total and catalog-ordered champion counts.
- Pybind transports the child without copying parent identity.
- CppTFTLobbyWrapper validates the child contract, rejects duplicated parent-envelope fields and validates count invariants.
- Trainer/RolloutBuffer retain the complete parent snapshot as non-tensor metadata.

## 4. Contract

The nested shared_pool record uses:
- contract ID tft.shared-champion-pool-snapshot, version 2;
- producer UnitPool::available;
- parent AuditSnapshot source namespace and identity, inherited rather than copied;
- catalog-ordered rows: champion_internal_id, champion_id, cost, initial_count and available_count;
- total_available, equal to the sum of row available_count values.

Invariants: unique champion IDs and names; nonnegative internal IDs; cost 1–5; positive initial count; available count between zero and initial count; total equals row sum; catalog order comes from ChampionCatalog::all(), not unordered pool maps. The child must not contain source_namespace, engine_instance_id, episode_id, snapshot_sequence or player_decision_sequences. This is shared-lobby state, not eight player-specific pools. The payload remains diagnostic/non-tensor metadata, not an Actor/Critic feature, reward, action candidate, legality mask or PPO label.

## 5. Cross-component impact

Changes the nested native DTO, pybind serialization, wrapper validation, snapshot fixtures and producer documentation. UnitPool draw/return rules, action dimensions, observation tensors, masks, rewards, policy, checkpoint semantics, Viewer and Overwolf remain unchanged.

## 6. Objective validation

- Native build proves all consumers compile against the v2 child DTO.
- Wrapper accepts v2 pool payloads correlated through the v3 parent.
- Wrapper rejects a child that reintroduces any parent-envelope field.
- Existing pool count, catalog uniqueness and total consistency tests pass.
- Reset and Step payloads continue to carry the exact parent identity.
- CI passes native and Python integration suites before this revision is accepted.

## 7. Architecture reconstruction review

1. **Prior problem:** the nested pool repeated the parent envelope and namespace, creating redundant values and a second consistency check.
2. **Technical rationale:** the pool is never transported independently; parent identity is authoritative while the pool's contract and producer are distinct.
3. **New responsibility:** AuditSnapshot owns correlation; AuditSharedPoolSnapshot owns pool semantics and UnitPool provenance.
4. **Contract/invariants:** child version 2; no copied identity/sequence/source namespace; producer and pool facts remain; total/count invariants remain strict.
5. **Cross-component impacts:** native DTO, pybind, Python wrapper, tests, docs and downstream snapshot consumers; no PPO/tensor/reward/mask changes.
6. **Objective validation:** compile, serialize, validate parent-only identity, reject duplicate fields, and pass CI.
