#include "composition_intelligence/LineupPlanner.hpp"
#include <cassert>
#include <iostream>
using namespace tft::composition_intelligence;
namespace {
CompositionCandidate comp() {
    CompositionCandidate c; c.composition_id="comp-A"; c.set_id="18"; c.target_board_size=8; c.main_carry_id=1;
    c.units={{1,UnitRole::MainCarry,true,100},{2,UnitRole::Frontline,true,90},
             {3,UnitRole::Support,false,60},{4,UnitRole::Flex,false,40}};
    return c;
}
void capacity_and_missing_units_are_separated_from_endgame() {
    ActiveCompositionManager manager; manager.publish(comp()); const auto active=*manager.current();
    UnitPrioritySnapshot p; p.composition_id=active.candidate.composition_id; p.composition_version=active.version;
    p.units={{1,UnitIntent::Keep,UnitStrategicRelation::ActiveCore,1,2,3,true,false,120,.9},
             {2,UnitIntent::Keep,UnitStrategicRelation::ActiveCore,1,1,2,true,false,110,.8},
             {3,UnitIntent::Seek,UnitStrategicRelation::MissingTarget,0,1,0,false,false,60,.4},
             {4,UnitIntent::Keep,UnitStrategicRelation::ActiveFlex,1,1,0,false,false,40,.7}};
    LineupPlannerContext c; c.level=4; c.board_capacity=4; c.current_board_ids={1,2};
    const auto r=LineupPlanner{}.plan(active,p,c);
    assert(!r.stale && r.endgame_target_ids.size()==4 && r.selected_board.size()==3);
    assert(r.deferred_target_ids.size()==1 && r.deferred_target_ids[0]==3);
    assert(r.entries.size()==1 && r.entries[0]==4 && r.exits.empty());
}
void owned_target_can_be_deferred_by_capacity() {
    ActiveCompositionManager manager; manager.publish(comp()); const auto active=*manager.current();
    UnitPrioritySnapshot p; p.composition_id=active.candidate.composition_id; p.composition_version=active.version;
    p.units={{1,UnitIntent::Keep,UnitStrategicRelation::ActiveCore,1,2,3,true,false,120,.9},
             {2,UnitIntent::Keep,UnitStrategicRelation::ActiveCore,1,1,2,true,false,110,.8},
             {3,UnitIntent::Keep,UnitStrategicRelation::ActiveFlex,1,1,0,false,false,60,.8},
             {4,UnitIntent::Keep,UnitStrategicRelation::ActiveFlex,1,1,0,false,false,40,.7}};
    LineupPlannerContext c; c.level=2; c.board_capacity=2; c.current_board_ids={1,2};
    const auto r=LineupPlanner{}.plan(active,p,c);
    assert(!r.stale && r.selected_board.size()==2);
    assert(r.endgame_target_ids.size()==4 && r.deferred_target_ids.size()==2);
    assert(r.status=="partial_target_waiting_for_units_or_capacity");
}
void pivot_keeps_bridge_only_as_temporary_capacity_fill() {
    ActiveCompositionManager manager; manager.publish(comp()); auto next=comp();
    next.composition_id="comp-B"; next.main_carry_id=5;
    next.units={{5,UnitRole::MainCarry,true,100},{6,UnitRole::Frontline,true,90}};
    manager.publish(next); const auto active=*manager.current();
    UnitPrioritySnapshot p; p.composition_id=active.candidate.composition_id; p.composition_version=active.version;
    p.units={{5,UnitIntent::Seek,UnitStrategicRelation::MissingTarget,0,1,0,false,false,120,.5},
             {6,UnitIntent::Keep,UnitStrategicRelation::ActiveCore,1,1,2,true,false,110,.8},
             {2,UnitIntent::Hold,UnitStrategicRelation::Bridge,1,2,0,true,false,35,.8},
             {9,UnitIntent::Keep,UnitStrategicRelation::OutsideTarget,1,1,0,true,false,20,.8}};
    LineupPlannerContext c; c.level=3; c.board_capacity=2; c.current_board_ids={2,6,9};
    const auto r=LineupPlanner{}.plan(active,p,c);
    assert(!r.stale && r.endgame_target_ids.size()==2 && r.selected_board.size()==2);
    assert(r.bridge_ids.size()==1 && r.bridge_ids[0]==2);
    assert(r.deferred_target_ids.size()==1 && r.deferred_target_ids[0]==5);
    assert(r.exits.size()==1 && r.exits[0]==9);
}

void valid_board_evidence_is_bound_to_lineup_version() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    UnitPrioritySnapshot p;
    p.composition_id = active.candidate.composition_id;
    p.composition_version = active.version;
    LineupPlannerContext c;
    c.level = 6;
    c.board_capacity = 6;
    PlannerEvidenceSnapshot evidence;
    c.planner_evidence = &evidence;
    evidence.match_id = 123;
    evidence->player_id = 2;
    evidence->composition_id = active.candidate.composition_id;
    evidence->composition_version = active.version;
    evidence->round = 14;
    evidence->board.metadata.source = "BoardEvaluation";
    evidence->board.metadata.source_version = active.version;
    evidence->board.metadata.match_id = 123;
    evidence->board.metadata.player_id = 2;
    evidence->board.metadata.composition_id = active.candidate.composition_id;
    evidence->board.metadata.source_round = 14;
    evidence->board.metadata.expected_round = 14;
    evidence->board.metadata.quality = EvidenceQuality::Valid;
    evidence->board.metadata.available = true;
    evidence->board.frontline_count = 3;
    evidence->board.carry_count = 2;
    evidence->board.exposed_carry_count = 1;
    evidence->board.missing_frontline_count = 0;
    evidence->board.missing_backline_count = 1;
    c.match_id = 123;
    c.player_id = 2;
    c.round = 14;
    const auto result = LineupPlanner{}.plan(active, p, c);
    assert(!result.stale && result.board_evidence_available);
    assert(result.observed_frontline_count == 3);
    assert(result.observed_exposed_carry_count == 1);
    assert(result.observed_missing_backline_count == 1);
}

