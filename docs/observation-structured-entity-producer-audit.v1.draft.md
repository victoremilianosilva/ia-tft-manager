# Structured Entity Producer Evidence Audit — Identity Slice v1 (Draft)

**Status:** partial source audit; not runtime-approved. Full coverage tracked by [#346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).

## Scope of this slice

This document records only source facts verified in the current new-arquiteture branch. It does not claim that all 17 entity kinds have been audited.

## Physical unit identity

### Native declaration

cpp/include/lobby/TftEngine.hpp declares UnitInstance with:

- champion_internal_id: internal catalog reference;
- champion_id: champion API/catalog identity;
- uuid: intended identity of an individual copy;
- star: mutable star state;
- items: equipment attached to that copy.

The header's own comment on uuid says effective UUID generation will be implemented later. is_valid() requires a non-empty UUID, but that predicate does not prove a generation path exists or that every live unit satisfies it.

### Current consumers

cpp/src/lobby/TftEngine.cpp reads unit.uuid for item profiles, item-engine equipped lookups, movement/purchase history correlation, item action targets and diagnostic snapshots. Several consumers explicitly skip or condition behavior when UUID is empty. These are consumers of a field, not proof of its producer lifecycle.

### Status

**UNVERIFIED**

No source-backed proof has yet established:

1. where a new unit UUID is generated;
2. whether it is guaranteed non-empty and unique;
3. whether it survives board/bench movement and copy operations;
4. whether merging/upgrading/selling invalidates or replaces identity correctly;
5. whether UUID scope is unique across players, matches and Engine resets;
6. whether the same UUID is exposed through a structured snapshot and Python binding.

### Schema reconciliation

Schema v2 currently requires unit.instance_id; the entity manifest previously called it canonical. Neither source inspected here proves a native instance_id member. The native candidate name is uuid, but it is not yet proven authoritative. Do not silently alias these fields.

## Current PPO delivery boundary

TFTEngine::Impl::build_observations() produces a flat numeric vector. It includes fixed board/bench/shop slot features and derived aggregates, but the function does not itself serialize a lossless structured unit record carrying UUID, provenance and source sequence. The current PPO tensor therefore cannot be treated as proof that the structured unit entity is already delivered to Python.

The Shadow/diagnostic path and item engine may consume UUIDs, but this is distinct from the trainer's actual observation tensor and rollout data.

## Confirmed source references

| Source | Confirmed fact | What it does not prove |
|---|---|---|
| cpp/include/lobby/TftEngine.hpp — UnitInstance | Declares uuid; comment says effective generation is future work | UUID production, uniqueness, stability, scope |
| cpp/src/lobby/TftEngine.cpp — Impl::build_observations() | Emits flat per-player float observation vector | Structured entity identity delivery |
| cpp/src/lobby/TftEngine.cpp — item binding and item action paths | Reads UUID for unit-specific item association | Valid UUID lifecycle |
| cpp/src/lobby/TftEngine.cpp — strategic evidence construction | Increments per-player strategic_context_sequences[i] for evidence_input.sequence | Correlation of that sequence with PPO observation and action masks |

## Required follow-up

Continue #346 by tracing UUID creation and lifecycle, then audit board/bench slots, shop offers, items/components/anvil, traits, positioning, strategic evidence, action candidates, temporal histories and Engine-to-Python exposure. Until proven, each unsupported entity field remains unavailable or unverified.

## Architecture reconstruction review

1. **Prior problem:** the structured entity contract assumed instance_id without proving a native producer.
2. **Technical rationale:** projection identity must reflect actual lifecycle and ownership, or joins/replay can silently associate the wrong physical copy.
3. **New responsibility:** this slice records source-backed producer evidence and blocks unsupported identity claims.
4. **Contracts/invariants:** no inferred UUID generation; no champion/slot substitute; schema fields are not runtime evidence; diagnostic availability is not PPO delivery.
5. **Cross-component impact:** UnitInstance, PlayerEnv, ItemEngine, board/bench transfer, shop, pybind, Python wrapper, PPO rollout, replay and checkpoint lineage.
6. **Objective validation:** UUID generation, uniqueness, movement stability, reset behavior and Python exposure must be demonstrated by code and tests before the field is accepted.
