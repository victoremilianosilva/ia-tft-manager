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
    auto second = recorder.capture(4, active, proposal, priorities, lineup, evidence, actions,
        CompositionTransition{1,2,"comp-old","comp-a",CompositionTransitionReason::StrategicPivot,{5},{10},{7}},
        CompositionOutcomeObservation{6,4,-3.0,0.15,"later observation"});
    assert(second.sequence == 2 && !second.stale);
    auto second_json = second.to_json();
    const auto& payload = second_json["diagnostics"];
    assert(payload["published_transition"]["invalidates_previous_version"] == true);
    assert(payload["recommendation_to_later_outcome"]["interpretation"] == "correlation_only_not_causation");
    assert(payload["source_metadata"]["source"] == "native");
    std::cout << "CompositionDiagnostics tests passed\n";
}