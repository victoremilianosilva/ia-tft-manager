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
inline constexpr std::uint32_t kContextualActionEvaluatorSchemaVersion = 4;

struct ContextualActionCandidateScore {
    std::size_t candidate_index{0};
    strategy::StrategicActionKind kind{strategy::StrategicActionKind::None};
    std::int32_t champion_id{-1};
    std::string candidate_id;
    std::uint64_t source_sequence{0};
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
    // Signed cost against HOLD: positive consumes liquidity; negative releases it.
    double liquidity_cost{0.0};
    bool opportunity_cost_available{false};
    double opportunity_cost{0.0};
    std::string opportunity_cost_value_basis{"unavailable"};
    std::string opportunity_cost_source{"unavailable_no_validated_producer"};
    std::string opportunity_cost_forgone_candidate_id;
    std::uint32_t opportunity_cost_horizon_rounds{0};
    double opportunity_cost_uncertainty{1.0};
    std::int32_t marginal_gold_delta{0};
    std::string evidence_source{"unknown"};
    std::uint32_t evidence_horizon_rounds{0};
    double evidence_uncertainty{1.0};
    bool marginal_economy_evidence_available{false};
    std::int32_t gold_before{0};
    std::int32_t gold_after{0};
    std::int32_t interest_before{0};
    std::int32_t interest_after{0};
    std::int32_t interest_delta{0};
    std::uint32_t marginal_horizon_rounds{0};
    double marginal_cost_uncertainty{1.0};
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
    bool economic_posture_available{false};
    strategy::EconomicPosture economic_posture{strategy::EconomicPosture::AccumulateResources};
    strategy::StrategicReason economic_reason{strategy::StrategicReason::InsufficientEvidence};
    bool economic_confidence_available{false};
    double economic_confidence{0.0};
    bool survival_pressure_available{false};
    double survival_pressure{0.0};
    bool board_pressure_available{false};
    double board_pressure{0.0};
    bool economy_pressure_available{false};
    double economy_pressure{0.0}; // diagnostic only; liquidity is scored from marginal gold delta
    std::vector<std::string> economic_evidence_used;
    std::vector<std::string> economic_evidence_missing;
    bool projected_income_available{false};
    bool incoming_damage_available{false};
    bool elimination_risk_available{false};
    bool progression_available{false};
    bool board_evidence_consumed{false};
    bool item_evidence_consumed{false};
    strategy::StrategicActionKind recommended_action{strategy::StrategicActionKind::None};
    std::int32_t recommended_champion_id{-1};
    double confidence_not_probability{0.0};
    std::string rationale{"no_positive_contextual_candidate"};
    std::vector<std::string> evidence_rejected;
    std::vector<ContextualActionCandidateScore> candidates;
    // Appended to preserve aggregate initialization of the evaluator result.
    std::string projected_income_source{"unavailable"};
    std::uint32_t projected_income_horizon_rounds{0};
    double projected_income_uncertainty{1.0};

