#include "reward/RewardModel.hpp"

#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <stdexcept>

namespace {
void require_close(double actual, double expected, const std::string& name) {
    if (std::abs(actual - expected) > 1e-9) {
        std::cerr << "[FAIL] " << name << ": actual=" << actual
                  << ", expected=" << expected << '\n';
        std::exit(EXIT_FAILURE);
    }
}
}

int main() {
    using namespace tft::reward_model;

    // Golden values mirror the formula-level Python tests and let us replay
    // the same sequence of snapshots on both implementations.
    require_close(combat(true, 3, 0, 0, 2),
                  2.0 + std::tanh(0.3) + 0.1,
                  "combat win reward");
    require_close(combat(false, 0, 3, 2, 0),
                  -2.0 - 0.1 - std::tanh(0.2),
                  "combat loss reward");

    // Sequence: empty board -> buy/place a 2-cost 1-star unit ->
    // improve synergy/positioning on the next action.
    const double first_action =
        0.05 + power(4.0, 0.0) + synergy(0.5, 0.0) +
        positioning(0.3, 0.0) + board(1, 28);
    const double second_action =
        power(4.0, 4.0) + synergy(1.0, 0.5) +
        positioning(0.8, 0.3) + economy(20, 100.0) +
        board(1, 28);

    require_close(first_action,
                  0.05 + std::tanh(0.4) + std::tanh(0.5) +
                      0.5 * std::tanh(0.3) + (1.0 / 28.0) * 0.15,
                  "first deterministic action reward");
    require_close(second_action,
                  std::tanh(0.5) + 0.5 * std::tanh(0.5) +
                      0.10 + (1.0 / 28.0) * 0.15,
                  "second deterministic action reward");

    require_close(placement(1, 8), 1.0, "first-place terminal reward");
    require_close(placement(8, 8), -1.0, "last-place terminal reward");
    require_close(placement(4, 8), 1.0 / 7.0, "middle-place terminal reward");

    require_close(xp_level_transition_value(60, 56, 80.0, 4, 7, 8),
                  0.05875, "late level milestone rewards surplus XP progress");
    require_close(xp_level_transition_value(22, 18, 80.0, 2, 4, 5),
                  0.02, "XP transition accounts for lost interest breakpoint");
    require_close(xp_level_transition_value(40, 36, 80.0, 2, 5, 5),
                  0.0, "XP without level transition has no progress reward");

    require_close(level(4, 1), 1.5, "level reward cap");
    require_close(economy(50, 20), 0.25 - 0.05, "economy reward");
    require_close(streak(5, 4), 0.15 + 0.08, "streak reward");
    require_close(blocked_move(), -0.35, "AntiLoop blocked move penalty");
    require_close(board_capacity_completion(), 0.25, "board capacity completion bonus");
    require_close(clamp_total(9.0), 5.0, "upper reward clamp");
    require_close(clamp_total(-9.0), -5.0, "lower reward clamp");
    require_close(gold_potential(0), 0.0, "zero gold potential");
    require_close(gold_potential(9), 0.018, "liquid gold potential below breakpoint");
    require_close(gold_potential(10), 0.10, "interest breakpoint potential");
    require_close(gold_change_reward(10, 9), -0.082, "spending below interest breakpoint");
    require_close(gold_change_reward(9, 10), 0.082, "saving to interest breakpoint");
    require_close(core_displacement_penalty(true, 0.0), -0.30,
                  "replacing a core unit without clear improvement is penalized");
    require_close(core_displacement_penalty(true, 2.0), 0.0,
                  "clear composition improvement can replace a core unit");
    require_close(core_displacement_penalty(false, -1.0), 0.0,
                  "non-core displacement does not receive the core-specific penalty");
    require_close(movement_no_progress_penalty(0.0, 0.0, 0.0), -0.10,
                  "no-progress movement baseline penalty");
    if (!(movement_no_progress_penalty(0.0, -2.0, -1.0) <
          movement_no_progress_penalty(0.0, 0.0, 0.0))) {
        throw std::runtime_error("movement degradation must increase penalty");
    }
    if (!(movement_no_progress_penalty(-4.0, 0.0, 0.0) <
          movement_no_progress_penalty(0.0, 0.0, 0.0))) {
        throw std::runtime_error("composition degradation must increase penalty");
    }
    require_close(purchase_quality(5.0, false), 0.22 * std::tanh(1.0),
                  "composition-aware purchase reward");
    require_close(purchase_quality(0.0, true), 0.20,
                  "purchase completing an upgrade");
    if (!(purchase_pair_quality(0.0) > 0.30)) {
        throw std::runtime_error("pair completion should have a clear but bounded acquisition signal");
    }
    if (!(unit_purchase_timing_reward(5, 50, 2, 1, 0.7, 80.0, false, false) > 0.0)) {
        throw std::runtime_error("useful unit purchase with excess gold should be rewarded in mid-game");
    }
    require_close(unit_purchase_timing_reward(5, 25, 2, 1, 0.7, 80.0, false, false),
                  0.0, "healthy mid-game should preserve a modest gold reserve");
    if (!(unit_purchase_timing_reward(6, 25, 2, 1, 0.7, 25.0, false, false) > 0.0)) {
        throw std::runtime_error("useful unit purchase should be rewarded under low-health pressure");
    }
    const double buy_50 = unit_purchase_timing_reward(4, 50, 2, 2, 0.8, 80.0, false, true);
    const double buy_100 = unit_purchase_timing_reward(4, 100, 2, 2, 0.8, 80.0, false, true);
    if (!(buy_100 > buy_50))
        throw std::runtime_error("useful unit acquisition should gain value from surplus gold");
    require_close(unit_purchase_timing_reward(4, 100, 2, 7, 0.8, 80.0, false, true),
                  0.0, "surplus must not fill an overcrowded bench");
    require_close(unit_purchase_timing_reward(5, 50, 1, 7, 0.7, 30.0, false, false),
                  0.0, "do not reward purchases when the bench is nearly full");
    require_close(early_purchase_reward(2, 10, 1, 2, 0.5, false, false),
                  0.20, "early useful unit purchase bonus");
    require_close(early_purchase_reward(2, 10, 1, 2, 0.0, false, true),
                  0.224, "early pair purchase bonus");
    require_close(early_purchase_reward(2, 10, 1, 8, 0.0, false, false),
                  0.0, "early low-fit purchase rejected with crowded bench");
    require_close(early_purchase_reward(3, 10, 1, 2, 0.5, false, false),
                  0.0, "early purchase bonus does not persist into later stages");
    require_close(reversed_purchase_penalty(), -0.18,
                  "targeted reversed-purchase penalty");
    // Regressions from the Viewer match: Teemo/Caitlyn were bought and sold
    // on the next action without being deployed or completing an upgrade.
    // Their low strategic-fit values must trigger the same reversal rule.
    if (!should_penalize_reversed_purchase(0.08, false, false, false, false))
        throw std::runtime_error("Teemo-like low-fit immediate reversal should be penalized");
    if (!should_penalize_reversed_purchase(0.14, false, false, false, false))
        throw std::runtime_error("Caitlyn-like low-fit immediate reversal should be penalized");
    if (!should_penalize_reversed_purchase(0.20, false, false, false, false))
        throw std::runtime_error("threshold-fit immediate reversal should be penalized");
    if (should_penalize_reversed_purchase(0.21, false, false, false, false))
        throw std::runtime_error("strategically useful unit should be exempt from low-fit reversal penalty");
    static_assert(kRecentPurchaseHistoryActions == 8,
                  "recent purchase association window should cover intervening actions");
    if (should_penalize_reversed_purchase(0.08, true, false, false, false))
        throw std::runtime_error("completed upgrades must remain exempt from reversal penalty");
    if (should_penalize_reversed_purchase(0.08, false, true, false, false))
        throw std::runtime_error("deployed purchases must remain exempt from reversal penalty");
    if (should_penalize_reversed_purchase(0.08, false, false, true, false))
        throw std::runtime_error("a sale required to free a full bench must remain exempt");
    if (should_penalize_reversed_purchase(0.08, false, false, false, true))
        throw std::runtime_error("explicitly verified composition improvement must remain exempt");
    const double teemo_sequence = 0.06 + (-0.02) +
        reversed_sequence_adjustment(0.06, -0.02);
    if (teemo_sequence > -0.05 + 1e-9)
        throw std::runtime_error("positive buy followed by a weakly negative sale must not retain positive aggregate reward");
    const double caitlyn_sequence = -0.09 + (-0.11) +
        reversed_sequence_adjustment(-0.09, -0.11);
    if (caitlyn_sequence > -0.05 + 1e-9)
        throw std::runtime_error("already-negative buy/sell sequence must remain negative");
    if (should_penalize_reversed_purchase(0.0, true, false, false, false))
        throw std::runtime_error("completed upgrade must be exempt from reversal penalty");
    if (should_penalize_reversed_purchase(0.0, false, true, false, false))
        throw std::runtime_error("deployed unit must be exempt from reversal penalty");
    if (should_penalize_reversed_purchase(0.0, false, false, true, false))
        throw std::runtime_error("full bench must be exempt from reversal penalty");
    if (should_penalize_reversed_purchase(0.0, false, false, false, true))
        throw std::runtime_error("composition transition must be exempt from reversal penalty");
    const double reversal_adjustment = reversed_sequence_adjustment(0.02, 0.20);
    if (!(0.02 + 0.20 + reversal_adjustment <= -0.05 + 1e-9)) {
        throw std::runtime_error("reversed purchase sequence must not retain positive aggregate reward");
    }
    require_close(reversed_sequence_adjustment(-0.10, -0.20), 0.0,
                  "already-negative reversal sequence needs no extra adjustment");
    require_close(purchase_pair_quality(0.0), 0.32,
                  "pair-building baseline bonus");
    if (!(purchase_pair_quality(10.0) > purchase_pair_quality(0.0))) {
        throw std::runtime_error("pair reward must increase with composition fit");
    }
    if (!(purchase_pair_quality(10.0) > purchase_quality(0.0, true))) {
        throw std::runtime_error("forming a pair must be valued above a generic upgrade signal");
    }
    if (!(spending_timing_reward(50, 100.0, 2, 1.0, false, false) > 0.0)) {
        throw std::runtime_error("a capped gold balance with a useful early purchase should have a small spending signal");
    }
    if (!(spending_timing_reward(50, 20.0, 5, 0.0, true, false) > 0.0)) {
        throw std::runtime_error("completing an upgrade with high gold must be rewarded under pressure");
    }
    if (!(spending_timing_reward(50, 20.0, 5, 0.9, false, false) > 0.0)) {
        throw std::runtime_error("high-fit purchase with excess gold must be rewarded under pressure");
    }
    if (!(spending_timing_reward(20, 10.0, 7, 1.0, true, false) > 0.0)) {
        throw std::runtime_error("an urgent upgrade should still be rewarded with low liquidity");
    }
    require_close(buy_xp_timing_reward(125, 80.0, 5, false), 0.0,
                  "non-leveling XP must not be a generic excess-gold sink");
    require_close(buy_xp_timing_reward(50, 35.0, 5, false), 0.0,
                  "non-leveling XP must not compete with useful unit purchases");
    if (!(buy_xp_timing_reward(50, 35.0, 5, true) >
          buy_xp_timing_reward(20, 80.0, 2, true))) {
        throw std::runtime_error("urgent level-up should be rewarded above safe early leveling");
    }
    require_close(buy_xp_timing_reward(25, 80.0, 5, false), 0.0,
                  "do not reward XP spending with low gold and safe health");
    require_close(buy_xp_timing_reward(40, 30.0, 5, false), 0.0,
                  "non-leveling XP below the interest cap must not receive a reward");
    if (!(buy_xp_timing_reward(25, 30.0, 5, true) > 0.0)) {
        throw std::runtime_error("an urgent level-up may be rewarded even below the interest cap");
    }
    require_close(buy_xp_timing_reward(10, 100.0, 2, false), 0.0,
                  "do not encourage early XP spending when economy and health are safe");
    if (!(buy_xp_timing_reward(50, 20.0, 5, true) <= 0.10)) {
        throw std::runtime_error("XP spending reward must remain capped to avoid repeated XP spam");
    }
    if (!(pass_opportunity_penalty(50, 100.0, 2, true) < 0.0)) {
        throw std::runtime_error("passing at the interest cap with a useful offer should be discouraged");
    }
    const double pass_50 = pass_opportunity_penalty(50, 100.0, 2, false);
    const double pass_75 = pass_opportunity_penalty(75, 100.0, 2, false);
    const double pass_125 = pass_opportunity_penalty(125, 100.0, 2, false);
    const double pass_200 = pass_opportunity_penalty(200, 100.0, 2, false);
    if (!(pass_50 > pass_75 && pass_75 > pass_125 && pass_125 > pass_200))
        throw std::runtime_error("PASS penalty must grow with gold above 50");
    if (!(pass_opportunity_penalty(125, 100.0, 2, true) <
          pass_opportunity_penalty(125, 100.0, 2, false)))
        throw std::runtime_error("PASS with a useful unit offer must be penalized more");
    if (!(pass_opportunity_penalty(50, 20.0, 6, true) < 0.0)) {
        throw std::runtime_error("passing with a useful offer, high gold and low HP must be discouraged");
    }
    require_close(pass_opportunity_penalty(50, 20.0, 6, false),
                  0.0, "must not force spending when the shop has no useful offer");
    require_close(item_crafting_bonus(-0.02), 0.0,
                  "poor item craft should not receive a crafting bonus");
    if (!(item_crafting_bonus(0.15) > 0.0 && item_crafting_bonus(0.15) <= 0.08)) {
        throw std::runtime_error("useful crafted items should receive a small bounded bonus");
    }
    require_close(reroll_quality_reward(8.0, 8.0), 0.0,
                  "reroll with no quality improvement receives no reward");
    require_close(strategy_action_reward(0, 1, 60, 58, 80.0, 4,
                                         false, true, false, false),
                  0.0, "non-reroll strategy gets no reroll improvement bonus");
    if (!(reroll_quality_reward(2.0, 10.0) > 0.0)) {
        throw std::runtime_error("reroll that reveals a much better offer should be rewarded");
    }
    if (!(reroll_quality_reward(10.0, 2.0) < 0.0)) {
        throw std::runtime_error("reroll that destroys a strong shop option should be discouraged");
    }
    if (!(reroll_quality_reward(2.0, 10.0, 50, 80.0, 4) >
          reroll_quality_reward(2.0, 10.0, 15, 80.0, 1))) {
        throw std::runtime_error("reroll improvement must be more valuable with surplus gold than in the safe early game");
    }
    if (!(reroll_quality_reward(10.0, 2.0, 50, 80.0, 4) < 0.0)) {
        throw std::runtime_error("reroll that destroys a stronger shop must receive a negative quality signal");
    }

    if (!protects_upgrade_path(2) || protects_upgrade_path(1)) {
        throw std::runtime_error("upgrade path must be protected across different star levels, but not for a lone unit");
    }
    if (!(sale_quality(0.0, false, true, true) < 0.0)) {
        throw std::runtime_error("selling a pair copy must remain unattractive even when it frees bench space");
    }
    require_close(sale_quality(0.0, false, false, true), 0.05,
                  "sale of low-fit non-core unit frees space");
    require_close(sale_quality(1.0, true, true, false), -0.765,
                  "sale protects core unit and upgrade copies");
    if (!(sale_quality(0.0, false, false, false) >
          sale_quality(0.5, false, false, false) &&
          sale_quality(0.5, false, false, false) >
          sale_quality(1.0, false, false, false))) {
        throw std::runtime_error("sale reward must decrease as bench-unit fit increases");
    }

    // Test A: a high-fit purchase should beat PASS even when it spends through
    // an interest threshold, while a low-value purchase should not.
    const double pass_reward = 0.0;
    const double strong_buy_reward = 0.05 +
        purchase_quality(10.0, false) + gold_change_reward(10, 8);
    const double weak_buy_reward = 0.05 +
        purchase_quality(0.0, false) + gold_change_reward(10, 8);
    if (!(strong_buy_reward > pass_reward && weak_buy_reward < pass_reward)) {
        std::cerr << "[FAIL] Economic decision shaping does not distinguish a strong buy from PASS.\\n";
        std::exit(EXIT_FAILURE);
    }

    // Phase 5: item reward shaping balances immediate combat value with
    // data-driven role/composition fit, shifting that balance by game stage.
    const double weak_item_strength = item_immediate_strength(
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    const double damage_item_strength = item_immediate_strength(
        10.0, 0.15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    const double defense_item_strength = item_immediate_strength(
        0.0, 0.0, 150.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    const double ability_item_strength = item_immediate_strength(
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 30.0, 0.0, 0.0);
    const double resist_item_strength = item_immediate_strength(
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 30.0, 0.0);
    const double mana_item_strength = item_immediate_strength(
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 30.0);
    require_close(weak_item_strength, 0.0, "no numeric combat effects have zero immediate strength");
    if (!(damage_item_strength > weak_item_strength &&
          defense_item_strength > weak_item_strength &&
          ability_item_strength > weak_item_strength &&
          resist_item_strength > weak_item_strength &&
          mana_item_strength > weak_item_strength &&
          damage_item_strength <= 1.0 && defense_item_strength <= 1.0 &&
          ability_item_strength <= 1.0 && resist_item_strength <= 1.0 &&
          mana_item_strength <= 1.0)) {
        throw std::runtime_error("item immediate strength must respond to supported combat stats and stay normalized");
    }
    const double early_comp_fit = item_assignment_quality(0.2, 0.9, 0.9, 1);
    const double early_raw_power = item_assignment_quality(0.9, 0.1, 0.1, 1);
    if (!(early_comp_fit > early_raw_power)) {
        throw std::runtime_error("early-game item reward should favor planned-comp fit over raw stats alone");
    }
    const double late_raw_power = item_assignment_quality(0.9, 0.1, 0.1, 7);
    const double late_comp_fit = item_assignment_quality(0.1, 0.9, 0.9, 7);
    if (!(late_raw_power > late_comp_fit)) {
        throw std::runtime_error("late-game item reward should favor immediate combat strength when comp fit is weak");
    }
    require_close(item_assignment_quality(0.0, 0.0, 0.0, 1), -0.03,
                  "strategically poor item assignment has bounded negative reward");
    if (item_assignment_quality(2.0, 2.0, 2.0, 4) > 0.20 ||
        item_assignment_quality(-1.0, -1.0, -1.0, 4) < -0.03) {
        throw std::runtime_error("item assignment reward must clamp out-of-range inputs");
    }

    // Strategy-specific shaping stays small and rewards the plan's actual goal.
    require_close(strategy_action_reward(0, 2, 40, 35, 80.0, 3,
                                         false, false, false, false),
                  -0.09, "ECON strongly discourages premature XP below interest cap");
    require_close(strategy_action_reward(0, 2, 50, 46, 80.0, 3,
                                         false, false, false, false),
                  -0.09, "ECON protects the interest floor when XP starts at 50 gold");
    require_close(strategy_action_reward(0, 1, 40, 38, 80.0, 3,
                                         false, true, false, false),
                  0.0, "ECON permits an improved reroll without preferring it to saving");
    require_close(strategy_action_reward(0, 1, 40, 38, 80.0, 3,
                                         false, false, false, false),
                  -0.025, "ECON discourages an unproductive reroll");
    require_close(strategy_action_reward(0, 0, 55, 50, 80.0, 4,
                                         true, false, false, false),
                  0.03, "ECON allows useful spending from surplus above 50");
    require_close(strategy_action_reward(2, 2, 40, 35, 80.0, 4,
                                         false, false, true, true),
                  0.025, "FAST8 keeps level progress modest below the interest cap");
    require_close(strategy_action_reward(3, 1, 40, 38, 80.0, 3,
                                         false, true, false, true),
                  0.10, "SLOWROLL rewards a useful reroll");
    require_close(strategy_action_reward(3, 1, 40, 38, 80.0, 3,
                                         false, false, false, true),
                  -0.025, "SLOWROLL penalizes a reroll without improvement");
    require_close(strategy_action_reward(1, 0, 25, 22, 30.0, 3,
                                         true, false, false, false),
                  0.07, "STABILIZE rewards a useful purchase");
    require_close(strategy_action_reward(6, 0, 40, 37, 70.0, 3,
                                         false, false, false, false),
                  -0.04, "LOSS_STREAK discourages wasteful spending");

    std::cout << "[PASS] C++ reward formulas and deterministic action sequence.\n";
    return EXIT_SUCCESS;
}
