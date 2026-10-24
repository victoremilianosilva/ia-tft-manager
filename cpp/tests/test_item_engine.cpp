#include "items/ItemEngine.hpp"
#include "items/CombatItemAdapter.hpp"
#include "items/ItemCatalog.hpp"

#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <stdexcept>

namespace {
void require(bool condition, const char* message) {
    if (!condition) {
        std::cerr << "[FAIL] " << message << '\n';
        std::exit(EXIT_FAILURE);
    }
}
}

int main() {
    using namespace tft::items;

    ItemDefinition damage;
    damage.id = "damage_blade";
    damage.name = "Damage Blade";
    damage.recipe_components = {"sword", "bow"};
    damage.attack_damage = 10.0;
    damage.attack_speed = 0.15;
    damage.critical_strike_chance = 0.20;
    damage.omnivamp = 0.10;
    damage.damage_amplification = 0.15;
    damage.carry_weight = 1.0;

    ItemDefinition guard;
    guard.id = "guard_plate";
    guard.name = "Guard Plate";
    guard.recipe_components = {"armor", "cloak"};
    guard.max_health = 150.0;
    guard.armor = 20.0;
    guard.tank_weight = 1.0;

    ItemDefinition double_component;
    double_component.id = "double_rod";
    double_component.name = "Double Rod";
    double_component.recipe_components = {"rod", "rod"};
    double_component.ability_power = 10.0;

    std::istringstream catalog_json(R"json({
        "schema_version": 1,
        "set_id": "synthetic-test-only",
        "components": [
            {"id": "sword", "name": "Test Sword"},
            {"id": "bow", "name": "Test Bow"}
        ],
        "items": [{
            "id": "catalog_blade", "name": "Catalog Blade",
            "recipe_components": ["sword", "bow"],
            "stats": {"attack_damage": 12.0, "attack_speed": 0.15},
            "weights": {"carry": 1.0}
        }]
    })json");
    const auto loaded_catalog = load_item_catalog(catalog_json);
    require(loaded_catalog.set_id == "synthetic-test-only" &&
            loaded_catalog.components.size() == 2 &&
            loaded_catalog.items.size() == 1 &&
            loaded_catalog.items.front().recipe_components[0] == "sword",
            "versioned external item catalog should load without hard-coded recipes");

    const auto combat_damage = to_combat_item(damage);
    require(combat_damage.api_name == "damage_blade" &&
            std::abs(combat_damage.attack_damage - 10.0f) < 0.001f &&
            std::abs(combat_damage.critical_strike_chance - 0.20f) < 0.001f &&
            std::abs(combat_damage.omnivamp - 0.10f) < 0.001f,
            "item catalog definition should map to combat item stats");

    ItemEngine engine({damage, guard, double_component});
    require(!engine.add_component("unknown_component"),
            "component IDs outside the loaded recipe catalog must be rejected");
    UnitProfile carry{"carry-1", 2, 1, false, true, 80.0, 1.2, 0.0, 900.0, 30.0, 30.0, 0.9};
    UnitProfile tank{"tank-1", 2, 0, true, false, 35.0, 0.7, 0.0, 1800.0, 70.0, 60.0, 0.8};

    require(engine.add_component("sword"), "component should be accepted");
    require(engine.add_component("bow"), "component should be accepted");
    require(engine.components().size() == 2, "component inventory count");
    const auto crafted = engine.craft("sword", "bow");
    require(crafted && *crafted == "damage_blade", "recipe should craft the expected item");
    require(engine.components().empty(), "craft must consume exactly both components");
    require(engine.inventory().size() == 1, "crafted item should enter inventory");

    require(engine.item_fit("damage_blade", carry) > engine.item_fit("damage_blade", tank),
            "damage item should fit carry better than tank");
    require(engine.equip("damage_blade", carry), "equip from inventory");
    require(engine.inventory().empty(), "equipped item leaves inventory");
    require(engine.equipped("carry-1").size() == 1, "equipped item is tracked by unit UUID");
    require(!engine.equip("damage_blade", tank), "cannot equip an item not in inventory");

    require(engine.transfer("damage_blade", "carry-1", tank), "transfer item between units");
    require(engine.equipped("carry-1").empty(), "transfer removes item from source");
    require(engine.equipped("tank-1").size() == 1, "transfer adds item to destination");
    require(engine.unequip("damage_blade", "tank-1"), "unequip returns item to inventory");
    require(engine.inventory().size() == 1, "unequip returns item to inventory");

    require(engine.add_component("armor"), "armor component accepted");
    require(engine.add_component("cloak"), "cloak component accepted");
    const auto crafted_guard = engine.craft("cloak", "armor");
    require(crafted_guard && *crafted_guard == "guard_plate", "recipe order is symmetric");

    require(!engine.craft("sword", "bow"), "missing components cannot be crafted");
    require(engine.add_component("rod"), "first repeated component accepted");
    require(engine.add_component("rod"), "second repeated component accepted");
    const auto double_craft = engine.craft("rod", "rod");
    require(double_craft && *double_craft == "double_rod",
            "recipes may consume two copies of the same component");
    require(item_action_reward(2.0, 1.0, 1.0) > 0.0,
            "valuable immediate item gain under pressure should be positive");
    require(item_action_reward(0.2, 2.0, 0.0) < 0.0,
            "preserving high future value early should discourage a weak craft");
    require(item_action_reward(0.0, 0.0, 0.5, 0.0) == 0.0,
            "no-op transfer must not create reward");
    require(item_action_reward(1.0, 0.0, 0.5, 2.0) >
            item_action_reward(1.0, 0.0, 0.5, -2.0),
            "transfer reward should depend on marginal holder improvement");
    require(engine.metrics().crafts == 3, "craft metric");
    require(engine.metrics().equips == 1, "equip metric");
    require(engine.metrics().transfers == 1, "transfer metric");
    require(engine.metrics().unequips == 1, "unequip metric");
    require(engine.metrics().invalid_actions >= 2, "invalid operations are counted");

    ItemEngine transfer_engine({damage});
    require(transfer_engine.add_component("sword"), "transfer decision sword accepted");
    require(transfer_engine.add_component("bow"), "transfer decision bow accepted");
    require(transfer_engine.craft("sword", "bow").has_value(), "transfer decision item crafted");
    require(transfer_engine.equip("damage_blade", tank), "transfer decision item equipped");
    const auto transfer_decision = transfer_engine.decide_best_action({carry, tank}, 4, 45.0);
    require(transfer_decision.kind == DecisionKind::TRANSFER,
            "decision search should transfer an item to a meaningfully better holder");
    require(transfer_decision.source_unit_uuid == "tank-1" &&
            transfer_decision.target_unit_uuid == "carry-1",
            "transfer decision should identify source and destination units");

    const auto missing_components = engine.decide_craft("sword", "bow", {carry, tank}, 6, 20.0);
    require(missing_components.kind == DecisionKind::WAIT,
            "decision must not craft components that are not in inventory");
    require(engine.add_component("sword"), "decision test sword accepted");
    require(engine.add_component("bow"), "decision test bow accepted");
    const auto urgent = engine.decide_craft("sword", "bow", {carry, tank}, 6, 20.0);
    require(urgent.kind == DecisionKind::CRAFT_AND_EQUIP,
            "useful craft under pressure should be considered");
    require(urgent.target_unit_uuid == "carry-1",
            "decision should choose the stronger item holder");
    const auto no_recipe = engine.decide_craft("component_a", "component_b", {carry}, 2, 100.0);
    require(no_recipe.kind == DecisionKind::WAIT,
            "no known recipe must preserve components");
    const auto best_action = engine.decide_best_action({carry, tank}, 2, 100.0);
    require(best_action.kind == DecisionKind::EQUIP_FROM_INVENTORY ||
            best_action.kind == DecisionKind::CRAFT_AND_EQUIP,
            "best-action search should compare inventory and craft options");


    // Regression: transfers must respect the destination's three-item cap and
    // must be atomic when rejected (the source keeps the item).
    ItemEngine capacity_engine({damage, guard, double_component});
    const auto add_and_craft = [&capacity_engine](const std::string& a,
                                                   const std::string& b) {
        require(capacity_engine.add_component(a), "capacity fixture first component");
        require(capacity_engine.add_component(b), "capacity fixture second component");
        require(capacity_engine.craft(a, b).has_value(), "capacity fixture craft");
    };
    add_and_craft("sword", "bow");
    add_and_craft("armor", "cloak");
    add_and_craft("rod", "rod");
    add_and_craft("sword", "bow");
    require(capacity_engine.equip("damage_blade", carry), "capacity carry item 1");
    require(capacity_engine.equip("guard_plate", carry), "capacity carry item 2");
    require(capacity_engine.equip("double_rod", carry), "capacity carry item 3");
    require(capacity_engine.equip("damage_blade", tank), "capacity source item");
    require(!capacity_engine.transfer("damage_blade", "tank-1", carry),
            "transfer to a unit with three items must be rejected");
    require(capacity_engine.equipped("tank-1").size() == 1 &&
            capacity_engine.equipped("carry-1").size() == 3,
            "rejected transfer must not mutate source or destination equipment");

    std::cout << "[PASS] Item inventory, recipes, equip, transfer, and decision tests.\n";
    return EXIT_SUCCESS;
}
