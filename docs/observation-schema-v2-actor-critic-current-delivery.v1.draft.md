# Schema v2 Current Actor/Critic Delivery Audit v1 — Draft

**Status:** current implementation trace only; not a target tensor projection.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.  
**Machine-readable field matrix:** [Schema v2 field/source crosswalk CSV](../spec/observation-schema-v2-field-source-crosswalk.v1.draft.csv).

## 1. Executive result

All 223 Schema v2 paths now have a field-level source disposition and an explicit current Actor/Critic delivery classification in the CSV. This audit traces the actual current code path:

`TftEngine::build_observations()` → native reset/step result → `CppTFTLobbyWrapper` float32 array → Trainer → `TFTPolicy` → RolloutBuffer.

The result is not a structured Schema v2 payload. The current runtime delivers a flat observation vector and separate native mask arrays. Shadow strategic evidence and diagnostic JSON sidecars do not enter that observation vector.

**Important asymmetry:** the Actor and Critic share the encoded observation representation, but they do not consume every observation sub-block identically. The Actor receives item compatibility matrices through item-specific heads; `TFTPolicy.encode()` removes those matrices from the shared encoder input used by the value head. The Critic therefore does not receive those exact fit matrices. The Critic also ignores action masks in the current implementation.

## 2. End-to-end delivery chain

### 2.1 Native Engine and Python wrapper

- Native `reset_to_dict` and `step_to_dict` return observations and action masks as separate values.
- `CppTFTLobbyWrapper.reset()` returns only `np.asarray(result["observations"], dtype=np.float32)`.
- `CppTFTLobbyWrapper.step()` returns observations, rewards, done and diagnostic `info`; it does not return the native masks in the tuple.
- Trainer calls `env_method("get_action_masks")` separately before policy action selection and before value bootstrap.
- Trainer flattens the masks and passes them to `get_action`/ `get_action_and_value`.
- RolloutBuffer stores observations and masks in separate tensors/dictionaries. It stores no native match/player/round/decision-sequence token proving that the separately fetched mask belongs to the exact observation transition.

The synchronous training loop may keep reads operationally adjacent, but call order is not an explicit correlation contract. The current implementation does not prove stale-mask rejection or exact observation/mask decision identity.

### 2.2 Shared Actor/Critic encoder

`TFTPolicy.encode(obs)`:
1. slices the board block and reshapes it to the existing 4×7 board tensor;
2. separates the candidate-slot tail;
3. removes the item compatibility matrix from the middle/global block when present;
4. appends deterministic economic context derived from the observation;
5. processes board and global features, fuses them, and returns one shared representation.

The Actor action heads and the value head both consume this encoded representation. The value path is `value_head(encode(obs))`. This is a shared current implementation, not a decision that the future architecture must share every feature.

### 2.3 Actor-only item compatibility matrices

The current item block contains:
- component features;
- nine inventory-item semantic feature rows;
- one hundred recipe semantic feature rows;
- thirty-seven unit target-profile rows;
- a 9×37 inventory-item/target compatibility matrix;
- a 100×37 recipe/target compatibility matrix.

`_item_state_features(obs)` extracts the two compatibility matrices separately. The item Actor heads use them:
- inventory selection uses per-item max/mean fit summaries;
- item target selection uses the selected inventory item's 37 target scores;
- recipe selection uses the selected recipe's 37 target scores.

By contrast, `encode()` removes the entire compatibility-matrix segment before constructing the shared global MLP input. The value head therefore receives the inventory/recipe semantic rows and unit target-profile rows, but **not** the 9×37 and 100×37 compatibility matrices. This is an actual Actor/Critic delivery difference, not a proposed target allocation.

The matrix target axis is positional (board/bench target slot). It is not a physical UnitInstance UUID. Recipe rows are catalog-derived positional rows; raw recipe IDs are not passed as continuous numeric IDs.

### 2.4 Actor-only mask side input

The Trainer retrieves masks separately and passes them to the Actor. The Actor applies masks to action-type, shop, bench/board source/target, item inventory, item target and component-choice logits. The masks are not ordinary observation features.

`get_value(obs, masks=None)` explicitly ignores masks and returns `value_head(encode(obs))`. The Trainer currently passes `next_masks` to this method, but they do not affect the value estimate.

