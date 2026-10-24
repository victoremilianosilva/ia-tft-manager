#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <iterator>
#include <optional>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include "items/ItemActionContract.hpp"

namespace tft::items {

// Data-driven: recipes and stats come from the active set's catalog. The engine
// deliberately does not hard-code a TFT set whose recipes can change.
struct ItemDefinition {
    std::string id;
    std::string name;
    std::array<std::string, 2> recipe_components{};
    double attack_damage{0.0};
    double attack_speed{0.0};
    double ability_power{0.0};
    double critical_strike_chance{0.0};
    double critical_strike_damage{0.0};
    double max_health{0.0};
    double armor{0.0};
    double magic_resist{0.0};
    double mana{0.0};
    double omnivamp{0.0};
    double damage_amplification{0.0};
    double damage_reduction{0.0};
    double carry_weight{0.0};
    double tank_weight{0.0};
    double support_weight{0.0};
    double utility_weight{0.0};
};

struct UnitProfile {
    std::string uuid;
    int star{1};
    int role{3}; // 0 tank, 1 carry, 2 support, 3 fighter, 4 assassin
    bool frontline{false};
    bool backline{false};
    double attack_damage{0.0};
    double attack_speed{0.0};
    double ability_power{0.0};
    double max_health{0.0};
    double armor{0.0};
    double magic_resist{0.0};
    double composition_fit{0.0}; // normalized [0,1]
};

struct ItemActionResult {
    bool success{false};
    std::string reason;
};

struct ItemMetrics {
    std::uint64_t components_collected{0};
    std::uint64_t crafts{0};
    std::uint64_t equips{0};
    std::uint64_t invalid_actions{0};
    std::uint64_t items_left_unused{0};
};

class ItemEngine {
public:
    static constexpr std::size_t kMaxItemsPerUnit = 3;

    explicit ItemEngine(std::vector<ItemDefinition> catalog,
                        std::vector<std::string> component_ids = {})
        : catalog_(std::move(catalog)) {
        for (const auto& component_id : component_ids) {
            if (component_id.empty() || !component_ids_.insert(component_id).second) {
                throw std::invalid_argument("Item catalog has an empty or duplicate component id");
            }
        }
        for (std::size_t i = 0; i < catalog_.size(); ++i) {
            const auto& item = catalog_[i];
            if (item.id.empty() || index_.contains(item.id)) {
                throw std::invalid_argument("Item catalog has an empty or duplicate id");
            }
            index_.emplace(item.id, i);
            const auto& a = item.recipe_components[0];
            const auto& b = item.recipe_components[1];
            if (!a.empty() && !b.empty()) {
                component_ids_.insert(a);
                component_ids_.insert(b);
                const auto key = recipe_key(a, b);
                if (recipes_.contains(key))
                    throw std::invalid_argument("Item catalog has duplicate component recipe");
                recipes_.emplace(key, item.id);
            }
        }
    }

    void reset() {
        components_.clear();
        inventory_.clear();
        equipped_.clear();
        metrics_ = {};
    }

    bool add_component(const std::string& component_id) {
        if (component_id.empty() || !component_ids_.contains(component_id)) {
            ++metrics_.invalid_actions;
            return false;
        }
        components_.push_back(component_id);
        ++metrics_.components_collected;
        return true;
    }

    // Called by game loot/armory events, never by the policy action decoder.
    bool add_completed_item(const std::string& item_id) {
        if (!find(item_id) || !find(item_id)->recipe_components[0].empty()) {
            ++metrics_.invalid_actions;
            return false;
        }
        inventory_.push_back(item_id);
        return true;
    }

    [[nodiscard]] bool can_craft(const std::string& first,
                                const std::string& second) const {
        const auto recipe = craftable_item(first, second);
        if (!recipe) return false;
        const auto count = [this](const std::string& id) {
            return static_cast<std::size_t>(std::count(
                components_.begin(), components_.end(), id));
        };
        if (first == second) return count(first) >= 2U;
        return count(first) >= 1U && count(second) >= 1U;
    }

    [[nodiscard]] bool can_equip(const std::string& item_id,
                                const std::string& unit_uuid) const {
        return !unit_uuid.empty() && has_item(item_id) &&
            equipped(unit_uuid).size() < kMaxItemsPerUnit;
    }

