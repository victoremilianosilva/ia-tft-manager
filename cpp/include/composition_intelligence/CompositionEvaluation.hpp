#pragma once

#include "composition_intelligence/ActiveCompositionManager.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <optional>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace tft::composition_intelligence {

enum class CompositionDecision {
    Keep,
    Refine,
    Pivot,
    Abandon,
    SelectInitial
};

enum class CompositionEvidenceSource {
    ObservedBoard,
    UserProvided,
    Heuristic
};

// A read-only snapshot. Counts represent owned copies across board + bench.
struct OwnedUnitEvidence {
    std::int32_t champion_id{-1};
    std::int32_t copies{0};
    std::int32_t highest_star{1};
    std::vector<std::string> equipped_item_ids;
};

struct CandidateEvidence {
    std::string composition_id;
    // All fit values are normalized to [0,1]. They are deliberately explicit:
    // source_score is not mixed into this scale because OP.GG and native scores
    // do not share a calibration.
    double board_fit{0.5};
    double item_fit{0.5};
    double availability{0.5};
    double economy_feasibility{0.5};
    double estimated_gold_cost{0.0};
    double evidence_confidence{0.5};
    CompositionEvidenceSource source{CompositionEvidenceSource::Heuristic};
};

struct CompositionEvaluationContext {
    std::uint32_t round{0};
    std::int32_t level{1};
    std::int32_t gold{0};
    std::vector<OwnedUnitEvidence> owned_units;
    std::vector<CandidateEvidence> candidate_evidence;
};

struct CompositionScoreBreakdown {
    double board_fit{0.0};
    double ownership_fit{0.0};
    double item_fit{0.0};
    double availability{0.0};
    double economy_feasibility{0.0};
    double total{0.0};
    double confidence{0.0};
};

struct CompositionEvaluationConfig {
    double pivot_min_advantage{0.12};
    double refine_min_advantage{0.04};
    double abandon_below_score{0.22};
    double minimum_pivot_overlap{0.35};
    double maximum_transition_cost{8.0};
    std::uint32_t required_consecutive_rounds{2};
};

struct CompositionTransitionPlan {
    std::string from_composition_id;
    std::string to_composition_id;
    std::uint64_t expected_active_version{0};
    std::vector<std::int32_t> shared_unit_ids;
    std::vector<std::int32_t> bridge_unit_ids;
    std::vector<std::int32_t> replaceable_unit_ids;
    std::vector<std::int32_t> sell_candidate_unit_ids;
    std::vector<std::int32_t> item_risk_unit_ids;
    double overlap_ratio{0.0};
    double estimated_gold_cost{0.0};
    double transition_cost{0.0};
    double strategic_advantage{0.0};
    double confidence{0.0};
};

struct CompositionProposal {
    CompositionDecision decision{CompositionDecision::Keep};
    std::optional<CompositionCandidate> target;
    CompositionScoreBreakdown active_score;
    CompositionScoreBreakdown target_score;
    CompositionTransitionPlan transition;
    std::string reason;
    std::uint32_t evidence_streak{0};
    bool hysteresis_satisfied{false};
    bool approved{false};
};

class CompositionEvaluator {
public:
    explicit CompositionEvaluator(CompositionEvaluationConfig config = {})
        : config_(config) {}

