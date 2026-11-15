# Schema v2 Legal State, Anti-Loop and Critic Context Field Proof v1 — Draft

**Status:** source-backed field-level audit; documentation only, not runtime-approved.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope

This slice reconciles the final 46 ancestor-matched paths:
- 32 `legal_state_context.anti_loop_state` fields;
- 10 `legal_state_context.mask_reference` fields;
- 4 `legal_state_context.critic_context` fields.

The key distinction is between internal AntiLoopEngine state, the actual mask arrays transported to policy, and the value head's current observation representation. None of these should be converted into a synthetic sequence-bound legal-state envelope.

## 2. AntiLoopEngine: internal bounded history, not exported event ledger

### 2.1 Internal data model

`AntiLoopHistory` stores position signatures, move records, blocked-move records, state visits, a state-visit index, last board signature, last move, execution metrics, current round and state-window length (`DecisionHistory.hpp:102-120`).

The underlying record contracts are narrower than Schema v2:
- `PositionSignature` contains board and bench arrays of `UnitIdentity`; its cached hash is a native `size_t` hash and is deliberately excluded from equality. `UnitIdentity` prefers UUID when present and otherwise compares champion identity plus star (`DecisionHistory.hpp:15-35`; `DecisionState.hpp:13-48`).
- `StateVisit` contains signature, visit count, repeated flag and last-seen round; it has no decision sequence.
- `MoveRecord` contains move type, source slot, target slot, optional unit identity and optional displaced-unit identity; it has no round, decision sequence or resulting-state hash.
- `BlockedMoveRecord` wraps a MoveRecord and optional blocked PositionSignature; it has no stored block reason, round or decision sequence (`DecisionHistory.hpp:38-63`).

### 2.2 Retention and reset semantics

Defaults are `history_size=20`, `blocked_move_size=10`, and `loop_threshold=2` (`AntiLoopEngine.hpp:22-26`). `AntiLoopHistory.state_window_rounds` defaults to 8 (`DecisionHistory.hpp:117-120`).

On episode reset, AntiLoopEngine clears history while preserving accumulated execution metrics and the state-window value. On `begin_round`, it clears position history, retains at most six movement records across the round boundary, clears blocked moves, resets the last board signature, and expires state visits older than the eight-round window (`AntiLoopEngine.cpp:102-147`). The six-move cross-round tail is a local constant, not a serialized configuration field.

### 2.3 Internal summary versus public export

`AntiLoopEngine::get_state()` returns only a summary: current position-history size, move-history size, blocked-move count, known-state count and optional last move (`AntiLoopEngine.hpp:143-154`; `AntiLoopEngine.cpp:720-727`). It does not return the ordered history collections.

The audited TFTEngine/pybind/Python surface exposes `get_anti_loop_metrics()`, which exports aggregate counters such as execution attempts/blocks, block categories, executed moves and mask-generation diagnostics. It does not expose `get_state()` or the underlying history vectors (`TftEngine.cpp:7196-7245`; `tft_engine_bindings.cpp:887-891`; `cpp_lobby_env.py:228-229`).

### 2.4 Per-field consequences

- Current counts and last move exist in an internal summary but are not exported through TFTEngine.
- Position history has no per-entry round or sequence. It is cleared each round.
- Move records have type/source/target and optional physical identities, but no round, decision sequence or result-state hash.
- Blocked records have nested move parameters and optional blocked signature, but no stored reason; `get_block_reason()` computes a transient reason on query (`AntiLoopEngine.cpp:610-649`).
- State visits have count and last-seen round, but no last-seen sequence.
- A native `size_t` hash is not the schema's SHA-256 state hash. No SHA-256 fingerprint is serialized for these records.

Anti-loop checks influence native move validation and mask generation. That legality effect remains separate from any future history projection; history is not a replacement for exact native masks.

## 3. Mask reference: real arrays, no identity/version/hash envelope

### 3.1 Native mask producers

