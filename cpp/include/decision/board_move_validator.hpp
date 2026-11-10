
#pragma once

#include <cstddef>
#include <functional>
#include <vector>

enum class BoardMoveKind {
    Invalid,
    Move,  // Destino vazio
    Swap   // Destino ocupado
};

struct BoardMoveValidation {
    bool valid = false;
    BoardMoveKind kind = BoardMoveKind::Invalid;
};

using AntiLoopCheck = std::function<bool(
    BoardMoveKind kind,
    std::size_t source,
    std::size_t target
)>;

inline BoardMoveValidation validate_board_move(
    std::size_t source,
    std::size_t target,
    const std::vector<bool>& occupied,
    const AntiLoopCheck& should_block = {}
) {
    // 1. Origem e destino devem existir no tabuleiro.
    if (source >= occupied.size() ||
        target >= occupied.size()) {
        return {};
    }

    // 2. Não permite mover para a própria posição.
    if (source == target) {
        return {};
    }

    // 3. A origem precisa conter uma unidade.
    if (!occupied[source]) {
        return {};
    }

    // 4. Classifica o movimento conforme o destino.
    const BoardMoveKind kind = occupied[target]
        ? BoardMoveKind::Swap
        : BoardMoveKind::Move;

    // 5. Preserva o ponto de integração com o AntiLoop.
    if (should_block) {
        try {
            if (should_block(kind, source, target)) {
                return {};
            }
        } catch (...) {
            // Compatibilidade com o Python atual:
            // uma falha na consulta ao AntiLoop não
            // invalida automaticamente o movimento.
        }
    }

    return {true, kind};
}