    // Returns the crafted item id; neither component is consumed on failure.
    std::optional<std::string> craft(const std::string& first, const std::string& second) {
        if (first.empty() || second.empty()) {
            ++metrics_.invalid_actions;
            return std::nullopt;
        }
        const auto recipe = recipes_.find(recipe_key(first, second));
        if (recipe == recipes_.end()) {
            ++metrics_.invalid_actions;
            return std::nullopt;
        }
        const auto a = std::find(components_.begin(), components_.end(), first);
        if (a == components_.end()) {
            ++metrics_.invalid_actions;
            return std::nullopt;
        }
        // Find the second component by index; this also handles recipes
        // that legitimately consume two copies of the same component.
        const auto first_index = static_cast<std::size_t>(std::distance(components_.begin(), a));
        std::optional<std::size_t> second_index;
        for (std::size_t i = 0; i < components_.size(); ++i) {
            if (i != first_index && components_[i] == second) {
                second_index = i;
                break;
            }
        }
        if (!second_index) {
            ++metrics_.invalid_actions;
            return std::nullopt;
        }
        const auto high = std::max(first_index, *second_index);
        const auto low = std::min(first_index, *second_index);
        components_.erase(components_.begin() + static_cast<std::ptrdiff_t>(high));
        components_.erase(components_.begin() + static_cast<std::ptrdiff_t>(low));
        inventory_.push_back(recipe->second);
        ++metrics_.crafts;
        return recipe->second;
    }

    bool equip(const std::string& item_id, const UnitProfile& target) {
        const auto target_items = equipped_.find(target.uuid);
        const std::size_t target_count = target_items == equipped_.end()
            ? 0U : target_items->second.size();
        if (!has_item(item_id) || target.uuid.empty() ||
            target_count >= kMaxItemsPerUnit) {
            ++metrics_.invalid_actions;
            return false;
        }
        const auto inventory_item = std::find(inventory_.begin(), inventory_.end(), item_id);
        if (inventory_item == inventory_.end()) {
            ++metrics_.invalid_actions;
            return false;
        }
        inventory_.erase(inventory_item);
        equipped_[target.uuid].push_back(item_id);
        ++metrics_.equips;
        return true;
    }

    [[nodiscard]] const std::vector<std::string>& components() const noexcept {
        return components_;
    }
    [[nodiscard]] const std::vector<std::string>& inventory() const noexcept {
        return inventory_;
    }
    [[nodiscard]] const std::vector<std::string>& equipped(const std::string& uuid) const noexcept {
        static const std::vector<std::string> empty;
        const auto it = equipped_.find(uuid);
        return it == equipped_.end() ? empty : it->second;
    }
    [[nodiscard]] const ItemMetrics& metrics() const noexcept { return metrics_; }
    [[nodiscard]] const ItemDefinition* find(const std::string& id) const noexcept {
        const auto it = index_.find(id);
        return it == index_.end() ? nullptr : &catalog_[it->second];
    }
    [[nodiscard]] std::optional<std::string> craftable_item(
        const std::string& first, const std::string& second) const {
        const auto it = recipes_.find(recipe_key(first, second));
        if (it == recipes_.end()) return std::nullopt;
        return it->second;
    }

    // Estimate only marginal item value. Actual combat remains the source of
    // truth; composition fit and current role are inputs, not fixed labels.
    [[nodiscard]] double item_fit(const std::string& item_id,
                                  const UnitProfile& unit) const noexcept {
        const auto* item = find(item_id);
        if (!item || unit.uuid.empty()) return -1.0;
        const double damage_fit =
            std::max(0.0, item->attack_damage) * std::max(0.0, unit.attack_damage) / 100.0 +
            std::max(0.0, item->attack_speed) * std::max(0.0, unit.attack_speed) +
            std::max(0.0, item->ability_power) * std::max(0.0, unit.ability_power) / 100.0 +
            std::max(0.0, item->critical_strike_chance) *
                std::max(0.0, unit.attack_damage) * 0.5 +
            std::max(0.0, item->critical_strike_damage) *
                std::max(0.0, unit.attack_damage) * 0.25 +
            std::max(0.0, item->damage_amplification) *
                std::max(0.0, unit.attack_damage) / 100.0 +
            std::max(0.0, item->omnivamp) *
                std::max(0.0, unit.attack_damage) / 100.0;
        const double durability_fit =
            std::max(0.0, item->max_health) * std::max(0.0, unit.max_health) / 10000.0 +
            std::max(0.0, item->armor) * std::max(0.0, unit.armor) / 100.0 +
            std::max(0.0, item->magic_resist) * std::max(0.0, unit.magic_resist) / 100.0 +
            std::max(0.0, item->damage_reduction) *
                std::max(0.0, unit.max_health) / 100.0;
        double role_fit = item->utility_weight;
        if (unit.role == 0 || unit.frontline) role_fit += item->tank_weight;
        if (unit.role == 1 || unit.role == 4 || unit.backline) role_fit += item->carry_weight;
        if (unit.role == 2) role_fit += item->support_weight;
        if (unit.role == 3) role_fit += 0.5 * (item->tank_weight + item->carry_weight);
        return damage_fit + durability_fit + role_fit +
            0.25 * std::clamp(unit.composition_fit, 0.0, 1.0);
    }

