#pragma once

#include "composition_intelligence/LineupPlanner.hpp"
#include "composition_intelligence/UnitPriorityPlanner.hpp"
#include "lobby/EconomyEngine.hpp"

#include <algorithm>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <optional>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <nlohmann/json.hpp>

namespace tft::composition_intelligence {

// Independent v1 contextual evaluator. It deliberately does not call or share
// scoring code with strategy::ActionEvaluator (the frozen baseline).
inline constexpr std::uint32_t kContextualActionEvaluatorSchemaVersion = 2;

struct ContextualActionCandidateScore {
    std::size_t candidate_index{0};
    strategy::StrategicActionKind kind{strategy::StrategicActionKind::None};
    std::int32_t champion_id{-1};
    std::string candidate_id;
    bool eligible{false};
    bool selected{false};
    std::string rejection_reason;
    double board_value{0.0};
    double survival_value{0.0};
    double streak_value{0.0};
    double unit_priority_value{0.0};
    double lineup_value{0.0};
    double upgrade_value{0.0};
    double economy_cost{0.0};
    bool marginal_economy_evidence_available{false};
    std::int32_t gold_before{0};
    std::int32_t gold_after{0};
    std::int32_t interest_before{0};
    std::int32_t interest_after{0};
    std::int32_t interest_delta{0};
    std::uint32_t marginal_horizon_rounds{0};
    std::string marginal_cost_source{"unavailable"};
    double total_score{0.0};
};

struct ContextualActionEvaluation {
    std::uint32_t schema_version{kContextualActionEvaluatorSchemaVersion};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::string composition_id;
    std::uint64_t composition_version{0};
    bool stale{false};
    std::string stale_reason;
    bool economy_evidence_consumed{false};
    bool board_evidence_consumed{false};
    bool item_evidence_consumed{false};
    strategy::StrategicActionKind recommended_action{strategy::StrategicActionKind::None};
    std::int32_t recommended_champion_id{-1};
    double confidence_not_probability{0.0};
    std::string rationale{"no_positive_contextual_candidate"};
    std::vector<std::string> evidence_rejected;
    std::vector<ContextualActionCandidateScore> candidates;

