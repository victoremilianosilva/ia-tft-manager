#pragma once

#include <algorithm>
#include <cmath>
#include <cstddef>
#include <cstdint>

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
    // Give a useful acquisition a learnable immediate signal. The board-fit
    // delta alone can be near zero when the team is still being assembled.
    return 0.22 * std::tanh(fit_delta / 5.0) +
        (completes_upgrade ? 0.20 : 0.0);
}

// Composition-aware value for acquiring the second matching 1-star copy.
// A pair has option value even before it changes the board: the next copy can
// produce a 2-star unit. Keep fit as a multiplier, not a gate, so useful pairs
// are not ignored just because the current board is temporarily weak.
inline double purchase_pair_quality(double fit_score) noexcept {
    // A pair is real upgrade progress even before the third copy appears.
    // Keep the baseline meaningful, while favoring units that fit the plan.
    return 0.32 + 0.14 * std::tanh(std::max(0.0, fit_score) / 5.0);
}

// Reward timely, high-value spending when liquidity is already healthy and
// either the player is under pressure or the game is late. This is deliberately
// conditional on purchase quality / an actual level-up: spending by itself is
// never rewarded, so reroll spam and low-fit shopping cannot farm reward.
inline double spending_timing_reward(
    int gold_before,
    double hp,
    int stage,
    double normalized_fit,
    bool completes_upgrade,
    bool leveled_up
) noexcept {
    if (gold_before < 20 || (!completes_upgrade && !leveled_up &&
        normalized_fit < 0.35)) {
        return 0.0;
    }

    // Spending becomes increasingly attractive once the 50-gold interest cap
    // is reached, but there is still a small signal for good early purchases.
    const double liquidity = gold_before >= 50 ? 1.0
        : (gold_before >= 40 ? 0.75
        : (gold_before >= 30 ? 0.50 : 0.25));
    const double health_urgency = std::clamp((55.0 - hp) / 55.0, 0.0, 1.0);
    const double stage_urgency = std::clamp((static_cast<double>(stage) - 2.0) / 4.0,
                                            0.0, 1.0);
    const double baseline_urgency = gold_before >= 50 ? 0.25 : 0.0;
    const double urgency = std::max({health_urgency, stage_urgency, baseline_urgency});
    if (liquidity <= 0.0 || urgency <= 0.0) return 0.0;

    const double quality = (completes_upgrade || leveled_up)
        ? 1.0 : std::clamp(normalized_fit, 0.0, 1.0);
    return 0.24 * liquidity * urgency * quality;
}

// Reward buying XP when it is strategically timely, including purchases that
// do not immediately cross a level boundary. This prevents the agent from
// hoarding a large bank until the end of the match. Early XP remains discouraged
// unless the player is under pressure; the strongest signal requires high gold
// or a level-up.
inline double buy_xp_timing_reward(
    int gold_before,
    double hp,
    int stage,
    bool leveled_up
) noexcept {
    // XP is not a generic reward for spending. Non-leveling XP gets only a
    // tiny signal while the player is at the 50-gold cap; once spending drops
    // below that cap, stop rewarding consecutive XP buys. Actual level-ups can
    // still be rewarded with less gold when they are strategically urgent.
    if (stage <= 2 && hp >= 60.0) return 0.0;
    if (!leveled_up && gold_before < 50) return 0.0;
    if (leveled_up && gold_before < 30 && hp >= 35.0) return 0.0;

    const double liquidity = gold_before >= 50 ? 1.0
        : (gold_before >= 40 ? 0.70 : (gold_before >= 30 ? 0.40 : 0.20));
    const double health_urgency = std::clamp((55.0 - hp) / 55.0, 0.0, 1.0);
    const double stage_urgency = std::clamp((static_cast<double>(stage) - 3.0) / 4.0,
                                            0.0, 1.0);
    const double hoarding_urgency = gold_before >= 50 ? 0.45 : 0.0;
    const double urgency = std::max({health_urgency, stage_urgency, hoarding_urgency});
    if (urgency <= 0.0) return 0.0;
    const double quality = leveled_up ? 1.0 : 0.20;
    // Level-up reward is capped; intermediate XP buys cannot farm large returns.
    return std::min(0.10, 0.10 * liquidity * urgency * quality);
}

