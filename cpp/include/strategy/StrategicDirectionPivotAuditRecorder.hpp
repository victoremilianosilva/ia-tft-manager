#pragma once

// Best-effort, read-only JSONL recorder for the unified strategic shadow cycle.
// It observes value snapshots only; it never calls back into or mutates the planner.

#include "strategy/UnifiedStrategicStateMachine.hpp"

#include <nlohmann/json.hpp>

#include <cstdint>
#include <filesystem>
#include <fstream>
#include <map>
#include <mutex>
#include <string>
#include <utility>

namespace tft::strategy {

struct StrategicCycleAuditContext {
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
};

class StrategicDirectionPivotAuditRecorder {
public:
    explicit StrategicDirectionPivotAuditRecorder(std::filesystem::path output)
        : output_(std::move(output)) {}

    // Returns false on invalid context or any I/O/serialization failure.
    // All failures are contained so callers can safely invoke this from Shadow.
    bool append(const StrategicCycleAuditContext& context,
                const StrategicCycleInput& input,
                const StrategicCycleResult& result) noexcept {
        try {
            if (context.player_id < 0 || context.match_id == 0) return false;
            std::lock_guard<std::mutex> lock(mutex_);
            const auto next_sequence = sequences_[context.player_id] + 1;
            const auto record = make_record(context, input, result, next_sequence);
            auto fingerprint_record = record;
            fingerprint_record.erase("sequence");
            const auto fingerprint = fingerprint_record.dump();
            const auto previous = last_fingerprints_.find(context.player_id);
            if (previous != last_fingerprints_.end() && previous->second == fingerprint)
                return false;
            if (!output_.parent_path().empty())
                std::filesystem::create_directories(output_.parent_path());
            std::ofstream stream(output_, std::ios::out | std::ios::app);
            if (!stream.is_open()) return false;
            stream << record.dump() << '\n';
            stream.flush();
            if (!stream.good()) return false;
            sequences_[context.player_id] = next_sequence;
            last_fingerprints_[context.player_id] = fingerprint;
            return true;
        } catch (...) {
            return false;
        }
    }

    const std::filesystem::path& output_path() const noexcept { return output_; }

    void reset_session() noexcept {
        try {
            std::lock_guard<std::mutex> lock(mutex_);
            sequences_.clear();
            last_fingerprints_.clear();
        } catch (...) {
        }
    }

private:
    static const char* lifecycle_name(StrategicAnchorLifecycle value) {
        switch (value) {
            case StrategicAnchorLifecycle::Empty: return "EMPTY";
            case StrategicAnchorLifecycle::Proposed: return "PROPOSED";
            case StrategicAnchorLifecycle::Active: return "ACTIVE";
            case StrategicAnchorLifecycle::Evaluating: return "EVALUATING";
            case StrategicAnchorLifecycle::Confirmed: return "CONFIRMED";
            case StrategicAnchorLifecycle::Rejected: return "REJECTED";
            case StrategicAnchorLifecycle::Invalidated: return "INVALIDATED";
        }
        return "UNKNOWN";
    }

    static const char* phase_name(StrategicCyclePhase value) {
        switch (value) {
            case StrategicCyclePhase::Exploration: return "EXPLORATION";
            case StrategicCyclePhase::CompositionActive: return "COMPOSITION_ACTIVE";
            case StrategicCyclePhase::PivotEvaluation: return "PIVOT_EVALUATION";
            case StrategicCyclePhase::PivotConfirmed: return "PIVOT_CONFIRMED";
            case StrategicCyclePhase::NoEvidence: return "NO_EVIDENCE";
            case StrategicCyclePhase::Invalidated: return "INVALIDATED";
        }
        return "UNKNOWN";
    }

    static const char* feasibility_status(PivotFeasibilityStatus value) {
        switch (value) {
            case PivotFeasibilityStatus::InsufficientEvidence: return "INSUFFICIENT_EVIDENCE";
            case PivotFeasibilityStatus::Rejected: return "REJECTED";
            case PivotFeasibilityStatus::Viable: return "VIABLE";
        }
        return "UNKNOWN";
    }

