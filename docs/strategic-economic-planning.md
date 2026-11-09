# Strategic and Economic Planning Architecture

## Goal

Introduce a coordinated strategic layer for composition and economy without
changing the PPO policy's behavior during the initial implementation.

The new architecture separates four responsibilities:

1. **Strategic Planner** — maintains a revisable medium-term plan, including
   composition direction and progression plan.
2. **Economic Controller** — selects the current resource posture needed to
   execute that plan while accounting for HP, projected damage, relative board
   strength, income, streaks, level and shop opportunities.
3. **Action Evaluator** — estimates the marginal value and cost of candidate
   actions. A posture is guidance, not a hard action restriction.
4. **Outcome Evaluator** — checks whether the investment achieved board,
   survival, upgrade, streak and economy outcomes.

## Composition behavior

Composition decisions are explicit:

- `KEEP`: preserve the current direction.
- `ADAPT`: adjust the lineup while retaining useful owned units.
- `PIVOT`: gradually transition toward a different direction.
- `ABANDON`: retire a direction that is no longer viable.

A pivot must account for transition cost and preserve valuable board pieces
where possible. A high-cost shop unit may become an anchor candidate, but cost
alone is not sufficient: item fit, current board contribution, reusable owned
units, contestation, level/shop odds and the cost of completing the direction
must also be considered. Buying an anchor does not force an immediate full
pivot; transition may be staged.

## Compatibility

The existing `EconomicStrategy` values (`ECON`, `STABILIZE`, `FAST8`,
`SLOWROLL`, `ALL_IN`, and legacy values) remain untouched in this phase.
They are legacy compatibility signals, not the new architecture's shared
decision model. No existing enum value is repurposed or renumbered.

## Safety boundary for PR 1

The C++ contract in `cpp/include/strategy/StrategicPlanning.hpp` is data-only.
It does not modify:
- PPO observation dimensions or encoding;
- action masks, action legality, or action execution;
- reward shaping or reward targets;
- checkpoint formats or training code.

The shared context uses native engine facts where available. Derived estimates
must be labeled as estimates and must not be presented as authoritative engine
values.

## Five-PR implementation sequence

### PR 1 — Shared contracts and audit schema
Add the typed data contract and document field semantics, ownership, and
compatibility. No decision logic or runtime behavior changes.

Acceptance:
- header is standalone and compiles under the repository's C++ standard;
- enums have stable explicit values;
- old strategy enum and checkpoint/action contracts remain unchanged;
- no reward, observation, mask, or action-execution diff.

### PR 2 — Strategic Planner in shadow mode
Build persistent plan selection and composition KEEP/ADAPT/PIVOT/ABANDON
recommendations. Include owned-unit reuse and anchor-opportunity scoring.
Recommendations are logged only; PPO actions remain authoritative.

Acceptance:
- deterministic tests for commitment persistence and revision hysteresis;
- tests for preserving high-value owned units;
- tests where a cost-4/5 anchor is rejected when fit or transition cost is poor;
- tests where an anchor supports a gradual pivot when the surrounding board
  makes the transition viable.

### PR 3 — Economic Controller and Action Evaluator in shadow mode
Produce posture and marginal action recommendations from the same context.
Allow exceptions; do not hard-mask actions or override PPO.

Acceptance:
- no fixed 50-gold or HP threshold used as a universal rule;
- a strong board can preserve a streak while retaining useful economy;
- a weak board can convert surplus into strength when the expected gain merits it;
- all recommendations include reason and confidence.

### PR 4 — Outcome evaluation and comparison reports
Correlate planner recommendations, actual PPO actions, and subsequent
outcomes. Report decision agreement, deviations, board/HP/streak/economy
changes, transition success, and plan churn.

Acceptance:
- shadow decisions never enter PPO rewards or training targets;
- reports distinguish correlation from causation;
- incomplete or unavailable fields are explicit, not silently defaulted.

### PR 5 — Gated, opt-in activation
Introduce explicit feature flags and staged activation. Keep shadow mode as the
default. Enable only validated recommendation classes; composition adaptation
precedes full pivots. Retain a one-switch rollback to PPO-only decisions.

Acceptance:
- default configuration remains behaviorally identical to the current PPO;
- no reward or PPO architecture changes are bundled into activation;
- integration tests prove disabled mode parity and enabled-mode scope;
- legacy strategy compatibility remains until downstream consumers migrate.

Fine-tuning and reward changes are a separate follow-up, based on evidence from
the outcome reports rather than assumptions.