    CompositionScoreBreakdown score(
        const CompositionCandidate& candidate,
        const CompositionEvaluationContext& context) const {
        CompositionScoreBreakdown out;
        const auto* evidence = evidence_for(candidate.composition_id, context);
        if (evidence) {
            out.board_fit = clamp01(evidence->board_fit);
            out.item_fit = clamp01(evidence->item_fit);
            out.availability = clamp01(evidence->availability);
            out.economy_feasibility = clamp01(evidence->economy_feasibility);
            out.confidence = clamp01(evidence->evidence_confidence);
        } else {
            out.board_fit = 0.5;
            out.item_fit = 0.5;
            out.availability = 0.5;
            out.economy_feasibility = 0.5;
            out.confidence = 0.25;
        }

        std::unordered_map<std::int32_t, const OwnedUnitEvidence*> owned;
        for (const auto& unit : context.owned_units)
            if (unit.champion_id >= 0 && unit.copies > 0)
                owned[unit.champion_id] = &unit;

        std::size_t owned_targets = 0;
        std::size_t core_targets = 0;
        std::size_t owned_core_targets = 0;
        for (const auto& unit : candidate.units) {
            const auto found = owned.find(unit.champion_id);
            if (found != owned.end()) {
                ++owned_targets;
                if (unit.core) ++owned_core_targets;
            }
            if (unit.core) ++core_targets;
        }
        const double target_count = static_cast<double>(candidate.units.size());
        const double owned_ratio = target_count > 0.0
            ? static_cast<double>(owned_targets) / target_count : 0.0;
        const double core_ratio = core_targets > 0
            ? static_cast<double>(owned_core_targets) / static_cast<double>(core_targets)
            : owned_ratio;
        out.ownership_fit = clamp01(0.65 * owned_ratio + 0.35 * core_ratio);
        out.total = 0.35 * out.board_fit + 0.25 * out.ownership_fit +
            0.15 * out.item_fit + 0.10 * out.availability +
            0.15 * out.economy_feasibility;
        return out;
    }

    CompositionProposal evaluate(
        const std::optional<ActiveComposition>& active,
        const std::vector<CompositionCandidate>& candidates,
        const CompositionEvaluationContext& context) const {
        CompositionProposal out;
        if (!active) {
            const CompositionCandidate* best = nullptr;
            double best_score = -1.0;
            for (const auto& candidate : candidates) {
                if (!ActiveCompositionManager::validate(candidate).empty()) continue;
                const auto candidate_score = score(candidate, context);
                if (candidate_score.total > best_score) {
                    best = &candidate;
                    best_score = candidate_score.total;
                    out.target_score = candidate_score;
                }
            }
            if (!best) {
                out.decision = CompositionDecision::Keep;
                out.reason = "No active composition and no valid candidate";
                return out;
            }
            out.decision = CompositionDecision::SelectInitial;
            out.target = *best;
            out.reason = "Select the highest-evidence valid initial composition";
            out.transition.to_composition_id = best->composition_id;
            out.transition.confidence = out.target_score.confidence;
            out.transition.strategic_advantage = out.target_score.total;
            out.transition.expected_active_version = 0;
            return out;
        }

        out.active_score = score(active->candidate, context);
        const CompositionCandidate* best = nullptr;
        double best_score = -1.0;
        for (const auto& candidate : candidates) {
            if (!ActiveCompositionManager::validate(candidate).empty()) continue;
            if (candidate.set_id != active->candidate.set_id) continue;
            const auto candidate_score = score(candidate, context);
            if (candidate_score.total > best_score) {
                best = &candidate;
                best_score = candidate_score.total;
                out.target_score = candidate_score;
            }
        }

        if (!best) {
            if (out.active_score.total < config_.abandon_below_score) {
                out.decision = CompositionDecision::Abandon;
                out.reason = "Active composition has insufficient evidence and no valid alternative exists";
            } else {
                out.decision = CompositionDecision::Keep;
                out.reason = "No valid same-Set alternative; preserve active composition";
            }
            return out;
        }

        out.target = *best;
        out.transition.from_composition_id = active->candidate.composition_id;
        out.transition.to_composition_id = best->composition_id;
        out.transition.expected_active_version = active->version;
        out.transition.strategic_advantage = best_score - out.active_score.total;
        out.transition.confidence = std::min(out.target_score.confidence,
            clamp01(0.5 + std::abs(out.transition.strategic_advantage)));

        const auto active_ids = ids(active->candidate);
        const auto target_ids = ids(*best);
        std::size_t shared = 0;
        for (const auto id : target_ids)
            if (active_ids.count(id)) ++shared;
        const auto denominator = std::max<std::size_t>(1,
            std::min(active_ids.size(), target_ids.size()));
        out.transition.overlap_ratio = static_cast<double>(shared) /
            static_cast<double>(denominator);

        const bool same_id = best->composition_id == active->candidate.composition_id;
        const bool materially_changed = !same_id &&
            out.transition.overlap_ratio < config_.minimum_pivot_overlap;
        if (materially_changed &&
            out.transition.strategic_advantage >= config_.pivot_min_advantage) {
            out.decision = CompositionDecision::Pivot;
            out.reason = "A complete alternative composition has a material evidence advantage";
        } else if (out.transition.strategic_advantage >= config_.refine_min_advantage &&
                   (same_id || out.transition.overlap_ratio >= config_.minimum_pivot_overlap)) {
            out.decision = CompositionDecision::Refine;
            out.reason = "A compatible refinement improves the active composition";
        } else if (out.active_score.total < config_.abandon_below_score &&
                   best_score < config_.abandon_below_score) {
            out.decision = CompositionDecision::Abandon;
            out.target.reset();
            out.reason = "Neither active nor alternative composition has sufficient evidence";
        } else {
            out.decision = CompositionDecision::Keep;
            out.target.reset();
            out.reason = "Alternative does not clear the strategic hysteresis margin";
        }
        return out;
    }

private:
    static double clamp01(double value) noexcept {
        return std::isfinite(value) ? std::clamp(value, 0.0, 1.0) : 0.0;
    }
    static const CandidateEvidence* evidence_for(
        const std::string& id, const CompositionEvaluationContext& context) {
        const auto it = std::find_if(context.candidate_evidence.begin(),
            context.candidate_evidence.end(),
            [&](const auto& evidence) { return evidence.composition_id == id; });
        return it == context.candidate_evidence.end() ? nullptr : &*it;
    }
    static std::unordered_set<std::int32_t> ids(const CompositionCandidate& candidate) {
        std::unordered_set<std::int32_t> result;
        for (const auto& unit : candidate.units) result.insert(unit.champion_id);
        return result;
    }
    CompositionEvaluationConfig config_;
};

