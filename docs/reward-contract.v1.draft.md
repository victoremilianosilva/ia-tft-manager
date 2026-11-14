# Reward Contract v1 — Draft

**Status:** documentary specification; not approved for runtime implementation  
**Contract ID:** `tft.reward.v1`  
**Target architecture:** `new-arquiteture`  
**Related issues:** #287, #288, #295, #286, #294  
**Scope:** reward semantics, temporal attribution, normalization policy, invariants, and acceptance-test plan.

> This document defines the proposed contract for the new PPO lineage. It does not change current reward formulas, training, Engine behavior, checkpoints, or Shadow components. Existing formulas are evidence/baselines only, not normative definitions for v1.

## 1. Goals and non-goals

### Goals

1. Reward realized game consequences and opportunity costs, not compliance with a named strategy or a Shadow recommendation.
2. Separate immediate action feedback, round-level combat outcomes, terminal placement, and optional potential-based shaping.
3. Define temporal ownership, attribution windows, deduplication, and episode-boundary behavior for every signal.
4. Preserve per-player trajectory semantics in self-play and make rollout truncation explicit.
5. Make reward semantics reproducible through a versioned contract recorded with each checkpoint and experiment.
6. Prevent reward hacking, duplicate payment, and hidden strategy defaults.

### Non-goals

- No reward weights, formulas, or runtime code are changed by this document.
- No reward is derived from Shadow confidence, recommendation, evaluator score, composition score, or action approval.
- No manual action-to-combat attribution is introduced merely because an action preceded a combat result.
- No backward-compatibility promise is made for new semantic lineages; old checkpoints remain immutable historical baselines.

## 2. Normative principles

- **Outcome over intention:** score what the game state actually did, not what a planner wanted to happen.
- **One event, one owner:** a realized event can contribute to one canonical reward component only once.
- **No nominal strategy authority:** ECON/STABILIZE/FAST8/SLOWROLL/ALL_IN/WINSTREAK IDs, enum values, and booleans derived from them are forbidden reward inputs.
- **Unknown is not a strategy:** missing strategy/composition evidence must remain missing/unknown; it must never default to ECON or another policy.
- **Shadow isolation:** Shadow state may be logged for diagnosis, but it is not a reward label, target, multiplier, or eligibility gate.
- **Per-player isolation:** rewards, dones, bootstrap, and GAE are computed independently for each player trajectory.
- **Bounded and auditable:** every component must state its units, scale, bounds, event identity, source, timing, and deduplication key.
- **No unverified shaping:** if an outcome cannot be measured reliably, omit that shaping term rather than substituting a heuristic confidence score.

## 3. Reward decomposition

For player (i) at environment transition (t), the proposed decomposition is:

```text
r[i,t] = r_action[i,t]
       + r_economy[i,t]
       + r_progress[i,t]
       + r_combat[i,t]
       + r_terminal[i,t]
       + r_potential[i,t]
```

The components are logically distinct even if the Engine transports their sum. A future implementation must preserve component-level audit data so aggregate reward can be reconstructed exactly.

| Component | Event time | Primary evidence | Attribution |
|---|---|---|---|
| Action outcome | Same transition | requested/effective/executed action and Engine result | The action transition only |
| Economy / opportunity cost | Same transition plus realized later costs where needed | gold, spend/proceeds, interest eligibility, HP, stage, level, shop opportunities | State transition; never a named strategy |
| Progress | When a pair/upgrade/level/capacity change actually occurs | unit identity/copies/stars, level, board capacity | One-time event; link to originating action only when identity is reliable |
| Combat | PvP resolution | winner, damage, survivors, own/enemy alive state | The resolved combat event for each participant |
| Terminal placement | When placement becomes final | validated final rank and lobby size | One-time terminal event |
| Potential shaping | Every eligible state transition | versioned, bounded state potential | Potential difference only; no repeated absolute-state payment |

No new component may be added without defining the same metadata and proving it does not duplicate an existing component.

## 4. Component contract

### 4.1 Action outcome

