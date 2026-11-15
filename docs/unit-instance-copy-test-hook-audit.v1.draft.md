# UnitInstance Copy Semantics and Test-Hook Audit v1 — Draft

**Status:** source-backed lifecycle/test audit; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Purpose and prior gap

The existing UnitInstance lifecycle audit established that UUIDs are generated from a seeded factory and can repeat after a same-seed Engine reset. Follow-up inventories have now inspected all 125 tracked Python files and all 127 tracked C++ files for explicit identity and test-hook references. Implicit C++ value-copy/assignment/destruction lifecycle proof remains unfinished.

This follow-up records:
- the actual C++ value/copy semantics of UnitInstance;
- the factory's deterministic UUID generation and current test coverage;
- production ownership-transfer surfaces versus diagnostic copies;
- test-only hooks that create or mutate units outside normal shop/pool/item lifecycle;
- the missing regression cases required before accepting physical identity.

No runtime, schema, PPO, reward, mask, training, checkpoint, Viewer, Overwolf or tensor behavior is changed.

## 2. UnitInstance and factory semantics

### 2.1 UnitInstance is an implicitly copyable value

`UnitInstance` is a public struct containing champion catalog reference, champion string, UUID, star and a vector of `CombatItem`. It declares no custom copy/move constructor, assignment operator, deleted copy operation or identity registry. Ordinary C++ value-copy semantics therefore copy the UUID string and item vector along with the rest of the object.

Consequences:
- copying a UnitInstance does not mint a new physical identity;
- two simultaneously retained copies can carry the same UUID;
- move operations preserve the UUID value while transferring the object's value state;
- code must distinguish an ownership transfer/move from a diagnostic/value copy;
- `is_valid()` checks only non-negative champion ID and non-empty UUID; it does not prove uniqueness or ownership.

Source: `cpp/include/lobby/TftEngine.hpp`, `UnitInstance` declaration (approximately lines 105–145).

### 2.2 Factory UUID generation is deterministic within a seed lineage

`UnitInstanceFactory` owns `std::mt19937_64` initialized directly from its constructor seed. `create()` validates the champion catalog entry, initializes a new UnitInstance and calls `generate_uuid()`. The UUID-shaped string uses 128 generated bits, then sets version/variant bits to the UUID v4 pattern.

This is deterministic pseudorandom generation, not a globally coordinated UUID service:
- the same factory seed and same create-call order reproduce the same UUID sequence;
- Engine reset reconstructs the factory with the reset seed;
- the same-seed reset can therefore reproduce UUIDs from the prior episode;
- no match/player namespace, episode nonce, collision registry or cross-engine uniqueness authority is present.

Source: `cpp/include/lobby/UnitInstanceFactory.hpp`; `cpp/src/lobby/UnitInstanceFactory.cpp`; Engine construction/reset callsites in `cpp/src/lobby/TftEngine.cpp` (factory initialization near lines 690 and 6219).

## 3. Ownership surfaces and copies

| Surface | Observed operation | Identity implication |
|---|---|---|
| Shop draw | Factory creates a UnitInstance placed in one shop slot | New UUID in current factory sequence |
| Shop purchase | `ShopEngine::take_unit` returns/moves the existing offer value | Purchase should preserve the offer UUID; no new identity is generated |
| Board/bench placement | UnitInstance values are moved/assigned between optional slots | Ownership location changes; UUID should remain unchanged |
| Merge | Existing lifecycle transfers equipment to the surviving purchased/base UUID and consumes other copies | One identity survives; consumed UUIDs retire from active ownership |
| Sale | Sold unit is removed from its slot after equipment return and pool-copy return | UUID leaves active player ownership |
| Elimination | Board/bench slots are cleared and champion copies returned | Unit UUIDs leave active ownership; item map cleanup is separately audited in #370 |
| Audit snapshot | Unit records are copied into diagnostic snapshot structures | Diagnostic copy is not a second owned unit |
| Combat/strategic local DTOs | Some builders copy champion/UUID or selected unit attributes into local values | DTO copy is not proof of another owned instance; each consumer must retain identity semantics explicitly |

A copied UUID is not automatically a duplicate live unit: the diagnostic and temporary local copies are expected. The actual invariant to prove is uniqueness among simultaneously owned physical units in the authoritative shop/board/bench domains for a given Engine/player/episode scope, with explicit exceptions for read-only copies.

## 4. Test-only hooks are not production lifecycle evidence

### 4.1 `set_unit_for_testing`

The hook calls the same UnitInstanceFactory to create a new unit, sets its star value and directly assigns it into a board or bench optional. It then registers position state, updates strategy and refreshes masks.

