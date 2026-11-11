#pragma once

#include "composition_intelligence/CompositionActionEvaluator.hpp"
#include "composition_intelligence/PlannerEvidenceAdapters.hpp"
#include <nlohmann/json.hpp>
#include <cstdint>
#include <ostream>
#include <optional>
#include <string>
#include <vector>

namespace tft::composition_intelligence {

struct CompositionOutcomeObservation {
    std::uint32_t observed_round{0};
    std::int32_t placement{0};
    double health_delta{0.0};
    double board_score_delta{0.0};
    std::string note;
};

// Read-only, append-only diagnostic record. It is a Viewer/export contract,
// not a runtime controller and never feeds decisions back into the engine.
struct CompositionDiagnosticSnapshot {
    std::uint32_t schema_version{1};
    std::uint64_t sequence{0};
    std::uint32_t round{0};
    std::string composition_id;
    std::uint64_t composition_version{0};
    bool stale{false};
    std::string stale_reason;
    nlohmann::json payload;

    nlohmann::json to_json() const {
        return {
            {"schema_version", schema_version},
            {"sequence", sequence},
            {"round", round},
            {"composition_id", composition_id},
            {"composition_version", composition_version},
            {"stale", stale},
            {"stale_reason", stale_reason},
            {"classification", {
                {"observed", {"source_metadata", "economic_evidence", "board_evidence", "item_evidence",
                              "owned_units", "round", "outcome_observation"}},
                {"inferred", {"composition_decision", "transition_plan", "unit_intentions",
                              "lineup_plan", "action_recommendation"}},
                {"correlated", {"recommendation_to_later_outcome"}}
            }},
            {"diagnostics", payload}
        };
    }

