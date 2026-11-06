[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$ReferenceCheckpoint,
    [Parameter(Mandatory = $true)][string]$CandidateCheckpoint,
    [Parameter(Mandatory = $true)][string]$Replay,
    [Parameter(Mandatory = $true)][string]$Coverage,
    [string]$OutputDirectory = "ppo_protection\evaluations",
    [int]$SeedStart = 20270101,
    [int]$SeedCount = 50,
    [int]$MinSeeds = 50,
    [int]$MaxSteps = 2500
)
$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot
function Resolve-RepoPath([string]$Path) {
    if ([System.IO.Path]::IsPathRooted($Path)) { return [System.IO.Path]::GetFullPath($Path) }
    return [System.IO.Path]::GetFullPath((Join-Path $repoRoot $Path))
}
$reference = Resolve-RepoPath $ReferenceCheckpoint
$candidate = Resolve-RepoPath $CandidateCheckpoint
$replayPath = Resolve-RepoPath $Replay
$coveragePath = Resolve-RepoPath $Coverage
$outDir = Resolve-RepoPath $OutputDirectory
foreach ($path in @($reference, $candidate, $replayPath, $coveragePath)) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Arquivo obrigatório não encontrado: $path" }
}
if ($SeedCount -lt 2 -or $MinSeeds -lt 2 -or $MaxSteps -lt 1) { throw "SeedCount/MinSeeds/MaxSteps inválidos." }
$python = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if (-not $cmd) { throw "Python não encontrado." }
    $python = $cmd.Source
}
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$paired = Join-Path $outDir "paired_regression_$stamp.jsonl"
$review = Join-Path $outDir "regression_review_$stamp.json"
$seeds = @(); for ($i = 0; $i -lt $SeedCount; $i++) { $seeds += ($SeedStart + $i) }
Write-Host "[1/2] Avaliação pareada de partidas completas ($SeedCount seeds)..." -ForegroundColor Cyan
& $python "economy_finetuning/paired_evaluator.py" --original $reference --finetuned $candidate --seeds ($seeds -join ",") --max-steps $MaxSteps --output $paired
if ($LASTEXITCODE -ne 0) { throw "Avaliação pareada falhou." }
Write-Host "[2/2] Portão de regressão e retenção dos dez cenários..." -ForegroundColor Cyan
& $python "ppo_protection/regression_gate.py" --paired $paired --checkpoint $candidate --replay $replayPath --coverage $coveragePath --output $review --min-seeds $MinSeeds
$gateExit = $LASTEXITCODE
Write-Host "Resultados pareados: $paired"
Write-Host "Revisão: $review"
if ($gateExit -ne 0) {
    Write-Host "CHECKPOINT BLOQUEADO: regressão ou cobertura insuficiente. Não promova." -ForegroundColor Red
    exit $gateExit
}
Write-Host "CHECKPOINT ELEGÍVEL PARA REVISÃO HUMANA. Nenhuma promoção automática foi feita." -ForegroundColor Green
