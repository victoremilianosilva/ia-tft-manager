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
        strategy::StrategicActionKind policy_action = strategy::StrategicActionKind::None) const {
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
                    else if (priority->sale_restricted)
                        reject(audit, "sale restricted by equipped-item or transition risk");
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
