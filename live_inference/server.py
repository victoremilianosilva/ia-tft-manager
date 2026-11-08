"""Local, read-only PPO inference endpoint for the TFT live-state adapter.

This service never advances a lobby, executes an action, or imports ViewerSession.
It accepts an observation and native action masks already produced by a trusted
adapter. Raw GEP snapshots are deliberately not converted here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

import numpy as np
import torch

from policy import ACTION_DIMS, LEGACY_ACTION_DIMS, TFTPolicy

ROOT = Path(__file__).resolve().parents[1]
ACTION_NAMES = {
    0: "BUY",
    1: "REROLL",
    2: "BUY_XP",
    3: "MOVE_BENCH",
    4: "MOVE_BOARD",
    5: "SELL",
    6: "PASS",
    7: "EQUIP_FROM_INVENTORY",
    8: "CRAFT_AND_EQUIP",
}
MAX_REQUEST_BYTES = 2 * 1024 * 1024


def _checkpoint_metadata(payload: dict[str, Any]) -> tuple[dict, int, list[int], int]:
    state = payload.get(
        "policy_state_dict",
        payload.get("model_state_dict", payload.get("state_dict", payload.get("policy", payload))),
    )
    if not isinstance(state, dict) or not state:
        raise ValueError("Checkpoint não contém pesos da TFTPolicy.")

    action_dims = payload.get("action_dims")
    if action_dims is None or list(action_dims) == LEGACY_ACTION_DIMS:
        action_dims = list(ACTION_DIMS)
    else:
        action_dims = [int(value) for value in action_dims]
    if action_dims != ACTION_DIMS:
        raise ValueError(f"action_dims incompatível: {action_dims}; esperado {ACTION_DIMS}.")

    obs_dim = payload.get("obs_dim")
    if obs_dim is None:
        weight = state.get("global_mlp.0.weight")
        if weight is None:
            raise ValueError("Checkpoint sem obs_dim e sem global_mlp.0.weight.")
        # Same legacy fallback used by ViewerSession.load_checkpoint.
        obs_dim = int(weight.shape[1]) + 140

    return state, int(obs_dim), action_dims, int(payload.get("hidden_size", 512))


class InferenceRuntime:
    def __init__(self, checkpoint: Path):
        checkpoint = checkpoint.expanduser().resolve()
        if not checkpoint.is_file():
            raise FileNotFoundError(f"Checkpoint não encontrado: {checkpoint}")

        payload = torch.load(checkpoint, map_location="cpu", weights_only=False)
        if not isinstance(payload, dict):
            raise ValueError("Formato de checkpoint inválido; esperado dict.")
        state, self.obs_dim, action_dims, hidden_size = _checkpoint_metadata(payload)

        self.policy = TFTPolicy(self.obs_dim, action_dims, hidden_size=hidden_size)
        self.policy.load_compatible_state_dict(state)
        self.policy.eval()
        for parameter in self.policy.parameters():
            parameter.requires_grad_(False)

        self.checkpoint = str(checkpoint)
        self.checkpoint_sha256 = hashlib.sha256(checkpoint.read_bytes()).hexdigest()

    def recommend(self, payload: dict[str, Any]) -> dict[str, Any]:
        request_id = payload.get("requestId")
        revision = payload.get("revision")
        observation = payload.get("observation")
        masks = payload.get("masks")

        if not isinstance(request_id, str) or not request_id.strip():
            raise ValueError("requestId obrigatório.")
        if not isinstance(revision, int) or revision < 0:
            raise ValueError("revision deve ser inteiro >= 0.")
        if not isinstance(observation, list) or len(observation) != self.obs_dim:
            actual = len(observation) if isinstance(observation, list) else None
            raise ValueError(f"observation deve ter {self.obs_dim} valores; recebido {actual}.")
        if not isinstance(masks, dict) or not masks:
            raise ValueError("masks nativas são obrigatórias; não serão inventadas.")

        obs_array = np.asarray(observation, dtype=np.float32)
        if not np.isfinite(obs_array).all():
            raise ValueError("observation contém NaN ou infinito.")

        # Exact native C++ mask contract exported by tft_engine_bindings.cpp.
        expected_mask_shapes = {
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
        if set(masks) != set(expected_mask_shapes):
            missing = sorted(set(expected_mask_shapes) - set(masks))
            extra = sorted(set(masks) - set(expected_mask_shapes))
            raise ValueError(f"Contrato de masks inválido; ausentes={missing}, extras={extra}.")

        tensor_masks: dict[str, torch.Tensor] = {}
        for key, value in masks.items():
            if not isinstance(key, str) or not isinstance(value, list):
                raise ValueError("Formato inválido em masks.")
            array = np.asarray(value)
            expected_shape = expected_mask_shapes[key]
            if array.shape != expected_shape:
                raise ValueError(
                    f"Shape inválido para {key}: {array.shape}; esperado {expected_shape}."
                )
            if array.dtype.kind not in {"b", "i", "u"}:
                raise ValueError(f"Máscara {key} deve conter booleanos/inteiros.")
            if not np.isin(array, [0, 1]).all():
                raise ValueError(f"Máscara {key} deve conter somente 0/1.")
            tensor_masks[key] = torch.as_tensor(array, dtype=torch.bool).unsqueeze(0)

        if not bool(tensor_masks["type_mask"].any()):
            raise ValueError("type_mask nativa não contém ação legal.")

        obs_tensor = torch.as_tensor(obs_array, dtype=torch.float32).unsqueeze(0)
        with torch.inference_mode():
            actions, logprob, entropy, value, diagnostics = (
                self.policy.get_action_and_value_with_diagnostics(
                    obs_tensor,
                    masks=tensor_masks,
                    deterministic=True,
                )
            )

        action = [int(item) for item in actions[0].cpu().tolist()]
        return {
            "type": "ai_recommendation",
            "schemaVersion": 1,
            "requestId": request_id,
            "revision": revision,
            "status": "ready",
            "checkpointSha256": self.checkpoint_sha256,
            "action": {
                "type": ACTION_NAMES.get(action[0], f"UNKNOWN_{action[0]}"),
                "components": action,
            },
            "valueEstimate": float(value[0].item()),
            "logProbability": float(logprob[0].item()),
            "entropy": float(entropy[0].item()),
            "diagnostics": diagnostics[0],
            "execution": "none",
        }


class Handler(BaseHTTPRequestHandler):
    runtime: InferenceRuntime | None = None

    def _send(self, status: int, body: dict[str, Any]) -> None:
        encoded = json.dumps(body, ensure_ascii=False, allow_nan=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self) -> None:
        if self.path != "/health":
            self._send(404, {"status": "not_found"})
            return
        runtime = self.runtime
        self._send(200, {
            "status": "ready" if runtime else "model_unavailable",
            "modelLoaded": runtime is not None,
            "checkpointSha256": runtime.checkpoint_sha256 if runtime else None,
            "observationDim": runtime.obs_dim if runtime else None,
            "mode": "read_only_inference",
        })

    def do_POST(self) -> None:
        if self.path != "/v1/recommendation":
            self._send(404, {"status": "not_found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_REQUEST_BYTES:
                raise ValueError("Content-Length inválido ou acima do limite.")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError("Body deve ser um objeto JSON.")
            if self.runtime is None:
                self._send(503, {"status": "model_unavailable"})
                return
            self._send(200, self.runtime.recommend(payload))
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError, TypeError) as exc:
            self._send(400, {"status": "invalid_request", "error": str(exc)})
        except Exception as exc:
            self._send(500, {"status": "inference_error", "error": str(exc)})

    def log_message(self, fmt: str, *args: Any) -> None:
        print("[live-inference] " + fmt % args)


def main() -> None:
    parser = argparse.ArgumentParser(description="TFT PPO read-only live inference service")
    parser.add_argument(
        "--checkpoint",
        default=os.environ.get("TFT_LIVE_CHECKPOINT", ""),
        help="PPO checkpoint path (or TFT_LIVE_CHECKPOINT).",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()

    if args.host not in {"127.0.0.1", "localhost", "::1"}:
        parser.error("O serviço aceita somente loopback local.")
    if not args.checkpoint:
        parser.error("Informe --checkpoint ou TFT_LIVE_CHECKPOINT.")

    Handler.runtime = InferenceRuntime(Path(args.checkpoint))
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(
        f"[live-inference] ready on http://{args.host}:{args.port} "
        f"(obs_dim={Handler.runtime.obs_dim}, read-only)"
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
