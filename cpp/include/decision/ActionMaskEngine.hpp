
#pragma once

#include "decision/AntiLoopEngine.hpp"
#include "decision/DecisionState.hpp"
#include "decision/DecisionTypes.hpp"

#include <array>
#include <cstdint>

namespace tft::decision {

struct ActionMaskBatch {
    std::array<MaskValue, ACTION_TYPE_COUNT> type_mask{};
    std::array<MaskValue, SHOP_SIZE> shop_mask{};
    std::array<MaskValue, BENCH_SIZE> bench_source_mask{};
    std::array<MaskValue, BOARD_SIZE> board_target_mask{};
    std::array<MaskValue, BOARD_SIZE> board_source_mask{};

    std::array<
        std::array<MaskValue, BOARD_SIZE>,
        BOARD_SIZE
    > board_move_target_masks{};

    // União dos destinos reais do tabuleiro, sem fallbacks
    // de origens que não possuem movimentos válidos.
    std::array<MaskValue, BOARD_SIZE>
        conditioned_board_target_mask{};

    std::array<MaskValue, BENCH_SIZE> bench_move_source_mask{};

    std::array<
        std::array<MaskValue, BOARD_SIZE>,
        BENCH_SIZE
    > bench_to_board_target_masks{};

    // Disponibilidade real, separada dos fallbacks categóricos.
    bool buy_available = false;
    bool sell_available = false;
    bool board_move_available = false;
    bool bench_move_available = false;

    // Contadores de candidatos reais; não incluem fallbacks categóricos.
    MaskDiagnostics diagnostics;
};

class ActionMaskEngine {
public:
    // Calcula todas as máscaras em lote.
    // Não registra movimentos nem modifica o histórico anti-loop.
    [[nodiscard]] ActionMaskBatch generate_masks(
        const PlayerState& state,
        const AntiLoopEngine& anti_loop,
        bool include_board_target = true
    ) const;

private:
    [[nodiscard]] static bool can_spend(
        const EconomyState& economy,
        std::int32_t amount
    ) noexcept;

    [[nodiscard]] static bool has_free_bench_slot(
        const PlayerState& state
    ) noexcept;

    [[nodiscard]] static bool is_valid_board_move(
        const PlayerState& state,
        const AntiLoopEngine& anti_loop,
        PositionSignature& current_signature,
        RawIndex source,
        RawIndex target,
        MaskDiagnostics& diagnostics
    );

    [[nodiscard]] static bool is_valid_bench_to_board_move(
        const PlayerState& state,
        const AntiLoopEngine& anti_loop,
        PositionSignature& current_signature,
        RawIndex bench_slot,
        RawIndex target,
        MaskDiagnostics& diagnostics
    );

    static void validate_state(const PlayerState& state);
    static void set_fallback(ActionMaskBatch& masks);
};

} // namespace tft::decision