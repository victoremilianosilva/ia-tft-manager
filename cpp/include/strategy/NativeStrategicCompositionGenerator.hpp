#pragma once

// Independent candidate/lineup generation for the new strategic architecture.
// This service consumes observed game facts only and has no dependency on
// CompositionPlanner, CompositionDirectionPolicy, or StrategyInfo.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace tft::strategy {

struct NativeCompositionUnitDefinition {
    std::int32_t champion_id{-1};
    std::string key;
    std::int32_t cost{0};
    std::vector<std::string> traits;
    bool carry{false};
    bool frontline{false};
    bool support{false};
};

struct NativeCompositionOwnedUnit {
    std::int32_t champion_id{-1};
    std::int32_t copies{0};
    std::int32_t star{1};
    bool on_board{false};
    bool on_bench{false};
    double board_contribution{0.0};
    double item_fit{0.0};
};

struct NativeCompositionTraitThreshold {
    std::string trait;
    std::int32_t units{0};
};

struct NativeCompositionGenerationInput {
    std::vector<NativeCompositionUnitDefinition> catalog;
    std::vector<NativeCompositionOwnedUnit> owned;
    std::unordered_set<std::int32_t> shop_ids;
    std::unordered_map<std::int32_t, std::int32_t> pool_remaining;
    std::vector<NativeCompositionTraitThreshold> trait_thresholds;
    std::vector<std::int32_t> currently_owned_unit_ids;
    std::int32_t level{1};
    std::int32_t gold{0};
    std::int32_t target_slots{8};
    std::size_t maximum_candidates{8};
};

struct NativeGeneratedComposition {
    std::string identity;
    std::string direction;
    std::vector<std::int32_t> unit_ids;
    std::int32_t anchor_champion_id{-1};
    std::int32_t main_carry_id{-1};
    std::vector<std::string> completed_traits;
    std::vector<std::string> evidence;
    double score{0.0};
    double transition_cost{0.0};
    std::int32_t reusable_owned_units{0};
    bool anchor_available_in_shop{false};
};

struct NativeCompositionGenerationResult {
    std::vector<NativeGeneratedComposition> candidates;
    std::uint32_t directions_considered{0};
    std::uint32_t rejected_missing_pool_data{0};
    std::string reason{"not_evaluated"};
};

