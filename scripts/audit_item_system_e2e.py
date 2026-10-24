#!/usr/bin/env python3
"""End-to-end compatibility audit for a TFT policy checkpoint and native match.

Writes audit.json and trace.jsonl. A successful exit requires a complete native
match and final placements for all eight players; a partial match is never
reported as a pass.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Callable

import numpy as np
import torch

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

ACTION_DIMS = [9, 5, 9, 28, 28, 28]
MASK_SHAPES = {
    "type_mask": (9,),
    "shop_mask": (5,),
    "bench_source_mask": (9,),
    "board_target_mask": (28,),
    "board_source_mask": (28,),
    "board_move_target_masks": (28, 28),
    "bench_move_source_mask": (9,),
    "bench_to_board_target_masks": (9, 28),
    "item_inventory_mask": (9,),
    "item_component_first_mask": (10,),
    "item_component_pair_masks": (10, 10),
    "item_target_mask": (37,),
}
ACTION_NAMES = {
    0: "BUY", 1: "REROLL", 2: "BUY_XP", 3: "MOVE_BENCH",
    4: "MOVE_BOARD", 5: "SELL", 6: "PASS",
    7: "EQUIP_FROM_INVENTORY", 8: "CRAFT_AND_EQUIP",
}


def _numpy_mask(mask: Any) -> np.ndarray:
    if hasattr(mask, "detach"):
        mask = mask.detach().cpu().numpy()
    return np.asarray(mask, dtype=np.bool_)


def validate_masks(masks: list[dict], player_count: int = 8) -> dict:
    if not isinstance(masks, (list, tuple)) or len(masks) != player_count:
        raise ValueError("A engine não retornou oito conjuntos de máscaras.")
    checked = 0
    missing_by_player = []
    for player_id, player_masks in enumerate(masks):
        if not isinstance(player_masks, dict):
            raise ValueError("Máscaras do jogador %d não são um dicionário." % player_id)
        missing = sorted(set(MASK_SHAPES) - set(player_masks))
        if missing:
            missing_by_player.append({"player_id": player_id, "missing": missing})
            continue
        for name, expected_shape in MASK_SHAPES.items():
            actual = _numpy_mask(player_masks[name])
            if actual.shape != expected_shape:
                raise ValueError(
                    "Máscara %s do jogador %d: shape %s, esperado %s"
                    % (name, player_id, actual.shape, expected_shape)
                )
            checked += 1
        type_mask = _numpy_mask(player_masks["type_mask"])
        if not type_mask.any():
            raise ValueError("Máscara de tipos sem nenhuma ação legal para jogador %d." % player_id)
    if missing_by_player:
        raise ValueError("Máscaras nativas incompletas: %s" % missing_by_player)
    return {"players": player_count, "mask_arrays_checked": checked, "action_type_count": 9}


def _assert_selected(mask: Any, index: int, description: str) -> None:
    values = _numpy_mask(mask).reshape(-1)
    if index < 0 or index >= len(values) or not bool(values[index]):
        raise ValueError("%s selecionado fora da máscara legal: índice %d." % (description, index))


def validate_action(action: list[int], masks: dict, player_id: int) -> None:
    if len(action) != 6:
        raise ValueError("Ação do jogador %d não tem seis componentes." % player_id)
    action_type = int(action[0])
    _assert_selected(masks["type_mask"], action_type, "action_type")
    if action_type == 0:
        _assert_selected(masks["shop_mask"], int(action[1]), "shop_slot")
    elif action_type == 3:
        source = int(action[2])
        _assert_selected(masks.get("bench_move_source_mask", masks["bench_source_mask"]), source, "bench_source")
        target_mask = _numpy_mask(masks["bench_to_board_target_masks"])[source]
        _assert_selected(target_mask, int(action[3]), "bench_to_board_target")
    elif action_type == 4:
        source = int(action[4])
        _assert_selected(masks["board_source_mask"], source, "board_source")
        target_mask = _numpy_mask(masks["board_move_target_masks"])[source]
        _assert_selected(target_mask, int(action[5]), "board_move_target")
    elif action_type == 5:
        _assert_selected(masks["bench_source_mask"], int(action[2]), "sell_source")
    elif action_type == 7:
        _assert_selected(masks["item_inventory_mask"], int(action[1]), "item_inventory")
        _assert_selected(masks["item_target_mask"], int(action[2]), "item_target")
    elif action_type == 8:
        first, second, target = int(action[1]), int(action[2]), int(action[3])
        _assert_selected(masks["item_component_first_mask"], first, "item_component_first")
        _assert_selected(_numpy_mask(masks["item_component_pair_masks"])[first], second, "item_component_second")
        _assert_selected(masks["item_target_mask"], target, "item_target")


def action_dict(values: list[int]) -> dict:
    action_type = int(values[0])
    result = {
        "type": action_type,
        "shop_slot": int(values[1]),
        "bench_slot": int(values[2]),
        "board_target": int(values[3]),
        "board_source": int(values[4]),
        "conditioned_board_target": int(values[5]),
    }
    if action_type == 7:
        result.update({"item_slot": int(values[1]), "item_target": int(values[2])})
    elif action_type == 8:
        result.update({
            "component_first": int(values[1]),
            "component_second": int(values[2]),
            "item_target": int(values[3]),
        })
    return result


def _checkpoint_state(checkpoint: Any) -> dict:
    if isinstance(checkpoint, dict) and isinstance(checkpoint.get("policy"), dict):
        return checkpoint["policy"]
    if isinstance(checkpoint, dict) and checkpoint and all(torch.is_tensor(v) for v in checkpoint.values()):
        return checkpoint
    raise ValueError("Checkpoint não contém state_dict da policy reconhecível.")


def _placements(state: dict, lobby: Any) -> dict[int, int]:
    ranking = state.get("ranking") or state.get("final_ranking") or getattr(lobby, "final_ranking", [])
    result = {}
    if isinstance(ranking, list):
        for rank, entry in enumerate(ranking, start=1):
            player_id = entry.get("player_id") if isinstance(entry, dict) else entry
            try:
                result[int(player_id)] = rank
            except (TypeError, ValueError):
                continue
    players = state.get("players", [])
    if isinstance(players, list):
        for index, player in enumerate(players):
            if not isinstance(player, dict) or player.get("placement") is None:
                continue
            try:
                result[int(player.get("player_id", index))] = int(player["placement"])
            except (TypeError, ValueError):
                continue
    return result


def run_audit(
    checkpoint_path: Path,
    output_dir: Path,
    seed: int = 20261024,
    max_steps: int = 5000,
    env_factory: Callable[..., Any] | None = None,
    device_name: str = "cpu",
) -> dict:
    if not checkpoint_path.is_file():
        raise FileNotFoundError("Checkpoint não encontrado: %s" % checkpoint_path)
    if max_steps < 1:
        raise ValueError("max_steps precisa ser maior que zero.")
    output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device(device_name)
    checkpoint_hash = hashlib.sha256(checkpoint_path.read_bytes()).hexdigest()
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
    source_state = _checkpoint_state(checkpoint)

    if env_factory is None:
        from cpp_lobby_env import CppTFTLobbyWrapper
        env_factory = CppTFTLobbyWrapper

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    lobby = env_factory(seed=seed)
    trace_path = output_dir / "trace.jsonl"
    report_path = output_dir / "audit.json"
    report = {
        "status": "running",
        "checkpoint": str(checkpoint_path),
        "checkpoint_sha256": checkpoint_hash,
        "checkpoint_update": checkpoint.get("update") if isinstance(checkpoint, dict) else None,
        "seed": seed,
        "device": str(device),
        "max_steps": max_steps,
        "checks": {},
        "steps": 0,
        "complete_match": False,
        "action_counts": {},
        "player_metrics": {
            str(player_id): {
                "actions": 0, "item_actions": 0, "reward_sum": 0.0, "reward_steps": 0,
            }
            for player_id in range(8)
        },
        "item_action_counts": {"EQUIP_FROM_INVENTORY": 0, "CRAFT_AND_EQUIP": 0},
        "native_event_count": 0,
        "placements": {},
        "errors": [],
    }
    action_counts = Counter()
    item_counts = Counter()
    total_events = 0
    complete = False
    try:
        observations = np.asarray(lobby.reset(), dtype=np.float32)
        if observations.ndim != 2 or observations.shape[0] != 8:
            raise ValueError("Observações nativas esperadas em shape (8, obs_dim), recebidas %s." % (observations.shape,))
        if not np.isfinite(observations).all():
            raise ValueError("Observações iniciais contêm NaN/Inf.")
        obs_dim = int(observations.shape[-1])
        report["checks"]["observations"] = {"shape": list(observations.shape), "finite": True}

        from policy import TFTPolicy
        policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
        migrated = bool(policy.load_compatible_state_dict(source_state))
        policy.eval()
        report["checks"]["checkpoint"] = {
            "loaded": True,
            "obs_dim": obs_dim,
            "action_dims": ACTION_DIMS,
            "compatible_migration_applied": migrated,
            "item_heads_present_in_checkpoint": all(
                key in source_state for key in (
                    "item_inventory_head.weight", "item_component_first_head.weight",
                    "item_component_second_head.weight", "item_target_head.weight",
                )
            ),
        }
        masks = lobby.get_action_masks()
        report["checks"]["native_masks"] = validate_masks(masks)

        with trace_path.open("w", encoding="utf-8") as trace:
            for step in range(max_steps):
                if bool(getattr(lobby, "finished", False)):
                    complete = True
                    break
                masks = lobby.get_action_masks()
                report["checks"]["last_mask_validation"] = validate_masks(masks)
                mask_batch = {
                    key: torch.as_tensor(
                        np.stack([_numpy_mask(player_masks[key]) for player_masks in masks]),
                        dtype=torch.bool,
                        device=device,
                    )
                    for key in masks[0]
                }
                obs_batch = torch.as_tensor(observations, dtype=torch.float32, device=device)
                with torch.no_grad():
                    chosen = policy.get_action(obs_batch, masks=mask_batch, deterministic=True)[0]
                chosen = chosen.detach().cpu().numpy().astype(int).tolist()
                if len(chosen) != 8:
                    raise ValueError("A policy retornou %d ações, esperado 8." % len(chosen))

                step_actions = []
                for player_id, values in enumerate(chosen):
                    if bool(getattr(lobby.players[player_id], "alive", True)):
                        validate_action(values, masks[player_id], player_id)
                        action_name = ACTION_NAMES.get(int(values[0]), "UNKNOWN")
                        action_counts[action_name] += 1
                        player_metric = report["player_metrics"][str(player_id)]
                        player_metric["actions"] += 1
                        if int(values[0]) in (7, 8):
                            item_counts[action_name] += 1
                            player_metric["item_actions"] += 1
                        step_actions.append(action_dict(values))
                    else:
                        step_actions.append({"type": 6})
                observations, rewards, done, info = lobby.step(step_actions)
                observations = np.asarray(observations, dtype=np.float32)
                if not np.isfinite(observations).all():
                    raise ValueError("Observações contêm NaN/Inf após step %d." % step)
                reward_values = np.asarray(rewards, dtype=np.float64).reshape(-1)
                if reward_values.shape[0] != 8:
                    raise ValueError("A engine retornou %d recompensas, esperado 8." % reward_values.shape[0])
                for player_id, reward_value in enumerate(reward_values):
                    player_metric = report["player_metrics"][str(player_id)]
                    player_metric["reward_sum"] += float(reward_value)
                    player_metric["reward_steps"] += 1
                events = info.get("events", []) if isinstance(info, dict) else []
                total_events += len(events) if isinstance(events, list) else 0
                trace.write(json.dumps({
                    "step": step,
                    "round": info.get("round") if isinstance(info, dict) else None,
                    "actions": chosen,
                    "rewards": np.asarray(rewards).astype(float).tolist(),
                    "events": events,
                    "done": bool(done),
                }, ensure_ascii=False, default=str) + "\n")
                report["steps"] = step + 1
                if done:
                    complete = True
                    break
        report["action_counts"] = dict(action_counts)
        for player_metric in report["player_metrics"].values():
            steps_count = int(player_metric["reward_steps"])
            player_metric["mean_reward_per_step"] = (
                float(player_metric["reward_sum"]) / steps_count if steps_count else 0.0
            )
        report["item_action_counts"] = {
            "EQUIP_FROM_INVENTORY": int(item_counts["EQUIP_FROM_INVENTORY"]),
            "CRAFT_AND_EQUIP": int(item_counts["CRAFT_AND_EQUIP"]),
            "total_item_actions": int(item_counts["EQUIP_FROM_INVENTORY"] + item_counts["CRAFT_AND_EQUIP"]),
        }
        report["native_event_count"] = total_events
        report["complete_match"] = complete
        if not complete:
            raise RuntimeError("Partida não terminou dentro de max_steps=%d; auditoria incompleta." % max_steps)

        get_public_state = getattr(lobby, "get_public_state", None)
        state = get_public_state() if callable(get_public_state) else {}
        if not isinstance(state, dict):
            state = {}
        placements = _placements(state, lobby)
        if len(placements) != 8 or set(placements) != set(range(8)):
            raise RuntimeError(
                "Partida terminou, mas a engine não forneceu colocação para os oito jogadores: %s"
                % sorted(placements)
            )
        report["placements"] = {str(key): value for key, value in sorted(placements.items())}
        report["checks"]["final_placements"] = {"players": len(placements), "valid": True}
        report["status"] = "passed"
    except Exception as exc:
        report["status"] = "failed"
        report["errors"].append({"type": type(exc).__name__, "message": str(exc)})
        raise
    finally:
        report["action_counts"] = dict(action_counts)
        report["item_action_counts"] = {
            "EQUIP_FROM_INVENTORY": int(item_counts["EQUIP_FROM_INVENTORY"]),
            "CRAFT_AND_EQUIP": int(item_counts["CRAFT_AND_EQUIP"]),
            "total_item_actions": int(item_counts["EQUIP_FROM_INVENTORY"] + item_counts["CRAFT_AND_EQUIP"]),
        }
        report["native_event_count"] = total_events
        report["complete_match"] = complete
        for player_metric in report["player_metrics"].values():
            steps_count = int(player_metric["reward_steps"])
            player_metric["mean_reward_per_step"] = (
                float(player_metric["reward_sum"]) / steps_count if steps_count else 0.0
            )
        close = getattr(lobby, "close", None)
        if callable(close):
            close()
        report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True, type=Path)
    parser.add_argument("--seed", type=int, default=20261024)
    parser.add_argument("--max-steps", type=int, default=5000)
    parser.add_argument("--out-dir", type=Path, default=Path("reports/item_system_phase7"))
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    args = parser.parse_args()
    try:
        report = run_audit(args.checkpoint, args.out_dir, args.seed, args.max_steps, device_name=args.device)
    except Exception as exc:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        report_path = args.out_dir / "audit.json"
        if not report_path.exists():
            report_path.write_text(json.dumps({
                "status": "failed",
                "checkpoint": str(args.checkpoint),
                "seed": args.seed,
                "max_steps": args.max_steps,
                "complete_match": False,
                "errors": [{"type": type(exc).__name__, "message": str(exc)}],
            }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("AUDIT FAILED: %s: %s" % (type(exc).__name__, exc), file=sys.stderr)
        print("Consulte %s para detalhes." % report_path, file=sys.stderr)
        return 1
    print(json.dumps({
        "status": report["status"],
        "steps": report["steps"],
        "complete_match": report["complete_match"],
        "placements": report["placements"],
        "item_action_counts": report["item_action_counts"],
        "report": str(args.out_dir / "audit.json"),
        "trace": str(args.out_dir / "trace.jsonl"),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
