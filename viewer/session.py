"""Read-only PPO evaluation session, event logging and replay support."""
from __future__ import annotations

import json
import hashlib
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import torch

from policy import TFTPolicy
from cpp_lobby_env import CppTFTLobbyWrapper
from viewer.player_logs import PlayerJsonLogWriter

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "units_gerado.json"
ACTION_NAMES = {
    0: "BUY", 1: "REROLL", 2: "BUY_XP", 3: "MOVE_BENCH",
    4: "MOVE_BOARD", 5: "SELL", 6: "PASS",
}


def _jsonable(value: Any):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, torch.Tensor):
        return value.detach().cpu().tolist()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def unit_label(unit: dict | None) -> str:
    if not unit or not unit.get("occupied", True):
        return ""
    name = unit.get("champion_id") or unit.get("apiName") or unit.get("api_name") or "?"
    star = int(unit.get("star", 1) or 1)
    return f"{name} {'★' * max(1, min(star, 3))}"


@dataclass
class ViewerConfig:
    checkpoint: Path
    seed: int = 20261016
    deterministic: bool = True


class ViewerSession:
    """Controller that advances the native lobby only on explicit requests."""

    def __init__(self):
        self.lobby: CppTFTLobbyWrapper | None = None
        self.policy: TFTPolicy | None = None
        self.obs: np.ndarray | None = None
        self.masks: list[dict] | None = None
        self.public_state: dict = {}
        self.audit_snapshot: dict = {}
        self.last_actions: list[list[int]] = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        self.last_policy: list[dict] = [{} for _ in range(8)]
        self.last_info: dict = {}
        self.last_rewards = np.zeros(8, dtype=np.float32)
        self.step_count = 0
        self.config: ViewerConfig | None = None
        self.match_id = ""
        self.checkpoint_sha256 = ""
        self.started = False
        self.finished = False
        self._player_log_writer: PlayerJsonLogWriter | None = None
        self._session_dir: Path | None = None
        self._metadata_path: Path | None = None
        self._sequence = 0
        self._rng = torch.Generator(device="cpu")
        self._rng.manual_seed(0)
        self.replay_events: list[dict] = []
        self.live_events: list[dict] = []
        self.replay_mode = False
        self.replay_cursor = 0

    def load_checkpoint(self, checkpoint: str | Path, seed: int, deterministic: bool,
                        output_dir: str | Path, record: bool = True):
        path = Path(checkpoint).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Checkpoint não encontrado: {path}")
        if not CATALOG.is_file():
            raise FileNotFoundError(f"Catálogo de unidades não encontrado: {CATALOG}")
        self.close()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        payload = torch.load(path, map_location="cpu", weights_only=False)
        if isinstance(payload, dict):
            state_dict = payload.get("policy_state_dict", payload.get("model_state_dict", payload.get("state_dict", payload.get("policy", payload))))
            obs_dim = payload.get("obs_dim")
            action_dims = payload.get("action_dims", [7, 5, 9, 28, 28, 28])
            hidden_size = payload.get("hidden_size", 512)
        else:
            raise ValueError("Formato de checkpoint não reconhecido: esperado um dicionário de pesos/metadata.")
        if not isinstance(state_dict, dict) or not state_dict:
            raise ValueError("O checkpoint não contém state_dict de política.")
        if obs_dim is None:
            # Infer the input dimension from the global MLP first layer when available.
            weight = state_dict.get("global_mlp.0.weight")
            if weight is None:
                raise ValueError("Checkpoint sem obs_dim e sem global_mlp.0.weight para inferir a arquitetura.")
            obs_dim = int(weight.shape[1]) + 140
        self.policy = TFTPolicy(int(obs_dim), list(action_dims), hidden_size=int(hidden_size))
        missing, unexpected = self.policy.load_state_dict(state_dict, strict=False)
        if missing or unexpected:
            raise ValueError(
                "Checkpoint incompatível com TFTPolicy atual. "
                f"Parâmetros ausentes={missing[:8]}, extras={unexpected[:8]}"
            )
        self.policy.eval()
        for parameter in self.policy.parameters():
            parameter.requires_grad_(False)
        self._rng.manual_seed(int(seed))
        torch.manual_seed(int(seed))
        self.config = ViewerConfig(path, int(seed), bool(deterministic))
        self.checkpoint_sha256 = digest
        self.match_id = str(uuid.uuid4())
        self.lobby = CppTFTLobbyWrapper(seed=int(seed), catalog_path=str(CATALOG))
        self.obs = self.lobby.reset(seed=int(seed))
        self.masks = self.lobby.get_action_masks()
        self.public_state = self.lobby.get_public_state()
        self.audit_snapshot = self.lobby.get_audit_snapshot()
        self.started = True
        self.finished = False
        self.step_count = 0
        self.last_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        self.last_policy = [{} for _ in range(8)]
        self.last_rewards = np.zeros(8, dtype=np.float32)
        self.last_info = {}
        if record:
            out = Path(output_dir).expanduser().resolve()
            out.mkdir(parents=True, exist_ok=True)
            session_dir = out / f"match-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{self.match_id[:8]}"
            session_dir.mkdir(parents=True, exist_ok=False)
            self._session_dir = session_dir
            self._metadata_path = session_dir / "metadata.json"
            log_files = [f"player_{player_id + 1}_log.json" for player_id in range(8)]
            self._metadata_path.write_text(json.dumps({
                "schema_version": 1,
                "match_id": self.match_id,
                "checkpoint_path": str(path),
                "checkpoint_sha256": digest,
                "seed": int(seed),
                "deterministic": bool(deterministic),
                "engine": "cpp",
                "created_at": datetime.now(timezone.utc).isoformat(),
                "policy_class": "TFTPolicy",
                "observation_dim": int(obs_dim),
                "action_dims": list(action_dims),
                "log_format": "one JSON file per player",
                "player_log_files": log_files,
            }, ensure_ascii=False, indent=2), encoding="utf-8")
            self._player_log_writer = PlayerJsonLogWriter(
                session_dir,
                match_id=self.match_id,
                checkpoint_sha256=digest,
                seed=int(seed),
                deterministic=bool(deterministic),
                catalog_path=CATALOG,
                initial_snapshot=self._snapshot_for_event(),
            )
        self._emit("match_started", {
            "checkpoint_sha256": digest, "seed": int(seed),
            "mode": "deterministic" if deterministic else "stochastic",
            "initial_snapshot": self._snapshot_for_event(),
        })
        return self._snapshot_for_event()

    def _snapshot_for_event(self):
        return {
            "round": self.public_state.get("round", self.audit_snapshot.get("round", 0)),
            "stage": self.public_state.get("stage", self.audit_snapshot.get("stage", 1)),
            "finished": bool(self.public_state.get("finished", False)),
            "ranking": self.public_state.get("ranking", []),
            "winner_id": self.public_state.get("winner_id"),
            "players": self.public_state.get("players", []),
            "audit_players": self.audit_snapshot.get("players", []),
        }

    def _emit(self, event_type: str, payload: dict):
        self._sequence += 1
        event = {
            "schema_version": 1,
            "match_id": self.match_id,
            "sequence_id": self._sequence,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "step": self.step_count,
            "round": self.public_state.get("round", 0),
            "stage": self.public_state.get("stage", 1),
            "event_type": event_type,
            "checkpoint_id": self.checkpoint_sha256,
            "payload": _jsonable(payload),
        }
        self.live_events.append(event)
        if len(self.live_events) > 5000:
            del self.live_events[:1000]
        return event

    def _action_for_player(self, player_id: int):
        if self.policy is None or self.obs is None or self.masks is None:
            return [6, 0, 0, 0, 0, 0], {}
        mask = self.masks[player_id]
        obs = torch.as_tensor(self.obs[player_id:player_id + 1], dtype=torch.float32)
        tensor_masks = {}
        for key, value in mask.items():
            try:
                tensor_masks[key] = torch.as_tensor(np.asarray(value), dtype=torch.bool).unsqueeze(0)
            except (ValueError, TypeError):
                continue
        infer = self.policy.get_action_and_value_with_diagnostics
        with torch.inference_mode():
            actions, logprob, entropy, value, diagnostics = infer(
                obs, masks=tensor_masks, deterministic=self.config.deterministic
            )
        action = [int(x) for x in actions[0].detach().cpu().tolist()]
        diag = {
            "action_name": ACTION_NAMES.get(action[0], f"UNKNOWN_{action[0]}"),
            "action": action,
            "log_probability": float(logprob[0].item()),
            "entropy": float(entropy[0].item()),
            "value_estimate": float(value[0].item()),
            "distributions": diagnostics[0],
        }
        return action, diag

    def step(self):
        if not self.started or self.lobby is None:
            raise RuntimeError("Carregue um checkpoint antes de avançar.")
        if self.finished:
            return self._snapshot_for_event()
        before = self._snapshot_for_event()
        actions, diagnostics = [], []
        for player_id in range(8):
            player_state = self.public_state.get("players", [])
            player = next((p for p in player_state if int(p.get("player_id", -1)) == player_id), {})
            if not player.get("alive", True):
                actions.append([6, 0, 0, 0, 0, 0])
                diagnostics.append({"action_name": "PASS", "action": [6, 0, 0, 0, 0, 0], "status": "eliminated_seat"})
            else:
                action, diag = self._action_for_player(player_id)
                actions.append(action)
                diagnostics.append(diag)
        self._emit("decision_batch", {
            "before": before,
            "players": [
                {"player_id": i, "action_proposed": actions[i], "policy_diagnostics": diagnostics[i]}
                for i in range(8)
            ],
        })
        # One native step is a simultaneous eight-seat lobby step.
        obs, rewards, done, info = self.lobby.step(actions)
        self.obs = obs
        self.last_actions = actions
        self.last_policy = diagnostics
        self.last_rewards = np.asarray(rewards, dtype=np.float32)
        self.last_info = info
        self.masks = self.lobby.get_action_masks()
        self.public_state = self.lobby.get_public_state()
        self.audit_snapshot = self.lobby.get_audit_snapshot()
        self.finished = bool(done or self.public_state.get("finished", False))
        self.step_count += 1
        after = self._snapshot_for_event()
        self._emit("step_completed", {
            "actions_submitted": actions,
            "rewards": self.last_rewards,
            "action_rewards": info.get("action_rewards"),
            "combat_rewards": info.get("combat_rewards"),
            "placement_rewards": info.get("placement_rewards"),
            "engine_events": info.get("events", []),
            "before": before,
            "after": after,
            "players": after.get("players", []),
        })
        if self._player_log_writer is not None:
            self._player_log_writer.record_step(
                before=before,
                after=after,
                actions=actions,
                diagnostics=diagnostics,
                rewards=self.last_rewards,
                info=info,
                step=self.step_count,
                finished=self.finished,
            )
        if self.finished:
            self._emit("match_finished", {
                "ranking": self.public_state.get("ranking", []),
                "winner_id": self.public_state.get("winner_id"),
                "final_snapshot": after,
            })
            self._flush_close_log()
        return after

    def _flush_close_log(self):
        if self._player_log_writer is not None:
            self._player_log_writer.close()
            self._player_log_writer = None

    def load_replay(self, path: str | Path):
        source = Path(path).expanduser().resolve()
        if source.is_dir():
            legacy_stream = source / "events.jsonl"
            source = legacy_stream if legacy_stream.is_file() else source / "player_1_log.json"
        if not source.is_file():
            raise FileNotFoundError(source)

        events = []
        if source.suffix.casefold() == ".json":
            try:
                document = json.loads(source.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Log JSON inválido: {exc}") from exc
            if not isinstance(document, dict) or document.get("schema_version") != 1:
                raise ValueError("Versão ou estrutura do log JSON não suportada.")
            if document.get("log_format") == "tft_player_log":
                events = document.get("entries", [])
            elif isinstance(document.get("events"), list):
                events = document["events"]
            else:
                raise ValueError("O JSON não contém entries de um log de jogador.")
        else:
            # Compatibility reader only: new sessions no longer write JSONL.
            with source.open("r", encoding="utf-8") as stream:
                for line_no, line in enumerate(stream, 1):
                    if not line.strip():
                        continue
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"Replay JSONL legado inválido na linha {line_no}: {exc}") from exc
                    events.append(event)

        if not isinstance(events, list):
            raise ValueError("O arquivo de replay precisa conter uma lista de eventos.")
        for index, event in enumerate(events, 1):
            if not isinstance(event, dict) or event.get("schema_version") != 1:
                raise ValueError(f"Evento {index} possui esquema ausente ou incompatível.")
        seq = [int(e.get("sequence_id", -1)) for e in events]
        if seq != sorted(seq) or len(seq) != len(set(seq)):
            raise ValueError("Replay com sequence_id duplicado ou fora de ordem.")

        self._flush_close_log()
        if self.lobby is not None:
            self.lobby.close()
            self.lobby = None
        self.policy = None
        self.obs = None
        self.masks = None
        self.started = False
        self.finished = False
        self._metadata_path = None
        self._session_dir = None
        self.live_events = []
        self.replay_events = events
        self.replay_cursor = 0
        self.replay_mode = True
        return len(events)

    def replay_event(self, index: int):
        if not self.replay_mode:
            raise RuntimeError("Nenhum replay carregado.")
        if not self.replay_events:
            return None
        self.replay_cursor = max(0, min(int(index), len(self.replay_events) - 1))
        return self.replay_events[self.replay_cursor]

    def close(self):
        self._flush_close_log()
        if self.lobby is not None:
            self.lobby.close()
            self.lobby = None
        self.policy = None
        self.obs = None
        self.masks = None
        self.started = False
        self.finished = False
        self._metadata_path = None
        self._session_dir = None
        self._sequence = 0
        self.replay_events = []
        self.live_events = []
        self.replay_mode = False
        self.replay_cursor = 0
