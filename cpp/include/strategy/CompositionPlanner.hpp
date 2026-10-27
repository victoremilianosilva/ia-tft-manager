#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <limits>
#include <cstdlib>
#include <fstream>
#include <nlohmann/json.hpp>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include "lobby/TftEngine.hpp"
#include "lobby/ShopEngine.hpp"

namespace tft::strategy {

// A flexible target lineup derived from the current direction and the full
// champion pool. The direction is an anchor, not a requirement that every slot
// belong to the same trait.
struct CompositionPlan {
    std::vector<std::int32_t> unit_ids;
    std::vector<std::string> unit_names;
    std::vector<std::string> core_traits;
    std::int32_t main_carry_id{-1};
    double score{0.0};
    std::vector<std::string> acquisition_notes;
};

class CompositionPlanner {
public:
    // Levels 1-8 share a stable eight-unit target. At levels 9/10 the planner
    // expands to the actual level and is recomputed from the latest game state.
    static std::size_t target_slots_for_level(int level) noexcept {
        return level <= 8 ? 8U
            : static_cast<std::size_t>(std::clamp(level, 9, 10));
    }

    using TraitMilestones = std::unordered_map<std::string, std::vector<int>>;
    using OwnedCopies = std::unordered_map<std::int32_t, int>;
    using FocusWeights = std::vector<std::pair<std::string, double>>;
    using AvailableCopies = std::unordered_map<std::int32_t, int>;