class TransitionManager {
public:
    explicit TransitionManager(CompositionEvaluationConfig config = {})
        : config_(config), evaluator_(config) {}

    CompositionProposal propose(
        const std::optional<ActiveComposition>& active,
        const std::vector<CompositionCandidate>& candidates,
        const CompositionEvaluationContext& context) {
        auto proposal = evaluator_.evaluate(active, candidates, context);
        if (!proposal.target || (proposal.decision != CompositionDecision::Pivot &&
            proposal.decision != CompositionDecision::Refine &&
            proposal.decision != CompositionDecision::SelectInitial)) {
            reset_hysteresis();
            return proposal;
        }

        const auto& target = *proposal.target;
        if (proposal.decision == CompositionDecision::SelectInitial) {
            proposal.hysteresis_satisfied = true;
            proposal.evidence_streak = 1;
        } else {
            if (target.composition_id != pending_candidate_id_) {
                pending_candidate_id_ = target.composition_id;
                evidence_streak_ = 1;
                last_evidence_round_ = context.round;
            } else if (context.round > last_evidence_round_) {
                ++evidence_streak_;
                last_evidence_round_ = context.round;
            }
            proposal.evidence_streak = evidence_streak_;
            proposal.hysteresis_satisfied =
                evidence_streak_ >= std::max<std::uint32_t>(1, config_.required_consecutive_rounds);
        }

        build_transition_plan(proposal, active, context);
        const bool affordable = proposal.transition.estimated_gold_cost <=
            static_cast<double>(std::max(0, context.gold));
        const bool within_cost = proposal.transition.transition_cost <=
            config_.maximum_transition_cost;
        proposal.approved = proposal.hysteresis_satisfied && affordable && within_cost &&
            proposal.transition.confidence >= 0.5;
        if (!proposal.hysteresis_satisfied)
            proposal.reason += "; awaiting consecutive-round evidence";
        else if (!affordable)
            proposal.reason += "; estimated gold cost exceeds available gold";
        else if (!within_cost)
            proposal.reason += "; transition cost exceeds configured limit";
        else if (!proposal.approved)
            proposal.reason += "; confidence is insufficient";
        return proposal;
    }

