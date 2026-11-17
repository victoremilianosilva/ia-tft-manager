#pragma once

#include "strategy/StrategicDirectionPivotAuditRecorder.hpp"

#include <optional>
#include <string>
#include <utility>

namespace tft::strategy {

// Session-scoped entry point for callers that own the unified shadow planner.
// The recorder observes the returned value only; recording failure never
// changes the strategic result or propagates to the game/runtime caller.
class UnifiedStrategicShadowRuntime {
public:
    explicit UnifiedStrategicShadowRuntime(std::filesystem::path audit_path,
                                            PivotConfirmationPolicy policy = {})
        : machine_(policy), recorder_(std::move(audit_path)) {}

    StrategicCycleResult refresh(const StrategicCycleAuditContext& context,
                                 const StrategicCycleInput& input) noexcept {
        try {
            const auto fingerprint = input_fingerprint(context, input);
            if (last_result_ && last_player_id_ == context.player_id &&
                last_input_fingerprint_ == fingerprint) {
                // Do not advance pivot hysteresis for an unchanged observation.
                return *last_result_;
            }

            auto result = machine_.refresh(input);
            last_player_id_ = context.player_id;
            last_input_fingerprint_ = fingerprint;
            last_result_ = result;
            (void)recorder_.append(context, input, result);
            return result;
        } catch (...) {
            // The strategic shadow cycle is isolated from the caller as well.
            StrategicCycleResult result;
            result.phase = StrategicCyclePhase::NoEvidence;
            result.diagnostics.transition_reason = "shadow_cycle_exception_contained";
            result.shadow_only = true;
            return result;
        }
    }

    void reset_machine() noexcept {
        machine_ = UnifiedStrategicStateMachine{};
        last_player_id_ = -1;
        last_input_fingerprint_.clear();
        last_result_.reset();
    }

    void reset_session() noexcept {
        recorder_.reset_session();
        reset_machine();
    }

    const UnifiedStrategicStateMachine& machine() const noexcept { return machine_; }

private:
    static nlohmann::json composition_fingerprint(
        const composition_intelligence::CompositionCandidate& candidate
    ) {
        nlohmann::json units = nlohmann::json::array();
        for (const auto& unit : candidate.units) {
            units.push_back({
                {"champion_id", unit.champion_id},
                {"core", unit.core},
                {"priority", unit.priority}
            });
        }
        return {
            {"composition_id", candidate.composition_id},
            {"source", static_cast<std::int32_t>(candidate.source)},
            {"set_id", candidate.set_id},
            {"patch", candidate.patch},
            {"units", std::move(units)},
            {"main_carry_id", candidate.main_carry_id},
            {"target_board_size", candidate.target_board_size},
            {"source_score", candidate.source_score},
            {"source_reference", candidate.source_reference}
        };
    }

