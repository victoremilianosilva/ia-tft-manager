# Action Execution and Reward-Credit Regression Coverage Audit v1 — Draft

**Status:** source-backed test-coverage inventory; documentation only.
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).
**Base:** `new-arquiteture`.

## 1. Purpose and boundary

PR #382 traced native action execution and reward-credit flow. This document checks which parts of that contract already have executable regression coverage and which remain unproven. It is a test inventory, not a request to implement runtime changes now.

Primary audited fixture: `cpp/tests/test_tft_engine_pool.cpp`. Related item behavior: `cpp/tests/test_item_engine.cpp`. The source references below describe the current branch content inspected for this audit.

## 2. Existing executable coverage

| Contract / scenario | Existing evidence | Coverage assessment |
|---|---|---|
| Invalid sell from empty bench slot | `test_tft_engine_pool.cpp` around lines 270–300: expects `std::invalid_argument`; checks round, pool and gold unchanged | Covered for this invalid action and these state fields |
| Buy without sufficient gold | Around lines 300–320: expects rejection; checks round, pool and gold unchanged | Covered for this invalid action and these state fields |
| Whole-lobby preflight atomicity | Around lines 325–365: player 0 submits invalid sell while player 1 submits valid buy; expects exception and verifies no round, pool or player-1 gold mutation | Strong explicit batch-atomicity regression |
| Invalid move from empty source | Around lines 400–430: expects rejection; checks round, gold, pool and anti-loop attempts unchanged | Covered for invalid source path |
| Successful buy action reward | Around lines 375–390: verifies nonnegative gold, `rewards == action_rewards` when no combat is resolved, and a bounded action reward | Covered for isolated action-reward parity in this fixture |
| Buy→sell reversal shaping | Around lines 740–790: buys a unit, identifies the new physical UUID in audit snapshot, sells it and expects negative sell reward | Covered for immediate reversal penalty; does not assert total sequence return |
| Pair-protecting sale shaping | Around lines 790–820: compares isolated-unit sale with sale of one copy from a pair | Covered for relative penalty |
| Craft/equip mutation and diagnostic identity | Around lines 830–875: validates item reaches target and audit snapshot includes item kind, catalog ID, components, target UUID/slot and fit | Covered for item action diagnostic fields in the direct native fixture |
| Item reaches combat team | Around lines 875–930: obtains CombatTeam through normal conversion path and checks equipped item stats | Covered for item-to-combat propagation |

## 3. Existing coverage does not prove

- A typed `submitted_action` vs `effective_action` vs `execution_resolution` record exists; no such field is asserted in these tests or exported in `StepResult`.
- The `PlayerTransition::acted` status is exported and correlated to the PPO sample; current tests exercise state effects, not a public typed acted/rejected result.
- The exact action mask used to sample a policy action is retained with a native decision identity. The native test obtains masks and submits an action, but the result does not carry a shared decision ID.
- A preflight exception is converted into a recoverable per-player training transition. Current native contract throws for invalid batch; wrapper/trainer propagation/recovery behavior needs separate proof.
- Finished-player submitted-action replacement with PASS is visible in the result as an explicit substitution outcome.
- Dead-player skip, valid PASS, anti-loop block and board-capacity violation each have distinct typed execution outcomes and replay correlation.
- Combat and placement reward components are stored separately in RolloutBuffer; tests of native result arrays do not prove PPO rollout persistence.
- Action/combat/placement reward components are bound to the exact same typed decision/episode/player identity as the combined reward.
- Native `action_serial` is exposed as a cross-layer decision ID; it remains player-local bookkeeping.

## 4. Important precision about current evidence

The atomic-batch test is meaningful: it verifies that an invalid action from one player prevents another player's valid buy from being applied. This corroborates the side-effect-free preflight contract in `TFTEngine::step` and argues against describing the current behavior as partial batch execution.

The successful-buy reward assertion is deliberately scoped to a step with no combat resolution. It verifies action-only parity in that fixture, not general equivalence of `rewards` and `action_rewards`. Once combat or placement contributes, the combined reward is expected to differ.

The item audit snapshot assertions prove useful native diagnostic detail for item operations, but they do not establish a general typed action ledger for all action types.

## 5. Future acceptance test matrix

