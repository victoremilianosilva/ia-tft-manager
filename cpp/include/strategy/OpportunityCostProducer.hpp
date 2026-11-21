#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <string>
#include <unordered_set>
#include <vector>

namespace tft::strategy {

// Evidence supplied by a producer that can quantify the value preserved or
// sacrificed by an alternative on the exact same decision snapshot.
struct OpportunityAlternativeEvidence {
    std::string candidate_id;
    std::string value_basis;
    double marginal_strategic_value{0.0};
    double direct_economy_cost{0.0};
    double interest_cost{0.0};
    double progression_value{0.0};
    double unit_value{0.0};
    double upgrade_value{0.0};
    double liquidity_value{0.0};
    std::uint32_t horizon_rounds{0};
    double uncertainty{1.0};
    bool available{false};
    bool identity_valid{false};
};

struct OpportunityCostResult {
    bool available{false};
    double cost{0.0};
    std::string source{"unavailable_no_validated_alternative"};
    std::string value_basis;
    std::string sacrificed_candidate_id;
    std::uint32_t horizon_rounds{0};
    double uncertainty{1.0};
    std::string reason{"no_competing_alternative"};
};

// Computes the best *forgone* alternative, not a fixed cost by action family.
// All values must originate from the same native snapshot. The caller supplies
// a value already net of the alternative's direct gold, liquidity and interest;
// the cost fields are audit metadata and are never re-applied here.
class OpportunityCostProducer {
public:
    OpportunityCostResult evaluate(
        const std::string& selected_candidate_id,
        const std::vector<OpportunityAlternativeEvidence>& alternatives,
        std::uint32_t selected_horizon_rounds,
        const std::string& selected_value_basis
    ) const {
        OpportunityCostResult out;
        if (selected_candidate_id.empty() || selected_horizon_rounds == 0 ||
            selected_value_basis.empty()) {
            out.reason = "selected_candidate_contract_missing";
            return out;
        }
        const OpportunityAlternativeEvidence* best = nullptr;
        double best_value = 0.0;
        std::unordered_set<std::string> seen_candidate_ids;
        for (const auto& alternative : alternatives) {
            if (alternative.candidate_id.empty()) continue;
            if (!seen_candidate_ids.insert(alternative.candidate_id).second) {
                out.reason = "duplicate_competing_candidate_identity";
                return out;
            }
            if (alternative.candidate_id == selected_candidate_id ||
                !alternative.available || !alternative.identity_valid ||
                alternative.horizon_rounds != selected_horizon_rounds ||
                alternative.value_basis != selected_value_basis ||
                !std::isfinite(alternative.marginal_strategic_value) ||
                alternative.marginal_strategic_value < 0.0 ||
                !std::isfinite(alternative.progression_value) ||
                alternative.progression_value < 0.0 ||
                !std::isfinite(alternative.unit_value) ||
                alternative.unit_value < 0.0 ||
                !std::isfinite(alternative.upgrade_value) ||
                alternative.upgrade_value < 0.0 ||
                !std::isfinite(alternative.liquidity_value) ||
                alternative.liquidity_value < 0.0 ||
                !std::isfinite(alternative.uncertainty) ||
                alternative.uncertainty < 0.0 || alternative.uncertainty > 1.0 ||
                !std::isfinite(alternative.direct_economy_cost) ||
                !std::isfinite(alternative.interest_cost)) {
                continue;
            }
            // Economic costs are deliberately not included: they are already
            // compared to HOLD by the marginal liquidity/interest envelope.
            const double value = alternative.marginal_strategic_value +
                alternative.progression_value + alternative.unit_value +
                alternative.upgrade_value + alternative.liquidity_value;
            if (!std::isfinite(value)) continue;
            if (best == nullptr || value > best_value) {
                best = &alternative;
                best_value = value;
            }
        }
        if (best == nullptr) {
            out.reason = "no_valid_competing_alternative";
            return out;
        }
        out.available = true;
        out.cost = std::max(0.0, best_value);
        out.source = "same_snapshot_competing_alternative.v1";
        out.value_basis = selected_value_basis;
        out.sacrificed_candidate_id = best->candidate_id;
        out.horizon_rounds = selected_horizon_rounds;
        out.uncertainty = best->uncertainty;
        out.reason = "best_valid_forgone_alternative";
        return out;
    }
};

} // namespace tft::strategy