    void write_jsonl(std::ostream& output) const {
        output << to_json().dump() << '\n';
    }
};

class CompositionDiagnosticRecorder {
public:
    CompositionDiagnosticSnapshot capture(
        std::uint32_t round,
        const std::optional<ActiveComposition>& active,
        const CompositionProposal& proposal,
        const UnitPrioritySnapshot& priorities,
        const LineupPlan& lineup,
        const PlannerEvidenceSnapshot& evidence,
        const CompositionActionEvaluation& actions,
        const std::optional<CompositionTransition>& published_transition = std::nullopt,
        const std::optional<CompositionOutcomeObservation>& outcome = std::nullopt) {
        CompositionDiagnosticSnapshot out;
        out.sequence = next_sequence_++;
        out.round = round;
        out.stale = priorities.stale || lineup.stale || actions.stale ||
            (active && (priorities.composition_id != active->candidate.composition_id ||
                        priorities.composition_version != active->version));
        if (priorities.stale) out.stale_reason = priorities.stale_reason;
        else if (lineup.stale) out.stale_reason = lineup.stale_reason;
        else if (actions.stale) out.stale_reason = actions.stale_reason;
        else if (out.stale) out.stale_reason = "diagnostic component identity/version mismatch";

        if (active) {
            out.composition_id = active->candidate.composition_id;
            out.composition_version = active->version;
        }
        auto& p = out.payload;
        p["source_metadata"] = nullptr;
        if (active) {
            const auto& c = active->candidate;
            p["source_metadata"] = {
                {"source", c.source == CompositionSource::Oppg ? "opgg" : "native"},
                {"source_reference", c.source_reference}, {"patch", c.patch},
                {"set_id", c.set_id}, {"source_score", c.source_score},
                {"unit_ids", ids(c.units)}
            };
        }
        p["composition_decision"] = {
            {"decision", decision_name(proposal.decision)}, {"reason", proposal.reason},
            {"approved", proposal.approved}, {"hysteresis_satisfied", proposal.hysteresis_satisfied},
            {"evidence_streak", proposal.evidence_streak},
            {"active_score", score_json(proposal.active_score)},
            {"target_score", score_json(proposal.target_score)}
        };
        p["transition_plan"] = {
            {"from", proposal.transition.from_composition_id},
            {"to", proposal.transition.to_composition_id},
            {"expected_active_version", proposal.transition.expected_active_version},
            {"shared_unit_ids", proposal.transition.shared_unit_ids},
            {"bridge_unit_ids", proposal.transition.bridge_unit_ids},
            {"replaceable_unit_ids", proposal.transition.replaceable_unit_ids},
            {"sell_candidate_unit_ids", proposal.transition.sell_candidate_unit_ids},
            {"item_risk_unit_ids", proposal.transition.item_risk_unit_ids},
            {"overlap_ratio", proposal.transition.overlap_ratio},
            {"estimated_gold_cost", proposal.transition.estimated_gold_cost},
            {"transition_cost", proposal.transition.transition_cost},
            {"strategic_advantage", proposal.transition.strategic_advantage},
            {"confidence_not_probability", proposal.transition.confidence}
        };
        if (published_transition) {
            p["published_transition"] = {
                {"previous_version", published_transition->previous_version},
                {"new_version", published_transition->new_version},
                {"previous_composition_id", published_transition->previous_composition_id},
                {"new_composition_id", published_transition->new_composition_id},
                {"reason", transition_reason_name(published_transition->reason)},
                {"shared_unit_ids", published_transition->shared_unit_ids},
                {"added_unit_ids", published_transition->added_unit_ids},
                {"removed_unit_ids", published_transition->removed_unit_ids},
                {"invalidates_previous_version", true}
            };
        } else p["published_transition"] = nullptr;

        p["unit_priority_evidence_consumption"] = {
            {"consumed", priorities.evidence_consumed},
            {"rejected", priorities.evidence_rejected}
        };
        p["unit_intentions"] = nlohmann::json::array();
        for (const auto& u : priorities.units) {
            nlohmann::json reasons = nlohmann::json::array();
            for (const auto& r : u.reasons)
                reasons.push_back({{"code", static_cast<int>(r.code)}, {"message", r.message}});
            p["unit_intentions"].push_back({
                {"champion_id", u.champion_id}, {"intent", intent_name(u.intent)},
                {"relation", relation_name(u.relation)}, {"priority", u.priority},
                {"confidence_not_probability", u.confidence},
                {"copies_owned", u.copies_owned}, {"highest_star", u.highest_star},
                {"target_star", u.target_star}, {"on_board", u.on_board},
                {"sale_restricted", u.sale_restricted},
                {"board_contribution", u.board_contribution},
                {"synergy_contribution", u.synergy_contribution}, {"reasons", reasons}
            });
        }
        p["lineup_plan"] = {
            {"composition_id", lineup.composition_id}, {"composition_version", lineup.composition_version},
            {"stale", lineup.stale}, {"stale_reason", lineup.stale_reason},
            {"level", lineup.level}, {"board_capacity", lineup.board_capacity},
            {"board_evidence", {{"available", lineup.board_evidence_available},
                {"reason", lineup.board_evidence_reason},
                {"frontline_count", lineup.observed_frontline_count},
                {"carry_count", lineup.observed_carry_count},
                {"exposed_carry_count", lineup.observed_exposed_carry_count},
                {"missing_frontline_count", lineup.observed_missing_frontline_count},
                {"missing_backline_count", lineup.observed_missing_backline_count}}},
            {"endgame_target_ids", lineup.endgame_target_ids},
            {"selected_board", lineup_json(lineup)},
            {"entries", lineup.entries}, {"exits", lineup.exits},
            {"deferred_target_ids", lineup.deferred_target_ids},
            {"bridge_ids", lineup.bridge_ids}, {"status", lineup.status}
        };
        p["evidence"] = evidence_json(evidence);
        p["action_recommendation"] = {
            {"stale", actions.stale}, {"stale_reason", actions.stale_reason},
            {"recommended_action", static_cast<int>(actions.evaluation.recommended_action)},
            {"recommended_champion_id", actions.evaluation.recommended_champion_id},
            {"confidence_not_probability", actions.evaluation.confidence},
            {"reason_code", static_cast<int>(actions.evaluation.reason)},
            {"shadow_only", actions.evaluation.shadow_only},
            {"evidence_consumption", {{"economy", actions.economy_evidence_consumed},
                {"board_validated", actions.board_evidence_validated},
                {"items", actions.item_evidence_consumed},
                {"gold", actions.observed_gold}, {"interest", actions.observed_interest},
                {"projected_next_round_income", actions.projected_next_round_income},
                {"economic_posture", actions.observed_economic_posture},
                {"rejected", actions.evidence_rejected}}},
            {"candidates", nlohmann::json::array()}
        };
        for (const auto& a : actions.candidates) {
            p["action_recommendation"]["candidates"].push_back({
                {"candidate_index", a.candidate_index}, {"kind", static_cast<int>(a.kind)},
                {"champion_id", a.champion_id},
                {"disposition", a.disposition == ActionCandidateDisposition::Accepted ? "accepted" : "rejected"},
                {"reason", a.reason}, {"selected", a.selected}
            });
        }
        if (outcome) {
            p["outcome_observation"] = {
                {"observed_round", outcome->observed_round}, {"placement", outcome->placement},
                {"health_delta", outcome->health_delta},
                {"board_score_delta", outcome->board_score_delta}, {"note", outcome->note},
                {"interpretation", "correlation_only_not_causation"}
            };
            p["recommendation_to_later_outcome"] = {
                {"recommendation_round", round}, {"outcome_round", outcome->observed_round},
                {"composition_version", out.composition_version},
                {"interpretation", "correlation_only_not_causation"}
            };
        } else {
            p["outcome_observation"] = nullptr;
            p["recommendation_to_later_outcome"] = nullptr;
        }
        return out;
    }