This is a current implementation gap against the approved target mask contract, which requires exact decision-correlated masks for Actor and Critic (or a provably lossless encoding). Additional Critic history context cannot replace those masks.

## 3. Current delivery classification

The CSV's `actor_delivery` and `critic_delivery` columns describe **current runtime delivery**, not future eligibility and not a tensor-layout proposal.

| Classification family | Actor | Critic |
|---|---|---|
| `shared_*` observation features | Receives the corresponding numeric/derived feature block through the shared encoder | Receives the same shared encoded feature block |
| Board/bench/shop slot features | Receives fixed slot features and board CNN representation; raw champion/UUID identity is not implied | Same shared slot/CNN representation; raw identity is not implied |
| Candidate slot tail | Specialized BUY/SELL and movement candidate heads consume bench/shop slot features | Candidate tail is also present in the shared global encoder |
| Item global semantics | Component counts, inventory/recipe semantics, target profiles and conditional anvil features are in the shared encoder | Same shared item-global semantic features |
| Item compatibility matrices | Inventory/recipe fit matrices feed item-specific Actor heads | Removed from `encode()`; not delivered to value head |
| Item target/recipe axes | Actor sees positional target/recipe row indices used to select matrix rows/columns; no raw UUID/recipe ID | No compatibility matrix or physical target UUID; semantic recipe/target features remain in shared block |
| Native masks | Separate side input applied to Actor logits | Current `get_value` ignores masks |
| Anti-loop history | No history features; its legality effects can influence the separately delivered masks | No history features and no masks in current value path |
| Shadow strategic evidence and diagnostic snapshots | Not delivered to Actor | Not delivered to Critic |
| Conditional anvil features | Feature block exists in shared input, but audited gameplay path has no grant producer; current live values are not established | Same conditional/unpopulated boundary |
| Critic context | No separate context object; Actor shares the encoded observation | Value head consumes shared encoded observation; no separate status/sequence/reason object |

The current candidate tail's eight per-slot values include composition fit, cost, star, role, core flag, owned-copy count, upgrade signal, and either bench sell value or shop affordability. The cost value is a real shared Actor/Critic slot feature, but it is not a `StrategicActionCandidate.gold_cost` record and has no candidate ID, action kind or decision sequence.

## 4. Important per-family outcomes

### Shared current observation features

Both Actor and Critic currently receive, through the shared encoder:
- normalized player/economy observation scalars;
- board 4×7 slot features and CNN representation;
- bench/shop fixed slot features and candidate tail;
- normalized unit star/occupancy/role/selected combat profile features;
- aggregate item/trait features and component/inventory semantic blocks;
- selected positioning metrics, fixed trait-count blocks and capacity scalars;
- normalized remaining-action horizon and per-slot board-move-age features;
- legacy StrategyInfo focus-weight feature block;
- stage derived in Python from the normalized round observation.

This does **not** mean that every Schema v2 field is delivered literally. Champion IDs, UUIDs, raw item IDs, full trait lists, complete combat-stat maps and typed candidate records remain absent or transformed into aggregate/positional features as documented in the field crosswalk.

### Actor-only item compatibility

The 9×37 inventory-fit and 100×37 recipe-fit matrices are used by item action heads and removed from the value-head encoder input. The Actor receives those numeric compatibility scores; the Critic does not. The Critic still receives item semantic rows and unit target profiles, which are different features.

### Actor-only masks

The native mask arrays are separate from observations and are applied to Actor logits. The Critic ignores them. No action/mask contract ID/version/hash, mask snapshot hash or decision identity hash accompanies the current mask arrays.

### Shadow/diagnostic exclusion

The following remain outside the current PPO observation and value input:
- StrategicPlanner owner snapshots and commitment diagnostics;
- Composition Intelligence snapshots and transition diagnostics;
- UnifiedStrategicShadowRuntime JSONL;
- UnitPrioritySnapshot/anchor-candidate/candidate-generation diagnostic records;
- economic pressure scalars in PlayerInfo;
- action-evaluator recommendations and aggregate diagnostics;
- AntiLoopEngine history records.

