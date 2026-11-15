# Remaining Identity, Ownership, Rollout and Gate Reconciliation v1

**Status:** source-backed documentary reconciliation; no runtime acceptance.  
**Branch target:** `new-arquiteture`.  
**Scope:** remaining main-repository identity, UnitInstance value semantics, PPO transition correlation, schema dispositions and Gates 1–7 readiness.  
**GEP:** real-source validation explicitly deferred until Overwolf integration, per the domain owner's direction.  
**Implementation:** no runtime work before Gate 8 and explicit authorization.

## 1. Executive disposition

The remaining documentary work can be consolidated without waiting for a real GEP capture. The Overwolf match-ID source path is already documented; real-source validation, reconnect semantics and capture lifecycle are deferred to the OW integration phase and are not a blocker for the current main-repository audit.

| Workstream | Evidence now established | Remaining status |
|---|---|---|
| Engine scope | TFTEngine is move-only; its pimpl has an episode counter but no Engine-instance token | Semantic contract defined; producer and transport remain post-Gate 8 |
| UnitInstance identity | Implicit value copy/move preserves UUID; factory UUIDs repeat across same-seed reset/object lineages | Source semantics documented; no globally scoped physical ID |
| Active ownership | Production transfer paths distinguish moves, rollback copies and projection copies | Full proof of every implicit lifetime/alias path and duplicate-active-owner invariant remains a runtime test obligation |
| Wrapper/rollout | Native episode/masks survive pybind; wrapper drops them; rollout stores masks at same index as obs/action but no durable identity | Exact identity propagation and terminal-boundary replay remain unimplemented |
| Schema v2 | Current structured identity and entity fields exceed what PPO receives | Keep unavailable/not-correlated/not-delivered statuses; do not promote schema declarations to producer proof |
| Gates 1–7 | Documentary contracts and audits exist | Runtime acceptance remains pending; Gate 8 remains blocked |
| GEP | Mapper path and synthetic test are documented | Real fixture/lifecycle validation deferred until OW integration; not a blocker for this current workstream |

## 2. Native Engine instance and episode scope

### 2.1 Source facts

- `TFTEngine` owns its implementation through `std::unique_ptr<Impl> impl_`.
- Copy construction and copy assignment are deleted in `cpp/include/lobby/TftEngine.hpp`.
- Move construction and move assignment are defaulted in `cpp/src/lobby/TftEngine.cpp`.
- Construction allocates a new `Impl`; the audited `Impl` has `episode_id{0}`.
- `reset()` increments `episode_id`.
- No Engine-instance UUID/token, process namespace, global registry or other independent instance-scope producer was found in the audited class/constructor/reset/result paths.
- Defaulted move transfers the `unique_ptr` and therefore the existing Impl state; it does not mint an instance token.
- Independently constructed Engines can have the same seed and same numeric episode counter.

### 2.2 Canonical semantic contract

The minimum semantic Engine episode reference remains:

`engine_episode_ref = (engine_instance_scope, episode_id)`

This is a semantic requirement, not an implemented tuple or selected UUID algorithm. A moved Engine retains the same logical Impl scope; a newly constructed Engine requires a distinct scope within the supported collision domain. Numeric `episode_id` alone is not enough.

The Engine-instance token must be owned by the native Engine lifecycle. Python, Viewer, Trainer, JSONL or replay must not synthesize it from object address, seed, timestamp, array index or creation order.

### 2.3 Player and decision scope

Player seat `0..7` is an episode-local lobby position, not a durable player identity. A decision reference additionally needs an explicit player scope and a typed native decision/observation sequence. The following remain separate:
- Engine instance scope;
- Engine episode counter;
- player seat;
- observation/snapshot sequence;
- action-decision sequence;
- mask source sequence;
- Viewer session/event sequence;
- JSONL append sequence;
- rollout storage pointer.

No namespace may be substituted for another merely because counters happen to increase together.

## 3. UnitInstance value and ownership semantics

### 3.1 Confirmed C++ semantics

`UnitInstance` in `cpp/include/lobby/TftEngine.hpp` is a public aggregate-like struct with:
- champion internal ID and textual ID;
- UUID string;
- star tier;
- vector of item mirror records.

It declares no custom copy constructor, move constructor, copy assignment, move assignment or destructor, and no deleted copy operation. Its members are copyable/movable value types. Consequently:
- copy construction copies the UUID string and item vector;
- copy assignment replaces them with the source values;
- move construction/assignment transfers member values but does not mint a new UUID;
- `is_valid()` checks a non-empty UUID and valid champion ID, not uniqueness or ownership.

The stale comment in the struct saying UUID generation will be implemented later is contradicted by `UnitInstanceFactory::create()` calling `generate_uuid()`. The comment is historical/stale; no header/runtime edit is made in this documentation PR.

### 3.2 Factory and scope

