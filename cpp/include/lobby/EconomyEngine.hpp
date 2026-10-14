
#pragma once

#include <cstdint>

namespace tft {

// Estado econômico de um jogador.
// Mantém os dados mutáveis separados da configuração estática.
struct PlayerEconomy {
    std::int32_t gold = 0;
    std::int32_t level = 2;
    std::int32_t xp = 0;

    std::int32_t win_streak = 0;
    std::int32_t loss_streak = 0;

    std::int32_t round_gold = 0;
    std::int32_t round_interest = 0;
    std::int32_t round_streak_gold = 0;
    std::int32_t round_base_gold = 0;
    std::int32_t round_win_gold = 0;
};

struct BuyXpResult {
    bool success = false;
    std::int32_t xp_gained = 0;
    bool leveled_up = false;
    std::int32_t old_level = 0;
    std::int32_t new_level = 0;
};

struct RoundEconomyResult {
    std::int32_t round = 0;
    std::int32_t old_gold = 0;
    std::int32_t new_gold = 0;

    std::int32_t base_gold = 0;
    std::int32_t passive_gold = 0;
    std::int32_t interest_gold = 0;
    std::int32_t streak_gold = 0;
    std::int32_t win_gold = 0;
    std::int32_t total_gold = 0;

    std::int32_t old_level = 0;
    std::int32_t new_level = 0;
    bool leveled_up = false;

    std::int32_t xp = 0;
    std::int32_t xp_to_next = 0;
};

class EconomyEngine {
public:
    static constexpr std::int32_t STARTING_GOLD = 0;
    static constexpr std::int32_t STARTING_LEVEL = 2;
    static constexpr std::int32_t STARTING_XP = 0;

    static constexpr std::int32_t REROLL_COST = 2;
    static constexpr std::int32_t BUY_XP_COST = 4;
    static constexpr std::int32_t XP_PER_BUY = 4;
    static constexpr std::int32_t XP_PER_ROUND = 2;

    static constexpr std::int32_t MAX_LEVEL = 10;
    static constexpr std::int32_t MAX_INTEREST = 5;
    static constexpr std::int32_t WIN_GOLD = 1;

    void reset(PlayerEconomy& economy) const noexcept;

    [[nodiscard]] bool can_spend(
        const PlayerEconomy& economy,
        std::int32_t amount
    ) const noexcept;

    bool spend_gold(
        PlayerEconomy& economy,
        std::int32_t amount
    ) const noexcept;

    std::int32_t add_gold(
        PlayerEconomy& economy,
        std::int32_t amount
    ) const noexcept;

    [[nodiscard]] std::int32_t get_interest(
        std::int32_t gold
    ) const noexcept;

    [[nodiscard]] std::int32_t get_streak(
        const PlayerEconomy& economy
    ) const noexcept;

    [[nodiscard]] std::int32_t get_streak_gold(
        const PlayerEconomy& economy
    ) const noexcept;

    [[nodiscard]] std::int32_t get_xp_to_next(
        const PlayerEconomy& economy
    ) const noexcept;

    [[nodiscard]] bool can_buy_xp(
        const PlayerEconomy& economy
    ) const noexcept;

    BuyXpResult buy_xp(PlayerEconomy& economy) const;

    bool add_round_xp(PlayerEconomy& economy) const;

    void register_win(PlayerEconomy& economy) const noexcept;
    void register_loss(PlayerEconomy& economy) const noexcept;
    void reset_streak(PlayerEconomy& economy) const noexcept;

    void register_pvp_win(PlayerEconomy& economy) const noexcept;

    [[nodiscard]] RoundEconomyResult resolve_round(
        PlayerEconomy& economy,
        std::int32_t round_number
    ) const;

    [[nodiscard]] static std::int32_t get_sell_value(
        std::int32_t cost,
        std::int32_t star
    ) noexcept;

private:
    static std::int32_t get_round_gold(
        std::int32_t round_number
    ) noexcept;

    static std::int32_t xp_required_for_level(
        std::int32_t level
    ) noexcept;

    static void check_level_up(PlayerEconomy& economy) noexcept;
};

} // namespace tft
