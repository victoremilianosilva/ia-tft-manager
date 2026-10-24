#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <optional>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

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
    double max_health{0.0};
    double armor{0.0};
    double magic_resist{0.0};
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

enum class DecisionKind : std::uint8_t {
    WAIT,
    EQUIP_FROM_INVENTORY,
    CRAFT_AND_EQUIP,
    TRANSFER
};

struct ItemDecision {
    DecisionKind kind{DecisionKind::WAIT};
    std::string item_id;
    std::string source_unit_uuid;
    std::string target_unit_uuid;
    double immediate_value{0.0};
    double future_value{0.0};
    double urgency{0.0};
    double total_value{0.0};
};

struct ItemMetrics {
    std::uint64_t components_collected{0};
    std::uint64_t crafts{0};
    std::uint64_t equips{0};
    std::uint64_t unequips{0};
    std::uint64_t transfers{0};
    std::uint64_t invalid_actions{0};
    std::uint64_t items_left_unused{0};
};

class ItemEngine {
public:
    static constexpr std::size_t kMaxItemsPerUnit = 3;

    explicit ItemEngine(std::vector<ItemDefinition> catalog)
        : catalog_(std::move(catalog)) {
        for (std::size_t i = 0; i < catalog_.size(); ++i) {
            const auto& item = catalog_[i];
            if (item.id.empty() || index_.contains(item.id)) {
                throw std::invalid_argument("Item catalog has an empty or duplicate id");
            }
            index_.emplace(item.id, i);
            const auto& a = item.recipe_components[0];
            const auto& b = item.recipe_components[1];
            if (!a.empty() && !b.empty()) {
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
        if (component_id.empty()) {
            ++metrics_.invalid_actions;
            return false;
        }
        components_.push_back(component_id);
        ++metrics_.components_collected;
        return true;
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
        if (!has_item(item_id) || target.uuid.empty() ||
            equipped_[target.uuid].size() >= kMaxItemsPerUnit) {
            ++metrics_.invalid_actions;
            return false;
        }
        inventory_.erase(std::find(inventory_.begin(), inventory_.end(), item_id));
        equipped_[target.uuid].push_back(item_id);
        ++metrics_.equips;
        return true;
    }

    bool unequip(const std::string& item_id, const std::string& unit_uuid) {
        const auto unit = equipped_.find(unit_uuid);
        if (unit == equipped_.end()) {
            ++metrics_.invalid_actions;
            return false;
        }
        const auto item = std::find(unit->second.begin(), unit->second.end(), item_id);
        if (item == unit->second.end()) {
            ++metrics_.invalid_actions;
            return false;
        }
        unit->second.erase(item);
        inventory_.push_back(item_id);
        ++metrics_.unequips;
        return true;
    }

    bool transfer(const std::string& item_id, const std::string& from_uuid,
                  const UnitProfile& target) {
        if (from_uuid.empty() || target.uuid.empty() || from_uuid == target.uuid) {
            ++metrics_.invalid_actions;
            return false;
        }
        const auto source = equipped_.find(from_uuid);
        if (source == equipped_.end()) {
            ++metrics_.invalid_actions;
            return false;
        }
        const auto item = std::find(source->second.begin(), source->second.end(), item_id);
        if (item == source->second.end() || equipped_[target.uuid].size() >= kMaxItemsPerUnit) {
            ++metrics_.invalid_actions;
            return false;
        }
        source->second.erase(item);
        equipped_[target.uuid].push_back(item_id);
        ++metrics_.transfers;
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
            std::max(0.0, item->ability_power) * std::max(0.0, unit.ability_power) / 100.0;
        const double durability_fit =
            std::max(0.0, item->max_health) * std::max(0.0, unit.max_health) / 10000.0 +
            std::max(0.0, item->armor) * std::max(0.0, unit.armor) / 100.0 +
            std::max(0.0, item->magic_resist) * std::max(0.0, unit.magic_resist) / 100.0;
        double role_fit = item->utility_weight;
        if (unit.role == 0 || unit.frontline) role_fit += item->tank_weight;
        if (unit.role == 1 || unit.role == 4 || unit.backline) role_fit += item->carry_weight;
        if (unit.role == 2) role_fit += item->support_weight;
        if (unit.role == 3) role_fit += 0.5 * (item->tank_weight + item->carry_weight);
        return damage_fit + durability_fit + role_fit +
            0.25 * std::clamp(unit.composition_fit, 0.0, 1.0);
    }

    // Keep/wait is a first-class option. Spend a component only when the
    // immediate gain exceeds the estimated future value after urgency weighting.
    [[nodiscard]] ItemDecision decide_craft(
        const std::string& first, const std::string& second,
        const std::vector<UnitProfile>& candidates, int stage, double hp) const {
        ItemDecision best;
        best.kind = DecisionKind::WAIT;
        best.total_value = 0.0;
        const auto item_id = craftable_item(first, second);
        if (!item_id) return best;
        const auto* item = find(*item_id);
        if (!item) return best;
        const double urgency = std::max(
            std::clamp((65.0 - hp) / 65.0, 0.0, 1.0),
            std::clamp((static_cast<double>(stage) - 2.0) / 6.0, 0.0, 1.0));
        for (const auto& candidate : candidates) {
            if (candidate.uuid.empty()) continue;
            const double fit = item_fit(*item_id, candidate);
            const double future = 0.15 + 0.35 * std::clamp(candidate.composition_fit, 0.0, 1.0);
            const double immediate = fit * (0.65 + 0.35 * urgency);
            const double value = immediate + urgency * 0.25 - future * (1.0 - urgency);
            if (value > best.total_value) {
                best.kind = DecisionKind::CRAFT_AND_EQUIP;
                best.item_id = *item_id;
                best.target_unit_uuid = candidate.uuid;
                best.immediate_value = immediate;
                best.future_value = future;
                best.urgency = urgency;
                best.total_value = value;
            }
        }
        return best;
    }

private:
    std::vector<ItemDefinition> catalog_;
    std::unordered_map<std::string, std::size_t> index_;
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
