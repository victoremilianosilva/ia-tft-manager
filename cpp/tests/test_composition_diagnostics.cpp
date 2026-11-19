#include "composition_intelligence/CompositionDiagnostics.hpp"
#include <cassert>
#include <sstream>
#include <iostream>
using namespace tft::composition_intelligence;
int main() {
    CompositionDiagnosticRecorder recorder;
    std::optional<ActiveComposition> active;
    CompositionProposal proposal;
    proposal.decision = CompositionDecision::SelectInitial;
    proposal.reason = "initial candidate";
    UnitPrioritySnapshot priorities;
    priorities.stale = true;
    priorities.stale_reason = "waiting for active composition";
    LineupPlan lineup; lineup.stale = true; lineup.stale_reason = "no active composition";
    PlannerEvidenceSnapshot evidence;
    CompositionActionEvaluation actions; actions.stale = true; actions.stale_reason = "no active composition";
    auto first = recorder.capture(3, active, proposal, priorities, lineup, evidence, actions);
    assert(first.sequence == 1 && first.stale);
    auto json = first.to_json();
    assert(json["classification"]["inferred"].size() == 5);
    assert(json["diagnostics"]["action_recommendation"]["shadow_only"] == true);
    assert(json["diagnostics"]["evidence"]["economy"]["gold"].is_null());
    assert(json["diagnostics"]["evidence"]["board"]["total_score"].is_null());
    assert(json["diagnostics"]["evidence"]["items"]["units"].is_null());
    assert(json["diagnostics"]["lineup_plan"]["board_evidence"]["frontline_count"].is_null());
    std::ostringstream stream;
    first.write_jsonl(stream);
    assert(!stream.str().empty() && stream.str().back() == '\n');

    CompositionCandidate candidate;
    candidate.composition_id = "comp-a"; candidate.set_id = "TFT18";
    candidate.target_board_size = 1; candidate.units = {{10, UnitRole::MainCarry, true, 80}};
    candidate.main_carry_id = 10;
    active = ActiveComposition{candidate, 2};
    priorities.composition_id = "comp-a"; priorities.composition_version = 2; priorities.stale = false;
    lineup.composition_id = "comp-a"; lineup.composition_version = 2; lineup.stale = false;
    actions.composition_id = "comp-a"; actions.composition_version = 2; actions.stale = false;
    evidence.economy.metadata.source = "EconomicController";
    evidence.economy.metadata.quality = EvidenceQuality::Valid;
    evidence.economy.metadata.available = true;
    evidence.economy.gold = 0;
    evidence.economy.interest_if_resolved_now = 2;
    evidence.economy.gold_available = true;
    evidence.economy.interest_available = true;
    evidence.economy.projected_income_available = false;
    evidence.items.metadata.source = "ItemEngine";
    evidence.items.metadata.quality = EvidenceQuality::Valid;
    evidence.items.metadata.available = true;
    ItemUnitPlannerEvidence item_unit;
    item_unit.champion_id = 10;
    item_unit.role_source = "derived:UnitCombatClassifier";
    item_unit.composition_source = "derived:ActiveCompositionManager.core_unit_catalog_traits";
    item_unit.composition_id = "comp-a";
    item_unit.composition_version = 2;
    item_unit.composition_fit = 0.8;
    item_unit.preferred_traits = {"Arcanist"};
    evidence.items.units.push_back(item_unit);
    auto second = recorder.capture(4, active, proposal, priorities, lineup, evidence, actions,
        CompositionTransition{1,2,"comp-old","comp-a",CompositionTransitionReason::StrategicPivot,{5},{10},{7}},
        CompositionOutcomeObservation{6,4,-3.0,0.15,"later observation"});
    assert(second.sequence == 2 && !second.stale);
    auto second_json = second.to_json();
    const auto& payload = second_json["diagnostics"];
    assert(payload["published_transition"]["invalidates_previous_version"] == true);
    assert(payload["recommendation_to_later_outcome"]["interpretation"] == "correlation_only_not_causation");
    assert(payload["source_metadata"]["source"] == "native");
    assert(payload["evidence"]["economy"]["gold"] == 0);
    assert(payload["evidence"]["economy"]["interest"] == 2);
    assert(payload["evidence"]["economy"]["projected_income"].is_null());
    assert(payload["evidence"]["economy"]["posture"].is_null());
    assert(payload["evidence"]["items"]["units"][0]["composition_id"] == "comp-a");
    assert(payload["evidence"]["items"]["units"][0]["role_source"] == "derived:UnitCombatClassifier");
    assert(payload["evidence"]["items"]["units"][0]["preferred_traits"][0] == "Arcanist");
    const auto& prior_link = payload["recommendation_to_later_outcome"];
    assert(prior_link["recommendation_round"] == 3);
    assert(prior_link["recommendation_sequence"] == first.sequence);
    assert(prior_link["outcome_round"] == 6);
    assert(prior_link["interpretation"] == "correlation_only_not_causation");

    CompositionOutcomeObservation later{7, std::nullopt, -2.0, 0.0,
        "placement not yet available"};
    const auto third = recorder.capture(5, active, proposal, priorities, lineup,
        evidence, actions, std::nullopt, later);
    const auto third_json = third.to_json();
    const auto& third_payload = third_json["diagnostics"];
    assert(third_payload["outcome_observation"]["placement"].is_null());
    assert(third_payload["recommendation_to_later_outcome"]["recommendation_round"] == 4);
    assert(third_payload["recommendation_to_later_outcome"]["recommendation_sequence"] == second.sequence);
    assert(third_payload["recommendation_to_later_outcome"]["recommendation_composition_id"] == "comp-a");
    assert(third_payload["recommendation_to_later_outcome"]["recommendation_composition_version"] == 2);
    std::cout << "CompositionDiagnostics tests passed\n";
}