class NativeStrategicCompositionGenerator {
public:
    NativeCompositionGenerationResult generate(
        const NativeCompositionGenerationInput& input) const {
        NativeCompositionGenerationResult result;
        if (input.catalog.empty() || input.target_slots <= 0 ||
            input.maximum_candidates == 0) {
            result.reason = "insufficient_catalog_or_capacity";
            return result;
        }

        std::unordered_map<std::int32_t, NativeCompositionOwnedUnit> owned;
        std::unordered_map<std::int32_t, const NativeCompositionUnitDefinition*> definitions;
        std::map<std::string, std::int32_t> direction_evidence;
        std::map<std::string, std::int32_t> thresholds;
        for (const auto& unit : input.catalog) {
            if (unit.champion_id < 0 || unit.cost < 1 || unit.cost > 5) continue;
            definitions[unit.champion_id] = &unit;
        }
        for (const auto& unit : input.owned) {
            if (unit.champion_id < 0 || unit.copies < 0 || unit.star < 1 ||
                unit.star > 3 || !std::isfinite(unit.board_contribution) ||
                !std::isfinite(unit.item_fit)) continue;
            owned[unit.champion_id] = unit;
            const auto found = definitions.find(unit.champion_id);
            if (found != definitions.end()) {
                for (const auto& trait : found->second->traits)
                    if (!trait.empty()) ++direction_evidence[trait];
            }
        }
        for (const auto id : input.shop_ids) {
            const auto found = definitions.find(id);
            if (found == definitions.end()) continue;
            for (const auto& trait : found->second->traits)
                if (!trait.empty()) ++direction_evidence[trait];
        }
        for (const auto& threshold : input.trait_thresholds)
            if (!threshold.trait.empty() && threshold.units > 0)
                thresholds[threshold.trait] = threshold.units;

        std::vector<std::string> directions;
        for (const auto& [trait, evidence] : direction_evidence)
            if (evidence > 0) directions.push_back(trait);
        std::stable_sort(directions.begin(), directions.end(),
            [&](const auto& lhs, const auto& rhs) {
                if (direction_evidence[lhs] != direction_evidence[rhs])
                    return direction_evidence[lhs] > direction_evidence[rhs];
                return lhs < rhs;
            });

        const auto effective_target_slots = static_cast<std::size_t>(
            std::clamp(std::min(input.target_slots, input.level), 1, 10));

        struct ScoredUnit {
            const NativeCompositionUnitDefinition* definition{nullptr};
            double score{0.0};
            bool owned{false};
            bool shop{false};
        };

        for (const auto& direction : directions) {
            if (result.candidates.size() >= input.maximum_candidates) break;
            ++result.directions_considered;
            std::vector<ScoredUnit> scored;
            for (const auto& [id, definition] : definitions) {
                if (std::find(definition->traits.begin(), definition->traits.end(),
                              direction) == definition->traits.end()) continue;
                const auto owned_it = owned.find(id);
                const bool has_owned = owned_it != owned.end();
                const bool in_shop = input.shop_ids.count(id) != 0;
                const auto pool_it = input.pool_remaining.find(id);
                const bool pool_known = pool_it != input.pool_remaining.end() &&
                    pool_it->second >= 0;
                if (pool_known && pool_it->second == 0 && !has_owned && !in_shop)
                    continue;
                if (!pool_known) ++result.rejected_missing_pool_data;

                const auto& observed = has_owned
                    ? owned_it->second : NativeCompositionOwnedUnit{};
                const double copies = has_owned
                    ? std::min(5, observed.copies) * 0.65 : 0.0;
                const double pair_progress = has_owned && observed.copies >= 2 ? 1.1 : 0.0;
                const double star_progress = has_owned
                    ? (observed.star >= 3 ? 0.9 : observed.star == 2 ? 0.55 : 0.0)
                    : 0.0;
                const double location = has_owned
                    ? (observed.on_board ? 0.85 : observed.on_bench ? 0.55 : 0.0)
                    : 0.0;
                const double pool_score = pool_known
                    ? std::min(0.45, pool_it->second * 0.02) : 0.0;
                const double cost_score = definition->cost * 0.10;
                const double affordability = definition->cost <= input.gold ? 0.25 : -0.20;
                const double score = copies + pair_progress + star_progress + location +
                    (in_shop ? 0.65 : 0.0) + (definition->carry ? 1.15 : 0.0) +
                    (definition->frontline ? 0.45 : 0.0) +
                    (definition->support ? 0.25 : 0.0) + pool_score +
                    cost_score + affordability +
                    (has_owned ? std::max(0.0, observed.board_contribution) * 0.35 : 0.0) +
                    (has_owned ? std::max(0.0, observed.item_fit) * 0.25 : 0.0);
                scored.push_back({definition, score, has_owned, in_shop});
            }
            std::stable_sort(scored.begin(), scored.end(),
                [](const ScoredUnit& lhs, const ScoredUnit& rhs) {
                    if (lhs.score != rhs.score) return lhs.score > rhs.score;
                    return lhs.definition->champion_id < rhs.definition->champion_id;
                });
            if (scored.empty()) continue;

            NativeGeneratedComposition candidate;
            candidate.direction = direction;
            candidate.identity = "native:" + direction;
            bool has_carry = false;
            bool has_frontline = false;
            bool has_support = false;
            for (const auto& unit : scored) {
                if (candidate.unit_ids.size() >= effective_target_slots) break;
                candidate.unit_ids.push_back(unit.definition->champion_id);
                candidate.score += unit.score;
                if (unit.owned) {
                    ++candidate.reusable_owned_units;
                    const auto id = unit.definition->champion_id;
                    candidate.evidence.push_back("owned_unit:" + std::to_string(id));
                    const auto& observed = owned.at(id);
                    if (observed.copies >= 2)
                        candidate.evidence.push_back("owned_pair:" + std::to_string(id));
                    if (observed.star >= 2)
                        candidate.evidence.push_back("star_progress:" +
                            std::to_string(observed.star) + ":" + std::to_string(id));
                    if (observed.item_fit > 0.0)
                        candidate.evidence.push_back("item_fit:" + std::to_string(id));
                }
                if (unit.shop)
                    candidate.evidence.push_back("shop_offer:" +
                        std::to_string(unit.definition->champion_id));
                const auto pool_fact = input.pool_remaining.find(
                    unit.definition->champion_id);
                if (pool_fact == input.pool_remaining.end() || pool_fact->second < 0) {
                    candidate.evidence.push_back("pool_unknown:" +
                        std::to_string(unit.definition->champion_id));
                } else {
                    candidate.evidence.push_back("pool_remaining:" +
                        std::to_string(pool_fact->second) + ":" +
                        std::to_string(unit.definition->champion_id));
                }
                if (unit.definition->carry && !has_carry) {
                    candidate.main_carry_id = unit.definition->champion_id;
                    has_carry = true;
                }
                has_frontline = has_frontline || unit.definition->frontline;
                has_support = has_support || unit.definition->support;
                if (unit.shop && candidate.anchor_champion_id < 0) {
                    candidate.anchor_champion_id = unit.definition->champion_id;
                    candidate.anchor_available_in_shop = true;
                }
            }
            if (candidate.anchor_champion_id < 0) {
                for (const auto& unit : scored) {
                    if (unit.owned) {
                        candidate.anchor_champion_id = unit.definition->champion_id;
                        break;
                    }
                }
            }
            if (candidate.anchor_champion_id < 0)
                candidate.anchor_champion_id = candidate.unit_ids.front();

            std::set<std::string> active_traits;
            for (const auto id : candidate.unit_ids) {
                const auto found = definitions.find(id);
                if (found == definitions.end()) continue;
                for (const auto& trait : found->second->traits)
                    if (!trait.empty()) active_traits.insert(trait);
            }
            for (const auto& trait : active_traits) {
                const auto count = static_cast<std::int32_t>(std::count_if(
                    candidate.unit_ids.begin(), candidate.unit_ids.end(),
                    [&](std::int32_t id) {
                        const auto found = definitions.find(id);
                        return found != definitions.end() &&
                            std::find(found->second->traits.begin(),
                                      found->second->traits.end(), trait) !=
                                found->second->traits.end();
                    }));
                const auto threshold = thresholds.find(trait);
                if (threshold != thresholds.end() && count >= threshold->second)
                    candidate.completed_traits.push_back(trait);
            }
            if (std::find(candidate.completed_traits.begin(),
                          candidate.completed_traits.end(), direction) !=
                candidate.completed_traits.end())
                candidate.score += 1.0;
            if (has_carry) candidate.evidence.push_back("carry_role_present");
            if (has_frontline) candidate.evidence.push_back("frontline_role_present");
            if (has_support) candidate.evidence.push_back("support_role_present");
            if (!candidate.completed_traits.empty())
                candidate.evidence.push_back("trait_milestone_reached");

            std::size_t overlap = 0;
            std::unordered_set<std::int32_t> current(
                input.currently_owned_unit_ids.begin(), input.currently_owned_unit_ids.end());
            for (const auto id : candidate.unit_ids)
                if (current.count(id)) ++overlap;
            const auto union_size = current.size() + candidate.unit_ids.size() - overlap;
            candidate.transition_cost = union_size == 0 ? 0.0 :
                1.0 - static_cast<double>(overlap) /
                    static_cast<double>(union_size);
            candidate.identity += ":";
            for (std::size_t index = 0; index < candidate.unit_ids.size(); ++index) {
                if (index != 0) candidate.identity += ",";
                candidate.identity += std::to_string(candidate.unit_ids[index]);
            }
            result.candidates.push_back(std::move(candidate));
        }

        std::stable_sort(result.candidates.begin(), result.candidates.end(),
            [](const auto& lhs, const auto& rhs) {
                if (lhs.score != rhs.score) return lhs.score > rhs.score;
                return lhs.direction < rhs.direction;
            });
        result.reason = result.candidates.empty()
            ? "no_candidate_from_observed_traits" : "native_candidates_generated";
        return result;
    }
};

} // namespace tft::strategy
