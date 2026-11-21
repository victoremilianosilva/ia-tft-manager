#include "combat/CombatProjectionEngine.hpp"

#include <cassert>
#include <cmath>
#include <iostream>

using namespace tft;
using namespace tft::combat_evidence;

namespace {
CombatUnit make_unit(int id, UnitTeam team, int x, int source_slot) {
    CombatUnit unit;
    unit.id = id;
    unit.source_unit_uuid = team == UnitTeam::PLAYER_A
        ? "player-unit-uuid" : "opponent-unit-uuid";
    unit.api_name = "TFT_TestUnit";
    unit.name = "Test Unit";
    unit.team = team;
    unit.position = {x, 1};
    unit.source_board_position = source_slot;
    unit.hp = 100.0f;
    unit.max_hp = 100.0f;
    unit.attack_damage = 30.0f;
    unit.attack_speed = 1.0f;
    unit.attack_range = 1.0f;
    unit.ability.api_name = "generic_basic_attack_only";
    unit.ability.metadata_complete = true;
    return unit;
}

CombatInput make_input() {
    CombatInput input;
    input.context = CombatContext::PVP;
    input.seed = 7;
    input.config.seed = 7;
    input.config.max_duration = 30.0f;
    input.config.deterministic = true;
    input.player_a.team = UnitTeam::PLAYER_A;
    input.player_a.player_id = 0;
    input.player_a.player_hp = 40.0f;
    input.player_a.units.push_back(make_unit(0, UnitTeam::PLAYER_A, 0, 0));
    input.player_b.team = UnitTeam::PLAYER_B;
    input.player_b.player_id = 1;
    input.player_b.player_hp = 70.0f;
    input.player_b.units.push_back(make_unit(1, UnitTeam::PLAYER_B, 6, 0));
    return input;
}

CombatSnapshot make_identity() {
    CombatSnapshot identity;
    identity.match_id = 17;
    identity.player_id = 0;
    identity.opponent_id = 1;
    identity.round = 12;
    identity.sequence = 31;
    identity.engine_decision_sequence = 88;
    identity.player_hp = 40.0;
    identity.opponent_hp = 70.0;
    identity.player_unit_ids = {"player-unit-uuid"};
    identity.opponent_unit_ids = {"opponent-unit-uuid"};
    identity.player_roster_complete = true;
    identity.opponent_roster_complete = true;
    return identity;
}
}

