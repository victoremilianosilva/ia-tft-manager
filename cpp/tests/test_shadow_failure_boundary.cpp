#ifdef NDEBUG
#undef NDEBUG
#endif

#include "composition_intelligence/ShadowFailureBoundary.hpp"

#include <cassert>
#include <stdexcept>

using tft::composition_intelligence::run_shadow_isolated;

int main() {
    bool failure_called = false;
    const bool success = run_shadow_isolated(
        [] {},
        [&]() noexcept { failure_called = true; }
    );
    assert(success);
    assert(!failure_called);

    const bool standard_exception = run_shadow_isolated(
        [] { throw std::runtime_error("synthetic planner failure"); },
        [&]() noexcept { failure_called = true; }
    );
    assert(!standard_exception);
    assert(failure_called);

    failure_called = false;
    const bool unknown_exception = run_shadow_isolated(
        [] { throw 42; },
        [&]() noexcept { failure_called = true; }
    );
    assert(!unknown_exception);
    assert(failure_called);

    const bool throwing_failure_reporter = run_shadow_isolated(
        [] { throw std::runtime_error("planner failure"); },
        [] { throw std::runtime_error("diagnostic recorder failure"); }
    );
    assert(!throwing_failure_reporter);
    return 0;
}
