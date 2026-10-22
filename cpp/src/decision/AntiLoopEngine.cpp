#include "decision/AntiLoopEngine.hpp"

#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

namespace tft::decision {

namespace {

void hash_combine(std::size_t& seed, std::size_t value) noexcept {
    seed ^= value + static_cast<std::size_t>(0x9e3779b9U)
        + (seed << 6U) + (seed >> 2U);
}

template <typename T>
void hash_optional(
    std::size_t& seed,
    const std::optional<T>& value
) noexcept {
    hash_combine(seed, value.has_value() ? 1U : 0U);
    if (value.has_value()) {
        hash_combine(seed, std::hash<T>{}(*value));
    }
}

void hash_identity(std::size_t& seed, const UnitIdentity& identity) noexcept {
    // Keep the hash contract aligned with UnitIdentity::operator==:
    // UUID identities ignore id/star; identities without UUID use id,
    // textual_id and star.
    hash_combine(seed, identity.uuid.has_value() ? 1U : 0U);
    if (identity.uuid.has_value()) {
        hash_combine(seed, std::hash<std::string>{}(*identity.uuid));
        return;
    }

    hash_optional(seed, identity.id);
    hash_optional(seed, identity.textual_id);
    hash_combine(seed, std::hash<std::uint8_t>{}(identity.star));
}

} // namespace

namespace {
std::size_t slot_contribution(
    bool is_bench, std::size_t slot, const std::optional<UnitIdentity>& unit
) noexcept {
    if (!unit.has_value()) return 0;
    std::size_t seed = is_bench ? static_cast<std::size_t>(0xB3A5U)
                                : static_cast<std::size_t>(0xB04DU);
    hash_combine(seed, slot);
    hash_identity(seed, *unit);
    return seed;
}
} // namespace

std::size_t PositionSignatureHash::operator()(
    const PositionSignature& signature
) const noexcept {
    if (signature.hash_cached) return signature.cached_hash;

    std::size_t result = 0;
    for (std::size_t i = 0; i < signature.board.size(); ++i)
        result ^= slot_contribution(false, i, signature.board[i]);
    for (std::size_t i = 0; i < signature.bench.size(); ++i)
        result ^= slot_contribution(true, i, signature.bench[i]);

    signature.cached_hash = result;
    signature.hash_cached = true;
    return result;
}

void PositionSignature::swap_board_slots(std::size_t first, std::size_t second) {
    (void)PositionSignatureHash{}(*this);
    if (first == second) return;
    cached_hash ^= slot_contribution(false, first, board[first]);
    cached_hash ^= slot_contribution(false, second, board[second]);
    std::swap(board[first], board[second]);
    cached_hash ^= slot_contribution(false, first, board[first]);
    cached_hash ^= slot_contribution(false, second, board[second]);
}

void PositionSignature::swap_board_bench(std::size_t board_slot, std::size_t bench_slot) {
    (void)PositionSignatureHash{}(*this);
    cached_hash ^= slot_contribution(false, board_slot, board[board_slot]);
    cached_hash ^= slot_contribution(true, bench_slot, bench[bench_slot]);
    std::swap(board[board_slot], bench[bench_slot]);
    cached_hash ^= slot_contribution(false, board_slot, board[board_slot]);
    cached_hash ^= slot_contribution(true, bench_slot, bench[bench_slot]);
}

AntiLoopEngine::AntiLoopEngine()
    : AntiLoopEngine(AntiLoopConfig{}) {
}

AntiLoopEngine::AntiLoopEngine(AntiLoopConfig config)
    : config_(config) {
}

void AntiLoopEngine::reset() {
    const auto metrics = history_.metrics;
    const auto state_window_rounds = history_.state_window_rounds;
    history_ = AntiLoopHistory{};
    history_.metrics = metrics;
    history_.state_window_rounds = state_window_rounds;
}

void AntiLoopEngine::begin_round(std::uint32_t round_number) {
    history_.current_round = std::max<std::uint32_t>(1, round_number);
    history_.position_history.clear();
    history_.move_history.clear();
    history_.blocked_moves.clear();
    history_.last_move.reset();
    history_.last_board_signature.reset();

    auto& visits = history_.state_visits;
    visits.erase(
        std::remove_if(visits.begin(), visits.end(), [&](const StateVisit& visit) {
            return history_.current_round > visit.last_seen_round
                && history_.current_round - visit.last_seen_round > history_.state_window_rounds;
        }),
        visits.end()
    );
    history_.state_visit_index.clear();
    history_.state_visit_index.reserve(visits.size());
    for (std::size_t i = 0; i < visits.size(); ++i) {
        history_.state_visit_index.emplace(visits[i].signature, i);
    }
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

    auto indexed = history_.state_visit_index.find(signature);
    std::size_t visit_index = 0;

    if (indexed == history_.state_visit_index.end()) {
        visit_index = history_.state_visits.size();
        history_.state_visits.push_back(
            StateVisit{signature, 1, config_.loop_threshold <= 1, history_.current_round}
        );
        history_.state_visit_index.emplace(signature, visit_index);
    } else {
        visit_index = indexed->second;
        auto& visit = history_.state_visits[visit_index];
        if (history_.current_round > visit.last_seen_round
            && history_.current_round - visit.last_seen_round > history_.state_window_rounds) {
            visit.visits = 1;
            visit.repeated = config_.loop_threshold <= 1;
        } else {
            ++visit.visits;
            visit.repeated = visit.visits >= config_.loop_threshold;
        }
        visit.last_seen_round = history_.current_round;
    }

    history_.last_board_signature = signature;
    const auto& visit = history_.state_visits[visit_index];

    return StateRegistrationResult{
        signature,
        visit.visits >= config_.loop_threshold,
        visit.visits
    };
}

MoveRecord AntiLoopEngine::register_move(
    const std::string& move_type,
    std::int32_t source,
    std::int32_t target,
    const std::optional<UnitIdentity>& unit,
    const std::optional<UnitIdentity>& displaced_unit
) {
    MoveRecord move{
        move_type,
        source,
        target,
        unit,
        displaced_unit
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
                    key.unit_identity,
                    std::nullopt
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
    if (history_.move_history.empty()) return false;

    // Unrelated actions must not hide the latest relevant reverse candidate.
    const MoveRecord* last_ptr = nullptr;
    for (auto it = history_.move_history.rbegin(); it != history_.move_history.rend(); ++it) {
        if (move_type == "board_swap" && it->move_type == "board_swap") {
            const bool same_pair = (it->source == source && it->target == target)
                || (it->source == target && it->target == source);
            if (same_pair) { last_ptr = &*it; break; }
        }
        const bool board_move_candidate =
            move_type == "board_move" || move_type == "board_swap";
        const bool same_unit_move =
            board_move_candidate
                ? (it->move_type == "board_move" || it->move_type == "board_swap")
                : it->move_type == move_type;
        if (it->unit == unit && same_unit_move) {
            last_ptr = &*it;
            break;
        }
    }
    if (last_ptr == nullptr) return false;
    const auto& last = *last_ptr;

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

    // Filtra primeiro pela unidade e pelo tipo de movimento; só então limita
    // o histórico. Antes, movimentos de outras unidades consumiam a janela de
    // seis registros e escondiam oscilações quando a política alternava peças.
    std::vector<std::pair<std::int32_t, std::int32_t>> relevant;

    const bool candidate_is_swap =
        move_type.has_value() && *move_type == "board_swap";

    for (const auto& move : history_.move_history) {
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

    if (relevant.size() > 6) {
        relevant.erase(relevant.begin(), relevant.end() - 6);
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

    // The action space has no board-to-bench action. A displaced unit is
    // tracked through MoveRecord::displaced_unit on bench_to_board instead.
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

    // A substituição registra a unidade que entrou no board. A reversão
    // seleciona a unidade deslocada, portanto a identidade muda entre ações.
    // Se a candidata é exatamente a unidade deslocada nos mesmos slots,
    // a ação desfaz imediatamente a substituição anterior.
    if (history_.last_move.has_value()) {
        const auto& last = *history_.last_move;
        const auto last_type = normalize_bench_move(last.move_type);
        if (
            last_type.has_value()
            && *last_type == *candidate_type
            && source.has_value()
            && target.has_value()
            && last.source == *source
            && last.target == *target
            && last.displaced_unit == unit
            && unit.has_value()
        ) {
            return true;
        }
    }

    // Non-immediate multi-round cycles are handled by the rolling
    // visited-state window; the executor has no board_to_bench action.
    return false;
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
        || move_type == "MOVE_BENCH_TO_BOARD";

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

    if (is_bench_board_loop(unit, move_type, source, target)) {
        risk += 0.9;
    }
    if (is_cycle_move(move_type, source, target, unit)) {
        risk += 0.85;
    }

    return std::min(1.0, risk);
}

bool AntiLoopEngine::was_state_seen(
    const PositionSignature& signature
) const {
    const auto indexed = history_.state_visit_index.find(signature);
    if (indexed == history_.state_visit_index.end()) return false;
    const auto& visit = history_.state_visits[indexed->second];
    return history_.current_round <= visit.last_seen_round
        || history_.current_round - visit.last_seen_round <= history_.state_window_rounds;
}

std::uint32_t AntiLoopEngine::get_state_visits(
    const PositionSignature& signature
) const {
    const auto indexed = history_.state_visit_index.find(signature);
    if (indexed == history_.state_visit_index.end()) {
        return 0;
    }

    const auto& visit = history_.state_visits[indexed->second];
    if (history_.current_round > visit.last_seen_round
        && history_.current_round - visit.last_seen_round > history_.state_window_rounds) return 0;
    return visit.visits;
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

void AntiLoopEngine::record_mask_diagnostics(
    const MaskDiagnostics& diagnostics
) {
    auto& total = history_.metrics.mask;
    total.board_move_candidates += diagnostics.board_move_candidates;
    total.board_move_valid += diagnostics.board_move_valid;
    total.board_move_blocked_anti_loop += diagnostics.board_move_blocked_anti_loop;
    total.board_move_blocked_seen_state += diagnostics.board_move_blocked_seen_state;
    total.bench_move_candidates += diagnostics.bench_move_candidates;
    total.bench_move_valid += diagnostics.bench_move_valid;
    total.bench_move_blocked_anti_loop += diagnostics.bench_move_blocked_anti_loop;
    total.bench_move_blocked_seen_state += diagnostics.bench_move_blocked_seen_state;
    total.blocked_reverse += diagnostics.blocked_reverse;
    total.blocked_oscillation += diagnostics.blocked_oscillation;
    total.blocked_explicit += diagnostics.blocked_explicit;
    total.blocked_bench_board_loop += diagnostics.blocked_bench_board_loop;
    total.blocked_cycle += diagnostics.blocked_cycle;
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