- A successful legal action is not automatically valuable.
- A failed/rejected action may receive a small bounded failure signal only when the rejection is attributable to the action request and not to missing/corrupt producer data.
- The Engine remains the authority for legality and execution status.
- A no-op/PASS is not intrinsically good or bad. Its value comes from opportunity cost and subsequent outcomes, not a fixed nominal-mode bonus.
- Invalid/missing action envelopes are contract/data-quality failures, not player mistakes; they must not be converted into ordinary negative reward.

**Deduplication:** one action identity / transition identity. Revalidation or repeated log records must not pay or penalize again.

### 4.2 Economy and opportunity cost

The canonical economic signal must measure actual state consequences rather than reward a prescribed reserve target.

Permitted factual inputs include:
- gold before/after the action and actual spend/proceeds;
- interest earned/lost at the actual economy transition;
- level and XP before/after;
- HP, stage, streak, and remaining board capacity;
- whether a real useful shop opportunity existed, if that fact is independently defined and reproducible.

Rules:
- Do not add separate positive rewards for gold balance, interest thresholds, and gold-potential deltas when they describe the same liquidity event.
- Charge spending once; do not infer action cost from net gold if round income can occur in the same transition.
- A purchase, reroll, or XP spend is not rewarded merely for consuming gold.
- Economic urgency may depend on factual HP/stage/liquidity context, but not a strategy ID or Shadow recommendation.
- A missing strategic plan must not change the economic reward path.

**Candidate v1 design:** one bounded economic potential/delta or an equivalent single accounting model. Its exact function and coefficients remain calibration decisions; no legacy gold-potential formula is adopted automatically.

### 4.3 Purchase, pair, and upgrade progress

- Buying a unit is an acquisition event, not proof of board-strength improvement.
- A pair is progress only when the Engine confirms matching unit identity/copy state; an upgrade is progress only when the star-level transition is realized.
- Pay a pair/upgrade event once, at the transition where it becomes true.
- If a purchase immediately consumes bench copies to create an upgrade, count the realized upgrade once; do not also count the same copies as a separate pair event.
- Bench value may be recognized through a measured future upgrade or deployment outcome, not a composition-fit score.
- A later sale or pivot is a new realized event with its own proceeds/opportunity cost; it must not retroactively erase history or cause duplicate negative reward.

**Attribution window:** from acquisition until the copy is consumed, sold, eliminated with the episode, or the episode ends. A delayed event may be linked to the originating purchase only with stable unit/copy identity. If identity is ambiguous or several actions jointly enabled the event, record it as contextual progress without inventing a single causal owner.

### 4.4 XP and level progression

- Reward the realized level transition and its factual consequences (e.g. newly available board capacity), not XP expenditure by itself.
- Do not separately reward the same level-up through both generic level reward and capacity-unlock reward unless the contract defines non-overlapping outcomes.
- XP progress that does not cross a level boundary is not automatically valuable; any shaping must be potential-based, bounded, and proven not to encourage wasteful spending.
- Emergency survival context may alter opportunity cost only through observable facts, not a FAST8/ALL_IN/etc. multiplier.

### 4.5 Reroll

- A reroll is an expense, not a positive event.
- Any positive signal must be based on a realized, reproducible improvement in the available shop or a subsequent acquired outcome, and must not be paid repeatedly for cycling shops.
- The same acquired unit/upgrade cannot be credited once as reroll quality and again as purchase/progress.
- If the shop comparison cannot be made on a stable, versioned evidence basis, omit the quality shaping and retain only the canonical economic cost.

### 4.6 Sale and reversal

- Sale proceeds and lost future option value must be accounted for once.
- A buy→sell reversal may be measured as a complete sequence only when purchase and sale are joined by stable unit identity and action lineage.
- Do not apply both a generic sale penalty and a second reversal penalty for the same lost value.
- Do not punish a sale solely because a unit was previously labeled core by a legacy composition field.
- A pivot is not inherently bad; evaluate realized net consequences and allow new evidence to justify it.

### 4.7 Board strength and positioning

