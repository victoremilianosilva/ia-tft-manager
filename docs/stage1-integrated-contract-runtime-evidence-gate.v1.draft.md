# Stage 1 — Integrated Contract and Runtime Evidence Gate v1

**Status:** consolidated acceptance ledger; Stage 1 is not yet accepted.  
**Base:** `new-arquiteture` after PRs #450–#452.  
**Tracking:** #294, #293, #346, #288, #289 and #295.

## 1. Prior problem

Stage 1 work was delivered in four distinct evidence layers: action/mask runtime contract, Observation Schema v2 validation, structured-entity producer audit and the earlier snapshot/vector/rollout correlation changes. Without one integrated ledger, a merged PR could be mistaken for acceptance of its parent issue or for proof of the complete native→PPO→replay path.

The repository also contains several replay-adjacent artifacts that are not equivalent: a cross-language fixture, Viewer log playback, terminal vector→rollout tests and a deterministic multi-round Engine/PPO replay.

## 2. Technical rationale

A stage can only be accepted when each contract is proven at its actual boundary. A schema validator does not prove a producer; a valid mask hash does not establish a canonical per-player decision identity; a stored action trace does not prove strategic recommendation separation; and a terminal integration test using controlled test doubles does not prove a real multi-round native replay.

This ledger separates merged implementation evidence, integration-test evidence, documented capability and outstanding acceptance.

## 3. New responsibility and ownership

This document is the Stage 1 integrated acceptance ledger:
- #294 owns PPO Action/Mask runtime contract and legality boundary.
- #293 owns semantic Observation Schema v2 and its executable validation.
- #346 owns source-backed structured entity production, identity, lifecycle and delivery.
- #288 owns full checkpoint semantic lineage beyond the Action/Mask component delivered in #450.
- #289 owns deterministic multi-round integrated replay.
- #295 owns evaluation protocol and promotion evidence.

The ledger does not replace these issue owners and does not authorize new tensor layouts, training, real GEP claims or autonomous execution.

## 4. Merged evidence

| Delivery | Merged scope | What it proves | What it does not prove |
|---|---|---|---|
| PRs #425–#449 | Native snapshot/mask correlation, Engine identity, vector/rollout metadata, action traces, fail-closed behavior and test isolation | Transition metadata and masks are preserved and validated through the tested wrapper/vector/rollout boundaries | Canonical logical match ID, authoritative per-player decision sequence, complete GEP source identity or full multi-round replay |
| #450 | Action Contract v1 and Mask Contract v1, independent hashes, strict action encoding, exact mask digest recomputation, checkpoint component identity | Action/Mask compatibility and persisted mask payload integrity are explicit and independently versioned | Full #288 checkpoint manifest, Critic mask conditioning, every strategic recommendation separation scenario or new training lineage |
| #451 | Observation Schema v2 Draft 2020-12 validator, identity/provenance/cardinality rules, fixtures and corrected sequence registry | Schema declarations and identity boundary have executable validation; Engine snapshot ordinal is not misrepresented as player decision sequence | Runtime structured producer serialization, full semantic source coverage, tensor projection or per-player decision identity |
| #452 | 17-kind producer audit reconciliation, 31 field-family rows, 223-path crosswalk and delivery dispositions | Source/identity/Python/PPO gaps are explicitly inventoried without synthetic fields | Missing native producers, physical item IDs, stable shop offer IDs, complete structured delivery or closure of #346 |

## 5. Integrated boundary evidence

### 5.1 Native snapshot and action-mask boundary

- Wrapper captures masks from the exact native ResetResult/StepResult rather than re-reading a later Engine state.
- Engine instance identity and episode/snapshot metadata survive wrapper, vector environment and RolloutBuffer.
- Mask payload digest is recomputed from the stored boolean tensors by #450.
- Active players with missing/empty required masks fail closed; synthetic PASS is restricted to explicitly eliminated players.
- Vector partial-step/reset failures poison the vector until a complete successful reset.

### 5.2 Action transition boundary

- PPO action is kept distinct from native requested/effective action trace.
- Native trace includes player identity, requested/effective action, handler status and status reason.
- Rollout rejects malformed trace association and metadata identity types.
- Engine remains the final legality authority; the strategic system does not replace PPO action selection or native legality.

### 5.3 Observation and entity boundary

- Observation Schema v2 is machine-validated.
- Native Engine snapshot sequence is one Engine-instance-scoped publication ordinal shared by all eight player rows.
- A per-player decision sequence and authoritative logical match identity remain unavailable in the audited main-repository path.
- Raw UnitInstance UUID is not accepted as globally/cross-episode-safe physical identity.
- Diagnostic entity snapshots and derived slot features are not equivalent to typed Python or PPO entity delivery.

### 5.4 Existing replay boundary

