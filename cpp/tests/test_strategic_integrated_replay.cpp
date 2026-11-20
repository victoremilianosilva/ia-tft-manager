#include "composition_intelligence/CompositionActionEvaluator.hpp"
#include "composition_intelligence/ContextualActionEvaluator.hpp"
#include "composition_intelligence/StrategicActionCandidateBuilder.hpp"
#include "composition_intelligence/StrategicActionExecutor.hpp"

#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

using namespace tft;
using namespace tft::composition_intelligence;
using namespace tft::strategy;
using json = nlohmann::json;

namespace {
void enable(PlayerActionMasks& masks, decision::ActionType type) {
    masks.type_mask[static_cast<std::size_t>(type)] = decision::MASK_ENABLED;
}

struct ReplayFixture {
    std::optional<ActiveComposition> active;
    UnitPrioritySnapshot priorities;
    LineupPlan lineup;
    StrategicSharedContext context;
    StrategicActionNativeSnapshot native;
    StrategicActionCandidateBuildResult built;
};

ReplayFixture make_fixture() {
    ReplayFixture f;
    CompositionCandidate composition;
    composition.composition_id = "replay-comp-a";
    composition.set_id = "TFT18";
    composition.target_board_size = 2;
    composition.main_carry_id = 10;
    composition.units = {
        {10, UnitRole::MainCarry, true, 100},
        {20, UnitRole::Frontline, true, 90}
    };
    f.active = ActiveComposition{composition, 3};

    UnitPriority carry;
    carry.champion_id = 10;
    carry.intent = UnitIntent::Upgrade;
    carry.relation = UnitStrategicRelation::ActiveCore;
    carry.copies_owned = 2;
    carry.highest_star = 1;
    carry.target_star = 2;
    carry.on_board = true;
    carry.priority = 95;
    carry.confidence = 0.9;
    carry.board_contribution = 0.8;

    UnitPriority frontline;
    frontline.champion_id = 20;
    frontline.intent = UnitIntent::Keep;
    frontline.relation = UnitStrategicRelation::ActiveCore;
    frontline.copies_owned = 1;
    frontline.highest_star = 1;
    frontline.priority = 80;
    frontline.confidence = 0.8;
    frontline.board_contribution = 0.7;

    UnitPriority sale;
    sale.champion_id = 30;
    sale.intent = UnitIntent::SellCandidate;
    sale.relation = UnitStrategicRelation::OutsideTarget;
    sale.copies_owned = 1;
    sale.highest_star = 1;
    sale.priority = 10;
    sale.confidence = 0.9;
    f.priorities.composition_id = composition.composition_id;
    f.priorities.composition_version = 3;
    f.priorities.units = {carry, frontline, sale};

    f.lineup.composition_id = composition.composition_id;
    f.lineup.composition_version = 3;
    f.lineup.level = 5;
    f.lineup.board_capacity = 5;
    f.lineup.endgame_target_ids = {10, 20};
    f.lineup.selected_board = {
        {10, LineupSlotKind::ActiveTarget, 95, true, true},
        {20, LineupSlotKind::ActiveTarget, 80, false, true}
    };

    f.context.player_id = 0;
    f.context.round = 9;
    f.context.gold = 20;
    f.context.level = 5;
    f.context.xp_to_next = 4;
    f.context.alive = true;
    f.context.evidence.gold = true;
    f.context.evidence.level = true;
    f.context.evidence.xp_to_next = true;

    f.native.match_id = 77;
    f.native.player_id = 0;
    f.native.round = 9;
    f.native.sequence = 42;
    f.native.composition_id = composition.composition_id;
    f.native.composition_version = 3;
    f.native.gold = 20;
    f.native.alive = true;
    f.native.shop_champion_ids[0] = 10;
    f.native.bench_champion_ids[0] = 20;
    f.native.bench_champion_ids[1] = 30;
    f.native.bench_unit_uuids[0] = "physical-unit-20";
    f.native.bench_unit_uuids[1] = "physical-unit-30";

    enable(f.native.masks, decision::ActionType::PASS);
    enable(f.native.masks, decision::ActionType::BUY);
    enable(f.native.masks, decision::ActionType::BUY_XP);
    enable(f.native.masks, decision::ActionType::REROLL);
    enable(f.native.masks, decision::ActionType::SELL);
    enable(f.native.masks, decision::ActionType::MOVE_BENCH);
    f.native.masks.shop_mask[0] = decision::MASK_ENABLED;
    f.native.masks.bench_source_mask[1] = decision::MASK_ENABLED;
    f.native.masks.bench_move_source_mask[0] = decision::MASK_ENABLED;
    for (std::size_t target = 0; target < decision::BOARD_SIZE; ++target)
        f.native.masks.bench_to_board_target_masks[target] = decision::MASK_ENABLED;

    f.built = StrategicActionCandidateBuilder{}.build(
        f.context, f.active, f.priorities, f.lineup, f.native,
        {{10, 3}, {20, 2}, {30, 1}});
    assert(f.built.status == "candidates_generated");
    f.context.action_candidates = f.built.candidates;
    return f;
}

const StrategicActionCandidate& candidate(
    const ReplayFixture& f, StrategicActionKind kind, std::int32_t champion_id = -1) {
    const auto found = std::find_if(f.built.candidates.begin(), f.built.candidates.end(),
        [&](const auto& item) {
            return item.kind == kind && item.champion_id == champion_id;
        });
    assert(found != f.built.candidates.end());
    return *found;
}

struct ResolvedScenario {
    StrategicSharedContext source;
    ContextualActionEvaluation recommendation;
    StrategicActionResolution resolution;
};

ResolvedScenario resolve_candidate(
    const ReplayFixture& f, StrategicActionKind kind, std::int32_t champion_id,
    StrategicActionExecutor& executor, const std::string& recommendation_id) {
    ResolvedScenario result;
    result.source = f.context;
    result.source.action_candidates = {candidate(f, kind, champion_id)};
    result.recommendation = ContextualActionEvaluator{}.evaluate(
        f.active, f.priorities, f.lineup, result.source, nullptr, f.native.match_id);
    assert(!result.recommendation.stale);
    assert(result.recommendation.recommended_action == kind);
    if (kind != StrategicActionKind::Hold)
        assert(result.recommendation.recommended_champion_id == champion_id);

    StrategicActionResolutionRequest request;
    request.recommendation_id = recommendation_id;
    request.expected_snapshot_sequence = f.native.sequence;
    request.recommendation = &result.recommendation;
    request.source_context = &result.source;
    request.current_state = &f.native;
    result.resolution = executor.resolve(request);
    return result;
}

json event(const std::string& name, const StrategicActionResolution& result) {
    return {
        {"scenario", name},
        {"accepted", result.accepted},
        {"validation_reason", result.validation_reason},
        {"native_action", result.native_action.values},
        {"shadow_only", result.shadow_only},
        {"execution_attempted", result.execution_attempted},
        {"native_action_applied", false},
        {"identity", {
            {"match_id", result.match_id},
            {"player_id", result.player_id},
            {"round", result.round},
            {"source_sequence", result.source_sequence},
            {"composition_id", result.composition_id},
            {"composition_version", result.composition_version}
        }}
    };
}

std::vector<json> run_replay() {
    auto f = make_fixture();
    assert(f.built.positioning.size() == 1);
    assert(f.built.positioning.front().champion_id == 20);

    const auto baseline = CompositionActionEvaluator{}.evaluate(
        f.active, f.priorities, f.lineup, f.context,
        EconomicControlDecision{}, StrategicActionKind::None, nullptr,
        f.native.match_id);
    assert(!baseline.stale);

    StrategicActionExecutor executor;
    std::vector<json> records;

    const auto buy = resolve_candidate(
        f, StrategicActionKind::BuyUnit, 10, executor, "replay-buy-upgrade");
    assert(buy.resolution.accepted);
    const auto& buy_candidate = candidate(f, StrategicActionKind::BuyUnit, 10);
    auto buy_record = event("buy_upgrade", buy.resolution);
    buy_record["candidate_id"] = buy_candidate.candidate_id;
    buy_record["upgrade_value"] = buy_candidate.upgrade_value;
    buy_record["baseline_candidate_count"] = baseline.candidates.size();
    buy_record["contextual_candidate_count"] = buy.recommendation.candidates.size();
    records.push_back(std::move(buy_record));

    const auto sell = resolve_candidate(
        f, StrategicActionKind::SellUnit, 30, executor, "replay-sell");
    assert(sell.resolution.accepted);
    records.push_back(event("sell", sell.resolution));

    const auto move = resolve_candidate(
        f, StrategicActionKind::DeployOrMove, 20, executor, "replay-positioning");
    assert(move.resolution.accepted);
    auto move_record = event("positioning", move.resolution);
    move_record["target_board_slot"] = candidate(
        f, StrategicActionKind::DeployOrMove, 20).target_board_slot;
    records.push_back(std::move(move_record));

    auto stale_state = f.native;
    stale_state.sequence += 1; // Same round, newer native decision snapshot.
    StrategicActionResolutionRequest stale_request;
    stale_request.recommendation_id = "replay-stale-same-round";
    stale_request.expected_snapshot_sequence = f.native.sequence;
    stale_request.recommendation = &buy.recommendation;
    stale_request.source_context = &buy.source;
    stale_request.current_state = &stale_state;
    const auto stale_result = executor.resolve(stale_request);
    assert(!stale_result.accepted);
    assert(stale_result.validation_reason == "stale_native_snapshot");
    records.push_back(event("stale_same_round", stale_result));

    auto pivoted_state = f.native;
    pivoted_state.sequence += 1;
    pivoted_state.composition_id = "replay-comp-b";
    pivoted_state.composition_version = 4;
    StrategicActionResolutionRequest pivot_request;
    pivot_request.recommendation_id = "replay-old-recommendation-after-pivot";
    pivot_request.expected_snapshot_sequence = pivoted_state.sequence;
    pivot_request.recommendation = &buy.recommendation;
    pivot_request.source_context = &buy.source;
    pivot_request.current_state = &pivoted_state;
    const auto pivot_result = executor.resolve(pivot_request);
    assert(!pivot_result.accepted);
    assert(pivot_result.validation_reason == "stale_or_incompatible_context");
    records.push_back(event("pivot_invalidates_old_recommendation", pivot_result));

    PlannerEvidenceSnapshot contradictory;
    contradictory.match_id = f.native.match_id + 1;
    contradictory.player_id = f.native.player_id;
    contradictory.composition_id = f.native.composition_id;
    contradictory.composition_version = f.native.composition_version;
    contradictory.round = f.native.round;
    const auto contradiction = ContextualActionEvaluator{}.evaluate(
        f.active, f.priorities, f.lineup, buy.source, &contradictory,
        f.native.match_id);
    assert(contradiction.stale);
    assert(contradiction.stale_reason.find("identity mismatch") != std::string::npos);
    records.push_back({
        {"scenario", "contradictory_evidence"},
        {"stale", contradiction.stale},
        {"reason", contradiction.stale_reason},
        {"recommendation", static_cast<int>(contradiction.recommended_action)},
        {"candidates", contradiction.candidates.size()}
    });

    auto empty_source = f.context;
    empty_source.action_candidates.clear();
    const auto no_candidates = ContextualActionEvaluator{}.evaluate(
        f.active, f.priorities, f.lineup, empty_source, nullptr,
        f.native.match_id);
    assert(!no_candidates.stale);
    assert(no_candidates.rationale == "no_candidates");
    assert(no_candidates.candidates.empty());
    StrategicActionResolutionRequest empty_request;
    empty_request.recommendation_id = "replay-no-candidates";
    empty_request.expected_snapshot_sequence = f.native.sequence;
    empty_request.recommendation = &no_candidates;
    empty_request.source_context = &empty_source;
    empty_request.current_state = &f.native;
    const auto empty_resolution = executor.resolve(empty_request);
    assert(!empty_resolution.accepted);
    records.push_back({
        {"scenario", "no_candidates"},
        {"rationale", no_candidates.rationale},
        {"candidate_count", no_candidates.candidates.size()},
        {"resolution_accepted", empty_resolution.accepted},
        {"resolution_reason", empty_resolution.validation_reason}
    });

    StrategicActionResolutionRequest duplicate_request;
    duplicate_request.recommendation_id = "replay-buy-upgrade";
    duplicate_request.expected_snapshot_sequence = f.native.sequence;
    duplicate_request.recommendation = &buy.recommendation;
    duplicate_request.source_context = &buy.source;
    duplicate_request.current_state = &f.native;
    const auto duplicate = executor.resolve(duplicate_request);
    assert(!duplicate.accepted);
    assert(duplicate.validation_reason == "duplicate_recommendation");
    executor.reset();
    const auto after_reset = executor.resolve(duplicate_request);
    assert(after_reset.accepted);
    records.push_back({
        {"scenario", "executor_reset"},
        {"duplicate_rejected", !duplicate.accepted},
        {"duplicate_reason", duplicate.validation_reason},
        {"accepted_after_reset", after_reset.accepted},
        {"execution_attempted", after_reset.execution_attempted}
    });

    for (std::size_t i = 0; i < records.size(); ++i) {
        records[i] = {
            {"schema_version", 1},
            {"sequence_id", i + 1},
            {"event_type", "strategic_replay_scenario"},
            {"payload", std::move(records[i])}
        };
    }
    return records;
}

std::string serialize(const std::vector<json>& records) {
    std::string output;
    for (const auto& record : records) output += record.dump() + "\n";
    return output;
}
}

int main(int argc, char** argv) {
    const auto first = serialize(run_replay());
    const auto second = serialize(run_replay());
    assert(first == second && "Integrated replay artifact must be deterministic.");

    std::ifstream manifest_file(TFT_STRATEGIC_REPLAY_FIXTURE);
    assert(manifest_file.good());
    const auto manifest = json::parse(manifest_file);
    assert(manifest.at("schema_version") == 1);
    assert(manifest.at("replay_id") == "strategic-integrated-replay-v1");
    const auto records = run_replay();
    assert(manifest.at("scenarios").size() == records.size());
    for (std::size_t i = 0; i < records.size(); ++i)
        assert(manifest.at("scenarios").at(i) == records[i].at("payload").at("scenario"));

    const std::string output_path = argc > 1
        ? argv[1] : "strategic_integrated_replay.jsonl";
    std::ofstream output(output_path, std::ios::binary | std::ios::trunc);
    assert(output.good());
    output << first;
    output.close();
    assert(output.good());
    std::cout << "Strategic integrated replay passed; artifact: "
              << output_path << "\n";
    return 0;
}
