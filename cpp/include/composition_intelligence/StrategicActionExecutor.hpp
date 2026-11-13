#pragma once

#include "composition_intelligence/ContextualActionEvaluator.hpp"
#include "decision/DecisionTypes.hpp"
#include "lobby/TftEngine.hpp"

#include <algorithm>
#include <array>
#include <cstdint>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>
#include <nlohmann/json.hpp>

namespace tft::composition_intelligence {

enum class StrategicActionUnitZone : std::uint8_t { Bench = 0, Board = 1 };

struct StrategicActionMoveTarget {
    std::int32_t champion_id{-1};
    std::int32_t target_board_slot{-1};
};

struct StrategicActionNativeSnapshot {
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    std::string composition_id;
    std::uint64_t composition_version{0};
    std::int32_t gold{-1};
    bool alive{false};
    std::array<std::int32_t, decision::SHOP_SIZE> shop_champion_ids{};
    std::array<std::int32_t, decision::BENCH_SIZE> bench_champion_ids{};
    std::array<std::int32_t, decision::BOARD_SIZE> board_champion_ids{};
    PlayerActionMasks masks{};
    std::vector<StrategicActionMoveTarget> requested_move_targets;
};

struct StrategicActionResolutionRequest {
    std::string recommendation_id;
    std::uint64_t expected_snapshot_sequence{0};
    const ContextualActionEvaluation* recommendation{nullptr};
    const strategy::StrategicSharedContext* source_context{nullptr};
    const StrategicActionNativeSnapshot* current_state{nullptr};
};

struct StrategicActionResolution {
    std::uint32_t schema_version{1};
    std::string recommendation_id;
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t source_sequence{0};
    std::string composition_id;
    std::uint64_t composition_version{0};
    strategy::StrategicActionKind recommended_kind{strategy::StrategicActionKind::None};
    std::int32_t recommended_champion_id{-1};
    std::size_t candidate_index{0};
    bool accepted{false};
    std::string resolution_reason{"not_evaluated"};
    std::string validation_reason{"not_validated"};
    PlayerAction native_action{};
    bool shadow_only{true};
    bool execution_attempted{false};
    std::string execution_status{"not_attempted_shadow_only"};

