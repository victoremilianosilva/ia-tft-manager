```cmake
cmake_minimum_required(VERSION 3.20)

project(tft_combat_engine
    VERSION 0.1.0
    LANGUAGES CXX
)

# =========================================================
# Configuração global
# =========================================================

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY
    "${CMAKE_BINARY_DIR}/bin"
)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY
    "${CMAKE_BINARY_DIR}/bin"
)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY
    "${CMAKE_BINARY_DIR}/lib"
)

# Diretórios principais de includes.
set(TFT_INCLUDE_DIR
    "${CMAKE_CURRENT_SOURCE_DIR}/include"
)

set(TFT_COMBAT_INCLUDE_DIR
    "${TFT_INCLUDE_DIR}/combat"
)

set(TFT_DECISION_INCLUDE_DIR
    "${TFT_INCLUDE_DIR}/decision"
)

set(TFT_LOBBY_INCLUDE_DIR
    "${TFT_INCLUDE_DIR}/lobby"
)

# =========================================================
# Python e pybind11
# =========================================================

find_package(Python REQUIRED COMPONENTS
    Interpreter
    Development
)

execute_process(
    COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
    OUTPUT_VARIABLE PYBIND11_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE PYBIND11_RESULT
)

if(NOT PYBIND11_RESULT EQUAL 0)
    message(FATAL_ERROR
        "Nao foi possivel localizar pybind11 no Python selecionado.\n"
        "Instale com: ${Python_EXECUTABLE} -m pip install pybind11"
    )
endif()

find_package(pybind11 CONFIG REQUIRED
    PATHS "${PYBIND11_CMAKE_DIR}"
    NO_DEFAULT_PATH
)

message(STATUS "Python: ${Python_EXECUTABLE}")
message(STATUS "pybind11: ${PYBIND11_CMAKE_DIR}")

# =========================================================
# Função auxiliar para configurar módulos Python
# =========================================================

function(configure_tft_module target)
    target_compile_features(
        ${target}
        PRIVATE
            cxx_std_20
    )

    # Os módulos usam includes no formato:
    #   decision/DecisionEngine.hpp
    #   lobby/TftEngine.hpp
    #   CombatEngine.hpp (no módulo de combate)
    target_include_directories(
        ${target}
        PRIVATE
            "${TFT_INCLUDE_DIR}"
    )

    if(MSVC)
        target_compile_options(
            ${target}
            PRIVATE
                /W4
        )
    else()
        target_compile_options(
            ${target}
            PRIVATE
                -Wall
                -Wextra
                -Wpedantic
        )
    endif()
endfunction()

# =========================================================
# Módulo: combate
#
# Estrutura:
#   src/combat/CombatEngine.cpp
#   bindings/combat_engine_bindings.cpp
#   include/combat/*.hpp
# =========================================================

pybind11_add_module(
    combat_engine
    src/combat/CombatEngine.cpp
    bindings/combat_engine_bindings.cpp
)

configure_tft_module(combat_engine)

# CombatEngine.cpp e combat_engine_bindings.cpp usam includes
# sem o prefixo "combat/", como "CombatEngine.hpp".
target_include_directories(
    combat_engine
    PRIVATE
        "${TFT_COMBAT_INCLUDE_DIR}"
)

# =========================================================
# Módulo: decisões
#
# Estrutura:
#   src/decision/*.cpp
#   include/decision/*.hpp
# =========================================================

pybind11_add_module(
    decision_engine
    src/decision/DecisionEngine.cpp
    src/decision/AntiLoopEngine.cpp
    src/decision/MoveValidator.cpp
    src/decision/ActionMaskEngine.cpp
    src/decision/decision_bindings.cpp
)

configure_tft_module(decision_engine)

# Os arquivos usam includes com prefixo "decision/".
# O diretório include/ é suficiente para esses caminhos.
# include/decision também é adicionado para compatibilidade
# com arquivos que incluam headers diretamente pelo nome.
target_include_directories(
    decision_engine
    PRIVATE
        "${TFT_DECISION_INCLUDE_DIR}"
)

# =========================================================
# Módulo: lobby completa
#
# A API está declarada em:
#   include/lobby/TftEngine.hpp
#
# O módulo só será criado quando a implementação existir.
# Isso permite compilar e testar combate/decisões enquanto
# src/lobby/TftEngine.cpp ainda está pendente.
# =========================================================

set(TFT_LOBBY_SOURCE
    "${CMAKE_CURRENT_SOURCE_DIR}/src/lobby/TftEngine.cpp"
)

set(TFT_LOBBY_BINDINGS
    "${CMAKE_CURRENT_SOURCE_DIR}/bindings/tft_engine_bindings.cpp"
)

if(EXISTS "${TFT_LOBBY_SOURCE}")
    pybind11_add_module(
        tft_engine
        src/lobby/TftEngine.cpp
        bindings/tft_engine_bindings.cpp
    )

    configure_tft_module(tft_engine)

    target_include_directories(
        tft_engine
        PRIVATE
            "${TFT_LOBBY_INCLUDE_DIR}"
            "${TFT_COMBAT_INCLUDE_DIR}"
            "${TFT_DECISION_INCLUDE_DIR}"
    )

    message(STATUS "Modulo tft_engine habilitado.")
else()
    message(WARNING
        "Modulo tft_engine ainda desabilitado: "
        "src/lobby/TftEngine.cpp nao existe. "
        "Implemente a API declarada em include/lobby/TftEngine.hpp."
    )
endif()

# =========================================================
# Testes nativos
# =========================================================

include(CTest)

if(BUILD_TESTING)

    # -----------------------------------------------------
    # Contrato de erros
    # -----------------------------------------------------

    add_executable(
        test_decision_error
        tests/test_decision_error.cpp
    )

    configure_tft_module(test_decision_error)

    add_test(
        NAME decision_error_contract
        COMMAND test_decision_error
    )

    # -----------------------------------------------------
    # Validador de movimentos
    # -----------------------------------------------------

    add_executable(
        test_move_validator
        tests/test_move_validator.cpp
        src/decision/MoveValidator.cpp
    )

    configure_tft_module(test_move_validator)

    target_include_directories(
        test_move_validator
        PRIVATE
            "${TFT_DECISION_INCLUDE_DIR}"
    )

    add_test(
        NAME move_validator
        COMMAND test_move_validator
    )

    # -----------------------------------------------------
    # Anti-loop
    # -----------------------------------------------------

    add_executable(
        test_anti_loop_engine
        tests/test_anti_loop_engine.cpp
        src/decision/AntiLoopEngine.cpp
    )

    configure_tft_module(test_anti_loop_engine)

    target_include_directories(
        test_anti_loop_engine
        PRIVATE
            "${TFT_DECISION_INCLUDE_DIR}"
    )

    add_test(
        NAME anti_loop_engine
        COMMAND test_anti_loop_engine
    )

    # -----------------------------------------------------
    # Máscaras de ações
    # -----------------------------------------------------

    add_executable(
        test_action_mask_engine
        tests/test_action_mask_engine.cpp
        src/decision/ActionMaskEngine.cpp
        src/decision/MoveValidator.cpp
        src/decision/AntiLoopEngine.cpp
    )

    configure_tft_module(test_action_mask_engine)

    target_include_directories(
        test_action_mask_engine
        PRIVATE
            "${TFT_DECISION_INCLUDE_DIR}"
    )

    add_test(
        NAME action_mask_engine
        COMMAND test_action_mask_engine
    )

    # -----------------------------------------------------
    # Importação dos módulos Python
    # -----------------------------------------------------

    add_test(
        NAME combat_engine_import
        COMMAND
            "${Python_EXECUTABLE}"
            -c
            "import combat_engine; print(combat_engine.__doc__)"
    )

    set_tests_properties(
        combat_engine_import
        PROPERTIES
            ENVIRONMENT
                "PYTHONPATH=$<TARGET_FILE_DIR:combat_engine>"
    )

    add_test(
        NAME decision_engine_import
        COMMAND
            "${Python_EXECUTABLE}"
            -c
            "import decision_engine; print(decision_engine.__doc__)"
    )

    set_tests_properties(
        decision_engine_import
        PROPERTIES
            ENVIRONMENT
                "PYTHONPATH=$<TARGET_FILE_DIR:decision_engine>"
    )

    # O teste da lobby só existe quando seu módulo é criado.
    if(TARGET tft_engine)
        add_test(
            NAME tft_engine_import
            COMMAND
                "${Python_EXECUTABLE}"
                -c
                "import tft_engine; print(tft_engine.__doc__)"
        )

        set_tests_properties(
            tft_engine_import
            PROPERTIES
                ENVIRONMENT
                    "PYTHONPATH=$<TARGET_FILE_DIR:tft_engine>"
        )
    endif()

endif()
```