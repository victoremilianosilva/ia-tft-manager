
#include "decision/MoveValidator.hpp"

#include <cstddef>
#include <string>

namespace tft::decision {
namespace {

MoveValidationResult invalid_result(
    const char* code,
    const char* message
) {
    MoveValidationResult result;

    result.validation.status = ValidationStatus::INVALID;
    result.validation.error_code = code;
    result.validation.error_message = message;
    result.move_type = std::nullopt;

    return result;
}

MoveValidationResult valid_result(MoveType move_type) {
    MoveValidationResult result;

    result.validation.status = ValidationStatus::VALID;
    result.validation.block_reason = BlockReason::NONE;
    result.validation.error_code.clear();
    result.validation.error_message.clear();
    result.move_type = move_type;

    return result;
}

bool is_valid_index(
    RawIndex index,
    std::size_t size
) noexcept {
    return index >= 0
        && static_cast<std::size_t>(index) < size;
}

} // namespace

bool MoveValidator::is_board_position_available(
    std::span<const std::optional<UnitSnapshot>> board,
    RawIndex position
) noexcept {
    if (!is_valid_index(position, board.size())) {
        return false;
    }

    return !board[static_cast<std::size_t>(position)].has_value();
}

bool MoveValidator::has_free_board_position(
    std::span<const std::optional<UnitSnapshot>> board
) noexcept {
    for (const auto& unit : board) {
        if (!unit.has_value()) {
            return true;
        }
    }

    return false;
}

MoveValidationResult MoveValidator::validate_board_move(
    std::span<const std::optional<UnitSnapshot>> board,
    RawIndex source,
    RawIndex target
) {
    // Os índices são validados antes de acessar o tabuleiro.
    if (!is_valid_index(source, board.size())) {
        return invalid_result(
            "INVALID_SOURCE",
            "A origem nao pertence ao tabuleiro."
        );
    }

    if (!is_valid_index(target, board.size())) {
        return invalid_result(
            "INVALID_TARGET",
            "O destino nao pertence ao tabuleiro."
        );
    }

    if (source == target) {
        return invalid_result(
            "SAME_POSITION",
            "Origem e destino nao podem ser iguais."
        );
    }

    const auto source_index =
        static_cast<std::size_t>(source);

    if (!board[source_index].has_value()) {
        return invalid_result(
            "EMPTY_SOURCE",
            "A origem nao contem uma unidade."
        );
    }

    // Mantém a regra atual do Python:
    // destino ocupado permite classificar uma troca;
    // destino vazio permite classificar um movimento.
    if (board[target_index].has_value()) {
        return valid_result(MoveType::BOARD_SWAP);
    }

    return valid_result(MoveType::BOARD_MOVE);
}

MoveValidationResult
MoveValidator::validate_bench_to_board_move(
    std::span<const std::optional<UnitSnapshot>> board,
    std::span<const std::optional<UnitSnapshot>> bench,
    RawIndex bench_slot,
    RawIndex target
) {
    if (!is_valid_index(bench_slot, bench.size())) {
        return invalid_result(
            "INVALID_BENCH_SLOT",
            "O slot do banco nao e valido."
        );
    }

    if (!is_valid_index(target, board.size())) {
        return invalid_result(
            "INVALID_TARGET",
            "O destino nao pertence ao tabuleiro."
        );
    }

    const auto bench_index =
        static_cast<std::size_t>(bench_slot);

    const auto target_index =
        static_cast<std::size_t>(target);

    if (!bench[bench_index].has_value()) {
        return invalid_result(
            "EMPTY_BENCH_SLOT",
            "O slot do banco nao contem uma unidade."
        );
    }

    // Destino vazio: implantação que consome capacidade de nível.
    // Destino ocupado: substituição atômica; a unidade atual retorna ao banco.
    // A regra de capacidade é validada na máscara e na execução da ação.
    return valid_result(MoveType::BENCH_TO_BOARD);
}

} // namespace tft::decision
