param(
    [string]$OutputRoot = "",
    [int]$Runs = 3,
    [int]$Updates = 160,
    [int]$Lobbies = 4,
    [int]$RolloutSteps = 128,
    [int]$BatchSize = 64,
    [int]$PpoEpochs = 4
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if ($Runs -le 0) {
    throw "Runs deve ser maior que zero."
}

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

# Generate independent, unpredictable seeds for this battery.
$seedSet = [System.Collections.Generic.HashSet[uint32]]::new()
$rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
try {
    while ($seedSet.Count -lt $Runs) {
        $randomBytes = New-Object byte[] 4
        $rng.GetBytes($randomBytes)
        [void]$seedSet.Add([BitConverter]::ToUInt32($randomBytes, 0))
    }
}
finally {
    $rng.Dispose()
}
$Seeds = (@($seedSet) | ForEach-Object { $_ }) -join ","

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "     TFT AI - BATERIA PPO NATIVA" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Execuções:      $Runs"
Write-Host "Seeds geradas:  $Seeds"
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

$trainingExitCode = 1
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
