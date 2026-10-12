#pragma once

#include "decision/DecisionState.hpp"

#include <cstdint>
#include <optional>
#include <string>

namespace tft::decision {

// Chave equivalente ao tuple produzido por AntiLoopManager.make_move_key.
// O tipo de movimento é mantido como texto porque a referência Python
// aceita aliases históricos (por exemplo, "board_move" e "MOVE_BOARD").
struct MoveKey {
    std::string move_type;
    std::int64_t source = 0;
    std::int64_t target = 0;
    std::optional<UnitIdentity> unit_identity;

    bool operator==(const MoveKey&) const = default;
};

class AntiLoopEngine {
public:
    [[nodiscard]] MoveKey make_move_key(
        const std::string& move_type,
        std::int64_t source,
        std::int64_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;
};

} // namespace tft::decision
