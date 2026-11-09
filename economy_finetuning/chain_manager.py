"""Sequential fine-tuning chain with explicit human approval between scenarios."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "economy_finetuning" / "chain_state.json"
SCENARIO_ORDER = (
    # Preserve the two already executed fine-tunings and their lineage.
    "critical_hp_high_gold",
    "late_game_high_gold_underleveled",
    # New focused strategy curriculum.
    "econ_gold_reserve",
    "econ_surplus_strong_board",
    "stabilize_weak_board",
    "fast8_strong_board",
    "all_in_emergency",
    "slowroll_winstreak",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {"version": 1, "scenarios": {}}
    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if data.get("version") != 1 or not isinstance(data.get("scenarios"), dict):
        raise RuntimeError(f"Estado da cadeia inválido: {STATE_PATH}")
    return data


def _save(data: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = STATE_PATH.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, STATE_PATH)


def predecessor(scenario: str) -> str | None:
    if scenario not in SCENARIO_ORDER:
        raise ValueError(f"Cenário fora da sequência: {scenario}")
    index = SCENARIO_ORDER.index(scenario)
    return SCENARIO_ORDER[index - 1] if index else None


def check_scenario(
    scenario: str, requested_checkpoint: Path, *, custom_source: bool = False
) -> Path:
    requested_checkpoint = requested_checkpoint.expanduser().resolve()
    if not requested_checkpoint.is_file():
        raise FileNotFoundError(f"Checkpoint de origem não encontrado: {requested_checkpoint}")
    # Explicit custom source is an opt-in branch for this run only.
    if custom_source:
        return requested_checkpoint
    data = _load()
    previous = predecessor(scenario)
    if previous is None:
        return requested_checkpoint.resolve()
    previous_entry = data["scenarios"].get(previous)
    if not previous_entry or previous_entry.get("status") != "approved":
        raise RuntimeError(
            f"Execução bloqueada: {scenario} depende de {previous} aprovado. "
            "Treinar não aprova; execute avaliação pareada e aprove explicitamente."
        )
    approved_path = Path(previous_entry["checkpoint_path"]).resolve()
    if not approved_path.is_file():
        raise RuntimeError(f"Checkpoint aprovado do cenário anterior não existe: {approved_path}")
    actual_hash = sha256_file(approved_path)
    if actual_hash != previous_entry.get("checkpoint_sha256"):
        raise RuntimeError("Checkpoint anterior foi alterado após aprovação; cadeia bloqueada.")
    # For scenarios after the first, the approved predecessor is authoritative.
    # Ignore the user-supplied base path rather than allowing accidental branching.
    return approved_path


def record_training(scenario: str, checkpoint: Path, summary: Path) -> None:
    if scenario not in SCENARIO_ORDER:
        raise ValueError(f"Cenário fora da sequência: {scenario}")
    if not checkpoint.is_file() or not summary.is_file():
        raise FileNotFoundError("Checkpoint e training_summary.json são obrigatórios.")
    report = json.loads(summary.read_text(encoding="utf-8"))
    if report.get("selected_scenario") != scenario:
        raise RuntimeError("O relatório não corresponde ao cenário selecionado.")
    if int(report.get("selected_scenario_transitions", 0)) <= 0:
        raise RuntimeError("Não há transições elegíveis; cenário não pode entrar na cadeia.")
    data = _load()
    source_mode = report.get("source_mode", "chain")
    if source_mode not in {"chain", "custom"}:
        raise RuntimeError(f"Modo de origem inválido no resumo: {source_mode}")
    source_path_value = report.get("source_checkpoint_path") or report.get("checkpoint_original")
    if not source_path_value:
        raise RuntimeError("O resumo não registra o caminho do checkpoint de origem.")
    source_path = Path(source_path_value).expanduser().resolve()
    if not source_path.is_file():
        raise FileNotFoundError(f"Checkpoint de origem do treino não existe: {source_path}")
    source_hash = sha256_file(source_path)
    if report.get("source_checkpoint_sha256") != source_hash:
        raise RuntimeError("Hash do checkpoint de origem diverge do training_summary.json.")
    previous = predecessor(scenario)
    if source_mode == "chain" and previous:
        entry = data["scenarios"].get(previous)
        if not entry or entry.get("status") != "approved":
            raise RuntimeError(f"Não é possível registrar {scenario}: {previous} não aprovado.")
        if source_hash != entry.get("checkpoint_sha256"):
            raise RuntimeError("O checkpoint de origem não corresponde ao predecessor aprovado.")
    data["scenarios"][scenario] = {
        "status": "trained",
        "checkpoint_path": str(checkpoint.resolve()),
        "checkpoint_sha256": sha256_file(checkpoint),
        "source_mode": source_mode,
        "source_checkpoint_path": str(source_path),
        "source_checkpoint_sha256": source_hash,
        "summary_path": str(summary.resolve()),
        "evaluation_path": None,
        "approved": False,
    }
    # A new training run invalidates all later approvals and artifacts.
    index = SCENARIO_ORDER.index(scenario)
    for later in SCENARIO_ORDER[index + 1:]:
        data["scenarios"].pop(later, None)
    _save(data)


def approve_scenario(scenario: str, evaluation: Path) -> None:
    if scenario not in SCENARIO_ORDER:
        raise ValueError(f"Cenário fora da sequência: {scenario}")
    data = _load()
    entry = data["scenarios"].get(scenario)
    if not entry or entry.get("status") != "trained":
        raise RuntimeError(f"{scenario} ainda não possui treino registrado.")
    if not evaluation.is_file():
        raise FileNotFoundError(evaluation)
    result = json.loads(evaluation.read_text(encoding="utf-8"))
    if result.get("approved") is not True:
        raise RuntimeError("Avaliação não contém approved=true; cenário permanece bloqueado.")
    if result.get("checkpoint_sha256") != entry["checkpoint_sha256"]:
        raise RuntimeError("Hash da avaliação não corresponde ao checkpoint treinado.")
    entry["status"] = "approved"
    entry["approved"] = True
    entry["evaluation_path"] = str(evaluation.resolve())
    entry["evaluation_summary"] = result.get("summary", {})
    _save(data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    check.add_argument("--scenario", choices=SCENARIO_ORDER, required=True)
    check.add_argument("--checkpoint", required=True)
    check.add_argument("--custom-source", action="store_true", help="Use an explicit custom checkpoint for this run.")
    record = sub.add_parser("record")
    record.add_argument("--scenario", choices=SCENARIO_ORDER, required=True)
    record.add_argument("--checkpoint", required=True)
    record.add_argument("--summary", required=True)
    approve = sub.add_parser("approve")
    approve.add_argument("--scenario", choices=SCENARIO_ORDER, required=True)
    approve.add_argument("--evaluation", required=True)
    sub.add_parser("status")
    args = parser.parse_args()

    if args.command == "check":
        print(check_scenario(args.scenario, Path(args.checkpoint), custom_source=args.custom_source))
    elif args.command == "record":
        record_training(args.scenario, Path(args.checkpoint), Path(args.summary))
        print(f"Treino registrado: {args.scenario} (aguardando aprovação)")
    elif args.command == "approve":
        approve_scenario(args.scenario, Path(args.evaluation))
        print(f"Cenário aprovado: {args.scenario}")
    else:
        print(json.dumps(_load(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
