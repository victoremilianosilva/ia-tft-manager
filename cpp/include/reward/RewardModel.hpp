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

inline double clamp_total(double total) noexcept {
    return std::clamp(total, -5.0, 5.0);
}

} // namespace tft::reward_model