    nlohmann::json to_json() const {
        nlohmann::json items = nlohmann::json::array();
        for (const auto& c : candidates) {
            items.push_back({
                {"candidate_index", c.candidate_index},
                {"kind", static_cast<int>(c.kind)},
                {"champion_id", c.champion_id},
                {"candidate_id", c.candidate_id},
                {"source_sequence", c.source_sequence},
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
                    {"liquidity_cost", c.liquidity_cost},
                    {"opportunity_cost_available", c.opportunity_cost_available},
                    {"opportunity_cost_source", c.opportunity_cost_source},
                    {"opportunity_cost_forgone_candidate_id", c.opportunity_cost_forgone_candidate_id},
                    {"opportunity_cost_horizon_rounds", c.opportunity_cost_horizon_rounds},
                    {"opportunity_cost_uncertainty", c.opportunity_cost_uncertainty},
                    {"marginal_gold_delta", c.marginal_gold_delta},
                    {"evidence_source", c.evidence_source},
                    {"evidence_horizon_rounds", c.evidence_horizon_rounds},
                    {"evidence_uncertainty", c.evidence_uncertainty},
                    {"marginal_economy_evidence_available", c.marginal_economy_evidence_available},
                    {"gold_before", c.gold_before},
                    {"gold_after", c.gold_after},
                    {"interest_before", c.interest_before},
                    {"interest_after", c.interest_after},
                    {"interest_delta", c.interest_delta},
                    {"marginal_horizon_rounds", c.marginal_horizon_rounds},
                    {"marginal_cost_uncertainty", c.marginal_cost_uncertainty},
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
            {"economic_context", {{"posture_available", economic_posture_available},
                {"posture", static_cast<int>(economic_posture)},
                {"reason", static_cast<int>(economic_reason)},
                {"confidence_available", economic_confidence_available},
                {"confidence_not_probability", economic_confidence},
                {"survival_pressure_available", survival_pressure_available},
                {"survival_pressure", survival_pressure},
                {"board_pressure_available", board_pressure_available},
                {"board_pressure", board_pressure},
                {"economy_pressure_available", economy_pressure_available},
                {"economy_pressure", economy_pressure},
                {"evidence_used", economic_evidence_used},
                {"evidence_missing", economic_evidence_missing},
                {"projected_income_available", projected_income_available},
                {"projected_income_source", projected_income_source},
                {"projected_income_horizon_rounds", projected_income_horizon_rounds},
                {"projected_income_uncertainty", projected_income_uncertainty},
                {"incoming_damage_available", incoming_damage_available},
                {"elimination_risk_available", elimination_risk_available},
                {"progression_available", progression_available}}},
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
        if (context.sequence != 0 &&
            (lineup.match_id != match_id || lineup.player_id != context.player_id ||
                lineup.round != context.round || lineup.sequence != context.sequence))
            return stale(std::move(out), "lineup match/player/round/sequence mismatch");

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
        if (economy_valid) {
            out.economic_posture_available = evidence->economy.sufficient_evidence;
            out.economic_posture = evidence->economy.posture;
            out.economic_reason = evidence->economy.reason;
            out.economic_confidence_available = true;
            out.economic_confidence = evidence->economy.confidence;
            out.survival_pressure_available = evidence->economy.survival_evidence_available;
            out.survival_pressure = evidence->economy.survival_pressure;
            out.board_pressure_available = evidence->economy.board_pressure_available;
            out.board_pressure = evidence->economy.board_pressure;
            out.economy_pressure_available = evidence->economy.economy_pressure_available;
            out.economy_pressure = evidence->economy.economy_pressure;
            out.economic_evidence_used = evidence->economy.evidence_used;
            out.economic_evidence_missing = evidence->economy.evidence_missing;
            out.projected_income_available = evidence->economy.projected_income_available;
            out.projected_income_source = evidence->economy.projected_income_source;
            out.projected_income_horizon_rounds = evidence->economy.projected_income_horizon_rounds;
            out.projected_income_uncertainty = evidence->economy.projected_income_uncertainty;
            out.incoming_damage_available = evidence->economy.incoming_damage_available;
            out.elimination_risk_available = evidence->economy.elimination_risk_available;
            out.progression_available = evidence->economy.progression_available;
        }
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
            score.source_sequence = candidate.source_sequence;
            score.evidence_source = candidate.evidence_source;
            score.evidence_horizon_rounds = candidate.evidence_horizon_rounds;
            score.evidence_uncertainty = std::isfinite(candidate.evidence_uncertainty)
                ? std::clamp(candidate.evidence_uncertainty, 0.0, 1.0) : 1.0;
            const bool requires_observed_gold =
                candidate.kind == strategy::StrategicActionKind::BuyUnit ||
                candidate.kind == strategy::StrategicActionKind::BuyExperience ||
                candidate.kind == strategy::StrategicActionKind::RerollShop ||
                candidate.kind == strategy::StrategicActionKind::SellUnit;
            const bool requires_marginal_economy = requires_observed_gold;
            score.eligible = candidate.available &&
                (!requires_observed_gold || context.evidence.gold) &&
                candidate.gold_cost <= context.gold;
            if (candidate.source_sequence > 0 && context.sequence > 0 &&
                candidate.source_sequence != context.sequence)
                reject(score, "candidate_strategic_sequence_mismatch");
            if (!candidate.available) score.rejection_reason = "candidate_unavailable";
            else if (requires_observed_gold && !context.evidence.gold)
                score.rejection_reason = "gold_evidence_unavailable";
            else if (candidate.gold_cost > context.gold)
                score.rejection_reason = "insufficient_gold";

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
                    const double unit_value = std::clamp(
                        static_cast<double>(priority->priority) / 100.0, 0.0, 1.0) * 0.24;
                    // Selling sacrifices the unit's retained strategic value;
                    // seeking/upgrading candidates receive that value positively.
                    score.unit_priority_value =
                        candidate.kind == strategy::StrategicActionKind::SellUnit
                            ? -unit_value : unit_value;
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
                const bool direct_cost_in_range =
                    std::isfinite(candidate.direct_gold_cost) &&
                    candidate.direct_gold_cost >= static_cast<double>(
                        std::numeric_limits<std::int32_t>::min()) &&
                    candidate.direct_gold_cost <= static_cast<double>(
                        std::numeric_limits<std::int32_t>::max());
                const auto expected_gold_after = direct_cost_in_range
                    ? static_cast<std::int64_t>(context.gold) -
                        static_cast<std::int64_t>(std::llround(candidate.direct_gold_cost))
                    : -1;
                const auto expected_interest_before =
                    context.gold >= 0 ? EconomyEngine{}.get_interest(context.gold) : -1;
                const bool marginal_valid =
                    context.evidence.gold && context.gold >= 0 && direct_cost_in_range &&
                    candidate.marginal_economy_evidence_available &&
                    candidate.marginal_cost_source ==
                        "native_gold+EconomyEngine::get_interest" &&
                    candidate.marginal_cost_horizon_rounds == 1 &&
                    candidate.marginal_cost_uncertainty == 0.0 &&
                    candidate.marginal_gold_before == context.gold &&
                    expected_gold_after >= 0 &&
                    expected_gold_after <= std::numeric_limits<std::int32_t>::max() &&
                    candidate.marginal_gold_after == expected_gold_after &&
                    candidate.marginal_interest_before == expected_interest_before &&
                    candidate.marginal_interest_after ==
                        EconomyEngine{}.get_interest(candidate.marginal_gold_after) &&
                    candidate.marginal_interest_delta ==
                        candidate.marginal_interest_after -
                            candidate.marginal_interest_before;
                score.marginal_economy_evidence_available = marginal_valid;
                const bool opportunity_valid =
                    candidate.opportunity_cost_evidence_available &&
                    candidate.opportunity_cost_source == "same_snapshot_competing_alternative.v1" &&
                    !candidate.opportunity_cost_forgone_candidate_id.empty() &&
                    candidate.opportunity_cost_horizon_rounds > 0 &&
                    std::isfinite(candidate.opportunity_cost) && candidate.opportunity_cost >= 0.0 &&
                    std::isfinite(candidate.opportunity_cost_uncertainty) &&
                    candidate.opportunity_cost_uncertainty >= 0.0 &&
                    candidate.opportunity_cost_uncertainty < 1.0;
                score.opportunity_cost_available = opportunity_valid;
                if (opportunity_valid) {
                    score.opportunity_cost = candidate.opportunity_cost;
                    score.opportunity_cost_value_basis = "native_board_contribution.v1";
                    score.opportunity_cost_source = candidate.opportunity_cost_source;
                    score.opportunity_cost_forgone_candidate_id =
                        candidate.opportunity_cost_forgone_candidate_id;
                    score.opportunity_cost_horizon_rounds =
                        candidate.opportunity_cost_horizon_rounds;
                    score.opportunity_cost_uncertainty = candidate.opportunity_cost_uncertainty;
                    // Strategic opportunity is distinct from principal and interest;
                    // its own uncertainty discounts its contribution conservatively.
                    // Applied after the marginal envelope is assembled below.
                }
                if (marginal_valid) {
                    score.gold_before = candidate.marginal_gold_before;
                    score.gold_after = candidate.marginal_gold_after;
                    score.interest_before = candidate.marginal_interest_before;
                    score.interest_after = candidate.marginal_interest_after;
                    score.interest_delta = candidate.marginal_interest_delta;
                    score.marginal_gold_delta = candidate.marginal_gold_after -
                        candidate.marginal_gold_before;
                    score.marginal_horizon_rounds =
                        candidate.marginal_cost_horizon_rounds;
                    score.marginal_cost_uncertainty = candidate.marginal_cost_uncertainty;
                    score.marginal_cost_source = candidate.marginal_cost_source;
                    const double liquidity_base = static_cast<double>(
                        std::max<std::int32_t>(1, candidate.marginal_gold_before));
                    // Normalize the exact gold delta by observed starting liquidity.
                    // This is a relative liquidity impact, not a future-income estimate.
                    score.liquidity_cost = std::clamp(
                        -static_cast<double>(score.marginal_gold_delta) / liquidity_base,
                        -1.0, 1.0) * 0.18;
                    const double interest_cost =
                        -static_cast<double>(candidate.marginal_interest_delta);
                    // The signed interest delta preserves both lost interest and
                    // a verified interest gain. Principal and interest are counted once.
                    // No projected income or unproduced opportunity cost is added.
                    score.economy_cost = score.liquidity_cost + (interest_cost * 0.12);
                }
                if (opportunity_valid) {
                    // Opportunity values from the builder use native board-
                    // contribution units; apply the same coefficient as this
                    // evaluator's board-value component instead of a second,
                    // unrelated action-family discount.
                    score.economy_cost += candidate.opportunity_cost *
                        (1.0 - candidate.opportunity_cost_uncertainty) * 0.55;
                }
                if (requires_marginal_economy && !marginal_valid)
                    reject(score, "marginal_economy_evidence_unavailable");
                score.total_score = score.eligible
                    ? score.board_value + score.survival_value +
                        score.streak_value + score.unit_priority_value +
                        score.lineup_value + score.upgrade_value - score.economy_cost
                    : 0.0;
                if (candidate.kind == strategy::StrategicActionKind::Hold) {
                    score.total_score = 0.0;
                    if (hold_candidate_index == std::numeric_limits<std::size_t>::max())
                        hold_candidate_index = i;
                }
                if (score.eligible && score.total_score > best_score) {
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
        // Compare every eligible action family on the same net contextual
        // score against HOLD. The score already includes its own board,
        // unit/upgrade, liquidity, principal and interest components, so the
        // alternative's costs are counted once and no action-family priors are
        // fabricated. Uncertain or horizon-mismatched alternatives are omitted.
        std::vector<strategy::OpportunityAlternativeEvidence> opportunity_alternatives;
        opportunity_alternatives.reserve(out.candidates.size());
        const bool opportunity_identity_valid = context.match_id > 0 &&
            context.player_id >= 0 && context.round > 0 && context.sequence > 0;
        for (const auto& candidate_score : out.candidates) {
            strategy::OpportunityAlternativeEvidence alternative;
            alternative.candidate_id = candidate_score.candidate_id;
            alternative.value_basis = "contextual_action_score.v1";
            alternative.marginal_strategic_value =
                std::max(0.0, candidate_score.total_score);
            alternative.horizon_rounds = candidate_score.evidence_horizon_rounds;
            alternative.uncertainty = candidate_score.evidence_uncertainty;
            alternative.available = candidate_score.eligible &&
                candidate_score.kind != strategy::StrategicActionKind::Hold &&
                candidate_score.total_score > 0.0 &&
                candidate_score.evidence_horizon_rounds > 0 &&
                std::isfinite(candidate_score.evidence_uncertainty) &&
                candidate_score.evidence_uncertainty >= 0.0 &&
                candidate_score.evidence_uncertainty < 1.0;
            alternative.identity_valid = opportunity_identity_valid &&
                !candidate_score.candidate_id.empty() &&
                candidate_score.source_sequence == context.sequence;
            opportunity_alternatives.push_back(std::move(alternative));
        }

        const strategy::OpportunityCostProducer opportunity_producer;
        for (auto& candidate_score : out.candidates) {
            if (!candidate_score.eligible ||
                candidate_score.kind == strategy::StrategicActionKind::Hold ||
                candidate_score.opportunity_cost_available ||
                candidate_score.total_score <= 0.0 ||
                candidate_score.evidence_uncertainty >= 1.0 ||
                candidate_score.evidence_horizon_rounds == 0 ||
                !opportunity_identity_valid ||
                candidate_score.source_sequence != context.sequence)
                continue;
            const auto opportunity = opportunity_producer.evaluate(
                candidate_score.candidate_id, opportunity_alternatives,
                candidate_score.evidence_horizon_rounds,
                "contextual_action_score.v1");
            if (!opportunity.available) continue;
            const double effective_cost =
                opportunity.cost * (1.0 - opportunity.uncertainty);
            candidate_score.opportunity_cost = opportunity.cost;
            candidate_score.opportunity_cost_value_basis = opportunity.value_basis;
            candidate_score.opportunity_cost_available = true;
            candidate_score.opportunity_cost_source = opportunity.source;
            candidate_score.opportunity_cost_forgone_candidate_id =
                opportunity.sacrificed_candidate_id;
            candidate_score.opportunity_cost_horizon_rounds =
                opportunity.horizon_rounds;
            candidate_score.opportunity_cost_uncertainty = opportunity.uncertainty;
            candidate_score.economy_cost += effective_cost;
            candidate_score.total_score -= effective_cost;
        }

        // Re-select after opportunity costs have been applied. The first pass
        // only establishes each candidate's net value against HOLD.
        selected_index = std::numeric_limits<std::size_t>::max();
        hold_candidate_index = std::numeric_limits<std::size_t>::max();
        best_score = 0.0;
        out.recommended_action = strategy::StrategicActionKind::None;
        out.recommended_champion_id = -1;
        out.rationale = "no_positive_contextual_candidate";
        for (std::size_t i = 0; i < out.candidates.size(); ++i) {
            const auto& candidate_score = out.candidates[i];
            if (candidate_score.kind == strategy::StrategicActionKind::Hold) {
                if (hold_candidate_index == std::numeric_limits<std::size_t>::max())
                    hold_candidate_index = i;
                continue;
            }
            if (!candidate_score.eligible || candidate_score.total_score <= best_score)
                continue;
            best_score = candidate_score.total_score;
            selected_index = i;
            out.recommended_action = candidate_score.kind;
            out.recommended_champion_id = candidate_score.champion_id;
            const auto priority_it = priority_by_id.find(candidate_score.champion_id);
            const UnitPriority* selected_priority = priority_it == priority_by_id.end()
                ? nullptr : priority_it->second;
            out.rationale = !has_active_composition &&
                candidate_score.kind == strategy::StrategicActionKind::BuyUnit
                ? "native_anchor_shop_purchase"
                : rationale(candidate_score.kind, selected_priority, economy_valid, board_valid);
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
