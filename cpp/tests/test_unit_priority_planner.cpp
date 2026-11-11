#include "composition_intelligence/UnitPriorityPlanner.hpp"

#include <algorithm>
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
        if (unit.champion_id == 7) assert(unit.intent == UnitIntent::Hold);
    }
}

void pairs_and_star_progress_are_not_sell_candidates() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    auto ctx = context(active);
    CompositionTransitionPlan transition;
    transition.sell_candidate_unit_ids = {8, 9, 10};
    ctx.transition = transition;
    ctx.owned_units = {
        {8, 2, 1, false, {}},
        {9, 1, 2, false, {}},
        {10, 1, 1, false, {}}
    };
    ctx.evidence = {{8, 0.0, 0.0, 0.8, 0}, {9, 0.0, 0.0, 0.8, 0}};
    const auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    for (const auto& unit : result.units) {
        if (unit.champion_id == 8 || unit.champion_id == 9) {
            assert(unit.intent == UnitIntent::Hold);
            assert(unit.sale_restricted);
        }
        if (unit.champion_id == 10) {
            assert(unit.intent == UnitIntent::Hold);
            assert(!unit.sale_restricted);
        }
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

void board_gap_increases_matching_missing_unit_priority() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.match_id = 91; ctx.player_id = 0; ctx.round = 10;
    ctx.owned_units = {{1, 1, 1, true, {}}};
    PlannerEvidenceSnapshot evidence;
    evidence.match_id = 91; evidence.player_id = 0;
    evidence.composition_id = active.candidate.composition_id;
    evidence.composition_version = active.version; evidence.round = 10;
    auto& metadata = evidence.board.metadata;
    metadata.source = "BoardEvaluation"; metadata.source_version = active.version;
    metadata.match_id = 91; metadata.player_id = 0;
    metadata.composition_id = active.candidate.composition_id;
    metadata.source_round = 10; metadata.expected_round = 10;
    metadata.quality = EvidenceQuality::Valid; metadata.available = true;
    evidence.board.missing_frontline_count = 1;
    ctx.planner_evidence = &evidence;
    const auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    const auto frontline = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.champion_id == 2; });
    assert(frontline != result.units.end());
    assert(frontline->intent == UnitIntent::Seek);
    assert(frontline->priority == 364);
    assert(std::find(result.evidence_consumed.begin(), result.evidence_consumed.end(),
        "BoardEvaluation:role_gap_priority_context") != result.evidence_consumed.end());
}

void composition_hierarchy_beats_easy_external_upgrade() {
    ActiveCompositionManager manager;
    auto candidate = comp();
    candidate.units = {
        {1, UnitRole::MainCarry, true, 100},
        {2, UnitRole::Frontline, true, 90},
        {3, UnitRole::Support, false, 60},
        {4, UnitRole::Flex, false, 40}
    };
    manager.publish(candidate);
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.owned_units = {
        {1, 1, 1, true, {}},
        {4, 1, 1, false, {}},
        {9, 2, 2, true, {}}
    };
    ctx.evidence = {
        {1, 0.2, 0.2, 0.9, 1, 1, -1, false},
        {4, 0.2, 0.2, 0.9, 0, 0, -1, false},
        {9, 1.0, 1.0, 1.0, 0, 0, -1, false}
    };
    const auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    const auto carry = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 1; });
    const auto flex = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 4; });
    const auto external = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 9; });
    assert(carry != result.units.end() && carry->tier == UnitPriorityTier::Carry);
    assert(carry->intent == UnitIntent::Upgrade && carry->target_star == 2);
    assert(flex != result.units.end() && flex->tier == UnitPriorityTier::Composition);
    assert(external != result.units.end() && external->priority < flex->priority);
    assert(external->intent == UnitIntent::Hold); // Pair protected, but not promoted above target units.
}

