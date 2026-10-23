#!/usr/bin/env python3
"""Unified TFT evaluation runner that writes one consolidated Markdown report.

Example:
  python scripts/evaluate_all.py --checkpoint checkpoints/latest.pt --seeds 11,12,13
  python scripts/evaluate_all.py --checkpoint checkpoints/latest.pt --baseline checkpoints/old.pt --candidate checkpoints/new.pt --matches 20 --ablation

Raw evidence is retained under reports/evaluation_data/.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "reports" / "evaluation_data"
DEFAULT_REPORT = ROOT / "reports" / "evaluation_report.md"


def run_step(name: str, command: list[str]) -> dict[str, Any]:
    print(f"\n=== {name} ===", flush=True)
    print("> " + " ".join(command), flush=True)
    result = subprocess.run(command, cwd=ROOT, check=False)
    return {"name": name, "returncode": result.returncode, "ok": result.returncode == 0}


def read_json(path: Path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else None
    except (OSError, json.JSONDecodeError):
        return None


def read_jsonl(path: Path):
    rows, errors = [], 0
    if not path.exists():
        return rows, errors
    with path.open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                value = json.loads(line)
                if isinstance(value, dict):
                    rows.append(value)
                else:
                    errors += 1
            except json.JSONDecodeError:
                errors += 1
    return rows, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True, type=Path)
    parser.add_argument("--seeds", default="20261022,20261023")
    parser.add_argument("--max-steps", type=int, default=300)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--matches", type=int, default=20)
    parser.add_argument("--ablation", action="store_true")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    def rooted(path: Path | None) -> Path | None:
        if path is None:
            return None
        return path if path.is_absolute() else ROOT / path

    checkpoint, baseline, candidate = rooted(args.checkpoint), rooted(args.baseline), rooted(args.candidate)
    if not checkpoint.is_file():
        parser.error(f"Checkpoint não encontrado: {checkpoint}")
    if args.max_steps < 1 or args.matches < 1:
        parser.error("--max-steps e --matches precisam ser positivos")
    if bool(baseline) != bool(candidate):
        parser.error("--baseline e --candidate devem ser informados juntos")
    if baseline and (not baseline.is_file() or not candidate.is_file()):
        parser.error("Os checkpoints --baseline e --candidate precisam existir.")
    seeds = ",".join(x.strip() for x in args.seeds.split(",") if x.strip())
    if not seeds:
        parser.error("--seeds precisa conter pelo menos um inteiro.")

    DATA.mkdir(parents=True, exist_ok=True)
    py = sys.executable
    strategic_base = DATA / "strategic_policy.jsonl"
    strategic_dir = DATA / "strategic_policy"
    native_path = DATA / "native_ppo_loop_audit.jsonl"
    analysis_dir = DATA / "strategic_analysis"
    cycles_path = DATA / "strategic_cycle_validation.json"
    steps = []

    def execute(name, script, extra):
        command = [py, str(SCRIPTS / script), *[str(x) for x in extra]]
        result = run_step(name, command)
        steps.append(result)
        if not result["ok"]:
            raise RuntimeError(f"{name} falhou (exit code {result['returncode']}).")

    try:
        execute("Auditoria estratégica por jogador", "audit_strategic_policy.py", [
            "--checkpoint", checkpoint, "--seeds", seeds, "--max-steps", args.max_steps,
            "--output", strategic_base])
        execute("Auditoria nativa PPO/máscara/loops", "audit_native_ppo_loops.py", [
            "--checkpoint", checkpoint, "--seeds", seeds, "--max-steps", args.max_steps,
            "--output", native_path])
        execute("Análise de ações, recompensas e máscaras", "analyze_strategic_policy.py", [
            "--input-dir", strategic_dir, "--out-dir", analysis_dir])
        execute("Validação de ciclos e assinaturas de estado", "validate_strategic_cycles.py", [
            "--input-dir", strategic_dir, "--seeds", seeds, "--out", cycles_path])
        if baseline and candidate:
            execute("Comparação head-to-head", "evaluate_checkpoints.py", [
                "--baseline", baseline, "--candidate", candidate, "--matches", args.matches,
                "--max-steps", args.max_steps, "--output", DATA / "head_to_head.csv",
                "--json-output", DATA / "head_to_head_summary.json"])
        if args.ablation:
            execute("Ablação dos controles de composição", "evaluate_composition_ablation.py", [
                "--checkpoint", checkpoint, "--matches", args.matches,
                "--max-steps", args.max_steps, "--output", DATA / "composition_ablation.json"])
    except RuntimeError as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1

    lines = [
        "# Relatório unificado de avaliação da IA TFT", "",
        f"- Gerado (UTC): {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Checkpoint: **{checkpoint}**", f"- Seeds: **{seeds}**",
        f"- Limite de steps por partida: **{args.max_steps}**", "",
        "> Alertas e padrões de ação são evidências para investigação; não provam, isoladamente, que outra ação seria melhor.",
        "", "## Resultado das etapas", "", "| Etapa | Status | Exit code |", "|---|---|---:|"
    ]
    for step in steps:
        lines.append(f"| {step['name']} | {'OK' if step['ok'] else 'FALHOU'} | {step['returncode']} |")

    lines += ["", "## 1. Auditoria estratégica", ""]
    strategic_md = analysis_dir / "strategic_audit.md"
    lines.append(strategic_md.read_text(encoding="utf-8").strip()
                  if strategic_md.exists() else "Relatório estratégico não encontrado.")

    lines += ["", "## 2. Auditoria nativa: ações, máscaras e loops", ""]
    native_rows, malformed = read_jsonl(native_path)
    loops = [r for r in native_rows if r.get("loop_detected") or r.get("returned_to_previous_state")]
    blocked = sum(1 for r in native_rows if r.get("execution_effect") in ("blocked", "no_effect"))
    action_counts = Counter(str(r.get("action_name", r.get("action_type", "unknown"))) for r in native_rows)
    lines += [
        f"- Steps registrados: **{len(native_rows)}**",
        f"- Linhas JSONL inválidas: **{malformed}**",
        f"- Loops/retornos de estado sinalizados: **{len(loops)}**",
        f"- Execuções bloqueadas/sem efeito (quando identificadas): **{blocked}**",
        f"- Contagem de ações disponível no schema: **{dict(action_counts) if action_counts else 'não disponível'}**",
        f"- Evidência bruta: {native_path.relative_to(ROOT)}",
    ]
    for row in loops[:30]:
        evidence = {k: row.get(k) for k in ("seed", "step", "player_id", "action", "loop_detected",
                                             "returned_to_previous_state", "previous_step") if k in row}
        lines.append("- **Loop/retorno sinalizado:** " + json.dumps(evidence, ensure_ascii=False))

    lines += ["", "## 3. Validação de ciclos e estados", ""]
    cycles = read_json(cycles_path)
    if cycles is None:
        lines.append("Resultado de validação ausente ou JSON inválido.")
    else:
        lines += [
            f"- Resultado: **{'PASSOU' if cycles.get('ok') else 'ATENÇÃO'}**",
            f"- Registros: {cycles.get('records', 'n/d')}",
            f"- Seeds observados: {cycles.get('observed_seeds', [])}",
            f"- Seeds ausentes: {cycles.get('missing_seeds', [])}",
            f"- Divergências de assinatura: {len(cycles.get('signature_mismatches', []))}",
            f"- Conflitos de identidade: {len(cycles.get('identity_conflicts', []))}",
            f"- UUIDs duplicados: {len(cycles.get('duplicate_uuids', []))}",
            f"- Erros de leitura: {len(cycles.get('errors', []))}",
        ]
        for issue in cycles.get("signature_mismatches", [])[:20]:
            lines.append("- Divergência: " + json.dumps(issue, ensure_ascii=False))

    if baseline and candidate:
        lines += ["", "## 4. Comparação head-to-head", ""]
        summary = read_json(DATA / "head_to_head_summary.json")
        if summary is None:
            lines.append("Resumo head-to-head ausente.")
        else:
            lines += [f"- Baseline: **{baseline}**", f"- Candidate: **{candidate}**",
                      f"- Partidas: **{summary.get('matches', args.matches)}**",
                      f"- Métricas completas: {DATA.relative_to(ROOT) / 'head_to_head_summary.json'}"]
            for key, value in summary.items():
                if key not in {"checkpoints", "paired_matches"}:
                    lines.append(f"- {key}: {json.dumps(value, ensure_ascii=False)}")

    if args.ablation:
        lines += ["", "## 5. Ablação dos controles de composição", ""]
        ablation = read_json(DATA / "composition_ablation.json")
        if ablation is None:
            lines.append("Resultado da ablação ausente.")
        else:
            lines += [f"- Checkpoint migrado: {ablation.get('checkpoint_migrated', 'n/d')}",
                      f"- Partidas por condição: {ablation.get('matches_per_condition', args.matches)}"]
            for key, value in (ablation.get("conditions") or {}).items():
                lines.append(f"- {key}: {json.dumps(value, ensure_ascii=False)}")

    lines += [
        "", "## Limitações", "",
        "- Use um checkpoint compatível com as dimensões da policy e com a engine C++ compilada.",
        "- Ciclo confirmado requer retorno ao mesmo estado reconstruído; repetição de ação é apenas indício.",
        "- Ouro e recompensa são sinais parciais: devem ser interpretados junto de upgrades, sinergias, qualidade/posicionamento do board e colocação final.",
        "- Head-to-head e ablação só rodam quando as opções correspondentes são informadas.",
        "", "## Arquivos de evidência", "",
        f"- Auditoria estratégica por jogador: {strategic_dir.relative_to(ROOT)}",
        f"- Resumo estratégico JSON: {(analysis_dir / 'strategic_audit.json').relative_to(ROOT)}",
        f"- Auditoria nativa JSONL: {native_path.relative_to(ROOT)}",
        f"- Validação de ciclos JSON: {cycles_path.relative_to(ROOT)}",
        ""
    ]
    report_path = rooted(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nRelatório Markdown unificado: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
