#pragma once

#include <utility>

namespace tft::composition_intelligence {

// Runs diagnostic-only work without allowing a Shadow failure to escape into
// the game transition, PPO observation/reward, or action-execution path.
// The failure callback is also contained so diagnostics cannot rethrow.
template <typename Work, typename OnFailure>
bool run_shadow_isolated(Work&& work, OnFailure&& on_failure) noexcept {
    try {
        std::forward<Work>(work)();
        return true;
    } catch (...) {
        try {
            std::forward<OnFailure>(on_failure)();
        } catch (...) {
            // Failure reporting is diagnostic too; it must remain best-effort.
        }
        return false;
    }
}

} // namespace tft::composition_intelligence
