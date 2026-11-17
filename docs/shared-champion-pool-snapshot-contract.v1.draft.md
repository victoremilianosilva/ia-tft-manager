# Shared Champion Pool Snapshot Contract v1 — Draft

**Status:** bounded Stage 1 runtime contract; review required.  
**Tracking:** #346, #293 and #294.

## 1. Prior problem

The Engine already exposed authoritative per-champion pool_available, pool_initial_count and pool_total_available queries through C++ and pybind. Those independent queries were not captured in the same immutable payload as observations and masks, so a later query could describe a different pool state.

## 2. Technical rationale

The shared champion pool is lobby-scoped mutable state. A count is meaningful only with its catalog identity and the exact Engine/episode/snapshot that observed it. Champion catalog ID and API name identify a champion definition, not an owned physical copy. Pool counts are not player inventory, shop-offer identity, physical UnitInstance identity or a per-player resource.

## 3. New responsibility and owner

UnitPool remains authoritative for initial and currently available copy counts. TFTEngine::get_audit_snapshot() owns the immutable, sequence-bound capture. Pybind transports it; CppTFTLobbyWrapper validates the envelope and count invariants; Trainer/RolloutBuffer retain it only as non-tensor native metadata.

## 4. Contract

The nested shared_pool record uses:
- contract ID tft.shared-champion-pool-snapshot, version 1;
- source namespace tft.engine.observation-snapshot;
- producer UnitPool::available;
- Engine instance, episode, Engine snapshot sequence and eight player decision sequences copied from the enclosing native snapshot;
- catalog-ordered rows: champion_internal_id, champion_id, cost, initial_count and available_count;
- total_available, equal to the sum of row available_count values.

Invariants: unique champion IDs and names; nonnegative internal IDs; cost 1–5; positive initial count; available count between zero and initial count; total equals row sum; nested identity equals enclosing identity; catalog order comes from ChampionCatalog::all(), not unordered pool maps. This is shared-lobby state, not eight player-specific pools. The payload remains diagnostic/non-tensor metadata, not an Actor/Critic feature, reward, action candidate, legality mask or PPO label.

## 5. Cross-component impact

Changes native audit snapshot types/capture, pybind serialization, wrapper validation, rollout metadata transport and producer documentation. UnitPool draw/return rules, action dimensions, observation tensors, masks, rewards, policy, checkpoint semantics, Viewer and Overwolf remain unchanged.

## 6. Objective validation

Native API tests compare each captured row with pool_available() and pool_initial_count() and verify total consistency. Wrapper tests reject nested identity mismatch and inconsistent totals. Reset and Step payloads carry the same identity as the enclosing native snapshot. No training or Stage 1 acceptance is implied.

## 7. Explicit limitations

No physical UnitInstance IDs, pool mutation event history, per-player pool ownership, shop-offer ID/revision, GEP match identity or stable catalog fingerprint are added. Issue #346 and Stage 1 remain open.
