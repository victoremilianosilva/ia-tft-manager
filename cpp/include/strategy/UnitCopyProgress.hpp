#pragma once

#include <algorithm>
#include <array>
#include <cstdint>

namespace tft::strategy {

// Physical owned instances by star tier. Index zero is unused. Shop offers
// remain separate and are included only when the caller proves affordability.
inline std::int32_t owned_star_equivalent_copies(
    const std::array<std::int32_t, 4>& owned_by_star) noexcept {
    return std::max(0, owned_by_star[1]) +
        3 * std::max(0, owned_by_star[2]) +
        9 * std::max(0, owned_by_star[3]);
}

inline std::int32_t copies_toward_next_star(
    const std::array<std::int32_t, 4>& owned_by_star,
    std::int32_t highest_star,
    std::int32_t affordable_shop_one_star_copies = 0) noexcept {
    if (highest_star < 1 || highest_star >= 3) return 0;
    const auto one_star = std::max(0, owned_by_star[1]) +
        std::max(0, affordable_shop_one_star_copies);
    if (highest_star == 1)
        return std::clamp(one_star - 1, 0, 2);
    const auto available_two_star = std::max(0, owned_by_star[2]) + one_star / 3;
    return std::clamp(available_two_star - 1, 0, 2);
}

inline std::int32_t additional_one_star_copies_to_two_star(
    const std::array<std::int32_t, 4>& owned_by_star,
    std::int32_t highest_star,
    std::int32_t shop_one_star_copies = 0) noexcept {
    if (highest_star >= 2 || highest_star < 1) return 0;
    const auto available = std::max(0, owned_by_star[1]) +
        std::max(0, shop_one_star_copies);
    return std::max(0, 3 - available);
}

} // namespace tft::strategy
