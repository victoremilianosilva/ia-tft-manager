
#pragma once

#include <cstdint>
#include <string>
#include <string_view>

namespace tft::decision {

// ============================================================
// Códigos padronizados de erro
//
// INVALID_INPUT: entrada malformada ou índice inválido.
// INVALID_STATE: estado incompatível com a operação.
// INVALID_CONFIGURATION: configuração inconsistente.
// DEPENDENCY_FAILURE: falha em uma dependência.
// INTERNAL_ERROR: falha interna inesperada.
// ============================================================

enum class DecisionErrorCode : std::uint8_t {
    NONE                  = 0,
    INVALID_INPUT         = 1,
    INVALID_STATE         = 2,
    INVALID_CONFIGURATION = 3,
    DEPENDENCY_FAILURE    = 4,
    INTERNAL_ERROR        = 5
};

// ============================================================
// Diagnóstico de uma operação
// ============================================================

struct DecisionError {
    DecisionErrorCode code = DecisionErrorCode::NONE;
    std::string message;

    [[nodiscard]] bool has_error() const noexcept {
        return code != DecisionErrorCode::NONE;
    }

    [[nodiscard]] explicit operator bool() const noexcept {
        return has_error();
    }
};

// ============================================================
// Conversão dos códigos para nomes estáveis
//
// Útil para logs e integração com Python.
// Não utilizar a mensagem como identificador de erro.
// ============================================================

[[nodiscard]] constexpr std::string_view
decision_error_code_name(DecisionErrorCode code) noexcept {
    switch (code) {
        case DecisionErrorCode::NONE:
            return "NONE";

        case DecisionErrorCode::INVALID_INPUT:
            return "INVALID_INPUT";

        case DecisionErrorCode::INVALID_STATE:
            return "INVALID_STATE";

        case DecisionErrorCode::INVALID_CONFIGURATION:
            return "INVALID_CONFIGURATION";

        case DecisionErrorCode::DEPENDENCY_FAILURE:
            return "DEPENDENCY_FAILURE";

        case DecisionErrorCode::INTERNAL_ERROR:
            return "INTERNAL_ERROR";
    }

    return "UNKNOWN_ERROR";
}

// ============================================================
// Compatibilidade dos códigos
// ============================================================

static_assert(
    static_cast<std::uint8_t>(DecisionErrorCode::NONE) == 0
);

static_assert(
    static_cast<std::uint8_t>(DecisionErrorCode::INVALID_INPUT) == 1
);

static_assert(
    static_cast<std::uint8_t>(DecisionErrorCode::INVALID_STATE) == 2
);

static_assert(
    static_cast<std::uint8_t>(
        DecisionErrorCode::INVALID_CONFIGURATION
    ) == 3
);

static_assert(
    static_cast<std::uint8_t>(
        DecisionErrorCode::DEPENDENCY_FAILURE
    ) == 4
);

static_assert(
    static_cast<std::uint8_t>(
        DecisionErrorCode::INTERNAL_ERROR
    ) == 5
);

} // namespace tft::decision
