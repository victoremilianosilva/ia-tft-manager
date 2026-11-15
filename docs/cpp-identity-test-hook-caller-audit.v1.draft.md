# C++ Identity and Test-Hook Caller Audit v1

**Status:** source-backed targeted audit; documentation only.  
**Target:** `new-arquiteture`.  
**Tracking:** issue #346.  
**Related:** Unit Instance Copy/Test Hook Audit; Shop Offer Identity/Reroll Lifecycle Audit; Engine Episode Identity Reset Reconciliation; Native Engine Instance and Episode Identity Scope Audit; Python Identity/Test-Hook Call-Site Inventory.

> This audit completes the C++ test-suite call-site pass and reconciles it with the native implementation and binding surfaces already traced. It does not claim a grep-equivalent exhaustive scan of every production C++ translation unit.

## 1. Prior problem

The prior hook audit established the implementation semantics and Python binding exposure, but did not yet record a consolidated C++ test-caller inventory. That left ambiguity about which test hooks are exercised by native tests, which are only declared/bound, and which identity fields are consumed by native test helpers.

## 2. Coverage and method

The recursive `new-arquiteture` tree contains 127 tracked C++ source/header files, including 48 files under `cpp/tests/`. All 48 C++ test files were fetched and inspected for:
- `set_unit_for_testing`;
- `set_shop_offer_for_testing`;
- `set_next_shop_roll_for_testing`;
- `set_unit_items_for_testing`;
- `get_combat_team_for_testing`;
- `UnitInstance`, `generate_uuid`, `episode_id`, and `uuid`.

The native implementation/binding surfaces reviewed for this reconciliation include:
- `cpp/include/lobby/TftEngine.hpp`;
- `cpp/src/lobby/TftEngine.cpp`;
- `cpp/bindings/tft_engine_bindings.cpp`;
- `cpp/include/lobby/UnitInstanceFactory.hpp`;
- `cpp/src/lobby/UnitInstanceFactory.cpp`;
- `cpp/include/lobby/ShopEngine.hpp` and `cpp/src/lobby/ShopEngine.cpp`;
- `cpp/include/items/ItemEngine.hpp` and `ItemActionContract.hpp`;
- `cpp/include/decision/DecisionState.hpp`;
- `cpp/src/decision/AntiLoopEngine.cpp` and `decision_bindings.cpp`.

This is a complete C++ test-file enumeration, with a targeted implementation/binding cross-check. It is not a claim that every one of the 79 non-test C++ files was exhaustively scanned for every possible indirect caller.

## 3. Native test-hook callers

The only C++ test file with direct calls to the Engine test hooks is `cpp/tests/test_tft_engine_pool.cpp`.

| Hook | C++ test caller | What the fixture is used for |
|---|---|---|
| `set_unit_for_testing` | `test_tft_engine_pool.cpp` | Populate board/bench states for pool, strategy, item, and action scenarios |
| `set_shop_offer_for_testing` | `test_tft_engine_pool.cpp` | Inject a known champion offer for purchase/reversal scenarios |
| `set_unit_items_for_testing` | `test_tft_engine_pool.cpp` | Populate the UnitInstance item mirror for audit/fixture checks |
| `get_combat_team_for_testing` | `test_tft_engine_pool.cpp` | Read a fixture combat team for item propagation assertions |
| `set_next_shop_roll_for_testing` | No direct C++ test caller found in the 48-file test tree | Declared/implemented and Python-bound, but not exercised by the inspected C++ tests |

The direct hook references are concentrated in the pool/lifecycle integration test. Other C++ tests use independent fixtures or lower-level objects; they do not call these TFTEngine fixture APIs.

### 3.1 What this means

- The Engine fixture hooks are not broadly called across the C++ test suite.
- The item fixture hook is exercised by the pool/lifecycle integration test, but its implementation still writes the UnitInstance mirror rather than ItemEngine's authoritative UUID-keyed ownership map.
- `get_combat_team_for_testing` is used to inspect the resulting combat-team fixture; it is not an execution API.
- Absence of a C++ test caller for `set_next_shop_roll_for_testing` is a coverage gap, not proof that the method is dead or incorrect.
- Fixture-hook tests must not be used as standalone proof of ordinary shop draw, purchase, pool accounting, or authoritative ItemEngine inventory/equipment transactions.

## 4. Binding boundary

`cpp/bindings/tft_engine_bindings.cpp` exposes:
- `set_unit_for_testing`;
- `set_shop_offer_for_testing`;
- `set_next_shop_roll_for_testing`;
- read-only `episode_id`.

The same binding file's reset/step dictionary conversion preserves native `episode_id`.

The inspected binding chain does **not** expose:
- `set_unit_items_for_testing`;
- `get_combat_team_for_testing`.

Those two methods remain native C++ test hooks in the audited pybind surface, despite their declarations and definitions in the public Engine header/implementation. This matches the Python call-site inventory: no Python references were found for either method.