    static std::string input_fingerprint(
        const StrategicCycleAuditContext& context,
        const StrategicCycleInput& input
    ) {
        nlohmann::json value = {
            {"match_id", context.match_id},
            {"player_id", context.player_id},
            {"round", context.round},
            {"exploration", {
                {"round", input.exploration.round},
                {"gold_available", input.exploration.gold_available},
                {"composition_defined", input.exploration.composition_defined},
                {"active_composition_identity", input.exploration.active_composition_identity},
                {"previous_direction", input.exploration.previous_direction},
                {"maximum_hypotheses", input.exploration.maximum_hypotheses}
            }}
        };

        auto& exploration = value["exploration"];
        exploration["units"] = nlohmann::json::array();
        for (const auto& unit : input.exploration.units) {
            exploration["units"].push_back({
                {"champion_id", unit.champion_id},
                {"cost", unit.cost},
                {"copies_owned", unit.copies_owned},
                {"star", unit.star},
                {"pool_remaining", unit.pool_remaining},
                {"on_board", unit.on_board},
                {"on_bench", unit.on_bench},
                {"in_shop", unit.in_shop},
                {"carry_potential", unit.carry_potential},
                {"core_potential", unit.core_potential},
                {"board_contribution", unit.board_contribution},
                {"traits", unit.traits}
            });
        }
        exploration["trait_thresholds"] = nlohmann::json::array();
        for (const auto& trait : input.exploration.trait_thresholds) {
            exploration["trait_thresholds"].push_back({
                {"trait", trait.trait},
                {"activation_threshold", trait.activation_threshold}
            });
        }

        value["active_composition"] = input.active_composition
            ? composition_fingerprint(input.active_composition->candidate)
            : nlohmann::json(nullptr);
        if (input.active_composition)
            value["active_composition_version"] = input.active_composition->version;

        value["initial_composition_candidate"] = input.initial_composition_candidate
            ? composition_fingerprint(*input.initial_composition_candidate)
            : nlohmann::json(nullptr);

        if (input.pivot_candidate) {
            value["pivot_candidate"] = {
                {"identity", input.pivot_candidate->identity},
                {"target_direction", input.pivot_candidate->target_direction},
                {"target_composition_identity", input.pivot_candidate->target_composition_identity},
                {"source_direction_anchor_identity", input.pivot_candidate->source_direction_anchor_identity},
                {"source_composition_version", input.pivot_candidate->source_composition_version},
                {"reference_unit_ids", input.pivot_candidate->reference_unit_ids},
                {"evidence", nlohmann::json::array()},
                {"confidence", input.pivot_candidate->confidence},
                {"reason", input.pivot_candidate->reason},
                {"lifecycle", static_cast<std::int32_t>(input.pivot_candidate->lifecycle)}
            };
            for (const auto evidence : input.pivot_candidate->evidence)
                value["pivot_candidate"]["evidence"].push_back(
                    static_cast<std::int32_t>(evidence));
        } else {
            value["pivot_candidate"] = nullptr;
        }

        value["pivot_destination"] = input.pivot_destination
            ? composition_fingerprint(*input.pivot_destination)
            : nlohmann::json(nullptr);

        if (input.pivot_feasibility) {
            const auto& feasibility = *input.pivot_feasibility;
            value["pivot_feasibility"] = {
                {"candidate_composition_identity", feasibility.candidate_composition_identity},
                {"source_direction_anchor_identity", feasibility.source_direction_anchor_identity},
                {"source_composition_version", feasibility.source_composition_version},
                {"gold_available", feasibility.gold_available},
                {"protected_gold_floor", feasibility.protected_gold_floor},
                {"transition_economic_cost", feasibility.transition_economic_cost},
                {"required_units", nlohmann::json::array()},
                {"observed_units", nlohmann::json::array()},
                {"required_traits", nlohmann::json::array()}
            };
            for (const auto& unit : feasibility.required_units) {
                value["pivot_feasibility"]["required_units"].push_back({
                    {"champion_id", unit.champion_id},
                    {"cost", unit.cost},
                    {"core", unit.core},
                    {"carry", unit.carry},
                    {"traits", unit.traits}
                });
            }
            for (const auto& unit : feasibility.observed_units) {
                value["pivot_feasibility"]["observed_units"].push_back({
                    {"champion_id", unit.champion_id},
                    {"owned_copies", unit.owned_copies},
                    {"star", unit.star},
                    {"shop_copies", unit.shop_copies},
                    {"pool_remaining", unit.pool_remaining}
                });
            }
            for (const auto& trait : feasibility.required_traits) {
                value["pivot_feasibility"]["required_traits"].push_back({
                    {"trait", trait.trait},
                    {"minimum_units", trait.minimum_units}
                });
            }
        } else {
            value["pivot_feasibility"] = nullptr;
        }

        // Emission sequence is deliberately excluded. It identifies recorder
        // order, not a new strategic observation.
        return value.dump();
    }

    UnifiedStrategicStateMachine machine_;
    StrategicDirectionPivotAuditRecorder recorder_;
    std::int32_t last_player_id_{-1};
    std::string last_input_fingerprint_;
    std::optional<StrategicCycleResult> last_result_;
};

} // namespace tft::strategy
