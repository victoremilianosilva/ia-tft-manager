#include "strategy/StrategicDirectionPivotAuditRecorder.hpp"

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

    // A failed append is contained and does not escape into the caller.
    StrategicDirectionPivotAuditRecorder failing(root);
    assert(!failing.append(player_one, input, result));

    std::filesystem::remove_all(root);
    std::cout << "Strategic direction/pivot JSONL recorder tests passed\n";
    return 0;
}
