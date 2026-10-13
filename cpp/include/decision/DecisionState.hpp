
#pragma once

#include "decision/DecisionTypes.hpp"

#include <array>
#include <cstdint>
#include <optional>
#include <string>

namespace tft::decision {

// Identidade estável para comparação de unidades no histórico.
// Se uuid existir, ele tem prioridade sobre id + star.
// Identidade estável para comparação de unidades no histórico.
// Se uuid existir, ele tem prioridade sobre id + star.
struct UnitIdentity {
    std::optional<std::string> uuid;
    std::optional<std::int64_t> id;
    std::uint8_t star = 1;

    [[nodiscard]] bool has_identity() const noexcept {
        return uuid.has_value() || id.has_value();
    }

    bool operator==(const UnitIdentity& other) const noexcept {
        // Se qualquer uma possuir UUID, compara exclusivamente UUID.
        if (uuid.has_value() || other.uuid.has_value()) {
            return uuid.has_value()
                && other.uuid.has_value()
                && uuid == other.uuid;
        }

        // Sem UUID, compara id + star.
        return id == other.id && star == other.star;
    }
};

// Snapshot mínimo da unidade necessário ao motor de decisões.
// Campos adicionais podem ser incluídos quando uma regra nativa
// realmente precisar deles.
struct UnitSnapshot {
    UnitIdentity identity;

    std::uint8_t cost = 1;
    bool available = true;
};

// Posição ocupada ou vazia, identificada pelo índice do slot.
template <typename TIndex>
struct Position {
    TIndex index = 0;
    bool occupied = false;
};

// Estado de economia usado nas futuras validações.
struct EconomyState {
    std::int32_t gold = 0;
    std::int32_t level = 1;
    std::int32_t current_xp = 0;
    std::int32_t xp_to_next_level = 0;

    std::int32_t reroll_cost = 2;
    std::int32_t xp_purchase_cost = 4;
};

// Estado completo relevante para as decisões de um jogador.
// Slots vazios são representados por std::nullopt.
struct PlayerState {
    std::int64_t player_id = -1;
    bool is_alive = true;

    EconomyState economy;

    std::array<std::optional<UnitSnapshot>, BOARD_SIZE> board{};
    std::array<std::optional<UnitSnapshot>, BENCH_SIZE> bench{};
    std::array<std::optional<UnitSnapshot>, SHOP_SIZE> shop{};

    [[nodiscard]] bool has_free_board_slot() const noexcept {
        for (const auto& unit : board) {
            if (!unit.has_value()) {
                return true;
            }
        }
        return false;
    }

    [[nodiscard]] bool has_free_bench_slot() const noexcept {
        for (const auto& unit : bench) {
            if (!unit.has_value()) {
                return true;
            }
        }
        return false;
    }
};

} // namespace tft::decision
