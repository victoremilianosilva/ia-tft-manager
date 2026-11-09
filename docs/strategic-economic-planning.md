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
possible. Cost-4/5 shop units and already-owned high-value units may become
anchors, but cost alone is insufficient: the alternative lineup must actually
include the anchor, reuse owned units where possible, and account for item fit,
opponent-owned copies, shop odds and lineup overlap. The runtime currently
evaluates at most two anchor directions per strategy refresh to bound the
additional planner work.

The reported transition cost is a normalized lineup-replacement estimate
(1 minus Jaccard overlap), not a gold cost. Confidence is a heuristic ranking
signal, not a calibrated probability. Pivot hysteresis advances at most once
per round; repeated actions in one round do not count as independent evidence.
A shadow pivot recommendation does not change the active commitment or live
composition direction.

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

### PR 2 — Strategic Planner in shadow mode (implementation in review)
The native engine now evaluates high-cost (4/5) shop units as possible
composition anchors. For each candidate trait it builds an alternative lineup
with the existing CompositionPlanner, measures overlap/reusable owned pieces,
and feeds the result to the new StrategicPlanner. The recommendation and
commitment/hysteresis state are exposed through strategy diagnostics only.

The planner can recommend `KEEP/ADAPT/PIVOT/ABANDON`; a pivot from a viable
locked direction requires repeated evidence. A direction that is no longer
viable can pivot immediately when a supported alternative exists. Valuable
owned/core units and item-bearing units are reported as preserve candidates.

Acceptance: deterministic tests for commitment persistence/hysteresis,
preservation of valuable owned units, rejection of poor anchors, and gradual
pivot when an anchor plus existing board makes transition viable. Runtime
shadow output must remain observational and never mutate the active direction
or PPO action path.

### PR 3 — Economic Controller and Action Evaluator in shadow mode
Generate posture and marginal action recommendations from the shared context.
Allow exceptions; do not hard-mask actions or override PPO.

The Economic Controller ranks contextual postures (accumulate, preserve a
streak, invest XP, roll for upgrades, stabilize, emergency investment) using
continuous pressure signals rather than a single universal gold/HP cutoff.
The current progression intent is carried into the shared context explicitly:
FAST8 maps to a level-eight plan and SLOWROLL maps to a three-star reroll plan;
these legacy labels are compatibility inputs, not the new controller's output.
The Action Evaluator ranks only available candidates supplied from native
state, balancing estimated board gain, composition fit, upgrade opportunity,
survival/streak value and opportunity cost (including engine-computed lost
interest at the current balance). A recommendation is not an instruction.

Current shop-unit board gains and future HP/streak effects are heuristic
estimates, not calibrated probabilities. Incoming damage is not yet a reliable
shared-context signal and remains unavailable rather than being fabricated.
The active PPO action is not overridden or compared here; exact action
agreement/deviation belongs to PR 4's event-level correlation.

Acceptance: no universal fixed gold/HP threshold; preserve a strong streak
without needless spending; convert surplus into strength when justified;
every recommendation includes reason and confidence; no changes to PPO,
rewards, masks, action legality, execution or training.

### PR 4 — Outcome evaluation and comparison reports
Correlate recommendations, actual PPO actions and subsequent outcomes. The
Viewer's existing **Auditoria completa…** flow captures the shadow diagnostics
in each action snapshot and generates a linked set of Markdown reports in one
run: PPO actions, Strategic Planner, Economic Controller, Action Evaluator,
divergences, immediate outcomes and final observed state.

The offline Outcome Evaluator measures before/after deltas for gold, HP, board
power, level, XP, pairs and star upgrades, plus the state observed at the end
of the round (after remaining preparation actions and combat) and the last
round-end state for each player. Round-end deltas are contextual outcomes, not
attribution to an individual action. These are descriptive correlations, not
causal attribution. Agreement between PPO and Action Evaluator is calculated
only when both action labels are present and normalized to equivalent categories.

The Viewer keeps the structured JSON report in a temporary directory for its
internal hand-off; the session audit folder receives Markdown files only.
Older sessions without shadow fields remain auditable and show those sections
as unavailable rather than failing or fabricating defaults.

Acceptance: shadow decisions never enter PPO rewards or targets; reports
distinguish correlation from causation; unavailable data is explicit; one
existing Viewer action generates the Markdown index and split reports; no JSON
artifact is left in the session audit directory.

### PR 5 — Gated, opt-in activation
Add explicit feature flags and staged activation. Shadow remains default.
Enable validated recommendation classes gradually; composition adaptation
precedes full pivots. Keep one-switch rollback to PPO-only behavior.

Acceptance: default mode remains behaviorally identical; no reward/PPO changes
are bundled; tests prove disabled-mode parity and enabled-mode scope; legacy
strategy compatibility remains until consumers migrate.

Fine-tuning and reward changes are separate follow-ups, based on outcome
reports rather than assumptions.