It does not use the normal shop purchase or pool transaction path. It can overwrite an occupied fixture slot directly; the audited implementation does not first return the overwritten unit's champion copies to the pool or return its equipment through ItemEngine.

This is suitable for isolated fixtures, but tests using it cannot prove shop/pool accounting, sale, merge, or physical ownership lifecycle by themselves.

Source: `cpp/src/lobby/TftEngine.cpp`, `TFTEngine::set_unit_for_testing` (approximately lines 6778–6829).

### 4.2 `set_unit_items_for_testing`

This hook validates supplied CombatItem fields and directly writes the vector to `UnitInstance::items` on a board/bench unit. It does not populate the ItemEngine's UUID-keyed `equipped_` map or consume a catalog item from the player's inventory.

Therefore, tests that use this hook to attach fixture items prove the UnitInstance mirror/snapshot path, not the authoritative ItemEngine ownership transfer path. They must not be used as evidence that sale/merge/elimination item accounting is correct.

Source: `cpp/src/lobby/TftEngine.cpp`, `TFTEngine::set_unit_items_for_testing` (approximately lines 6839–6880).

### 4.3 Shop fixture hooks

`set_shop_offer_for_testing` creates a new factory UnitInstance and installs it through `ShopEngine::set_offer_for_testing`. This bypasses ordinary probability/draw behavior and should be treated as a fixture injection. `set_next_shop_roll_for_testing` configures champion IDs for a later deterministic roll; it does not define a stable offer ID or revision.

Source: `cpp/src/lobby/TftEngine.cpp` (approximately lines 6910 onward); `cpp/include/lobby/ShopEngine.hpp`.

## 5. Existing tests and what they actually prove

### 5.1 Factory test

`cpp/tests/test_unit_instance_factory.cpp` creates two units from one factory seeded with 12345 and asserts:
- both values are valid;
- their UUID strings differ;
- both refer to the same champion;
- both start at one star;
- an invalid champion ID is rejected.

It does **not** construct a second factory with the same seed, reset an Engine and compare UUIDs across episodes, test copies/assignments, or assert global uniqueness.

### 5.2 Engine pool/lifecycle test

`cpp/tests/test_tft_engine_pool.cpp` checks pool totals across a same-seed Engine reset and contains numerous fixtures using `set_unit_for_testing`, shop injection and item fixture hooks. The inspected reset assertions validate pool totals and player economy state; they do not compare pre-reset and post-reset UnitInstance UUID sets.

The test also verifies buy/sell behavior using the UUID of the purchased unit to identify the exact new bench copy. That is useful lifecycle evidence for a single episode, but it does not prove cross-episode uniqueness.

### 5.3 Missing test coverage

No audited test currently proves all of the following:
1. two factories with the same seed and same create order reproduce the same UUID sequence (documented deterministic behavior);
2. Engine reset with the same seed reproduces UUIDs, so a bare UUID is not episode-global;
3. copied UnitInstance values preserve UUID and are classified as non-owning copies where appropriate;
4. no two simultaneously owned shop/bench/board units in one active Engine scope share a UUID;
5. purchase/move/swap preserve the exact UUID without generating another one;
6. merge retains exactly the intended survivor UUID and retires consumed UUIDs;
7. sale/elimination remove retired UUIDs from active ownership and do not leave reachable item-target references;
8. fixture hooks are excluded from tests that claim to prove production pool/item lifecycle;
9. the ItemEngine equipment map and UnitInstance item mirror remain consistent across authoritative equip/sale/merge/reset paths.

These are future executable acceptance criteria, not tests run by this documentation-only change.

## 6. Identity contract implications

The evidence supports a narrow conclusion: current UUID is a deterministic per-factory creation token that follows UnitInstance value copies and moves. It is useful for correlating one live object lineage within an episode, but it is not a sufficient standalone physical identity across reset/replay episodes or across Engine/player scopes.

A future identity contract must distinguish:
- **instance token:** current UUID-shaped factory value;
- **episode/Engine scope:** unique namespace that prevents same-seed reset collisions;
- **player ownership scope:** player identity where required by cross-player records;
- **ownership location:** shop/bench/board domain and slot, which can change without changing the instance token;
- **diagnostic copy:** non-owning copy of an instance record;
- **retirement:** sale, merge consumption, elimination and reset semantics.

Do not synthesize a globally unique ID from champion ID, slot, round or factory call order in the adapter. The accepted identity must be produced or scoped by an authoritative owner and transported with explicit provenance/sequence.

## 7. Architecture reconstruction review

