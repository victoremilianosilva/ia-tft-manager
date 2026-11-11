#pragma once

// Independent shadow contracts for the active strategic direction and a
// separately evaluated pivot candidate. These types are intentionally not
// wired into PPO, training, observations, masks, legal actions, or execution.

#include <cmath>
#include <cstdint>
#include <string>
#include <vector>

namespace tft::strategy {

enum class StrategicAnchorLifecycle : std::uint8_t {
    Empty = 0,
    Proposed = 1,
    Active = 2,
    Evaluating = 3,
    Confirmed = 4,
    Rejected = 5,
    Invalidated = 6
};

enum class StrategicAnchorEvidenceKind : std::uint8_t {
    Unknown = 0,
    OwnedUnit = 1,
    BoardUnit = 2,
    BenchUnit = 3,
    ShopOffer = 4,
    PairProgress = 5,
    TraitCompletion = 6,
    CompositionCore = 7
};

// The direction anchor answers: "What strategic direction currently guides
// the plan?" It may be exploratory before a composition has been selected.
struct StrategicDirectionAnchor {
    std::string identity;
    std::string direction;
    std::string composition_identity;
    std::uint64_t composition_version{0};
    std::vector<std::int32_t> reference_unit_ids;
    std::vector<StrategicAnchorEvidenceKind> evidence;
    double confidence{0.0};
    std::string reason;
    StrategicAnchorLifecycle lifecycle{StrategicAnchorLifecycle::Empty};
    bool composition_bound{false};

    bool is_valid() const {
        if (identity.empty() || direction.empty() ||
            reference_unit_ids.empty() || !std::isfinite(confidence) ||
            confidence < 0.0 || confidence > 1.0) {
            return false;
        }
        if (lifecycle != StrategicAnchorLifecycle::Proposed &&
            lifecycle != StrategicAnchorLifecycle::Active) {
            return false;
        }
        return !composition_bound ||
            (!composition_identity.empty() && composition_version > 0);
    }
};

// The pivot candidate answers: "Is there a separately identified destination
// worth evaluating?" It is bound to the direction/version from which it was
// evaluated and cannot itself replace the active direction anchor.
struct StrategicPivotAnchorCandidate {
    std::string identity;
    std::string target_direction;
    std::string target_composition_identity;
    std::string source_direction_anchor_identity;
    std::uint64_t source_composition_version{0};
    std::vector<std::int32_t> reference_unit_ids;
    std::vector<StrategicAnchorEvidenceKind> evidence;
    double confidence{0.0};
    std::string reason;
    StrategicAnchorLifecycle lifecycle{StrategicAnchorLifecycle::Empty};

    bool is_valid() const {
        return !identity.empty() && !target_direction.empty() &&
            !target_composition_identity.empty() &&
            !source_direction_anchor_identity.empty() &&
            !reference_unit_ids.empty() && std::isfinite(confidence) &&
            confidence >= 0.0 && confidence <= 1.0 &&
            (lifecycle == StrategicAnchorLifecycle::Proposed ||
             lifecycle == StrategicAnchorLifecycle::Evaluating);
    }
};

// Co-locates the two independent references without introducing transition
// behavior. A caller may update pivot_candidate while direction_anchor stays
// unchanged; promotion/synchronization belongs to a later transition contract.
struct StrategicAnchorState {
    StrategicDirectionAnchor direction_anchor;
    StrategicPivotAnchorCandidate pivot_candidate;

    bool has_direction_anchor() const {
        return direction_anchor.is_valid();
    }

    bool has_pivot_candidate() const {
        return pivot_candidate.is_valid();
    }
};

} // namespace tft::strategy
