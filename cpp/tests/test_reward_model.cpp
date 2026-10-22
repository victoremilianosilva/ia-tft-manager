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
    require_close(movement_no_progress_penalty(0.0, 0.0, 0.0), -0.05,
                  "no-progress movement baseline penalty");
    if (!(movement_no_progress_penalty(0.0, -2.0, -1.0) <
          movement_no_progress_penalty(0.0, 0.0, 0.0))) {
        throw std::runtime_error("movement degradation must increase penalty");
    }
    if (!(movement_no_progress_penalty(-4.0, 0.0, 0.0) <
          movement_no_progress_penalty(0.0, 0.0, 0.0))) {
        throw std::runtime_error("composition degradation must increase penalty");
    }
    require_close(purchase_quality(5.0, false), 0.10 * std::tanh(1.0),
                  "composition-aware purchase reward");
    require_close(purchase_quality(0.0, true), 0.12,
                  "purchase completing an upgrade");
    require_close(sale_quality(0.0, false, false, true), 0.13,
                  "sale of low-fit non-core unit frees space");
    require_close(sale_quality(1.0, true, true, false), -0.22,
                  "sale protects core unit and upgrade copies");

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

    std::cout << "[PASS] C++ reward formulas and deterministic action sequence.\n";
    return EXIT_SUCCESS;
}
