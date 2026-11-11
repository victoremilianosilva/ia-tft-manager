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

    const auto anchor = CompositionBoundDirectionAnchor::from_active_composition(active);
    assert(anchor.has_value());
    assert(anchor->is_valid());
    assert(anchor->composition_bound);
    assert(anchor->composition_identity == active.candidate.composition_id);
    assert(anchor->composition_version == active.version);
    assert(anchor->direction == active.candidate.composition_id);
    assert(anchor->lifecycle == StrategicAnchorLifecycle::Active);
    assert((anchor->reference_unit_ids == std::vector<std::int32_t>{10, 20, 30}));
    assert(anchor->reason == "derived_from_active_composition_identity_and_version");

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
