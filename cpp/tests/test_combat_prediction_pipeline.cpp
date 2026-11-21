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

    auto stale = identity;
    stale.sequence = 30;
    assert(!builder.build(stale, input, 31).valid);

    auto wrong_matchup = input;
    wrong_matchup.player_b.player_id = 2;
    assert(!builder.build(identity, wrong_matchup, 31).valid);

    assert(!CombatProjectionEngine{}.project(snapshot, 6, 0, 300).simulation_completed);
    assert(!CombatProjectionEngine{}.project(snapshot, 6, 33, 300).simulation_completed);

    std::cout << "combat prediction pipeline tests passed\n";
}
