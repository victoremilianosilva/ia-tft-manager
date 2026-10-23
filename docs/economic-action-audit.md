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
