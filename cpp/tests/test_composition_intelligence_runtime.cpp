#include "composition_intelligence/CompositionIntelligenceRuntime.hpp"
#include "composition_intelligence/PlannerEvidenceAdapters.hpp"
#include "composition_intelligence/UnitPriorityPlanner.hpp"

#include <algorithm>
#include <cassert>
#include <iostream>

using namespace tft::composition_intelligence;


void shadow_runtime_uses_native_core_and_item_evidence_without_legacy_strategy() {
    CompositionIntelligencePlayerRuntime runtime;
    runtime.begin_cycle(901, 0, 12);

    CompositionCandidate candidate;
    candidate.composition_id = "native-shadow-core";
    candidate.set_id = "TFT18";
    candidate.target_board_size = 1;
    candidate.main_carry_id = 42;
    candidate.units = {{42, UnitRole::MainCarry, true, 90}};

    // This represents the native generator/catalog trait projection for the
    // active core unit. No StrategyInfo or legacy direction is constructed.
    const std::vector<std::string> native_core_traits{"Blackthorn", "Arcanist"};
    tft::items::ItemDefinition emblem;
    emblem.id = "DA_18_Blackthorn";
    emblem.name = "Blackthorn Emblem";
    emblem.grants_trait = emblem.id;
    emblem.carry_weight = 0.4;
    tft::items::ItemEngine item_engine({emblem});
    tft::items::ItemPlayerState item_state;
    item_state.inventory = {emblem.id};
    tft::items::UnitProfile profile;
    profile.uuid = "native-core-unit-42";
    profile.role = 1;
    profile.backline = true;
    profile.attack_damage = 100.0;
    profile.composition_fit = 1.0;
    profile.traits = {"Arcanist"};
    profile.preferred_traits = native_core_traits;
    const auto item_evidence = PlannerEvidenceAdapters::item(
        item_engine, item_state, {{42, profile}}, 12, 12);
    assert(item_evidence.metadata.available);
    assert(item_evidence.units.size() == 1);
    assert(item_evidence.units.front().has_inventory_candidate);
    assert(item_evidence.units.front().best_inventory_fit > 0.0);

    std::size_t matching_core_traits = 0;
    for (const auto& trait : profile.traits)
        if (std::find(native_core_traits.begin(), native_core_traits.end(), trait) !=
            native_core_traits.end()) ++matching_core_traits;
    const double native_synergy = std::clamp(
        static_cast<double>(matching_core_traits) / 2.0, 0.0, 1.0);
    const std::int32_t current_arcanist_count = 2;
    const std::int32_t arcanist_milestone = 2;
    const bool completes_active_trait =
        current_arcanist_count >= arcanist_milestone &&
        current_arcanist_count - 1 < arcanist_milestone;

    CompositionEvaluationContext context;
    context.match_id = 901;
    context.player_id = 0;
    context.round = 12;
    context.level = 7;
    context.gold = 20;
    OwnedUnitEvidence owned;
    owned.champion_id = 42;
    owned.copies = 1;
    owned.highest_star = 1;
    owned.board_contribution = 0.9;
    owned.synergy_contribution = native_synergy;
    owned.completes_active_trait = completes_active_trait;
    context.owned_units.push_back(owned);
    CandidateEvidence candidate_evidence;
    candidate_evidence.composition_id = candidate.composition_id;
    candidate_evidence.board_fit = 1.0;
    candidate_evidence.item_fit = std::clamp(
        item_evidence.units.front().best_inventory_fit / 2.0, 0.0, 1.0);
    candidate_evidence.availability = 1.0;
    candidate_evidence.economy_feasibility = 1.0;
    candidate_evidence.evidence_confidence = 0.9;
    context.candidate_evidence.push_back(candidate_evidence);

    const auto proposal = runtime.transitions.propose(std::nullopt, {candidate}, context);
    assert(proposal.approved);
    assert(proposal.decision == CompositionDecision::SelectInitial);
    const auto published = runtime.transitions.publish_if_approved(proposal, runtime.active);
    assert(published.has_transition);
    assert(runtime.active.current());
    assert(runtime.active.current()->candidate.composition_id == "native-shadow-core");
    assert(runtime.active.current()->version == 1);

    UnitPriorityContext priority_context;
    priority_context.composition_id = runtime.active.current()
        ? runtime.active.current()->candidate.composition_id : std::string{};
    priority_context.composition_version = runtime.active.current()
        ? runtime.active.current()->version : 0;
    priority_context.owned_units = {{42, 1, 1, true, {}}};
    UnitPriorityEvidence unit_evidence;
    unit_evidence.champion_id = 42;
    unit_evidence.board_contribution = 0.9;
    unit_evidence.synergy_contribution = native_synergy;
    unit_evidence.confidence = 0.9;
    unit_evidence.trait_completion = completes_active_trait;
    priority_context.evidence = {unit_evidence};
    const auto priorities = UnitPriorityPlanner{}.resolve(
        runtime.active.current(), priority_context);
    assert(!priorities.stale);
    const auto prioritized_core = std::find_if(priorities.units.begin(),
        priorities.units.end(), [](const auto& unit) { return unit.champion_id == 42; });
    assert(prioritized_core != priorities.units.end());
    assert(prioritized_core->synergy_contribution > 0.0);
    assert(std::find_if(prioritized_core->reasons.begin(), prioritized_core->reasons.end(),
        [](const auto& reason) {
            return reason.code == UnitReasonCode::TraitCompletionPriority;
        }) != prioritized_core->reasons.end());
}

