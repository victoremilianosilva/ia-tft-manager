# PPO / Shadow isolation contract

## Purpose

This contract makes Shadow isolation a continuously checked architecture
boundary. Shadow planners may inspect the live state and emit diagnostics, but
their outputs are not policy inputs and failures must not escape into the game
transition that supplies PPO with observations, masks, rewards and outcomes.

## Allowed dependencies

- Read-only access to the current player, board, bench, shop, economy, items,
  opponent snapshots and composition context.
- Pure planner/evaluator calls whose outputs are diagnostic recommendations.
- Shadow-owned runtime state and append-only diagnostic recording.
- Viewer/audit serialization of source observations and recommendations.

## Forbidden dependencies and effects

Shadow code must not:
- execute or rewrite a \`PlayerAction\`;
- call action validation, action-mask generation or mask refresh APIs;
- mutate game state, board, bench, shop, economy, items or combat state;
- write PPO observations, action masks, rewards, rollout buffers, checkpoints,
  optimizer state or training configuration;
- feed a recommendation back into the active composition, policy or executor;
- make the engine transition depend on successful diagnostic recording.

The current Shadow evaluation block is fenced by
\`run_shadow_isolated()\`. Planner, adapter, evaluator and recorder exceptions
are contained; the failure callback is itself best-effort and cannot rethrow
into the engine transition. The existing strategic/economic diagnostic
success flags are cleared on failure.

## CI enforcement

\`tests/test_shadow_ppo_isolation_architecture.py\` checks:
- the complete strategic/economic/Composition Intelligence evaluation block
  uses the no-throw boundary;
- prohibited game/PPO mutator APIs are absent from that block;
- Shadow diagnostic fields are not read by \`build_observations()\`;
- the failure boundary catches both planner and failure-reporter exceptions.

\`cpp/tests/test_shadow_failure_boundary.cpp\` exercises successful execution,
standard and unknown planner exceptions, and a throwing failure reporter.

The native Shadow workflow builds the boundary test and runs the architecture
checks on every relevant pull request.

## Limits of this proof

This layer proves source-level dependency restrictions and exception
containment; it does not claim that recommendation quality is validated or
that PPO should agree with either evaluator. It also does not replace
state-fixture parity tests for every future Shadow integration. Such tests
must compare observations, masks, available actions, rewards and deterministic
transition outputs with the same fixture and seed before any Shadow output can
be considered for activation.

PPO remains the policy authority. Baseline/contextual/PPO divergence is
diagnostic only. No recommendation is activated by this contract.
