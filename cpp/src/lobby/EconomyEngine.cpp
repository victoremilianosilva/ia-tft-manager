
#include "lobby/EconomyEngine.hpp"

#include <algorithm>

namespace tft {
namespace {

// Equivalente a GameConfig.XP_TO_NEXT.
constexpr std::int32_t xp_to_next_by_level(
    std::int32_t level
) noexcept {
    switch (level) {
        case 2: return 2;
        case 3: return 6;
        case 4: return 10;
        case 5: return 20;
        case 6: return 36;
        case 7: return 56;
        case 8: return 68;
        case 9: return 68;
        default: return 0;
    }
}

} // namespace

void EconomyEngine::reset(PlayerEconomy& economy) const noexcept {
    economy = PlayerEconomy{};
    economy.gold = STARTING_GOLD;
    economy.level = STARTING_LEVEL;
    economy.xp = STARTING_XP;
}

bool EconomyEngine::can_spend(
    const PlayerEconomy& economy,
    std::int32_t amount
) const noexcept {
    return amount >= 0 && economy.gold >= amount;
}

bool EconomyEngine::spend_gold(
    PlayerEconomy& economy,
    std::int32_t amount
) const noexcept {
    if (!can_spend(economy, amount)) {
        return false;
    }

    economy.gold -= amount;
    return true;
}

std::int32_t EconomyEngine::add_gold(
    PlayerEconomy& economy,
    std::int32_t amount
) const noexcept {
    amount = std::max<std::int32_t>(0, amount);
    economy.gold += amount;
    return amount;
}

std::int32_t EconomyEngine::get_interest(
    std::int32_t gold
) const noexcept {
    gold = std::max<std::int32_t>(0, gold);
    return std::min(gold / 10, MAX_INTEREST);
}

std::int32_t EconomyEngine::get_streak(
    const PlayerEconomy& economy
) const noexcept {
    if (economy.win_streak > 0) {
        return economy.win_streak;
    }

    if (economy.loss_streak > 0) {
        return -economy.loss_streak;
    }

    return 0;
}

std::int32_t EconomyEngine::get_streak_gold(
    const PlayerEconomy& economy
) const noexcept {
    const auto streak = std::abs(get_streak(economy));

    if (streak < 2) return 0;
    if (streak <= 4) return 1;
    if (streak == 5) return 2;
    return 3;
}

std::int32_t EconomyEngine::get_xp_to_next(
    const PlayerEconomy& economy
) const noexcept {
    if (economy.level >= MAX_LEVEL) {
        return 0;
    }

    return xp_required_for_level(economy.level);
}

std::int32_t EconomyEngine::xp_required_for_level(
    std::int32_t level
) noexcept {
    return xp_to_next_by_level(level);
}

void EconomyEngine::check_level_up(
    PlayerEconomy& economy
) noexcept {
    while (economy.level < MAX_LEVEL) {
        const auto required = xp_required_for_level(economy.level);

        if (required <= 0 || economy.xp < required) {
            break;
        }

        economy.xp -= required;
        ++economy.level;
    }
}

bool EconomyEngine::can_buy_xp(
    const PlayerEconomy& economy
) const noexcept {
    return economy.level < MAX_LEVEL
        && can_spend(economy, BUY_XP_COST);
}

BuyXpResult EconomyEngine::buy_xp(
    PlayerEconomy& economy
) const {
    const auto old_level = economy.level;

    if (!can_buy_xp(economy) || !spend_gold(economy, BUY_XP_COST)) {
        return {
            false, 0, false, old_level, economy.level
        };
    }

    economy.xp += XP_PER_BUY;
    check_level_up(economy);

    return {
        true,
        XP_PER_BUY,
        economy.level > old_level,
        old_level,
        economy.level
    };
}

bool EconomyEngine::add_round_xp(
    PlayerEconomy& economy
) const {
    if (economy.level >= MAX_LEVEL) {
        return false;
    }

    const auto old_level = economy.level;
    economy.xp += XP_PER_ROUND;
    check_level_up(economy);

    return economy.level > old_level;
}

void EconomyEngine::register_win(
    PlayerEconomy& economy
) const noexcept {
    ++economy.win_streak;
    economy.loss_streak = 0;
}

void EconomyEngine::register_loss(
    PlayerEconomy& economy
) const noexcept {
    ++economy.loss_streak;
    economy.win_streak = 0;
}

void EconomyEngine::reset_streak(
    PlayerEconomy& economy
) const noexcept {
    economy.win_streak = 0;
    economy.loss_streak = 0;
}

void EconomyEngine::register_pvp_win(
    PlayerEconomy& economy
) const noexcept {
    register_win(economy);
    add_gold(economy, WIN_GOLD);
    economy.round_win_gold += WIN_GOLD;
}

std::int32_t EconomyEngine::get_round_gold(
    std::int32_t round_number
) noexcept {
    switch (round_number) {
        case 1: return 0;
        case 2: return 2;
        case 3: return 2;
        case 4: return 3;
        case 5: return 4;
        default: return 5;
    }
}

RoundEconomyResult EconomyEngine::resolve_round(
    PlayerEconomy& economy,
    std::int32_t round_number
) const {
    const auto old_gold = economy.gold;
    const auto old_level = economy.level;

    // A ordem importa: os juros usam o ouro antes da renda. Persistimos o
    // saldo para auditoria; o viewer não reimplementa a fórmula econômica.
    const auto gold_before_interest = economy.gold;
    const auto interest = get_interest(gold_before_interest);
    economy.gold_before_interest = gold_before_interest;
    const auto base_gold = get_round_gold(round_number);
    const auto streak_gold = get_streak_gold(economy);

    add_gold(economy, base_gold);
    add_gold(economy, interest);
    add_gold(economy, streak_gold);

    const bool leveled_up = add_round_xp(economy);

    economy.round_base_gold = base_gold;
    economy.round_interest = interest;
    economy.round_streak_gold = streak_gold;
    economy.round_gold = economy.gold - old_gold;

    RoundEconomyResult result{
        round_number,
        old_gold,
        gold_before_interest,
        gold_before_interest,
        economy.gold,
        base_gold,
        base_gold,
        interest,
        streak_gold,
        economy.round_win_gold,
        base_gold + interest + streak_gold + economy.round_win_gold,
        old_level,
        economy.level,
        leveled_up,
        economy.xp,
        get_xp_to_next(economy)
    };

    // Preserva o bônus de vitória resolvido para auditoria/logs antes de
    // zerar o acumulador que será usado na próxima rodada.
    economy.last_round_win_gold = economy.round_win_gold;
    economy.round_win_gold = 0;

    return result;
}

std::int32_t EconomyEngine::get_sell_value(
    std::int32_t cost,
    std::int32_t star
) noexcept {
    cost = std::max<std::int32_t>(1, cost);

    if (star >= 3) {
        const auto value = cost * 9;
        return std::max<std::int32_t>(
            1, cost == 1 ? value : value - 1
        );
    }
    if (star >= 2) {
        const auto value = cost * 3;
        return std::max<std::int32_t>(
            1, cost == 1 ? value : value - 1
        );
    }
    return cost;
}

} // namespace tft
