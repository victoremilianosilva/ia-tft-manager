#pragma once

#include "composition_intelligence/LineupPlanner.hpp"
#include "composition_intelligence/UnitPriorityPlanner.hpp"
#include "strategy/ActionEvaluator.hpp"

#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <optional>
#include <string>
#include <unordered_map>
#include <vector>

namespace tft::composition_intelligence {

enum class ActionCandidateDisposition { Accepted, Rejected };
struct CompositionActionCandidateAudit {
    std::size_t candidate_index{0};
    strategy::StrategicActionKind kind{strategy::StrategicActionKind::None};
    std::int32_t champion_id{-1};
    ActionCandidateDisposition disposition{ActionCandidateDisposition::Rejected};
    std::string reason;
    bool selected{false};
};

struct CompositionActionEvaluation {
    strategy::ActionEvaluation evaluation;
    std::string composition_id;
    std::uint64_t composition_version{0};
    bool stale{false};
    std::string stale_reason;
    std::vector<CompositionActionCandidateAudit> candidates;
    bool economy_evidence_consumed{false};
    bool board_evidence_validated{false};
    bool item_evidence_consumed{false};
    std::int32_t observed_gold{-1};
    std::int32_t observed_interest{-1};
    std::int32_t projected_next_round_income{-1};
    std::int32_t observed_economic_posture{-1};
    std::vector<std::string> evidence_rejected;
};

// Shadow-only bridge: enriches and filters diagnostic candidates, then delegates
// scoring to the existing ActionEvaluator. It never executes or publishes actions.
class CompositionActionEvaluator {
public:
    CompositionActionEvaluation evaluate(
        const std::optional<ActiveComposition>& active,
        const UnitPrioritySnapshot& priorities,
        const LineupPlan& lineup,
        const strategy::StrategicSharedContext& context,
        const strategy::EconomicControlDecision& posture,
        strategy::StrategicActionKind policy_action = strategy::StrategicActionKind::None,
        const PlannerEvidenceSnapshot* planner_evidence = nullptr,
        std::uint64_t match_id = 0) const {
        CompositionActionEvaluation out;
        out.evaluation.recommended_action = strategy::StrategicActionKind::Hold;
        out.evaluation.shadow_only = true;
        if (!active) return stale(std::move(out), "no active composition");
        out.composition_id = active->candidate.composition_id;
        out.composition_version = active->version;
        if (priorities.stale ||
            priorities.composition_id != out.composition_id ||
            priorities.composition_version != active->version) {
            return stale(std::move(out), priorities.stale ? priorities.stale_reason :
                "unit priority composition identity/version mismatch");
        }
        if (lineup.stale || lineup.composition_id != out.composition_id ||
            lineup.composition_version != active->version) {
            return stale(std::move(out), lineup.stale ? lineup.stale_reason :
                "lineup composition identity/version mismatch");
        }

        const bool snapshot_identity_valid = planner_evidence &&
            PlannerEvidenceAdapters::snapshot_identity_matches(*planner_evidence, match_id,
                context.player_id, out.composition_id, active->version, context.round);
        const bool economy_valid = snapshot_identity_valid &&
            PlannerEvidenceAdapters::source_matches(planner_evidence->economy.metadata, match_id,
                context.player_id, out.composition_id, active->version, context.round);
        const bool board_valid = snapshot_identity_valid &&
            PlannerEvidenceAdapters::source_matches(planner_evidence->board.metadata, match_id,
                context.player_id, out.composition_id, active->version, context.round);
        const bool items_valid = snapshot_identity_valid &&
            PlannerEvidenceAdapters::source_matches(planner_evidence->items.metadata, match_id,
                context.player_id, out.composition_id, active->version, context.round);
        out.economy_evidence_consumed = economy_valid;
        out.board_evidence_validated = board_valid;
        if (economy_valid) {
            out.observed_gold = planner_evidence->economy.gold;
            out.observed_interest = planner_evidence->economy.interest_if_resolved_now;
            out.projected_next_round_income = planner_evidence->economy.projected_next_round_income;
            out.observed_economic_posture = static_cast<std::int32_t>(planner_evidence->economy.posture);
        }
        if (planner_evidence && !snapshot_identity_valid)
            out.evidence_rejected.push_back("PlannerEvidenceSnapshot:identity_mismatch");
        else if (planner_evidence) {
            if (!economy_valid) out.evidence_rejected.push_back("EconomicController:" + planner_evidence->economy.metadata.reason);
            if (!board_valid) out.evidence_rejected.push_back("BoardEvaluation:" + planner_evidence->board.metadata.reason);
            if (!items_valid) out.evidence_rejected.push_back("ItemEngine:" + planner_evidence->items.metadata.reason);
        }
        std::unordered_map<std::int32_t, bool> item_risk_by_unit;
        if (items_valid) {
            for (const auto& item : planner_evidence->items.units)
                if (item.champion_id >= 0 && item.has_equipped_items)
                    item_risk_by_unit[item.champion_id] = true;
        }
        std::unordered_map<std::int32_t, const UnitPriority*> by_id;
        bool has_upgrade_target = false;
        for (const auto& unit : priorities.units) {
            if (unit.champion_id < 0) continue;
            by_id[unit.champion_id] = &unit;
            has_upgrade_target = has_upgrade_target ||
                unit.intent == UnitIntent::Upgrade || unit.intent == UnitIntent::Seek;
        }
        std::unordered_map<std::int32_t, bool> selected_lineup;
        for (const auto& slot : lineup.selected_board)
            selected_lineup[slot.champion_id] = true;
        std::unordered_map<std::int32_t, bool> endgame_target;
        for (const auto id : lineup.endgame_target_ids) endgame_target[id] = true;

        auto enriched = context;
        enriched.action_candidates.clear();
        out.candidates.reserve(context.action_candidates.size());
        for (std::size_t i = 0; i < context.action_candidates.size(); ++i) {
            auto candidate = context.action_candidates[i];
            CompositionActionCandidateAudit audit;
            audit.candidate_index = i;
            audit.kind = candidate.kind;
            audit.champion_id = candidate.champion_id;
            audit.disposition = ActionCandidateDisposition::Accepted;
            audit.reason = "accepted_by_composition_context";

            const auto found = by_id.find(candidate.champion_id);
            const UnitPriority* priority = found == by_id.end() ? nullptr : found->second;
            if (economy_valid) {
                double evidence_cost = 0.0;
                if (candidate.kind == strategy::StrategicActionKind::BuyUnit)
                    evidence_cost = planner_evidence->economy.buy_unit_opportunity_cost;
                else if (candidate.kind == strategy::StrategicActionKind::BuyExperience)
                    evidence_cost = planner_evidence->economy.buy_experience_opportunity_cost;
                else if (candidate.kind == strategy::StrategicActionKind::RerollShop)
                    evidence_cost = has_upgrade_target
                        ? planner_evidence->economy.reroll_with_target_opportunity_cost
                        : planner_evidence->economy.reroll_without_target_opportunity_cost;
                candidate.opportunity_cost = std::max(candidate.opportunity_cost, evidence_cost);
            }
            if (board_valid && candidate.champion_id >= 0) {
                const auto target = std::find_if(active->candidate.units.begin(), active->candidate.units.end(),
                    [&](const auto& unit) { return unit.champion_id == candidate.champion_id; });
                if (target != active->candidate.units.end()) {
                    const auto& board = planner_evidence->board;
                    const bool addresses_gap =
                        (target->role == UnitRole::Frontline && board.missing_frontline_count > 0) ||
                        (target->role == UnitRole::MainCarry &&
                         (board.missing_backline_count > 0 || board.exposed_carry_count > 0));
                    if (addresses_gap) candidate.composition_fit = std::max(candidate.composition_fit, 0.65);
                }
            }
            switch (candidate.kind) {
                case strategy::StrategicActionKind::BuyUnit:
                    if (!priority || !endgame_target[candidate.champion_id] ||
                        (priority->intent != UnitIntent::Seek && priority->intent != UnitIntent::Upgrade)) {
                        reject(audit, "buy requires a SEEK/UPGRADE priority in the active endgame target");
                    } else {
                        candidate.composition_fit = std::max(candidate.composition_fit,
                            priority->priority > 0 ? std::min(1.0, priority->priority / 100.0) : 0.0);
                        if (priority->intent == UnitIntent::Upgrade)
                            candidate.upgrade_value = std::max(candidate.upgrade_value,
                                priority->target_star > 0 ? 0.75 : 0.50);
                    }
                    break;
                case strategy::StrategicActionKind::DeployOrMove:
                    if (!selected_lineup[candidate.champion_id])
                        reject(audit, "unit is not selected by the current deployable lineup");
                    else if (priority) {
                        candidate.composition_fit = std::max(candidate.composition_fit,
                            priority->priority > 0 ? std::min(1.0, priority->priority / 100.0) : 0.0);
                    }
                    break;
                case strategy::StrategicActionKind::SellUnit:
                    if (!priority || priority->intent != UnitIntent::SellCandidate)
                        reject(audit, "SELL_CANDIDATE intent is required; REPLACE is not sale authorization");
                    else if (priority->sale_restricted || item_risk_by_unit[candidate.champion_id])
                        reject(audit, "sale restricted by validated equipped-item or transition risk");
                    else if (endgame_target[candidate.champion_id] || selected_lineup[candidate.champion_id])
                        reject(audit, "unit is part of the active deployable/endgame target");
                    break;
                case strategy::StrategicActionKind::RerollShop:
                    if (!has_upgrade_target)
                        reject(audit, "no SEEK/UPGRADE target justifies a targeted reroll");
                    break;
                case strategy::StrategicActionKind::BuyExperience:
                case strategy::StrategicActionKind::Hold:
                    break;
                case strategy::StrategicActionKind::None:
                default:
                    reject(audit, "unsupported strategic action kind");
                    break;
            }

            if (!candidate.available) reject(audit, "candidate is unavailable in source context");
            if (candidate.gold_cost > context.gold) reject(audit, "insufficient gold");
            if (audit.disposition == ActionCandidateDisposition::Accepted) {
                enriched.action_candidates.push_back(candidate);
            } else {
                candidate.available = false;
                enriched.action_candidates.push_back(candidate);
            }
            out.candidates.push_back(std::move(audit));
        }

        out.item_evidence_consumed = items_valid;
        out.evaluation = strategy::ActionEvaluator{}.evaluate(enriched, posture, policy_action);
        out.evaluation.shadow_only = true;
        for (auto& audit : out.candidates) {
            if (audit.candidate_index < out.evaluation.candidate_scores.size())
                audit.selected = out.evaluation.candidate_scores[audit.candidate_index].selected;
        }
        return out;
    }

private:
    static void reject(CompositionActionCandidateAudit& audit, std::string reason) {
        audit.disposition = ActionCandidateDisposition::Rejected;
        audit.reason = std::move(reason);
    }
    static CompositionActionEvaluation stale(CompositionActionEvaluation out, std::string reason) {
        out.stale = true;
        out.stale_reason = std::move(reason);
        out.evaluation.recommended_action = strategy::StrategicActionKind::Hold;
        out.evaluation.recommended_champion_id = -1;
        out.evaluation.reason = strategy::StrategicReason::InsufficientEvidence;
        out.evaluation.confidence = 0.0;
        out.evaluation.candidate_scores.clear();
        out.candidates.clear();
        return out;
    }
};

} // namespace tft::composition_intelligence
