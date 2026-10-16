"""Thin Gym-style adapter for the native C++ eight-player lobby.

The wrapper intentionally contains no game rules. The C++ lobby owns the
match state, the eight player environments, action execution, combat,
rewards, observations and masks. Python keeps only the interface expected by
LobbyVectorEnv/Trainer.
"""
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
import sys

import numpy as np


_REPO_ROOT = Path(__file__).resolve().parent
_CPP_BUILD_DIRS = (
    _REPO_ROOT / "cpp" / "build" / "bin" / "Release",
    _REPO_ROOT / "cpp" / "build" / "bin",
)
for _build_dir in _CPP_BUILD_DIRS:
    if _build_dir.exists() and str(_build_dir) not in sys.path:
        sys.path.insert(0, str(_build_dir))

try:
    from tft_engine import TFTLobby as _NativeTFTLobby
except ImportError as exc:
    raise ImportError(
        "Não foi possível importar tft_engine. "
        "Compile o módulo C++ com CMake antes de iniciar o Trainer."
    ) from exc


class CppTFTLobbyWrapper:
    """Python adapter around one native C++ lobby containing eight players."""

    PLAYERS_PER_LOBBY = 8
    ACTION_COMPONENTS = 6

    def __init__(self, seed: int | None = None, catalog_path: str | None = None):
        native_seed = 0 if seed is None else int(seed)
        self._engine = _NativeTFTLobby(
            native_seed,
            "" if catalog_path is None else str(catalog_path),
        )
        self._last_dones = np.zeros(self.PLAYERS_PER_LOBBY, dtype=np.bool_)
        self._players = [
            SimpleNamespace(player_id=i, alive=True, eliminated=False)
            for i in range(self.PLAYERS_PER_LOBBY)
        ]
        self._closed = False

    @property
    def players(self):
        """Compatibility view used by LobbyVectorEnv; state remains in C++."""
        return self._players

    @staticmethod
    def _normalize_action(action):
        if isinstance(action, dict):
            values = [
                action.get("type", 6),
                action.get("shop_slot", 0),
                action.get("bench_slot", action.get("bench_source", 0)),
                action.get("board_target", 0),
                action.get("board_source", 0),
                action.get(
                    "board_move_target",
                    action.get(
                        "conditioned_board_target",
                        action.get("board_target", 0),
                    ),
                ),
            ]
        else:
            values = list(action)
        if len(values) != CppTFTLobbyWrapper.ACTION_COMPONENTS:
            raise ValueError("Cada ação deve conter exatamente 6 componentes.")
        return [int(value) for value in values]

    def reset(self, seed: int | None = None):
        result = self._engine.reset(seed)
        self._last_dones.fill(False)
        self._players = [
            SimpleNamespace(player_id=i, alive=True, eliminated=False)
            for i in range(self.PLAYERS_PER_LOBBY)
        ]
        return np.asarray(result["observations"], dtype=np.float32)

    def step(self, actions):
        """Execute one action for each of the eight player environments."""
        if len(actions) != self.PLAYERS_PER_LOBBY:
            raise ValueError(
                f"Esperava {self.PLAYERS_PER_LOBBY} ações; recebi {len(actions)}."
            )

        native_actions = [self._normalize_action(action) for action in actions]
        result = self._engine.step(native_actions)

        observations = np.asarray(result["observations"], dtype=np.float32)
        rewards = np.asarray(result["rewards"], dtype=np.float32)
        self._last_dones = np.asarray(result["dones"], dtype=np.bool_)
        player_info = result.get("players", [])
        self._players = [
            SimpleNamespace(
                player_id=int(player.get("player_id", idx)),
                alive=bool(player.get("alive", False)),
                eliminated=bool(player.get("eliminated", False)),
            )
            for idx, player in enumerate(player_info)
        ]

        info = {
            "players": result.get("players", []),
            "round": int(result.get("round", 0)),
            "stage": int(result.get("stage", 1)),
            "finished": bool(result.get("lobby_done", False)),
            "lobby_done": bool(result.get("lobby_done", False)),
            "events": list(result.get("events", [])),
            "action_rewards": np.asarray(
                result.get("action_rewards", rewards), dtype=np.float32
            ),
            "combat_rewards": np.asarray(
                result.get("combat_rewards", np.zeros(8)), dtype=np.float32
            ),
            "placement_rewards": np.asarray(
                result.get("placement_rewards", np.zeros(8)), dtype=np.float32
            ),
        }
        return observations, rewards, bool(result.get("lobby_done", False)), info

    def get_action_masks(self):
        return self._engine.get_action_masks()

    def get_strategies(self):
        """Return native strategy snapshots as the enum expected by Trainer logs."""
        from strategy.StrategyManager import Strategy

        snapshots = self._engine.get_strategies()
        result = []
        for snapshot in snapshots:
            if isinstance(snapshot, dict):
                strategy_id = int(snapshot.get("strategy", 0))
            else:
                strategy_id = int(snapshot)
            try:
                result.append(Strategy(strategy_id))
            except ValueError:
                result.append(Strategy.ECON)
        return result

    def get_anti_loop_metrics(self):
        return dict(self._engine.get_anti_loop_metrics())


    def close(self):
        if not self._closed:
            self._engine.close()
            self._closed = True

    def get_public_state(self):
        """Read-only public lobby snapshot exposed by the native engine."""
        return self._engine.get_public_state()

    def get_audit_snapshot(self):
        """Read-only board/bench/shop and mask snapshot for the observer."""
        return self._engine.get_audit_snapshot()
