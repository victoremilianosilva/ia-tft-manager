# Strategic and Economic Planning Architecture

## Goal

Coordinate composition and economy without changing PPO behavior during the
initial implementation.

The architecture has four responsibilities:

1. **Strategic Planner** — maintains a revisable medium-term plan, including
   composition direction and progression plan.
2. **Economic Controller** — selects the resource posture needed to execute
   that plan using HP, projected damage, relative board strength, income,
   streaks, level and shop opportunities.
3. **Action Evaluator** — estimates marginal value and cost of actions. A
   posture is guidance, never a hard action restriction.
4. **Outcome Evaluator** — checks whether investments achieved board,
   survival, upgrade, streak and economy outcomes.

## Composition behavior

- `KEEP`: preserve the current direction.
- `ADAPT`: adjust the lineup while retaining useful owned units.
- `PIVOT`: gradually transition toward another direction.
- `ABANDON`: retire a direction that is no longer viable.

A pivot accounts for transition cost and preserves valuable board pieces where
possible. A high-cost shop unit may become an anchor, but cost alone is
insufficient: item fit, current board contribution, reusable owned units,
contestation, level/shop odds and completion cost also matter. Buying an anchor
does not force an immediate full pivot; transition may be staged.

## Compatibility

Existing `EconomicStrategy` values (`ECON`, `STABILIZE`, `FAST8`,
`SLOWROLL`, `ALL_IN`, and legacy values) remain unchanged in this phase.
They are compatibility signals, not the new architecture's decision model.
No old enum value is repurposed or renumbered.

## PR 1 safety boundary

`cpp/include/strategy/StrategicPlanning.hpp` is data-only. It does not modify
PPO observations/dimensions, action masks or legality, action execution,
reward shaping/targets, checkpoint formats, or training code. Derived
estimates must be labeled as estimates, not authoritative engine facts.

## Five-PR sequence

### PR 1 — Shared contracts and audit schema (this PR)
Add typed contracts and document field semantics and compatibility. No runtime
decision logic or behavior changes.

Acceptance: standalone header compiles under the repository C++ standard;
enum values are explicit and stable; old strategy/action/checkpoint contracts
remain unchanged; no reward, observation, mask or execution changes.

### PR 2 — Strategic Planner in shadow mode
Implement persistent plan selection and `KEEP/ADAPT/PIVOT/ABANDON`
recommendations, owned-unit reuse and anchor-opportunity scoring. Log only;
PPO actions remain authoritative.

Acceptance: deterministic tests for commitment persistence/hysteresis,
preservation of valuable owned units, rejection of poor anchors, and gradual
pivot when an anchor plus existing board makes transition viable.

### PR 3 — Economic Controller and Action Evaluator in shadow mode
Generate posture and marginal action recommendations from the shared context.
Allow exceptions; do not hard-mask actions or override PPO.

Acceptance: no universal fixed gold/HP threshold; preserve a strong streak
without needless spending; convert surplus into strength when justified;
every recommendation includes reason and confidence.

### PR 4 — Outcome evaluation and comparison reports
Correlate recommendations, actual PPO actions and subsequent outcomes. Report
agreement/deviation, board/HP/streak/economy changes, transition success and
plan churn.

Acceptance: shadow decisions never enter PPO rewards or targets; reports
distinguish correlation from causation; unavailable data is explicit.

### PR 5 — Gated, opt-in activation
Add explicit feature flags and staged activation. Shadow remains default.
Enable validated recommendation classes gradually; composition adaptation
precedes full pivots. Keep one-switch rollback to PPO-only behavior.

Acceptance: default mode remains behaviorally identical; no reward/PPO changes
are bundled; tests prove disabled-mode parity and enabled-mode scope; legacy
strategy compatibility remains until consumers migrate.

Fine-tuning and reward changes are separate follow-ups, based on outcome
reports rather than assumptions.
