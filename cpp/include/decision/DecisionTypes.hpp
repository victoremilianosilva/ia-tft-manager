
#pragma once

#include <cstdint>
#include <optional>

namespace tft::decision {

// ============================================================
// Ações da política PPO
//
// Os valores numéricos devem permanecer compatíveis com
// o contrato de ações já utilizado pelo ambiente Python.
// ============================================================

enum class ActionType : std::uint8_t {
    BUY        = 0,
    REROLL     = 1,
    BUY_XP     = 2,
    MOVE_BENCH = 3,
    MOVE_BOARD = 4,
    SELL       = 5,
    PASS       = 6,
    EQUIP_FROM_INVENTORY = 7,
    CRAFT_AND_EQUIP = 8
};

// ============================================================
// Categorias de movimento usadas na validação e no AntiLoop
// ============================================================

enum class MoveType : std::uint8_t {
    BENCH_TO_BOARD = 0,
    BOARD_MOVE     = 1,
    BOARD_SWAP     = 2
};

// ============================================================
// Motivos de bloqueio
// ============================================================

enum class BlockReason : std::uint8_t {
    NONE             = 0,
    EXPLICIT         = 1,
    REVERSE          = 2,
    OSCILLATION      = 3,
    BENCH_BOARD_LOOP = 4,
    CYCLE            = 5
};

// ============================================================
// Resultado geral da validação
// ============================================================

enum class ValidationStatus : std::uint8_t {
    VALID   = 0,
    INVALID = 1,
    ERROR   = 2
};

// ============================================================
// Índices dos espaços do jogo
//
// Os aliases compactos são usados somente depois que o índice
// bruto foi validado.
// ============================================================

using RawIndex   = std::int32_t;
using BoardIndex = std::uint8_t;
using BenchIndex = std::uint8_t;
using ShopIndex  = std::uint8_t;

// ============================================================
// Valores das máscaras
// ============================================================

using MaskValue = std::uint8_t;

inline constexpr MaskValue MASK_DISABLED = 0;
inline constexpr MaskValue MASK_ENABLED  = 1;

// ============================================================
// Dimensões conhecidas do ambiente
// ============================================================

inline constexpr BoardIndex BOARD_SIZE = 28;
inline constexpr BenchIndex BENCH_SIZE = 9;
inline constexpr ShopIndex SHOP_SIZE   = 5;

inline constexpr std::uint8_t ACTION_TYPE_COUNT = 9;

// ============================================================
// Validação de índices brutos
//
// Retorna std::nullopt para índices fora dos limites.
// Não converta para BoardIndex, BenchIndex ou ShopIndex antes
// de validar: esses tipos são unsigned e podem perder valores
// negativos durante uma conversão.
// ============================================================

[[nodiscard]] constexpr std::optional<BoardIndex>
to_board_index(RawIndex index) noexcept {
    if (index < 0 || index >= BOARD_SIZE) {
        return std::nullopt;
    }

    return static_cast<BoardIndex>(index);
}

[[nodiscard]] constexpr std::optional<BenchIndex>
to_bench_index(RawIndex index) noexcept {
    if (index < 0 || index >= BENCH_SIZE) {
        return std::nullopt;
    }

    return static_cast<BenchIndex>(index);
}

[[nodiscard]] constexpr std::optional<ShopIndex>
to_shop_index(RawIndex index) noexcept {
    if (index < 0 || index >= SHOP_SIZE) {
        return std::nullopt;
    }

    return static_cast<ShopIndex>(index);
}

// ============================================================
// Validação dos valores de máscara
// ============================================================

[[nodiscard]] constexpr bool
is_valid_mask_value(MaskValue value) noexcept {
    return value == MASK_DISABLED || value == MASK_ENABLED;
}

// ============================================================
// Verificações de compatibilidade em tempo de compilação
// ============================================================

static_assert(static_cast<std::uint8_t>(ActionType::BUY) == 0);
static_assert(static_cast<std::uint8_t>(ActionType::REROLL) == 1);
static_assert(static_cast<std::uint8_t>(ActionType::BUY_XP) == 2);
static_assert(static_cast<std::uint8_t>(ActionType::MOVE_BENCH) == 3);
static_assert(static_cast<std::uint8_t>(ActionType::MOVE_BOARD) == 4);
static_assert(static_cast<std::uint8_t>(ActionType::SELL) == 5);
static_assert(static_cast<std::uint8_t>(ActionType::PASS) == 6);
static_assert(static_cast<std::uint8_t>(ActionType::EQUIP_FROM_INVENTORY) == 7);
static_assert(static_cast<std::uint8_t>(ActionType::CRAFT_AND_EQUIP) == 8);

static_assert(BOARD_SIZE == 28);
static_assert(BENCH_SIZE == 9);
static_assert(SHOP_SIZE == 5);
static_assert(ACTION_TYPE_COUNT == 9);

} // namespace tft::decision
