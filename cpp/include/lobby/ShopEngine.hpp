#pragma once
#include "lobby/TftEngine.hpp"
#include "lobby/UnitInstanceFactory.hpp"
#include "lobby/UnitPool.hpp"
#include <array>
#include <cstdint>
#include <optional>
#include <random>
namespace tft {
class ShopEngine {
public:
    explicit ShopEngine(UnitPool& pool, UnitInstanceFactory& factory, std::uint64_t seed = 0);
    void roll(std::int32_t level, bool force = false);
    void reroll(std::int32_t level);
    bool set_locked(bool locked) noexcept;
    bool toggle_lock() noexcept;
    bool is_locked() const noexcept;
    const std::array<std::optional<UnitInstance>, kShopSlots>& offers() const noexcept;
    const UnitInstance* get_unit(std::int32_t slot) const noexcept;
    std::optional<UnitInstance> take_unit(std::int32_t slot) noexcept;
    void return_current_shop();
    void reset();
    bool set_offer_for_testing(std::int32_t slot, UnitInstance unit);
    bool set_next_roll_for_testing(const std::vector<std::int32_t>& champion_internal_ids);

    // Fonte única das probabilidades por nível, compartilhada pelo shop e
    // pelo CompositionPlanner. Inline para também ser utilizável por testes
    // unitários que não linkam a implementação completa da loja.
    [[nodiscard]] static const std::array<std::array<double, 5>, 10>& odds_by_level() {
        static const std::array<std::array<double, 5>, 10> odds{{
            {{1.00,0.00,0.00,0.00,0.00}}, {{1.00,0.00,0.00,0.00,0.00}},
            {{0.75,0.25,0.00,0.00,0.00}}, {{0.55,0.30,0.15,0.00,0.00}},
            {{0.45,0.33,0.20,0.02,0.00}}, {{0.30,0.40,0.25,0.05,0.00}},
            {{0.16,0.30,0.43,0.10,0.01}}, {{0.15,0.20,0.32,0.30,0.03}},
            {{0.10,0.17,0.25,0.33,0.15}}, {{0.05,0.10,0.20,0.40,0.25}}
        }};
        return odds;
    }

private:
    UnitPool& pool_;
    UnitInstanceFactory& factory_;
    std::mt19937_64 rng_;
    std::array<std::optional<UnitInstance>, kShopSlots> offers_{};
    bool locked_{false};
    std::optional<std::vector<std::int32_t>> next_roll_for_testing_;
    std::int32_t roll_cost(std::int32_t level);
    std::optional<UnitInstance> draw(std::int32_t cost);
};
} // namespace tft
