# Native State Snapshot Contract v3 — Draft

**Status:** Stage 1 consolidation contract; runtime implementation in PR #484, pending review and CI.  
**Supersedes:** v2 for the nested combat, economy, PvP-credit and shared-pool envelope shape.  
**Tracking:** #346, #293 and #294.

## 1. Prior problem

Snapshot v2 carried a single parent identity envelope, but several nested records copied its identity and sequence fields:
- Combat events repeated the parent `round` and `combat_sequence`.
- Economy and PvP-credit events repeated Engine instance, episode, snapshot sequence and player decision sequence; PvP events also repeated round and combat sequence.
- The nested shared-pool snapshot repeated the parent source namespace and all Engine/episode/snapshot/player sequence fields.

Those copies created multiple representations of the same decision context. A future producer could update the parent and forget one child copy, leaving contradictory identities inside an otherwise atomic snapshot.

## 2. Technical rationale

These records are transported only as children of one `AuditSnapshot` in ResetResult/StepResult. They are not independent top-level streams. Their correlation identity therefore belongs to the parent envelope exactly once.

Event-specific provenance is not redundant:
- Event `contract_id` and `contract_version` identify the event payload contract.
- Event `source_namespace` and `producer` identify the actual source of the event.
- Player IDs select the corresponding entry in the parent `player_decision_sequences` array.
- Combat event rows inherit the parent `round` but retain `combat_sequence`, because one snapshot may contain multiple PvP matchups with different combat sequence values.
- Economy `resolved_after_round` and `income_for_round` remain separate because they describe two different temporal boundaries.

The independent AntiLoop JSONL API is intentionally not consolidated into this parent envelope: each row is exported independently and must retain its own decision identity.

## 3. New responsibility and owners

- `AuditSnapshot` owns Engine instance, episode, snapshot sequence, all eight player decision sequences, round and combat sequence.
- `AuditCombatDamageEvent`, `AuditCombatAttackEvent` and `AuditCombatDeathEvent` own only event-specific combat facts; their parent supplies round and combat sequence.
- `AuditEconomyResolutionEvent` owns economy-resolution provenance and result fields. Its player identity is `player_id`; its sequence is resolved through the parent array.
- `AuditPvpResultCreditEvent` owns PvP-credit provenance and balance/streak transition fields. Winner and loser identities select the parent player sequences.
- `AuditSharedPoolSnapshot` owns its independent pool contract, producer and pool data. Its correlation identity and source namespace are inherited from the parent snapshot.
- Pybind serializes this single-envelope structure without recreating child identity copies.
- The Python wrapper validates the parent envelope and rejects reintroduced duplicate pool-envelope fields.

## 4. Contract and invariants

### Parent snapshot envelope

The v3 parent envelope remains:
- `contract_id=tft.native-state-snapshot`, `contract_version=3`;
- `source_namespace=tft.engine.observation-snapshot`;
- `producer=TFTEngine::get_audit_snapshot`;
- `engine_instance_id`, `episode_id`, `snapshot_sequence`;
- `player_decision_sequences[8]`;
- `round`, `stage`, `finished`, and `combat_sequence`.

### Nested combat events

- Combat damage/attack/death rows no longer contain `round`; each retains its own `combat_sequence` so events from multiple matchups in one round remain distinguishable.
- All rows in these arrays belong to the combat identified by the parent snapshot's round/combat sequence.
- Timestamp, unit/player ownership mapping, damage/attack/death facts remain event-specific.
- Truncation flags remain on the parent collection.

### Nested economy and PvP-credit events

- Economy event contract version is 2; PvP-credit event contract version is 2.
- Both retain their event contract ID, source namespace and producer.
- Neither event repeats `engine_instance_id`, `episode_id`, `snapshot_sequence` or `player_decision_sequence`.
- Economy `player_id` maps to `player_decision_sequences[player_id]`.
- PvP `winner_player_id` and `loser_player_id` map to their respective parent sequence entries.
- PvP rows inherit `round` but retain their event-specific `combat_sequence`.
- Economy `resolved_after_round` and `income_for_round` remain event-specific and are not aliases for the parent round.

### Shared pool snapshot

- Shared-pool contract version is 2.
- It retains `contract_id`, `producer=UnitPool::available`, total availability and catalog-ordered champion counts.
- It no longer repeats `source_namespace`, Engine/episode/snapshot identity or player decision sequences.
- The enclosing AuditSnapshot is the sole correlation authority.

### Explicitly separate AntiLoop history

- The #475 temporal JSONL diagnostic stream remains a separate API with per-event Engine/episode/player/decision-sequence identity.
- It is not nested in AuditSnapshot and is not an Actor/Critic input.
- Operational AntiLoop state remains responsible for movement-cycle queries and native legality checks; action masks remain the independent legality contract.

## 5. Cross-component impact

Changes the native snapshot DTO, event producers, pybind serialization, Python wrapper validation, snapshot-binding fixtures/tests and the Stage 1 producer-audit documentation. The parent envelope becomes the only identity authority for nested snapshot records.

No changes to observation tensor dimensions, PPO policy, Actor/Critic projection, reward, action masks, native legality, checkpoints, Viewer behavior, GEP or Overwolf integration.

## 6. Objective validation

- Native C++ targets compile after removal of obsolete child field assignments.
- Pybind builds with the v3 DTO; combat sequence remains event-specific while duplicate parent identity and round fields are absent.
- Python wrapper accepts v3 and shared-pool v2 payloads with parent-only correlation.
- Python wrapper rejects a shared-pool record that reintroduces parent envelope fields.
- Existing snapshot identity, sequence, pool total and unit-cardinality tests continue to pass.
- CI runs native engine integration and PPO contract tests.
- AntiLoop JSONL identity tests remain unchanged and prove that the independent stream retains its own event identity.

## 7. Migration and compatibility

This is an explicit snapshot schema revision. Consumers must require v3 and must not infer v3 semantics from a v2 payload. No attempt is made to accept both child-envelope shapes in the same runtime DTO. Historical v2 snapshots remain historical artifacts; they are not rewritten.

## 8. Architecture reconstruction review

1. **Prior problem:** nested records repeated parent identity/sequence fields, allowing redundant values to drift and multiplying transport/validation obligations.
2. **Technical rationale:** these rows are children of one atomic snapshot, so parent identity is authoritative; only event-specific producer provenance and temporal facts belong on child rows.
3. **New responsibility:** the parent AuditSnapshot owns correlation; each child owns only its event or pool semantics.
4. **Contract/invariants:** v3 is explicit; child event IDs/producers remain; player sequences are resolved by player ID; combat round/sequence inherit from the parent; economy round boundaries remain distinct; AntiLoop JSONL remains independently enveloped.
5. **Cross-component impacts:** C++ DTO/producers, pybind, Python wrapper, fixtures, producer-audit docs and downstream snapshot consumers; no tensor, reward, masks or PPO behavior changes.
6. **Objective validation:** compile native code, validate pybind shape, accept/reject wrapper fixtures, preserve parent identity checks and run CI before considering this consolidation complete.

