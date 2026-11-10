
#include "decision/DecisionError.hpp"

#include <cassert>
#include <string_view>

using namespace tft::decision;

int main() {
    // Erro padrão: nenhuma falha.
    const DecisionError no_error{};

    assert(!no_error.has_error());
    assert(!static_cast<bool>(no_error));
    assert(no_error.code == DecisionErrorCode::NONE);

    // Erro de entrada inválida.
    const DecisionError invalid_input{
        DecisionErrorCode::INVALID_INPUT,
        "Invalid board index"
    };

    assert(invalid_input.has_error());
    assert(static_cast<bool>(invalid_input));
    assert(
        invalid_input.code == DecisionErrorCode::INVALID_INPUT
    );
    assert(invalid_input.message == "Invalid board index");

    // Todos os códigos devem possuir nomes estáveis.
    assert(decision_error_code_name(DecisionErrorCode::NONE) == "NONE");

    assert(
        decision_error_code_name(DecisionErrorCode::INVALID_INPUT)
        == "INVALID_INPUT"
    );

    assert(
        decision_error_code_name(DecisionErrorCode::INVALID_STATE)
        == "INVALID_STATE"
    );

    assert(
        decision_error_code_name(
            DecisionErrorCode::INVALID_CONFIGURATION
        ) == "INVALID_CONFIGURATION"
    );

    assert(
        decision_error_code_name(
            DecisionErrorCode::DEPENDENCY_FAILURE
        ) == "DEPENDENCY_FAILURE"
    );

    assert(
        decision_error_code_name(DecisionErrorCode::INTERNAL_ERROR)
        == "INTERNAL_ERROR"
    );

    // Código desconhecido: não deve causar comportamento indefinido.
    const auto unknown =
        static_cast<DecisionErrorCode>(255);

    assert(
        decision_error_code_name(unknown) == "UNKNOWN_ERROR"
    );

    return 0;
}