## 5. Identity-bearing native test usage

The 48-file test scan found several lower-level identity uses that are distinct from Engine fixture-hook calls:

- `test_unit_instance_factory.cpp` creates two instances from one seeded factory and asserts their UUIDs differ. It does not test same-seed factory reproduction, cross-reset collisions, or cross-Engine uniqueness.
- `test_shop_engine.cpp` records offer UUIDs and verifies a locked shop preserves the same physical offers. This tests identity preservation under lock, not a separate offer ID/revision/generation.
- `test_action_mask_engine.cpp` and `test_anti_loop_engine.cpp` construct decision-state unit identities with UUID values.
- `test_item_engine.cpp` and `test_planner_evidence_adapters.cpp` use UUID-keyed equipment/profile fixtures.
- `test_combat_engine.cpp` uses a unit UUID to target equipped-item behavior.

These tests demonstrate local UUID-based distinction and propagation in their respective fixtures. They do not establish globally unique identity across Engine objects or episodes.

## 6. Native owner and implementation cross-check

### 6.1 UnitInstance and UUID producer

`UnitInstance` is declared in `TftEngine.hpp`; UUID creation is implemented by `UnitInstanceFactory::generate_uuid()`, called from `UnitInstanceFactory::create()`.

The factory is seeded deterministically. Engine reset reconstructs it from the base seed, so repeated same-seed creation order can repeat UUIDs across resets/independent Engine objects. The UUID remains an instance token, not a globally unique identity.

### 6.2 Engine episode identity

`TFTEngine::Impl` owns numeric `episode_id`, incremented on reset. The native reset/step result structures and pybind dictionaries preserve it. The earlier Python wrapper audit establishes where that value is dropped before Trainer/RolloutBuffer.

The C++ test suite includes reset/episode checks, but does not prove a distinct Engine-instance scope token. No such token was found in the audited Engine constructor/reset/move/result/binding surfaces.

### 6.3 Item ownership and decision history

- `ItemEngine` stores equipped items by `UnitInstance::uuid`; this is a local ownership key under the current Engine lifecycle, not an independent global identity.
- `DecisionState::UnitIdentity` prefers UUID when present and falls back to champion/numeric identity plus star tier according to its comparison semantics.
- `AntiLoopEngine` hashes that identity for bounded movement-history signatures.
- These consumers rely on the same scoped UUID semantics; none upgrades the UUID to an Engine-instance or episode-global key.

## 7. Consolidated findings

1. All 48 tracked C++ test files were inspected for the five test-hook names and identity fields.
2. Direct C++ TFTEngine fixture-hook calls are confined to `test_tft_engine_pool.cpp`.
3. `set_next_shop_roll_for_testing` has no direct caller in the inspected C++ test tree.
4. The pybind surface exposes three fixture hooks and native `episode_id`; it does not expose the item fixture hook or combat-team test getter.
5. Native test UUID usage proves local distinction/preservation in individual scenarios, not cross-Engine uniqueness.
6. The authoritative UUID producer remains UnitInstanceFactory; the Engine episode counter remains local to one Impl lifetime.
7. The C++ test-file enumeration is complete; a whole-production-source caller enumeration remains explicitly outside this audit's claim.

## 8. Architecture reconstruction review

1. **Prior problem:** native hook semantics were documented, but the C++ test caller set and binding boundary were not consolidated.
2. **Technical justification:** fixture API declaration, binding exposure, test caller, and production ownership are separate facts; conflating them overstates test coverage and lifecycle guarantees.
3. **New responsibility:** this note owns the C++ test-hook caller inventory and its reconciliation with native identity-bearing tests and binding exposure.
4. **Contract and invariants:** fixture hooks are not production lifecycle evidence; UUID is a scoped instance token; episode_id is Engine-object-local; bound and unbound test APIs remain explicitly distinguished.
5. **Cross-component impacts:** TFTEngine, pybind, UnitInstanceFactory, ShopEngine, ItemEngine, DecisionState/AntiLoopEngine, C++ tests and Python tests.
6. **Objective validation:** all 48 C++ test files were enumerated and inspected; direct callers were identified; implementation/binding declarations were cross-checked; no runtime or test code was modified.

## 9. Remaining work and gate status

The C++ test-hook caller inventory is closed for the tracked test tree. The full production C++ caller graph is not claimed complete. Remaining identity acceptance still requires:
- an authoritative Engine-instance scope decision and producer;
- typed native decision/snapshot sequence producers;
- exact transport through native results, pybind, wrapper, vector environment and PPO rollout;
- Viewer-to-Engine correlation and terminal auto-reset proof;
- complete producer proof for all 17 structured entity kinds and integrated replay acceptance.

Issue #346 remains open. Gate 7 executable replay/evaluation remains pending. Gate 8 remains blocked pending integrated review of Gates 1–7 and explicit user authorization.

No runtime, test, action, mask, reward, observation, PPO, Viewer, checkpoint, or tensor behavior is changed by this document.
