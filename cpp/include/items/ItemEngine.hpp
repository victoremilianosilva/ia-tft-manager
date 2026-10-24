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

enum class DecisionKind : std::uint8_t {
    WAIT,
    EQUIP_FROM_INVENTORY,
    CRAFT_AND_EQUIP,
    TRANSFER,
    UNEQUIP_TO_INVENTORY
};

struct ItemDecision {
    DecisionKind kind{DecisionKind::WAIT};
    std::string item_id;
    std::string source_unit_uuid;
    std::string target_unit_uuid;
    std::string first_component;
    std::string second_component;
    double immediate_value{0.0};
    double future_value{0.0};
    double urgency{0.0};
    double total_value{0.0};
};

// Bounded reward shaping for RL integration. Reward marginal value, not the
// mechanical act of crafting/equipping; preserve components when waiting has
// more expected value and do not let repeated transfers farm reward.
inline double item_action_reward(double immediate_gain, double future_value,
                                double urgency, double transfer_fit_delta = 0.0) noexcept {
    const double urgent = std::clamp(urgency, 0.0, 1.0);
    const double gain = std::clamp(immediate_gain, -5.0, 5.0);
    const double future = std::clamp(future_value, 0.0, 5.0);
    const double transfer = 0.15 * std::tanh(transfer_fit_delta);
    return std::clamp(gain * (0.65 + 0.35 * urgent) -
                      future * (1.0 - urgent) + transfer, -1.0, 1.0);
}

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
        const auto target_items = equipped_.find(target.uuid);
        const std::size_t target_count = target_items == equipped_.end()
            ? 0U : target_items->second.size();
        if (item == source->second.end() || target_count >= kMaxItemsPerUnit) {
            ++metrics_.invalid_actions;
            return false;
        }
        // Do not insert target into the unordered_map until after using source
        // iterators: insertion could rehash and invalidate them.
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

    // Keep/wait is a first-class option. Spend a component only when the
    // immediate gain exceeds the estimated future value after urgency weighting.
    [[nodiscard]] ItemDecision decide_craft(
        const std::string& first, const std::string& second,
        const std::vector<UnitProfile>& candidates, int stage, double hp) const {
        ItemDecision best;
        best.kind = DecisionKind::WAIT;
        best.total_value = 0.0;
        const auto count_component = [this](const std::string& id) {
            return static_cast<std::size_t>(std::count(
                components_.begin(), components_.end(), id));
        };
        if (first.empty() || second.empty() ||
            (first == second && count_component(first) < 2U) ||
            (first != second &&
             (count_component(first) == 0U || count_component(second) == 0U))) {
            return best;
        }
        const auto item_id = craftable_item(first, second);
        if (!item_id) return best;
        const auto* item = find(*item_id);
        if (!item) return best;
        const double urgency = std::max(
            std::clamp((65.0 - hp) / 65.0, 0.0, 1.0),
            std::clamp((static_cast<double>(stage) - 2.0) / 6.0, 0.0, 1.0));
        for (const auto& candidate : candidates) {
            if (candidate.uuid.empty() ||
                equipped(candidate.uuid).size() >= kMaxItemsPerUnit) continue;
            const double fit = item_fit(*item_id, candidate);
            const double future = 0.15 + 0.35 * std::clamp(candidate.composition_fit, 0.0, 1.0);
            const double immediate = fit * (0.65 + 0.35 * urgency);
            const double value = immediate + urgency * 0.25 - future * (1.0 - urgency);
            if (value > best.total_value) {
                best.kind = DecisionKind::CRAFT_AND_EQUIP;
                best.item_id = *item_id;
                best.target_unit_uuid = candidate.uuid;
                best.first_component = first;
                best.second_component = second;
                best.immediate_value = immediate;
                best.future_value = future;
                best.urgency = urgency;
                best.total_value = value;
            }
        }
        return best;
    }

    // Compare all currently legal item decisions against WAIT. This method
    // considers every craftable pair, inventory equip and beneficial transfer;
    // it never treats the mechanical action itself as value.
    [[nodiscard]] ItemDecision decide_best_action(
        const std::vector<UnitProfile>& candidates, int stage, double hp) const {
        ItemDecision best;
        best.kind = DecisionKind::WAIT;
        best.total_value = 0.0;
        const double urgency = std::max(
            std::clamp((65.0 - hp) / 65.0, 0.0, 1.0),
            std::clamp((static_cast<double>(stage) - 2.0) / 6.0, 0.0, 1.0));

        const auto consider = [&best](const ItemDecision& candidate) {
            if (candidate.kind != DecisionKind::WAIT &&
                candidate.total_value > best.total_value) {
                best = candidate;
            }
        };

        // Do not greedily consume the first available pair: score all pairs.
        for (std::size_t i = 0; i < components_.size(); ++i) {
            for (std::size_t j = i + 1; j < components_.size(); ++j) {
                consider(decide_craft(
                    components_[i], components_[j], candidates, stage, hp));
            }
        }

        // Crafted items already in inventory have no additional component
        // opportunity cost, but still need a free slot and a useful holder.
        for (const auto& item_id : inventory_) {
            for (const auto& target : candidates) {
                if (target.uuid.empty() ||
                    equipped(target.uuid).size() >= kMaxItemsPerUnit) continue;
                const double fit = item_fit(item_id, target);
                const double value = fit * (0.65 + 0.35 * urgency);
                if (value > best.total_value) {
                    ItemDecision decision;
                    decision.kind = DecisionKind::EQUIP_FROM_INVENTORY;
                    decision.item_id = item_id;
                    decision.target_unit_uuid = target.uuid;
                    decision.immediate_value = fit;
                    decision.urgency = urgency;
                    decision.total_value = value;
                    best = std::move(decision);
                }
            }
        }

        // Transfer only when the destination is a meaningfully better holder.
        // A small deadband prevents shuffling items for negligible fit changes.
        for (const auto& [source_uuid, item_ids] : equipped_) {
            const auto source_profile = std::find_if(
                candidates.begin(), candidates.end(),
                [&source_uuid](const UnitProfile& unit) {
                    return unit.uuid == source_uuid;
                });
            if (source_profile == candidates.end()) continue;
            for (const auto& item_id : item_ids) {
                const double source_fit = item_fit(item_id, *source_profile);
                for (const auto& target : candidates) {
                    if (target.uuid.empty() || target.uuid == source_uuid ||
                        equipped(target.uuid).size() >= kMaxItemsPerUnit) continue;
                    const double delta = item_fit(item_id, target) - source_fit;
                    if (delta <= 0.10) continue;
                    const double value = delta * (0.65 + 0.35 * urgency);
                    if (value > best.total_value) {
                        ItemDecision decision;
                        decision.kind = DecisionKind::TRANSFER;
                        decision.item_id = item_id;
                        decision.source_unit_uuid = source_uuid;
                        decision.target_unit_uuid = target.uuid;
                        decision.immediate_value = delta;
                        decision.urgency = urgency;
                        decision.total_value = value;
                        best = std::move(decision);
                    }
                }
            }
        }
        return best;
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
