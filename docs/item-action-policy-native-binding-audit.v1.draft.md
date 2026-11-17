# Item Action Policy-to-Native Binding Audit v1 — Draft

**Status:** source-backed action-binding audit; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Prior ambiguity

The item system has a six-component native action vector, separate item masks, and policy-side autoregressive heads. The same native action type 7 is used for both ordinary inventory equip and a mandatory anvil choice. Without an explicit binding map, positional action fields and mask names can be mistaken for their legacy labels or for one universal item operation.

This audit records the current semantic binding without changing the action vector, tensor dimensions, masks or runtime.

## 2. Shared action envelope

The native action remains six components with dimensions `[9, 5, 9, 28, 28, 28]` (`cpp/include/lobby/TftEngine.hpp`). The header's positional comments describe the general action envelope as type, shop slot, bench slot, board target, board source and board-move target. Item actions reuse these positions with type-specific meanings; they do not create a new action head or change the six-wide contract.

Native item masks are separate from the six action components:
- `item_inventory_mask[9]`
- `item_component_first_mask[10]`
- `item_component_pair_masks[10][10]`
- `item_target_mask[37]`

They are generated from the current per-player ItemEngine and board/bench state (`cpp/src/lobby/TftEngine.cpp:1060-1100`). The mask arrays are legality constraints, not fields packed into the action vector or substitutes for observation semantics.

## 3. Policy sampling and native decoding map

| Decision | Native type | Action positions | Policy mask/head | Native interpretation |
|---|---:|---|---|---|
| Equip inventory item | 7 | `a[1]=inventory slot`, `a[2]=board/bench target` | `item_inventory_mask`, then `item_target_mask` | Select inventory catalog ID at slot, then exact target UnitInstance |
| Choose component anvil option | 7 | `a[1]=anvil option index`, `a[2]=0 sentinel` | `item_inventory_mask` reused for offered options; `item_target_mask[0]` sentinel | If anvil pending, choose exactly one queued component option; no target/equip occurs |
| Choose completed-item anvil option | 7 | `a[1]=anvil option index`, `a[2]=0 sentinel` | Same conditional masks as component anvil | If anvil pending, choose exactly one queued completed-item option |
| Craft and equip | 8 | `a[1]=first component index`, `a[2]=second component index`, `a[3]=board/bench target` | `item_component_first_mask`, selected row of `item_component_pair_masks`, then `item_target_mask` | Resolve catalog component IDs, craft recipe, equip result to exact target |

Policy sampling is implemented in `policy.py:883-979`; PPO replay/log-probability reconstruction is implemented in `policy.py:1185-1245`. Native decoding is in `cpp/src/lobby/TftEngine.cpp:5340-5380`.

## 4. Anvil's type-7 overload

When an anvil is pending, native mask generation clears the ordinary action types, sets type 7 as the only permitted type, repurposes the nine-position `item_inventory_mask` to mark the offered option indices, and sets only target index zero in `item_target_mask` (`TftEngine.cpp:1115-1130`).

The policy's item-inventory scorer receives both the anvil option features and `anvil_pending`; it selects an option index using the same type-7 branch (`policy.py:883-905`). It also samples the target head, but the target mask restricts it to the zero sentinel. The native decoder checks `has_pending_anvil()` before ordinary inventory decoding, consumes only `action[1]`, and ignores the target sentinel (`TftEngine.cpp:5344-5359`).

Thus:
- The name `item_inventory_mask` is context-dependent: ordinary inventory positions when no anvil is pending, offered option positions when anvil is pending.
- Type 7 does not always mean equip. The pending-anvil state changes its native meaning to a mandatory grant choice.
- Target index zero is a forced placeholder for the autoregressive policy contract, not a real unit target during anvil selection.
- Native mask generation and native decoding jointly enforce this special case; a UI or replay consumer must preserve the pending-anvil context to interpret the action correctly.

## 5. Craft action and recipe conditioning

