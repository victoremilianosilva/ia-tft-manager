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
        }, {
            "id": "catalog_emblem", "name": "Catalog Emblem",
            "recipe_components": [],
            "stats": {}, "weights": {"utility": 1.0},
            "grants_trait": "DA_18_TestTrait",
            "granted_trait_active_count": 1,
            "combat_effects": []
        }]
    })json");
    const auto loaded_catalog = load_item_catalog(catalog_json);
    require(loaded_catalog.set_id == "synthetic-test-only" &&
            loaded_catalog.components.size() == 2 &&
            loaded_catalog.items.size() == 2 &&
            loaded_catalog.items.front().recipe_components[0] == "sword",
            "versioned external item catalog should load without hard-coded recipes");

    const auto emblem = std::find_if(loaded_catalog.items.begin(), loaded_catalog.items.end(),
        [](const ItemDefinition& item) { return item.id == "catalog_emblem"; });
    require(emblem != loaded_catalog.items.end() &&
            emblem->recipe_components[0].empty() &&
            emblem->grants_trait == "DA_18_TestTrait",
            "non-craftable trait item should load without a recipe");
    ItemEngine loaded_engine(loaded_catalog.items, {"sword", "bow"});
    require(loaded_engine.add_completed_item("catalog_emblem"),
            "non-craftable emblem should be a valid inventory item");
    UnitProfile emblem_target{"emblem-target", 1, 2, false, true,
                              30.0, 0.8, 20.0, 900.0, 30.0, 30.0, 0.8};
    require(loaded_engine.item_fit("catalog_emblem", emblem_target) > 0.0,
            "trait emblem should have strategic value despite zero numeric stats");
    auto planned_emblem_target = emblem_target;
    planned_emblem_target.preferred_traits = {"Test Trait"};
    auto unrelated_emblem_target = emblem_target;
    unrelated_emblem_target.preferred_traits = {"Other Trait"};
    auto natural_emblem_target = planned_emblem_target;
    natural_emblem_target.traits = {"Test Trait"};
    require(loaded_engine.item_fit("catalog_emblem", planned_emblem_target) >
                loaded_engine.item_fit("catalog_emblem", unrelated_emblem_target) + 0.5,
            "emblem compatibility must favor a trait selected by the current composition");
    require(loaded_engine.item_fit("catalog_emblem", planned_emblem_target) >
                loaded_engine.item_fit("catalog_emblem", natural_emblem_target),
            "an emblem should have lower marginal value on a unit that already has that trait");

    std::istringstream inert_catalog_json(R"json({
        "schema_version": 1,
        "set_id": "synthetic-inert-test",
        "components": [
            {"id": "sword", "name": "Test Sword"},
            {"id": "bow", "name": "Test Bow"}
        ],
        "items": [{
            "id": "inert_blade", "name": "Inert Blade",
            "recipe_components": ["sword", "bow"],
            "stats": {}, "weights": {}, "combat_effects": []
        }]
    })json");
    bool inert_catalog_rejected = false;
    try {
        (void)load_item_catalog(inert_catalog_json);
    } catch (const std::invalid_argument&) {
        inert_catalog_rejected = true;
    }
    require(inert_catalog_rejected,
            "runtime loader must reject a structurally valid but inert item catalog");

    std::istringstream mismatched_set_json(R"json({
        "schema_version": 1,
        "set_id": "Set17",
        "source_set_number": 18,
        "components": [],
        "items": []
    })json");
    bool mismatched_set_rejected = false;
    try {
        (void)load_item_catalog(mismatched_set_json);
    } catch (const std::invalid_argument&) {
        mismatched_set_rejected = true;
    }
    require(mismatched_set_rejected,
            "runtime loader must reject set_id/source_set_number mismatches");

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
    require(!invalid_result.success,
            "missing operation must be rejected rather than interpreted as WAIT");
    require(engine.metrics().crafts == 4, "craft metric");
    require(engine.metrics().equips == 3, "equip metric");
    require(engine.metrics().invalid_actions >= 2, "invalid operations are counted");

    // An anvil is a queued choice, not a random direct grant. Only the selected
    // option enters the inventory, and queued anvils are opened one at a time.
    require(engine.grant_component_anvil({"sword", "bow", "rod"}),
            "component anvil should accept unique known component options");
    require(engine.has_pending_anvil() &&
            engine.pending_anvil()->kind == ItemAnvilKind::COMPONENT &&
            engine.pending_anvil()->options.size() == 3,
            "component anvil should expose its three choices");
    const auto components_before_anvil_choice = engine.components().size();
    require(!engine.choose_anvil_option(3),
            "anvil choice outside the offered option range must be rejected");
    require(engine.has_pending_anvil() &&
            engine.components().size() == components_before_anvil_choice,
            "invalid choice must not consume the anvil or grant a component");
    require(engine.choose_anvil_option(1),
            "policy should be able to select one offered component");
    require(!engine.has_pending_anvil() &&
            engine.components().back() == "bow",
            "selected component is granted and the anvil is consumed exactly once");

    require(engine.grant_completed_item_anvil({"damage_blade", "guard_plate"}),
            "completed-item anvil should accept known catalog item options");
    require(engine.choose_anvil_option(0),
            "policy should select one completed item from the anvil");
    require(engine.inventory().back() == "damage_blade" &&
            !engine.has_pending_anvil(),
            "completed-item choice grants only the selected catalog item");
    require(engine.metrics().anvils_received == 2 &&
            engine.metrics().anvil_choices == 2,
            "anvil grant/choice metrics should count exactly once per transition");

    require(!engine.grant_component_anvil({"sword", "sword"}),
            "anvil must not present duplicate options");

    // Auto-merge lifecycle: equipment moves to the upgraded unit; if the
    // three-slot cap is reached, overflow returns to the bag instead of vanishing.
    ItemEngine merge_engine({damage, guard});
    UnitProfile merge_target{"merge-target", 2, 1, false, true, 80.0, 1.2, 0.0, 900.0, 30.0, 30.0, 0.9};
    UnitProfile merge_source_a{"merge-source-a", 1, 0, true, false, 35.0, 0.7, 0.0, 1800.0, 70.0, 60.0, 0.8};
    UnitProfile merge_source_b{"merge-source-b", 1, 0, true, false, 35.0, 0.7, 0.0, 1800.0, 70.0, 60.0, 0.8};
    for (const auto* id : {"damage_blade", "damage_blade", "guard_plate", "damage_blade"}) {
        require(merge_engine.add_completed_item(id), "merge fixture item enters inventory");
    }
    require(merge_engine.equip("damage_blade", merge_target), "equip first target item");
    require(merge_engine.equip("damage_blade", merge_target), "equip second target item");
    require(merge_engine.equip("guard_plate", merge_source_a), "equip first consumed copy");
    require(merge_engine.equip("damage_blade", merge_source_b), "equip second consumed copy");
    require(merge_engine.transfer_equipped_on_merge("merge-source-a", "merge-target"),
            "first consumed unit transfers equipment");
    require(merge_engine.transfer_equipped_on_merge("merge-source-b", "merge-target"),
            "second consumed unit transfers equipment");
    require(merge_engine.equipped("merge-target").size() == ItemEngine::kMaxItemsPerUnit,
            "upgraded unit keeps at most three equipped items");
    require(merge_engine.equipped("merge-source-a").empty() &&
            merge_engine.equipped("merge-source-b").empty(),
            "consumed unit UUIDs no longer own equipment");
    require(merge_engine.inventory().size() == 1 &&
            merge_engine.inventory().front() == "damage_blade",
            "overflow item returns to inventory rather than being lost");

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

    // Selling/removing a unit must return every equipped item to the bag,
    // after which any of those copies can be equipped on another unit.
    const auto inventory_before_release = engine.inventory().size();
    const auto carry_equipped_before_release = engine.equipped("carry-1").size();
    require(carry_equipped_before_release == 2,
            "fixture should have two equipped items before unit sale");
    require(engine.return_equipped_to_inventory("carry-1"),
            "selling an equipped unit should release its items into inventory");
    require(engine.equipped("carry-1").empty(),
            "sold unit must no longer own equipped items");
    require(engine.inventory().size() ==
                inventory_before_release + carry_equipped_before_release,
            "sale must return every equipped item exactly once");
    require(engine.equip("damage_blade", tank),
            "returned item must be equippable on another unit");
    require(engine.equipped("tank-1").size() == 2,
            "new target should own the re-equipped item");
    require(engine.inventory().size() ==
                inventory_before_release + carry_equipped_before_release - 1,
            "re-equipping consumes exactly one returned item");

    std::cout << "[PASS] Item inventory, recipes, equip, and decision tests.\n";
    return EXIT_SUCCESS;
}
