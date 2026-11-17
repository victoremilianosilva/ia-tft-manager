#include "composition_intelligence/CompositionIntelligenceRuntime.hpp"

#include <cassert>
#include <iostream>

using namespace tft::composition_intelligence;

int main() {
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
