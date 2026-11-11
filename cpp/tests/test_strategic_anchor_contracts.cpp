#include "strategy/StrategicAnchorContracts.hpp"

#include <cassert>
#include <iostream>

using namespace tft::strategy;

int main() {
    StrategicAnchorState state;

    // No evidence is represented explicitly as an empty state, not as an
    // invented direction or pivot.
    assert(!state.has_direction_anchor());
    assert(!state.has_pivot_candidate());

    StrategicDirectionAnchor initial;
    initial.identity = "direction:early:1";
    initial.direction = "Bruiser";
    initial.reference_unit_ids = {101, 102};
    initial.evidence = {
        StrategicAnchorEvidenceKind::OwnedUnit,
        StrategicAnchorEvidenceKind::PairProgress
    };
    initial.confidence = 0.62;
    initial.reason = "owned_pair_with_upgrade_potential";
    initial.lifecycle = StrategicAnchorLifecycle::Active;
    // The contract does not impose a 4/5-cost restriction on a direction
    // anchor. Unit-cost policy belongs to the discovery implementation.
    state.direction_anchor = initial;
    assert(state.has_direction_anchor());
    assert(!state.direction_anchor.composition_bound);

    // A candidate pivot has its own identity and references the source
    // direction/version; adding it does not mutate the current direction.
    StrategicPivotAnchorCandidate pivot;
    pivot.identity = "pivot:invoker:2";
    pivot.target_direction = "Invoker";
    pivot.target_composition_identity = "composition:invoker";
    pivot.source_direction_anchor_identity = state.direction_anchor.identity;
    pivot.source_composition_version = 0;
    pivot.reference_unit_ids = {201, 202};
    pivot.evidence = {
        StrategicAnchorEvidenceKind::ShopOffer,
        StrategicAnchorEvidenceKind::TraitCompletion
    };
    pivot.confidence = 0.71;
    pivot.reason = "shop_offers_complete_target_trait";
    pivot.lifecycle = StrategicAnchorLifecycle::Evaluating;
    state.pivot_candidate = pivot;

    assert(state.has_direction_anchor());
    assert(state.has_pivot_candidate());
    assert(state.direction_anchor.identity == "direction:early:1");
    assert(state.direction_anchor.direction == "Bruiser");
    assert(state.direction_anchor.reference_unit_ids.size() == 2);
    assert(state.pivot_candidate.target_direction == "Invoker");
    assert(state.pivot_candidate.source_direction_anchor_identity ==
           state.direction_anchor.identity);

    // Invalid/incomplete data must not be treated as a valid anchor.
    auto invalid_direction = initial;
    invalid_direction.identity.clear();
    assert(!invalid_direction.is_valid());

    auto invalid_pivot = pivot;
    invalid_pivot.source_direction_anchor_identity.clear();
    assert(!invalid_pivot.is_valid());

    invalid_pivot = pivot;
    invalid_pivot.confidence = 1.5;
    assert(!invalid_pivot.is_valid());

    // A composition-bound direction must carry a concrete identity/version.
    auto bound_direction = initial;
    bound_direction.composition_bound = true;
    assert(!bound_direction.is_valid());
    bound_direction.composition_identity = "composition:bruiser";
    bound_direction.composition_version = 3;
    assert(bound_direction.is_valid());

    // Terminal pivot states are not active candidates.
    auto rejected_pivot = pivot;
    rejected_pivot.lifecycle = StrategicAnchorLifecycle::Rejected;
    assert(!rejected_pivot.is_valid());

    std::cout << "strategic anchor contract tests passed\n";
    return 0;
}