    std::uint64_t next_sequence() const noexcept { return next_sequence_; }

private:
    static std::vector<std::int32_t> ids(const std::vector<CompositionUnit>& units) {
        std::vector<std::int32_t> out;
        for (const auto& u : units) out.push_back(u.champion_id);
        return out;
    }
    static nlohmann::json score_json(const CompositionScoreBreakdown& s) {
        return {{"board_fit", s.board_fit}, {"ownership_fit", s.ownership_fit},
            {"item_fit", s.item_fit}, {"availability", s.availability},
            {"economy_feasibility", s.economy_feasibility}, {"total", s.total},
            {"confidence_not_probability", s.confidence}};
    }
    static std::string decision_name(CompositionDecision v) {
        switch(v) { case CompositionDecision::Keep:return "KEEP"; case CompositionDecision::Refine:return "REFINE";
        case CompositionDecision::Pivot:return "PIVOT"; case CompositionDecision::Abandon:return "ABANDON";
        case CompositionDecision::SelectInitial:return "SELECT_INITIAL"; } return "UNKNOWN";
    }
    static std::string transition_reason_name(CompositionTransitionReason v) {
        switch(v) { case CompositionTransitionReason::InitialSelection:return "INITIAL_SELECTION";
        case CompositionTransitionReason::SourceReplacement:return "SOURCE_REPLACEMENT";
        case CompositionTransitionReason::StrategicPivot:return "STRATEGIC_PIVOT";
        case CompositionTransitionReason::Refinement:return "REFINEMENT"; } return "UNKNOWN";
    }
    static std::string intent_name(UnitIntent v) {
        switch(v) { case UnitIntent::Keep:return "KEEP"; case UnitIntent::Seek:return "SEEK";
        case UnitIntent::Upgrade:return "UPGRADE"; case UnitIntent::Replace:return "REPLACE";
        case UnitIntent::Hold:return "HOLD"; case UnitIntent::SellCandidate:return "SELL_CANDIDATE"; }
        return "UNKNOWN";
    }
    static std::string relation_name(UnitStrategicRelation v) {
        switch(v) { case UnitStrategicRelation::ActiveCore:return "ACTIVE_CORE";
        case UnitStrategicRelation::ActiveFlex:return "ACTIVE_FLEX"; case UnitStrategicRelation::SharedCore:return "SHARED_CORE";
        case UnitStrategicRelation::SharedFlex:return "SHARED_FLEX"; case UnitStrategicRelation::Bridge:return "BRIDGE";
        case UnitStrategicRelation::OutsideTarget:return "OUTSIDE_TARGET"; case UnitStrategicRelation::MissingTarget:return "MISSING_TARGET"; }
        return "UNKNOWN";
    }
    static nlohmann::json lineup_json(const LineupPlan& l) {
        auto out = nlohmann::json::array();
        for (const auto& s : l.selected_board)
            out.push_back({{"champion_id", s.champion_id}, {"kind", static_cast<int>(s.kind)},
                {"priority", s.priority}, {"currently_on_board", s.currently_on_board}, {"owned", s.owned}});
        return out;
    }
    static const char* evidence_quality_name(EvidenceQuality quality) {
        switch (quality) {
            case EvidenceQuality::Missing: return "missing";
            case EvidenceQuality::Stale: return "stale";
            case EvidenceQuality::Partial: return "partial";
            case EvidenceQuality::Invalid: return "invalid";
            case EvidenceQuality::Valid: return "valid";
        }
        return "unknown";
    }
    static nlohmann::json metadata_json(const EvidenceSourceMetadata& m) {
        return {{"source", m.source}, {"source_version", m.source_version},
            {"match_id", m.match_id}, {"player_id", m.player_id},
            {"composition_id", m.composition_id},
            {"source_round", m.source_round}, {"expected_round", m.expected_round},
            {"quality", static_cast<int>(m.quality)}, {"quality_name", evidence_quality_name(m.quality)},
            {"available", m.available}, {"reason", m.reason}};
    }
    static nlohmann::json evidence_json(const PlannerEvidenceSnapshot& e) {
        nlohmann::json item_units = nlohmann::json::array();
        for (const auto& u : e.items.units)
            item_units.push_back({{"champion_id", u.champion_id},
                {"equipped_item_ids", u.equipped_item_ids}, {"equipped_fit", u.equipped_fit},
                {"best_inventory_item_id", u.best_inventory_item_id},
                {"best_inventory_fit", u.best_inventory_fit},
                {"has_equipped_items", u.has_equipped_items},
                {"has_inventory_candidate", u.has_inventory_candidate}});
        return {{"schema_version", e.schema_version}, {"match_id", e.match_id},
            {"player_id", e.player_id}, {"composition_id", e.composition_id},
            {"composition_version", e.composition_version}, {"round", e.round},
            {"economy", {{"metadata", metadata_json(e.economy.metadata)}, {"gold", e.economy.gold},
                {"level", e.economy.level}, {"xp", e.economy.xp}, {"xp_to_next", e.economy.xp_to_next},
                {"interest", e.economy.interest_if_resolved_now},
                {"projected_income", e.economy.projected_next_round_income},
                {"win_streak", e.economy.win_streak}, {"loss_streak", e.economy.loss_streak},
                {"posture", static_cast<int>(e.economy.posture)}, {"reason", static_cast<int>(e.economy.reason)},
                {"survival_pressure", e.economy.survival_pressure}, {"board_pressure", e.economy.board_pressure},
                {"economy_pressure", e.economy.economy_pressure}, {"confidence_not_probability", e.economy.confidence},
                {"buy_xp_opportunity_cost", e.economy.buy_experience_opportunity_cost},
                {"reroll_with_target_opportunity_cost", e.economy.reroll_with_target_opportunity_cost},
                {"reroll_without_target_opportunity_cost", e.economy.reroll_without_target_opportunity_cost},
                {"buy_unit_opportunity_cost", e.economy.buy_unit_opportunity_cost}}},
            {"board", {{"metadata", metadata_json(e.board.metadata)},
                {"positional_score", e.board.positional_score}, {"structural_score", e.board.structural_score},
                {"synergy_score", e.board.synergy_score}, {"total_score", e.board.total_score},
                {"strategic_fit_score", e.board.strategic_fit_score}, {"unit_quality_score", e.board.unit_quality_score},
                {"trait_coherence_score", e.board.trait_coherence_score}, {"unit_count", e.board.unit_count},
                {"frontline_count", e.board.frontline_count}, {"carry_count", e.board.carry_count},
                {"exposed_carry_count", e.board.exposed_carry_count},
                {"missing_frontline_count", e.board.missing_frontline_count},
                {"missing_backline_count", e.board.missing_backline_count}}},
            {"items", {{"metadata", metadata_json(e.items.metadata)},
                {"inventory_count", e.items.inventory_count}, {"component_count", e.items.component_count},
                {"units", item_units}}}};
    }
    std::uint64_t next_sequence_{1};
};

} // namespace tft::composition_intelligence
