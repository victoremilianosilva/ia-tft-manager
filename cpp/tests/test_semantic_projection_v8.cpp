#include <cassert>
#include <cmath>
#include <map>
#include <limits>
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
    strategic.round = snapshot.round;
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
    strategic.planner_output_sequence = 8;
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
    strategic.opportunity_costs.push_back({7, 50.0, 0.1, 3, "same_snapshot_competing_alternative.v1", "candidate:2", "contextual_action_score.v1"});

    player.item_component_catalog = {
        "component:test", "component:1", "component:2", "component:3", "component:4",
        "component:5", "component:6", "component:7", "component:8", "component:9"
    };
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
    assert(close(projection.numeric[76], 1.0));  // active unit
    assert(close(projection.numeric[77], 1.0));  // active core
    assert(close(projection.numeric[78], 1.0));  // direction reference
    assert(close(projection.numeric[79], 1.0));  // pivot reference
    assert(close(projection.numeric[109], 0.8)); // native unit priority
    assert(close(projection.numeric[110], 0.5)); // native priority intent
    assert(close(projection.numeric[111], 1.0)); // selected lineup
    assert(close(projection.numeric[112], 1.0)); // lineup target
    assert(close(projection.numeric[113], 0.5)); // opportunity cost value
    assert(close(projection.numeric[114], 1.0)); // opportunity cost available

    // Every item feature block must land at its canonical v8 carrier offset.
    assert(close(projection.numeric[1960], 0.15));
    assert(close(projection.numeric[1970], 0.25));
    assert(close(projection.numeric[2123], 0.35));
    assert(close(projection.numeric[3823], 0.45));
    assert(close(projection.numeric[4156], 0.55));
    assert(close(projection.numeric[7856], 1.0)); // pending anvil
    assert(close(projection.numeric[7859], 0.65)); // first anvil option

    const auto original_hash = projection.sha256;
    auto changed = snapshot;
    changed.players[0].strategic_state.unit_priorities[0].priority = 60;
    const auto changed_projection = project_player(changed, 0, 0, catalog);
    assert(close(changed_projection.numeric[109], 0.6));
    assert(changed_projection.sha256 != original_hash);

    auto changed_pivot = snapshot;
    changed_pivot.players[0].strategic_state.pivot_candidate_identity = "pivot:alternative";
    const auto changed_pivot_projection = project_player(changed_pivot, 0, 0, catalog);
    assert(changed_pivot_projection.sha256 != original_hash);

    auto changed_direction = snapshot;
    changed_direction.players[0].strategic_state.direction_identity = "direction:alternative";
    const auto changed_direction_projection = project_player(changed_direction, 0, 0, catalog);
    assert(changed_direction_projection.sha256 != original_hash);

    auto changed_item = snapshot;
    changed_item.players[0].item_inventory_features[0][0] = 0.75f;
    const auto changed_item_projection = project_player(changed_item, 0, 0, catalog);
    assert(close(changed_item_projection.numeric[1970], 0.75));
    assert(changed_item_projection.sha256 != original_hash);

    // Missing/unknown catalog identity is represented as unknown (ID 0), not
    // fabricated from an internal integer that is absent from the loaded catalog.
    auto unknown = snapshot;
    unknown.players[0].board[0].champion_id = "TFT_UnknownChampion";
    unknown.players[0].board[0].champion_internal_id = 999;
    unknown.players[0].strategic_state.active_unit_ids.clear();
    unknown.players[0].strategic_state.active_core_unit_ids.clear();
    unknown.players[0].strategic_state.direction_reference_unit_ids.clear();
    unknown.players[0].strategic_state.pivot_reference_unit_ids.clear();
    unknown.players[0].strategic_state.unit_copy_progress.clear();
    unknown.players[0].strategic_state.unit_priorities.clear();
    unknown.players[0].strategic_state.opportunity_costs.clear();
    unknown.players[0].strategic_state.opportunity_cost_available = false;
    unknown.players[0].strategic_state.lineup_selected_unit_ids.clear();
    unknown.players[0].strategic_state.lineup_entry_unit_ids.clear();
    unknown.players[0].strategic_state.planner_outputs_valid = false;
    unknown.players[0].strategic_state.planner_output_sequence = 0;
    const auto unknown_projection = project_player(unknown, 0, 0, catalog);
    assert(unknown_projection.champion_ids[0] == 0);
    assert(close(unknown_projection.numeric[70 + 5], 0.0));

    // Target-profile normalization saturates at one and preserves zero as zero.
    auto boundary = snapshot;
    boundary.players[0].board[0].attack_damage = 500.0;
    boundary.players[0].board[0].attack_speed = 3.0;
    boundary.players[0].board[0].max_health = 3000.0;
    boundary.players[0].board[0].armor = 200.0;
    boundary.players[0].board[0].magic_resist = 200.0;
    const auto boundary_projection = project_player(boundary, 0, 0, catalog);
    assert(close(boundary_projection.numeric[93], 1.0));
    assert(close(boundary_projection.numeric[94], 1.0));
    assert(close(boundary_projection.numeric[95], 1.0));
    assert(close(boundary_projection.numeric[96], 1.0));
    assert(close(boundary_projection.numeric[97], 1.0));

    const auto rejects = [&](AuditSnapshot invalid) {
        try {
            (void)project_player(invalid, 0, 0, catalog);
        } catch (const std::runtime_error&) {
            return true;
        }
        return false;
    };
    auto invalid_item_feature = snapshot;
    invalid_item_feature.players[0].item_recipe_target_fit[0][0] = 1.01f;
    assert(rejects(invalid_item_feature));
    auto non_finite_item_feature = snapshot;
    non_finite_item_feature.players[0].item_inventory_features[0][0] =
        std::numeric_limits<float>::quiet_NaN();
    assert(rejects(non_finite_item_feature));
    auto duplicate_priority = snapshot;
    duplicate_priority.players[0].strategic_state.unit_priorities.push_back(
        duplicate_priority.players[0].strategic_state.unit_priorities.front());
    assert(rejects(duplicate_priority));
    auto unavailable_planner_with_rows = snapshot;
    unavailable_planner_with_rows.players[0].strategic_state.planner_outputs_valid = false;
    assert(rejects(unavailable_planner_with_rows));
    auto invalid_anvil = snapshot;
    invalid_anvil.players[0].pending_anvil = false;
    invalid_anvil.players[0].pending_anvil_sequence = 5;
    assert(rejects(invalid_anvil));

    return 0;
}