`ActionMaskBatch` contains action-type, shop, bench-source, board-source/target and conditioned movement masks, per-source movement matrices, availability flags and generation diagnostics (`ActionMaskEngine.hpp:14-46`). `PlayerActionMasks` stores the corresponding arrays, including item masks (`TftEngine.hpp:166-190`).

`TftEngine::refresh_masks` builds a current `PlayerState`, calls `ActionMaskEngine::generate_masks` with the current AntiLoopEngine, records mask diagnostics, and copies the arrays into the player's stored masks (`TftEngine.cpp:1037-1069`). The Engine returns those masks from `get_action_masks()`; pybind converts them to dictionaries of arrays, without a metadata envelope (`TftEngine.cpp:6574-6585`; `tft_engine_bindings.cpp:100-110,876-880`).

The static action shape exists as `kActionDims{9,5,9,28,28,28}`, but it is not accompanied by a runtime action-contract ID, version or hash (`TftEngine.hpp:18-25`). Neither `ActionMaskBatch` nor `PlayerActionMasks` carries mask-contract identity, mask snapshot hash or decision identity hash.

### 3.2 Python, Actor and Critic boundary

The Python wrapper returns mask arrays; the Trainer flattens them into per-agent tensors and passes them separately to policy inference. RolloutBuffer stores masks in a separate dictionary alongside observations/actions/rewards, rather than embedding mask metadata in the observation (`cpp_lobby_env.py:185-205`; `trainer.py:480-545`; `rollout.py:217-231,237-406`).

The policy applies masks to Actor logits during action selection. Native masks remain the final legality input. No mask-reference status, reason, contract identifier/version/hash, snapshot hash or decision-identity hash travels with the arrays.

## 4. Critic context: shared observation encoder, no separate context envelope

The policy's `encode(obs)` validates and encodes the same flat observation for the action and value paths. The value estimator is `value_head(encode(obs))`; `get_value(obs, masks=None)` explicitly ignores masks (`policy.py:271-304,528-530`). The Actor path uses the same encoded features before applying masks to action logits (`policy.py:710-721`).

The Trainer passes `next_masks` to `get_value`, but the value method ignores them. RolloutBuffer stores observation and masks separately; it does not store a separate critic-context object or source decision sequence (`trainer.py:1465-1482`; `rollout.py:237-406`).

Therefore, current Critic representation is the shared encoded observation, not a distinct structured `critic_context`. No status, source decision sequence or reason envelope is produced. This documents current behavior only; it does not decide the future Critic projection or tensor layout.

## 5. Field-level dispositions

