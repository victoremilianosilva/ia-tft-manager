#pragma once

#include "decision/DecisionState.hpp"

#include <array>
#include <cstddef>
#include <cstdint>
#include <optional>
#include <string>
#include <unordered_map>
#include <vector>

namespace tft::decision {

// Assinatura do posicionamento no tabuleiro e no banco.
struct PositionSignature {
    std::array<std::optional<UnitIdentity>, BOARD_SIZE> board{};
    std::array<std::optional<UnitIdentity>, BENCH_SIZE> bench{};

    // XOR/Zobrist-style hash cache. Equality deliberately ignores the cache.
    mutable std::size_t cached_hash = 0;
    mutable bool hash_cached = false;

    bool operator==(const PositionSignature& other) const {
        return board == other.board && bench == other.bench;
    }

    void swap_board_slots(std::size_t first, std::size_t second);
    void swap_board_bench(std::size_t board_slot, std::size_t bench_slot);
};

struct PositionSignatureHash {
    [[nodiscard]] std::size_t operator()(
        const PositionSignature& signature
    ) const noexcept;
};

// Resultado do registro de um estado visitado.
struct StateVisit {
    PositionSignature signature;
    std::uint32_t visits = 0;
    bool repeated = false;
    std::uint32_t last_seen_round = 1;
};

// Movimento efetivamente registrado.
// O tipo permanece textual para preservar os aliases do Python.
struct MoveRecord {
    std::string move_type;
    std::int32_t source = -1;
    std::int32_t target = -1;
    std::optional<UnitIdentity> unit;
    // Unidade que ocupava o destino antes de uma substituição bench -> board.
    std::optional<UnitIdentity> displaced_unit;

    bool operator==(const MoveRecord&) const = default;
};

// Movimento bloqueado e estado em que o bloqueio foi criado.
struct BlockedMoveRecord {
    MoveRecord move;
    std::optional<PositionSignature> blocked_state;
};

// Diagnósticos coletados durante a geração das máscaras. Contam somente
// pares estruturalmente legais; fallbacks categóricos nunca entram nesses contadores.
struct MaskDiagnostics {
    std::uint64_t board_move_candidates = 0;
    std::uint64_t board_move_valid = 0;
    std::uint64_t board_move_blocked_anti_loop = 0;
    std::uint64_t board_move_blocked_seen_state = 0;

    std::uint64_t bench_move_candidates = 0;
    std::uint64_t bench_move_valid = 0;
    std::uint64_t bench_move_blocked_anti_loop = 0;
    std::uint64_t bench_move_blocked_seen_state = 0;

    std::uint64_t blocked_reverse = 0;
    std::uint64_t blocked_oscillation = 0;
    std::uint64_t blocked_explicit = 0;
    std::uint64_t blocked_bench_board_loop = 0;
    std::uint64_t blocked_cycle = 0;
};

// Métricas acumuladas durante a execução do ambiente.
struct ExecutionMetrics {
    std::uint64_t execution_attempts = 0;
    std::uint64_t execution_blocks = 0;

    std::uint64_t blocked_reverse = 0;
    std::uint64_t blocked_oscillation = 0;
    std::uint64_t blocked_explicit = 0;
    std::uint64_t blocked_bench_board_loop = 0;
    std::uint64_t blocked_cycle = 0;

    std::uint64_t board_moves_executed = 0;
    std::uint64_t bench_to_board_executed = 0;

    MaskDiagnostics mask;
};

// Histórico interno da engine AntiLoop.
// A retenção limitada é aplicada pela própria engine.
struct AntiLoopHistory {
    std::vector<PositionSignature> position_history;
    std::vector<MoveRecord> move_history;
    std::vector<BlockedMoveRecord> blocked_moves;
    std::vector<StateVisit> state_visits;
    // Índice O(1) médio para consultas e registro de estados já conhecidos.
    // O índice aponta para state_visits, cuja ordem é estável até reset().
    std::unordered_map<PositionSignature, std::size_t, PositionSignatureHash>
        state_visit_index;

    std::optional<PositionSignature> last_board_signature;
    std::optional<MoveRecord> last_move;

    ExecutionMetrics metrics;
    std::uint32_t current_round = 1;
    std::uint32_t state_window_rounds = 4;
};

} // namespace tft::decision