    nlohmann::json to_json() const {
        return {
            {"schema_version", schema_version},
            {"recommendation", {
                {"id", recommendation_id},
                {"kind", static_cast<int>(recommended_kind)},
                {"champion_id", recommended_champion_id},
                {"candidate_index", candidate_index}
            }},
            {"identity", {
                {"match_id", match_id}, {"player_id", player_id},
                {"round", round}, {"source_sequence", source_sequence},
                {"composition_id", composition_id},
                {"composition_version", composition_version}
            }},
            {"resolution", {{"accepted", accepted}, {"reason", resolution_reason}}},
            {"validation", {{"reason", validation_reason},
                {"native_action", native_action.values}}},
            {"execution", {{"attempted", execution_attempted},
                {"status", execution_status}}},
            {"shadow_only", shadow_only}
        };
    }
};

// Resolves only into the existing six-component native action vector.
// It never applies an action to TFTEngine and has no route to mutate game state.
class StrategicActionExecutor {
public:
    StrategicActionResolution resolve(const StrategicActionResolutionRequest& request) {
        StrategicActionResolution out;
        out.recommendation_id = request.recommendation_id;
        if (!request.recommendation || !request.source_context || !request.current_state)
            return reject(std::move(out), "missing_resolution_input", "missing_required_input");

        const auto& recommendation = *request.recommendation;
        const auto& source = *request.source_context;
        const auto& state = *request.current_state;
        out.match_id = state.match_id;
        out.player_id = state.player_id;
        out.round = state.round;
        out.source_sequence = state.sequence;
        out.composition_id = state.composition_id;
        out.composition_version = state.composition_version;

        if (request.recommendation_id.empty())
            return reject(std::move(out), "recommendation_id_missing", "not_validated");
        if (recommendation.stale)
            return reject(std::move(out), "recommendation_stale:" + recommendation.stale_reason, "stale_recommendation");
        if (!state.alive)
            return reject(std::move(out), "player_not_alive", "player_not_alive");
        if (state.sequence == 0 || request.expected_snapshot_sequence == 0 ||
            state.sequence != request.expected_snapshot_sequence)
            return reject(std::move(out), "native_snapshot_sequence_mismatch", "stale_native_snapshot");
        if (recommendation.match_id != state.match_id || source.player_id != state.player_id ||
            recommendation.player_id != state.player_id || recommendation.round != state.round ||
            source.round != state.round || recommendation.composition_id != state.composition_id ||
            recommendation.composition_version != state.composition_version)
            return reject(std::move(out), "recommendation_context_identity_mismatch", "stale_or_incompatible_context");
        if (state.gold < 0 || source.gold != state.gold)
            return reject(std::move(out), "gold_evidence_missing_or_mismatched", "incomplete_native_state");

        const ContextualActionCandidateScore* selected = nullptr;
        for (const auto& candidate : recommendation.candidates) {
            if (!candidate.selected) continue;
            if (selected) return reject(std::move(out), "multiple_selected_candidates", "ambiguous_recommendation");
            selected = &candidate;
        }
        if (!selected || !selected->eligible)
            return reject(std::move(out), "no_eligible_selected_candidate", "recommendation_not_accepted");
        if (selected->candidate_index >= source.action_candidates.size())
            return reject(std::move(out), "candidate_index_out_of_range", "source_candidate_mismatch");
        const auto& source_candidate = source.action_candidates[selected->candidate_index];
        if (source_candidate.kind != selected->kind ||
            source_candidate.champion_id != selected->champion_id)
            return reject(std::move(out), "selected_candidate_does_not_match_source", "source_candidate_mismatch");

        out.recommended_kind = selected->kind;
        out.recommended_champion_id = selected->champion_id;
        out.candidate_index = selected->candidate_index;

        const auto idempotency_key = std::to_string(state.match_id) + ":" +
            std::to_string(state.player_id) + ":" + request.recommendation_id;
        if (!consumed_recommendations_.insert(idempotency_key).second)
            return reject(std::move(out), "recommendation_already_resolved", "duplicate_recommendation");

        auto action = PlayerAction{};
        auto& values = action.values;
        const auto type_enabled = [&](decision::ActionType type) {
            return state.masks.type_mask[static_cast<std::size_t>(type)] == decision::MASK_ENABLED;
        };
        switch (selected->kind) {
            case strategy::StrategicActionKind::Hold:
                if (!type_enabled(decision::ActionType::PASS))
                    return reject(std::move(out), "PASS_disabled_by_native_mask", "native_type_mask_rejected");
                values[0] = static_cast<std::int32_t>(decision::ActionType::PASS);
                break;
            case strategy::StrategicActionKind::BuyUnit: {
                if (!type_enabled(decision::ActionType::BUY))
                    return reject(std::move(out), "BUY_disabled_by_native_mask", "native_type_mask_rejected");
                std::int32_t slot = -1;
                for (std::size_t i = 0; i < state.shop_champion_ids.size(); ++i) {
                    if (state.shop_champion_ids[i] == selected->champion_id &&
                        state.masks.shop_mask[i] == decision::MASK_ENABLED) {
                        slot = static_cast<std::int32_t>(i);
                        break;
                    }
                }
                if (slot < 0)
                    return reject(std::move(out), "champion_not_in_legal_shop_slot", "native_shop_mask_rejected");
                values[0] = static_cast<std::int32_t>(decision::ActionType::BUY);
                values[1] = slot;
                break;
            }
            case strategy::StrategicActionKind::RerollShop:
                if (!type_enabled(decision::ActionType::REROLL))
                    return reject(std::move(out), "REROLL_disabled_by_native_mask", "native_type_mask_rejected");
                values[0] = static_cast<std::int32_t>(decision::ActionType::REROLL);
                break;
            case strategy::StrategicActionKind::BuyExperience:
                if (!type_enabled(decision::ActionType::BUY_XP))
                    return reject(std::move(out), "BUY_XP_disabled_by_native_mask", "native_type_mask_rejected");
                values[0] = static_cast<std::int32_t>(decision::ActionType::BUY_XP);
                break;
            case strategy::StrategicActionKind::SellUnit: {
                if (!type_enabled(decision::ActionType::SELL))
                    return reject(std::move(out), "SELL_disabled_by_native_mask", "native_type_mask_rejected");
                std::int32_t slot = -1;
                for (std::size_t i = 0; i < state.bench_champion_ids.size(); ++i) {
                    if (state.bench_champion_ids[i] == selected->champion_id &&
                        state.masks.bench_source_mask[i] == decision::MASK_ENABLED) {
                        if (slot >= 0)
                            return reject(std::move(out), "multiple_matching_bench_copies_require_explicit_instance", "ambiguous_unit_instance");
                        slot = static_cast<std::int32_t>(i);
                    }
                }
                if (slot < 0)
                    return reject(std::move(out), "sell_target_not_in_legal_bench_slot", "native_bench_mask_rejected");
                values[0] = static_cast<std::int32_t>(decision::ActionType::SELL);
                values[2] = slot;
                break;
            }
            case strategy::StrategicActionKind::DeployOrMove: {
                const auto target = std::find_if(state.requested_move_targets.begin(),
                    state.requested_move_targets.end(), [&](const auto& item) {
                        return item.champion_id == selected->champion_id;
                    });
                if (target == state.requested_move_targets.end())
                    return reject(std::move(out), "explicit_positioning_target_missing", "move_intent_unresolved");
                if (target->target_board_slot < 0 ||
                    target->target_board_slot >= static_cast<std::int32_t>(decision::BOARD_SIZE))
                    return reject(std::move(out), "positioning_target_out_of_range", "invalid_move_target");
                {
                    std::int32_t bench_slot = -1;
                    for (std::size_t i = 0; i < state.bench_champion_ids.size(); ++i)
                        if (state.bench_champion_ids[i] == selected->champion_id) {
                            if (bench_slot >= 0)
                                return reject(std::move(out), "multiple_bench_copies_require_explicit_instance", "ambiguous_unit_instance");
                            bench_slot = static_cast<std::int32_t>(i);
                        }
                    if (bench_slot >= 0) {
                        if (!type_enabled(decision::ActionType::MOVE_BENCH) ||
                            state.masks.bench_to_board_target_masks[
                                static_cast<std::size_t>(bench_slot) * decision::BOARD_SIZE +
                                static_cast<std::size_t>(target->target_board_slot)] != decision::MASK_ENABLED)
                            return reject(std::move(out), "bench_to_board_move_disabled_by_native_mask", "native_move_mask_rejected");
                        values[0] = static_cast<std::int32_t>(decision::ActionType::MOVE_BENCH);
                        values[2] = bench_slot;
                        values[3] = target->target_board_slot;
                        break;
                    }
                }
                {
                    std::int32_t board_slot = -1;
                    for (std::size_t i = 0; i < state.board_champion_ids.size(); ++i)
                        if (state.board_champion_ids[i] == selected->champion_id) {
                            if (board_slot >= 0)
                                return reject(std::move(out), "multiple_board_copies_require_explicit_instance", "ambiguous_unit_instance");
                            board_slot = static_cast<std::int32_t>(i);
                        }
                    if (board_slot < 0)
                        return reject(std::move(out), "move_unit_not_owned", "unit_not_found");
                    if (!type_enabled(decision::ActionType::MOVE_BOARD) ||
                        state.masks.board_move_target_masks[
                            static_cast<std::size_t>(board_slot) * decision::BOARD_SIZE +
                            static_cast<std::size_t>(target->target_board_slot)] != decision::MASK_ENABLED)
                        return reject(std::move(out), "board_move_disabled_by_native_mask", "native_move_mask_rejected");
                    values[0] = static_cast<std::int32_t>(decision::ActionType::MOVE_BOARD);
                    values[4] = board_slot;
                    values[5] = target->target_board_slot;
                }
                break;
            }
            case strategy::StrategicActionKind::None:
            default:
                return reject(std::move(out), "semantic_intent_has_no_native_resolution", "unsupported_semantic_action");
        }
        out.native_action = action;
        out.accepted = true;
        out.resolution_reason = "resolved_to_concrete_native_action";
        out.validation_reason = "accepted_by_current_native_type_and_parameter_masks";
        return out;
    }

private:
    static StrategicActionResolution reject(StrategicActionResolution out,
        std::string resolution_reason, std::string validation_reason) {
        out.accepted = false;
        out.resolution_reason = std::move(resolution_reason);
        out.validation_reason = std::move(validation_reason);
        out.native_action = PlayerAction{};
        return out;
    }

    std::unordered_set<std::string> consumed_recommendations_;

public:
    void reset() { consumed_recommendations_.clear(); }
};

} // namespace tft::composition_intelligence