| Schema path | Source-backed evidence | Python/PPO surface | Disposition |
|---|---|---|---|
| `legal_state_context.anti_loop_state.status` | No status field in AntiLoopHistory/Summary | No parent status export | `not_produced_parent_status` |
| `legal_state_context.anti_loop_state.history_size` | Internal position-history count in get_state summary | get_state not exposed | `internal_position_history_count` |
| `legal_state_context.anti_loop_state.move_history_size` | Internal move-history count in get_state summary | get_state not exposed | `internal_move_history_count` |
| `legal_state_context.anti_loop_state.blocked_moves` | Internal blocked-record count in summary | Aggregate metrics only | `internal_blocked_move_count` |
| `legal_state_context.anti_loop_state.known_states` | Internal state-visit count in summary | get_state not exposed | `internal_state_visit_count` |
| `legal_state_context.anti_loop_state.last_move` | Optional internal MoveRecord in summary | Not exported; record lacks round/sequence | `internal_optional_move_record` |
| `legal_state_context.anti_loop_state.state_window_rounds` | Internal default 8-round state expiry | No serialized configuration | `internal_history_window_default_8` |
| `legal_state_context.anti_loop_state.cross_round_move_window` | Local six-record retention constant | No serialized configuration | `internal_begin_round_constant_6` |
| `legal_state_context.anti_loop_state.blocked_move_size` | AntiLoopConfig default capacity 10 | Private config | `private_config_default_10` |
| `legal_state_context.anti_loop_state.loop_threshold` | AntiLoopConfig default repeat threshold 2 | Private config | `private_config_default_2` |
| `legal_state_context.anti_loop_state.source_decision_sequence` | No sequence in AntiLoopHistory/records | Not exported | `not_produced_no_decision_sequence` |
| `legal_state_context.anti_loop_state.reason` | get_block_reason returns transient string | Aggregate category metrics only | `ephemeral_block_reason_not_recorded` |
| `legal_state_context.anti_loop_state.position_history[].state_hash` | PositionSignature with computed native size_t hash | No serialized hash | `computed_size_t_signature_hash_not_sha256_field` |
| `legal_state_context.anti_loop_state.position_history[].round` | No round in PositionSignature; vector cleared per round | Not exported | `not_stored_per_position_record` |
| `legal_state_context.anti_loop_state.position_history[].decision_sequence` | No sequence in PositionSignature | Not exported | `not_produced_no_sequence` |
| `legal_state_context.anti_loop_state.move_history[].round` | MoveRecord has no round | Not exported | `not_stored_in_move_record` |
| `legal_state_context.anti_loop_state.move_history[].decision_sequence` | MoveRecord has no sequence | Not exported | `not_produced_no_sequence` |
| `legal_state_context.anti_loop_state.move_history[].move_type` | Internal MoveRecord field | No history export | `internal_move_record_type` |
| `legal_state_context.anti_loop_state.move_history[].source_slot` | Internal MoveRecord source | No history export | `internal_move_record_source` |
| `legal_state_context.anti_loop_state.move_history[].target_slot` | Internal MoveRecord target | No history export | `internal_move_record_target` |
| `legal_state_context.anti_loop_state.move_history[].result_state_hash` | No link from MoveRecord to later state registration | Not exported | `not_produced_no_move_state_link` |
| `legal_state_context.anti_loop_state.blocked_move_records[].round` | BlockedMoveRecord has no round | Not exported | `not_stored_in_blocked_record` |
| `legal_state_context.anti_loop_state.blocked_move_records[].decision_sequence` | BlockedMoveRecord has no sequence | Not exported | `not_produced_no_sequence` |
| `legal_state_context.anti_loop_state.blocked_move_records[].move_type` | Nested MoveRecord has move_type | Not exported | `internal_nested_move_type` |
| `legal_state_context.anti_loop_state.blocked_move_records[].source_slot` | Nested MoveRecord has source | Not exported | `internal_nested_move_source` |
| `legal_state_context.anti_loop_state.blocked_move_records[].target_slot` | Nested MoveRecord has target | Not exported | `internal_nested_move_target` |
| `legal_state_context.anti_loop_state.blocked_move_records[].reason` | Reason computed transiently by query | Not stored in BlockedMoveRecord | `ephemeral_reason_not_stored` |
| `legal_state_context.anti_loop_state.blocked_move_records[].state_hash` | Optional blocked PositionSignature | No serialized SHA-256 | `optional_blocked_signature_not_sha256_field` |
| `legal_state_context.anti_loop_state.state_visits[].state_hash` | StateVisit stores PositionSignature key | Native hash only, not SHA-256 | `signature_key_hash_not_sha256_field` |
| `legal_state_context.anti_loop_state.state_visits[].visit_count` | Internal StateVisit.visits | No per-state export | `internal_visit_counter` |
| `legal_state_context.anti_loop_state.state_visits[].last_seen_round` | Internal StateVisit.last_seen_round | No per-state export | `internal_visit_round` |
| `legal_state_context.anti_loop_state.state_visits[].last_seen_sequence` | StateVisit has no sequence field | Not exported | `not_produced_no_sequence` |
| `legal_state_context.mask_reference.status` | Native mask arrays returned without parent status | Arrays only | `native_masks_without_status_envelope` |
| `legal_state_context.mask_reference.action_contract_id` | Static action shape/type definitions | No runtime contract ID | `static_action_shape_no_runtime_contract_id` |
| `legal_state_context.mask_reference.action_contract_version` | No version in mask payload | No version transported | `no_runtime_action_contract_version` |
| `legal_state_context.mask_reference.action_contract_hash` | No action-contract hash producer | None | `not_produced_no_action_contract_hash` |
| `legal_state_context.mask_reference.mask_contract_id` | ActionMaskBatch/PlayerActionMasks arrays | Arrays only | `no_runtime_mask_contract_id` |
| `legal_state_context.mask_reference.mask_contract_version` | No mask version field | Arrays only | `no_runtime_mask_contract_version` |
| `legal_state_context.mask_reference.mask_contract_hash` | No mask-contract hash producer | None | `not_produced_no_mask_contract_hash` |
| `legal_state_context.mask_reference.mask_snapshot_hash` | No snapshot fingerprint in mask API | None | `not_produced_no_snapshot_hash` |
| `legal_state_context.mask_reference.decision_identity_hash` | No decision identity envelope in mask API | None | `not_produced_no_decision_identity_envelope` |
| `legal_state_context.mask_reference.reason` | Local validation/anti-loop reasons only | No parent mask reason | `no_parent_mask_reason` |
| `legal_state_context.critic_context.status` | No critic-context envelope | Value head uses observation | `not_produced_no_critic_context_envelope` |
| `legal_state_context.critic_context.representation` | Shared encode(obs) and value_head | Same flat observation encoder as Actor | `shared_actor_critic_encoded_observation` |
| `legal_state_context.critic_context.source_decision_sequence` | No sequence on value input/rollout record | Observation and masks stored separately | `not_produced_no_critic_sequence` |
| `legal_state_context.critic_context.reason` | No critic-context envelope | None | `not_produced_no_critic_context_reason` |

