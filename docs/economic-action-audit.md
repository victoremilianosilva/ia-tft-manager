# Economic action audit

The economic audit is an observability layer. It does not modify action masks,
the observation supplied to the policy, or PPO reward targets.

## Source of truth

The C++ EconomyEngine remains the authority for economy rules. Each audit
snapshot exposes the actual gold balance used for the most recent interest
calculation (gold_before_interest), the interest that would be paid if the
round resolved at the current balance (interest_if_resolved_now), and the
engine-computed board power, synergy, and positioning scores. Python records
and compares these values; it does not reimplement the interest formula.

Interest is calculated from the gold balance before base income, interest,
streak income, and win income are added. gold_before_interest therefore must
not be inferred from the final round balance.

## Per-action fields

Each action entry includes economic_diagnostics. Actual action cost, sale proceeds, action-time gold before/after, interest potential before/after, and XP/level before/after come from a native engine event captured before round income is resolved. gold_after_step preserves the later snapshot balance if the same step also resolves a round. Older logs without that event are explicitly marked as using a gold-delta fallback.

- gold_before, gold_after, gold_delta, action_cost, listed_cost, and
  sale_proceeds;
- gold_before_interest, current potential interest before/after the action,
  and potential_interest_delta;
- base_income, interest_income, streak_income, and win_income from the
  engine's last resolved round;
- level and XP before/after, board power, synergy, positioning, pair/upgrade
  counts, and trait milestone changes;
- reason_code and measurable_improvement.

reward_components preserves the available action, combat, placement, and
returned reward channels for diagnosis. These are not a decomposition of every
internal term used by the action reward formula.

## Reason-code interpretation

- PURCHASE_UPGRADE, PURCHASE_SYNERGY_GAIN, PURCHASE_BOARD_GAIN,
  PURCHASE_NO_IMMEDIATE_GAIN
- REROLL_IMMEDIATE_GAIN, REROLL_NO_IMMEDIATE_BOARD_GAIN
- XP_LEVEL_UP, XP_NO_LEVEL_UP; xp_level_up_unused is an aggregate audit metric
- DEPLOY_BOARD_GAIN, DEPLOY_NO_POWER_GAIN
- REPOSITION_IMPROVED, REPOSITION_NO_SCORE_GAIN
- SALE_GOLD_RECOVERY, PASS_NO_SPEND

“No immediate gain” is not proof of a bad decision. For example, a reroll may
improve future shop options, and XP may be a deliberate investment that pays off
later. The report flags these cases for review instead of applying a penalty.


## Purchase followed by sale

A recent purchase followed by a sale is not automatically classified as a bad
decision. The audit correlates the acquired UUID and records the sale context
using separate categories:

- `IMPULSIVE_REVERSED`: low composition fit and low strategic value, with no
  pair/upgrade progress, better owned alternative, composition transition,
  deployment, full-bench constraint, or sale-funded necessary action.
- `EXPERIMENTAL_REPLACED`: a later, materially better-fit purchase remains
  owned when the earlier experiment is sold.
- `PAIR_OR_UPGRADE`: the acquisition completed a same-star pair/upgrade path.
- `COMP_TRANSITION`: the composition direction/focus/core plan changed before
  the sale.
- `BENCH_CAPACITY`: the bench was full immediately before the sale.
- `ECONOMIC_NEED`: sale proceeds made the next XP purchase, reroll, or shop
  purchase affordable when it was not affordable before the sale.
- `DEPLOYED_THEN_SOLD`: the acquired unit was deployed before being sold.
- `UNJUSTIFIED_REVIEW`: no reason was demonstrated, but the purchase had
  enough strategic value that the audit must not label it impulsive.

Only `IMPULSIVE_REVERSED` contributes to the reversed-purchase counters and
the corresponding medium-severity finding. `UNJUSTIFIED_REVIEW` is a low
severity review item, not a PPO penalty. Ambiguous UUID correlation remains
`UNKNOWN` and is never penalized automatically.

The native PPO shaping follows the same conservative principle: it penalizes
only low-fit purchases without a concrete exception. Pair-building, a better
owned alternative, a real composition transition, deployment, full-bench
pressure, and sales that unlock the 2g/4g spending thresholds are exempt. This
does not prevent the policy from buying, testing, or changing its mind; it
reduces the reward for demonstrably wasteful low-value buy/sell loops.


## Core units and upgrade-path sale potential

Selling is never blocked solely because a champion is marked core or because
copies exist. The native reward uses a graduated retention cost and a small default sale cost. Selling low-fit clutter is positively shaped only when the bench is actually full; the separate gold-potential delta still recognizes real interest-threshold recovery. The candidate feature vector exposes exact same-star upgrade-path strength to the SELL head instead of a redundant trait-overlap count:

- Composition importance is based on the unit's normalized fit with the active
  plan; a core label with weak actual fit receives less protection than a
  high-fit core unit.
- Upgrade potential is based on remaining same-champion, same-star copies.
  Selling one of exactly two 1-star copies has the highest immediate pair
  opportunity cost; additional copies reduce that cost because a pair may
  remain. A 2-star copy is valued for a same-star 3-star route, while three
  1-star copies are treated as a weaker route to another 2-star.
- A materially better-fit unit already owned, a confirmed composition/focus
  transition, a measurable board improvement, full bench pressure, or a sale
  that unlocks a real 2g reroll / 4g XP purchase softens the retention cost.
- Gold recovery remains represented by the economy reward and is not treated
  as proof that every sale was strategically correct.

The audit records copy counts, star tier, estimated upgrade-path strength,
core status, composition-decision status, and bench capacity for every sale.
Core/pair findings are still checked for immediate or near-term board,
synergy, positioning, and upgrade compensation. This is reward shaping and
diagnostics, not a hard sale prohibition.

## Reports and metrics

Run the viewer on a match, then audit the resulting session directory:

    python audit_viewer_match.py viewer/sessions/<match-directory>

The Markdown and JSON reports include per-player economic action totals,
gold spent by action and stage, sale proceeds, potential interest lost by
crossing an engine-reported interest threshold, XP purchases without a level-up,
level-ups whose new board capacity was not used before passing/round end, and
rerolls without immediate board/upgrade/synergy improvement (including reroll
followed by PASS). Final gold and final board power are reported together.

Potential interest lost is an opportunity indicator computed from the engine's
current-interest snapshots; it is not a claim that the player definitely would
have received that exact amount at the next round. Strategic outcomes require
multi-seed comparisons of placements, HP, board power, and final gold.
