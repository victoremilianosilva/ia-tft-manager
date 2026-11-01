# ============================================================
# TFT AI - CICLO PADRAO DE TREINAMENTO PPO
# Execute uma vez apos cada modificacao que deva ser aprendida.
# O checkpoint e preservado entre ciclos compativeis.
# ============================================================

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# ------------------------------------------------------------
# CONFIGURACAO DO CICLO
# ------------------------------------------------------------

# Um ciclo por modificacao. O horizonte do scheduler cobre 4 ciclos.
$env:TFT_TOTAL_UPDATES = "300"
$env:TFT_PPO_LR = "0.0002"
$env:TFT_PPO_MIN_LR = "0.00005"
$env:TFT_PPO_LR_SCHEDULE_UPDATES = "1200"

# Adam
$env:TFT_PPO_ADAM_EPS = "0.00001"
$env:TFT_PPO_ADAM_BETA1 = "0.9"
$env:TFT_PPO_ADAM_BETA2 = "0.999"
$env:TFT_PPO_WEIGHT_DECAY = "0.0"

# PPO
$env:TFT_PPO_CLIP_COEF = "0.2"
$env:TFT_PPO_VF_COEF = "0.5"
$env:TFT_PPO_MAX_GRAD_NORM = "0.5"
$env:TFT_PPO_TARGET_KL = "0.02"

# Entropia: exploracao gradual, sem queda abrupta entre ciclos
$env:TFT_PPO_ENT_COEF = "0.015"
$env:TFT_PPO_ENT_COEF_FINAL = "0.005"
$env:TFT_PPO_ENT_DECAY_RATE = "2.0"
$env:TFT_PPO_ENT_SCHEDULE_UPDATES = "1200"

# Coleta e otimizacao
$env:TFT_NUM_LOBBIES = "4"
$env:TFT_ROLLOUT_STEPS = "128"
$env:TFT_PPO_BATCH_SIZE = "64"
$env:TFT_PPO_EPOCHS = "4"

# Retorno e estimativa de vantagem
$env:TFT_PPO_GAMMA = "0.99"
$env:TFT_PPO_GAE_LAMBDA = "0.95"

# Checkpoint persistente: trainer restaura este arquivo se existir.
$env:TFT_CHECKPOINT_PATH = "tft_checkpoint.pt"

# ------------------------------------------------------------
# VALIDACOES PREVIAS
# ------------------------------------------------------------

if (-not (Test-Path ".\trainer.py")) {
    throw "trainer.py nao encontrado. Execute este script na raiz do repositorio."
}

$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    $python = $venvPython
}
else {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if (-not $pythonCommand) {
        throw "Python nao encontrado. Crie/ative o ambiente virtual do projeto."
    }
    $python = $pythonCommand.Source
}

$logDirectory = Join-Path $PSScriptRoot "logs\training"
New-Item -ItemType Directory -Force -Path $logDirectory | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logFile = Join-Path $logDirectory "training_$timestamp.log"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "          TFT AI - TREINAMENTO PPO" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Ciclo:          300 updates"
Write-Host "Lobbies:        4"
Write-Host "Rollout:        128"
Write-Host "Batch size:     64"
Write-Host "Epocas PPO:     4"
Write-Host "Learning rate:  0.0002 -> 0.00005"
Write-Host "Scheduler:      1200 updates (4 ciclos)"
Write-Host "Target KL:      0.02"
Write-Host "Checkpoint:     $env:TFT_CHECKPOINT_PATH"
Write-Host "Log:            $logFile"
Write-Host ""

# Start-Transcript registra a saida sem colocar Tee-Object no pipeline
# do processo Python, preservando a renderizacao dinamica do Rich.
Start-Transcript -Path $logFile -Force | Out-Null
try {
    & $python -u trainer.py
    $trainingExitCode = $LASTEXITCODE
}
finally {
    Stop-Transcript | Out-Null
}

Write-Host ""
if ($trainingExitCode -ne 0) {
    Write-Host "TREINAMENTO FALHOU (codigo $trainingExitCode)." -ForegroundColor Red
    Write-Host "Consulte: $logFile"
    exit $trainingExitCode
}

Write-Host "TREINAMENTO FINALIZADO." -ForegroundColor Green
Write-Host "Log:        $logFile"
Write-Host "Checkpoint: $env:TFT_CHECKPOINT_PATH"
