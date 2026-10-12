
cmake_minimum_required(VERSION 3.20)

project(tft_combat_engine
    VERSION 0.1.0
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY
    ${CMAKE_BINARY_DIR}/bin
)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY
    ${CMAKE_BINARY_DIR}/bin
)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY
    ${CMAKE_BINARY_DIR}/lib
)

# Python do ambiente ativo
find_package(Python REQUIRED COMPONENTS
    Interpreter
    Development
)

# pybind11 instalado no Python ativo
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
    OUTPUT_VARIABLE PYBIND11_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE PYBIND11_RESULT
)

if(NOT PYBIND11_RESULT EQUAL 0)
    message(FATAL_ERROR
        "Nao foi possivel localizar o pybind11 no Python selecionado."
    )
endif()

find_package(pybind11 CONFIG REQUIRED
    PATHS "${PYBIND11_CMAKE_DIR}"
    NO_DEFAULT_PATH
)

# =========================================================
# Modulo existente: combate
# =========================================================

pybind11_add_module(
    combat_engine
    src/CombatEngine.cpp
    src/bindings.cpp
)

target_include_directories(
    combat_engine
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# =========================================================
# Modulo novo: decisoes
# =========================================================

pybind11_add_module(
    decision_engine
    src/decision/DecisionEngine.cpp
    src/decision/decision_bindings.cpp
)

target_include_directories(
    decision_engine
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)


# ============================================================
# Testes nativos automatizados
# ============================================================

include(CTest)

if(BUILD_TESTING)
    add_executable(
        test_decision_error
        tests/test_decision_error.cpp
    )

    target_include_directories(
        test_decision_error
        PRIVATE
            ${CMAKE_CURRENT_SOURCE_DIR}/include
    )

    target_compile_features(
        test_decision_error
        PRIVATE
            cxx_std_20
    )

    add_test(
        NAME decision_error_contract
        COMMAND test_decision_error
    )

    # Confirma que o módulo Python pode ser importado
    # pelo mesmo interpretador selecionado no CMake.
    add_test(
        NAME decision_engine_import
        COMMAND
            ${Python_EXECUTABLE}
            -c
            "import decision_engine; print(decision_engine.__doc__)"
    )

    set_tests_properties(
        decision_engine_import
        PROPERTIES
            ENVIRONMENT
                "PYTHONPATH=$<TARGET_FILE_DIR:decision_engine>"
    )
endif()