// Small additional signal for useful unit acquisitions beyond the early game.
// Requires real composition fit or upgrade progress, available bench space and
// enough remaining gold, so this cannot reward arbitrary shop-clearing.
inline double unit_purchase_timing_reward(
    int stage,
    int gold_before,
    int cost,
    int bench_count,
    double normalized_fit,
    double hp,
    bool completes_upgrade,
    bool builds_pair
) noexcept {
    if (stage < 3 || cost <= 0 || gold_before < cost ||
        bench_count >= 7 || gold_before - cost < 15) return 0.0;

    const double fit = std::clamp(normalized_fit, 0.0, 1.0);
    if (!completes_upgrade && !builds_pair && fit < 0.35) return 0.0;

    const double liquidity = gold_before >= 50 ? 1.0
        : (gold_before >= 40 ? 0.70 : (gold_before >= 30 ? 0.35 : 0.0));
    const double urgency = std::max(
        gold_before >= 50 ? 0.65 : (gold_before >= 40 ? 0.30 : 0.0),
        std::clamp((50.0 - hp) / 50.0, 0.0, 1.0));
    if (liquidity <= 0.0 || urgency <= 0.0) return 0.0;

    const double quality = (completes_upgrade || builds_pair)
        ? 1.0 : fit;
    const double bench_capacity = bench_count <= 3 ? 1.0
        : (bench_count <= 5 ? 0.75 : 0.40);
    return std::min(0.08, 0.08 * liquidity * urgency * quality * bench_capacity);
}

// Early-game acquisition shaping: prefer filling useful pairs and building a
// playable bench before spending actions on XP. This is deliberately bounded
// and only applies when there is room and the purchase is affordable.
inline double early_purchase_reward(
    int stage,
    int gold_before,
    int cost,
    int bench_count,
    double normalized_fit,
    bool completes_upgrade,
    bool builds_pair
) noexcept {
    if (stage > 2 || bench_count >= 9 || cost <= 0 || gold_before < cost)
        return 0.0;

    const double fit = std::clamp(normalized_fit, 0.0, 1.0);
    if (!completes_upgrade && !builds_pair && fit < 0.15)
        return 0.0;

    const double capacity = bench_count <= 3 ? 1.0
        : (bench_count <= 5 ? 0.75 : 0.40);
    const double quality = completes_upgrade ? 1.0
        : (builds_pair ? std::max(0.65, fit) : fit);
    return capacity * (0.12 + 0.16 * quality);
}

// Small opportunity-cost signal for passing while rich and under pressure,
// but only when a genuinely useful shop purchase or upgrade is available.
// The caller must establish that opportunity; an empty/weak shop is not a
// reason to force spending.
inline double reroll_quality_reward(double old_best_fit, double new_best_fit) noexcept {
    // Reward only a real increase in the best available offer; rerolling itself
    // is not progress and repeatedly rerolling a weak shop cannot farm reward.
    return 0.16 * std::tanh((new_best_fit - old_best_fit) / 5.0);
}

inline double pass_opportunity_penalty(
    int gold,
    double hp,
    int stage,
    bool useful_purchase_available
) noexcept {
    if (!useful_purchase_available || gold < 20) return 0.0;
    const double liquidity = gold >= 50 ? 1.0
        : (gold >= 40 ? 0.75 : (gold >= 30 ? 0.50 : 0.25));
    const double health_urgency = std::clamp((50.0 - hp) / 50.0, 0.0, 1.0);
    const double stage_urgency = std::clamp((static_cast<double>(stage) - 2.0) / 4.0,
                                            0.0, 1.0);
    // A rich player should not pass indefinitely in early rounds when a useful
    // unit is available; preserve saving only when there is no good opportunity.
    const double baseline_urgency = gold >= 50 ? 0.25 : 0.0;
    const double urgency = std::max({health_urgency, stage_urgency, baseline_urgency});
    return -0.20 * liquidity * urgency;
}

