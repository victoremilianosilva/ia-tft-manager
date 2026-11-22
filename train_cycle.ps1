param(
    [string]$OutputRoot = "",
    [string]$Seeds = "11,12,13",
    [int]$Updates = 160,
    [int]$Lobbies = 4,
    [int]$RolloutSteps = 128,
    [int]$BatchSize = 64,
    [int]$PpoEpochs = 4
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    $python = $venvPython
}
else {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if (-not $pythonCommand) {
        throw "Python não encontrado. Crie/ative o ambiente virtual do projeto."
    }
    $python = $pythonCommand.Source
}

if ([string]::IsNullOrWhiteSpace($OutputRoot)) {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $OutputRoot = Join-Path $PSScriptRoot "training_runs\native_battery_$timestamp"
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "     TFT AI - BATERIA PPO NATIVA" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Seeds:          $Seeds"
Write-Host "Updates/seed:   $Updates"
Write-Host "Lobbies:        $Lobbies"
Write-Host "Rollout:        $RolloutSteps"
Write-Host "Batch size:     $BatchSize"
Write-Host "Épocas PPO:     $PpoEpochs"
Write-Host "Saída:          $OutputRoot"
Write-Host ""

$logDirectory = Join-Path $PSScriptRoot "logs\training"
New-Item -ItemType Directory -Force -Path $logDirectory | Out-Null
$logFile = Join-Path $logDirectory ("native_battery_{0}.log" -f (Get-Date -Format "yyyyMMdd_HHmmss"))

Start-Transcript -Path $logFile -Force | Out-Null
try {
    & $python scripts/run_training_battery.py `
        --output-root $OutputRoot `
        --seeds $Seeds `
        --updates $Updates `
        --lobbies $Lobbies `
        --rollout-steps $RolloutSteps `
        --batch-size $BatchSize `
        --ppo-epochs $PpoEpochs
    $trainingExitCode = $LASTEXITCODE
}
finally {
    Stop-Transcript | Out-Null
}

if ($trainingExitCode -ne 0) {
    Write-Host "BATERIA DE TREINAMENTO FALHOU (código $trainingExitCode)." -ForegroundColor Red
    Write-Host "Consulte: $logFile"
    exit $trainingExitCode
}

Write-Host "BATERIA FINALIZADA." -ForegroundColor Green
Write-Host "Manifesto: $(Join-Path $OutputRoot 'battery_manifest.json')"
Write-Host "Log:       $logFile"
