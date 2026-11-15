# PvE Loot and Anvil Gameplay Producer Boundary Audit v1 — Draft

**Status:** source-backed producer-boundary clarification; documentation only, not runtime-approved.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Prior ambiguity

The earlier item/anvil audit correctly found no call to `grant_component_anvil()` or `grant_completed_item_anvil()` in the audited `TftEngine.cpp` gameplay path, but its wording could be read as saying that the game has no PvE item producer. That is too broad: the Engine has a real PvE loot-resolution path. The relevant distinction is whether that path creates a queued choice (an anvil) or directly grants inventory contents.

## 2. Actual PvE reward producer

`TFTEngine::Impl::grant_round_pve_item_rewards()` is implemented in `cpp/src/lobby/TftEngine.cpp:919-1024` and is invoked when a round is resolved at `TftEngine.cpp:6406`.

The producer:
- Determines stage and round-in-stage, then selects component-reward rounds for stages 1–4 and completed-item reward rounds from stage 5 onward (`TftEngine.cpp:925-940`).
- Restricts recipients to living players with an ItemEngine (`TftEngine.cpp:942-948`).
- Derives deterministic reward RNG state from Engine seed, episode ID, round number and a fixed domain constant (`TftEngine.cpp:950-952`).
- For component rewards, rolls the stage table, draws component catalog IDs from each player's PvE component pool and calls `ItemEngine::add_component()` (`TftEngine.cpp:954-995`).
- For completed-item rewards, builds a pool of unit-equipable catalog items, selects one per living player and calls `ItemEngine::add_completed_item()` (`TftEngine.cpp:1000-1023`).
- Refreshes masks after each player's reward grant.

The round-resolution call occurs after PvP resolution (or the no-PvP branch) and before the next preparation-phase economy progression (`TftEngine.cpp:6386-6415`). The reward is therefore a real Engine gameplay transition, not merely an ItemEngine unit test.

## 3. Why this is not an anvil producer

The ItemEngine has a separate queue-based choice API:
- `grant_component_anvil(options)` and `grant_completed_item_anvil(options)` enqueue validated option vectors (`cpp/include/items/ItemEngine.hpp:141-147`).
- `pending_anvil()` exposes the queue head; `choose_anvil_option(index)` validates the positional choice, grants exactly the selected catalog ID, and consumes the queue head only after a successful grant (`ItemEngine.hpp:149-175`).
- While an anvil is pending, the Engine masks every other action and enables the item-choice action with option positions as the selection mask (`TftEngine.cpp:1115-1130`).
- The observation builder projects pending/kind flags and up to nine positional option slots (`TftEngine.cpp:1546-1609`); the audit snapshot separately serializes pending state, kind and ordered option IDs (`TftEngine.cpp:6750-6760`).

The PvE reward path above calls only `add_component()` and `add_completed_item()`. It does not enqueue an anvil and does not create option sets. A direct one-item grant is not semantically equivalent to a multi-option decision.

## 4. Implementation and binding callsite audit

A scan of all 12 implementation translation units under `cpp/src/**/*.cpp` on the audited branch found:
- one production callsite for `grant_round_pve_item_rewards()`;
- direct gameplay grants through `add_component()` and `add_completed_item()` in that PvE producer;
- no call to `grant_component_anvil()` or `grant_completed_item_anvil()` in those implementation translation units.

The ItemEngine grant-anvil methods are implemented inline in `ItemEngine.hpp`; their observed callsites are the ItemEngine tests, not the audited lobby gameplay implementation. The public TFTEngine APIs `grant_item_component()` and `grant_completed_item()` are direct inventory-grant methods (`TftEngine.cpp:6889-6907`) and are bound in pybind (`tft_engine_bindings.cpp:911-917`). They do not enqueue an anvil. Their existence or external invocability is not evidence of a gameplay anvil producer.