    // The ActiveCompositionManager remains the only publication authority.
    // This method is an explicit gate and rejects stale proposals by version.
    PublishResult publish_if_approved(
        const CompositionProposal& proposal,
        ActiveCompositionManager& active_manager) const {
        if (!proposal.approved || !proposal.target ||
            (proposal.decision != CompositionDecision::SelectInitial &&
             proposal.decision != CompositionDecision::Pivot &&
             proposal.decision != CompositionDecision::Refine)) {
            return {PublishStatus::RejectedInvalidCandidate,
                "transition proposal is not approved", active_manager.current().value_or(ActiveComposition{}),
                false, {}};
        }
        const auto current_version = active_manager.current()
            ? active_manager.current()->version : 0;
        if (current_version != proposal.transition.expected_active_version) {
            return {PublishStatus::RejectedInvalidCandidate,
                "stale transition proposal: active composition version changed",
                active_manager.current().value_or(ActiveComposition{}), false, {}};
        }
        const auto reason = proposal.decision == CompositionDecision::Refine
            ? CompositionTransitionReason::Refinement
            : (proposal.decision == CompositionDecision::SelectInitial
                ? CompositionTransitionReason::InitialSelection
                : CompositionTransitionReason::StrategicPivot);
        return active_manager.publish(*proposal.target, reason);
    }

private:
    static std::unordered_set<std::int32_t> ids(const CompositionCandidate& candidate) {
        std::unordered_set<std::int32_t> result;
        for (const auto& unit : candidate.units) result.insert(unit.champion_id);
        return result;
    }
    static const OwnedUnitEvidence* owned(
        std::int32_t id, const CompositionEvaluationContext& context) {
        const auto it = std::find_if(context.owned_units.begin(), context.owned_units.end(),
            [&](const auto& unit) { return unit.champion_id == id && unit.copies > 0; });
        return it == context.owned_units.end() ? nullptr : &*it;
    }
    void build_transition_plan(
        CompositionProposal& proposal,
        const std::optional<ActiveComposition>& active,
        const CompositionEvaluationContext& context) const {
        if (!proposal.target) return;
        auto& plan = proposal.transition;
        const auto target_ids = ids(*proposal.target);
        std::unordered_set<std::int32_t> active_ids;
        if (active) active_ids = ids(active->candidate);

        std::size_t missing_target = 0;
        for (const auto id : target_ids) {
            if (active_ids.count(id)) plan.shared_unit_ids.push_back(id);
            if (owned(id, context)) {
                if (!active_ids.count(id)) plan.bridge_unit_ids.push_back(id);
            } else {
                ++missing_target;
            }
        }
        if (active) {
            for (const auto id : active_ids) {
                if (target_ids.count(id)) continue;
                plan.replaceable_unit_ids.push_back(id);
                if (const auto* unit = owned(id, context)) {
                    plan.sell_candidate_unit_ids.push_back(id);
                    if (!unit->equipped_item_ids.empty())
                        plan.item_risk_unit_ids.push_back(id);
                }
            }
        }
        const auto sort = [](auto& values) { std::sort(values.begin(), values.end()); };
        sort(plan.shared_unit_ids);
        sort(plan.bridge_unit_ids);
        sort(plan.replaceable_unit_ids);
        sort(plan.sell_candidate_unit_ids);
        sort(plan.item_risk_unit_ids);

        const double item_risk = static_cast<double>(plan.item_risk_unit_ids.size());
        const double owned_replacements = static_cast<double>(plan.sell_candidate_unit_ids.size());
        const double target_size = static_cast<double>(std::max<std::size_t>(1, target_ids.size()));
        plan.estimated_gold_cost = static_cast<double>(missing_target) * 3.0;
        if (const auto it = std::find_if(context.candidate_evidence.begin(),
            context.candidate_evidence.end(), [&](const auto& e) {
                return e.composition_id == proposal.target->composition_id;
            }); it != context.candidate_evidence.end() && it->estimated_gold_cost >= 0.0) {
            plan.estimated_gold_cost = it->estimated_gold_cost;
        }
        plan.transition_cost = static_cast<double>(missing_target) +
            0.5 * owned_replacements + 0.75 * item_risk;
        plan.transition_cost += 0.25 * (1.0 - plan.overlap_ratio) * target_size;
    }

    void reset_hysteresis() noexcept {
        pending_candidate_id_.clear();
        evidence_streak_ = 0;
        last_evidence_round_ = 0;
    }

    CompositionEvaluationConfig config_;
    CompositionEvaluator evaluator_;
    std::string pending_candidate_id_;
    std::uint32_t evidence_streak_{0};
    std::uint32_t last_evidence_round_{0};
};

} // namespace tft::composition_intelligence
