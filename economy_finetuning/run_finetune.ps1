[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet(
        "s4_fast8_lvl6_gold60_hp_ok",
        "s4_fast8_lvl6_gold80",
        "s4_fast8_lvl7_gold60",
        "late_game_high_gold_underleveled",
        "slowroll_gold_reserve",
        "critical_hp_high_gold"
    )]
    [string]$Scenario,

    [string]$Checkpoint = "tft_checkpoint.pt",
    [int]$Updates = 100,
    [int]$RolloutSteps = 512,
    [int]$BatchSize = 64,
    [int]$PpoEpochs = 2,
    [double]$LearningRate = 0.00001,
    [double]$ClipCoef = 0.10,
    [double]$TargetKl = 0.01,
    [double]$EntropyCoef = 0.002,
    [double]$MaxTypeHeadDrift = 0.02,
    [int]$MinScenarioTransitions = 8,
    [int]$Seed = 20261105
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$checkpointPath = if ([System.IO.Path]::IsPathRooted($Checkpoint)) {
    $Checkpoint
} else {
    Join-Path $repoRoot $Checkpoint
}
if (-not (Test-Path -LiteralPath $checkpointPath -PathType Leaf)) {
    throw "Checkpoint original não encontrado: $checkpointPath"
}

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path -LiteralPath $venvPython -PathType Leaf) {
    $python = $venvPython
} else {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if (-not $pythonCommand) {
        throw "Python não encontrado. Crie/ative o ambiente virtual do projeto."
    }
    $python = $pythonCommand.Source
}

if ($Updates -le 0 -or $RolloutSteps -le 0 -or $BatchSize -le 0 -or $PpoEpochs -le 0) {
    throw "Updates, RolloutSteps, BatchSize e PpoEpochs devem ser positivos."
}
if ($LearningRate -le 0 -or $ClipCoef -le 0 -or $ClipCoef -ge 1 -or $TargetKl -le 0) {
    throw "LearningRate, ClipCoef ou TargetKl inválido."
}

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$runName = "${Scenario}_${timestamp}"
$runDirectory = Join-Path $repoRoot "economy_finetuning\runs\$runName"
$outputDirectory = Join-Path $repoRoot "economy_finetuning\checkpoints"
$logDirectory = Join-Path $repoRoot "logs\fine_tuning"
New-Item -ItemType Directory -Force -Path $runDirectory, $outputDirectory, $logDirectory | Out-Null

$outputCheckpoint = Join-Path $outputDirectory "tft_${Scenario}_${timestamp}.pt"
$logFile = Join-Path $logDirectory "finetune_${runName}.log"

$arguments = @(
    "-u", "economy_finetuning/finetune.py",
    "--scenario", $Scenario,
    "--checkpoint", $checkpointPath,
    "--output", $outputCheckpoint,
    "--run-dir", $runDirectory,
    "--updates", "$Updates",
    "--rollout-steps", "$RolloutSteps",
    "--batch-size", "$BatchSize",
    "--ppo-epochs", "$PpoEpochs",
    "--learning-rate", "$LearningRate",
    "--clip-coef", "$ClipCoef",
    "--target-kl", "$TargetKl",
    "--entropy-coef", "$EntropyCoef",
    "--max-type-head-drift", "$MaxTypeHeadDrift",
    "--min-scenario-transitions", "$MinScenarioTransitions",
    "--seed", "$Seed"
)

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "       TFT AI - FINE-TUNING FOCADO PPO" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Cenário:          $Scenario"
Write-Host "Checkpoint base:  $checkpointPath"
Write-Host "Checkpoint novo:  $outputCheckpoint"
Write-Host "Updates:          $Updates"
Write-Host "Lobbies:          1 (8 agentes self-play)"
Write-Host "Rollout:          $RolloutSteps"
Write-Host "Batch size:       $BatchSize"
Write-Host "Épocas PPO:       $PpoEpochs"
Write-Host "Learning rate:    $LearningRate"
Write-Host "Clip:             $ClipCoef"
Write-Host "Target KL:        $TargetKl"
Write-Host "Drift type_head:  $MaxTypeHeadDrift"
Write-Host "Seed:             $Seed"
Write-Host "Run directory:    $runDirectory"
Write-Host "Log:              $logFile"
Write-Host ""

Start-Transcript -Path $logFile -Force | Out-Null
try {
    & $python @arguments
    $trainingExitCode = $LASTEXITCODE
}
finally {
    Stop-Transcript | Out-Null
}

if ($trainingExitCode -ne 0) {
    Write-Host "FINE-TUNING FALHOU (código $trainingExitCode)." -ForegroundColor Red
    Write-Host "Consulte: $logFile"
    exit $trainingExitCode
}

Write-Host ""
Write-Host "FINE-TUNING FINALIZADO." -ForegroundColor Green
Write-Host "Checkpoint: $outputCheckpoint"
Write-Host "Execução:   $runDirectory"
Write-Host "Log:        $logFile"
