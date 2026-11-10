
#include "decision/MoveValidator.hpp"

#include <array>
#include <cassert>
#include <optional>

using namespace tft::decision;

namespace {

UnitSnapshot make_unit(std::int64_t id) {
    UnitSnapshot unit;
    unit.identity.id = id;
    unit.identity.star = 1;
    return unit;
}

} // namespace

int main() {
    using Slot = std::optional<UnitSnapshot>;

    // Tabuleiro reduzido intencionalmente para testar
    // o uso do tamanho real da sequência.
    std::array<Slot, 4> board{};
    std::array<Slot, 2> bench{};

    board[0] = make_unit(100);
    board[2] = make_unit(200);
    bench[0] = make_unit(300);

    // --------------------------------------------------------
    // Disponibilidade de posições
    // --------------------------------------------------------

    assert(!MoveValidator::is_board_position_available(
        board, 0
    ));

    assert(MoveValidator::is_board_position_available(
        board, 1
    ));

    assert(!MoveValidator::is_board_position_available(
        board, -1
    ));

    assert(!MoveValidator::is_board_position_available(
        board, 4
    ));

    assert(MoveValidator::has_free_board_position(board));

    // --------------------------------------------------------
    // Movimento para destino vazio
    // --------------------------------------------------------

    const auto move = MoveValidator::validate_board_move(
        board, 0, 1
    );

    assert(move.is_valid());
    assert(move.move_type.has_value());
    assert(*move.move_type == MoveType::BOARD_MOVE);

    // --------------------------------------------------------
    // Troca com destino ocupado
    // --------------------------------------------------------

    const auto swap = MoveValidator::validate_board_move(
        board, 0, 2
    );

    assert(swap.is_valid());
    assert(swap.move_type.has_value());
    assert(*swap.move_type == MoveType::BOARD_SWAP);

    // --------------------------------------------------------
    // Origem vazia e índices inválidos
    // --------------------------------------------------------

    assert(!MoveValidator::validate_board_move(
        board, 1, 3
    ).is_valid());

    assert(!MoveValidator::validate_board_move(
        board, -1, 1
    ).is_valid());

    assert(!MoveValidator::validate_board_move(
        board, 0, 4
    ).is_valid());

    assert(!MoveValidator::validate_board_move(
        board, 0, 0
    ).is_valid());

    // --------------------------------------------------------
    // Banco -> tabuleiro
    // --------------------------------------------------------

    const auto bench_move =
        MoveValidator::validate_bench_to_board_move(
            board, bench, 0, 3
        );

    assert(bench_move.is_valid());
    assert(
        *bench_move.move_type == MoveType::BENCH_TO_BOARD
    );

    assert(!MoveValidator::validate_bench_to_board_move(
        board, bench, 0, 2
    ).is_valid());

    assert(!MoveValidator::validate_bench_to_board_move(
        board, bench, 1, 3
    ).is_valid());

    assert(!MoveValidator::validate_bench_to_board_move(
        board, bench, -1, 3
    ).is_valid());

    assert(!MoveValidator::validate_bench_to_board_move(
        board, bench, 0, 4
    ).is_valid());

    // --------------------------------------------------------
    // A validação não pode modificar o estado real
    // --------------------------------------------------------

    assert(board[0].has_value());
    assert(board[0]->identity.id == 100);

    assert(board[2].has_value());
    assert(board[2]->identity.id == 200);

    assert(!board[1].has_value());
    assert(!board[3].has_value());

    assert(bench[0].has_value());
    assert(bench[0]->identity.id == 300);

    assert(!bench[1].has_value());

    // Tabuleiro completamente ocupado.
    std::array<Slot, 2> full_board{
        make_unit(400),
        make_unit(500)
    };

    assert(!MoveValidator::has_free_board_position(full_board));
    assert(!MoveValidator::is_board_position_available(
        full_board, 1
    ));

    // --------------------------------------------------------
    // Restrições adicionais: banco -> tabuleiro
    // --------------------------------------------------------

    // Destino negativo.
    assert(!MoveValidator::validate_bench_to_board_move(
        board, bench, 0, -1
    ).is_valid());

    // Banco sem nenhuma unidade.
    std::array<Slot, 2> empty_bench{};

    assert(!MoveValidator::validate_bench_to_board_move(
        board, empty_bench, 0, 3
    ).is_valid());

    // Tabuleiro completamente ocupado.
    std::array<Slot, 4> completely_full_board{
        make_unit(401),
        make_unit(402),
        make_unit(403),
        make_unit(404)
    };

    assert(!MoveValidator::has_free_board_position(
        completely_full_board
    ));

    // Nenhuma unidade do banco pode entrar num tabuleiro cheio.
    assert(!MoveValidator::validate_bench_to_board_move(
        completely_full_board, bench, 0, 0
    ).is_valid());

    assert(!MoveValidator::validate_bench_to_board_move(
        completely_full_board, bench, 0, 3
    ).is_valid());

    // Uma tentativa inválida não pode alterar o estado.
    const auto invalid_move =
        MoveValidator::validate_bench_to_board_move(
            completely_full_board, bench, 0, 0
        );

    assert(!invalid_move.is_valid());

    for (std::size_t i = 0; i < completely_full_board.size(); ++i) {
        assert(completely_full_board[i].has_value());
        assert(
            completely_full_board[i]->identity.id
            == static_cast<std::int64_t>(401 + i)
        );
    }

    assert(bench[0].has_value());
    assert(bench[0]->identity.id == 300);

    return 0;
}