1. **Action identity:** submit a known action and assert a typed resolution links the submitted arguments, effective arguments, pre-action observation/masks and post-action result.
2. **PASS substitution:** mark one player round-finished, submit a non-PASS action, and assert the native resolution records the effective PASS and why it was substituted.
3. **Dead player:** submit the lobby batch with one eliminated player and assert a distinct inactive/skipped outcome, not a false successful execution.
4. **Anti-loop block:** submit a structurally valid movement blocked by AntiLoop; assert a typed blocked outcome, no board mutation and the corresponding metrics.
5. **Capacity violation:** submit a deployment attempt that is intentionally admitted for penalty; assert the exact outcome, no unintended board mutation and reward component.
6. **Atomic invalid batch:** retain the existing player-0-invalid/player-1-valid test and extend assertions to every authoritative mutable domain touched by candidate actions (gold, pool, board, bench, shop and round progression).
7. **Reward decomposition:** cover action-only, action+combat, and terminal placement cases; assert combined reward equals the documented component sum and preserve the components in replay/audit records.
8. **Rollout persistence:** assert the sampled action, masks, combined reward, component rewards and typed execution resolution share one stable transition identity in the replay record.
9. **Wrapper error path:** assert native preflight exceptions are surfaced deterministically and do not leave Python vector-env bookkeeping or agent ordering partially advanced.
10. **Item action:** preserve existing item UUID/target diagnostics while binding them to the same decision identity as the sampled type-7/type-8 action.

## 6. Architecture reconstruction review

1. **Prior problem:** source tracing identified the action/result/reward boundaries, but existing executable tests had not been inventoried against each claimed invariant.
2. **Technical justification:** gate acceptance must distinguish proven runtime behavior from merely specified future behavior; existing atomicity and reward tests should be reused rather than rediscovered.
3. **New responsibility:** this audit owns the mapping from action-execution/reward contract claims to current regression tests and uncovered acceptance scenarios.
4. **Contract and invariants:** current whole-batch preflight atomicity is tested; action-only reward parity is tested only without combat; diagnostic item fields are not a universal typed execution record.
5. **Cross-component impacts:** native Engine tests, wrapper/vector-env error handling, Trainer, RolloutBuffer, reward decomposition, replay and future decision envelope.
6. **Objective validation:** every existing coverage claim is tied to concrete test sections; unproven claims have explicit acceptance cases. Documentation only.

No runtime, test, schema, tensor-layout, PPO architecture, reward, mask, training, checkpoint, Viewer or Overwolf implementation is authorized by this audit. Issue #346 remains open; Gate 8 remains blocked.

## 7. Unit elimination and equipment lifecycle test coverage follow-up — 2026-11-15

The focused inspection of `cpp/tests/test_item_engine.cpp` and `cpp/tests/test_tft_engine_pool.cpp` establishes:

- ItemEngine tests directly verify `return_equipped_to_inventory()` for a sold/removed UUID and verify `transfer_equipped_on_merge()` for merge sources.
- The pool/Engine test verifies sale validation and pool accounting, and checks diagnostic item fields/combat propagation.
- Neither inspected test file exercises the Engine elimination path `eliminate_players() → return_eliminated_player_units()` with equipped board/bench units.
- Neither asserts that the eliminated player's UUID-keyed equipment entries are cleared/retired or returned to that player's own bag.
- The sale test's comment uses “selling/removing”; it is a direct ItemEngine method test and must not be counted as proof of the Engine elimination lifecycle.

This is a scoped negative finding for these two relevant test files, not a claim that no test anywhere in the repository touches elimination. A repository-wide test-name/behavior audit would be required for that stronger claim.

### Required regression cases

1. Eliminate a player with one equipped board unit and one equipped bench unit while other players remain active.
2. Assert champion copies return exactly once and all active board/bench units are removed.
3. Assert the selected item terminal policy is applied exactly once to every eliminated UUID.
4. Assert no item becomes available to another player's inventory.
5. Assert removed UUIDs are no longer valid item targets.
6. Assert repeated elimination handling and subsequent Engine reset do not duplicate or resurrect items.
7. Assert a diagnostic snapshot clearly separates active equipment from terminal/orphaned records.

These are future acceptance criteria; no tests or runtime code were changed.
