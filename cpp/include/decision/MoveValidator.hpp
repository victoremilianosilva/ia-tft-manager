
#pragma once

#include "decision/DecisionState.hpp"
#include "decision/DecisionResult.hpp"
#include "decision/DecisionTypes.hpp"

#include <optional>
#include <span>

namespace tft::decision {

struct MoveValidationResult {
    ValidationResult validation;

    // Só possui valor quando origem e destino permitem
    // classificar o movimento.
    std::optional<MoveType> move_type;

    [[nodiscard]] bool is_valid() const noexcept {
        return validation.is_valid();
    }
};

enum class ValidationFailureKind {
    NONE,
    INVALID_INPUT,
    DEPENDENCY_FAILURE
};

struct DetailedMoveValidationResult {
    MoveValidationResult movement;
    ValidationFailureKind failure_kind =
        ValidationFailureKind::NONE;

    [[nodiscard]] bool is_valid() const noexcept {
        return movement.is_valid();
    }

    [[nodiscard]] bool has_dependency_failure() const noexcept {
        return failure_kind ==
            ValidationFailureKind::DEPENDENCY_FAILURE;
    }
};


class MoveValidator {
public:
    // Consulta somente de leitura: posição válida e vazia.
    [[nodiscard]] static bool is_board_position_available(
        std::span<const std::optional<UnitSnapshot>> board,
        RawIndex position
    ) noexcept;

    // Consulta somente de leitura: existe ao menos uma casa vazia.
    [[nodiscard]] static bool has_free_board_position(
        std::span<const std::optional<UnitSnapshot>> board
    ) noexcept;

    // Valida movimento dentro do tabuleiro.
    //
    // Destino vazio   -> BOARD_MOVE.
    // Destino ocupado -> BOARD_SWAP.
    //
    // A política AntiLoop é uma etapa separada.
    [[nodiscard]] static MoveValidationResult validate_board_move(
        std::span<const std::optional<UnitSnapshot>> board,
        RawIndex source,
        RawIndex target
    );

    // Valida movimentação do banco para o tabuleiro.
    // Destino vazio implanta (consome capacidade); destino ocupado substitui
    // e devolve a unidade antiga ao mesmo slot do banco.
    [[nodiscard]] static MoveValidationResult
    validate_bench_to_board_move(
        std::span<const std::optional<UnitSnapshot>> board,
        std::span<const std::optional<UnitSnapshot>> bench,
        RawIndex bench_slot,
        RawIndex target
    );
};

} // namespace tft::decision
