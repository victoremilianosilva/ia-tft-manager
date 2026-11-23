#include "strategy/CompositionBoundDirectionAnchor.hpp"

#include <cassert>
#include <iostream>

using namespace tft::strategy;
using namespace tft::composition_intelligence;

int main() {
    ActiveComposition active;
    active.version = 7;
    active.candidate.composition_id = "comp-set18-carry";
    active.candidate.units = {
        {10, UnitRole::MainCarry, true, 100},
        {20, UnitRole::Frontline, true, 90},
        {30, UnitRole::Support, false, 60}
    };

    // A composition ID is not a semantic direction. Without an explicit
    // direction owner, the adapter must refuse to manufacture one.
    assert(!CompositionBoundDirectionAnchor::from_active_composition(active));

    const auto anchor =
        CompositionBoundDirectionAnchor::from_active_composition(active, "TraitBruiser");
    assert(anchor.has_value());
    assert(anchor->is_valid());
    assert(anchor->composition_bound);
    assert(anchor->composition_identity == active.candidate.composition_id);
    assert(anchor->composition_version == active.version);
    assert(anchor->direction == "TraitBruiser");
    assert(anchor->lifecycle == StrategicAnchorLifecycle::Active);
    assert((anchor->reference_unit_ids == std::vector<std::int32_t>{10, 20, 30}));
    assert(anchor->reason == "bound_to_active_composition_and_committed_direction");

    auto invalid = active;
    invalid.version = 0;
    assert(!CompositionBoundDirectionAnchor::from_active_composition(invalid));

    invalid = active;
    invalid.candidate.units[1].champion_id = -1;
    assert(!CompositionBoundDirectionAnchor::from_active_composition(invalid));

    invalid = active;
    invalid.candidate.units[1].champion_id = 10;
    assert(!CompositionBoundDirectionAnchor::from_active_composition(invalid));

    std::cout << "composition-bound direction anchor tests passed\n";
    return 0;
}