For type 8, policy sampling chooses the first component under `item_component_first_mask`, then chooses the second component using the row of `item_component_pair_masks` selected by the first index. It then conditions target scoring on the ordered pair and recipe semantic features. The native decoder maps the two catalog-order indices to component IDs and uses `action[3]` as the board/bench target (`TftEngine.cpp:5360-5380`).

The pair mask is generated from exact `ItemEngine::can_craft()` availability. The recipe feature matrix and compatibility scores provide policy context; masks remain the legality authority. Symmetric recipes may be represented in both ordered index positions even though the underlying recipe lookup is order-independent.

## 6. Python ablation and replay evidence

`cpp_lobby_env.py:get_action_masks()` supports the evaluation-only `TFT_ABLATE_ITEM_ACTIONS` setting. It suppresses optional type-7 equip and type-8 craft actions, but preserves type 7 when it is the sole legal action because that state is a mandatory anvil choice (`cpp_lobby_env.py:185-203`). This is consistent with the native overload and avoids making a pending anvil impossible to resolve in the ablation.

Existing tests:
- `tests/test_policy_item_conditioning.py:308-335` verifies anvil option sampling, forced target sentinel and equality of sampled versus replayed log probability.
- `tests/test_policy_item_conditioning.py:334-360` verifies craft component-pair conditioning and sampled/replayed log-probability agreement.
- `tests/test_action_mask_validation.py:64-84` validates selected item actions against their conditional masks.

These tests prove selected policy-level cases, not a complete end-to-end native/Python replay across every item state, inventory reorder, reset and invalid action.

## 7. Field-level dispositions

| Contract element | Current disposition |
|---|---|
| Six-wide action vector | `existing_shared_action_envelope_type_specific_semantics` |
| Type 7 ordinary inventory equip | `policy_and_native_binding_source_traced` |
| Type 7 anvil choice | `conditional_overload_with_forced_target_sentinel` |
| Type 8 craft-and-equip | `autoregressive_pair_then_target_binding` |
| Item masks | `separate_conditional_legality_inputs` |
| Inventory mask meaning | `context_dependent_inventory_or_anvil_option_indices` |
| Action/replay identity envelope | `not_established_by_this_positional_binding_audit` |

## 8. Remaining validation gaps (not authorized implementation)

1. Add native-to-Python round-trip fixtures for inventory equip, component anvil, completed-item anvil and craft-and-equip using the exact same observation/masks/action.
2. Validate inventory slot semantics when duplicate catalog item IDs exist and when an earlier inventory position is removed.
3. Validate anvil option ordering and the option index against the exact pending queue head across consecutive queued anvils.
4. Prove that invalid/stale action masks are rejected consistently at native decode and PPO replay boundaries.
5. Correlate each sampled action with the same episode/player/decision identity in the rollout buffer and replay manifest.
6. Keep type-7's conditional meaning explicit in any future action schema; do not rename the existing mask or infer ordinary equip from type 7 alone.

No runtime, schema, tensor-layout, PPO architecture, reward, mask, training, checkpoint, Viewer or Overwolf implementation is authorized by this audit. Issue #346 remains open and Gate 8 remains blocked.

## 9. Architecture reconstruction review

1. **Prior problem:** the overloaded type-7 semantics and reused mask names could be mistaken for a single equip operation.
2. **Technical justification:** anvil selection and equip share an action envelope but have different state transitions, target semantics and option sources.
3. **New responsibility:** this audit owns the explicit policy-to-native binding map for item actions.
4. **Contract and invariants:** type 7 is anvil selection when a pending anvil exists; otherwise it is inventory equip; anvil target zero is a sentinel; type 8 is component-pair craft-and-equip; masks are separate final legality constraints.
5. **Cross-component impacts:** native action vector, ItemEngine queue/inventory, mask generation, observation features, policy sampling, PPO replay, Python wrapper ablation, native decoder and diagnostic events.
6. **Objective validation:** source locations and current policy tests are enumerated; remaining native/Python round-trip tests are stated. Documentation only.

Issue #346 remains open. This document does not approve Gate 8 or runtime implementation.