- Board power, frontline/backline structure, synergy, and positioning scores are currently heuristic state evaluators, not ground-truth outcomes.
- They may be diagnostics or candidates for a bounded potential function only after calibration against combat outcomes and explicit validity checks.
- If used as shaping, use a potential difference of the form (F_t = gamma Phi(s_{t+1}) - Phi(s_t)), with bounded/versioned (Phi), terminal handling, and tests against reward farming.
- Do not pay the same board gain as both purchase quality, board-power delta, synergy delta, positioning delta, and a later combat bonus without a demonstrated non-overlap.
- A board move that only changes a heuristic score is not proof of combat improvement.

### 4.8 Combat

- Combat reward is owned by the PvP resolution event and is delivered to the participating players.
- Victory/defeat, damage, and survivor counts may be retained as candidate outcome features, subject to regression and calibration.
- Damage and survivor terms must not duplicate the same underlying health/placement consequence.
- Combat reward must not be manually copied back onto every preceding buy/XP/reroll action.
- PvE rounds require a separately specified event contract; they must not be silently treated as PvP.

### 4.9 Terminal placement

- Placement reward is emitted exactly once when final rank is known and validated against lobby size.
- It is terminal, per player, and must not be emitted again on later calls or duplicate terminal events.
- The current linear rank mapping is a historical baseline, not an irrevocable v1 weight choice.
- Placement is not copied into every prior action reward; temporal credit flows through the return/GAE mechanism.

## 5. Temporal credit assignment

### 5.1 Existing PPO trajectory behavior confirmed by audit

The audited implementation currently:
- stores one reward, done, and value per agent and rollout step in `RolloutBuffer`;
- computes GAE independently for each agent;
- defaults to `gamma=0.99` and `gae_lambda=0.95`;
- uses each agent's `done` to stop both TD bootstrap and recursive GAE propagation;
- uses `next_value` / `next_done` at the end of the collected rollout, so a non-terminal rollout boundary bootstraps the value estimate;
- stores a per-transition `valid` flag, normalizes advantages using valid transitions, and builds optimizer batches from valid indices only.

For the current implementation, the recurrence is:

```text
delta[t] = reward[t] + gamma * next_value[t] * (1 - done[t]) - value[t]
gae[t]   = delta[t] + gamma * lambda * (1 - done[t]) * gae[t+1]
return[t] = gae[t] + value[t]
```

Defaults are configuration defaults, not immutable contract constants. The actual values used by an experiment must be recorded.

### 5.2 What GAE does and does not guarantee

- GAE propagates later reward information backward through the sampled per-player trajectory; it does not establish a causal mapping from a specific combat result to one purchase.
- The influence of distant rewards decays with (gammalambda) per step; long-delayed outcomes may have weak or noisy influence.
- At a non-terminal rollout boundary, the value estimate bootstraps the next state, but recursive GAE does not continue through data that has not yet been collected.
- At a true terminal state, bootstrap and recursion stop for that player.
- A player's elimination must not stop or leak into another player's trajectory.
- The rollout horizon, episode boundary, and terminal semantics must be recorded with the experiment.

### 5.3 Validity gap requiring explicit resolution

The audited `compute_returns_and_advantages()` recurrence does not consult `valid`; validity is applied later during advantage normalization and batch selection. Therefore, an invalid transition can still participate in the backward GAE recurrence and influence an earlier valid transition if the corresponding done boundary does not stop propagation.

**Required resolution before runtime acceptance:** define whether invalid rows are impossible in a contiguous trajectory, must break the recurrence, or must be represented by a separate validity/boundary mask. Add a regression test where an invalid row sits between valid rows and prove it cannot contaminate a valid advantage. Do not silently assume batch filtering alone solves this.

### 5.4 Termination versus truncation

The current buffer API exposes `done` and rollout-end bootstrap inputs, but the audit does not establish a separate, explicit terminal-versus-time-limit truncation contract for every wrapper.

The v1 data contract must distinguish:
- true terminal (elimination/final placement): no bootstrap beyond terminal;
- rollout truncation with a valid next state: bootstrap from that next state, but stop recursion at the collected boundary;
- environment interruption/data loss without a valid next state: mark the sample invalid or fail collection; do not fabricate a value.