1. **Prior problem:** the lifecycle audit knew the UUID was seed-deterministic but had not documented implicit copy semantics, test-hook bypasses or the exact limits of existing tests.
2. **Technical justification:** value copies preserve UUID; test hooks can bypass pool and ItemEngine transactions; same-seed factory reset repeats identifiers. Treating all UUID occurrences as independent physical units would corrupt ownership/replay semantics.
3. **New responsibility:** this note owns the distinction between instance token, ownership transfer, diagnostic copy and fixture injection; UnitInstanceFactory remains the current token producer.
4. **Contract and invariants:** no UUID minting on copy/move; diagnostic copies are non-owning; authoritative live ownership is distinct from fixture writes; same-seed cross-episode uniqueness is not guaranteed; no synthetic cross-episode identity.
5. **Cross-component impacts:** UnitInstance, UnitInstanceFactory, ShopEngine, PlayerEnv, UnitPool, ItemEngine, audit snapshot, test hooks, C++ fixtures, pybind, Python wrapper, structured schema and replay.
6. **Objective validation:** factory and test-hook implementations are traced; existing test claims are bounded to their actual assertions; missing regression cases are enumerated; no runtime or tensor change is made.

Issue #346 remains open. Gate 8 remains blocked.

## 8. Cross-check of fixture exposure and stale identity comment — 2026-11-15

### 8.1 Native declaration comment is stale

`cpp/include/lobby/TftEngine.hpp`, immediately above `UnitInstance::uuid`, still says: `A geração efetiva do UUID será implementada posteriormente.` That statement is contradicted by the current implementation: `UnitInstanceFactory::create()` assigns `unit.uuid = generate_uuid()`, and `generate_uuid()` constructs the UUID-shaped value from its seeded `std::mt19937_64` stream. This is a stale source comment, not evidence that UUID generation is absent. It should be corrected in a future code change, but this audit does not edit runtime/header code.

### 8.2 Fixture hooks: native versus Python exposure

| Hook | Native behavior | Python binding in inspected `tft_engine_bindings.cpp` | Identity/lifecycle boundary |
|---|---|---|---|
| `set_unit_for_testing` | Creates a factory unit and writes directly to board/bench slot; may overwrite an occupied slot without production pool/item cleanup | Exposed | Fixture-only ownership injection; does not prove shop/pool lifecycle |
| `set_unit_items_for_testing` | Writes `UnitInstance::items` mirror directly; does not update ItemEngine UUID-keyed equipment or inventory | Not exposed in inspected pybind chain | C++ fixture-only item mirror mutation |
| `set_shop_offer_for_testing` | Creates a factory unit and calls `ShopEngine::set_offer_for_testing`; that method takes the champion from pool and returns replaced offer's champion copy | Exposed | Bypasses normal weighted draw, but retains explicit pool accounting; offer has no stable offer ID/revision |
| `set_next_shop_roll_for_testing` | Queues five champion catalog IDs for a later deterministic `ShopEngine::roll`; forced roll still checks/takes pool copies and creates units through factory | Exposed | Controls fixture draw outcome; does not establish offer identity or ordinary RNG/odds behavior |
| `get_combat_team_for_testing` | Read-only conversion to CombatTeam for a selected player/team | Not exposed in inspected pybind chain | Diagnostic/test projection; does not create or transfer UnitInstance ownership |

The inspected pybind chain also exposes item grant fixture helpers and player/economy fixtures, but those do not create or copy UnitInstance values directly. Their presence must not be confused with the four unit/shop fixture surfaces above.

### 8.3 Disposition

The prior audit's ownership conclusions remain unchanged. This follow-up narrows the fixture boundary and identifies a stale source comment. The header comment is not silently treated as runtime truth; implementation and tests remain the evidence. No test hook is promoted to production lifecycle evidence.

## 9. Architecture reconstruction review

1. **Prior problem:** the copy/test-hook audit did not distinguish which fixture hooks cross the Python binding boundary, and the native UnitInstance declaration retains an outdated statement that UUID generation is future work.
2. **Technical justification:** source comments can lag implementation; Python-visible fixtures and C++-only fixtures have different reachability, while both remain non-production evidence.
3. **New responsibility:** this addendum owns the cross-check between UnitInstance fixture declarations/implementations and the inspected pybind surface, plus the stale-comment discrepancy.
4. **Contract and invariants:** implementation is authoritative over stale comments; fixture writes do not establish production ownership; `set_unit_items_for_testing` only mutates the mirror; shop fixtures retain pool accounting where the implementation explicitly performs it; no stable offer identity is inferred.
5. **Cross-component impacts:** UnitInstance declaration/factory, TFTEngine test hooks, ShopEngine, ItemEngine, pybind, C++ tests, Python parity fixtures and the physical-identity audit.
6. **Objective validation:** each listed hook is traced to declaration/implementation and checked against the binding chain; native and Python exposure are distinguished; the UUID comment is compared against the actual factory implementation. Documentation only.
