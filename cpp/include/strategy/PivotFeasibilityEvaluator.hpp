#pragma once

// Shadow-only pivot feasibility evaluation. This contract consumes an
// already-normalized strategic snapshot and never mutates the active direction,
// composition, PPO state, observations, masks, rewards, or action execution.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace tft::strategy {

enum class PivotFeasibilityStatus : std::uint8_t {
    InsufficientEvidence = 0,
    Rejected = 1,
    Viable = 2
};

struct PivotRequiredUnit {
    std::int32_t champion_id{-1};
    std::int32_t cost{-1};
    bool core{false};
    bool carry{false};
    std::vector<std::string> traits;
};

struct PivotObservedUnit {
    std::int32_t champion_id{-1};
    std::int32_t owned_copies{0};
    std::int32_t star{1};
    std::int32_t shop_copies{0};
    // -1 means pool availability was not supplied.
    std::int32_t pool_remaining{-1};
};

struct PivotTraitRequirement {
    std::string trait;
    std::int32_t minimum_units{0};
};

struct PivotFeasibilityInput {
    std::string candidate_composition_identity;
    std::string source_direction_anchor_identity;
    std::uint64_t source_composition_version{0};
    std::vector<PivotRequiredUnit> required_units;
    std::vector<PivotObservedUnit> observed_units;
    std::vector<PivotTraitRequirement> required_traits;
    std::int32_t gold_available{-1};
    std::int32_t protected_gold_floor{-1};
    // Combined direct cost, lost interest and opportunity cost.
    double transition_economic_cost{-1.0};
};

struct PivotTraitEvidence {
    std::string trait;
    std::int32_t required{0};
    std::int32_t owned{0};
    std::int32_t reachable_with_shop{0};
    bool satisfied{false};
};

struct PivotUnitEvidence {
    std::int32_t champion_id{-1};
    std::int32_t owned_copies{0};
    std::int32_t shop_copies{0};
    std::int32_t pool_remaining{-1};
    bool core{false};
    bool carry{false};
    bool available{false};
    bool availability_unknown{false};
};

struct PivotFeasibilityResult {
    PivotFeasibilityStatus status{PivotFeasibilityStatus::InsufficientEvidence};
    std::string reason{"not_evaluated"};
    std::vector<std::string> favorable_evidence;
    std::vector<std::string> blockers;
    std::vector<std::string> missing_data;
    std::vector<PivotUnitEvidence> units;
    std::vector<PivotTraitEvidence> traits;
    double score{0.0};
    double transition_economic_cost{0.0};
    bool carry_eligible{false};
    bool shadow_only{true};
};