## 6. Non-equivalences and invariants

1. Internal AntiLoopEngine records are not exported history entities.
2. A native size_t hash is not a SHA-256 content identity.
3. A round counter is not a decision sequence.
4. A transient block reason is not a stored blocked-move reason.
5. Aggregate anti-loop metrics are not position/move/state-visit histories.
6. Native mask arrays are real legality inputs, but do not imply a versioned/hash-bound mask-reference envelope.
7. Action masks are stored separately from observations and remain final legality inputs.
8. The current value head consumes the shared encoded observation and ignores masks; no separate Critic context is currently delivered.

## 7. Remaining proof

- Decide whether anti-loop history belongs in Schema v2 at all, or whether the required contract should expose only bounded aggregate metrics; if event history remains, define identity/sequence/hash/lifecycle before implementation.
- Define SHA-256 state fingerprinting and exact serialization scope if schema requires hashes; do not reuse native size_t hashes.
- Define mask contract/version/hash and decision identity correlation only after the action/legality contract is finalized; keep masks independent and authoritative.
- Decide whether future Critic context is a distinct structured projection or the existing shared observation representation; do not select tensor layout here.
- Complete the remaining 43 exact source-map callsite validations and Actor/Critic leaf-level delivery proof.

Issue #346 remains open. This is documentation only; no runtime, schema, tensor, PPO, reward, mask, training, checkpoint or Viewer changes.

## 8. Architecture reconstruction review

1. **Prior problem:** schema paths implied sequence-bound anti-loop records, SHA-256 state hashes, mask contract references and a dedicated Critic context without proving those outputs exist.
2. **Technical justification:** internal records, native masks, diagnostic counters and shared value-network inputs have distinct lifecycles and semantics; promoting them to typed entities would fabricate hashes, sequences and ownership.
3. **New responsibility:** this audit owns field-level classification of AntiLoopEngine internals, the current mask transport and the current value-head representation.
4. **Contract and invariants:** no synthetic decision sequences or hashes; transient reasons remain transient; masks stay separate and authoritative; Critic representation remains current shared observation until a future explicit decision.
5. **Cross-component impacts:** DecisionHistory, AntiLoopEngine, ActionMaskEngine, TftEngine, pybind, Python wrapper, Trainer, policy encoder/value head, RolloutBuffer, schema and replay.
6. **Objective validation:** all 46 remaining ancestor-matched paths are enumerated and traced to native records, mask transport or value-head behavior; no runtime/schema/tensor change.

