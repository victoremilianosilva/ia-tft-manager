[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$Run,
    [int]$SeedStart = 20261201,
    [int]$SeedCount = 20,
    [int]$MinSeedsForReview = 20,
    [int]$MaxSteps = 2500,
    [string]$OriginalCheckpoint = "",
    [switch]$OpenViewer
)
$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot
function Resolve-RepoPath([string]$Path) {
    if ([System.IO.Path]::IsPathRooted($Path)) { return [System.IO.Path]::GetFullPath($Path) }
    return [System.IO.Path]::GetFullPath((Join-Path $repoRoot $Path))
}
$runPath = Resolve-RepoPath $Run
if (-not (Test-Path -LiteralPath $runPath -PathType Container)) { throw "Pasta da execução não encontrada: $runPath" }
$logsPath = Join-Path $runPath "logs"
$reportsPath = Join-Path $runPath "reports"
$tracePath = Join-Path $logsPath "decision_trace.jsonl"
$metadataPath = Join-Path $reportsPath "experiment_config.json"
$summaryPath = Join-Path $reportsPath "training_summary.json"
foreach ($required in @($tracePath, $metadataPath, $summaryPath)) {
    if (-not (Test-Path -LiteralPath $required -PathType Leaf)) { throw "Artefato obrigatório ausente: $required" }
}
if ($SeedCount -lt 1 -or $MinSeedsForReview -lt 1 -or $MaxSteps -lt 1) { throw "SeedCount, MinSeedsForReview e MaxSteps devem ser positivos." }
$python = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    $command = Get-Command python -ErrorAction SilentlyContinue
    if (-not $command) { throw "Python não encontrado. Crie o ambiente virtual do projeto." }
    $python = $command.Source
}
$metadata = Get-Content -LiteralPath $metadataPath -Raw | ConvertFrom-Json
$training = Get-Content -LiteralPath $summaryPath -Raw | ConvertFrom-Json
if (-not $metadata.selected_scenario -or $metadata.selected_scenario -ne $training.selected_scenario) { throw "Cenário divergente entre experiment_config.json e training_summary.json." }
if (-not $training.checkpoint_finetuned -or -not (Test-Path -LiteralPath $training.checkpoint_finetuned -PathType Leaf)) { throw "Checkpoint fine-tuned indicado no training_summary.json não foi encontrado: $($training.checkpoint_finetuned)" }
$finetunedPath = [System.IO.Path]::GetFullPath($training.checkpoint_finetuned)
$originalReference = if ([string]::IsNullOrWhiteSpace($OriginalCheckpoint)) { [string]$metadata.checkpoint } else { $OriginalCheckpoint }
$originalPath = Resolve-RepoPath $originalReference
if (-not (Test-Path -LiteralPath $originalPath -PathType Leaf)) { throw "Checkpoint original não encontrado: $originalPath" }
$pairedPath = Join-Path $logsPath "paired_match_results.jsonl"
if (Test-Path -LiteralPath $pairedPath) { throw "O arquivo pareado já existe e não será sobrescrito: $pairedPath" }
$seeds = @()
for ($i = 0; $i -lt $SeedCount; $i++) { $seeds += ($SeedStart + $i) }
$seedArgument = $seeds -join ","
$auditPath = Join-Path $reportsPath ("ECONOMY_FINETUNING_AUDIT_{0}.md" -f $metadata.selected_scenario)
$evaluationPath = Join-Path $reportsPath "evaluation_review.json"
if (Test-Path -LiteralPath $evaluationPath) {
    $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $evaluationPath = Join-Path $reportsPath "evaluation_review_$stamp.json"
}
Write-Host "=== AVALIAÇÃO AUTOMÁTICA DE FINE-TUNING ===" -ForegroundColor Cyan
Write-Host "Cenário: $($metadata.selected_scenario)"
Write-Host "Seeds: $seedArgument"
Write-Host "[1/3] Executando comparação pareada..." -ForegroundColor Cyan
& $python "economy_finetuning/paired_evaluator.py" --original $originalPath --finetuned $finetunedPath --seeds $seedArgument --max-steps $MaxSteps --output $pairedPath
if ($LASTEXITCODE -ne 0) { throw "Comparação pareada falhou. Consulte o erro acima." }
Write-Host "[2/3] Gerando auditoria consolidada..." -ForegroundColor Cyan
& $python "economy_finetuning/audit.py" --trace $tracePath --paired $pairedPath --metadata $metadataPath --summary $summaryPath --output $auditPath
if ($LASTEXITCODE -ne 0) { throw "Geração da auditoria falhou." }
Write-Host "[3/3] Verificando integridade e cobertura..." -ForegroundColor Cyan
$pairedRows = @(Get-Content -LiteralPath $pairedPath | Where-Object { $_.Trim() } | ForEach-Object { $_ | ConvertFrom-Json })
$completed = @($pairedRows | Where-Object { $_.both_completed -eq $true }).Count
$sameInitial = @($pairedRows | Where-Object { $_.same_initial_state -eq $true }).Count
$transitions = [int]$training.selected_scenario_transitions
$checkpointHash = (Get-FileHash -LiteralPath $finetunedPath -Algorithm SHA256).Hash.ToLowerInvariant()
$auditText = Get-Content -LiteralPath $auditPath -Raw
$nonTargetMatch = [regex]::Match($auditText, 'Divergência de ação nesses estados:\s*\*\*\d+\s*\(([\d.]+)%\)\*\*')
$nonTargetRate = $null
if ($nonTargetMatch.Success) { $nonTargetRate = [double]::Parse($nonTargetMatch.Groups[1].Value, [Globalization.CultureInfo]::InvariantCulture) }
$checks = [ordered]@{
    training_has_target_transitions = ($transitions -gt 0)
    paired_seed_count_sufficient = ($pairedRows.Count -ge $MinSeedsForReview)
    all_paired_matches_completed = ($pairedRows.Count -gt 0 -and $completed -eq $pairedRows.Count)
    all_initial_states_match = ($pairedRows.Count -gt 0 -and $sameInitial -eq $pairedRows.Count)
    non_target_divergence_within_triage_limit = ($null -ne $nonTargetRate -and $nonTargetRate -le 5.0)
}
$ready = $true
foreach ($value in $checks.Values) { if (-not $value) { $ready = $false } }
$reviewStatus = if ($ready) { "READY_FOR_HUMAN_REVIEW" } else { "INCONCLUSIVE_OR_INVESTIGATE" }
$evaluation = [ordered]@{
    approved = $false
    review_status = $reviewStatus
    checkpoint_sha256 = $checkpointHash
    summary = [ordered]@{
        scenario = $metadata.selected_scenario
        paired_seeds = $pairedRows.Count
        completed_pairs = $completed
        identical_initial_states = $sameInitial
        selected_scenario_transitions = $transitions
        non_target_divergence_percent = $nonTargetRate
        checks = $checks
        audit_report = $auditPath
        paired_results = $pairedPath
        note = "Pacote de revisão; approved permanece false até decisão humana. Os checks não provam melhoria de desempenho."
    }
}
$evaluationJson = $evaluation | ConvertTo-Json -Depth 8
[System.IO.File]::WriteAllText($evaluationPath, $evaluationJson, (New-Object System.Text.UTF8Encoding($false)))
Write-Host ""
Write-Host "AVALIAÇÃO CONCLUÍDA" -ForegroundColor Green
Write-Host "Status: $reviewStatus"
Write-Host "Auditoria: $auditPath"
Write-Host "Resultados pareados: $pairedPath"
Write-Host "Pacote de revisão: $evaluationPath"
Write-Host "Hash: $checkpointHash"
foreach ($key in $checks.Keys) {
    $mark = if ($checks[$key]) { "OK" } else { "FALHOU" }
    $color = if ($checks[$key]) { "Green" } else { "Yellow" }
    Write-Host (" - {0}: {1}" -f $key, $mark) -ForegroundColor $color
}
Write-Host ""
Write-Host "Nenhum cenário foi aprovado automaticamente. Revise o Markdown e os resultados de desempenho." -ForegroundColor Yellow
Write-Host "Depois da revisão, altere approved para true em: $evaluationPath"
$approvalCommand = '.\economy_finetuning\approve_scenario.ps1 -Scenario ' + $metadata.selected_scenario + ' -Evaluation "' + $evaluationPath + '"'
Write-Host ("E execute: " + $approvalCommand)
if ($OpenViewer) {
    $streamlit = Get-Command streamlit -ErrorAction SilentlyContinue
    if ($streamlit) { & $streamlit.Source run "economy_finetuning/viewer/app.py" }
    else { Write-Warning "Streamlit não encontrado. Instale requirements-viewer.txt para abrir o viewer." }
}
