
#pragma once

#include "decision/DecisionState.hpp"
#include "decision/DecisionTypes.hpp"

#include <array>
#include <cstdint>
#include <string>

namespace tft::decision {

// Todas as máscaras são binárias. Os fallbacks técnicos usados
// para manter distribuições categóricas válidas não significam
// necessariamente que exista uma ação real disponível.
struct ActionMasks {
    std::array<MaskValue, ACTION_TYPE_COUNT> type_mask{};
    std::array<MaskValue, SHOP_SIZE> shop_mask{};
    std::array<MaskValue, BENCH_SIZE> bench_source_mask{};

    std::array<MaskValue, BOARD_SIZE> board_target_mask{};
    std::array<MaskValue, BOARD_SIZE> board_source_mask{};
    std::array<MaskValue, BOARD_SIZE> conditioned_board_target_mask{};

    // Destinos condicionados pela origem escolhida.
    std::array<
        std::array<MaskValue, BOARD_SIZE>,
        BOARD_SIZE
    > board_move_target_masks{};

    // Destinos condicionados pelo slot escolhido no banco.
    std::array<
        std::array<MaskValue, BOARD_SIZE>,
        BENCH_SIZE
    > bench_to_board_target_masks{};

    // Origens do banco que possuem ao menos um movimento válido.
    std::array<MaskValue, BENCH_SIZE> bench_move_source_mask{};
};

// Resultado de uma validação individual.
struct ValidationResult {
    ValidationStatus status = ValidationStatus::VALID;
    BlockReason block_reason = BlockReason::NONE;

    std::string error_code;
    std::string error_message;

    [[nodiscard]] bool is_valid() const noexcept {
        return status == ValidationStatus::VALID;
    }
};

// Resultado retornado por uma operação do motor de decisões.
struct DecisionResult {
    bool success = false;

    ActionMasks masks;
    ValidationResult validation;

    std::string error_code;
    std::string error_message;
};

} // namespace tft::decision