`UnitInstanceFactory` uses `std::mt19937_64` initialized from the Engine base seed. Same seed plus same create-call order reproduces the UUID sequence. Engine reset reconstructs the factory using the base seed, not the incremented episode ID. Therefore same-seed resets and independent same-seed Engine instances can reproduce UUID values.

A UUID is thus a local factory-generated physical-instance token, not a globally unique identity. Cross-episode references require Engine episode scope plus the instance token. A copied DTO/snapshot may legitimately repeat a UUID without representing a second active owner.

### 3.3 Ownership map remains authoritative

The documented production path distinguishes:
- shop draw: new factory instance;
- reroll rollback: temporary value copy for failure restoration;
- strategic UnitSnapshot projection: non-owning value projection;
- purchase: existing offer moved into bench;
- board/bench positioning: move/swap;
- merge: purchased/base UUID survives; consumed UUID equipment mappings transfer before consumed slots retire;
- sale: equipped items return before unit leaves active ownership;
- elimination: board/bench owners are removed; item state is retired only under the accepted terminal policy;
- Engine reset: ItemEngine state clears and factory sequence restarts from base seed.

The invariant is uniqueness among simultaneously active physical owners within the authoritative Engine/player/episode domain, not uniqueness across diagnostic copies. Existing source maps narrow explicit ownership paths; they do not prove every possible alias, implicit lifetime path or absence of all duplicate-active-owner bugs. Those require native regression tests.

### 3.4 Fixture hooks remain non-production evidence

- `set_unit_for_testing` bypasses ordinary shop/pool transaction semantics and may overwrite fixture slots.
- `set_unit_items_for_testing` updates the UnitInstance mirror but not ItemEngine's authoritative UUID-keyed equipment map.
- Shop fixture injection bypasses weighted draw semantics; it does not create durable offer identity.
- Tests using these hooks cannot substitute for production buy/move/merge/sale/elimination transaction tests.

## 4. Native → Python → PPO transition correlation

### 4.1 Native and pybind

Native `ResetResult`/`StepResult` and their pybind dictionaries preserve `episode_id` and action masks. The loss occurs in `cpp_lobby_env.py`, not in the native result structs:
- `reset()` returns only observations;
- `step()` returns observations/rewards/dones/info but omits native `episode_id` and returned masks;
- `get_action_masks()` fetches masks through a separate native call.

### 4.2 Current Trainer and RolloutBuffer behavior

The synchronous Trainer path:
1. fetches masks for the current environment state;
2. samples PPO action using current observation plus those masks;
3. submits actions to each lobby;
4. receives next observation, reward, done and info;
5. stores pre-action observation, sampled action, logprob, reward, done, value and the exact masks used for sampling at one RolloutBuffer pointer;
6. advances to returned next observation.

`RolloutBuffer.add()` shape-checks and stores masks at the same temporal index as observation/action. This is real preservation of the masks used for sampling. It is not durable identity correlation: the buffer has no Engine scope, episode ID, player ID, round, observation sequence, decision sequence or mask source sequence. Its pointer and flattened agent position are storage coordinates only.

### 4.3 Terminal auto-reset boundary

The vector environment captures the terminal result, then resets a completed lobby before returning its next observation/masks. The returned reward/done describe the terminal episode while the returned observation belongs to the next episode. In the current synchronous flow, the next iteration fetches masks from that reset state; this is not evidence of a stale-mask race.

However, without episode identity in the wrapper/rollout, the boundary cannot be reconstructed or proven from stored transition metadata. A future replay contract must bind:
- pre-action observation + pre-action masks + sampled action to the old episode/decision;
- reward + done + terminal result to that same old episode;
- returned next observation + next-state masks to the new episode after auto-reset.

No runtime fix is made here.

## 5. Schema v2 and CSV dispositions

Schema v2 remains a proposal and a traceability contract, not a claim that all structured entities are delivered to PPO. Preserve the following distinctions:
- native observed vs derived;
- authoritative producer vs diagnostic-only serialization;
- available vs not-produced vs unavailable vs not-correlated;
- pybind exposure vs wrapper exposure;
- structured sidecar vs current flat PPO observation;
- masks as independent final legality inputs;
- typed identity/sequence availability vs storage order.

Do not change a field to `available` merely because a schema property exists or a diagnostic snapshot can serialize it. In particular:
- UnitInstance UUID is not global physical identity and is not a typed PPO feature;
- shop slot is not durable offer identity;
- item catalog IDs/multiplicity are not physical item-instance identity;
- pool availability is a native query but not an immutable observation/rollout field;
- Shadow proposals remain diagnostic/read-only and are not PPO labels;
- Engine episode number without Engine scope is incomplete;
- rollout index is not decision identity.

No tensor layout, dimension, hash scope or historical schema-v1 artifact is changed by this reconciliation.

