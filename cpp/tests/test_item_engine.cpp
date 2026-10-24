#include "items/ItemEngine.hpp"
#include "items/ItemActionContract.hpp"
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
    require(engine.metrics().crafts == 3, "craft metric");
    require(engine.metrics().equips == 1, "equip metric");
    require(engine.metrics().invalid_actions >= 2, "invalid operations are counted");

    // Item operations are commands selected by the main policy. There is
    // no item-specific WAIT or parallel heuristic decision function.
    ItemActionCommand equip_command;
    equip_command.operation = ItemOperation::EQUIP_FROM_INVENTORY;
    equip_command.item_id = "guard_plate";
    equip_command.target_unit_uuid = "tank-1";
    const auto equip_result = engine.apply_action(equip_command, {carry, tank});
    require(equip_result.success, "policy equip action should execute");
    require(engine.equipped("tank-1").size() == 1 &&
            engine.inventory().size() == 1,
            "equip action should consume exactly one inventory item");

    require(engine.add_component("sword"), "policy craft sword accepted");
    require(engine.add_component("bow"), "policy craft bow accepted");
    ItemActionCommand craft_command;
    craft_command.operation = ItemOperation::CRAFT_AND_EQUIP;
    craft_command.first_component_id = "sword";
    craft_command.second_component_id = "bow";
    craft_command.target_unit_uuid = "carry-1";
    const auto craft_result = engine.apply_action(craft_command, {carry, tank});
    require(craft_result.success, "policy craft-and-equip action should execute");
    require(engine.components().empty() &&
            engine.equipped("carry-1").size() == 2,
            "craft-and-equip should consume components and equip exactly once");

    ItemActionCommand invalid_command;
    invalid_command.target_unit_uuid = "carry-1";
    const auto invalid_result = engine.apply_action(invalid_command, {carry, tank});
    require(!invalid_result.success && invalid_result.reward == 0.0,
            "missing operation must be rejected rather than interpreted as WAIT");
    require(engine.metrics().crafts == 4, "craft metric");
    require(engine.metrics().equips == 3, "equip metric");
    require(engine.metrics().invalid_actions >= 2, "invalid operations are counted");

    // Phase 1 contract: repeated component IDs represent separate copies,
    // and equipment is keyed by unit-instance UUID rather than champion ID.
    tft::items::ItemPlayerState item_state;
    item_state.components = {"sword", "sword"};
    item_state.inventory = {"damage_blade"};
    item_state.equipped_by_unit_uuid["unit-copy-a"] = {"damage_blade"};
    item_state.equipped_by_unit_uuid["unit-copy-b"] = {};
    require(item_state.components.size() == 2 &&
            item_state.components[0] == item_state.components[1],
            "item state must preserve duplicate component copies");
    require(item_state.equipped_by_unit_uuid["unit-copy-a"].size() == 1 &&
            item_state.equipped_by_unit_uuid["unit-copy-b"].empty(),
            "equipment must be tracked independently for each unit UUID");
    tft::items::ItemActionCommand item_command;
    item_command.operation = tft::items::ItemOperation::EQUIP_FROM_INVENTORY;
    item_command.item_id = "damage_blade";
    item_command.target_unit_uuid = "unit-copy-b";
    require(item_command.operation.has_value() &&
            *item_command.operation == tft::items::ItemOperation::EQUIP_FROM_INVENTORY &&
            item_command.target_unit_uuid == "unit-copy-b",
            "semantic equip command must identify the target unit instance");

    std::cout << "[PASS] Item inventory, recipes, equip, and decision tests.\n";
    return EXIT_SUCCESS;
}
