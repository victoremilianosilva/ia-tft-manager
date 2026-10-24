#pragma once

#include <array>
#include <cstddef>
#include <cstdint>

namespace tft::items {
enum class ItemActionType : std::uint8_t { WAIT = 0, CRAFT = 1, EQUIP = 2, TRANSFER = 3, UNEQUIP = 4 };
enum class UnitLocation : std::uint8_t { BENCH = 0, BOARD = 1 };

// Fixed PPO schema bounds. State-derived masks and native execution must still
// reject empty slots; these dimensions do not imply that a slot is occupied.
inline constexpr std::size_t kItemActionTypeCount = 5;
inline constexpr std::size_t kItemComponentSlots = 18;
inline constexpr std::size_t kItemInventorySlots = 18;
inline constexpr std::size_t kItemUnitSlots = 37; // bench 0..8, board 9..36
inline constexpr std::size_t kItemsPerUnit = 3;
inline constexpr std::array<std::size_t, 7> kItemActionDims{5, 18, 18, 18, 37, 37, 3};

struct ItemAction {
    // type, component A, component B, inventory item, source unit, target unit, equipped item slot
    std::array<std::int32_t, 7> values{0, 0, 0, 0, 0, 0, 0};

    [[nodiscard]] bool has_valid_indices() const noexcept {
        for (std::size_t i = 0; i < values.size(); ++i)
            if (values[i] < 0 || static_cast<std::size_t>(values[i]) >= kItemActionDims[i])
                return false;
        return values[0] != static_cast<std::int32_t>(ItemActionType::TRANSFER) ||
               values[4] != values[5];
    }
};

struct ItemActionMasks {
    std::array<std::uint8_t, 5> type{};
    std::array<std::uint8_t, 18> first_component{};
    std::array<std::uint8_t, 18> second_component{};
    std::array<std::uint8_t, 18> inventory_item{};
    std::array<std::uint8_t, 37> source_unit{};
    std::array<std::uint8_t, 37> target_unit{};
    std::array<std::uint8_t, 3> equipped_item{};

    void set_wait_only() noexcept {
        *this = ItemActionMasks{};
        type[static_cast<std::size_t>(ItemActionType::WAIT)] = 1;
        first_component[0] = second_component[0] = inventory_item[0] = 1;
        source_unit[0] = target_unit[0] = equipped_item[0] = 1;
    }
    [[nodiscard]] bool has_any_legal_type() const noexcept {
        for (auto enabled : type) if (enabled != 0) return true;
        return false;
    }
};
static_assert(kItemActionDims.size() == 7);
} // namespace tft::items
