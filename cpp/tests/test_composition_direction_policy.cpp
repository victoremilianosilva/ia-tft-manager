#include "strategy/CompositionDirectionPolicy.hpp"

#include <cassert>
#include <cmath>
#include <iostream>

using tft::strategy::CompositionDirectionConfig;
using tft::strategy::CompositionDirectionInput;
using tft::strategy::CompositionDirectionPolicy;
using tft::strategy::CompositionDirectionState;

int main() {
    CompositionDirectionPolicy policy(CompositionDirectionConfig{0.20, 0.75, 3});
    CompositionDirectionState state;

    // Initial direction can be selected while the composition is open.
    auto result = policy.update(state, {"Bruiser", 5.0, true, false});
    assert(result.changed);
    assert(state.direction == "Bruiser");
    assert(state.change_count == 1);

    // Once locked, a small one-step advantage must not switch the direction.
    state.locked = true;
    result = policy.update(state, {"Mage", 5.5, true, false});
    assert(!result.changed);
    assert(state.direction == "Bruiser");
    assert(state.candidate_streak == 0);

    // A temporarily missing trait must not erase a locked direction.
    result = policy.update(state, {"", 0.0, true, false});
    assert(!result.changed);
    assert(state.direction == "Bruiser");
    assert(state.locked);

    // A clearly better candidate needs consecutive evidence.
    result = policy.update(state, {"Mage", 7.0, true, false});
    assert(!result.changed);
    assert(state.direction == "Bruiser");
    assert(state.candidate_streak == 1);
    result = policy.update(state, {"Mage", 7.1, true, false});
    assert(!result.changed);
    assert(state.candidate_streak == 2);
    result = policy.update(state, {"Mage", 7.2, true, false});
    assert(result.changed);
    assert(result.unlocked);
    assert(state.direction == "Mage");
    assert(state.previous_direction == "Bruiser");
    assert(state.change_reason == "persistent_superior_candidate");

    // A genuinely unviable current composition may adapt immediately.
    state.locked = true;
    result = policy.update(state, {"Ranger", 4.5, false, false});
    assert(result.changed);
    assert(result.unlocked);
    assert(state.direction == "Ranger");
    assert(state.change_reason == "current_direction_unviable");

    // Emergency transitions are explicit and do not wait for persistence.
    state.locked = true;
    result = policy.update(state, {"Assassin", 3.0, true, true});
    assert(result.changed);
    assert(state.direction == "Assassin");
    assert(state.change_reason == "emergency_transition");

    // A viability loss unlocks even if this refresh still proposes the old
    // direction; it must not remain locked forever on stale evidence.
    state.locked = true;
    result = policy.update(state, {"Assassin", 2.8, false, false});
    assert(!result.changed);
    assert(result.unlocked);
    assert(!state.locked);
    assert(state.direction == "Assassin");
    assert(state.change_reason == "current_direction_unviable");

    // Invalid strengths are treated as missing evidence, not as a direction.
    state.locked = true;
    result = policy.update(state, {"Tank", std::nan(""), true, false});
    assert(!result.changed);
    assert(state.direction == "Assassin");
    assert(state.locked);

    std::cout << "composition direction policy tests passed\n";
    return 0;
}