    // Execute an item action selected by the main policy. There is no
    // item-specific WAIT or parallel heuristic action selector.
    [[nodiscard]] ItemActionResult apply_action(
        const ItemActionCommand& command,
        const std::vector<UnitProfile>& candidates) {
        const auto reject = [this](const char* reason) {
            ++metrics_.invalid_actions;
            return ItemActionResult{false, reason};
        };
        if (!command.operation) return reject("missing_item_operation");

        const auto find_unit = [&candidates](const std::string& uuid)
            -> const UnitProfile* {
            const auto it = std::find_if(candidates.begin(), candidates.end(),
                [&uuid](const UnitProfile& unit) { return unit.uuid == uuid; });
            return it == candidates.end() ? nullptr : &*it;
        };
        const auto* target = find_unit(command.target_unit_uuid);
        if (!target || target->uuid.empty())
            return reject("invalid_item_target");
        if (equipped(target->uuid).size() >= kMaxItemsPerUnit)
            return reject("target_item_capacity_reached");

        if (*command.operation == ItemOperation::EQUIP_FROM_INVENTORY) {
            if (!find(command.item_id) || !has_item(command.item_id))
                return reject("item_not_available_in_inventory");
            if (!equip(command.item_id, *target))
                return reject("equip_transition_failed");
            return {true, {}};
        }

        if (*command.operation == ItemOperation::CRAFT_AND_EQUIP) {
            if (command.first_component_id.empty() ||
                command.second_component_id.empty())
                return reject("missing_recipe_components");
            const auto recipe = craftable_item(
                command.first_component_id, command.second_component_id);
            if (!recipe || !find(*recipe))
                return reject("unknown_item_recipe");

            const auto count_component = [this](const std::string& id) {
                return static_cast<std::size_t>(std::count(
                    components_.begin(), components_.end(), id));
            };
            const bool components_available =
                command.first_component_id == command.second_component_id
                ? count_component(command.first_component_id) >= 2U
                : count_component(command.first_component_id) >= 1U &&
                  count_component(command.second_component_id) >= 1U;
            if (!components_available)
                return reject("recipe_components_unavailable");

            const auto components_before = components_;
            const auto inventory_before = inventory_;
            const auto equipped_before = equipped_;
            const auto metrics_before = metrics_;
            const auto rollback = [this, &components_before, &inventory_before,
                                   &equipped_before, &metrics_before]() {
                components_ = components_before;
                inventory_ = inventory_before;
                equipped_ = equipped_before;
                metrics_ = metrics_before;
            };
            const auto crafted = craft(
                command.first_component_id, command.second_component_id);
            if (!crafted || *crafted != *recipe) {
                rollback();
                return reject("craft_transition_failed");
            }
            if (!equip(*crafted, *target)) {
                rollback();
                return reject("equip_transition_failed_rolled_back");
            }
            return {true, {}};
        }
        return reject("unsupported_item_operation");
    }

private:
    std::vector<ItemDefinition> catalog_;
    std::unordered_map<std::string, std::size_t> index_;
    std::unordered_set<std::string> component_ids_;
    std::unordered_map<std::string, std::string> recipes_;
    std::vector<std::string> components_;
    std::vector<std::string> inventory_;
    std::unordered_map<std::string, std::vector<std::string>> equipped_;
    ItemMetrics metrics_{};

    static std::string recipe_key(const std::string& a, const std::string& b) {
        return a < b ? a + "\x1f" + b : b + "\x1f" + a;
    }
    bool has_item(const std::string& id) const {
        return std::find(inventory_.begin(), inventory_.end(), id) != inventory_.end();
    }
};

} // namespace tft::items