int main() {
    shadow_runtime_uses_native_core_and_item_evidence_without_legacy_strategy();

    CompositionIntelligencePlayerRuntime player_a;
    CompositionIntelligencePlayerRuntime player_b;

    player_a.begin_cycle(77, 0, 12);
    player_a.mark_stage("candidate_evaluation", "completed", "two candidates");
    player_a.mark_stage("transition_publication", "skipped", "no approved transition");
    nlohmann::json a = {{"composition_id", "comp-a"}, {"composition_version", 3},
                        {"sequence", 100}};
    assert(player_a.append_snapshot(a));
    assert(player_a.snapshots.size() == 1);
    assert(player_a.snapshots.back()["player_id"] == 0);
    assert(player_a.snapshots.back()["match_id"] == 77);
    assert(player_a.snapshots.back()["player_sequence"] == 1);
    assert(player_a.snapshots.back()["runtime_execution"]["stages"].size() == 2);

    // The same logical snapshot with only a different global sequence is a duplicate.
    a["sequence"] = 101;
    assert(!player_a.append_snapshot(a));
    assert(player_a.snapshots.size() == 1);

    player_b.begin_cycle(77, 1, 12);
    player_b.mark_stage("candidate_evaluation", "completed");
    nlohmann::json b = {{"composition_id", "comp-b"}, {"composition_version", 1},
                        {"sequence", 102}};
    assert(player_b.append_snapshot(b));
    assert(player_b.snapshots.size() == 1);
    assert(player_b.snapshots.back()["player_sequence"] == 1);
    assert(player_b.snapshots.back()["player_id"] == 1);

    // A new round is a new logical state and receives the next player sequence.
    player_a.begin_cycle(77, 0, 13);
    player_a.mark_stage("candidate_evaluation", "completed");
    a["round"] = 13;
    assert(player_a.append_snapshot(a));
    assert(player_a.snapshots.size() == 2);
    assert(player_a.snapshots.back()["player_sequence"] == 2);

    player_a.reset();
    assert(player_a.snapshots.empty());
    assert(player_a.next_player_sequence() == 1);
    player_b.begin_cycle(77, 1, 13);
    assert(player_b.next_player_sequence() == 2);
    std::cout << "Composition Intelligence runtime isolation tests passed\n";
    return 0;
}
