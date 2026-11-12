#include "strategy/UnifiedStrategicShadowRuntime.hpp"

#include <cassert>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <utility>
#include <vector>

using namespace tft::strategy;
namespace ci = tft::composition_intelligence;
namespace ci = tft::composition_intelligence;

int main() {
    const auto root = std::filesystem::temp_directory_path() /
        "tft-strategic-direction-pivot-recorder-test";
    std::filesystem::remove_all(root);
    const auto output = root / "session" / "strategic_direction_pivot.jsonl";

    StrategicDirectionPivotAuditRecorder recorder(output);
    StrategicCycleInput input;
    input.exploration.round = 4;
    input.evaluation_sequence = 1;

    StrategicCycleResult result;
    result.phase = StrategicCyclePhase::Exploration;
    result.diagnostics.transition_reason = "no_direction_hypothesis_yet";
    result.shadow_only = true;

    const StrategicCycleAuditContext player_one{77, 1, 4};
    const StrategicCycleAuditContext player_two{77, 2, 4};
    assert(recorder.append(player_one, input, result));
    input.evaluation_sequence = 2; // a new emission sequence is not new evidence
    assert(!recorder.append(player_one, input, result));
    input.exploration.gold_available = 10; // a real observed change is retained
    input.evaluation_sequence = 3;
    assert(recorder.append(player_one, input, result));
    assert(recorder.append(player_two, input, result));

    std::ifstream stream(output);
    assert(stream.good());
    std::string line;
    nlohmann::json first, second, third;
    assert(static_cast<bool>(std::getline(stream, line)));
    first = nlohmann::json::parse(line);
    assert(static_cast<bool>(std::getline(stream, line)));
    second = nlohmann::json::parse(line);
    assert(static_cast<bool>(std::getline(stream, line)));
    third = nlohmann::json::parse(line);
    assert(!std::getline(stream, line));

    assert(first.at("schema_version") == 1);
    assert(first.at("match_id") == 77);
    assert(first.at("player_id") == 1);
    assert(first.at("round") == 4);
    assert(first.at("phase") == "EXPLORATION");
    assert(first.at("sequence") == 1);
    assert(second.at("sequence") == 2);
    assert(second.at("observed_context").at("gold_available") == 10);
    assert(third.at("player_id") == 2);
    assert(third.at("sequence") == 1);
    assert(first.at("active_composition").is_null());
    assert(first.at("pivot_candidate").is_null());
    assert(first.at("feasibility").at("status") == "UNAVAILABLE");
    assert(first.at("shadow_only") == true);

    // The runtime-facing bridge executes the real state machine and emits its
    // resulting phase without requiring a game/PPO action or mutating input.
    const auto runtime_output = root / "runtime" / "strategic_direction_pivot.jsonl";
    UnifiedStrategicShadowRuntime runtime(runtime_output);
    StrategicCycleInput runtime_input;
    runtime_input.exploration.round = 6;
    const StrategicCycleAuditContext runtime_context{88, 3, 6};
    const auto runtime_result = runtime.refresh(runtime_context, runtime_input);
    const auto duplicate_runtime_result = runtime.refresh(runtime_context, runtime_input);
    assert(runtime_result.shadow_only);
    assert(duplicate_runtime_result.shadow_only);
    std::ifstream runtime_stream(runtime_output);
    assert(runtime_stream.good());
    assert(static_cast<bool>(std::getline(runtime_stream, line)));
    const auto runtime_record = nlohmann::json::parse(line);
    assert(runtime_record.at("match_id") == 88);
    assert(runtime_record.at("player_id") == 3);
    assert(runtime_record.at("phase") == "NO_EVIDENCE");

    // Re-anchoring the machine after an external composition publication must
    // preserve the recorder sequence for this player/session.
    runtime.reset_machine();
    runtime_input.exploration.gold_available = 25;
    (void)runtime.refresh(runtime_context, runtime_input);
    assert(static_cast<bool>(std::getline(runtime_stream, line)));
    const auto resynchronized_record = nlohmann::json::parse(line);
    assert(resynchronized_record.at("sequence") == 2);
    assert(resynchronized_record.at("observed_context").at("gold_available") == 25);
    assert(!std::getline(runtime_stream, line));

    // Repeated live observations must not advance pivot hysteresis, even
    // when the producer's emission sequence changes.
    const auto pivot_runtime_path = root / "pivot-runtime" / "events.jsonl";
    UnifiedStrategicShadowRuntime pivot_runtime(pivot_runtime_path,
        PivotConfirmationPolicy{3, 60.0, 5});
    const auto make_composition = [](const std::string& id, int carry,
                                     std::vector<ci::CompositionUnit> units) {
        ci::CompositionCandidate candidate;
        candidate.composition_id = id;
        candidate.source = ci::CompositionSource::Native;
        candidate.set_id = "18";
        candidate.patch = "18.1";
        candidate.units = std::move(units);
        candidate.main_carry_id = carry;
        candidate.target_board_size = 8;
        candidate.source_score = 80.0;
        candidate.source_reference = "runtime-dedup-test";
        return candidate;
    };
    StrategicCycleInput pivot_input;
    pivot_input.exploration.round = 4;
    pivot_input.active_composition = ci::ActiveComposition{
        make_composition("composition-current", 1,
            {{1, ci::UnitRole::MainCarry, true, 100},
             {2, ci::UnitRole::Frontline, true, 80}}), 1};
    const StrategicCycleAuditContext pivot_context{101, 0, 4};
    auto pivot_result = pivot_runtime.refresh(pivot_context, pivot_input);
    assert(pivot_result.phase == StrategicCyclePhase::CompositionActive);

    pivot_input.active_composition.reset();
    pivot_input.pivot_candidate = StrategicPivotAnchorCandidate{};
    pivot_input.pivot_candidate->identity = "pivot-next";
    pivot_input.pivot_candidate->target_direction = "composition-next";
    pivot_input.pivot_candidate->target_composition_identity = "composition-next";
    pivot_input.pivot_candidate->source_direction_anchor_identity =
        "direction:composition:composition-current:1";
    pivot_input.pivot_candidate->source_composition_version = 1;
    pivot_input.pivot_candidate->reference_unit_ids = {1, 2, 3};
    pivot_input.pivot_candidate->evidence = {
        StrategicAnchorEvidenceKind::OwnedUnit,
        StrategicAnchorEvidenceKind::TraitCompletion
    };
    pivot_input.pivot_candidate->confidence = 0.9;
    pivot_input.pivot_candidate->reason = "observed_owned_core";
    pivot_input.pivot_candidate->lifecycle = StrategicAnchorLifecycle::Evaluating;
    pivot_input.pivot_destination = make_composition("composition-next", 1,
        {{1, ci::UnitRole::MainCarry, true, 100},
         {2, ci::UnitRole::Frontline, true, 80},
         {3, ci::UnitRole::Support, false, 40}});
    pivot_input.pivot_feasibility = PivotFeasibilityInput{};
    pivot_input.pivot_feasibility->candidate_composition_identity = "composition-next";
    pivot_input.pivot_feasibility->source_direction_anchor_identity =
        "direction:composition:composition-current:1";
    pivot_input.pivot_feasibility->source_composition_version = 1;
    pivot_input.pivot_feasibility->gold_available = 40;
    pivot_input.pivot_feasibility->protected_gold_floor = 20;
    pivot_input.pivot_feasibility->transition_economic_cost = 12.0;
    pivot_input.pivot_feasibility->required_units = {
        {1, 4, true, true, {"Invoker", "Arcanist"}},
        {2, 3, true, false, {"Invoker"}},
        {3, 2, false, false, {"Arcanist"}}
    };
    pivot_input.pivot_feasibility->observed_units = {
        {1, 1, 1, 1, 8}, {2, 1, 1, 0, 7}, {3, 0, 1, 1, 9}
    };
    pivot_input.pivot_feasibility->required_traits = {
        {"Invoker", 2}, {"Arcanist", 2}
    };
    pivot_input.evaluation_sequence = 1;
    pivot_result = pivot_runtime.refresh(pivot_context, pivot_input);
    assert(pivot_result.phase == StrategicCyclePhase::PivotEvaluation);
    assert(pivot_result.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 1);

    pivot_input.evaluation_sequence = 2;
    const auto duplicate_pivot_result =
        pivot_runtime.refresh(pivot_context, pivot_input);
    assert(duplicate_pivot_result.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 1);

    pivot_input.pivot_feasibility->gold_available = 39;
    pivot_input.exploration.gold_available = 39;
    pivot_input.evaluation_sequence = 3;
    pivot_result = pivot_runtime.refresh(pivot_context, pivot_input);
    assert(pivot_result.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 2);

    pivot_input.pivot_feasibility->gold_available = 38;
    pivot_input.exploration.gold_available = 38;
    pivot_input.evaluation_sequence = 4;
    pivot_result = pivot_runtime.refresh(pivot_context, pivot_input);
    assert(pivot_result.phase == StrategicCyclePhase::PivotConfirmed);

    {
        std::ifstream pivot_stream(pivot_runtime_path);
        std::size_t pivot_records = 0;
        while (std::getline(pivot_stream, line)) ++pivot_records;
        assert(pivot_records == 4);
    }

    // A failed append is contained and does not escape into the caller.
    StrategicDirectionPivotAuditRecorder failing(root);
    assert(!failing.append(player_one, input, result));

    std::filesystem::remove_all(root);
    std::cout << "Strategic direction/pivot JSONL recorder tests passed\n";
    return 0;
}