    static nlohmann::json make_record(const StrategicCycleAuditContext& context,
                                      const StrategicCycleInput& input,
                                      const StrategicCycleResult& result,
                                      std::uint64_t sequence) {
        nlohmann::json active = nullptr;
        if (result.active_composition) {
            active = {
                {"identity", result.active_composition->candidate.composition_id},
                {"version", result.active_composition->version}
            };
        }

        const auto& direction = result.anchors.direction_anchor;
        nlohmann::json direction_json = nullptr;
        if (!direction.identity.empty()) {
            direction_json = {
                {"identity", direction.identity},
                {"composition_identity", direction.composition_identity},
                {"composition_version", direction.composition_version},
                {"lifecycle", lifecycle_name(direction.lifecycle)},
                {"unit_ids", direction.reference_unit_ids},
                {"direction", direction.direction},
                {"reason", direction.reason}
            };
        }

        const auto& pivot = result.anchors.pivot_candidate;
        nlohmann::json pivot_json = nullptr;
        if (!pivot.identity.empty()) {
            pivot_json = {
                {"identity", pivot.identity},
                {"target_composition_identity", pivot.target_composition_identity},
                {"source_direction_anchor_identity", pivot.source_direction_anchor_identity},
                {"source_composition_version", pivot.source_composition_version},
                {"lifecycle", lifecycle_name(pivot.lifecycle)},
                {"unit_ids", pivot.reference_unit_ids},
                {"reason", pivot.reason}
            };
        }

        nlohmann::json support = nlohmann::json::array();
        nlohmann::json shop = nlohmann::json::array();
        nlohmann::json carry = {
            {"eligible", nullptr},
            {"champion_id", nullptr},
            {"cost", nullptr},
            {"star", nullptr},
            {"reason", "carry_evidence_unavailable"}
        };
        nlohmann::json feasibility = {
            {"status", "UNAVAILABLE"},
            {"reason", result.diagnostics.transition_reason},
            {"blockers", nlohmann::json::array()},
            {"missing_data", nlohmann::json::array()}
        };

        if (!input.pivot_feasibility) {
            for (const auto& unit : input.exploration.units) {
                support.push_back({
                    {"champion_id", unit.champion_id},
                    {"relation", unit.core_potential ? "core" : "composition"},
                    {"copies_owned", unit.copies_owned},
                    {"highest_star", unit.star},
                    {"target_star", 2},
                    {"cost", unit.cost},
                    {"on_board", unit.on_board},
                    {"on_bench", unit.on_bench},
                    {"in_shop", unit.in_shop},
                    {"carry_potential", unit.carry_potential},
                    {"core_potential", unit.core_potential},
                    {"traits", unit.traits}
                });
                if (unit.in_shop) {
                    shop.push_back({
                        {"champion_id", unit.champion_id},
                        {"cost", unit.cost},
                        {"copies", 1},
                        {"source_sequence", input.evaluation_sequence}
                    });
                }
            }
        }

        if (input.pivot_feasibility) {
            const auto& evidence = *input.pivot_feasibility;
            const auto* evaluated = result.diagnostics.pivot_feasibility
                ? &*result.diagnostics.pivot_feasibility : nullptr;
            std::map<std::int32_t, PivotObservedUnit> observed;
            for (const auto& unit : evidence.observed_units)
                observed.emplace(unit.champion_id, unit);

            for (const auto& required : evidence.required_units) {
                const auto found = observed.find(required.champion_id);
                const auto owned = found == observed.end() ? 0 : found->second.owned_copies;
                const auto star = found == observed.end() ? 1 : found->second.star;
                const auto shop_copies = found == observed.end() ? 0 : found->second.shop_copies;
                support.push_back({
                    {"champion_id", required.champion_id},
                    {"relation", required.core ? "core" : "composition"},
                    {"copies_owned", owned},
                    {"highest_star", star},
                    {"target_star", 2},
                    {"cost", required.cost},
                    {"core", required.core},
                    {"carry", required.carry}
                });
                if (shop_copies > 0) {
                    shop.push_back({
                        {"champion_id", required.champion_id},
                        {"cost", required.cost},
                        {"copies", shop_copies},
                        {"source_sequence", input.evaluation_sequence}
                    });
                }
                if (required.carry) {
                    const bool eligible = star >= 2 || required.cost == 4 || required.cost == 5;
                    carry = {
                        {"eligible", eligible},
                        {"champion_id", required.champion_id},
                        {"cost", required.cost},
                        {"star", star},
                        {"reason", star >= 2 ? "carry_already_two_star"
                            : (required.cost >= 4 ? "carry_cost_four_or_five"
                                                  : "carry_below_two_star_and_cost_four")}
                    };
                }
            }

            if (evaluated) {
                feasibility = {
                    {"status", feasibility_status(evaluated->status)},
                    {"reason", evaluated->reason},
                    {"blockers", evaluated->blockers},
                    {"missing_data", evaluated->missing_data},
                    {"favorable_evidence", evaluated->favorable_evidence},
                    {"score", evaluated->score}
                };
                carry["eligible"] = evaluated->carry_eligible;
            } else {
                feasibility["missing_data"].push_back("pivot_evaluation_result_unavailable");
            }
        } else if (result.phase == StrategicCyclePhase::NoEvidence) {
            feasibility["status"] = "INSUFFICIENT_EVIDENCE";
            feasibility["missing_data"].push_back("pivot_feasibility_snapshot_unavailable");
        }

        nlohmann::json transition = nullptr;
        if (result.diagnostics.pivot_confirmation &&
            result.diagnostics.pivot_confirmation->status == PivotConfirmationStatus::Confirmed &&
            result.diagnostics.pivot_confirmation->state_changed &&
            result.active_composition.has_value() &&
            !result.anchors.direction_anchor.identity.empty()) {
            transition = {
                {"source_direction_anchor_identity",
                    input.pivot_candidate ? input.pivot_candidate->source_direction_anchor_identity : ""},
                {"destination_direction_anchor_identity", result.anchors.direction_anchor.identity},
                {"previous_composition_identity", input.active_composition
                    ? nlohmann::json(input.active_composition->candidate.composition_id)
                    : nlohmann::json(nullptr)},
                {"previous_composition_version", input.pivot_candidate
                    ? nlohmann::json(input.pivot_candidate->source_composition_version)
                    : nlohmann::json(nullptr)},
                {"destination_composition_identity", result.anchors.direction_anchor.composition_identity},
                {"new_composition_version", result.anchors.direction_anchor.composition_version},
                {"evaluation_sequence", input.evaluation_sequence}
            };
        }

        return {
            {"schema_version", 1},
            {"match_id", context.match_id},
            {"sequence", sequence},
            {"player_id", context.player_id},
            {"round", context.round ? context.round :
                (input.exploration.round ? input.exploration.round : 0)},
            {"phase", phase_name(result.phase)},
            {"observed_context", {
                {"gold_available", input.exploration.gold_available},
                {"evaluation_sequence", input.evaluation_sequence}
            }},
            {"active_composition", active},
            {"direction_anchor", direction_json},
            {"pivot_candidate", pivot_json},
            {"unit_support", support},
            {"shop_evidence", shop},
            {"carry_gate", carry},
            {"feasibility", feasibility},
            {"transition", transition},
            {"reason", result.diagnostics.transition_reason},
            {"shadow_only", true}
        };
    }

    std::filesystem::path output_;
    std::mutex mutex_;
    std::map<std::int32_t, std::uint64_t> sequences_;
    std::map<std::int32_t, std::string> last_fingerprints_;
};

} // namespace tft::strategy