The current terminal vector→rollout integration test (#444/#445) validates decision/result/next snapshots, mask hash, eight player identities and native action traces using production Trainer adapter methods. This is valuable transition-correlation evidence.

It is not the Gate 7 deterministic multi-round replay. The existing cross-language fixture covers round barriers and BUY_XP state/reward/observation parity with stated limitations; Viewer replay is event-log playback and does not re-run Engine or PPO.

## 6. Acceptance matrix and remaining blockers

| Acceptance area | Current status | Required evidence before acceptance |
|---|---|---|
| Atomic native observation+mask capture | Implemented and tested in focused/integrated terminal cases | Full stale-state and mask/state mismatch matrix across all native action paths |
| Action/Mask contract identity | Implemented in #450 | End-to-end compatibility and rejection tests for every supported checkpoint/load path |
| All nine action encodings and 12 masks | Contract and focused tests implemented | Complete positive/negative matrix for conditional parameters, stale state, mask emptiness and schema/action incompatibility |
| Observation Schema v2 | Validator and fixtures merged | Full semantic-field/source/consumer acceptance; runtime projection remains later-stage work |
| Structured entity producer evidence | Audit consolidated in #452 | Resolve or keep unavailable all 17 entity-family gaps; prove ownership/lifecycle/completeness/provenance and delivery |
| Per-player decision identity | Not available as authoritative native source | Producer-owned typed decision sequence and authoritative logical match scope; do not substitute Engine snapshot ordinal |
| Strategic recommendation separation | Architectural invariant documented | Integrated tests/replay proving baseline and strategic proposals cannot dispatch or bypass Engine legality |
| Checkpoint lineage | Action/Mask component delivered | Full #288 schema/projection/reward/encoder/catalog lineage and incompatibility policy |
| Multi-round integrated replay | Not yet accepted | Deterministic native Engine→wrapper→vector→Trainer/PPO→rollout/replay fixture with reset, stale/missing identity, mask and strategic evidence cases |
| PPO evaluation/promotion | Not yet accepted | #295 paired-seed/seat-rotation/train-validation-test evidence and immutable checkpoint lineage |

### Explicit non-acceptance conditions

Stage 1 must not be marked accepted while:
1. per-player decision identity is fabricated from the Engine-wide snapshot ordinal, round, slot or call order;
2. structured entities are inferred from schema declarations or diagnostic sidecars without producer proof;
3. strategic recommendations, baselines or executor resolutions are confused with PPO-selected/executed actions;
4. stale, missing, empty or mismatched masks can be silently replaced with a later snapshot;
5. the terminal correlation test is described as full multi-round replay;
6. CI is reported green without a completed successful workflow run.

## 7. Contract and invariants

- Action Contract, Mask Contract, Observation Schema, tensor projection and checkpoint lineage remain separate versioned components.
- Exact masks are side inputs bound to the decision snapshot; Engine is final legality authority.
- Engine snapshot sequence, future per-player decision sequence, strategic owner sequences, replay sequences and Viewer sequences remain typed, separate namespaces.
- No synthetic match IDs, unit/item/shop/candidate IDs, decision sequences, producer outputs or replay events.
- Missing, empty, unknown, partial, stale, incompatible and not-applicable remain distinct.
- PPO remains the learning/policy algorithm; strategic intelligence is context/proposal, not imitation target or direct command.
- No autonomous gameplay execution is introduced.

## 8. Cross-component impacts

This ledger covers TFTEngine/Impl, native ResetResult/StepResult, pybind, `cpp_lobby_env.py`, vector environment, Trainer, Policy, RolloutBuffer, Action/Mask contracts, Observation Schema v2, structured entity producers, checkpoint manifests, replay and evaluation. It changes no runtime component.

## 9. Objective validation criteria

- Merged PR references and commit identities are checked against GitHub.
- Existing tests and fixtures are mapped to the exact boundary they exercise.
- Known gaps are cross-checked against #293, #294, #346, #288, #289 and #295.
- The 17-kind/31-family/223-path scopes remain separate and are not added together.
- No workflow is marked successful unless its completed job conclusion is `success`.
- Stage 1 remains open until each acceptance row has source-backed implementation and reproducible integrated evidence.

## 10. Architecture reconstruction review

1. **Prior problem:** separate PRs and replay-like artifacts could be mistaken for complete Stage 1 acceptance.
2. **Technical rationale:** contract validity, producer delivery, decision identity, transition correlation and multi-round replay are distinct proof obligations.
3. **New responsibility:** this document owns the integrated acceptance ledger and maps evidence to the issue that owns it.
4. **Contract/invariants:** preserve typed identity namespaces, exact mask correlation, Engine legality, strategic/PPO separation and explicit unavailable states.
5. **Cross-component impacts:** native Engine, Python wrapper/vector/Trainer/Policy/RolloutBuffer, schema, entities, checkpoints, replay and evaluation.
6. **Objective validation:** every merged delivery is tied to bounded claims; each residual blocker has an owner and explicit proof requirement; no runtime change or stage acceptance is implied.