// A low-fit purchase sold almost immediately is usually a wasted buy.
// Fit is normalized to [0, 1]; legitimate exceptions are explicit so a real
// upgrade, deployment, comp transition, or full bench is not punished.
inline constexpr double kRecentPurchaseLowFitThreshold = 0.20;
// Keep purchase provenance long enough to associate a sale after intervening
// shop/position actions, without carrying stale intent across a whole round.
inline constexpr std::uint64_t kRecentPurchaseHistoryActions = 8;

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
    // A move that changes the slot but does not improve any strategic metric
    // should be less attractive than buying/deploying a useful unit. The larger
    // baseline specifically discourages the repeated empty-slot shuffling seen
    // in Viewer logs, while degradations add further cost.
    return -0.10
        - 0.14 * std::tanh(std::max(0.0, -composition_delta) / 5.0)
        - 0.14 * std::tanh(std::max(0.0, -synergy_delta))
        - 0.08 * std::tanh(std::max(0.0, -positioning_delta));
}


// Normalized immediate combat value for the numeric effects currently consumed
// by CombatEngine. Stats that the simulator does not yet model (for example,
// ability-specific passives) are intentionally excluded rather than guessed.
inline double item_immediate_strength(
    double attack_damage,
    double attack_speed,
    double max_health,
    double armor,
    double critical_strike_chance,
    double critical_strike_damage,
    double omnivamp,
    double damage_amplification,
    double damage_reduction,
    double ability_power = 0.0,
    double magic_resist = 0.0,
    double mana = 0.0
) noexcept {
    const double raw =
        std::max(0.0, attack_damage) / 100.0 +
        std::max(0.0, attack_speed) / 0.5 +
        std::max(0.0, ability_power) / 100.0 +
        std::max(0.0, max_health) / 1000.0 +
        std::max(0.0, armor) / 100.0 +
        std::max(0.0, magic_resist) / 100.0 +
        std::max(0.0, mana) / 100.0 +
        std::max(0.0, critical_strike_chance) / 0.5 +
        std::max(0.0, critical_strike_damage) +
        std::max(0.0, omnivamp) / 0.5 +
        std::max(0.0, damage_amplification) / 0.5 +
        std::max(0.0, damage_reduction) / 0.5;
    return std::clamp(1.0 - std::exp(-raw), 0.0, 1.0);
}

// Potential-like reward for item assignment. Composition fit and catalog role
// weights preserve long-term build value early; the balance shifts toward
// measured immediate combat stats as the match approaches its end. This is
// shaping only: it does not force a target or prescribe a particular item.
inline double item_assignment_quality(
    double immediate_strength,
    double composition_fit,
    double role_alignment,
    int stage
) noexcept {
    const double immediate = std::clamp(immediate_strength, 0.0, 1.0);
    const double fit = std::clamp(composition_fit, 0.0, 1.0);
    const double role = std::clamp(role_alignment, 0.0, 1.0);
    const double progress = std::clamp((static_cast<double>(stage) - 1.0) / 6.0, 0.0, 1.0);
    const double composition_weight = 0.70 - 0.55 * progress;
    const double immediate_weight = 1.0 - composition_weight;
    const double long_term_value = 0.70 * fit + 0.30 * role;
    return std::clamp(
        0.28 * (immediate_weight * immediate +
                composition_weight * long_term_value - 0.15),
        -0.03, 0.20);
}

// Crafting consumes two components and produces a completed item. Add only a
// small bonus when the resulting item has positive value for its recipient;
// the policy must still learn which item/target is best.
inline double item_crafting_bonus(double assignment_quality) noexcept {
    return assignment_quality > 0.0
        ? std::min(0.08, assignment_quality * 0.40)
        : 0.0;
}

inline double clamp_total(double total) noexcept {
    return std::clamp(total, -5.0, 5.0);
}

} // namespace tft::reward_model