A single ambiguous boolean must not encode both terminal and truncation if their bootstrap semantics differ.

### 5.5 Delayed-event attribution policy

1. Prefer ordinary trajectory returns/GAE for delayed combat and placement consequences.
2. Use explicit event-to-action linkage only for deterministic, identity-backed events such as a specific copy completing an upgrade.
3. If multiple actions jointly contributed, do not invent a single causal owner. Let trajectory credit operate, or use a separately validated shared attribution rule.
4. Never add a manual combat/placement bonus to earlier actions while the same event already enters the trajectory reward.
5. Record unresolved attribution as unknown; do not use hindsight labels derived from Shadow recommendations.

## 6. Normalization, clipping, and scale

Every component must specify:
- raw unit and sign convention;
- normalization denominator / reference range;
- lower and upper bounds;
- whether clipping occurs per component or after aggregation;
- aggregation order and numeric precision;
- handling of NaN, infinity, missing, stale, or invalid evidence;
- calibration dataset and version.

**No numeric v1 coefficients are approved in this draft.** Existing values in `RewardModel.hpp` and `TftEngine.cpp` are legacy behavior. They may be used as comparison baselines but must not be copied without ablation evidence.

The aggregation contract must explicitly state whether action-level clipping occurs before combat/terminal addition. The current path has an action transition clamp followed by Lobby combat/placement aggregation without a second combined clamp (as documented by the audit); a future implementation must not accidentally change this ordering.

## 7. Event identity, provenance, and checkpoint metadata

Each reward component should be reconstructible from an audit record containing at least:

- `reward_contract_id` and semantic version;
- match/episode ID, player ID, round/step, and transition sequence;
- component name and event ID / deduplication key;
- source state version and source fields;
- requested/effective/executed action identity when applicable;
- raw value, normalized value, clipped value, and final contribution;
- event timestamp/round and attribution window;
- attribution mode: direct, event-linked, trajectory-only, shared, or unknown;
- validity/staleness status and omission reason;
- aggregation order and total reward.

Checkpoint/training manifests must record the reward contract version/hash, relevant configuration (including `gamma`, `gae_lambda`, rollout length, reward normalization/clipping), Engine/catalog/rules identity, and code revision. A same-shaped tensor with a different reward meaning is semantically incompatible.

## 8. Legacy audit map — active versus not established

The source audit identified the following active legacy reward families in `PlayerEnv::step` / Lobby aggregation:

| Family | Existing examples | v1 disposition |
|---|---|---|
| Strategy-ID shaping | `strategy_action_reward`, `xp_strategy_reward_scale`, strategy-derived branches/fallbacks | Remove from new contract; replace only with factual consequences |
| Purchase/composition shaping | `purchase_quality`, `purchase_pair_quality`, composition fit, early purchase timing | Rebuild from realized acquisition/progress events; no composition score as target |
| Spending/economy shaping | `spending_timing_reward`, `gold_change_reward`, interest/liquidity logic | Consolidate into one non-duplicative factual accounting model |
| Reroll shaping | `tactical_reroll_quality_scale`, `reroll_quality_reward` | Rebuild from one-time realized shop/acquisition evidence; otherwise omit |
| XP shaping | `xp_level_transition_value`, `phase_xp_progress_reward`, `surplus_xp_spending_reward`, `xp_progress_reward`, `level` | Reward realized level/capacity outcomes once |
| Sale/reversal | `sale_quality`, `critical_all_in_sale_penalty`, reversal guards | Rebuild from identity-backed net outcomes; remove nominal mode |
| PASS/movement/core protection | `pass_opportunity_penalty`, `core_displacement_penalty`, movement shaping | Rebuild only from factual opportunity/cost and validated outcomes |

The audit also found:
- combat reward is called during PvP resolution and added to each participant's reward;
- placement reward is added once when rank becomes known;
- `state_reward()` / the broad RewardManager path was not established as the active Python training reward path in the inspected callgraph;
- empty `StrategyInfo` can fall back to strategy ID 0 (ECON) in active reward branches. This is prohibited in v1.