class PivotFeasibilityEvaluator {
public:
    PivotFeasibilityResult evaluate(const PivotFeasibilityInput& input) const {
        PivotFeasibilityResult out;
        if (input.candidate_composition_identity.empty() ||
            input.source_direction_anchor_identity.empty() ||
            input.source_composition_version == 0) {
            out.missing_data.push_back("candidate_or_source_identity_missing");
        }
        if (input.required_units.empty()) {
            out.missing_data.push_back("required_composition_units_missing");
        }
        if (input.gold_available < 0 || input.protected_gold_floor < 0) {
            out.missing_data.push_back("economic_snapshot_missing");
        }
        if (!std::isfinite(input.transition_economic_cost) ||
            input.transition_economic_cost < 0.0) {
            out.missing_data.push_back("transition_economic_cost_missing_or_invalid");
        }

        std::unordered_map<std::int32_t, PivotObservedUnit> observed;
        for (const auto& unit : input.observed_units) {
            if (unit.champion_id < 0 || unit.owned_copies < 0 ||
                unit.shop_copies < 0 || unit.star < 1 ||
                unit.star > 3 || unit.pool_remaining < -1 ||
                !observed.emplace(unit.champion_id, unit).second) {
                out.blockers.push_back("invalid_or_duplicate_unit_evidence");
                continue;
            }
        }

        std::unordered_set<std::int32_t> required_ids;
        std::unordered_map<std::string, std::int32_t> owned_traits;
        std::unordered_map<std::string, std::int32_t> reachable_traits;
        std::int32_t core_total = 0;
        std::int32_t core_reachable = 0;
        bool carry_defined = false;
        bool carry_found = false;
        double owned_support = 0.0;
        double shop_support = 0.0;

        for (const auto& required : input.required_units) {
            if (required.champion_id < 0 || required.cost < 1 ||
                required.cost > 5 || !required_ids.insert(required.champion_id).second) {
                out.blockers.push_back("invalid_or_duplicate_required_unit");
                continue;
            }
            if (required.core) ++core_total;
            if (required.carry) {
                if (carry_defined) out.blockers.push_back("multiple_main_carries");
                carry_defined = true;
            }

            const auto found = observed.find(required.champion_id);
            const PivotObservedUnit* evidence =
                found == observed.end() ? nullptr : &found->second;
            const std::int32_t owned = evidence ? evidence->owned_copies : 0;
            const std::int32_t shop = evidence ? evidence->shop_copies : 0;
            const std::int32_t pool = evidence ? evidence->pool_remaining : -1;
            const bool reachable = owned > 0 || shop > 0 || pool > 0;
            const bool unknown = owned == 0 && shop == 0 && pool < 0;
            const bool available = owned > 0 || shop > 0 || pool > 0;

            out.units.push_back({required.champion_id, owned, shop, pool,
                required.core, required.carry, available, unknown});

            if (owned > 0) {
                owned_support += 1.0;
                for (const auto& trait : required.traits) ++owned_traits[trait];
            }
            if (shop > 0) {
                shop_support += 1.0;
                if (owned == 0) {
                    for (const auto& trait : required.traits) ++reachable_traits[trait];
                }
            }
            if (owned > 0 || shop > 0) {
                for (const auto& trait : required.traits) {
                    if (owned == 0) ++reachable_traits[trait];
                }
            }

            if (required.core && reachable) ++core_reachable;
            if (unknown) out.missing_data.push_back(
                "pool_availability_unknown_for_unit_" + std::to_string(required.champion_id));
            if (pool == 0 && owned == 0 && shop == 0) {
                out.blockers.push_back(
                    "required_unit_unavailable_" + std::to_string(required.champion_id));
            }

            if (required.carry) {
                carry_found = true;
                const bool carry_two_star = evidence && evidence->star >= 2;
                const bool high_cost_carry = required.cost == 4 || required.cost == 5;
                out.carry_eligible = carry_two_star || high_cost_carry;
                if (carry_two_star) out.favorable_evidence.push_back("main_carry_already_two_star");
                else if (high_cost_carry) out.favorable_evidence.push_back("main_carry_cost_four_or_five");
                else out.blockers.push_back("main_carry_not_two_star_and_below_four_cost");
            }
        }

        if (!carry_defined || !carry_found)
            out.missing_data.push_back("main_carry_definition_missing");

        for (const auto& requirement : input.required_traits) {
            if (requirement.trait.empty() || requirement.minimum_units <= 0) {
                out.blockers.push_back("invalid_trait_requirement");
                continue;
            }
            const auto owned = owned_traits[requirement.trait];
            const auto reachable = owned + reachable_traits[requirement.trait];
            const bool satisfied = reachable >= requirement.minimum_units;
            out.traits.push_back({requirement.trait, requirement.minimum_units,
                owned, reachable, satisfied});
            if (satisfied) {
                out.favorable_evidence.push_back("trait_reachable_" + requirement.trait);
            } else {
                out.blockers.push_back("trait_not_reachable_" + requirement.trait);
            }
        }

        if (core_total == 0) {
            out.missing_data.push_back("core_unit_requirements_missing");
        } else if (core_reachable < core_total) {
            out.blockers.push_back("core_unit_coverage_incomplete");
        } else {
            out.favorable_evidence.push_back("all_core_units_owned_or_reachable");
        }

        if (shop_support > 0.0) out.favorable_evidence.push_back("target_units_present_in_shop");
        if (owned_support > 0.0) out.favorable_evidence.push_back("target_units_already_owned");
        if (input.gold_available >= 0 && input.protected_gold_floor >= 0 &&
            std::isfinite(input.transition_economic_cost) &&
            input.transition_economic_cost >= 0.0) {
            out.transition_economic_cost = input.transition_economic_cost;
            const double spendable = std::max(
                0, input.gold_available - input.protected_gold_floor);
            if (input.transition_economic_cost > spendable) {
                out.blockers.push_back("transition_exceeds_spendable_economy");
            } else {
                out.favorable_evidence.push_back("transition_within_spendable_economy");
            }
        }

        const bool has_missing = !out.missing_data.empty();
        const bool has_blocker = !out.blockers.empty();
        if (has_blocker) {
            out.status = PivotFeasibilityStatus::Rejected;
            out.reason = "candidate_has_explicit_feasibility_blockers";
        } else if (has_missing) {
            out.status = PivotFeasibilityStatus::InsufficientEvidence;
            out.reason = "missing_evidence_prevents_viability_approval";
        } else {
            out.status = PivotFeasibilityStatus::Viable;
            out.reason = "all_required_feasibility_gates_satisfied";
        }

        const double unit_denominator = std::max<std::size_t>(1, input.required_units.size());
        const double trait_denominator = std::max<std::size_t>(1, input.required_traits.size());
        const double unit_ratio = std::min(1.0, owned_support / unit_denominator);
        const double shop_ratio = std::min(1.0, shop_support / unit_denominator);
        const double trait_ratio = input.required_traits.empty() ? 0.0 :
            static_cast<double>(std::count_if(out.traits.begin(), out.traits.end(),
                [](const PivotTraitEvidence& t) { return t.satisfied; })) / trait_denominator;
        const double core_ratio = core_total == 0 ? 0.0 :
            static_cast<double>(core_reachable) / core_total;
        out.score = std::clamp(
            25.0 * unit_ratio + 15.0 * shop_ratio + 25.0 * trait_ratio +
            25.0 * core_ratio + (out.carry_eligible ? 10.0 : 0.0),
            0.0, 100.0);
        if (out.status != PivotFeasibilityStatus::Viable) out.score = std::min(out.score, 49.0);
        return out;
    }
};

} // namespace tft::strategy
