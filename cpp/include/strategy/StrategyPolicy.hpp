#pragma once

#include <algorithm>
#include <array>
#include <cstdint>

namespace tft::strategy {

enum class EconomicStrategy : std::int32_t {
    Econ = 0,
    Stabilize = 1,
    Fast8 = 2,
    Slowroll = 3,
    AllIn = 4,
    WinStreak = 5,
    LossStreak = 6
};

struct EconomicStrategyContext {
    int gold{0};
    double hp{100.0};
    int level{1};
    int win_streak{0};
    int loss_streak{0};
    double board_power{0.0};
    bool composition_requests_fast8{false};
    bool composition_requests_three_star{false};
};

struct EconomicStrategyDecision {
    EconomicStrategy selected{EconomicStrategy::Econ};
    std::array<double, 7> scores{};
    double confidence{0.5};
    const char* reason{"Economia neutra"};
};

inline EconomicStrategyDecision select_economic_strategy(
    const EconomicStrategyContext& s) noexcept {
    constexpr double kIneligible = -1000.0;
    EconomicStrategyDecision out;
    out.scores.fill(kIneligible);

    // Emergency spending overrides greed and long-term plans.
    if (s.hp <= 15.0) {
        out.scores[4] = 100.0 + (15.0 - s.hp);
        out.reason = "HP crítico: gastar para sobreviver";
    }

    if (s.hp <= 38.0 || (s.board_power < 25.0 && s.hp < 65.0)) {
        out.scores[1] = 65.0 + std::max(0.0, 38.0 - s.hp) * 0.25
            + std::max(0.0, 25.0 - s.board_power) * 0.15;
        if (s.hp <= 15.0) out.scores[1] = kIneligible;
        out.reason = s.hp <= 38.0
            ? "STABILIZE: pressão de vida"
            : "STABILIZE: tabuleiro fraco sob pressão";
    }

    const bool has_comp_goal =
        s.composition_requests_fast8 || s.composition_requests_three_star;

    if (!has_comp_goal && s.win_streak >= 3 && s.hp >= 55.0 &&
        s.board_power >= 35.0) {
        out.scores[5] = 55.0 + std::min(s.win_streak, 6) * 1.5;
        out.reason = "WINSTREAK: preservar vantagem atual";
    }

    // Slowroll is a comp-driven plan, never a generic fallback just because
    // the player has gold and is at a low level.
    if (s.composition_requests_three_star && s.level >= 5 &&
        s.level <= 6 && s.gold >= 30 && s.hp > 25.0) {
        out.scores[3] = 76.0 + std::min(s.gold, 50) * 0.04;
        out.reason = "SLOWROLL: composição tem alvo de 3 estrelas";
    }

    // Fast 8 is only enabled when the active composition plan calls for at
    // least eight units; gold alone must never select this strategy.
    if (s.composition_requests_fast8 && s.level >= 6 && s.level < 8 &&
        s.gold >= 30 && s.hp > 25.0 && s.board_power >= 25.0) {
        out.scores[2] = 74.0 + std::min(s.gold, 50) * 0.04
            + (s.level >= 7 ? 2.0 : 0.0);
        out.reason = "FAST8: composição planejada exige nível 8";
    }

    // A deliberate loss streak is only an option while healthy enough to
    // survive it and when no composition-directed spend has priority.
    if (!has_comp_goal && s.loss_streak >= 3 && s.hp >= 50.0 &&
        s.gold < 50 && s.board_power < 40.0) {
        out.scores[6] = 49.0 + std::min(s.loss_streak, 6) * 1.2;
        out.reason = "LOSS_STREAK: converter derrota em economia sem risco crítico";
    }

    // ECON means protecting the interest threshold, not hoarding forever.
    // At/above 50 gold it remains eligible as a reserve policy, but reward
    // shaping must permit useful spending from the surplus.
    if (s.hp >= 40.0 && s.board_power >= 25.0 &&
        !s.composition_requests_fast8 &&
        !s.composition_requests_three_star &&
        s.hp > 15.0) {
        out.scores[0] = 35.0 + std::min(s.gold, 50) * 0.20;
        out.reason = s.gold < 50
            ? "ECON: acumular até o limite de juros de 50"
            : "ECON: manter reserva de 50 e gastar excedente útil";
    }

    // If no other mode is eligible, stabilize rather than silently selecting
    // ECON while the board is in trouble.
    if (out.scores[1] == kIneligible && out.scores[2] == kIneligible &&
        out.scores[3] == kIneligible && out.scores[4] == kIneligible &&
        out.scores[5] == kIneligible && out.scores[6] == kIneligible &&
        out.scores[0] == kIneligible) {
        out.scores[1] = 30.0;
        out.reason = "STABILIZE: modo de segurança";
    }

    int best = 0;
    for (int i = 1; i < 7; ++i)
        if (out.scores[static_cast<std::size_t>(i)] >
            out.scores[static_cast<std::size_t>(best)]) best = i;

    out.selected = static_cast<EconomicStrategy>(best);
    double second = kIneligible;
    for (int i = 0; i < 7; ++i)
        if (i != best) second = std::max(second, out.scores[static_cast<std::size_t>(i)]);
    out.confidence = std::clamp(
        0.5 + (out.scores[static_cast<std::size_t>(best)] - second) / 100.0,
        0.5, 0.99);
    return out;
}

} // namespace tft::strategy
