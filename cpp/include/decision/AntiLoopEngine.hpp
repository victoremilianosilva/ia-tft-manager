#pragma once

#include "decision/DecisionHistory.hpp"

#include <cstddef>
#include <cstdint>
#include <optional>
#include <string>
#include <vector>

namespace tft::decision {

struct MoveKey {
    std::string move_type;
    std::int64_t source = 0;
    std::int64_t target = 0;
    std::optional<UnitIdentity> unit_identity;

    bool operator==(const MoveKey&) const = default;
};

struct AntiLoopConfig {
    std::size_t history_size = 20;
    std::size_t blocked_move_size = 10;
    std::uint32_t loop_threshold = 2;
};

struct StateRegistrationResult {
    PositionSignature signature;
    bool repeated = false;
    std::uint32_t visits = 0;
};

struct AntiLoopStateSummary {
    std::size_t history_size = 0;
    std::size_t move_history_size = 0;
    std::size_t blocked_moves = 0;
    std::size_t known_states = 0;
    std::optional<MoveRecord> last_move;
};

class AntiLoopEngine {
public:
    AntiLoopEngine();
    explicit AntiLoopEngine(AntiLoopConfig config);
    
    // Reset de episódio preserva métricas acumuladas.
    void reset();

    // Inicia uma nova preparação: heurísticas locais são limpas e estados
    // visitados expiram após uma janela limitada de rodadas.
    void begin_round(std::uint32_t round_number);

    // Identidade do movimento e assinatura do posicionamento.
    [[nodiscard]] MoveKey make_move_key(
        const std::string& move_type,
        std::int64_t source,
        std::int64_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;

    [[nodiscard]] PositionSignature make_board_signature(
        const PlayerState& state
    ) const;

    // Operações que alteram o histórico.
    [[nodiscard]] StateRegistrationResult register_state(
        const PositionSignature& signature
    );

    [[nodiscard]] MoveRecord register_move(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt,
        const std::optional<UnitIdentity>& displaced_unit = std::nullopt
    );

    [[nodiscard]] MoveKey block_move(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    );

    // Consultas sem efeitos colaterais.
    [[nodiscard]] bool is_move_blocked(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;

    [[nodiscard]] bool is_reverse_move(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;

    [[nodiscard]] bool is_oscillating(
        const std::optional<UnitIdentity>& unit,
        std::int32_t source,
        std::int32_t target,
        const std::optional<std::string>& move_type = std::nullopt
    ) const;

    [[nodiscard]] bool is_bench_board_loop(
        const std::optional<UnitIdentity>& unit,
        const std::optional<std::string>& move_type = std::nullopt,
        std::optional<std::int32_t> source = std::nullopt,
        std::optional<std::int32_t> target = std::nullopt
    ) const;

    [[nodiscard]] bool is_cycle_move(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;

    [[nodiscard]] std::optional<std::string> get_block_reason(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;

    [[nodiscard]] bool should_block_move(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;

    [[nodiscard]] double evaluate_move_risk(
        const std::string& move_type,
        std::int32_t source,
        std::int32_t target,
        const std::optional<UnitIdentity>& unit = std::nullopt
    ) const;

    // Consultas de estado.
    [[nodiscard]] bool was_state_seen(
        const PositionSignature& signature
    ) const;

    [[nodiscard]] std::uint32_t get_state_visits(
        const PositionSignature& signature
    ) const;

    [[nodiscard]] AntiLoopStateSummary get_state() const;

    [[nodiscard]] ExecutionMetrics get_metrics() const;

    // Limpeza explícita de bloqueios antigos.
    void clear_old_blocks();

    // Métricas: devem ser chamadas no fluxo real de execução,
    // não durante a criação de máscaras ou consultas de candidatos.
    void record_execution_attempt();

    void record_execution_block(const std::string& reason);

    void record_successful_move(const std::string& move_type);

    // Registra diagnósticos da geração de máscaras sem alterar o histórico.
    void record_mask_diagnostics(const MaskDiagnostics& diagnostics);

private:
    AntiLoopConfig config_;
    AntiLoopHistory history_;

    [[nodiscard]] static bool same_move_key(
        const MoveRecord& record,
        const MoveKey& key
    );

    [[nodiscard]] static std::optional<std::string> normalize_bench_move(
        const std::string& move_type
    );

    void trim_position_history();
    void trim_move_history();
    void trim_blocked_moves();
};

} // namespace tft::decision