    nlohmann::json to_json() const {
        nlohmann::json items = nlohmann::json::array();
        for (const auto& c : candidates) {
            items.push_back({
                {"candidate_index", c.candidate_index},
                {"kind", static_cast<int>(c.kind)},
                {"champion_id", c.champion_id},
                {"candidate_id", c.candidate_id},
                {"eligible", c.eligible},
                {"selected", c.selected},
                {"rejection_reason", c.rejection_reason},
                {"components", {
                    {"board_value", c.board_value},
                    {"survival_value", c.survival_value},
                    {"streak_value", c.streak_value},
                    {"unit_priority_value", c.unit_priority_value},
                    {"lineup_value", c.lineup_value},
                    {"upgrade_value", c.upgrade_value},
                    {"economy_cost", c.economy_cost},
                    {"marginal_economy_evidence_available", c.marginal_economy_evidence_available},
                    {"gold_before", c.gold_before},
                    {"gold_after", c.gold_after},
                    {"interest_before", c.interest_before},
                    {"interest_after", c.interest_after},
                    {"interest_delta", c.interest_delta},
                    {"marginal_horizon_rounds", c.marginal_horizon_rounds},
                    {"marginal_cost_source", c.marginal_cost_source},
                    {"total_score", c.total_score}
                }}
            });
        }
        return {
            {"schema_version", schema_version},
            {"identity", {{"match_id", match_id}, {"player_id", player_id},
                {"round", round}, {"composition_id", composition_id},
                {"composition_version", composition_version}}},
            {"stale", stale}, {"stale_reason", stale_reason},
            {"evidence_consumed", {{"economy", economy_evidence_consumed},
                {"board", board_evidence_consumed}, {"items", item_evidence_consumed}}},
            {"evidence_rejected", evidence_rejected},
            {"recommended_action", static_cast<int>(recommended_action)},
            {"recommended_champion_id", recommended_champion_id},
            {"confidence_not_probability", confidence_not_probability},
            {"rationale", rationale}, {"candidates", items},
            {"shadow_only", true}
        };
    }
};

class ContextualActionEvaluator {
public:
    ContextualActionEvaluation evaluate(
        const std::optional<ActiveComposition>& active,
        const UnitPrioritySnapshot& priorities,
        const LineupPlan& lineup,
        const strategy::StrategicSharedContext& context,
        const PlannerEvidenceSnapshot* evidence,
        std::uint64_t match_id) const {
        ContextualActionEvaluation out;
        out.match_id = match_id;
        out.player_id = context.player_id;
        out.round = context.round;
        const bool has_active_composition = active.has_value();
        if (has_active_composition) {
            out.composition_id = active->candidate.composition_id;
            out.composition_version = active->version;
        } else if (context.anchor_candidates.empty()) {
            return stale(std::move(out), "no active composition or native anchor hypothesis");
        }
        if (!context.alive) return stale(std::move(out), "player is not alive");
        if (has_active_composition &&
            (priorities.stale || priorities.composition_id != out.composition_id ||
                priorities.composition_version != active->version))
            return stale(std::move(out), "unit priority identity/version mismatch");
        if (has_active_composition &&
            (lineup.stale || lineup.composition_id != out.composition_id ||
                lineup.composition_version != active->version))
            return stale(std::move(out), "lineup identity/version mismatch");

        const bool envelope_valid = evidence &&
            PlannerEvidenceAdapters::snapshot_identity_matches(*evidence, match_id,
                context.player_id, out.composition_id, out.composition_version, context.round);
        const bool economy_valid = envelope_valid &&
            PlannerEvidenceAdapters::source_matches(evidence->economy.metadata, context.round);
        const bool board_valid = envelope_valid &&
            PlannerEvidenceAdapters::source_matches(evidence->board.metadata, context.round);
        const bool items_valid = envelope_valid &&
            PlannerEvidenceAdapters::source_matches(evidence->items.metadata, context.round);
        if (evidence && !envelope_valid)
            return stale(std::move(out), "planner evidence match/player/round/composition identity mismatch");
        out.economy_evidence_consumed = economy_valid;
        out.board_evidence_consumed = board_valid;
        out.item_evidence_consumed = items_valid;
        if (evidence && !envelope_valid) {
            out.evidence_rejected.push_back("PlannerEvidenceSnapshot:identity_mismatch");
        } else if (evidence) {
            if (!economy_valid) out.evidence_rejected.push_back("EconomicController:" + evidence->economy.metadata.reason);
            if (!board_valid) out.evidence_rejected.push_back("BoardEvaluation:" + evidence->board.metadata.reason);
            if (!items_valid) out.evidence_rejected.push_back("ItemEngine:" + evidence->items.metadata.reason);
        }

        std::unordered_map<std::int32_t, const UnitPriority*> priority_by_id;
        bool has_upgrade_target = false;
        if (has_active_composition) {
            for (const auto& unit : priorities.units) {
                if (unit.champion_id < 0) continue;
                priority_by_id[unit.champion_id] = &unit;
                has_upgrade_target = has_upgrade_target ||
                    unit.intent == UnitIntent::Seek || unit.intent == UnitIntent::Upgrade;
            }
        }
        std::unordered_set<std::int32_t> lineup_ids;
        if (has_active_composition) {
            for (const auto& slot : lineup.selected_board)
                lineup_ids.insert(slot.champion_id);
        }
        std::unordered_set<std::int32_t> target_ids;
        if (has_active_composition)
            target_ids.insert(lineup.endgame_target_ids.begin(), lineup.endgame_target_ids.end());
        std::unordered_map<std::int32_t, bool> equipped_item_risk;
        if (items_valid) {
            for (const auto& unit : evidence->items.units)
                if (unit.champion_id >= 0 && unit.has_equipped_items)
                    equipped_item_risk[unit.champion_id] = true;
        }

        if (context.action_candidates.empty()) {
            out.recommended_action = strategy::StrategicActionKind::None;
            out.recommended_champion_id = -1;
            out.confidence_not_probability = 0.0;
            out.rationale = "no_candidates";
            return out;
        }

        double best_score = 0.0; // HOLD remains the explicit zero-value option.
        std::size_t selected_index = std::numeric_limits<std::size_t>::max();
        std::size_t hold_candidate_index = std::numeric_limits<std::size_t>::max();
        out.candidates.reserve(context.action_candidates.size());
        for (std::size_t i = 0; i < context.action_candidates.size(); ++i) {
            const auto& candidate = context.action_candidates[i];
            ContextualActionCandidateScore score;
            score.candidate_index = i;
            score.kind = candidate.kind;
            score.champion_id = candidate.champion_id;
            score.candidate_id = candidate.candidate_id;
            score.eligible = candidate.available && candidate.gold_cost <= context.gold;
            if (!candidate.available) score.rejection_reason = "candidate_unavailable";
            else if (candidate.gold_cost > context.gold) score.rejection_reason = "insufficient_gold";

            const auto found = priority_by_id.find(candidate.champion_id);
            const UnitPriority* priority = found == priority_by_id.end() ? nullptr : found->second;
            if (score.eligible) {
                switch (candidate.kind) {
                    case strategy::StrategicActionKind::BuyUnit:
                        if (!has_active_composition) {
                            const auto anchor = std::find_if(context.anchor_candidates.begin(),
                                context.anchor_candidates.end(), [&](const auto& value) {
                                    return value.unit.champion_id == candidate.champion_id &&
                                        value.shop_available;
                                });
                            if (anchor == context.anchor_candidates.end() || candidate.shop_slot < 0)
                                reject(score, "buy_requires_native_anchor_and_exact_shop_slot");
                        } else if (!priority || !target_ids.count(candidate.champion_id) ||
                            (priority->intent != UnitIntent::Seek && priority->intent != UnitIntent::Upgrade)) {
                            reject(score, "buy_requires_seek_or_upgrade_in_active_target");
                        }
                        break;
                    case strategy::StrategicActionKind::DeployOrMove:
                        if (!lineup_ids.count(candidate.champion_id))
                            reject(score, "unit_not_in_deployable_lineup");
                        break;
                    case strategy::StrategicActionKind::SellUnit:
                        if (!priority || priority->intent != UnitIntent::SellCandidate)
                            reject(score, "sell_candidate_intent_required");
                        else if (priority->sale_restricted || priority->copies_owned >= 2 ||
                            priority->highest_star > 1 || priority->target_star > 0 ||
                            equipped_item_risk[candidate.champion_id])
                            reject(score, "sale_restricted_by_pair_star_item_or_transition_risk");
                        else if (target_ids.count(candidate.champion_id) || lineup_ids.count(candidate.champion_id) ||
                            priority->relation == UnitStrategicRelation::Bridge)
                            reject(score, "unit_preserved_by_target_lineup_or_bridge");
                        break;
                    case strategy::StrategicActionKind::RerollShop:
                        if (!has_upgrade_target) reject(score, "no_seek_or_upgrade_target");
                        break;
                    case strategy::StrategicActionKind::BuyExperience:
                    case strategy::StrategicActionKind::Hold:
                        break;
                    case strategy::StrategicActionKind::None:
                    default:
                        reject(score, "unsupported_action_kind");
                        break;
                }
            }
            if (score.eligible) {
                const double positive_board_delta =
                    std::max(0.0, candidate.expected_board_delta);
                score.board_value = positive_board_delta * 0.55;
                // Economic urgency changes the value of an evidenced board
                // improvement; posture labels never force an action category.
                if (economy_valid && evidence->economy.survival_evidence_available)
                    score.survival_value = positive_board_delta * 0.20 *
                        std::clamp(evidence->economy.survival_pressure, 0.0, 1.0);
                if (economy_valid && evidence->economy.streak_evidence_available) {
                    const auto streak = std::max(evidence->economy.win_streak,
                        evidence->economy.loss_streak);
                    score.streak_value = positive_board_delta * 0.08 *
                        std::clamp(static_cast<double>(streak) / 6.0, 0.0, 1.0);
                }
                if (priority) {
                    score.unit_priority_value = std::clamp(
                        static_cast<double>(priority->priority) / 100.0, 0.0, 1.0) * 0.24;
                } else if (!has_active_composition &&
                    candidate.kind == strategy::StrategicActionKind::BuyUnit) {
                    const auto anchor = std::find_if(context.anchor_candidates.begin(),
                        context.anchor_candidates.end(), [&](const auto& value) {
                            return value.unit.champion_id == candidate.champion_id &&
                                value.shop_available;
                        });
                    if (anchor != context.anchor_candidates.end())
                        score.unit_priority_value = std::clamp(
                            anchor->unit.composition_fit, 0.0, 1.0) * 0.24;
                }
                score.lineup_value = lineup_ids.count(candidate.champion_id) ? 0.12 : 0.0;
                score.upgrade_value = std::clamp(candidate.upgrade_value, 0.0, 1.0) * 0.18;
                if (board_valid && has_active_composition && candidate.champion_id >= 0) {
                    const auto target = std::find_if(active->candidate.units.begin(), active->candidate.units.end(),
                        [&](const auto& unit) { return unit.champion_id == candidate.champion_id; });
                    if (target != active->candidate.units.end()) {
                        const auto& board = evidence->board;
                        if ((target->role == UnitRole::Frontline && board.missing_frontline_count > 0) ||
                            (target->role == UnitRole::MainCarry &&
                                (board.missing_backline_count > 0 || board.exposed_carry_count > 0)))
                            score.board_value += 0.20;
                    }
                }
                const auto expected_interest_before =
                    EconomyEngine{}.get_interest(context.gold);
                const bool marginal_valid =
                    candidate.marginal_economy_evidence_available &&
                    candidate.marginal_cost_source ==
                        "native_gold+EconomyEngine::get_interest" &&
                    candidate.marginal_cost_horizon_rounds == 1 &&
                    candidate.marginal_cost_uncertainty == 0.0 &&
                    candidate.marginal_gold_before == context.gold &&
                    candidate.marginal_gold_after >= 0 &&
                    candidate.marginal_interest_before == expected_interest_before &&
                    candidate.marginal_interest_after ==
                        EconomyEngine{}.get_interest(candidate.marginal_gold_after) &&
                    std::isfinite(candidate.direct_gold_cost);
                score.marginal_economy_evidence_available = marginal_valid;
                if (marginal_valid) {
                    score.gold_before = candidate.marginal_gold_before;
                    score.gold_after = candidate.marginal_gold_after;
                    score.interest_before = candidate.marginal_interest_before;
                    score.interest_after = candidate.marginal_interest_after;
                    score.interest_delta = candidate.marginal_interest_delta;
                    score.marginal_horizon_rounds =
                        candidate.marginal_cost_horizon_rounds;
                    score.marginal_cost_source = candidate.marginal_cost_source;
                    const double direct_cost = candidate.direct_gold_cost;
                    const double lost_interest = std::max(
                        0.0, static_cast<double>(-candidate.marginal_interest_delta));
                    // Direct spend/credit and the exact interest delta are
                    // counted once. Unproduced shop/opportunity values add no prior.
                    score.economy_cost = (direct_cost * 0.045) +
                        (lost_interest * 0.12);
                }
                score.total_score = score.board_value + score.survival_value +
                    score.streak_value + score.unit_priority_value +
                    score.lineup_value + score.upgrade_value - score.economy_cost;
                if (candidate.kind == strategy::StrategicActionKind::Hold) {
                    score.total_score = 0.0;
                    if (hold_candidate_index == std::numeric_limits<std::size_t>::max())
                        hold_candidate_index = i;
                }
                if (score.total_score > best_score) {
                    best_score = score.total_score;
                    selected_index = i;
                    out.recommended_action = candidate.kind;
                    out.recommended_champion_id = candidate.champion_id;
                    out.rationale = !has_active_composition &&
                        candidate.kind == strategy::StrategicActionKind::BuyUnit
                        ? "native_anchor_shop_purchase" :
                        rationale(candidate.kind, priority, economy_valid, board_valid);
                }
            }
            out.candidates.push_back(std::move(score));
        }
        if (selected_index == std::numeric_limits<std::size_t>::max() &&
            hold_candidate_index != std::numeric_limits<std::size_t>::max()) {
            selected_index = hold_candidate_index;
            out.recommended_action = strategy::StrategicActionKind::Hold;
            out.recommended_champion_id = -1;
            out.rationale = "no_positive_contextual_candidate";
        }
        if (selected_index != std::numeric_limits<std::size_t>::max()) {
            out.candidates[selected_index].selected = true;
            out.confidence_not_probability = std::clamp(0.50 + best_score * 0.10, 0.50, 0.85);
        }
        return out;
    }

private:
    static void reject(ContextualActionCandidateScore& score, std::string reason) {
        score.eligible = false;
        score.rejection_reason = std::move(reason);
    }
    static ContextualActionEvaluation stale(ContextualActionEvaluation out, std::string reason) {
        out.stale = true;
        out.stale_reason = std::move(reason);
        out.rationale = "context_unavailable";
        return out;
    }
    static std::string rationale(strategy::StrategicActionKind kind,
        const UnitPriority* priority, bool economy_valid, bool board_valid) {
        switch (kind) {
            case strategy::StrategicActionKind::BuyUnit:
                return priority && priority->intent == UnitIntent::Upgrade
                    ? "upgrade_target_priority_and_board_value" : "seek_target_priority_and_board_value";
            case strategy::StrategicActionKind::DeployOrMove:
                return board_valid ? "deployable_lineup_and_observed_board_gap" : "deployable_lineup_priority";
            case strategy::StrategicActionKind::SellUnit:
                return "explicit_sell_candidate_without_item_or_transition_restriction";
            case strategy::StrategicActionKind::RerollShop:
                return economy_valid ? "upgrade_target_with_validated_economic_cost" : "upgrade_target";
            case strategy::StrategicActionKind::BuyExperience:
                return economy_valid ? "progression_with_validated_economic_cost" : "progression_candidate";
            case strategy::StrategicActionKind::Hold:
                return "no_positive_contextual_candidate";
            case strategy::StrategicActionKind::None:
                break;
        }
        return "unsupported";
    }
};

} // namespace tft::composition_intelligence
