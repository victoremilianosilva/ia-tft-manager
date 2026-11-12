#include "strategy/UnifiedStrategicShadowRuntime.hpp"

#include <cassert>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>

using namespace tft::strategy;

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
    assert(third.at("player_id") == 2);
    assert(third.at("sequence") == 1);
    assert(first.at("active_composition").is_null());
    assert(first.at("pivot_candidate").is_null());
    assert(first.at("feasibility").at("status") == "UNAVAILABLE");
    assert(first.at("shadow_only") == true);

    // A live candidate remains auditable even when feasibility is incomplete;
    // the recorder must not silently erase the observed target.
    const auto candidate_output = root / "candidate" / "strategic_direction_pivot.jsonl";
    StrategicDirectionPivotAuditRecorder candidate_recorder(candidate_output);
    StrategicCycleInput candidate_input;
    candidate_input.exploration.round = 8;
    candidate_input.pivot_candidate = StrategicPivotAnchorCandidate{};
    candidate_input.pivot_candidate->identity = "pivot:source:target";
    candidate_input.pivot_candidate->target_direction = "TargetTrait";
    candidate_input.pivot_candidate->target_composition_identity = "target-composition";
    candidate_input.pivot_candidate->source_direction_anchor_identity = "direction:source:v1";
    candidate_input.pivot_candidate->source_composition_version = 1;
    candidate_input.pivot_candidate->reference_unit_ids = {12};
    candidate_input.pivot_candidate->lifecycle = StrategicAnchorLifecycle::Evaluating;
    StrategicCycleResult incomplete_result;
    incomplete_result.phase = StrategicCyclePhase::NoEvidence;
    incomplete_result.diagnostics.transition_reason = "transition_economic_cost_missing";
    assert(candidate_recorder.append(
        StrategicCycleAuditContext{99, 4, 8}, candidate_input, incomplete_result));
    std::ifstream candidate_stream(candidate_output);
    assert(static_cast<bool>(std::getline(candidate_stream, line)));
    const auto candidate_record = nlohmann::json::parse(line);
    assert(candidate_record.at("pivot_candidate").at("identity") == "pivot:source:target");
    assert(candidate_record.at("pivot_candidate").at("target_direction") == "TargetTrait");
    assert(candidate_record.at("feasibility").at("status") == "UNAVAILABLE");

    // The runtime-facing bridge executes the real state machine and emits its
    // resulting phase without requiring a game/PPO action or mutating input.
    const auto runtime_output = root / "runtime" / "strategic_direction_pivot.jsonl";
    UnifiedStrategicShadowRuntime runtime(runtime_output);
    StrategicCycleInput runtime_input;
    runtime_input.exploration.round = 6;
    const auto runtime_result = runtime.refresh(
        StrategicCycleAuditContext{88, 3, 6}, runtime_input);
    assert(runtime_result.shadow_only);
    std::ifstream runtime_stream(runtime_output);
    assert(runtime_stream.good());
    assert(static_cast<bool>(std::getline(runtime_stream, line)));
    const auto runtime_record = nlohmann::json::parse(line);
    assert(runtime_record.at("match_id") == 88);
    assert(runtime_record.at("player_id") == 3);
    assert(runtime_record.at("phase") == "NO_EVIDENCE");

    // A failed append is contained and does not escape into the caller.
    StrategicDirectionPivotAuditRecorder failing(root);
    assert(!failing.append(player_one, input, result));

    std::filesystem::remove_all(root);
    std::cout << "Strategic direction/pivot JSONL recorder tests passed\n";
    return 0;
}