## 6. GEP deferral decision

The exact mapper source path `info.match_info.match_info.match_id`, synthetic normalization test, manager `sessionId`/revision behavior and recorder's new-baseline behavior remain documented in the Overwolf integration boundary and PR #418.

Per the user's explicit direction, real GEP capture validation is deferred until the Overwolf integration workstream. It is not a blocker for completing the current main-repository identity/rollout documentary work. Do not fabricate a real fixture, mark canonical `match_id` available, or make an OW change now. When OW integration begins, validate real source presence, consecutive matches, reconnect/reset, missing/null behavior and transport preservation.

## 7. Gate 1–7 consolidated readiness

| Gate | Documentary contract | Runtime status |
|---|---|---|
| 1 — Observation/context | Schema v2, source crosswalk, producer dispositions and identity semantics | Pending structured producer/adapter and typed identity-bound delivery |
| 2 — Actions/legality | Candidate contract and native mask contract | Pending candidate producer and exact mask/decision correlation; native masks remain final legality authority |
| 3 — Reward/credit | Reward contract and source audit | Legacy reward path remains active; migration and typed event attribution pending |
| 4 — PPO/checkpoint | Architecture, consumer matrix and evaluation/checkpoint contracts | Concrete projection, loader/manifest and executable lineage pending; do not freeze dimensions without projection decision |
| 5 — Strategic authority | Shadow ownership, candidate/economic/unit contracts | Runtime producer/consumer integration and end-to-end replay pending |
| 6 — Legacy audit | Static consumer inventory and migration matrix | Legacy StrategyInfo consumers remain active; migration/shutdown pending |
| 7 — Replay/evaluation | Replay contract and evaluation protocol | Deterministic integrated replay and new-lineage evaluation artifacts pending |
| 8 — Authorization | Explicit authorization required | **Blocked; not granted** |

### 7.1 Current cross-gate blockers

1. No canonical Engine-instance scope token is produced or transported.
2. No canonical typed decision/snapshot/mask sequence is delivered end-to-end.
3. Wrapper drops native episode identity and bundled masks; RolloutBuffer stores no durable identity.
4. Actor receives masks, but current Critic value path ignores them; policy/evaluation contract must account for this explicitly.
5. Current action-candidate source vector is empty; no confident comparison can be inferred from an empty candidate set.
6. Multiple structured entity families remain not-produced, diagnostic-only, Shadow-only, not-correlated or not-delivered to PPO.
7. Legacy strategic consumers remain active.
8. Full multi-round replay and new-lineage PPO evaluation remain unexecuted.
9. Terminal item discard/no-transfer is a settled domain rule; implementation and regression proof remain post-Gate 8, not an unresolved policy decision.
10. Real GEP source validation is deferred to OW integration and is not a blocker for the current main-repository workstream.

## 8. Issue #346 disposition

Issue #346 remains open. The documentary entity matrix and source audits do not establish complete producer delivery. Closure still requires source-backed producer dispositions for all 17 entity kinds, lifecycle/ownership/completeness/provenance/sequence proof, exact native→pybind→wrapper→rollout correlation and deterministic replay. GEP real-source acceptance is explicitly deferred to OW integration; it must not be used to block the current non-OW audit work.

The eliminated-player item domain decision is settled: terminal discard, no transfer to any player, no return to the eliminated player's active bag, and no redistribution to any pool/shop/PvE source. Implementation and regression tests remain blocked until Gate 8.

## 9. Reconstruction review

1. **Prior problem:** Engine scope, copy semantics, rollout identity and gate status were spread across audits; stale documentary statements still treated settled decisions as provisional.
2. **Technical rationale:** identity ownership and reset boundaries differ across native Engine, UnitInstanceFactory, wrapper, vector environment, PPO and replay.
3. **New responsibility:** this document consolidates the remaining identity/ownership/rollout evidence and current gate dispositions.
4. **Contract/invariants:** no synthetic IDs; no bare UUID as global identity; no array index as durable identity; no promotion of diagnostic/schema data to PPO delivery; masks remain independent legality input; no item redistribution; GEP real-source check deferred to OW integration.
5. **Cross-component impacts:** TFTEngine/Impl, UnitInstanceFactory, ShopEngine, ItemEngine, pybind, Python wrapper, vector environment, Trainer, RolloutBuffer, Actor/Critic, Schema v2, CSV, Viewer/replay and issue #346.
6. **Objective validation:** source declarations and call paths are cited by repository path; current runtime gaps and future tests are explicit; GEP deferral is recorded; no runtime or tensor files are changed.

## 10. Final status

The remaining main-repository documentary reconciliation is complete in this PR. This does not mean Gates 1–7 have runtime acceptance, does not close issue #346, and does not authorize Gate 8. Implementation remains blocked until the integrated review and explicit user authorization.
