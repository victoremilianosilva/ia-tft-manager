# Python Identity and Test-Hook Call-Site Inventory v1

**Status:** complete repository-wide Python static inventory for the audited revision; documentation only.  
**Target:** `new-arquiteture`.  
**Related:** #346; Unit Instance Copy and Test Hook Audit; Native Engine Instance and Episode Identity Scope Audit; Engine Identity Scope Reconciliation; Viewer/Engine Session Correlation Audit; Python Wrapper/Rollout Decision Correlation Audit.  
**Scope:** every tracked Python file present in the recursive Git tree at the time of this audit.

> This is a static call-site and semantic-use inventory. It does not claim Python tests were executed, does not replace C++ call-site analysis, and does not authorize runtime changes.

## 1. Prior problem

The earlier UnitInstance/test-hook audit traced the native implementations and pybind exposure, but the attempted repository-wide Python scan did not complete. Selected tests and wrapper files had been inspected, leaving uncertainty about whether fixture hooks or identity assumptions appeared elsewhere in Python.

This inventory closes that enumeration gap for the Python tree: all 125 tracked `.py` files were fetched and checked for the five known test-hook names, `UnitInstance`, `uuid`, `episode_id`, `engine_match_id`, and `match_id`.

## 2. Inventory coverage and method

| Category | Files enumerated | Files inspected |
|---|---:|---:|
| Root `tests/` and nested Python tests | 66 | 66 |
| Other Python files (wrappers, policy/training, Viewer, scripts, finetuning) | 59 | 59 |
| **Total** | **125** | **125** |

The scan used the `new-arquiteture` recursive Git tree and fetched each listed file at that ref. Matches were then reviewed by context to distinguish:
- actual calls into native fixture hooks;
- test fixtures and synthetic audit records;
- production diagnostic serialization/consumption;
- Viewer-owned session identity;
- native Engine episode metadata;
- strings and examples that merely contain an identifier field.

The scan is exhaustive for the Python files in that tree snapshot. It is not a claim about untracked local files, generated files absent from Git, other repositories, or C++ sources.

## 3. Test-hook call-site results

| Hook | Python references found | Classification |
|---|---|---|
| `set_unit_for_testing` | `tests/test_native_ppo_loop_regression.py`; `tests/test_tft_engine_api.py` | Test-only fixture setup |
| `set_shop_offer_for_testing` | `tests/test_tft_engine_api.py` | Test-only shop fixture injection |
| `set_next_shop_roll_for_testing` | None | No Python call site found |
| `set_unit_items_for_testing` | None | No Python call site found |
| `get_combat_team_for_testing` | None | No Python call site found |

No production Python module invokes the two hooks that are exposed through the inspected pybind chain. The C++-only item/combat hooks remain outside Python call-site coverage; their implementation and C++ callers must be assessed in native audits.

### 3.1 What the Python fixture calls prove

- `test_native_ppo_loop_regression.py` uses `set_unit_for_testing` to construct board fixtures before validating native masks and executor behavior. It is not a test of normal shop/pool acquisition.
- `test_tft_engine_api.py` uses `set_unit_for_testing` and `set_shop_offer_for_testing` to arrange a three-copy upgrade scenario. This verifies the scenario's resulting behavior under fixture injection, not the complete production draw/offer lifecycle.
- No Python call site uses `set_unit_items_for_testing`; therefore Python tests do not establish authoritative ItemEngine equip/inventory accounting through that fixture.
- No Python call site uses `set_next_shop_roll_for_testing`; deterministic queued-roll behavior remains supported only by native-side evidence already documented.

These results agree with the native hook semantics in the Unit Instance Copy/Test Hook Audit: fixture hooks must not be used as sole evidence for production ownership, pool, item, or offer-generation lifecycle.

## 4. Identity references found in Python

### 4.1 Native episode identity

`tests/test_tft_engine_api.py` verifies that successive native resets advance `episode_id` and that an invalid reset does not advance it. This is useful evidence for episode progression within one Engine object. It does not establish a globally unique Engine-instance scope or cross-object uniqueness.

The Python wrapper/training path remains as documented in the wrapper/rollout audit: native result dictionaries preserve `episode_id`, while `CppTFTLobbyWrapper` drops it from the training-facing reset/step outputs. The Python tree contains no alternate canonical Engine-instance identity producer.

### 4.2 Viewer session identity

`viewer/session.py` creates `match_id` with `uuid.uuid4()` when a Viewer session starts. It writes that value into Viewer metadata and events and copies it into the `match_id` field of composition diagnostic records. The same diagnostic correlation envelope preserves native `engine_match_id` as a separate field and records `sequence_id` from the diagnostic record.

The Viewer also labels the source as `ViewerSession.match_id`. This confirms the ownership distinction: the Viewer UUID identifies the Viewer recording/session, not the native Engine episode. The existing `identity_complete` predicate checks integer `player_id`, `round`, and `sequence`; it does not prove a globally unique Engine scope or canonical typed decision sequence.

### 4.3 Audit and Viewer UUID usage