This is an inventory of observed legacy behavior, not a claim that all helper functions in the repository are active.

## 9. Acceptance-test matrix (required before runtime migration is accepted)

| Area | Required cases / invariant |
|---|---|
| Component isolation | Each component can be computed independently; aggregate equals exact sum in declared order |
| Strategy independence | Every strategy ID produces identical reward for identical factual transition; empty strategy equals unknown, not ECON |
| Shadow isolation | Changing Shadow scores/recommendations without changing game facts leaves reward unchanged |
| Purchase | Failed purchase, successful purchase without outcome, pair, upgrade, immediate auto-upgrade; no double payment |
| XP | XP spend without level, level transition, capacity unlock; no duplicate level/capacity reward |
| Reroll | No improvement, improvement, repeated rerolls, acquired unit; no reroll+purchase duplicate |
| Sale/reversal | Sell unrelated unit, sell recently purchased unit, pivot, identity unavailable; no duplicated reversal penalty |
| Economy | Interest threshold crossing, income in same step, spend/proceeds, gold cap/surplus, low HP; actual cost separated from income |
| Board/position | No-op, score-only change, genuine combat outcome change; potential shaping cannot be farmed |
| Combat | Win/loss, damage, survivors, PvE separation, repeated resolution; one event per participant |
| Placement | Every valid rank, invalid rank, duplicate terminal event; exactly once |
| GAE | Per-agent dones, terminal versus truncation, rollout boundary bootstrap, multiple delayed rewards |
| Validity | Invalid row between valid rows cannot contaminate valid GAE; invalid transitions excluded from optimization |
| Attribution | Single deterministic event, multiple contributing actions, missing identity, event after episode end |
| Numeric safety | NaN/Inf/missing/stale inputs, clipping order, extreme values, deterministic replay |
| Reward hacking | PASS farming, reroll loops, buy/sell loops, repeated positioning, repeated event delivery |
| Regression | Combat/placement baseline distribution and total-return behavior compared against immutable legacy baseline |

Tests must assert component values and event counts, not only final episode return.

## 10. Migration and approval sequence

1. Freeze this semantic contract and cross-review it with Observation Schema (#293), Action Contract (#294), Checkpoint Contract (#288), and Evaluation Protocol (#295).
2. Resolve the validity/GAE and terminal/truncation gaps in the implementation design before coding.
3. Define candidate coefficients and normalization using a versioned offline dataset; document ablations and reward-hacking checks.
4. Implement in isolated, reviewable changes only after Gate 8 approval. Do not modify legacy checkpoints; create a new reward lineage.
5. Run component tests, deterministic replay, multi-seed PPO evaluation, reward ablations, and baseline comparisons.
6. Promote only when real decision/outcome metrics improve without critical regressions; a higher internal reward alone is insufficient.

## 11. Gate 3 exit criteria

### Documentary exit (this PR)

- [x] Active reward sources and inactive/unconfirmed paths distinguished.
- [x] Immediate, economy, progress, combat, placement, and shaping semantics defined.
- [x] Delayed attribution, GAE, per-player dones, rollout bootstrap, and truncation limitations documented.
- [x] Double-counting and reward-hacking risks mapped.
- [x] Shadow scores/recommendations excluded as reward targets.
- [x] Component-level acceptance-test matrix specified.
- [x] Runtime implementation explicitly deferred until Gate 8.

### Runtime migration (not part of this gate's documentary PR)

- [ ] Strategy/composition legacy dependencies removed from active reward path.
- [ ] Reward components implemented and tested against this contract.
- [ ] GAE validity and terminal/truncation gaps resolved in code.
- [ ] Reward schema/hash emitted in checkpoint and experiment manifests.
- [ ] Retraining and evaluation completed under #295.

**Gate status:** documentary Reward Contract v1 is specified; runtime migration and empirical acceptance remain blocked until Gate 8 and subsequent implementation/evaluation issues.
