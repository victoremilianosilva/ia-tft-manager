
$ErrorActionPreference = "Stop"

$Python = ".\.venv\Scripts\python.exe"
$BuildDir = "cpp/build"

if (-not (Test-Path $Python)) {
    throw "Ambiente virtual não encontrado. Crie .venv primeiro."
}

New-Item -ItemType Directory -Force artifacts | Out-Null

Write-Host "`n=== 1/3: CONFIGURANDO E COMPILANDO C++ ===" -ForegroundColor Cyan

cmake -S cpp -B $BuildDir -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=ON
if ($LASTEXITCODE -ne 0) { throw "CMake configure falhou" }

cmake --build $BuildDir --config Release --parallel
if ($LASTEXITCODE -ne 0) { throw "Build C++ falhou" }

Write-Host "`n=== 2/3: TESTES NATIVOS C++ ===" -ForegroundColor Cyan

ctest --test-dir $BuildDir -C Release --output-on-failure 2>&1 |
    Tee-Object -FilePath artifacts/ctest.log

if ($LASTEXITCODE -ne 0) { throw "CTest falhou; consulte artifacts/ctest.log" }

Write-Host "`n=== 3/3: TESTES PYTHON / C++ ===" -ForegroundColor Cyan

$env:PYTHONPATH = "$PWD\cpp\build\bin;$PWD\cpp\build\bin\Release;$PWD"
$env:REQUIRE_CPP_PARITY = "1"

$tests = @(
    "tests/test_combat_engine.py",
    "tests/test_combat_events.py",
    "tests/test_combat_movement.py",
    "tests/test_combat_profile_data.py",
    "tests/test_combat_stats.py",
    "tests/test_combat_timeout.py",
    "tests/test_determinismo_combate_cpp.py",
    "tests/test_empty_team_combat.py",
    "tests/test_integracao_combate_cpp.py",
    "tests/test_lobby_combat_regression.py",
    "tests/test_reward_integration.py",
    "tests/test_round_economy_combat_flow.py",
    "tests/test_tft_engine_api.py",
    "tests/test_lobby_end_to_end.py",
    "tests/test_cross_language_replay.py",
    "tests/test_positioning_parity.py",
    "tests/test_reward_manager_parity.py",
    "tests/test_combat_profile_parity.py",
    "tests/test_synergy_manager_parity.py",
    "tests/test_action_mask_equivalence.py",
    "tests/test_action_mask_integration.py",
    "tests/test_anti_loop_mask_integration.py",
    "tests/test_anti_loop_swap_cycles.py",
    "tests/test_combat_economy_integration.py",
    "tests/test_self_play_economy_progression.py",
    "tests/test_shop_manager_odds.py",
    "tests/test_shared_pool_shop_validation.py",
    "tests/test_upgrade_integration.py",
    "tests/test_engine_backend_selection.py"
)

& $Python -m pytest -q --junitxml=artifacts/cross-language-parity.xml @tests 2>&1 |
    Tee-Object -FilePath artifacts/python-parity.log

if ($LASTEXITCODE -ne 0) {
    throw "Pytest falhou; consulte artifacts/python-parity.log"
}

Write-Host "`nSUCESSO: C++ e suíte Python de paridade passaram." -ForegroundColor Green
Write-Host "Relatórios disponíveis em ./artifacts/"