The remaining Python UUID references are used for identity-aware audit and diagnostics, not as a new UUID producer:
- `viewer/player_logs.py`, `viewer/main.py`, and `viewer/audit_window.py` serialize or display UUIDs from native audit snapshots.
- `scripts/audit_viewer_match.py` uses UUIDs to correlate unit additions, removals, purchases, sales and current ownership inside one recorded match.
- `scripts/strategic_audit_state.py`, `scripts/audit_native_ppo_loops.py`, and `scripts/summarize_economy_audit.py` use UUIDs to distinguish unit records in state signatures and audit calculations.
- `tests/test_purchase_sequence_audit.py`, `tests/test_strategic_audit_state.py`, `tests/test_validate_strategic_cycles.py`, and Viewer/audit tests use synthetic UUID strings to verify duplicate-champion distinction, ownership changes, and audit behavior.
- Other audit fixtures use values such as `unit-0`, `u1`, or `unit-uuid`; these are test data, not factory-generated identities.

These call sites support the intended local use of UUID as a physical-unit correlation token within a snapshot/match audit. They do not establish cross-episode global uniqueness. The C++ factory/reset findings remain controlling for that limitation.

## 5. Schema validator cross-check

`scripts/validate_observation_schema.py` currently computes `decision_identity_hash` from the six fields:
- `match_id`;
- `engine_match_id`;
- `player_id`;
- `round`;
- `decision_sequence`;
- `snapshot_sequence`.

The validator checks that the mask reference carries the same decision identity hash and that incomplete identity does not carry a hash. It does not independently establish that the two sequence fields have producer-owned namespace semantics. This matches the documented Schema v2 design gap: the Python validator validates the declared envelope but cannot prove source ownership, native Engine-instance scope, or transport correlation that producers do not emit.

No alternative Python hash implementation or competing canonical identity owner was found in this inventory.

## 6. Consolidated conclusions

1. The earlier Python scan limitation is closed for the 125 tracked files in the audited repository tree.
2. Python fixture-hook usage is limited to two test files and two hook names: `set_unit_for_testing` and `set_shop_offer_for_testing`.
3. No Python references were found for `set_next_shop_roll_for_testing`, `set_unit_items_for_testing`, or `get_combat_team_for_testing`.
4. No production Python module was found minting native UnitInstance UUIDs or Engine-instance identity.
5. Viewer `match_id` is generated by ViewerSession and remains separate from native `engine_match_id`/episode metadata.
6. Unit UUIDs are consumed by Viewer and audit paths as local physical-unit correlation tokens; they are not upgraded into cross-episode identity.
7. The schema validator enforces hash equality and completeness rules but cannot supply missing namespace/producer semantics.
8. The inventory does not prove the C++ producer/caller universe complete; C++ audit evidence remains governed by the separate native documents.

## 7. Ownership and required boundaries

| Concern | Responsible owner | Boundary |
|---|---|---|
| UnitInstance UUID creation | Native UnitInstanceFactory | Python consumers preserve, never mint or repair it |
| Engine episode progression | Native Engine | Python transports the native episode reference without re-derivation |
| Engine-instance scope | Not currently produced in audited native/Python paths | Must be decided and produced by an authoritative Engine lifecycle owner |
| Viewer session UUID | ViewerSession | Session/recording identity only |
| Player seat/index | Native lobby/player array | Episode-local position, not persistent player identity |
| Decision/snapshot sequence namespaces | Actual native producers (not proven complete) | Must be typed and source-owned before canonical joins |
| Test fixture hooks | Native test APIs invoked by tests | Fixture setup only; not production lifecycle evidence |
| PPO transition correlation | Wrapper, vector environment, Trainer/RolloutBuffer | Must preserve exact typed references; storage order/call order are not identity |

## 8. Architecture reconstruction review

1. **Prior problem:** the previous native hook audit had not completed its attempted Python-wide call-site scan, leaving repository-level uncertainty.
2. **Technical justification:** fixture hooks, diagnostic UUIDs and Viewer session IDs can be mistaken for production identity/ownership if their call sites are not classified.
3. **New responsibility:** this inventory owns the complete tracked-Python enumeration and classification of fixture-hook and identity-field references for the audited tree revision.
4. **Contract and invariants:** test hooks are fixture-only; Python does not mint native UnitInstance or Engine identity; Viewer session UUID remains distinct; native UUID is not globally unique by itself; schema validation cannot invent missing source namespaces.
5. **Cross-component impacts:** native pybind hooks, test suite, UnitInstanceFactory, Engine episode lifecycle, Viewer/session logs, audit scripts, schema validator, wrapper, vector environment and PPO rollout.
6. **Objective validation:** all 125 tracked Python files were enumerated and inspected; the five hook names and identity fields were checked; all found hook references were classified; no runtime or test code was modified.

## 9. Remaining work and gate status

The Python enumeration gap is closed. The following are still separate acceptance tasks:
- finish/reconcile the native C++ caller inventory where not already proven;
- decide and implement (only after Gate 8 authorization) an authoritative Engine-instance scope and typed decision/snapshot sequence producers;
- transport native episode/identity references through wrapper, vector environment and rollout;
- prove Viewer-to-Engine mapping and terminal auto-reset correlation;
- complete all 17 structured entity producer audits and integrated replay acceptance.

Issue #346 remains open until the full 17-entity producer audit and end-to-end evidence are complete. Gate 7 executable replay/evaluation remains pending. Gate 8 remains blocked pending integrated review of Gates 1–7 and explicit user authorization.

No runtime, test, observation, mask, reward, PPO, Viewer, checkpoint, or tensor behavior is changed by this document.
