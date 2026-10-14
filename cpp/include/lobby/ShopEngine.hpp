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

    // Exposto para validação de equivalência com GameConfig.SHOP_ODDS.
    [[nodiscard]] static const std::array<std::array<double, 5>, 10>& odds_by_level();

private:
    UnitPool& pool_;
    UnitInstanceFactory& factory_;
    std::mt19937_64 rng_;
    std::array<std::optional<UnitInstance>, kShopSlots> offers_{};
    bool locked_{false};
    std::int32_t roll_cost(std::int32_t level);
    std::optional<UnitInstance> draw(std::int32_t cost);
};
} // namespace tft
