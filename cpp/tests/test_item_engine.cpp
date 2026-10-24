#include "items/ItemEngine.hpp"

#include <cmath>
#include <cstdlib>
#include <iostream>
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
    damage.carry_weight = 1.0;

    ItemDefinition guard;
    guard.id = "guard_plate";
    guard.name = "Guard Plate";
    guard.recipe_components = {"armor", "cloak"};
    guard.max_health = 150.0;
    guard.armor = 20.0;
    guard.tank_weight = 1.0;

    ItemEngine engine({damage, guard});
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
    require(engine.metrics().crafts == 2, "craft metric");
    require(engine.metrics().equips == 1, "equip metric");
    require(engine.metrics().transfers == 1, "transfer metric");
    require(engine.metrics().unequips == 1, "unequip metric");
    require(engine.metrics().invalid_actions >= 2, "invalid operations are counted");

    const auto urgent = engine.decide_craft("sword", "bow", {carry, tank}, 6, 20.0);
    require(urgent.kind == DecisionKind::CRAFT_AND_EQUIP,
            "useful craft under pressure should be considered");
    require(urgent.target_unit_uuid == "carry-1",
            "decision should choose the stronger item holder");
    const auto no_recipe = engine.decide_craft("component_a", "component_b", {carry}, 2, 100.0);
    require(no_recipe.kind == DecisionKind::WAIT,
            "no known recipe must preserve components");

    std::cout << "[PASS] Item inventory, recipes, equip, transfer, and decision tests.\n";
    return EXIT_SUCCESS;
}