The old PPO observation still includes selected legacy StrategyInfo features. Those legacy values are not proof that canonical Shadow evidence is delivered.

## 5. Machine-readable matrix

The crosswalk CSV now has 16 columns:
1. schema path;
2. schema type;
3. required flag;
4. source-map match;
5. source-map field;
6. inherited availability;
7. source nature;
8. current source;
9. formula/version;
10. source-map notes;
11. field-level proof status;
12. Python delivery;
13. PPO delivery;
14. next action;
15. current Actor delivery;
16. current Critic delivery.

All 223 unique schema paths have non-empty Actor and Critic delivery classifications. The CSV preserves the difference between:
- exact/aggregate/positional features delivered to a network;
- a raw identity field that is not delivered;
- a feature available only to the Actor;
- a diagnostic field outside both networks;
- a conditional feature whose native producer is not established.

## 6. Remaining integration gaps

1. **Decision correlation:** add explicit match/player/round/decision identity and sequence to observation and mask snapshots; reject stale/mismatched masks.
2. **Critic masks:** supply the exact native masks to the value path as required by the target contract, or prove a lossless alternative. Current `get_value` ignores them.
3. **Critic history:** decide and define any additional Markov/history context independently of masks. AntiLoopHistory is currently internal and not exported.
4. **Item fit semantics:** decide whether compatibility matrices belong in Critic context; current implementation gives them only to Actor. Do not change layout before Gate 8.
5. **Canonical strategic evidence:** build the post-Gate 8 producer/adapter path from canonical owner evidence; do not copy Shadow diagnostics or legacy StrategyInfo defaults into PPO.
6. **Projection manifest:** after producer and consumer decisions, define stable feature IDs, per-feature provenance/validity/missingness, normalization, ordering, catalog fingerprints and explicit Actor/Critic consumers.
7. **Replay/evaluation:** prove deterministic observation/mask pairing and replay the full producer→wrapper→policy→rollout chain under the accepted fixtures.

Issue #346 remains open. Gate 8 remains blocked. This audit makes no runtime, schema, tensor, PPO, reward, mask, training, checkpoint or Viewer changes.

## 7. Architecture reconstruction review

1. **Prior problem:** the crosswalk identified native/Python/PPO delivery but did not make the current Actor versus Critic consumer difference explicit for every Schema v2 path.
2. **Technical justification:** a shared encoder does not mean every input block is shared; item compatibility matrices are stripped from the value path, while masks are passed separately and ignored by the Critic.
3. **New responsibility:** the CSV Actor/Critic columns and this audit own the current per-path consumer trace; target consumer eligibility remains in the projection consumer matrix.
4. **Contract and invariants:** current delivery is not target approval; no raw identity inferred from positional features; no diagnostic/Shadow path treated as PPO input; masks remain independent legality inputs.
5. **Cross-component impacts:** TftEngine observation builder, pybind, CppTFTLobbyWrapper, Trainer, TFTPolicy encoder/Actor/item heads/value head, RolloutBuffer, schema crosswalk and future projection manifest.
6. **Objective validation:** all 223 paths have non-empty Actor/Critic classifications; policy source proves shared encoder, Actor-only item compatibility and Actor-only masks; no runtime or tensor-layout changes.



## 8. Target consumer decisions for the first new lineage — 2026-11-15

The current-delivery facts above remain unchanged. The initial target design is now clarified:

1. Actor and Critic must receive the exact same decision-correlated native mask snapshot as a separate side input. The current Critic ignoring masks is a migration gap, not the desired contract.
2. Item inventory/component facts and unit target-profile facts are shared semantic context. The 9×37 inventory-fit and 100×37 recipe-fit matrices remain Actor-specific conditional action-scoring inputs initially; they are not copied raw into the Critic. Any Critic summary must be derived from the same validated facts and versioned independently.
3. AntiLoopEngine history and untyped action-memory scalars are not projected as Critic history in the initial lineage. A later history feature requires typed identity/sequence, authoritative producer, reset behavior, replay fixtures and an ablation.
4. Encoder sharing/topology and all concrete dimensions remain open until the projection manifest and feature-to-consumer map are approved in Stage 0.

These target decisions do not change audited current-delivery classifications in the CSV and do not imply that the runtime currently conforms.
