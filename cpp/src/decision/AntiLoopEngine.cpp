#include "decision/AntiLoopEngine.hpp"

#include <algorithm>
#include <iterator>
#include <utility>

namespace tft::decision {

AntiLoopEngine::AntiLoopEngine(AntiLoopConfig config)
    : config_(config) {
}

void AntiLoopEngine::reset() {
    // O Python limpa os históricos, mas mantém as métricas.
    const auto metrics = history_.metrics;

    history_ = AntiLoopHistory{};
    history_.metrics = metrics;
}

MoveKey AntiLoopEngine::make_move_key(
    const std::string& move_type,
    std::int64_t source,
    std::int64_t target,
    const std::optional<UnitIdentity>& unit
) const {
    return MoveKey{
        move_type,
        source,
        target,
        unit
    };
}


PositionSignature AntiLoopEngine::make_board_signature(
    const PlayerState& state
) const {
    PositionSignature signature;

    // Uma posição ocupada continua ocupada mesmo que a unidade
    // não possua UUID ou ID. O Python também preserva essa unidade
    // na assinatura usando (id, star).
    for (std::size_t i = 0; i < BOARD_SIZE; ++i) {
        if (!state.board[i].has_value()) {
            signature.board[i] = std::nullopt;
            continue;
        }

        signature.board[i] = state.board[i]->identity;
    }

    for (std::size_t i = 0; i < BENCH_SIZE; ++i) {
        if (!state.bench[i].has_value()) {
            signature.bench[i] = std::nullopt;
            continue;
        }

        signature.bench[i] = state.bench[i]->identity;
    }

    return signature;
}


StateRegistrationResult AntiLoopEngine::register_state(
    const PositionSignature& signature
) {
    history_.position_history.push_back(signature);
    trim_position_history();

    auto it = std::find_if(
        history_.state_visits.begin(),
        history_.state_visits.end(),
        [&signature](const StateVisit& visit) {
            return visit.signature == signature;
        }
    );

    if (it == history_.state_visits.end()) {
        history_.state_visits.push_back(
            StateVisit{signature, 1, config_.loop_threshold <= 1}
        );

        it = std::prev(history_.state_visits.end());
    } else {
        ++it->visits;
        it->repeated = it->visits >= config_.loop_threshold;
    }

    history_.last_board_signature = signature;

    return StateRegistrationResult{
        signature,
        it->visits >= config_.loop_threshold,
        it->visits
    };
}

MoveRecord AntiLoopEngine::register_move(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) {
    MoveRecord move{
        move_type,
        source,
        target,
        unit
    };

    history_.move_history.push_back(move);
    trim_move_history();

    history_.last_move = move;

    return move;
}

bool AntiLoopEngine::same_move_key(
    const MoveRecord& record,
    const MoveKey& key
) {
    return record.move_type == key.move_type
        && record.source == key.source
        && record.target == key.target
        && record.unit == key.unit_identity;
}

MoveKey AntiLoopEngine::block_move(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) {
    const MoveKey key = make_move_key(
        move_type,
        source,
        target,
        unit
    );

    // Repetir um bloqueio existente move-o para o final,
    // tal como a implementação Python.
    const auto existing = std::find_if(
        history_.blocked_moves.begin(),
        history_.blocked_moves.end(),
        [&key](const BlockedMoveRecord& blocked) {
            return same_move_key(blocked.move, key);
        }
    );

    if (existing != history_.blocked_moves.end()) {
        history_.blocked_moves.erase(existing);
    } else if (
        config_.blocked_move_size > 0
        && history_.blocked_moves.size() >= config_.blocked_move_size
    ) {
        history_.blocked_moves.erase(
            history_.blocked_moves.begin()
        );
    }

    // Com capacidade zero, não há bloqueios que possam ser retidos.
    if (config_.blocked_move_size > 0) {
        history_.blocked_moves.push_back(
            BlockedMoveRecord{
                MoveRecord{
                    key.move_type,
                    static_cast<std::int32_t>(key.source),
                    static_cast<std::int32_t>(key.target),
                    key.unit_identity
                },
                history_.last_board_signature
            }
        );

        trim_blocked_moves();
    }

    return key;
}

bool AntiLoopEngine::is_move_blocked(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) const {
    const MoveKey key = make_move_key(
        move_type,
        source,
        target,
        unit
    );

    const auto it = std::find_if(
        history_.blocked_moves.begin(),
        history_.blocked_moves.end(),
        [&key](const BlockedMoveRecord& blocked) {
            return same_move_key(blocked.move, key);
        }
    );

    if (it == history_.blocked_moves.end()) {
        return false;
    }

    // O bloqueio só vale na assinatura em que foi registrado.
    return it->blocked_state == history_.last_board_signature;
}

bool AntiLoopEngine::is_reverse_move(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) const {
    if (!history_.last_move.has_value()) {
        return false;
    }

    const auto& last = *history_.last_move;

    // Um swap pode ser desfeito por qualquer uma das unidades
    // que passaram a ocupar o par de posições.
    if (
        move_type == "board_swap"
        && last.move_type == "board_swap"
    ) {
        return (
            last.source == source && last.target == target
        ) || (
            last.source == target && last.target == source
        );
    }

    if (last.unit != unit) {
        return false;
    }

    if (last.move_type != move_type) {
        return false;
    }

    return last.source == target
        && last.target == source;
}

bool AntiLoopEngine::is_oscillating(
    const std::optional<UnitIdentity>& unit,
    std::int32_t source,
    std::int32_t target,
    const std::optional<std::string>& move_type
) const {
    if (!unit.has_value() || history_.move_history.empty()) {
        return false;
    }

    // O Python examina os seis registros mais recentes antes
    // de filtrar os movimentos relevantes para a unidade.
    const std::size_t start =
        history_.move_history.size() > 6
            ? history_.move_history.size() - 6
            : 0;

    std::vector<std::pair<std::int32_t, std::int32_t>> relevant;

    const bool candidate_is_swap =
        move_type.has_value() && *move_type == "board_swap";

    for (std::size_t i = start; i < history_.move_history.size(); ++i) {
        const auto& move = history_.move_history[i];

        if (move.unit != unit) {
            continue;
        }

        const bool include =
            candidate_is_swap
                ? (
                    move.move_type == "board_swap"
                    || move.move_type == "board_move"
                )
                : move.move_type == "board_move";

        if (include) {
            relevant.emplace_back(move.source, move.target);
        }
    }

    if (relevant.empty()) {
        return false;
    }

    // O último movimento relevante precisa terminar na origem candidata.
    if (relevant.back().second != source) {
        return false;
    }

    std::vector<std::int32_t> chain{
        relevant.back().first,
        relevant.back().second
    };

    for (
        auto it = relevant.rbegin() + 1;
        it != relevant.rend();
        ++it
    ) {
        const auto previous_source = it->first;
        const auto previous_target = it->second;

        if (previous_target != chain.front()) {
            break;
        }

        chain.insert(chain.begin(), previous_source);
    }

    // Só caracteriza oscilação se o destino já apareceu
    // pelo menos duas vezes antes do movimento candidato.
    return std::count(
        chain.begin(),
        chain.end() - 1,
        target
    ) >= 2;
}

std::optional<std::string> AntiLoopEngine::normalize_bench_move(
    const std::string& move_type
) {
    if (
        move_type == "MOVE_BENCH_TO_BOARD"
        || move_type == "bench_to_board"
    ) {
        return "bench_to_board";
    }

    if (
        move_type == "MOVE_BOARD_TO_BENCH"
        || move_type == "board_to_bench"
    ) {
        return "board_to_bench";
    }

    return std::nullopt;
}

bool AntiLoopEngine::is_bench_board_loop(
    const std::optional<UnitIdentity>& unit,
    const std::optional<std::string>& move_type,
    std::optional<std::int32_t> source,
    std::optional<std::int32_t> target
) const {
    if (!unit.has_value() || !move_type.has_value()) {
        return false;
    }

    const auto candidate_type = normalize_bench_move(*move_type);

    if (!candidate_type.has_value()) {
        return false;
    }

    struct BenchTransition {
        std::string type;
        std::int32_t source;
        std::int32_t target;
    };

    std::vector<BenchTransition> recent;

    for (const auto& move : history_.move_history) {
        if (move.unit != unit) {
            continue;
        }

        const auto normalized = normalize_bench_move(move.move_type);

        if (normalized.has_value()) {
            recent.push_back({
                *normalized,
                move.source,
                move.target
            });
        }
    }

    if (recent.size() < 2) {
        return false;
    }

    const auto& previous = recent[recent.size() - 2];
    const auto& last = recent.back();

    const bool reversed_transition =
        previous.type != last.type
        && previous.source == last.target
        && previous.target == last.source;

    if (!reversed_transition) {
        return false;
    }

    return (
        *candidate_type == previous.type
        && source.has_value()
        && target.has_value()
        && *source == previous.source
        && *target == previous.target
    );
}

bool AntiLoopEngine::is_cycle_move(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) const {
    if (
        move_type != "board_move"
        && move_type != "board_swap"
    ) {
        return false;
    }

    std::vector<std::pair<std::int32_t, std::int32_t>> recent;

    for (const auto& move : history_.move_history) {
        if (
            (move.move_type == "board_move"
                || move.move_type == "board_swap")
            && move.unit == unit
        ) {
            recent.emplace_back(move.source, move.target);
        }
    }

    if (recent.size() > 8) {
        recent.erase(
            recent.begin(),
            recent.end() - 8
        );
    }

    if (recent.empty()) {
        return false;
    }

    bool started = false;
    std::optional<std::int32_t> expected_position;
    bool cycle_completed = false;

    for (const auto& [src, dst] : recent) {
        if (!started) {
            if (src == target) {
                started = true;
                expected_position = dst;
            }

            continue;
        }

        // Uma quebra na continuidade invalida a sequência.
        if (src != *expected_position) {
            return false;
        }

        expected_position = dst;

        if (dst == target) {
            cycle_completed = true;
        }
    }

    // O ciclo só bloqueia quando já se completou anteriormente
    // e a sequência terminou na origem do movimento candidato.
    return started
        && cycle_completed
        && expected_position.has_value()
        && *expected_position == source;
}

std::optional<std::string> AntiLoopEngine::get_block_reason(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) const {
    // A ordem é parte do contrato: determina o motivo retornado.
    if (is_move_blocked(move_type, source, target, unit)) {
        return "explicit";
    }

    if (is_reverse_move(move_type, source, target, unit)) {
        return "reverse";
    }

    if (is_oscillating(unit, source, target, move_type)) {
        return "oscillation";
    }

    const bool is_bench_candidate =
        move_type == "bench_to_board"
        || move_type == "board_to_bench"
        || move_type == "MOVE_BENCH_TO_BOARD"
        || move_type == "MOVE_BOARD_TO_BENCH";

    if (
        is_bench_candidate
        && is_bench_board_loop(
            unit,
            move_type,
            source,
            target
        )
    ) {
        return "bench_board_loop";
    }

    if (is_cycle_move(move_type, source, target, unit)) {
        return "cycle";
    }

    return std::nullopt;
}

bool AntiLoopEngine::should_block_move(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) const {
    return get_block_reason(
        move_type,
        source,
        target,
        unit
    ).has_value();
}

double AntiLoopEngine::evaluate_move_risk(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit
) const {
    if (is_move_blocked(move_type, source, target, unit)) {
        return 1.0;
    }

    double risk = 0.0;

    if (is_reverse_move(move_type, source, target, unit)) {
        risk += 0.7;
    }

    if (is_oscillating(unit, source, target, move_type)) {
        risk += 0.8;
    }

    if (
        is_bench_board_loop(
            unit,
            move_type,
            source,
            target
        )
    ) {
        risk += 0.9;
    }

    return std::min(1.0, risk);
}

bool AntiLoopEngine::was_state_seen(
    const PositionSignature& signature
) const {
    return std::any_of(
        history_.state_visits.begin(),
        history_.state_visits.end(),
        [&signature](const StateVisit& visit) {
            return visit.signature == signature;
        }
    );
}

std::uint32_t AntiLoopEngine::get_state_visits(
    const PositionSignature& signature
) const {
    const auto it = std::find_if(
        history_.state_visits.begin(),
        history_.state_visits.end(),
        [&signature](const StateVisit& visit) {
            return visit.signature == signature;
        }
    );

    return it == history_.state_visits.end()
        ? 0
        : it->visits;
}

AntiLoopStateSummary AntiLoopEngine::get_state() const {
    return AntiLoopStateSummary{
        history_.position_history.size(),
        history_.move_history.size(),
        history_.blocked_moves.size(),
        history_.state_visits.size(),
        history_.last_move
    };
}

ExecutionMetrics AntiLoopEngine::get_metrics() const {
    return history_.metrics;
}

void AntiLoopEngine::clear_old_blocks() {
    trim_blocked_moves();
}

void AntiLoopEngine::record_execution_attempt() {
    ++history_.metrics.execution_attempts;
}

void AntiLoopEngine::record_execution_block(
    const std::string& reason
) {
    ++history_.metrics.execution_blocks;

    if (reason == "reverse") {
        ++history_.metrics.blocked_reverse;
    } else if (reason == "oscillation") {
        ++history_.metrics.blocked_oscillation;
    } else if (reason == "explicit") {
        ++history_.metrics.blocked_explicit;
    } else if (reason == "bench_board_loop") {
        ++history_.metrics.blocked_bench_board_loop;
    } else if (reason == "cycle") {
        ++history_.metrics.blocked_cycle;
    }
}

void AntiLoopEngine::record_successful_move(
    const std::string& move_type
) {
    if (
        move_type == "board_move"
        || move_type == "board_swap"
    ) {
        ++history_.metrics.board_moves_executed;
    } else if (move_type == "bench_to_board") {
        ++history_.metrics.bench_to_board_executed;
    }
}

void AntiLoopEngine::trim_position_history() {
    while (
        history_.position_history.size() > config_.history_size
    ) {
        history_.position_history.erase(
            history_.position_history.begin()
        );
    }
}

void AntiLoopEngine::trim_move_history() {
    while (
        history_.move_history.size() > config_.history_size
    ) {
        history_.move_history.erase(
            history_.move_history.begin()
        );
    }
}

void AntiLoopEngine::trim_blocked_moves() {
    while (
        history_.blocked_moves.size() > config_.blocked_move_size
    ) {
        history_.blocked_moves.erase(
            history_.blocked_moves.begin()
        );
    }
}

} // namespace tft::decision