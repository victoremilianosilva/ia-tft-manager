#include "composition_intelligence/StrategicActionExecutor.hpp"

#include <cassert>
#include <iostream>

using namespace tft;
using namespace tft::composition_intelligence;
using namespace tft::strategy;

namespace {
StrategicActionNativeSnapshot native_state() {
    StrategicActionNativeSnapshot s;
    s.match_id = 100; s.player_id = 0; s.round = 8; s.sequence = 5;
    s.composition_id = "comp-a"; s.composition_version = 3;
    s.gold = 10; s.alive = true;
    s.shop_champion_ids.fill(-1);
    s.bench_champion_ids.fill(-1);
    s.board_champion_ids.fill(-1);
    return s;
}
StrategicSharedContext source_context(StrategicActionKind kind, int champion_id = -1) {
    StrategicSharedContext c;
    c.player_id = 0; c.round = 8; c.gold = 10; c.alive = true;
    StrategicActionCandidate candidate;
    candidate.kind = kind; candidate.champion_id = champion_id;
    candidate.available = true;
    c.action_candidates.push_back(candidate);
    return c;
}
ContextualActionEvaluation recommendation(StrategicActionKind kind, int champion_id = -1) {
    ContextualActionEvaluation r;
    r.match_id = 100; r.player_id = 0; r.round = 8;
    r.composition_id = "comp-a"; r.composition_version = 3;
    ContextualActionCandidateScore candidate;
    candidate.candidate_index = 0; candidate.kind = kind;
    candidate.champion_id = champion_id; candidate.eligible = true;
    candidate.selected = true;
    r.candidates.push_back(candidate);
    r.recommended_action = kind; r.recommended_champion_id = champion_id;
    return r;
}
StrategicActionResolution resolve(StrategicActionExecutor& executor,
    const ContextualActionEvaluation& r, const StrategicSharedContext& c,
    const StrategicActionNativeSnapshot& s, const std::string& id = "rec-1",
    std::uint64_t expected_sequence = 5) {
    StrategicActionResolutionRequest request;
    request.recommendation_id = id;
    request.expected_snapshot_sequence = expected_sequence;
    request.recommendation = &r; request.source_context = &c; request.current_state = &s;
    return executor.resolve(request);
}
void buy_resolves_shop_slot_and_full_native_vector() {
    auto s = native_state();
    s.shop_champion_ids[3] = 42;
    s.masks.type_mask[0] = 1; s.masks.shop_mask[3] = 1;
    auto c = source_context(StrategicActionKind::BuyUnit, 42);
    auto r = recommendation(StrategicActionKind::BuyUnit, 42);
    StrategicActionExecutor executor;
    const auto result = resolve(executor, r, c, s);
    assert(result.accepted);
    assert((result.native_action.values == std::array<std::int32_t, 6>{0,3,0,0,0,0}));
    assert(result.shadow_only && !result.execution_attempted);
    assert(result.execution_status == "not_attempted_shadow_only");
}
void buy_rejects_missing_shop_offer_or_disabled_masks() {
    auto s = native_state();
    s.shop_champion_ids[2] = 42; s.masks.type_mask[0] = 1;
    auto c = source_context(StrategicActionKind::BuyUnit, 42);
    auto r = recommendation(StrategicActionKind::BuyUnit, 42);
    StrategicActionExecutor executor;
    auto result = resolve(executor, r, c, s);
    assert(!result.accepted && result.validation_reason == "native_shop_mask_rejected");
    s.masks.shop_mask[2] = 1; s.masks.type_mask[0] = 0;
    StrategicActionExecutor second;
    result = resolve(second, r, c, s);
    assert(!result.accepted && result.validation_reason == "native_type_mask_rejected");
}
void reroll_xp_and_hold_resolve_only_when_type_mask_allows() {
    for (const auto kind_type : {
        std::pair<StrategicActionKind, std::int32_t>{StrategicActionKind::RerollShop,1},
        {StrategicActionKind::BuyExperience,2},
        {StrategicActionKind::Hold,6}}) {
        auto s = native_state(); s.masks.type_mask[static_cast<std::size_t>(kind_type.second)] = 1;
        auto c = source_context(kind_type.first);
        auto r = recommendation(kind_type.first);
        StrategicActionExecutor executor;
        const auto result = resolve(executor, r, c, s);
        assert(result.accepted);
        assert(result.native_action.values[0] == kind_type.second);
        for (std::size_t i=1;i<6;++i) assert(result.native_action.values[i] == 0);
    }
}
void sell_requires_one_legal_bench_instance() {
    auto s = native_state();
    s.bench_champion_ids[4] = 51;
    s.masks.type_mask[5] = 1; s.masks.bench_source_mask[4] = 1;
    auto c = source_context(StrategicActionKind::SellUnit, 51);
    auto r = recommendation(StrategicActionKind::SellUnit, 51);
    StrategicActionExecutor executor;
    auto result = resolve(executor, r, c, s);
    assert(result.accepted);
    assert((result.native_action.values == std::array<std::int32_t,6>{5,0,4,0,0,0}));

    s.bench_champion_ids[5] = 51; s.masks.bench_source_mask[5] = 1;
    StrategicActionExecutor ambiguous_executor;
    result = resolve(ambiguous_executor, r, c, s);
    assert(!result.accepted && result.validation_reason == "ambiguous_unit_instance");
}
void sell_does_not_resolve_board_only_unit() {
    auto s = native_state(); s.board_champion_ids[6] = 51; s.masks.type_mask[5] = 1;
    auto c = source_context(StrategicActionKind::SellUnit, 51);
    auto r = recommendation(StrategicActionKind::SellUnit, 51);
    StrategicActionExecutor executor;
    const auto result = resolve(executor, r, c, s);
    assert(!result.accepted && result.validation_reason == "native_bench_mask_rejected");
}
void movement_requires_explicit_target_and_conditioned_native_mask() {
    auto s = native_state(); s.bench_champion_ids[2] = 77;
    s.masks.type_mask[3] = 1;
    s.masks.bench_to_board_target_masks[2 * 28 + 9] = 1;
    auto c = source_context(StrategicActionKind::DeployOrMove, 77);
    auto r = recommendation(StrategicActionKind::DeployOrMove, 77);
    StrategicActionExecutor missing_target;
    auto result = resolve(missing_target, r, c, s);
    assert(!result.accepted && result.validation_reason == "move_intent_unresolved");

    s.requested_move_targets.push_back({77,9});
    StrategicActionExecutor valid_executor;
    result = resolve(valid_executor, r, c, s, "move-rec");
    assert(result.accepted);
    assert((result.native_action.values == std::array<std::int32_t,6>{3,0,2,9,0,0}));

    s.masks.bench_to_board_target_masks[2 * 28 + 9] = 0;
    StrategicActionExecutor blocked_executor;
    result = resolve(blocked_executor, r, c, s, "blocked-move");
    assert(!result.accepted && result.validation_reason == "native_move_mask_rejected");

    s.masks.bench_to_board_target_masks[2 * 28 + 9] = 1;
    s.board_champion_ids[4] = 77;
    StrategicActionExecutor ambiguous_zone_executor;
    result = resolve(ambiguous_zone_executor, r, c, s, "ambiguous-zone");
    assert(!result.accepted && result.validation_reason == "ambiguous_unit_instance");
}
void board_move_uses_exact_source_and_destination_mask() {
    auto s = native_state(); s.board_champion_ids[12] = 77;
    s.masks.type_mask[4] = 1;
    s.masks.board_move_target_masks[12 * 28 + 15] = 1;
    s.requested_move_targets.push_back({77,15});
    auto c = source_context(StrategicActionKind::DeployOrMove,77);
    auto r = recommendation(StrategicActionKind::DeployOrMove,77);
    StrategicActionExecutor executor;
    const auto result = resolve(executor,r,c,s);
    assert(result.accepted);
    assert((result.native_action.values == std::array<std::int32_t,6>{4,0,0,0,12,15}));
}
void unavailable_native_mask_generation_is_rejected_explicitly() {
    auto s = native_state();
    s.mask_generation_error = "invalid_economy_snapshot";
    auto c = source_context(StrategicActionKind::RerollShop);
    auto r = recommendation(StrategicActionKind::RerollShop);
    StrategicActionExecutor executor;
    const auto result = resolve(executor, r, c, s, "mask-error");
    assert(!result.accepted);
    assert(result.validation_reason == "native_legality_unavailable");
    assert(result.resolution_reason.find("native_mask_generation_failed") != std::string::npos);
}

void recommendation_summary_must_match_selected_candidate() {
    auto s = native_state(); s.masks.type_mask[1] = 1;
    auto c = source_context(StrategicActionKind::RerollShop);
    auto r = recommendation(StrategicActionKind::RerollShop);
    r.recommended_action = StrategicActionKind::BuyExperience;
    StrategicActionExecutor executor;
    const auto result = resolve(executor, r, c, s, "tampered-summary");
    assert(!result.accepted);
    assert(result.validation_reason == "recommendation_integrity_mismatch");
}

void stale_context_and_sequence_are_rejected() {
    auto s = native_state(); s.masks.type_mask[1] = 1;
    auto c = source_context(StrategicActionKind::RerollShop);
    auto r = recommendation(StrategicActionKind::RerollShop);
    StrategicActionExecutor stale_sequence;
    auto result = resolve(stale_sequence,r,c,s,"stale",4);
    assert(!result.accepted && result.validation_reason == "stale_native_snapshot");

    StrategicActionExecutor stale_identity;
    auto wrong = s; wrong.player_id = 1;
    result = resolve(stale_identity,r,c,wrong,"wrong-player");
    assert(!result.accepted && result.validation_reason == "stale_or_incompatible_context");
}
void recommendation_idempotency_is_scoped_by_match_and_player() {
    auto s = native_state(); s.masks.type_mask[1] = 1;
    auto c = source_context(StrategicActionKind::RerollShop);
    auto r = recommendation(StrategicActionKind::RerollShop);
    StrategicActionExecutor executor;
    auto first = resolve(executor,r,c,s,"same-id");
    auto duplicate = resolve(executor,r,c,s,"same-id");
    assert(first.accepted);
    assert(!duplicate.accepted && duplicate.validation_reason == "duplicate_recommendation");

    auto other_player_state = s; other_player_state.player_id = 1;
    auto other_context = c; other_context.player_id = 1;
    auto other_recommendation = r; other_recommendation.player_id = 1;
    const auto isolated = resolve(executor,other_recommendation,other_context,
        other_player_state,"same-id");
    assert(isolated.accepted);
}
void missing_candidate_and_unsupported_intent_are_rejected() {
    auto s = native_state(); s.masks.type_mask[6] = 1;
    auto c = source_context(StrategicActionKind::Hold);
    auto r = recommendation(StrategicActionKind::Hold);
    c.action_candidates.clear();
    StrategicActionExecutor missing;
    auto result = resolve(missing,r,c,s,"missing");
    assert(!result.accepted && result.validation_reason == "source_candidate_mismatch");

    auto unsupported_context = source_context(StrategicActionKind::None);
    auto unsupported_recommendation = recommendation(StrategicActionKind::None);
    StrategicActionExecutor unsupported;
    result = resolve(unsupported,unsupported_recommendation,unsupported_context,s,"unsupported");
    assert(!result.accepted && result.validation_reason == "unsupported_semantic_action");
}
void failed_resolution_is_audited_without_execution() {
    auto s = native_state();
    auto c = source_context(StrategicActionKind::RerollShop);
    auto r = recommendation(StrategicActionKind::RerollShop);
    StrategicActionExecutor executor;
    const auto result = resolve(executor,r,c,s,"failed");
    const auto json = result.to_json();
    assert(json["execution"]["attempted"] == false);
    assert(json["execution"]["status"] == "not_attempted_shadow_only");
    assert(json["shadow_only"] == true);
    assert(json["resolution"]["accepted"] == false);
    for (const auto value : result.native_action.values) assert(value == -1);
}
}

int main() {
    buy_resolves_shop_slot_and_full_native_vector();
    buy_rejects_missing_shop_offer_or_disabled_masks();
    reroll_xp_and_hold_resolve_only_when_type_mask_allows();
    sell_requires_one_legal_bench_instance();
    sell_does_not_resolve_board_only_unit();
    movement_requires_explicit_target_and_conditioned_native_mask();
    board_move_uses_exact_source_and_destination_mask();
    stale_context_and_sequence_are_rejected();
    unavailable_native_mask_generation_is_rejected_explicitly();
    recommendation_summary_must_match_selected_candidate();
    recommendation_idempotency_is_scoped_by_match_and_player();
    missing_candidate_and_unsupported_intent_are_rejected();
    failed_resolution_is_audited_without_execution();
    std::cout << "StrategicActionExecutor tests passed\\n";
}