    static CompositionPlan build(
        const std::vector<ChampionDefinition>& pool,
        const TraitMilestones& milestones,
        const std::string& direction,
        const FocusWeights& focus_weights,
        const OwnedCopies& owned_copies,
        std::size_t requested_slots,
        int current_level = 1,
        const AvailableCopies& available_copies = {},
        const std::unordered_set<std::int32_t>& currently_offered = {}) {
        CompositionPlan plan;
        if (pool.empty() || requested_slots == 0) return plan;

        const std::size_t slots = std::min<std::size_t>(requested_slots, 10);
        const int safe_level = std::clamp(current_level, 1, 10);
        const auto& shop_odds = tft::ShopEngine::odds_by_level();
        std::array<double, 5> available_by_cost{};
        for (const auto& champion : pool) {
            const auto found = available_copies.find(champion.internal_id);
            if (found != available_copies.end() && champion.cost >= 1 && champion.cost <= 5)
                available_by_cost[static_cast<std::size_t>(champion.cost - 1)] += std::max(0, found->second);
        }
        const auto chance_per_shop_at_level = [&](const ChampionDefinition& champion, int level) {
            if (champion.cost < 1 || champion.cost > 5) return 0.0;
            const auto available = available_copies.find(champion.internal_id);
            const double copies = available == available_copies.end()
                ? 0.0 : static_cast<double>(std::max(0, available->second));
            const double tier_total = available_by_cost[static_cast<std::size_t>(champion.cost - 1)];
            const double tier_odds = shop_odds[static_cast<std::size_t>(std::clamp(level, 1, 10) - 1)]
                [static_cast<std::size_t>(champion.cost - 1)];
            if (copies <= 0.0 || tier_total <= 0.0 || tier_odds <= 0.0) return 0.0;
            const double per_slot = tier_odds * copies / tier_total;
            return 1.0 - std::pow(1.0 - std::clamp(per_slot, 0.0, 1.0), 5.0);
        };
        const auto acquisition = [&](const ChampionDefinition& champion) {
            if (currently_offered.count(champion.internal_id) != 0)
                return std::pair<double, double>{1.0, 0.0};
            const auto owned = owned_copies.find(champion.internal_id);
            if (owned != owned_copies.end() && owned->second > 0)
                return std::pair<double, double>{1.0, 0.0};
            if (available_copies.empty() || champion.cost < 1 || champion.cost > 5)
                return std::pair<double, double>{1.0, 0.0};
            const auto available = available_copies.find(champion.internal_id);
            const double copies = available == available_copies.end()
                ? 0.0 : static_cast<double>(std::max(0, available->second));
            const double tier_total = available_by_cost[static_cast<std::size_t>(champion.cost - 1)];
            if (copies <= 0.0 || tier_total <= 0.0)
                return std::pair<double, double>{0.0, 4.5};

            // A composition is a forward-looking plan, not a demand to buy every
            // unit at the current level. Blend current and near-future shop odds
            // so a unit that becomes easier after leveling is not over-penalized.
            const int horizon_end = std::min(10, safe_level + 2);
            const int future_levels = horizon_end - safe_level;
            double horizon_probability = 0.5 * chance_per_shop_at_level(champion, safe_level);

            // Give the current level and the future outlook equal influence.
            // Split the future half across the next two levels when both exist;
            // near level 10, renormalize over the future levels that remain.
            if (future_levels > 0) {
                const double future_weight = 0.5 / static_cast<double>(future_levels);
                for (int level = safe_level + 1; level <= horizon_end; ++level)
                    horizon_probability += future_weight * chance_per_shop_at_level(champion, level);
            } else {
                // At max level there is no future-level estimate to blend in.
                horizon_probability = chance_per_shop_at_level(champion, safe_level);
            }
            const double penalty = 3.5 * (1.0 - std::clamp(horizon_probability / 0.20, 0.0, 1.0));
            return std::pair<double, double>{horizon_probability, penalty};
        };
        std::unordered_map<std::string, double> focus;
        for (const auto& [trait, weight] : focus_weights)
            if (!trait.empty() && std::isfinite(weight))
                focus[trait] = std::max(0.0, weight);

        std::unordered_set<std::string> anchor_traits;
        if (!direction.empty()) anchor_traits.insert(direction);
        // Champions that carry the current direction reveal compatible
        // bridge traits. This allows, for example, a carry with a secondary
        // trait to connect a defensive frontline direction to damage.
        for (const auto& champion : pool) {
            if (std::find(champion.traits.begin(), champion.traits.end(), direction)
                == champion.traits.end()) continue;
            for (const auto& trait : champion.traits)
                if (trait != direction) anchor_traits.insert(trait);
        }

        const auto role_of = [](const ChampionDefinition& champion) {
            return champion.combat_profile.role >= 0
                ? champion.combat_profile.role : champion.role;
        };
        const auto has_trait = [](const ChampionDefinition& champion,
                                  const std::string& trait) {
            return !trait.empty() &&
                std::find(champion.traits.begin(), champion.traits.end(), trait)
                    != champion.traits.end();
        };
        const auto count_role = [&](int role) {
            return static_cast<int>(std::count_if(
                plan.unit_ids.begin(), plan.unit_ids.end(),
                [&](std::int32_t id) {
                    const auto it = std::find_if(pool.begin(), pool.end(),
                        [id](const ChampionDefinition& champion) {
                            return champion.internal_id == id;
                        });
                    return it != pool.end() && role_of(*it) == role;
                }));
        };

        // Select a carry first. It may be outside the anchor trait if it shares
        // a bridge trait with a champion in that direction or with current focus.
        const ChampionDefinition* selected_carry = nullptr;
        double best_carry_score = -std::numeric_limits<double>::infinity();
        for (const auto& champion : pool) {
            if (role_of(champion) != 1) continue;
            if (acquisition(champion).first <= 0.0) continue;
            double score = 2.5 + champion.cost * 0.10;
            if (has_trait(champion, direction)) score += 2.2;
            for (const auto& trait : champion.traits) {
                const auto focus_it = focus.find(trait);
                if (focus_it != focus.end()) score += std::min(1.5, focus_it->second * 0.20);
                if (anchor_traits.count(trait) != 0) score += 0.8;
            }
            const auto owned = owned_copies.find(champion.internal_id);
            if (owned != owned_copies.end()) score += std::min(2.0, owned->second * 0.35);
            const auto [shop_probability, acquisition_penalty] = acquisition(champion);
            (void)shop_probability;
            score -= acquisition_penalty * 1.35;
            if (score > best_carry_score) {
                best_carry_score = score;
                selected_carry = &champion;
            }
        }
        if (selected_carry) {
            plan.unit_ids.push_back(selected_carry->internal_id);
            plan.unit_names.push_back(selected_carry->api_name.empty()
                ? selected_carry->name : selected_carry->api_name);
            plan.main_carry_id = selected_carry->internal_id;
            plan.score += best_carry_score;
        }

        std::unordered_map<std::string, int> selected_trait_counts;
        const auto add_champion_traits = [&](const ChampionDefinition& champion) {
            for (const auto& trait : champion.traits) ++selected_trait_counts[trait];
        };
        if (selected_carry) add_champion_traits(*selected_carry);

        // Score the marginal value of a trait count using the actual set-specific
        // breakpoints. Crossing 2/4/6 is worth substantially more than spreading
        // the lineup across many traits that never become active.
        const auto trait_milestone_potential = [&](const std::string& trait, int count) {
            const auto found = milestones.find(trait);
            static const std::vector<int> fallback{2};
            const auto& thresholds = found == milestones.end() ? fallback : found->second;
            double value = 0.0;
            int next_milestone = 0;
            for (const int milestone : thresholds) {
                if (milestone <= 0) continue;
                if (count >= milestone) value += 2.0;
                else if (next_milestone == 0 || milestone < next_milestone)
                    next_milestone = milestone;
            }
            // A small progress value rewards staying near the next breakpoint,
            // without making a 3/4 trait look as valuable as a completed 4/4.
            if (next_milestone > 0)
                value += 0.8 * std::clamp(static_cast<double>(count) / next_milestone, 0.0, 1.0);
            return value;
        };

        while (plan.unit_ids.size() < slots) {
            const ChampionDefinition* best = nullptr;
            double best_score = -std::numeric_limits<double>::infinity();
            for (const auto& champion : pool) {
                if (std::find(plan.unit_ids.begin(), plan.unit_ids.end(),
                              champion.internal_id) != plan.unit_ids.end()) continue;
                if (acquisition(champion).first <= 0.0) continue;
                const int role = role_of(champion);
                double score = 0.0;

                // Reward the marginal value of reaching the next real trait
                // breakpoint, including progress toward it, rather than just
                // counting trait names that happen to overlap.
                for (const auto& trait : champion.traits) {
                    const int before = selected_trait_counts[trait];
                    const double milestone_delta =
                        trait_milestone_potential(trait, before + 1) -
                        trait_milestone_potential(trait, before);
                    score += milestone_delta * (trait == direction ? 1.25 : 1.0);
                    if (trait == direction) score += 1.0;
                    const auto focus_it = focus.find(trait);
                    if (focus_it != focus.end())
                        score += std::min(1.2, focus_it->second * 0.16);
                    if (anchor_traits.count(trait) != 0 && trait != direction)
                        score += 0.45;
                    if (before > 0) score += std::min(0.45, before * 0.12);
                }

                if (role == 1 && count_role(1) == 0) score += 2.8;
                if ((role == 0 || role == 3) && count_role(0) + count_role(3) == 0)
                    score += 2.0;
                else if ((role == 0 || role == 3) &&
                         count_role(0) + count_role(3) == 1)
                    score += 0.9;
                if (role == 2) score += 0.25; // support has flexible utility
                score += std::min(1.8, owned_copies.count(champion.internal_id)
                    ? owned_copies.at(champion.internal_id) * 0.35 : 0.0);
                score -= champion.cost * 0.12; // avoid an all-expensive theoretical board
                const auto [shop_probability, acquisition_penalty] = acquisition(champion);
                (void)shop_probability;
                score -= acquisition_penalty;
                if (score > best_score) {
                    best_score = score;
                    best = &champion;
                }
            }
            if (!best) break;
            plan.unit_ids.push_back(best->internal_id);
            plan.unit_names.push_back(best->api_name.empty() ? best->name : best->api_name);
            plan.score += best_score;
            add_champion_traits(*best);
        }

        // Keep a compact strategic summary: primary direction first, then the
        // strongest additional traits actually represented by the planned lineup.
        if (!direction.empty() && selected_trait_counts.count(direction) != 0)
            plan.core_traits.push_back(direction);
        std::vector<std::pair<std::string, int>> traits(
            selected_trait_counts.begin(), selected_trait_counts.end());
        std::stable_sort(traits.begin(), traits.end(),
            [&](const auto& lhs, const auto& rhs) {
                if (lhs.second != rhs.second) return lhs.second > rhs.second;
                return focus[lhs.first] > focus[rhs.first];
            });
        for (const auto& [trait, count] : traits) {
            if (trait == direction || count < 2) continue;
            if (plan.core_traits.size() >= 3) break;
            plan.core_traits.push_back(trait);
        }
        if (!available_copies.empty()) {
            for (const auto id : plan.unit_ids) {
                const auto champion_it = std::find_if(pool.begin(), pool.end(),
                    [id](const ChampionDefinition& item) { return item.internal_id == id; });
                if (champion_it == pool.end()) continue;
                const auto owned = owned_copies.find(id);
                if (owned != owned_copies.end() && owned->second > 0) continue;
                if (currently_offered.count(id) != 0) {
                    std::string note = champion_it->api_name.empty() ? champion_it->name : champion_it->api_name;
                    note += " (currently_in_shop; immediate acquisition available)";
                    plan.acquisition_notes.push_back(std::move(note));
                    continue;
                }
                const auto [per_shop, penalty] = acquisition(*champion_it);
                const int horizon_percent = static_cast<int>(std::round(per_shop * 100.0));
                const int current_percent = static_cast<int>(std::round(
                    chance_per_shop_at_level(*champion_it, safe_level) * 100.0));
                std::string note = champion_it->api_name.empty() ? champion_it->name : champion_it->api_name;
                note += " (cost=" + std::to_string(champion_it->cost) +
                    ", chance_now~" + std::to_string(current_percent) +
                    "%, chance_horizon~" + std::to_string(horizon_percent) + "%";
                if (per_shop <= 0.0) note += ", unavailable";
                else if (penalty >= 2.0) note += ", hard_to_find";
                else if (penalty >= 0.8) note += ", low_odds";
                else note += ", viable";
                note += ")";
                plan.acquisition_notes.push_back(std::move(note));
            }

            // Explain why a missing, low-probability carry was not chosen.
            // Limit this to three candidates so logs remain useful rather than noisy.
            std::size_t rejected_carries = 0;
            for (const auto& champion : pool) {
                if (rejected_carries >= 3) break;
                if (role_of(champion) != 1 ||
                    std::find(plan.unit_ids.begin(), plan.unit_ids.end(), champion.internal_id) != plan.unit_ids.end())
                    continue;
                const auto owned = owned_copies.find(champion.internal_id);
                if (owned != owned_copies.end() && owned->second > 0) continue;
                if (currently_offered.count(champion.internal_id) != 0) continue;
                const auto [per_shop, penalty] = acquisition(champion);
                if (penalty < 1.5) continue;
                const int horizon_percent = static_cast<int>(std::round(per_shop * 100.0));
                const int current_percent = static_cast<int>(std::round(
                    chance_per_shop_at_level(champion, safe_level) * 100.0));
                std::string note = "NOT_SELECTED_CARRY: ";
                note += champion.api_name.empty() ? champion.name : champion.api_name;
                note += " (cost=" + std::to_string(champion.cost) +
                    ", chance_now~" + std::to_string(current_percent) +
                    "%, chance_horizon~" + std::to_string(horizon_percent) +
                    "%, hard_to_find; alternative carry preferred)";
                plan.acquisition_notes.push_back(std::move(note));
                ++rejected_carries;
            }
        }
        // Optional OP.GG catalog: use it as a candidate, not as a hard constraint.
        // The final lineup remains the target; early/mid snapshots score how well
        // the candidate matches the player's actual transition path.
        try {
            static const nlohmann::json meta_catalog = []() {
                const char* configured = std::getenv("TFT_OPGG_META_CATALOG");
                const std::string path = configured && *configured
                    ? configured : "data/opgg_tft_meta.json";
                std::ifstream input(path);
                if (!input) return nlohmann::json::object();
                nlohmann::json value;
                input >> value;
                if (!value.is_object() || !value.contains("compositions") ||
                    !value["compositions"].is_array() ||
                    value.value("schema_version", 0) != 1)
                    return nlohmann::json::object();
                return value;
            }();

            if (meta_catalog.contains("compositions") &&
                meta_catalog["compositions"].is_array() && !plan.unit_ids.empty()) {
                std::unordered_map<std::string, const ChampionDefinition*> by_key;
                for (const auto& champion : pool) {
                    if (!champion.api_name.empty()) by_key[champion.api_name] = &champion;
                    if (!champion.character_name.empty()) by_key[champion.character_name] = &champion;
                    if (!champion.name.empty()) by_key[champion.name] = &champion;
                }
                std::unordered_set<std::string> owned_traits;
                for (const auto& [id, count] : owned_copies) {
                    if (count <= 0) continue;
                    const auto found = std::find_if(pool.begin(), pool.end(),
                        [id](const ChampionDefinition& item) { return item.internal_id == id; });
                    if (found != pool.end())
                        for (const auto& trait : found->traits) owned_traits.insert(trait);
                }
                const auto lineup_score = [&](const std::vector<std::int32_t>& ids,
                                              const std::unordered_set<std::int32_t>& core,
                                              const std::unordered_set<std::int32_t>& stage_units,
                                              double stats_prior) {
                    double value = 0.0;
                    int carry_count = 0;
                    int frontline_count = 0;
                    std::unordered_set<std::string> lineup_traits;
                    for (const auto id : ids) {
                        const auto def = std::find_if(pool.begin(), pool.end(),
                            [id](const ChampionDefinition& item) { return item.internal_id == id; });
                        if (def == pool.end()) continue;
                        const auto owned = owned_copies.find(id);
                        const int copies = owned == owned_copies.end() ? 0 : owned->second;
                        if (copies > 0) value += 2.8 + std::min(1.2, (copies - 1) * 0.25);
                        if (currently_offered.count(id)) value += 2.2;
                        if (core.count(id)) value += 0.8;
                        if (stage_units.count(id)) {
                            value += copies > 0 ? 1.8 : (currently_offered.count(id) ? 1.2 : 0.0);
                        }
                        value -= def->cost * 0.13;
                        const auto [probability, penalty] = acquisition(*def);
                        (void)probability;
                        value -= penalty * 0.65;
                        for (const auto& trait : def->traits) {
                            if (owned_traits.count(trait)) value += 0.22;
                            if (lineup_traits.count(trait)) value += 0.32;
                            lineup_traits.insert(trait);
                        }
                        const int role = role_of(*def);
                        if (role == 1) ++carry_count;
                        if (role == 0 || role == 3) ++frontline_count;
                    }
                    if (carry_count > 0) value += 1.2;
                    if (frontline_count > 0) value += 1.0;
                    return value + stats_prior;
                };

                std::unordered_set<std::int32_t> no_core;
                std::unordered_set<std::int32_t> no_stage_units;
                const double own_score = lineup_score(plan.unit_ids, no_core, no_stage_units, 0.0);
                double best_meta_score = -std::numeric_limits<double>::infinity();
                std::vector<std::int32_t> best_meta_ids;
                std::vector<std::int32_t> best_meta_stage_ids;
                std::vector<std::int32_t> best_meta_core_ids;
                std::vector<std::string> best_meta_traits;
                std::string best_meta_name;

                for (const auto& composition : meta_catalog["compositions"]) {
                    if (!composition.is_object() || !composition.contains("units") ||
                        !composition["units"].is_array()) continue;
                    std::vector<std::int32_t> final_ids;
                    std::unordered_set<std::int32_t> core_ids;
                    std::vector<std::int32_t> core_order;
                    std::unordered_map<std::string, int> meta_trait_counts;
                    for (const auto& unit : composition["units"]) {
                        if (!unit.is_object()) continue;
                        const std::string key = unit.value("key", std::string{});
                        const auto found = by_key.find(key);
                        if (found == by_key.end()) continue;
                        const auto id = found->second->internal_id;
                        if (std::find(final_ids.begin(), final_ids.end(), id) != final_ids.end()) continue;
                        final_ids.push_back(id);
                        if (unit.value("is_core", false)) {
                            core_ids.insert(id);
                            core_order.push_back(id);
                        }
                        for (const auto& trait : found->second->traits) ++meta_trait_counts[trait];
                    }
                    if (final_ids.empty()) continue;

                    const char* snapshot_key = current_level <= 5 ? "early_game"
                        : (current_level <= 7 ? "mid_game" : "");
                    std::unordered_set<std::int32_t> stage_ids;
                    std::vector<std::int32_t> stage_order;
                    if (*snapshot_key && composition.contains(snapshot_key) &&
                        composition[snapshot_key].is_object() &&
                        composition[snapshot_key].contains("units") &&
                        composition[snapshot_key]["units"].is_array()) {
                        for (const auto& unit : composition[snapshot_key]["units"]) {
                            if (!unit.is_object()) continue;
                            const auto key = unit.value("key", std::string{});
                            const auto found = by_key.find(key);
                            if (found != by_key.end()) {
                                const auto id = found->second->internal_id;
                                stage_ids.insert(id);
                                if (std::find(stage_order.begin(), stage_order.end(), id) == stage_order.end())
                                    stage_order.push_back(id);
                            }
                        }
                    }
                    int owned_final_count = 0;
                    int owned_core_count = 0;
                    int offered_final_count = 0;
                    for (const auto id : final_ids) {
                        const auto owned = owned_copies.find(id);
                        if (owned != owned_copies.end() && owned->second > 0) {
                            ++owned_final_count;
                            if (core_ids.count(id)) ++owned_core_count;
                        }
                        if (currently_offered.count(id)) ++offered_final_count;
                    }
                    int stage_owned_count = 0;
                    double stage_snapshot_bonus = 0.0;
                    for (const auto id : stage_ids) {
                        const auto owned = owned_copies.find(id);
                        if (owned != owned_copies.end() && owned->second > 0) {
                            ++stage_owned_count;
                            stage_snapshot_bonus += 2.0;
                        } else if (currently_offered.count(id)) {
                            stage_snapshot_bonus += 1.25;
                        }
                    }
                    const bool direction_aligned = direction.empty() ||
                        meta_trait_counts.count(direction) != 0;
                    const bool has_contextual_evidence =
                        owned_final_count >= 2 ||
                        (owned_core_count >= 1 &&
                         (owned_final_count >= 1 || offered_final_count >= 1)) ||
                        stage_owned_count >= 2;
                    if (!direction_aligned || !has_contextual_evidence) continue;

                    double stats_prior = 0.0;
                    if (composition.contains("statistics") && composition["statistics"].is_object()) {
                        const auto& stats = composition["statistics"];
                        const auto deck = stats.value("deck", nlohmann::json::object());
                        const auto label = stats.value("label", nlohmann::json::object());
                        const auto& selected = deck.is_object() && deck.value("totalCount", 0) >= 1000
                            ? deck : label;
                        if (selected.is_object() && selected.value("totalCount", 0) >= 1000)
                            stats_prior = std::clamp(selected.value("top4Rate", 0.0), 0.0, 1.0) * 0.5;
                    }
                    const double score = lineup_score(final_ids, core_ids, stage_ids, stats_prior) + stage_snapshot_bonus;
                    if (score > best_meta_score) {
                        best_meta_score = score;
                        best_meta_ids = std::move(final_ids);
                        best_meta_stage_ids = std::move(stage_order);
                        best_meta_core_ids = std::move(core_order);
                        best_meta_name = composition.value("name", std::string{"OP.GG meta"});
                        best_meta_traits.clear();
                        std::vector<std::pair<std::string, int>> ordered_traits(
                            meta_trait_counts.begin(), meta_trait_counts.end());
                        std::stable_sort(ordered_traits.begin(), ordered_traits.end(),
                            [](const auto& lhs, const auto& rhs) { return lhs.second > rhs.second; });
                        for (const auto& [trait, count] : ordered_traits) {
                            if (count < 2) continue;
                            best_meta_traits.push_back(trait);
                            if (best_meta_traits.size() >= 3) break;
                        }
                    }
                }

                // Require a real contextual advantage over the native planner.
                // This prevents popularity alone from overriding a good own plan.
                if (!best_meta_ids.empty() && best_meta_score >= own_score + 1.0) {
                    const auto native_ids = plan.unit_ids;
                    plan.unit_ids.clear();
                    plan.unit_names.clear();
                    plan.main_carry_id = -1;
                    std::vector<std::int32_t> preferred_ids;
                    // During levels 1-7, keep the observed transition units in the
                    // strategic target, then reserve slots for final core units.
                    // At level 8+, the final lineup becomes the primary target.
                    if (current_level <= 7) {
                        preferred_ids.insert(preferred_ids.end(),
                            best_meta_stage_ids.begin(), best_meta_stage_ids.end());
                        for (const auto id : best_meta_ids) {
                            const auto def = std::find_if(pool.begin(), pool.end(),
                                [id](const ChampionDefinition& item) { return item.internal_id == id; });
                            if (def != pool.end() && role_of(*def) == 1)
                                preferred_ids.push_back(id);
                        }
                        preferred_ids.insert(preferred_ids.end(),
                            best_meta_core_ids.begin(), best_meta_core_ids.end());
                    }
                    preferred_ids.insert(preferred_ids.end(), best_meta_ids.begin(), best_meta_ids.end());
                    for (const auto id : preferred_ids) {
                        if (plan.unit_ids.size() >= slots) break;
                        if (std::find(plan.unit_ids.begin(), plan.unit_ids.end(), id) != plan.unit_ids.end()) continue;
                        const auto def = std::find_if(pool.begin(), pool.end(),
                            [id](const ChampionDefinition& item) { return item.internal_id == id; });
                        if (def == pool.end()) continue;
                        plan.unit_ids.push_back(id);
                        plan.unit_names.push_back(def->api_name.empty() ? def->name : def->api_name);
                    }
                    // Main carry is always selected from the final comp, not a temporary early-game unit.
                    for (const auto id : best_meta_ids) {
                        const auto def = std::find_if(pool.begin(), pool.end(),
                            [id](const ChampionDefinition& item) { return item.internal_id == id; });
                        if (def != pool.end() && role_of(*def) == 1) {
                            plan.main_carry_id = id;
                            break;
                        }
                    }
                    // At levels 9/10, keep the extra flexible slots from the native planner.
                    for (const auto id : native_ids) {
                        if (plan.unit_ids.size() >= slots) break;
                        if (std::find(plan.unit_ids.begin(), plan.unit_ids.end(), id) != plan.unit_ids.end()) continue;
                        const auto def = std::find_if(pool.begin(), pool.end(),
                            [id](const ChampionDefinition& item) { return item.internal_id == id; });
                        if (def == pool.end()) continue;
                        plan.unit_ids.push_back(id);
                        plan.unit_names.push_back(def->api_name.empty() ? def->name : def->api_name);
                    }
                    if (!best_meta_traits.empty()) plan.core_traits = best_meta_traits;
                    plan.score = best_meta_score;
                    plan.acquisition_notes.insert(plan.acquisition_notes.begin(),
                        "OPGG_META_CANDIDATE: " + best_meta_name +
                        " (score=" + std::to_string(best_meta_score) +
                        ", native_score=" + std::to_string(own_score) + ")");
                }
            }
        } catch (const std::exception&) {
            // A malformed/missing external catalog must never stop a game or training.
        }
        return plan;
    }
};

}  // namespace tft::strategy
