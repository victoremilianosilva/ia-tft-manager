[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet(
        "critical_hp_high_gold",
        "late_game_high_gold_underleveled",
        "s4_fast8_lvl6_gold60_hp_ok",
        "s4_fast8_lvl6_gold80",
        "s4_fast8_lvl7_gold60",
        "slowroll_gold_reserve",
        "core_sale_retention",
        "bench_deployment_quality",
        "carry_protection_positioning",
        "movement_no_progress"
    )]
    [string]$Scenario,
    [Parameter(Mandatory = $true)]
    [string]$Evaluation
)
$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot
$python = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    $command = Get-Command python -ErrorAction SilentlyContinue
    if (-not $command) { throw "Python não encontrado." }
    $python = $command.Source
}
& $python -m economy_finetuning.chain_manager approve --scenario $Scenario --evaluation $Evaluation
if ($LASTEXITCODE -ne 0) { throw "A aprovação de $Scenario falhou." }
Write-Host "Cenário $Scenario aprovado. O próximo cenário da cadeia foi liberado." -ForegroundColor Green