The current audit therefore supports the following precise classification:
- PvE component loot: **native observed direct inventory grant**.
- PvE completed-item loot: **native observed direct inventory grant**.
- Pending anvil queue: **native API/state and conditional consumer/projection exist**.
- In-game anvil grant event: **not produced by the audited C++ gameplay implementation**.
- Anvil option identity: **catalog ID plus queue position only; no stable anvil ID, option ID, revision or source decision sequence**.

## 5. Identity, provenance and delivery implications

- Component and completed-item loot IDs are catalog identifiers, not physical item-instance identifiers.
- The PvE component pool is a per-player reward-distribution pool; it is not the shared champion pool and does not establish physical component identity.
- The reward RNG is deterministic from seed/episode/round, but the current reward event does not expose a typed loot-event ID or a source decision sequence.
- The audit event strings (`PVE_COMPONENT_REWARD_ROLLED`, `COMPONENT_LOOT_GRANTED`, `COMPLETED_ITEM_GRANTED`) are emitted in round events; this is event/diagnostic output, not proof that a typed structured item entity with provenance is delivered to PPO.
- The pending-anvil diagnostic snapshot and flat observation projection are conditional on the queue being populated. Their existence does not prove that normal gameplay currently populates it.
- The normal Python `reset/step` boundary returns the native observation vector; the audit snapshot is a separate method. No typed anvil entity delivery to Actor/Critic is established here.

## 6. Field-level dispositions

| Schema family | Actual producer | Current disposition |
|---|---|---|
| Component inventory additions | PvE round resolver → `ItemEngine::add_component` | `native_observed_direct_grant`; catalog ID/count only |
| Completed-item inventory additions | PvE round resolver → `ItemEngine::add_completed_item` | `native_observed_direct_grant`; catalog ID/count only |
| Pending anvil | ItemEngine queue API | `conditional_native_state_no_gameplay_enqueue_callsite` |
| Anvil option records | Ordered catalog IDs in queue | `positional_catalog_options_no_stable_option_identity` |
| Anvil decision | Item-choice action and native masks | `conditional_consumer_no_audited_gameplay_producer` |
| Typed item/loot entity in PPO | No structured entity bridge established | `not_delivered_as_typed_entity` |

## 7. Required future proof (not authorized implementation)

Before changing the schema or claiming operational anvil availability:
1. Identify an authoritative gameplay event that should create a choice rather than a direct grant.
2. Define anvil identity, option identity/revision, owner, completeness and source decision sequence.
3. Trace the exact grant event through native state, snapshot, pybind, Python wrapper, rollout, Actor and Critic.
4. Add acceptance scenarios for direct PvE grant versus queued anvil choice, invalid option, successful single consumption, reset with pending choice and consecutive episodes.
5. Keep direct loot grants and player choices as distinct event types; do not convert a direct grant into a fabricated anvil.

No runtime implementation, schema mutation, tensor-layout decision, PPO/reward/mask/training/checkpoint/Viewer/Overwolf change is authorized by this audit. Issue #346 remains open; Gate 8 remains blocked.

## 8. Architecture reconstruction review

1. **Prior problem:** the previous anvil proof could be misread as absence of all PvE item production, despite a direct-grant gameplay path.
2. **Technical justification:** direct loot delivery and a queued multi-option choice have different action, identity, provenance and legality semantics.
3. **New responsibility:** this audit owns the boundary between PvE loot producers and the separate ItemEngine anvil queue/choice consumer.
4. **Contract and invariants:** direct grants are not anvils; catalog IDs are not physical item IDs; positional options are not stable identities; diagnostic/flat features are not typed PPO entities; native masks remain final legality authority.
5. **Cross-component impacts:** PvE loot distribution, TFTEngine round resolution, ItemEngine inventory/anvil queue, native masks, observation projection, audit snapshot, pybind, Python wrapper, PPO and Schema v2.
6. **Objective validation:** all 12 `cpp/src` implementation translation units were scanned for the anvil grant APIs; the actual PvE producer and its invocation are source-located; direct-grant and anvil callsites are explicitly separated. Documentation only.

Issue #346 remains open. This document does not approve Gate 8 or any runtime implementation.
