
#pragma once

#include "decision/DecisionState.hpp"

#include <cstddef>
#include <cstdint>
#include <optional>
#include <string>
#include <vector>

namespace tft::decision {

// Assinatura de posicionamento. A posição de cada unidade é
// representada pelo slot em que sua identidade aparece.
struct PositionSignature {
    std::array<std::optional<UnitIdentity>, BOARD_SIZE> board{};
    std::array<std::optional<UnitIdentity>, BENCH_SIZE> bench{};

    bool operator==(const PositionSignature&) const = default;
};

// Resultado do registro de um estado visitado.
struct StateVisit {
    PositionSignature signature;
    std::uint32_t visits = 0;
    bool repeated = false;
};

// Movimento efetivamente registrado no histórico.
struct MoveRecord {
    MoveType type = MoveType::BOARD_MOVE;
    std::int32_t source = -1;
    std::int32_t target = -1;
    std::optional<UnitIdentity> unit;
};

// Movimento bloqueado, associado à assinatura de estado
// em que o bloqueio foi registrado.
struct BlockedMoveRecord {
    MoveRecord move;
    std::optional<PositionSignature> blocked_state;
};

// Métricas de execução. As consultas de máscara não devem
// incrementar esses contadores.
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
};

// Dados persistentes do AntiLoop.
// Os limites de retenção serão aplicados pelo componente
// que manipular este histórico, não por esta estrutura.
struct AntiLoopHistory {
    std::vector<PositionSignature> position_history;
    std::vector<MoveRecord> move_history;
    std::vector<BlockedMoveRecord> blocked_moves;
    std::vector<StateVisit> state_visits;

    std::optional<PositionSignature> last_board_signature;
    std::optional<MoveRecord> last_move;

    ExecutionMetrics metrics;
};

} // namespace tft::decision
