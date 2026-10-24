#pragma once

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

// Canonical per-player item state contract.
// Components and completed items are ordered inventories; repeated IDs are
// distinct copies. Equipment is keyed by unit UUID so duplicate champions do
// not share equipment accidentally. CombatUnit::items is a projection of this
// equipment state at combat-input construction time, not a second authority.
struct ItemPlayerState {
    std::vector<std::string> components;
    std::vector<std::string> inventory;
    std::unordered_map<std::string, std::vector<std::string>> equipped_by_unit_uuid;
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