int main() {
    const auto input = make_input();
    const auto identity = make_identity();
    const auto builder = CombatProjectionSnapshotBuilder{};
    auto snapshot = builder.build(identity, input, 31);
    assert(snapshot.valid);
    assert(snapshot.validation_reason == "valid");

    const auto coverage = CombatCoverageValidator{}.validate(snapshot.coverage);
    assert(coverage.complete);
    assert(coverage.status == "complete");
    assert(snapshot.coverage.abilities_seen == 2);
    assert(snapshot.coverage.abilities_supported == 2);
    assert(snapshot.coverage.items_seen == 0);
    assert(snapshot.coverage.traits_seen == 0);

    const auto projection = CombatProjectionEngine{}.project(snapshot, 6, 4, 100);
    assert(projection.simulation_completed);
    assert(!projection.decision_eligible);
    assert(projection.status == "experimental_uncalibrated");
    assert(projection.reason == "awaiting_replay_calibration");
    assert(projection.scenarios_requested == 4);
    assert(projection.scenarios_completed == 4);
    assert(projection.incoming_damage_samples.size() == 4);
    assert(std::isfinite(projection.expected_incoming_damage));
    assert(std::isfinite(projection.p50_incoming_damage));
    assert(std::isfinite(projection.p90_incoming_damage));
    for (const auto damage : projection.incoming_damage_samples)
        assert(damage >= 6.0);

    auto missing_ability = input;
    missing_ability.player_a.units.front().ability.api_name.clear();
    missing_ability.player_a.units.front().ability.metadata_complete = false;
    auto incomplete_snapshot = builder.build(identity, missing_ability, 31);
    assert(incomplete_snapshot.valid);
    assert(!CombatCoverageValidator{}.validate(incomplete_snapshot.coverage).complete);
    const auto partial_projection =
        CombatProjectionEngine{}.project(incomplete_snapshot, 6, 2, 200);
    assert(partial_projection.simulation_completed);
    assert(!partial_projection.decision_eligible);
    assert(partial_projection.status == "partial_unsupported_mechanics");

    auto missing_trait_metadata = input;
    CombatTrait active_trait;
    active_trait.api_name = "TFT_TestTrait";
    active_trait.active = true;
    active_trait.active_count = 2;
    missing_trait_metadata.player_a.units.front().traits.push_back(active_trait);
    const auto trait_snapshot = builder.build(identity, missing_trait_metadata, 31);
    assert(!CombatCoverageValidator{}.validate(trait_snapshot.coverage).complete);
    assert(trait_snapshot.coverage.missing_trait_effect_metadata == 1);
    assert(trait_snapshot.coverage.traits_seen == 1);
    assert(trait_snapshot.coverage.traits_supported == 0);

    auto stale = identity;
    stale.sequence = 30;
    assert(!builder.build(stale, input, 31).valid);

    auto wrong_matchup = input;
    wrong_matchup.player_b.player_id = 2;
    assert(!builder.build(identity, wrong_matchup, 31).valid);
    auto wrong_unit_uuid = input;
    wrong_unit_uuid.player_b.units.front().source_unit_uuid = "wrong-unit-uuid";
    assert(!builder.build(identity, wrong_unit_uuid, 31).valid);

    assert(!CombatProjectionEngine{}.project(snapshot, 6, 0, 300).simulation_completed);
    assert(!CombatProjectionEngine{}.project(snapshot, 6, 33, 300).simulation_completed);

    auto second_opponent_input = input;
    second_opponent_input.player_b.player_id = 2;
    second_opponent_input.player_b.units.front().source_unit_uuid = "opponent-two-unit-uuid";
    auto second_opponent_identity = identity;
    second_opponent_identity.opponent_id = 2;
    second_opponent_identity.opponent_hp = 60.0;
    second_opponent_identity.opponent_unit_ids = {"opponent-two-unit-uuid"};
    const auto second_opponent_snapshot =
        builder.build(second_opponent_identity, second_opponent_input, 31);
    assert(second_opponent_snapshot.valid);
    const std::vector<CombatMatchupProjectionCandidate> matchup_candidates{
        {0.75, snapshot}, {0.25, second_opponent_snapshot}};
    const auto matchup_projection =
        CombatProjectionEngine{}.project_matchups(matchup_candidates, 6, 2, 500);
    assert(matchup_projection.simulation_completed);
    assert(!matchup_projection.decision_eligible);
    assert(matchup_projection.opponent_id == -1);
    assert(matchup_projection.weighted_scenarios.size() == 4);
    double probability_sum = 0.0;
    double weighted_damage = 0.0;
    bool saw_first_opponent = false;
    bool saw_second_opponent = false;
    for (const auto& scenario : matchup_projection.weighted_scenarios) {
        probability_sum += scenario.probability;
        weighted_damage += scenario.probability * scenario.incoming_damage;
        saw_first_opponent = saw_first_opponent || scenario.opponent_id == 1;
        saw_second_opponent = saw_second_opponent || scenario.opponent_id == 2;
    }
    assert(std::abs(probability_sum - 1.0) < 1e-9);
    assert(std::abs(weighted_damage - matchup_projection.expected_incoming_damage) < 1e-9);
    assert(saw_first_opponent && saw_second_opponent);
    assert(matchup_projection.status == "experimental_uncalibrated");
    auto invalid_matchup_candidates = matchup_candidates;
    invalid_matchup_candidates[0].probability = 0.50;
    invalid_matchup_candidates[1].probability = 0.25;
    const auto invalid_matchup_projection =
        CombatProjectionEngine{}.project_matchups(invalid_matchup_candidates, 6, 2, 600);
    assert(!invalid_matchup_projection.simulation_completed);
    assert(invalid_matchup_projection.reason ==
        "matchup_probabilities_do_not_sum_to_one");

    std::cout << "combat prediction pipeline tests passed\n";
}
