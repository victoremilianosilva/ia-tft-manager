#include <cassert>
#include <map>
#include <string>

#include "lobby/SemanticProjectionV8.hpp"

int main() {
    using tft::AuditSnapshot;
    using tft::semantic_v8::project_player;

    AuditSnapshot snapshot;
    snapshot.engine_instance_id = "semantic-projection-test-engine";
    snapshot.episode_id = 41;
    snapshot.snapshot_sequence = 9;
    snapshot.player_decision_sequences[0] = 7;
    snapshot.round = 12;
    snapshot.stage = 3;

    auto& player = snapshot.players[0];
    player.player_id = 0;
    auto& strategic = player.strategic_state;
    strategic.player_id = 0;
    strategic.episode_id = snapshot.episode_id;
    strategic.active_composition_valid = true;
    strategic.active_composition_id = "composition:test";
    strategic.active_composition_version = 4;
    strategic.direction_valid = true;
    strategic.direction_identity = "direction:test";
    strategic.pivot_candidate_valid = true;
    strategic.pivot_candidate_identity = "pivot:test";
    strategic.pivot_target_composition_identity = "composition:target";
    strategic.pivot_source_composition_version = 3;
    strategic.opportunity_cost_available = true;
    strategic.planner_outputs_valid = true;
    strategic.planner_output_sequence = 6;
    strategic.strategic_context_sequence = 8;

    auto& unit = player.board[0];
    unit.occupied = true;
    unit.champion_internal_id = 7;
    unit.champion_id = "TFT_TestChampion";
    unit.uuid = "physical-unit-7";
    unit.star = 1;
    unit.cost = 2;
    unit.trait_names = {"Trait_Test"};
    strategic.active_unit_ids = {7};
    strategic.active_core_unit_ids = {7};
    strategic.direction_reference_unit_ids = {7};
    strategic.pivot_reference_unit_ids = {7};
    strategic.unit_copy_progress.push_back({7, 1, 0, 1});
    strategic.unit_priorities.push_back({7, 3, 1, 80, 2, false, 0.9});
    strategic.lineup_selected_unit_ids = {7};
    strategic.lineup_entry_unit_ids = {7};
    strategic.opportunity_costs.push_back({7, 50.0, 0.1, 3, "planner", "candidate:2", "relative"});

    player.item_component_catalog = {"component:test"};
    player.item_component_features[0] = 0.15f;
    player.item_inventory_features[0][0] = 0.25f;
    player.item_recipe_features[0][0] = 0.35f;
    player.item_inventory_target_fit[0][0] = 0.45f;
    player.item_recipe_target_fit[0][0] = 0.55f;
    player.pending_anvil = true;
    player.pending_anvil_kind = 0;
    player.pending_anvil_sequence = 5;
    player.pending_anvil_options = {"item:test"};
    player.pending_anvil_option_features[0][0] = 0.65f;

    const std::map<std::string, std::int32_t> catalog{{"TFT_TestChampion", 7}};
    const auto projection = project_player(snapshot, 0, 0, catalog);

    const auto close = [](double actual, double expected) { return std::abs(actual - expected) < 1e-6; };

    assert(projection.numeric.size() == 7958);
    assert(projection.champion_ids[0] == 8);
    assert(projection.occupied[0]);
    assert(projection.unit_uuids[0] == "physical-unit-7");
    assert(projection.trait_ids[0][0] > 0);
    assert(projection.numeric[76] == 1.0);  // active unit
    assert(projection.numeric[77] == 1.0);  // active core
    assert(projection.numeric[109] == 0.8); // native unit priority
    assert(projection.numeric[110] == 0.5); // native priority intent

    // Every item feature block must land at its canonical v8 carrier offset.
    assert(projection.numeric[1960] == 0.15);
    assert(projection.numeric[1970] == 0.25);
    assert(projection.numeric[2123] == 0.35);
    assert(projection.numeric[3823] == 0.45);
    assert(projection.numeric[4156] == 0.55);
    assert(projection.numeric[7856] == 1.0); // pending anvil
    assert(projection.numeric[7859] == 0.65); // first anvil option

    const auto original_hash = projection.sha256;
    auto changed = snapshot;
    changed.players[0].strategic_state.unit_priorities[0].priority = 60;
    const auto changed_projection = project_player(changed, 0, 0, catalog);
    assert(changed_projection.numeric[109] == 0.6);
    assert(changed_projection.sha256 != original_hash);

    auto changed_item = snapshot;
    changed_item.players[0].item_inventory_features[0][0] = 0.75f;
    const auto changed_item_projection = project_player(changed_item, 0, 0, catalog);
    assert(changed_item_projection.numeric[1970] == 0.75);
    assert(changed_item_projection.sha256 != original_hash);

    return 0;
}
