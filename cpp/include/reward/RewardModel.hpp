#pragma once

#include <algorithm>
#include <cmath>
#include <cstddef>

namespace tft::reward_model {

// Formula-compatible counterparts of ai/RewardManager.py.
// State is passed explicitly so both implementations can replay the same
// sequence of snapshots and compare every reward component.
inline double combat(
    bool won,
    double damage_dealt = 0.0,
    double damage_taken = 0.0,
    int enemy_alive = 0,
    int own_alive = 0
) noexcept {
    double reward = won ? 2.0 : -2.0;
    if (damage_dealt > 0.0)
        reward += std::min(std::tanh(damage_dealt / 10.0), 1.0);
    if (own_alive > 0)
        reward += std::min(static_cast<double>(own_alive) * 0.05, 0.25);
    if (enemy_alive > 0)
        reward -= std::min(static_cast<double>(enemy_alive) * 0.05, 0.25);
    if (damage_taken > 0.0)
        reward -= std::min(std::tanh(damage_taken / 15.0), 0.75);
    return reward;
}

inline double power(double current, double previous) noexcept {
    const double delta = current - previous;
    if (std::abs(delta) < 1e-6) return 0.0;
    return std::tanh(delta / 10.0);
}

inline double synergy(double current, double previous) noexcept {
    return std::tanh(current - previous);
}

inline double positioning(double current, double previous) noexcept {
    return 0.5 * std::tanh(current - previous);
}

inline double level(int current, int previous) noexcept {
    if (current <= previous) return 0.0;
    return std::min((current - previous) * 0.5, 1.5);
}

inline double economy(int gold, double hp) noexcept {
    double reward = 0.0;
    for (int threshold = 10; threshold <= 50; threshold += 10)
        if (gold >= threshold) reward += 0.05;
    if (hp <= 15.0) reward -= 0.15;
    else if (hp <= 30.0) reward -= 0.05;
    return reward;
}

inline double streak(int win_streak, int loss_streak) noexcept {
    double reward = 0.0;
    if (win_streak >= 2)
        reward += std::min(win_streak * 0.03, 0.15);
    if (loss_streak >= 2)
        reward += std::min(loss_streak * 0.02, 0.10);
    return reward;
}

inline double board(int occupied, int total_slots) noexcept {
    if (total_slots <= 0) return 0.0;
    return static_cast<double>(occupied) /
        static_cast<double>(total_slots) * 0.15;
}

inline double placement(int placement, int total_players) noexcept {
    if (total_players <= 1) return 0.0;
    return 1.0 - 2.0 *
        (static_cast<double>(placement - 1) /
         static_cast<double>(total_players - 1));
}

// Penalidade explícita para uma ação estruturalmente válida bloqueada pelo AntiLoop.
// É maior que a falha genérica (-0.10), sem dominar a recompensa terminal (+/-1.0).
inline double blocked_move() noexcept {
    return -0.35;
}

// Bônus pequeno, concedido uma única vez ao preencher a última vaga do nível.
inline double board_capacity_completion() noexcept {
    return 0.25;
}

// Potential-based shaping for liquid gold. The small linear term values
// liquidity; the larger 10-gold steps approximate the interest breakpoints.
// Applying only the potential delta avoids paying the agent repeatedly just
// for sitting on the same balance.
inline double gold_potential(int gold) noexcept {
    const int bounded = std::clamp(gold, 0, 50);
    return static_cast<double>(bounded) * 0.002 +
        static_cast<double>(bounded / 10) * 0.08;
}

inline double gold_change_reward(int old_gold, int new_gold) noexcept {
    return std::clamp(
        gold_potential(new_gold) - gold_potential(old_gold),
        -0.25, 0.25);
}

// A purchase should be judged by marginal composition fit, not simply by
// the fact that a shop action succeeded. Completing an upgrade is a separate
// strategic signal because its value is not fully represented by cost/role.
inline double purchase_quality(double fit_delta, bool completes_upgrade) noexcept {
    return 0.10 * std::tanh(fit_delta / 5.0) +
        (completes_upgrade ? 0.12 : 0.0);
}

// Composition-aware value for acquiring the second matching 1-star copy.
// A pair has option value even before it changes the board: the next copy can
// produce a 2-star unit. Keep fit as a multiplier, not a gate, so useful pairs
// are not ignored just because the current board is temporarily weak.
inline double purchase_pair_quality(double fit_score) noexcept {
    return 0.18 + 0.06 * std::tanh(std::max(0.0, fit_score) / 5.0);
}

// A low-fit purchase sold almost immediately is usually a wasted buy.
// Fit is normalized to [0, 1]; legitimate exceptions are explicit so a real
// upgrade, deployment, comp transition, or full bench is not punished.
inline constexpr double kRecentPurchaseLowFitThreshold = 0.20;

inline bool should_penalize_reversed_purchase(
    double normalized_fit,
    bool completed_upgrade,
    bool was_deployed,
    bool bench_was_full,
    bool composition_changed
) noexcept {
    return !completed_upgrade && !was_deployed && !bench_was_full &&
        !composition_changed &&
        std::clamp(normalized_fit, 0.0, 1.0) <= kRecentPurchaseLowFitThreshold;
}

inline double reversed_purchase_penalty() noexcept {
    return -0.18;
}

inline double reversed_sequence_adjustment(
    double prior_buy_reward,
    double sale_reward_including_gold,
    double target = -0.05
) noexcept {
    return std::min(0.0, target - prior_buy_reward - sale_reward_including_gold);
}

// Selling should be attractive for low-value clutter, but not intrinsically
// rewarding for disposing of useful bench units. Fit is normalized to [0, 1].
// Gold recovery is shaped separately by gold_change_reward().
inline double sale_quality(double fit_score, bool core_unit,
                           bool protects_upgrade, bool frees_bench_space) noexcept {
    const double fit = std::clamp(fit_score, 0.0, 1.0);
    // Selling a copy that completes a pair destroys accumulated upgrade
    // progress; this must outweigh the small convenience of freeing a slot.
    return 0.06 - 0.12 * fit -
        (core_unit ? 0.12 : 0.0) -
        (protects_upgrade ? 0.20 : 0.0) +
        (frees_bench_space ? 0.04 : 0.0);
}

// Shared no-progress penalty for both board repositioning and bench-to-board
// replacement. Negative deltas add proportional cost instead of being flattened
// by a fixed assignment in the action executor.
inline double movement_no_progress_penalty(
    double composition_delta,
    double synergy_delta,
    double positioning_delta
) noexcept {
    return -0.05
        - 0.10 * std::tanh(std::max(0.0, -composition_delta) / 5.0)
        - 0.10 * std::tanh(std::max(0.0, -synergy_delta))
        - 0.05 * std::tanh(std::max(0.0, -positioning_delta));
}

inline double clamp_total(double total) noexcept {
    return std::clamp(total, -5.0, 5.0);
}

} // namespace tft::reward_model