void board_gap_changes_role_selection_within_target_priority_tier() {
    CompositionCandidate candidate;
    candidate.composition_id = "role-gap";
    candidate.set_id = "18";
    candidate.target_board_size = 2;
    candidate.units = {{3, UnitRole::Support, false, 60}, {4, UnitRole::Frontline, false, 40}};
    ActiveCompositionManager manager;
    manager.publish(candidate);
    const auto active = *manager.current();
    UnitPrioritySnapshot priorities;
    priorities.composition_id = active.candidate.composition_id;
    priorities.composition_version = active.version;
    priorities.units = {
        {3, UnitIntent::Keep, UnitStrategicRelation::ActiveFlex, 1, 1, 0, true, false, 60, .8},
        {4, UnitIntent::Keep, UnitStrategicRelation::ActiveFlex, 1, 1, 0, true, false, 40, .8}
    };
    PlannerEvidenceSnapshot evidence;
    evidence.match_id = 44; evidence.player_id = 1;
    evidence.composition_id = active.candidate.composition_id;
    evidence.composition_version = active.version; evidence.round = 8;
    auto& metadata = evidence.board.metadata;
    metadata.source = "BoardEvaluation"; metadata.source_version = active.version;
    metadata.match_id = 44; metadata.player_id = 1;
    metadata.composition_id = active.candidate.composition_id;
    metadata.source_round = 8; metadata.expected_round = 8;
    metadata.quality = EvidenceQuality::Valid; metadata.available = true;
    evidence.board.missing_frontline_count = 1;
    LineupPlannerContext context;
    context.level = 1; context.board_capacity = 1;
    context.planner_evidence = &evidence;
    context.match_id = 44; context.player_id = 1; context.round = 8;
    const auto result = LineupPlanner{}.plan(active, priorities, context);
    assert(!result.stale && result.selected_board.size() == 1);
    assert(result.selected_board.front().champion_id == 4);
}
void stale_snapshot_is_rejected() {
    ActiveCompositionManager manager; manager.publish(comp()); const auto active=*manager.current();
    UnitPrioritySnapshot p; p.composition_id=active.candidate.composition_id; p.composition_version=active.version+1;
    const auto r=LineupPlanner{}.plan(active,p,{6,6,{}});
    assert(r.stale && r.selected_board.empty());
}
}
int main() {
    capacity_and_missing_units_are_separated_from_endgame();
    owned_target_can_be_deferred_by_capacity();
    pivot_keeps_bridge_only_as_temporary_capacity_fill();
    valid_board_evidence_is_bound_to_lineup_version();
    board_gap_changes_role_selection_within_target_priority_tier();
    stale_snapshot_is_rejected();
    std::cout << "Lineup planner tests passed\n";
}
