#include "composition_intelligence/UnitPriorityPlanner.hpp"

#include <cassert>
#include <iostream>

using namespace tft::composition_intelligence;

namespace {
CompositionCandidate comp() {
    CompositionCandidate c;
    c.composition_id = "comp-A";
    c.set_id = "18";
    c.target_board_size = 8;
    c.main_carry_id = 1;
    c.units = {
        {1, UnitRole::MainCarry, true, 100},
        {2, UnitRole::Frontline, true, 90},
        {3, UnitRole::Support, false, 60}
    };
    return c;
}
UnitPriorityContext context(const ActiveComposition& active) {
    UnitPriorityContext c;
    c.composition_id = active.candidate.composition_id;
    c.composition_version = active.version;
    return c;
}
void resolves_keep_upgrade_seek_and_version() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.owned_units = {{1, 2, 1, true, {}}, {2, 1, 1, true, {}}};
    ctx.evidence = {{1, 0.8, 0.7, 0.9, 2}, {2, 0.7, 0.8, 0.9, 0}};
    UnitPriorityPlanner planner;
    auto result = planner.resolve(active, ctx);
    assert(!result.stale && result.units.size() == 3);
    bool keep=false, upgrade=false, seek=false;
    for (const auto& unit : result.units) {
        keep |= unit.champion_id == 2 && unit.intent == UnitIntent::Keep;
        upgrade |= unit.champion_id == 1 && unit.intent == UnitIntent::Upgrade && unit.target_star == 2;
        seek |= unit.champion_id == 3 && unit.intent == UnitIntent::Seek;
    }
    assert(keep && upgrade && seek);
    auto stale = ctx;
    stale.composition_version++;
    assert(planner.resolve(active, stale).stale);
}
void shared_and_bridge_units_survive_pivot() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    auto next = comp();
    next.composition_id = "comp-B";
    next.units = {{1, UnitRole::MainCarry, true, 100}, {4, UnitRole::Frontline, true, 90}};
    next.main_carry_id = 1;
    manager.publish(next);
    const auto active = *manager.current();
    auto ctx = context(active);
    CompositionTransitionPlan transition;
    transition.shared_unit_ids = {1};
    transition.bridge_unit_ids = {2};
    transition.sell_candidate_unit_ids = {3};
    ctx.transition = transition;
    ctx.owned_units = {{1, 1, 1, true, {}}, {2, 1, 2, true, {}}, {3, 1, 1, false, {}}, {9, 1, 1, false, {}}};
    ctx.evidence = {{2, 0.2, 0.3, 0.8, 0}, {3, 0.1, 0.1, 0.8, 0}};
    auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    bool bridge=false, sell=false, replace=false, shared=false, seek=false;
    for (const auto& unit : result.units) {
        bridge |= unit.champion_id == 2 && unit.intent == UnitIntent::Hold && unit.relation == UnitStrategicRelation::Bridge;
        sell |= unit.champion_id == 3 && unit.intent == UnitIntent::SellCandidate;
        replace |= unit.champion_id == 9 && unit.intent == UnitIntent::Replace;
        shared |= unit.champion_id == 1 && unit.intent == UnitIntent::Keep &&
            unit.relation == UnitStrategicRelation::SharedCore;
        seek |= unit.champion_id == 4 && unit.intent == UnitIntent::Seek;
    }
    assert(bridge && sell && replace && shared && seek);
}
void equipped_items_restrict_sale_and_low_evidence_holds() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    auto active = *manager.current();
    auto ctx = context(active);
    ctx.owned_units = {{8, 1, 1, true, {"item-x"}}, {7, 1, 1, false, {}}};
    ctx.evidence = {{7, 0.0, 0.0, 0.05, 0}};
    CompositionTransitionPlan transition;
    transition.sell_candidate_unit_ids = {8, 7};
    ctx.transition = transition;
    auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    for (const auto& unit : result.units) {
        if (unit.champion_id == 8) assert(unit.intent == UnitIntent::Hold && unit.sale_restricted);
        if (unit.champion_id == 7) assert(unit.intent == UnitIntent::SellCandidate);
    }
}

void validated_item_snapshot_protects_outside_target_unit() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.match_id = 99;
    ctx.player_id = 0;
    ctx.round = 12;
    ctx.owned_units = {{8, 1, 1, false, {}}};
    CompositionTransitionPlan transition;
    transition.sell_candidate_unit_ids = {8};
    ctx.transition = transition;
    PlannerEvidenceSnapshot evidence;
    evidence.match_id = 99;
    evidence.player_id = 0;
    evidence.composition_id = active.candidate.composition_id;
    evidence.composition_version = active.version;
    evidence.round = 12;
    evidence.items.metadata.source = "ItemEngine";
    evidence.items.metadata.source_version = active.version;
    evidence.items.metadata.match_id = 99;
    evidence.items.metadata.player_id = 0;
    evidence.items.metadata.composition_id = active.candidate.composition_id;
    evidence.items.metadata.source_round = 12;
    evidence.items.metadata.expected_round = 12;
    evidence.items.metadata.quality = EvidenceQuality::Valid;
    evidence.items.metadata.available = true;
    evidence.items.units.push_back({8, {"equipped-item"}, {}, 0.0, 0.0, true, false});
    ctx.planner_evidence = &evidence;
    auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    bool protected_unit = false;
    for (const auto& unit : result.units)
        if (unit.champion_id == 8)
            protected_unit = unit.intent == UnitIntent::Hold && unit.sale_restricted;
    assert(protected_unit);
    assert(!result.evidence_rejected.empty()); // Board evidence was intentionally absent.
}

void missing_active_is_safe() {
    auto result = UnitPriorityPlanner{}.resolve(std::nullopt, {});
    assert(result.stale && result.units.empty());
}
}
int main() {
    resolves_keep_upgrade_seek_and_version();
    shared_and_bridge_units_survive_pivot();
    equipped_items_restrict_sale_and_low_evidence_holds();
    validated_item_snapshot_protects_outside_target_unit();
    missing_active_is_safe();
    std::cout << "Unit Priority Planner tests passed\n";
}
