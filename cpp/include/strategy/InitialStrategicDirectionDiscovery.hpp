#pragma once

// Shadow-only discovery of early composition direction hypotheses.
// This module consumes an already assembled read-only snapshot. It does not
// mutate game state or connect to PPO, observations, masks, actions, or rules.

#include "strategy/StrategicAnchorContracts.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

namespace tft::strategy {

enum class DirectionDiscoveryStatus : std::uint8_t {
    NotEvaluated = 0,
    HypothesesFound = 1,
    InsufficientEvidence = 2,
    CompositionBound = 3,
    InvalidInput = 4
};

struct DirectionDiscoveryUnit {
    std::int32_t champion_id{-1};
    std::int32_t cost{0};
    std::int32_t copies_owned{0};
    std::int32_t star{1};
    bool on_board{false};
    bool on_bench{false};
    bool in_shop{false};
    bool carry_potential{false};
    bool core_potential{false};
    double board_contribution{0.0};
    std::vector<std::string> traits;
    // -1 means the native pool snapshot is unavailable.
    std::int32_t pool_remaining{-1};
};

struct DirectionDiscoveryTrait {
    std::string trait;
    std::int32_t activation_threshold{2};
};

struct DirectionDiscoveryInput {
    std::uint32_t round{0};
    // -1 means the economy snapshot did not provide a trustworthy gold value.
    std::int32_t gold_available{-1};
    bool composition_defined{false};
    std::string active_composition_identity;
    std::vector<DirectionDiscoveryUnit> units;
    std::vector<DirectionDiscoveryTrait> trait_thresholds;
    std::string previous_direction;
    std::size_t maximum_hypotheses{3};
};

struct DirectionDiscoveryHypothesis {
    StrategicDirectionAnchor anchor;
    double score{0.0};
    std::int32_t supporting_unit_count{0};
    std::int32_t owned_copies{0};
    std::int32_t shop_copies{0};
    std::int32_t synergy_owned_count{0};
    std::int32_t synergy_reachable_count{0};
    bool synergy_reachable{false};
    std::string score_explanation;
};

struct DirectionDiscoveryResult {
    DirectionDiscoveryStatus status{DirectionDiscoveryStatus::NotEvaluated};
    std::vector<DirectionDiscoveryHypothesis> hypotheses;
    std::string reason{"not_evaluated"};
    bool shadow_only{true};
};

class InitialStrategicDirectionDiscovery {
public:
    DirectionDiscoveryResult evaluate(const DirectionDiscoveryInput& input) const {
        DirectionDiscoveryResult out;

        // A defined composition owns direction selection. Early exploration
        // must stop rather than compete with or overwrite that direction.
        if (input.composition_defined || !input.active_composition_identity.empty()) {
            out.status = DirectionDiscoveryStatus::CompositionBound;
            out.reason = "active_composition_owns_direction_selection";
            return out;
        }
        if (input.maximum_hypotheses == 0) {
            out.status = DirectionDiscoveryStatus::InvalidInput;
            out.reason = "maximum_hypotheses_is_zero";
            return out;
        }

        std::map<std::string, DirectionDiscoveryTrait> thresholds;
        for (const auto& t : input.trait_thresholds) {
            if (!t.trait.empty() && t.activation_threshold > 0)
                thresholds[t.trait] = t;
        }

        struct Aggregate {
            std::set<std::int32_t> owned_units;
            std::set<std::int32_t> supported_units;
            std::set<std::int32_t> shop_units;
            std::int32_t copies{0};
            std::int32_t shop_copies{0};
            double board_value{0.0};
            bool pair{false};
            bool board{false};
            bool bench{false};
            std::int32_t highest_star{1};
            std::int32_t pool_remaining{0};
            bool pool_known{false};
            bool carry{false};
            bool core{false};
            std::int32_t cheapest_cost{0};
        };
        std::map<std::string, Aggregate> by_trait;
        std::set<std::int32_t> seen_ids;

        for (const auto& unit : input.units) {
            if (unit.champion_id < 0 || unit.copies_owned < 0 ||
                unit.cost < 0 || unit.star < 1 || unit.star > 3 ||
                unit.pool_remaining < -1 ||
                !std::isfinite(unit.board_contribution)) {
                out.status = DirectionDiscoveryStatus::InvalidInput;
                out.reason = "invalid_unit_evidence";
                return out;
            }
            if (!seen_ids.insert(unit.champion_id).second) {
                out.status = DirectionDiscoveryStatus::InvalidInput;
                out.reason = "duplicate_champion_evidence_must_be_aggregated";
                return out;
            }
            std::set<std::string> unique_traits(unit.traits.begin(), unit.traits.end());
            for (const auto& trait : unique_traits) {
                if (trait.empty()) continue;
                auto& a = by_trait[trait];
                const bool owned = unit.copies_owned > 0 || unit.on_board || unit.on_bench;
                if (owned) {
                    a.owned_units.insert(unit.champion_id);
                    a.supported_units.insert(unit.champion_id);
                    a.copies += std::max(unit.copies_owned, 1);
                    a.board_value += std::max(0.0, unit.board_contribution);
                    a.pair = a.pair || unit.copies_owned >= 2;
                    a.board = a.board || unit.on_board;
                    a.bench = a.bench || unit.on_bench;
                    a.highest_star = std::max(a.highest_star, unit.star);
                    a.carry = a.carry || unit.carry_potential;
                    a.core = a.core || unit.core_potential;
                    if (a.cheapest_cost == 0 || unit.cost < a.cheapest_cost)
                        a.cheapest_cost = unit.cost;
                }
                if (unit.pool_remaining >= 0) {
                    a.pool_known = true;
                    a.pool_remaining += unit.pool_remaining;
                }
                if (unit.in_shop) {
                    a.shop_units.insert(unit.champion_id);
                    a.shop_copies += 1;
                }
            }
        }

        for (const auto& [trait, a] : by_trait) {
            // A lone shop offer or an isolated owned unit is not a direction.
            // Require multiple owned references, or a concrete owned pair.
            if (a.owned_units.empty() ||
                (a.owned_units.size() < 2 && !a.pair)) continue;

            const auto threshold_it = thresholds.find(trait);
            const std::int32_t threshold = threshold_it == thresholds.end()
                ? 2 : threshold_it->second.activation_threshold;
            const auto owned_count = static_cast<std::int32_t>(a.owned_units.size());
            const auto reachable = owned_count +
                static_cast<std::int32_t>(a.shop_units.size());
            const bool synergy_reachable = reachable >= threshold;
            const bool synergy_owned = owned_count >= threshold;

            // Score components are intentionally transparent and bounded.
            // Shop contributes only when there is already owned support.
            const double pair_score = a.pair ? 2.0 : 0.0;
            const double support_score = std::min(2.0, owned_count * 0.75);
            const double star_progress_score = a.highest_star >= 3 ? 0.75 :
                (a.highest_star == 2 ? 0.50 : 0.0);
            // A known available pool modestly supports continued pursuit.
            // Unknown pool data is neutral, never interpreted as exhaustion.
            const double pool_score = a.pool_known
                ? std::min(0.50, a.pool_remaining * 0.025) : 0.0;
            const double synergy_score = synergy_owned ? 1.5 :
                (synergy_reachable && !a.shop_units.empty() ? 0.75 : 0.0);
            const double shop_score = std::min(0.5, a.shop_units.size() * 0.25);
            const double carry_score = a.carry ? 1.0 : 0.0;
            const double core_score = a.core ? 0.75 : 0.0;
            const double board_score = std::min(0.5, a.board_value * 0.1);
            const auto missing_for_synergy = std::max(0, threshold - reachable);
            const double estimated_pursuit_cost =
                static_cast<double>(missing_for_synergy * a.cheapest_cost);
            const double cost_penalty = std::min(0.75, a.cheapest_cost * 0.08);
            const double affordability_penalty =
                input.gold_available >= 0 && estimated_pursuit_cost > input.gold_available
                    ? std::min(1.0, (estimated_pursuit_cost - input.gold_available) * 0.1)
                    : 0.0;
            const double score = pair_score + support_score + star_progress_score +
                pool_score + synergy_score + shop_score + carry_score + core_score + board_score -
                cost_penalty - affordability_penalty;

            // Convert the explainable heuristic score to a ranking confidence,
            // not a calibrated probability.
            const double confidence = std::clamp(score / 7.0, 0.0, 0.95);
            if (confidence < 0.30) continue;

            DirectionDiscoveryHypothesis h;
            h.anchor.identity = "direction:early:" + trait + ":" +
                std::to_string(input.round);
            h.anchor.direction = trait;
            h.anchor.confidence = confidence;
            h.anchor.lifecycle = StrategicAnchorLifecycle::Proposed;
            h.anchor.composition_bound = false;
            h.anchor.reason = "early_evidence:" + trait;
            h.anchor.reference_unit_ids.assign(a.owned_units.begin(), a.owned_units.end());
            if (!a.owned_units.empty())
                h.anchor.evidence.push_back(StrategicAnchorEvidenceKind::OwnedUnit);
            if (a.board)
                h.anchor.evidence.push_back(StrategicAnchorEvidenceKind::BoardUnit);
            if (a.bench)
                h.anchor.evidence.push_back(StrategicAnchorEvidenceKind::BenchUnit);
            if (a.pair)
                h.anchor.evidence.push_back(StrategicAnchorEvidenceKind::PairProgress);
            if (!a.shop_units.empty())
                h.anchor.evidence.push_back(StrategicAnchorEvidenceKind::ShopOffer);
            if (synergy_reachable)
                h.anchor.evidence.push_back(StrategicAnchorEvidenceKind::TraitCompletion);
            if (a.core)
                h.anchor.evidence.push_back(StrategicAnchorEvidenceKind::CompositionCore);

            h.score = score;
            h.supporting_unit_count = owned_count;
            h.owned_copies = a.copies;
            h.shop_copies = a.shop_copies;
            h.synergy_owned_count = owned_count;
            h.synergy_reachable_count = reachable;
            h.synergy_reachable = synergy_reachable;
            h.score_explanation =
                "pair=" + std::to_string(pair_score) +
                ";owned_support=" + std::to_string(support_score) +
                ";star_progress=" + std::to_string(star_progress_score) +
                ";pool_remaining=" + (a.pool_known ? std::to_string(a.pool_remaining) : "unknown") +
                ";pool_score=" + std::to_string(pool_score) +
                ";synergy=" + std::to_string(synergy_score) +
                ";shop=" + std::to_string(shop_score) +
                ";carry=" + std::to_string(carry_score) +
                ";core=" + std::to_string(core_score) +
                ";board=" + std::to_string(board_score) +
                ";estimated_pursuit_cost=" + std::to_string(estimated_pursuit_cost) +
                ";cost_penalty=" + std::to_string(cost_penalty) +
                ";affordability_penalty=" + std::to_string(affordability_penalty);
            out.hypotheses.push_back(std::move(h));
        }

        std::sort(out.hypotheses.begin(), out.hypotheses.end(),
            [](const auto& lhs, const auto& rhs) {
                if (lhs.score != rhs.score) return lhs.score > rhs.score;
                return lhs.anchor.direction < rhs.anchor.direction;
            });

        // Small score differences should not cause direction churn. Preserve
        // the previous direction when it remains a viable near-top hypothesis.
        if (!input.previous_direction.empty() && !out.hypotheses.empty()) {
            const auto previous = std::find_if(out.hypotheses.begin(),
                out.hypotheses.end(), [&](const auto& h) {
                    return h.anchor.direction == input.previous_direction;
                });
            if (previous != out.hypotheses.end() &&
                out.hypotheses.front().score - previous->score <= 0.75 &&
                previous != out.hypotheses.begin()) {
                std::rotate(out.hypotheses.begin(), previous, previous + 1);
            }
        }

        if (out.hypotheses.size() > input.maximum_hypotheses)
            out.hypotheses.resize(input.maximum_hypotheses);
        if (out.hypotheses.empty()) {
            out.status = DirectionDiscoveryStatus::InsufficientEvidence;
            out.reason = "no_direction_has_sufficient_owned_support";
        } else {
            out.status = DirectionDiscoveryStatus::HypothesesFound;
            out.reason = "ranked_from_owned_pairs_synergy_and_unit_potential";
        }
        return out;
    }
};

} // namespace tft::strategy
