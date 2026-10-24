#pragma once

#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>

namespace tft::items {

// Semantic operations supported by the item subsystem. This is deliberately
// independent from the PPO's positional action vector: the policy adapter will
// map sampled indices to stable catalog IDs and unit UUIDs.
enum class ItemOperation {
    WAIT,
    EQUIP_FROM_INVENTORY,
    CRAFT_AND_EQUIP,
    TRANSFER,
    UNEQUIP_TO_INVENTORY
};

// Counters are owned by the per-player item state and are exposed for
// audit/metrics; they are not, by themselves, reward signals.
struct ItemPlayerMetrics {
    std::uint64_t components_collected{0};
    std::uint64_t crafts{0};
    std::uint64_t equips{0};
    std::uint64_t unequips{0};
    std::uint64_t transfers{0};
    std::uint64_t invalid_actions{0};
    std::uint64_t items_left_unused{0};
};

// Canonical per-player item state contract.
// Components and completed items are ordered inventories; repeated IDs are
// distinct copies. Equipment is keyed by unit UUID so duplicate champions do
// not share equipment accidentally. CombatUnit::items is a projection of this
// equipment state at combat-input construction time, not a second authority.
struct ItemPlayerState {
    std::vector<std::string> components;
    std::vector<std::string> inventory;
    std::unordered_map<std::string, std::vector<std::string>> equipped_by_unit_uuid;
    ItemPlayerMetrics metrics;
};

// Typed command used between policy-action decoding and item execution.
// Fields are operation-specific; IDs are catalog IDs, not display names or
// transient inventory positions. A decoder must resolve sampled indices against
// the exact observation used to sample the action.
struct ItemActionCommand {
    ItemOperation operation{ItemOperation::WAIT};
    std::string item_id;
    std::string source_unit_uuid;
    std::string target_unit_uuid;
    std::string first_component_id;
    std::string second_component_id;
};

// Explicit validation result for action-mask/execution parity tests.
struct ItemActionValidation {
    bool legal{false};
    std::string reason;
};

} // namespace tft::items
