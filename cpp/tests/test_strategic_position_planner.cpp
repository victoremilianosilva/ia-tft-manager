#include "composition_intelligence/StrategicPositionPlanner.hpp"

#include <cassert>
#include <iostream>

using namespace tft;
using namespace tft::composition_intelligence;

namespace {
StrategicPositionSnapshot snapshot() {
    StrategicPositionSnapshot s;
    s.match_id = 11; s.player_id = 0; s.round = 8; s.sequence = 19;
    s.composition_id = "active-comp"; s.composition_version = 3; s.alive = true;
    s.board_ids.fill(-1); s.bench_ids.fill(-1);
    return s;
}

void deploy_from_bench_uses_exact_conditioned_mask_and_role() {
    auto s = snapshot();
    s.bench_ids[2] = 77;
    s.composition_units.push_back({77, StrategicPositionRole::Frontline, 100});
    s.masks.type_mask[static_cast<std::size_t>(decision::ActionType::MOVE_BENCH)] = decision::MASK_ENABLED;
    s.masks.bench_move_source_mask[2] = decision::MASK_ENABLED;
    s.masks.bench_to_board_target_masks[2 * decision::BOARD_SIZE + 7] = decision::MASK_ENABLED;

    const auto proposal = StrategicPositionPlanner{}.plan(s);
    assert(proposal.available());
    assert(proposal.champion_id == 77);
    assert(proposal.source_zone == StrategicPositionZone::Bench);
    assert(proposal.source_slot == 2);
    assert(proposal.target_board_slot == 7);
    assert(proposal.reason.find("frontline_role_fit") != std::string::npos);
}

void board_reposition_requires_improved_role_fit_and_exact_mask() {
    auto s = snapshot();
    s.board_ids[0] = 42;
    s.board_ids[8] = 91; // frontline protection for the carry
    s.composition_units.push_back({42, StrategicPositionRole::MainCarry, 1000});
    s.masks.type_mask[static_cast<std::size_t>(decision::ActionType::MOVE_BOARD)] = decision::MASK_ENABLED;
    s.masks.board_source_mask[0] = decision::MASK_ENABLED;
    s.masks.board_move_target_masks[0 * decision::BOARD_SIZE + 21] = decision::MASK_ENABLED;

    const auto proposal = StrategicPositionPlanner{}.plan(s);
    assert(proposal.available());
    assert(proposal.source_zone == StrategicPositionZone::Board);
    assert(proposal.source_slot == 0);
    assert(proposal.target_board_slot == 21);
    assert(proposal.improvement > 1.0);
    assert(proposal.reason.find("carry_backline_and_protection_fit") != std::string::npos);
}

void no_proposal_when_legality_mask_is_disabled() {
    auto s = snapshot();
    s.bench_ids[1] = 77;
    s.composition_units.push_back({77, StrategicPositionRole::Frontline, 10});
    s.masks.type_mask[static_cast<std::size_t>(decision::ActionType::MOVE_BENCH)] = decision::MASK_ENABLED;
    s.masks.bench_move_source_mask[1] = decision::MASK_ENABLED;
    s.masks.bench_to_board_target_masks[1 * decision::BOARD_SIZE + 7] = decision::MASK_DISABLED;
    const auto proposal = StrategicPositionPlanner{}.plan(s);
    assert(!proposal.available());
    assert(proposal.reason.find("no_empty_destination") != std::string::npos);
}

void duplicate_champion_instances_are_never_guessed() {
    auto s = snapshot();
    s.bench_ids[0] = 77;
    s.board_ids[3] = 77;
    s.composition_units.push_back({77, StrategicPositionRole::Frontline, 10});
    s.masks.type_mask[static_cast<std::size_t>(decision::ActionType::MOVE_BENCH)] = decision::MASK_ENABLED;
    s.masks.bench_move_source_mask[0] = decision::MASK_ENABLED;
    s.masks.bench_to_board_target_masks[7] = decision::MASK_ENABLED;
    const auto proposal = StrategicPositionPlanner{}.plan(s);
    assert(!proposal.available());
}

void invalid_or_unversioned_snapshot_is_rejected() {
    auto s = snapshot();
    s.sequence = 0;
    s.bench_ids[0] = 77;
    s.composition_units.push_back({77, StrategicPositionRole::Frontline, 10});
    const auto proposal = StrategicPositionPlanner{}.plan(s);
    assert(!proposal.available());
    assert(proposal.reason == "positioning_snapshot_identity_or_schema_invalid");
}

void no_role_evidence_does_not_invent_a_position() {
    auto s = snapshot();
    s.bench_ids[0] = 77;
    const auto proposal = StrategicPositionPlanner{}.plan(s);
    assert(!proposal.available());
    assert(proposal.reason == "no_role_evidence_for_active_composition");
}

void audit_contains_identity_and_shadow_proposal() {
    auto s = snapshot();
    s.bench_ids[2] = 77;
    s.composition_units.push_back({77, StrategicPositionRole::Frontline, 100});
    s.masks.type_mask[static_cast<std::size_t>(decision::ActionType::MOVE_BENCH)] = decision::MASK_ENABLED;
    s.masks.bench_move_source_mask[2] = decision::MASK_ENABLED;
    s.masks.bench_to_board_target_masks[2 * decision::BOARD_SIZE + 7] = decision::MASK_ENABLED;
    const auto json = StrategicPositionPlanner{}.plan(s).to_json();
    assert(json["identity"]["sequence"] == 19);
    assert(json["target"]["slot"] == 7);
    assert(json["status"] == "positioning_proposal_available");
}
}

int main() {
    deploy_from_bench_uses_exact_conditioned_mask_and_role();
    board_reposition_requires_improved_role_fit_and_exact_mask();
    no_proposal_when_legality_mask_is_disabled();
    duplicate_champion_instances_are_never_guessed();
    invalid_or_unversioned_snapshot_is_rejected();
    no_role_evidence_does_not_invent_a_position();
    audit_contains_identity_and_shadow_proposal();
    std::cout << "StrategicPositionPlanner tests passed\\n";
}