void trait_completion_has_explicit_intermediate_tier() {
    ActiveCompositionManager manager;
    auto candidate = comp();
    candidate.units = {
        {1, UnitRole::Frontline, true, 90},
        {2, UnitRole::Support, false, 70},
        {3, UnitRole::Flex, false, 50}
    };
    manager.publish(candidate);
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.owned_units = {{1, 1, 1, true, {}}, {2, 1, 1, false, {}}, {3, 1, 1, false, {}}};
    ctx.evidence = {
        {1, 0.7, 0.7, 0.9, 0, 0, -1, false},
        {2, 0.2, 0.9, 0.9, 0, 0, -1, true},
        {3, 0.2, 0.2, 0.9, 0, 0, -1, false}
    };
    const auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    const auto trait_piece = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 2; });
    const auto flex = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 3; });
    const auto core = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 1; });
    assert(trait_piece != result.units.end() && trait_piece->tier == UnitPriorityTier::TraitCompletion);
    assert(core != result.units.end() && core->tier == UnitPriorityTier::Core);
    assert(core->priority > trait_piece->priority);
    assert(flex != result.units.end() && trait_piece->priority > flex->priority);
    assert(std::find_if(trait_piece->reasons.begin(), trait_piece->reasons.end(),
        [](const auto& r) { return r.code == UnitReasonCode::TraitCompletionPriority; }) != trait_piece->reasons.end());
}

void shop_copies_advance_two_star_priority_for_core() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.owned_units = {{1, 1, 1, false, {}}};
    ctx.evidence = {{1, 0.0, 0.0, 0.9, 1, 1, -1, false}};
    const auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    const auto carry = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 1; });
    assert(carry != result.units.end());
    assert(carry->intent == UnitIntent::Upgrade);
    assert(carry->target_star == 2);
    assert(std::find_if(carry->reasons.begin(), carry->reasons.end(),
        [](const auto& r) { return r.code == UnitReasonCode::UpgradeProgress; }) != carry->reasons.end());
}


void unaffordable_shop_copy_does_not_create_upgrade_priority() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.gold_available = 2;
    ctx.owned_units = {{1, 1, 1, false, {}}};
    ctx.evidence = {{1, 0.0, 0.0, 0.9, 1, 1, 4, false}};
    const auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    const auto carry = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 1; });
    assert(carry != result.units.end());
    assert(carry->intent == UnitIntent::Keep);
    assert(carry->target_star == 0);
}

void external_temporary_unit_requires_explicit_reason() {
    ActiveCompositionManager manager;
    manager.publish(comp());
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.owned_units = {{9, 1, 1, true, {}}};
    ctx.evidence = {{9, 0.9, 0.8, 0.95, 0, 0, -1, false}};
    auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    auto external = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 9; });
    assert(external != result.units.end() && external->intent == UnitIntent::Replace);

    ctx.temporary_support = {{9, "sustenta a frontline enquanto a peça core não aparece", 0.9}};
    result = UnitPriorityPlanner{}.resolve(active, ctx);
    external = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& u) { return u.champion_id == 9; });
    assert(external != result.units.end());
    assert(external->intent == UnitIntent::Hold);
    assert(external->tier == UnitPriorityTier::TemporarySupport);
    assert(std::find_if(external->reasons.begin(), external->reasons.end(),
        [](const auto& r) { return r.code == UnitReasonCode::TemporarySupportJustification; }) != external->reasons.end());
}

void priority_ties_are_deterministic_by_champion_id() {
    ActiveCompositionManager manager;
    auto candidate = comp();
    candidate.units = {
        {7, UnitRole::Flex, false, 50},
        {6, UnitRole::Flex, false, 50}
    };
    manager.publish(candidate);
    const auto active = *manager.current();
    auto ctx = context(active);
    ctx.owned_units = {{7, 1, 1, false, {}}, {6, 1, 1, false, {}}};
    const auto result = UnitPriorityPlanner{}.resolve(active, ctx);
    assert(result.units.size() == 2);
    assert(result.units[0].priority == result.units[1].priority);
    assert(result.units[0].champion_id == 6);
    assert(result.units[1].champion_id == 7);
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
    pairs_and_star_progress_are_not_sell_candidates();
    validated_item_snapshot_protects_outside_target_unit();
    board_gap_increases_matching_missing_unit_priority();
    composition_hierarchy_beats_easy_external_upgrade();
    trait_completion_has_explicit_intermediate_tier();
    shop_copies_advance_two_star_priority_for_core();
    unaffordable_shop_copy_does_not_create_upgrade_priority();
    external_temporary_unit_requires_explicit_reason();
    priority_ties_are_deterministic_by_champion_id();
    missing_active_is_safe();
    std::cout << "Unit Priority Planner tests passed\n";
}
