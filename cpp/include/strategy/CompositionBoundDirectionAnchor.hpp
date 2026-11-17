#pragma once

// Read-only projection from a versioned active composition to its strategic
// direction anchor. This adapter does not publish state or alter game behavior.

#include "composition_intelligence/contracts/CompositionContracts.hpp"
#include "strategy/StrategicAnchorContracts.hpp"

#include <algorithm>
#include <optional>
#include <string>
#include <vector>

namespace tft::strategy {

class CompositionBoundDirectionAnchor {
public:
    static std::optional<StrategicDirectionAnchor> from_active_composition(
        const composition_intelligence::ActiveComposition& active) {
        const auto& candidate = active.candidate;
        if (candidate.composition_id.empty() || active.version == 0 ||
            candidate.units.empty()) {
            return std::nullopt;
        }

        StrategicDirectionAnchor anchor;
        anchor.identity = "direction:composition:" + candidate.composition_id +
            ":" + std::to_string(active.version);
        anchor.direction = candidate.composition_id;
        anchor.composition_identity = candidate.composition_id;
        anchor.composition_version = active.version;
        anchor.composition_bound = true;
        anchor.lifecycle = StrategicAnchorLifecycle::Active;
        // Confidence describes the deterministic binding, not composition quality.
        anchor.confidence = 1.0;
        anchor.reason = "derived_from_active_composition_identity_and_version";

        for (const auto& unit : candidate.units) {
            if (unit.champion_id < 0) return std::nullopt;
            anchor.reference_unit_ids.push_back(unit.champion_id);
            if (unit.core &&
                std::find(anchor.evidence.begin(), anchor.evidence.end(),
                    StrategicAnchorEvidenceKind::CompositionCore) == anchor.evidence.end()) {
                anchor.evidence.push_back(StrategicAnchorEvidenceKind::CompositionCore);
            }
        }
        std::sort(anchor.reference_unit_ids.begin(), anchor.reference_unit_ids.end());
        if (std::adjacent_find(anchor.reference_unit_ids.begin(),
                anchor.reference_unit_ids.end()) != anchor.reference_unit_ids.end()) {
            return std::nullopt;
        }
        if (anchor.evidence.empty())
            anchor.evidence.push_back(StrategicAnchorEvidenceKind::Unknown);
        return anchor.is_valid() ? std::optional<StrategicDirectionAnchor>{anchor}
                                 : std::nullopt;
    }
};

} // namespace tft::strategy
