#include "decision/AntiLoopEngine.hpp"

namespace tft::decision {

MoveKey AntiLoopEngine::make_move_key(
    const std::string& move_type,
    std::int64_t source,
    std::int64_t target,
    const std::optional<UnitIdentity>& unit
) const {
    return MoveKey{
        move_type,
        source,
        target,
        unit
    };
}

} // namespace tft::decision
