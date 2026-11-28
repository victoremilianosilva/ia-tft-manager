"""Thin Gym-style adapter for the native C++ eight-player lobby.

The wrapper intentionally contains no game rules. The C++ lobby owns the
match state, the eight player environments, action execution, combat,
rewards, the neutral observation carrier and masks. The observation array is
only a [players, 1] batch/device carrier; PPO decision features must be built
from the correlated native semantic-v7 snapshot. Python keeps only the
interface expected by LobbyVectorEnv/Trainer.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
from types import SimpleNamespace
import copy
import os
import sys

import numpy as np

from decision_identity import build_player_identity_envelopes
from reward_audit import RewardAuditLedger
from immutable_snapshot import FrozenDict, FrozenList, freeze_snapshot

_REPO_ROOT = Path(__file__).resolve().parent
# CMake builds may live at the repository root (build/) or under cpp/.
# The extension can be emitted directly in the build directory or in bin/
# (and, on multi-config generators such as Visual Studio, bin/Release).
_CPP_BUILD_DIRS = (
    _REPO_ROOT / "build" / "bin" / "Release",
    _REPO_ROOT / "build" / "bin",
    _REPO_ROOT / "build",
    _REPO_ROOT / "cpp" / "build" / "bin" / "Release",
    _REPO_ROOT / "cpp" / "build" / "bin",
    _REPO_ROOT / "cpp" / "build",
)
# Preserve the priority order above: insert() prepends to sys.path.
for _build_dir in reversed(_CPP_BUILD_DIRS):
    if _build_dir.is_dir() and str(_build_dir) not in sys.path:
        sys.path.insert(0, str(_build_dir))

try:
    from tft_engine import TFTLobby as _NativeTFTLobby, LobbyBatchManager as _NativeLobbyBatchManager
except ImportError as exc:
    raise ImportError(
        "Não foi possível importar tft_engine. "
        "Compile o módulo C++ com CMake antes de iniciar o Trainer."
    ) from exc


class _NativeFrozenDict(FrozenDict):
    """Shallow, recursively read-only view over one native-owned record."""

    def __init__(self, values=()):
        dict.__init__(self)
        self._view_cache = {}
        source = values.items() if isinstance(values, Mapping) else values
        for key, value in source:
            dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        value = dict.__getitem__(self, key)
        if _is_native_snapshot_scalar(value):
            return value
        cached = self._view_cache.get(key, _MISSING_NATIVE_VIEW)
        if cached is not _MISSING_NATIVE_VIEW:
            return cached
        wrapped = _wrap_native_snapshot_value(value)
        self._view_cache[key] = wrapped
        return wrapped

    def get(self, key, default=None):
        try:
            value = dict.__getitem__(self, key)
        except KeyError:
            return default
        if _is_native_snapshot_scalar(value):
            return value
        cached = self._view_cache.get(key, _MISSING_NATIVE_VIEW)
        if cached is not _MISSING_NATIVE_VIEW:
            return cached
        wrapped = _wrap_native_snapshot_value(value)
        self._view_cache[key] = wrapped
        return wrapped

    def items(self):
        return ((key, self[key]) for key in dict.__iter__(self))

    def values(self):
        return (self[key] for key in dict.__iter__(self))

    def copy(self):
        return {key: self[key] for key in dict.__iter__(self)}

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self


class _NativeFrozenList(FrozenList):
    """Shallow, recursively read-only list view over native-owned values."""

    def __init__(self, values=()):
        list.__init__(self)
        self._view_cache = {}
        for value in values:
            list.append(self, value)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[position] for position in range(*index.indices(len(self)))]
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("native snapshot sequence index out of range")
        value = list.__getitem__(self, index)
        if _is_native_snapshot_scalar(value):
            return value
        cached = self._view_cache.get(index, _MISSING_NATIVE_VIEW)
        if cached is not _MISSING_NATIVE_VIEW:
            return cached
        wrapped = _wrap_native_snapshot_value(value)
        self._view_cache[index] = wrapped
        return wrapped

    def __iter__(self):
        for index in range(len(self)):
            yield self[index]

    def __eq__(self, other):
        if isinstance(other, Sequence) and not isinstance(other, (str, bytes)):
            return list(self) == list(other)
        return NotImplemented

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self


_MISSING_NATIVE_VIEW = object()


def _is_native_snapshot_scalar(value):
    # Scalar leaves are immutable already; caching them only adds hash-table
    # traffic and retains thousands of values during semantic projection.
    return value is None or isinstance(value, (str, bytes, int, float, bool))


def _wrap_native_snapshot_value(value):
    if isinstance(value, (_NativeFrozenDict, _NativeFrozenList)):
        return value
    if isinstance(value, Mapping):
        return _NativeFrozenDict(value)
    if isinstance(value, list):
        return _NativeFrozenList(value)
    if isinstance(value, tuple):
        return tuple(_wrap_native_snapshot_value(item) for item in value)
    return value


class _NativeSnapshotPlayers(Sequence):
    """Lazy immutable sequence of player records owned by one native handle."""

    def __init__(self, handle):
        self._handle = handle
        self._cache = {}

    def __len__(self):
        return int(self._handle.player_count())

    def _load_player(self, index):
        # C++ returns a fresh value tree from the pinned const snapshot. The
        # shallow wrappers make it recursively read-only without a second
        # recursive Python copy/freeze pass.
        return _NativeFrozenDict(self._handle.player(index))

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[position] for position in range(*index.indices(len(self)))]
        index = int(index)
        size = len(self)
        if index < 0:
            index += size
        if index < 0 or index >= size:
            raise IndexError("native snapshot player index out of range")
        if index not in self._cache:
            self._cache[index] = self._load_player(index)
        return self._cache[index]

    def __iter__(self):
        for index in range(len(self)):
            yield self[index]

    def __eq__(self, other):
        if isinstance(other, Sequence) and not isinstance(other, (str, bytes)):
            return list(self) == list(other)
        return NotImplemented

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self


class _NativeSnapshotMapping(Mapping):
    """Read-only mapping over one pinned native snapshot.

    The large combat event lists are converted to Python only when requested.
    Each deepcopy creates an independent Python materialization cache while
    retaining the immutable native snapshot value and its exact sequence.
    """

    _COMBAT_FIELDS = frozenset((
        "combat_damage_events",
        "combat_attack_events",
        "combat_death_events",
    ))

    def __init__(self, handle):
        self._handle = handle
        self._base = None
        self._combat_cache = {}
        self._players = None

    def _base_dict(self):
        if self._base is None:
            # Native handles materialize only envelope-level fields here;
            # player subtrees are fetched independently on first access.
            # Python fixture handles retain the legacy complete-dictionary path.
            envelope = getattr(self._handle, "to_envelope_dict", None)
            native_snapshot = envelope() if callable(envelope) else self._handle.to_dict()
            self._base = (
                native_snapshot
                if isinstance(native_snapshot, FrozenDict)
                else freeze_snapshot(native_snapshot)
            )
        return self._base

    def __getitem__(self, key):
        if key == "players" and callable(getattr(self._handle, "player", None)):
            if self._players is None:
                self._players = _NativeSnapshotPlayers(self._handle)
            return self._players
        if key in self._COMBAT_FIELDS:
            if key not in self._combat_cache:
                self._combat_cache[key] = freeze_snapshot(self._handle.combat_events(key))
            return self._combat_cache[key]
        return self._base_dict()[key]

    def __iter__(self):
        return iter(self._handle.keys())

    def __len__(self):
        return len(self._handle.keys())

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self._handle.keys()

    def keys(self):
        return self._handle.keys()

    def items(self):
        return ((key, self[key]) for key in self)

    def values(self):
        return (self[key] for key in self)

    def copy(self):
        return {key: self[key] for key in self}

    def _immutable(self, *_args, **_kwargs):
        raise TypeError("native audit snapshot is immutable")

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    pop = _immutable
    popitem = _immutable
    setdefault = _immutable
    update = _immutable
    __ior__ = _immutable

    def __deepcopy__(self, memo):
        # The handle pins a const native value and all Python materializations
        # are recursively frozen, so copying the mapping would only duplicate
        # immutable audit evidence.
        memo[id(self)] = self
        return self


class CppTFTLobbyWrapper:
    """Python adapter around one native C++ lobby containing eight players."""

    PLAYERS_PER_LOBBY = 8
    ACTION_COMPONENTS = 6

    def __init__(self, seed: int | None = None, catalog_path: str | None = None, item_catalog_path: str | None = None, *, native_engine=None):
        native_seed = 0 if seed is None else int(seed)
        # Default to the catalog generated by scripts/generate_item_catalog.py.
        # Callers can still supply an explicit set catalog or test fixture.
        resolved_item_catalog = (
            Path(item_catalog_path).expanduser().resolve()
            if item_catalog_path
            else _REPO_ROOT / "data" / "itens.json"
        )
        self._owns_engine = native_engine is None
        self._engine = native_engine if native_engine is not None else _NativeTFTLobby(
            native_seed,
            "" if catalog_path is None else str(catalog_path),
            str(resolved_item_catalog),
        )
        self._last_dones = np.zeros(self.PLAYERS_PER_LOBBY, dtype=np.bool_)
        self._last_action_masks = None
        self._last_snapshot_metadata = None
        self._reward_audit_ledger = RewardAuditLedger()
        self._players = [
            SimpleNamespace(player_id=i, alive=True, eliminated=False)
            for i in range(self.PLAYERS_PER_LOBBY)
        ]
        self._closed = False

    def grant_item_component(self, player_id: int, component_id: str) -> bool:
        """Forward a validated loot event into the authoritative native player state."""
        return bool(self._engine.grant_item_component(int(player_id), str(component_id)))

    def grant_completed_item(self, player_id: int, item_id: str) -> bool:
        """Forward a completed-item armory/loot event into the native player state."""
        return bool(self._engine.grant_completed_item(int(player_id), str(item_id)))

    @property
    def players(self):
        """Compatibility view used by LobbyVectorEnv; state remains in C++."""
        return self._players

    @staticmethod
    def _normalize_action(action):
        if isinstance(action, dict):
            action_type = int(action.get("type", 6))
            if action_type == 7:
                values = [
                    action_type, action.get("item_slot", 0),
                    action.get("item_target", 0), 0, 0, 0,
                ]
            elif action_type == 8:
                values = [
                    action_type, action.get("component_first", 0),
                    action.get("component_second", 0),
                    action.get("item_target", 0), 0, 0,
                ]
            else:
                values = [
                    action_type,
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

    _PACKED_ACTION_MASK_LAYOUT = (
        ("type_mask", (9,)),
        ("shop_mask", (5,)),
        ("bench_source_mask", (9,)),
        ("board_target_mask", (28,)),
        ("board_source_mask", (28,)),
        ("board_move_target_masks", (28, 28)),
        ("bench_move_source_mask", (9,)),
        ("bench_to_board_target_masks", (9, 28)),
        ("item_inventory_mask", (9,)),
        ("item_component_first_mask", (10,)),
        ("item_component_pair_masks", (10, 10)),
        ("item_target_mask", (37,)),
    )
    _PACKED_ACTION_MASK_WIDTH = 1280

    @staticmethod
    def _copy_action_masks(masks, *, detach_arrays=False):
        """Normalize either the packed native buffer or legacy mapping fixtures."""
        if isinstance(masks, np.ndarray):
            packed = np.asarray(masks)
            expected_shape = (
                CppTFTLobbyWrapper.PLAYERS_PER_LOBBY,
                CppTFTLobbyWrapper._PACKED_ACTION_MASK_WIDTH,
            )
            if packed.dtype != np.bool_ or packed.shape != expected_shape:
                raise RuntimeError(
                    "Buffer compacto de action masks inválido: "
                    f"dtype={packed.dtype}, shape={packed.shape}, esperado bool{expected_shape}."
                )
            normalized = []
            for player_index in range(CppTFTLobbyWrapper.PLAYERS_PER_LOBBY):
                offset = 0
                player_masks = {}
                for key, shape in CppTFTLobbyWrapper._PACKED_ACTION_MASK_LAYOUT:
                    width = int(np.prod(shape))
                    view = packed[player_index, offset:offset + width].reshape(shape)
                    player_masks[key] = view.copy() if detach_arrays else view
                    offset += width
                if offset != CppTFTLobbyWrapper._PACKED_ACTION_MASK_WIDTH:
                    raise RuntimeError("Layout compacto de action masks incompatível.")
                normalized.append(player_masks)
            return normalized

        if masks is None or len(masks) != CppTFTLobbyWrapper.PLAYERS_PER_LOBBY:
            raise RuntimeError("Snapshot nativo sem as oito action masks esperadas.")
        return [
            {
                key: (
                    np.asarray(value, dtype=np.bool_).copy()
                    if detach_arrays
                    else np.asarray(value, dtype=np.bool_)
                )
                for key, value in player.items()
            }
            for player in masks
        ]

    @classmethod
    def _copy_native_state_snapshot(cls, value, expected_identity):
        if not isinstance(value, Mapping):
            raise RuntimeError("Snapshot nativo estruturado ausente ou inválido.")
        version = value.get("contract_version")
        if (
            value.get("contract_id") != "tft.native-state-snapshot"
            or isinstance(version, bool)
            or not isinstance(version, int)
            or version != 6
        ):
            raise RuntimeError("Versão/identidade do contrato de snapshot estruturado incompatível.")
        geometry_version = value.get("board_geometry_version")
        board_rows = value.get("board_rows")
        board_columns = value.get("board_columns")
        if (
            value.get("board_geometry_id") != "tft.board-grid.rectangular-4x7"
            or isinstance(geometry_version, bool) or not isinstance(geometry_version, int) or geometry_version != 1
            or isinstance(board_rows, bool) or not isinstance(board_rows, int) or board_rows != 4
            or isinstance(board_columns, bool) or not isinstance(board_columns, int) or board_columns != 7
            or value.get("board_position_formula") != "row=slot/7;column=slot%7"
        ):
            raise RuntimeError("Snapshot estruturado contém contrato de geometria do board incompatível.")
        if value.get("source_namespace") != "tft.engine.observation-snapshot":
            raise RuntimeError("Namespace de sequência do snapshot estruturado incompatível.")
        if value.get("producer") != "TFTEngine::get_audit_snapshot":
            raise RuntimeError("Produtor do snapshot estruturado incompatível.")
        if value.get("engine_instance_id") != expected_identity["engine_instance_id"]:
            raise RuntimeError("Snapshot estruturado pertence a outra instância da Engine.")
        episode_id = value.get("episode_id")
        if isinstance(episode_id, bool) or not isinstance(episode_id, int) or episode_id < 0:
            raise RuntimeError("Snapshot estruturado contém episode_id inválido.")
        if episode_id != expected_identity["episode_id"]:
            raise RuntimeError("Snapshot estruturado pertence a outro episódio.")
        if "round" in expected_identity:
            snapshot_round = value.get("round")
            if (
                isinstance(snapshot_round, bool)
                or not isinstance(snapshot_round, int)
                or snapshot_round != expected_identity["round"]
            ):
                raise RuntimeError("Snapshot estruturado pertence a outro round.")
        snapshot_sequence = value.get("snapshot_sequence")
        if isinstance(snapshot_sequence, bool) or not isinstance(snapshot_sequence, int) or snapshot_sequence < 0:
            raise RuntimeError("Snapshot estruturado contém snapshot_sequence inválida.")
        if snapshot_sequence != expected_identity["decision_sequence"]:
            raise RuntimeError("Snapshot estruturado não corresponde à sequência publicada.")
        player_sequences = value.get("player_decision_sequences")
        if (
            not isinstance(player_sequences, list)
            or len(player_sequences) != cls.PLAYERS_PER_LOBBY
            or any(isinstance(seq, bool) or not isinstance(seq, int) or seq < 0 for seq in player_sequences)
        ):
            raise RuntimeError("Snapshot estruturado contém sequências individuais inválidas.")
        if player_sequences != expected_identity["player_decision_sequences"]:
            raise RuntimeError("Snapshot estruturado não corresponde às sequências individuais publicadas.")
        pool = value.get("shared_pool")
        if not isinstance(pool, dict):
            raise RuntimeError("Snapshot estruturado sem shared_pool nativo.")
        pool_version = pool.get("contract_version")
        if (
            pool.get("contract_id") != "tft.shared-champion-pool-snapshot"
            or isinstance(pool_version, bool)
            or not isinstance(pool_version, int)
            or pool_version != 2
            or pool.get("producer") != "UnitPool::available"
        ):
            raise RuntimeError("Contrato do snapshot compartilhado de pool incompatível.")
        inherited_pool_envelope = (
            "source_namespace", "engine_instance_id", "episode_id",
            "snapshot_sequence", "player_decision_sequences",
        )
        if any(key in pool for key in inherited_pool_envelope):
            raise RuntimeError(
                "Snapshot do pool duplicou campos do envelope nativo; "
                "a correlação deve ser herdada do AuditSnapshot."
            )
        total_available = pool.get("total_available")
        if isinstance(total_available, bool) or not isinstance(total_available, int) or total_available < 0:
            raise RuntimeError("Snapshot do pool contém total_available inválido.")
        champions = pool.get("champions")
        if not isinstance(champions, list) or not champions:
            raise RuntimeError("Snapshot do pool não contém catálogo de campeões.")
        seen_ids, seen_names, available_sum = set(), set(), 0
        for row in champions:
            if not isinstance(row, dict):
                raise RuntimeError("Registro de campeão inválido no snapshot do pool.")
            champion_id, name = row.get("champion_internal_id"), row.get("champion_id")
            cost, initial, available = row.get("cost"), row.get("initial_count"), row.get("available_count")
            if (
                isinstance(champion_id, bool) or not isinstance(champion_id, int) or champion_id < 0
                or not isinstance(name, str) or not name
                or isinstance(cost, bool) or not isinstance(cost, int) or not 1 <= cost <= 5
                or isinstance(initial, bool) or not isinstance(initial, int) or initial <= 0
                or isinstance(available, bool) or not isinstance(available, int)
                or not 0 <= available <= initial
                or champion_id in seen_ids or name in seen_names
            ):
                raise RuntimeError("Registro de campeão inválido/duplicado no snapshot do pool.")
            seen_ids.add(champion_id)
            seen_names.add(name)
            available_sum += available
        if available_sum != total_available:
            raise RuntimeError("Total do pool não corresponde à soma das disponibilidades por campeão.")

        inherited_event_envelope = {
            "engine_instance_id", "episode_id", "snapshot_sequence",
            "player_decision_sequence",
        }
        parent_combat_sequence = value.get("combat_sequence")
        if (
            isinstance(parent_combat_sequence, bool)
            or not isinstance(parent_combat_sequence, int)
            or parent_combat_sequence < 0
        ):
            raise RuntimeError("Snapshot estruturado contém combat_sequence inválido.")
        # NativeAuditSnapshotHandle validates every event sequence against the
        # pinned parent combat_sequence in C++ before publishing this view.
        # Dict-backed fixtures retain the full Python-side validation path.
        if not isinstance(value, _NativeSnapshotMapping):
            for field in ("combat_damage_events", "combat_attack_events", "combat_death_events"):
                rows = value.get(field)
                if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
                    raise RuntimeError(f"Snapshot estruturado contém {field} inválido.")
                for row in rows:
                    sequence = row.get("combat_sequence")
                    if "round" in row:
                        raise RuntimeError(f"{field} duplicou round do envelope pai.")
                    if (
                        isinstance(sequence, bool) or not isinstance(sequence, int)
                        or sequence <= 0 or sequence > parent_combat_sequence
                    ):
                        raise RuntimeError(f"{field} contém combat_sequence inválido.")

        event_contracts = (
            ("economy_resolution_events", "tft.economy-resolution-event",
             "tft.economy-engine.resolve-round", "EconomyEngine::resolve_round"),
            ("pvp_result_credit_events", "tft.pvp-result-credit-event",
             "tft.economy-engine.register-pvp-win", "EconomyEngine::register_pvp_win"),
        )
        for field, contract_id, source_namespace, producer in event_contracts:
            rows = value.get(field)
            if not isinstance(rows, list):
                raise RuntimeError(f"Snapshot estruturado contém {field} inválido.")
            for row in rows:
                version = row.get("contract_version") if isinstance(row, dict) else None
                if (
                    not isinstance(row, dict)
                    or row.get("contract_id") != contract_id
                    or isinstance(version, bool) or not isinstance(version, int) or version != 2
                    or row.get("source_namespace") != source_namespace
                    or row.get("producer") != producer
                ):
                    raise RuntimeError(f"Contrato de evento incompatível em {field}.")
                if inherited_event_envelope.intersection(row):
                    raise RuntimeError(
                        f"{field} duplicou identidade/sequence do envelope pai."
                    )
                if field == "economy_resolution_events":
                    player_id = row.get("player_id")
                    if (
                        isinstance(player_id, bool) or not isinstance(player_id, int)
                        or not 0 <= player_id < cls.PLAYERS_PER_LOBBY
                    ):
                        raise RuntimeError(
                            "economy_resolution_events contém player_id sem sequência no envelope pai."
                        )
                if field == "pvp_result_credit_events":
                    winner_id = row.get("winner_player_id")
                    loser_id = row.get("loser_player_id")
                    if (
                        isinstance(winner_id, bool) or not isinstance(winner_id, int)
                        or isinstance(loser_id, bool) or not isinstance(loser_id, int)
                        or not 0 <= winner_id < cls.PLAYERS_PER_LOBBY
                        or not 0 <= loser_id < cls.PLAYERS_PER_LOBBY
                        or winner_id == loser_id
                    ):
                        raise RuntimeError(
                            "pvp_result_credit_events contém owners sem sequência no envelope pai."
                        )
                    sequence = row.get("combat_sequence")
                    if "round" in row:
                        raise RuntimeError(
                            "pvp_result_credit_events duplicou round do envelope pai."
                        )
                    if (
                        isinstance(sequence, bool) or not isinstance(sequence, int)
                        or sequence <= 0 or sequence > parent_combat_sequence
                    ):
                        raise RuntimeError(
                            "pvp_result_credit_events contém combat_sequence inválido."
                        )

        players = value.get("players")
        if not isinstance(players, Sequence) or len(players) != cls.PLAYERS_PER_LOBBY:
            raise RuntimeError("Snapshot estruturado não contém exatamente oito jogadores.")
        expected_slots = {"board": 28, "bench": 9, "shop": 5}
        # Unit UUID is scoped by Engine/episode/player. One active copy may
        # occupy exactly one board, bench or shop slot in this snapshot.
        seen_unit_uuids = set()
        for player_id, player in enumerate(players):
            actual_player_id = player.get("player_id") if isinstance(player, dict) else None
            if (
                isinstance(actual_player_id, bool)
                or not isinstance(actual_player_id, int)
                or actual_player_id != player_id
            ):
                raise RuntimeError(f"Registro estruturado desalinhado para jogador {player_id}.")
            for field, expected_count in expected_slots.items():
                units = player.get(field)
                if not isinstance(units, list) or len(units) != expected_count:
                    raise RuntimeError(f"Snapshot do jogador {player_id} possui cardinalidade inválida em {field}.")
                for slot, unit in enumerate(units):
                    if not isinstance(unit, dict) or not isinstance(unit.get("occupied"), bool):
                        raise RuntimeError(f"Registro de unidade inválido em {field}[{slot}], jogador {player_id}.")
                    trait_names = unit.get("trait_names")
                    if (
                        not isinstance(trait_names, list)
                        or any(not isinstance(trait, str) or not trait for trait in trait_names)
                        or len(trait_names) != len(set(trait_names))
                    ):
                        raise RuntimeError("Unidade contém trait_names inválido ou duplicado.")
                    if not unit["occupied"] and trait_names:
                        raise RuntimeError("Slot vazio não pode declarar trait_names.")
                    if unit["occupied"]:
                        if not isinstance(unit.get("champion_id"), str) or not unit["champion_id"]:
                            raise RuntimeError("Unidade ocupada sem champion_id nativo.")
                        if not isinstance(unit.get("uuid"), str) or not unit["uuid"]:
                            raise RuntimeError("Unidade ocupada sem UUID nativo.")
                        if unit["uuid"] in seen_unit_uuids:
                            raise RuntimeError("UUID de UnitInstance duplicado entre owners/slots ativos.")
                        seen_unit_uuids.add(unit["uuid"])
                        star, cost, items = unit.get("star"), unit.get("cost"), unit.get("items")
                        if isinstance(star, bool) or not isinstance(star, int) or not 1 <= star <= 3:
                            raise RuntimeError("Unidade ocupada com nível de estrela inválido.")
                        if isinstance(cost, bool) or not isinstance(cost, int) or cost < 0:
                            raise RuntimeError("Unidade ocupada com custo de catálogo inválido.")
                        if not isinstance(items, list) or any(not isinstance(item, str) for item in items):
                            raise RuntimeError("Lista de itens da unidade inválida.")
                        role = unit.get("role")
                        if isinstance(role, bool) or not isinstance(role, int) or not 0 <= role <= 4:
                            raise RuntimeError("Unidade ocupada com role de alvo inválido.")
                        for stat_field in (
                            "attack_damage", "attack_speed", "max_health", "armor", "magic_resist"
                        ):
                            stat_value = unit.get(stat_field)
                            if (
                                isinstance(stat_value, bool)
                                or not isinstance(stat_value, (int, float))
                                or not np.isfinite(float(stat_value))
                                or float(stat_value) < 0.0
                            ):
                                raise RuntimeError(f"Perfil de alvo nativo inválido: {stat_field}.")
            offer_revisions = player.get("shop_offer_revisions")
            if (not isinstance(offer_revisions, list) or len(offer_revisions) != expected_slots["shop"] or any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in offer_revisions)):
                raise RuntimeError(f"Snapshot do jogador {player_id} contém revisões de oferta inválidas.")
            for slot, offer in enumerate(player["shop"]):
                if offer["occupied"] and offer_revisions[slot] == 0:
                    raise RuntimeError("Oferta ocupada sem revisão nativa de identidade.")
            pending_flag = player.get("pending_anvil")
            pending_sequence = player.get("pending_anvil_sequence")
            pending_kind = player.get("pending_anvil_kind")
            if (
                not isinstance(pending_flag, bool)
                or isinstance(pending_sequence, bool)
                or not isinstance(pending_sequence, int)
                or pending_sequence < 0
                or isinstance(pending_kind, bool)
                or not isinstance(pending_kind, int)
            ):
                raise RuntimeError(f"Snapshot do jogador {player_id} contém identidade de bigorna inválida.")
            if pending_flag and (
                pending_sequence == 0 or pending_kind not in (0, 1)
                or not player.get("pending_anvil_options")
            ):
                raise RuntimeError("Bigorna pendente sem sequência, tipo ou opções válidas.")
            if not pending_flag and (pending_sequence != 0 or pending_kind != -1 or player.get("pending_anvil_options")):
                raise RuntimeError("Identidade de bigorna presente sem escolha pendente.")
            action_count = player.get("actions_taken_this_round")
            move_ages = player.get("board_move_age")
            if isinstance(action_count, bool) or not isinstance(action_count, int) or action_count < 0:
                raise RuntimeError("Snapshot estruturado contém actions_taken_this_round inválido.")
            if (
                not isinstance(move_ages, (list, tuple))
                or len(move_ages) != 28
                or any(isinstance(age, bool) or not isinstance(age, int) or age < 0 for age in move_ages)
            ):
                raise RuntimeError("Snapshot estruturado contém board_move_age inválido.")
            for field in ("item_components", "item_inventory", "item_component_catalog", "pending_anvil_options"):
                values = player.get(field)
                if not isinstance(values, list) or any(not isinstance(item, str) for item in values):
                    raise RuntimeError(f"Campo estruturado {field} inválido para jogador {player_id}.")
            # Dict-backed fixtures have no native producer boundary, so keep
            # their defensive Python validation here. For a pinned native
            # snapshot, the semantic projection is the single authority for
            # item-feature shape, finiteness and [0, 1] checks before PPO use.
            # Avoid allocating six temporary NumPy arrays here only to repeat
            # those checks during project_native_player_state().
            if not isinstance(value, _NativeSnapshotMapping):
                semantic_item_shapes = {
                    "item_component_features": (10,),
                    "item_inventory_features": (9, 17),
                    "item_recipe_features": (100, 17),
                    "item_inventory_target_fit": (9, 37),
                    "item_recipe_target_fit": (100, 37),
                    "pending_anvil_option_features": (9, 11),
                }
                for field, expected_shape in semantic_item_shapes.items():
                    try:
                        values = np.asarray(player.get(field), dtype=np.float32)
                    except (TypeError, ValueError) as exc:
                        raise RuntimeError(f"Snapshot estruturado contém {field} inválido.") from exc
                    if values.shape != expected_shape or not np.isfinite(values).all():
                        raise RuntimeError(f"Snapshot estruturado contém {field} com shape/valores inválidos.")
            for field in ("item_component_counts", "item_inventory_counts"):
                rows = player.get(field)
                if not isinstance(rows, list): raise RuntimeError(f"Snapshot estruturado sem {field}.")
                seen = set()
                for row in rows:
                    if (not isinstance(row, dict) or not isinstance(row.get("catalog_id"), str) or not row["catalog_id"] or row["catalog_id"] in seen or isinstance(row.get("count"), bool) or not isinstance(row.get("count"), int) or row["count"] <= 0): raise RuntimeError(f"Snapshot estruturado contém {field} inválido.")
                    seen.add(row["catalog_id"])
            equipped = player.get("equipped_items")
            if not isinstance(equipped, list): raise RuntimeError("Snapshot estruturado sem equipped_items.")
            for row in equipped:
                if (not isinstance(row, dict) or not isinstance(row.get("unit_uuid"), str) or not row["unit_uuid"] or row.get("location") not in ("board", "bench") or isinstance(row.get("slot"), bool) or not isinstance(row.get("slot"), int) or not 0 <= row["slot"] < (28 if row["location"] == "board" else 9) or not isinstance(row.get("catalog_id"), str) or not row["catalog_id"]): raise RuntimeError("Snapshot estruturado contém equipped_items inválido.")
            retired_flag = player.get("item_ownership_retired")
            if not isinstance(retired_flag, bool):
                raise RuntimeError("Snapshot estruturado contém item_ownership_retired inválido.")
            retired_count_fields = ("retired_item_component_counts", "retired_item_inventory_counts")
            for field in retired_count_fields:
                rows = player.get(field)
                if not isinstance(rows, list):
                    raise RuntimeError(f"Snapshot estruturado sem {field}.")
                seen = set()
                for row in rows:
                    if (not isinstance(row, dict) or not isinstance(row.get("catalog_id"), str) or not row["catalog_id"] or row["catalog_id"] in seen or isinstance(row.get("count"), bool) or not isinstance(row.get("count"), int) or row["count"] <= 0):
                        raise RuntimeError(f"Snapshot estruturado contém {field} inválido.")
                    seen.add(row["catalog_id"])
            retired_equipped = player.get("retired_equipped_item_counts")
            if not isinstance(retired_equipped, list):
                raise RuntimeError("Snapshot estruturado sem retired_equipped_item_counts.")
            retired_equipped_seen = set()
            for row in retired_equipped:
                key = (row.get("unit_uuid"), row.get("catalog_id")) if isinstance(row, dict) else None
                if (not isinstance(row, dict) or not isinstance(row.get("unit_uuid"), str) or not row["unit_uuid"] or not isinstance(row.get("catalog_id"), str) or not row["catalog_id"] or key in retired_equipped_seen or isinstance(row.get("count"), bool) or not isinstance(row.get("count"), int) or row["count"] <= 0):
                    raise RuntimeError("Snapshot estruturado contém retired_equipped_item_counts inválido.")
                retired_equipped_seen.add(key)
            retired_anvils = player.get("retired_pending_anvils")
            if not isinstance(retired_anvils, list):
                raise RuntimeError("Snapshot estruturado sem retired_pending_anvils.")
            retired_anvil_sequences = set()
            for row in retired_anvils:
                if (not isinstance(row, dict) or isinstance(row.get("sequence"), bool) or not isinstance(row.get("sequence"), int) or row["sequence"] <= 0 or row["sequence"] in retired_anvil_sequences or isinstance(row.get("kind"), bool) or row.get("kind") not in (0, 1) or not isinstance(row.get("options"), list) or not row["options"] or any(not isinstance(option, str) or not option for option in row["options"])):
                    raise RuntimeError("Snapshot estruturado contém retired_pending_anvils inválido.")
                retired_anvil_sequences.add(row["sequence"])
            strategic = player.get("strategic_state")
            if not isinstance(strategic, dict):
                raise RuntimeError("Snapshot estruturado sem strategic_state dos owners nativos.")
            strategic_version = strategic.get("contract_version")
            if (
                strategic.get("contract_id") != "tft.strategic-owner-observation"
                or isinstance(strategic_version, bool)
                or not isinstance(strategic_version, int)
                or strategic_version != 3
                or strategic.get("producer") != "TFTEngine::get_audit_snapshot"
                or strategic.get("source_namespace") != "tft.engine.strategic-owners"
            ):
                raise RuntimeError("Contrato de strategic_state incompatível.")
            for field, expected in (
                ("episode_id", episode_id),
                ("player_decision_sequence", player_sequences[player_id]),
                ("player_id", player_id),
                ("round", value.get("round")),
            ):
                actual = strategic.get(field)
                if isinstance(actual, bool) or not isinstance(actual, int) or actual != expected:
                    raise RuntimeError(f"Strategic owner snapshot diverge em {field}.")
            strategic_context_sequence = strategic.get("strategic_context_sequence")
            if (
                isinstance(strategic_context_sequence, bool)
                or not isinstance(strategic_context_sequence, int)
                or strategic_context_sequence < 0
            ):
                raise RuntimeError("Strategic owner snapshot inválido em strategic_context_sequence.")
            valid_fields = (
                "active_composition_valid", "direction_valid",
                "pivot_candidate_valid", "opportunity_cost_available",
            )
            if any(not isinstance(strategic.get(field), bool) for field in valid_fields):
                raise RuntimeError("Validade dos strategic owners deve ser booleana.")
            def validate_ids(field):
                ids = strategic.get(field)
                if (
                    not isinstance(ids, list)
                    or any(isinstance(item, bool) or not isinstance(item, int) or item < 0 for item in ids)
                    or len(ids) != len(set(ids))
                ):
                    raise RuntimeError(f"Strategic owner contém IDs inválidos em {field}.")
                return set(ids)
            active_ids = validate_ids("active_unit_ids")
            core_ids = validate_ids("active_core_unit_ids")
            direction_ids = validate_ids("direction_reference_unit_ids")
            pivot_ids = validate_ids("pivot_reference_unit_ids")
            progress_rows = strategic.get("unit_copy_progress")
            if not isinstance(progress_rows, list):
                raise RuntimeError("Strategic owner snapshot sem unit_copy_progress nativo.")
            progress_ids = set()
            for row in progress_rows:
                if not isinstance(row, dict):
                    raise RuntimeError("unit_copy_progress contém registro inválido.")
                champion_id = row.get("champion_internal_id")
                copies = row.get("owned_copy_equivalent")
                toward_next = row.get("copies_toward_next_star")
                highest_star = row.get("highest_star")
                if (
                    isinstance(champion_id, bool) or not isinstance(champion_id, int) or champion_id < 0
                    or champion_id in progress_ids
                    or isinstance(copies, bool) or not isinstance(copies, int) or not 1 <= copies <= 9
                    or isinstance(toward_next, bool) or not isinstance(toward_next, int) or not 0 <= toward_next <= 2
                    or isinstance(highest_star, bool) or not isinstance(highest_star, int) or not 1 <= highest_star <= 3
                    or (highest_star == 3 and toward_next != 0)
                ):
                    raise RuntimeError("unit_copy_progress contém valores nativos inválidos.")
                progress_ids.add(champion_id)
            if not core_ids.issubset(active_ids):
                raise RuntimeError("Core units devem pertencer à composição ativa.")
            if not strategic["active_composition_valid"] and (active_ids or core_ids):
                raise RuntimeError("Composição inválida não pode publicar membros.")
            if strategic["active_composition_valid"] and (
                not isinstance(strategic.get("active_composition_id"), str)
                or not strategic["active_composition_id"]
                or isinstance(strategic.get("active_composition_version"), bool)
                or not isinstance(strategic.get("active_composition_version"), int)
                or strategic["active_composition_version"] <= 0
            ):
                raise RuntimeError("Identidade/versão da composição ativa inválida.")
            if not strategic["direction_valid"] and direction_ids:
                raise RuntimeError("Direção inválida não pode publicar referências.")
            if strategic["direction_valid"] and (
                not isinstance(strategic.get("direction_identity"), str)
                or not strategic["direction_identity"]
            ):
                raise RuntimeError("Identidade da direção nativa inválida.")
            if not strategic["pivot_candidate_valid"] and pivot_ids:
                raise RuntimeError("Pivot inválido não pode publicar referências.")
            if strategic["pivot_candidate_valid"] and (
                not isinstance(strategic.get("pivot_candidate_identity"), str)
                or not strategic["pivot_candidate_identity"]
                or not isinstance(strategic.get("pivot_target_composition_identity"), str)
                or not strategic["pivot_target_composition_identity"]
                or isinstance(strategic.get("pivot_source_composition_version"), bool)
                or not isinstance(strategic.get("pivot_source_composition_version"), int)
                or strategic["pivot_source_composition_version"] <= 0
            ):
                raise RuntimeError("Identidade/versão do pivot nativo inválida.")
            opportunity_rows = strategic.get("opportunity_costs")
            if not isinstance(opportunity_rows, list):
                raise RuntimeError("Strategic owner snapshot sem opportunity_costs nativo.")
            opportunity_ids = set()
            for row in opportunity_rows:
                if not isinstance(row, dict):
                    raise RuntimeError("opportunity_costs contém registro inválido.")
                champion_id = row.get("champion_internal_id")
                amount = row.get("value")
                uncertainty = row.get("uncertainty")
                horizon = row.get("horizon_rounds")
                source = row.get("source")
                value_basis = row.get("value_basis")
                forgone = row.get("forgone_candidate_id")
                if (
                    isinstance(champion_id, bool) or not isinstance(champion_id, int) or champion_id < 0
                    or champion_id in opportunity_ids
                    or isinstance(amount, bool) or not isinstance(amount, (int, float)) or not np.isfinite(amount) or amount < 0
                    or isinstance(uncertainty, bool) or not isinstance(uncertainty, (int, float)) or not np.isfinite(uncertainty) or not 0 <= uncertainty < 1
                    or isinstance(horizon, bool) or not isinstance(horizon, int) or horizon <= 0
                    or source != "same_snapshot_competing_alternative.v1"
                    or value_basis not in ("contextual_action_score.v1", "native_board_contribution.v1")
                    or not isinstance(forgone, str) or not forgone
                ):
                    raise RuntimeError("opportunity_costs contém evidência nativa inválida.")
                opportunity_ids.add(champion_id)
            if strategic["opportunity_cost_available"] != bool(opportunity_ids):
                raise RuntimeError("Disponibilidade de opportunity cost diverge das evidências nativas.")

            planner_valid = strategic.get("planner_outputs_valid")
            strategic_failed = strategic.get("strategic_refresh_failed")
            failure_reason = strategic.get("strategic_refresh_failure_reason")
            planner_sequence = strategic.get("planner_output_sequence")
            if (
                not isinstance(planner_valid, bool)
                or not isinstance(strategic_failed, bool)
                or not isinstance(failure_reason, str)
                or strategic_failed != bool(failure_reason)
                or isinstance(planner_sequence, bool)
                or not isinstance(planner_sequence, int)
                or planner_sequence < 0
            ):
                raise RuntimeError("Estado de planner/refresh estratégico inválido.")
            priority_rows = strategic.get("unit_priorities")
            lineup_fields = (
                "lineup_selected_unit_ids", "lineup_entry_unit_ids",
                "lineup_exit_unit_ids", "lineup_deferred_unit_ids",
            )
            if not isinstance(priority_rows, list):
                raise RuntimeError("Strategic owner snapshot sem unit_priorities nativo.")
            lineup_ids = {}
            for field in lineup_fields:
                values = strategic.get(field)
                if (
                    not isinstance(values, list)
                    or any(isinstance(item, bool) or not isinstance(item, int) or item < 0 for item in values)
                    or len(values) != len(set(values))
                ):
                    raise RuntimeError(f"Strategic owner contém IDs inválidos em {field}.")
                lineup_ids[field] = set(values)
            if planner_valid:
                if planner_sequence != strategic_context_sequence:
                    raise RuntimeError("Saídas do planner não pertencem à sequência estratégica atual.")
                priority_ids = set()
                for row in priority_rows:
                    if not isinstance(row, dict):
                        raise RuntimeError("unit_priorities contém registro inválido.")
                    champion_id = row.get("champion_internal_id")
                    priority = row.get("priority")
                    intent = row.get("intent")
                    confidence = row.get("confidence")
                    target_star = row.get("target_star")
                    sale_restricted = row.get("sale_restricted")
                    if (
                        isinstance(champion_id, bool) or not isinstance(champion_id, int) or champion_id < 0
                        or champion_id in priority_ids
                        or isinstance(priority, bool) or not isinstance(priority, int) or priority < 0
                        or isinstance(intent, bool) or not isinstance(intent, int) or not 0 <= intent <= 6
                        or isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not np.isfinite(confidence) or not 0 <= confidence <= 1
                        or isinstance(target_star, bool) or not isinstance(target_star, int) or not 0 <= target_star <= 3
                        or not isinstance(sale_restricted, bool)
                    ):
                        raise RuntimeError("unit_priorities contém evidência inválida ou duplicada.")
                    priority_ids.add(champion_id)
            elif priority_rows or any(lineup_ids.values()):
                raise RuntimeError("Saídas indisponíveis do planner não podem publicar prioridades ou lineup.")

            retired_has_evidence = any(player[field] for field in retired_count_fields) or bool(retired_equipped) or bool(retired_anvils)
            active_has_ownership = bool(player["item_components"] or player["item_inventory"] or player["item_component_counts"] or player["item_inventory_counts"] or equipped or pending_flag or pending_sequence or player["pending_anvil_options"])
            if retired_flag and active_has_ownership:
                raise RuntimeError("Ownership ativo presente após aposentadoria terminal dos itens.")
            if not retired_flag and retired_has_evidence:
                raise RuntimeError("Evidência de aposentadoria presente sem estado terminal.")
        # The pybind handle pins the immutable native value. Its Mapping view
        # materializes semantic fields on demand and defers combat event rows;
        # deepcopy creates an independent Python cache over the same pinned value.
        return value

    @staticmethod
    def _copy_player_decision_sequences(values):
        if not isinstance(values, (list, tuple, np.ndarray)) or len(values) != CppTFTLobbyWrapper.PLAYERS_PER_LOBBY:
            raise RuntimeError("Snapshot nativo sem as oito sequências individuais de decisão esperadas.")
        sequences = []
        for player_id, value in enumerate(values):
            if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or value < 0:
                raise RuntimeError(
                    f"Sequência de decisão inválida para o jogador {player_id}: {value!r}."
                )
            sequences.append(int(value))
        return sequences

    def _consume_reset_result(self, result):
        # Invalidate the previous pair before asking native code for a new
        # snapshot. If reset raises, callers must not reuse old observations'
        # masks or identity as though they belonged to the attempted reset.
        self._last_action_masks = None
        self._last_snapshot_metadata = None
        native_snapshot = result.get("native_state_snapshot")
        if native_snapshot is not None and not isinstance(native_snapshot, Mapping):
            native_snapshot = _NativeSnapshotMapping(native_snapshot)
            result["native_state_snapshot"] = native_snapshot
        self._last_dones = np.zeros(self.PLAYERS_PER_LOBBY, dtype=np.bool_)
        self._players = [
            SimpleNamespace(player_id=i, alive=True, eliminated=False)
            for i in range(self.PLAYERS_PER_LOBBY)
        ]
        self._last_action_masks = self._validate_action_masks_payload(result.get("action_masks"))
        self._last_snapshot_metadata = {
            "engine_instance_id": str(result["engine_instance_id"]),
            "episode_id": int(result["episode_id"]),
            "decision_sequence": int(result["decision_sequence"]),
            "player_decision_sequences": self._copy_player_decision_sequences(result.get("player_decision_sequences")),
            "round": int(result.get("native_state_snapshot", {}).get("round", 0)),
            "stage": 1,
            "snapshot_kind": "reset",
        }
        self._last_snapshot_metadata["player_identity_envelopes"] = build_player_identity_envelopes(
            self._last_snapshot_metadata
        )
        self._last_snapshot_metadata["native_state_snapshot"] = self._copy_native_state_snapshot(
            result.get("native_state_snapshot"), self._last_snapshot_metadata
        )
        self._reward_audit_ledger.reset(
            self._last_snapshot_metadata["engine_instance_id"],
            self._last_snapshot_metadata["episode_id"],
        )
        return np.asarray(result["observations"], dtype=np.float32)

    def _invalidate_current_snapshot(self):
        """Prevent consumers from reusing masks/metadata after a reset attempt."""
        self._last_action_masks = None
        self._last_snapshot_metadata = None
        self._last_dones = np.zeros(self.PLAYERS_PER_LOBBY, dtype=np.bool_)

    def reset(self, seed: int | None = None):
        self._invalidate_current_snapshot()
        return self._consume_reset_result(self._engine.reset(seed))

    def _prepare_batch_step(self, actions):
        """Execute one lobby action batch, optionally gated by a wall-clock preparation timer."""
        if len(actions) != self.PLAYERS_PER_LOBBY:
            raise ValueError(
                f"Esperava {self.PLAYERS_PER_LOBBY} ações; recebi {len(actions)}."
            )

        native_actions = [self._normalize_action(action) for action in actions]
        # Preserve the exact observation snapshot consumed by this action batch.
        # Clear the public cache before stepping so a failed native step cannot
        # accidentally authorize a second decision against stale state.
        # Published metadata is immutable for the lifetime of its decision.
        # Keep a local reference while replacing the wrapper's current snapshot;
        # the previous native payload is already Python-owned and won't be reused
        # or overwritten by the next C++ step.
        source_decision_snapshot = self._last_snapshot_metadata
        self._last_action_masks = None
        self._last_snapshot_metadata = None
        return native_actions, source_decision_snapshot

    def _consume_step_result(self, result, source_decision_snapshot):
        native_snapshot = result.get("native_state_snapshot")
        if native_snapshot is not None and not isinstance(native_snapshot, Mapping):
            native_snapshot = _NativeSnapshotMapping(native_snapshot)
            result["native_state_snapshot"] = native_snapshot

        observations = np.asarray(result["observations"], dtype=np.float32)
        rewards = np.asarray(result["rewards"], dtype=np.float32)
        self._last_dones = np.asarray(result["dones"], dtype=np.bool_)
        self._last_action_masks = self._validate_action_masks_payload(result.get("action_masks"))
        self._last_snapshot_metadata = {
            "engine_instance_id": str(result["engine_instance_id"]),
            "episode_id": int(result["episode_id"]),
            "decision_sequence": int(result["decision_sequence"]),
            "player_decision_sequences": self._copy_player_decision_sequences(result.get("player_decision_sequences")),
            "round": int(result.get("round", 0)),
            "stage": int(result.get("stage", 1)),
            "snapshot_kind": "step",
        }
        self._last_snapshot_metadata["player_identity_envelopes"] = build_player_identity_envelopes(
            self._last_snapshot_metadata
        )
        self._last_snapshot_metadata["native_state_snapshot"] = self._copy_native_state_snapshot(
            result.get("native_state_snapshot"), self._last_snapshot_metadata
        )
        player_info = result.get("players", [])
        self._players = [
            SimpleNamespace(
                player_id=int(player.get("player_id", idx)),
                alive=bool(player.get("alive", False)),
                eliminated=bool(player.get("eliminated", False)),
            )
            for idx, player in enumerate(player_info)
        ]

        # Reward component arrays are mandatory for the audit contract. Falling
        # back to the combined reward would fabricate component provenance.
        if not all(key in result for key in (
            "action_rewards", "combat_rewards", "placement_rewards",
            "action_traces", "players",
        )):
            raise RuntimeError(
                "Native StepResult sem os componentes/proveniência exigidos "
                "pelo RewardAuditLedger."
            )
        action_rewards = np.asarray(result["action_rewards"], dtype=np.float32)
        combat_rewards = np.asarray(result["combat_rewards"], dtype=np.float32)
        placement_rewards = np.asarray(result["placement_rewards"], dtype=np.float32)
        action_traces = [dict(item) for item in result["action_traces"]]
        if not isinstance(source_decision_snapshot, Mapping) or not isinstance(
            source_decision_snapshot.get("native_state_snapshot"), Mapping
        ):
            raise RuntimeError(
                "Não há snapshot nativo pré-ação para atribuir consequências factuais."
            )
        # The Engine emits factual outcomes at the action handler boundary.
        # Production must not reconstruct them by diffing generic snapshots.
        action_outcome_events = result.get("action_outcome_events")
        if not isinstance(action_outcome_events, (list, tuple)) or len(action_outcome_events) != self.PLAYERS_PER_LOBBY:
            raise RuntimeError("Native StepResult sem os oito ActionOutcomeEvent esperados.")
        for player_id, event in enumerate(action_outcome_events):
            if not isinstance(event, Mapping):
                raise RuntimeError(f"ActionOutcomeEvent inválido para player_id={player_id}.")
            if (
                event.get("contract_id") != "tft.engine.action-outcome-event"
                or int(event.get("contract_version", 0)) != 1
                or event.get("engine_instance_id") != self._last_snapshot_metadata["engine_instance_id"]
                or int(event.get("episode_id", -1)) != self._last_snapshot_metadata["episode_id"]
                or int(event.get("player_id", -1)) != player_id
                or int(event.get("outcome_player_decision_sequence", -1)) != self._last_snapshot_metadata["player_decision_sequences"][player_id]
            ):
                raise RuntimeError(f"ActionOutcomeEvent sem identidade/sequência alinhada para player_id={player_id}.")
        action_outcome_events = [dict(event) for event in action_outcome_events]
        reward_audit = self._reward_audit_ledger.build_record(
            rewards=rewards,
            action_rewards=action_rewards,
            combat_rewards=combat_rewards,
            placement_rewards=placement_rewards,
            action_traces=action_traces,
            action_outcome_events=action_outcome_events,
            players=player_info,
            decision_snapshot=self._last_snapshot_metadata,
            source_decision_snapshot=source_decision_snapshot,
        )
        action_context = {
            "contract_id": str(result.get("action_context_contract_id", "")),
            "contract_version": int(result.get("action_context_contract_version", 0)),
            "engine_instance_id": self._last_snapshot_metadata["engine_instance_id"],
            "episode_id": self._last_snapshot_metadata["episode_id"],
            "decision_sequence": self._last_snapshot_metadata["decision_sequence"],
            "player_decision_sequences": list(self._last_snapshot_metadata["player_decision_sequences"]),
            "action_mask_contract_id": str(result.get("action_mask_contract_id", "")),
            "action_mask_contract_version": int(result.get("action_mask_contract_version", 0)),
            "action_mask_layout": str(result.get("action_mask_layout", "")),
            "action_masks": self._last_action_masks,
            "action_traces": action_traces,
            "action_outcome_events": action_outcome_events,
        }
        if action_context["contract_id"] != "tft.engine.action-context" or action_context["contract_version"] != 1:
            raise RuntimeError("Native ActionContext ausente ou incompatível.")
        info = {
            "players": player_info,
            "action_context": action_context,
            "action_trace": action_traces,
            "decision_snapshot": copy.deepcopy(self._last_snapshot_metadata),
            "round": int(result.get("round", 0)),
            "stage": int(result.get("stage", 1)),
            "finished": bool(result.get("lobby_done", False)),
            "lobby_done": bool(result.get("lobby_done", False)),
            "events": list(result.get("events", [])),
            "action_rewards": action_rewards,
            "combat_rewards": combat_rewards,
            "placement_rewards": placement_rewards,
            "reward_audit": reward_audit,
            "action_outcome_events": action_outcome_events,
        }
        return observations, rewards, bool(result.get("lobby_done", False)), info

    def step(self, actions, *, timer_enabled: bool = False, timer_expired: bool = False):
        native_actions, source_snapshot = self._prepare_batch_step(actions)
        result = self._engine.step(native_actions, bool(timer_enabled), bool(timer_expired))
        return self._consume_step_result(result, source_snapshot)

    def adapt_opgg_compositions(self, catalog):
        """Map OP.GG unit keys through the native engine's loaded catalog."""
        import json
        raw = json.dumps(catalog, ensure_ascii=False, separators=(",", ":"))
        return json.loads(self._engine.adapt_opgg_compositions_json(raw))

    def get_champion_id_map(self):
        """Return apiName -> internal_id from the catalog loaded by native C++."""
        return dict(self._engine.get_champion_id_map())

    @classmethod
    def _validate_action_masks_payload(cls, masks):
        """Validate the native mask boundary without expanding packed buffers."""
        if isinstance(masks, np.ndarray):
            expected = (cls.PLAYERS_PER_LOBBY, cls._PACKED_ACTION_MASK_WIDTH)
            if masks.dtype != np.bool_ or masks.shape != expected:
                raise RuntimeError(
                    "Buffer compacto de action masks inválido: "
                    f"dtype={masks.dtype}, shape={masks.shape}, esperado bool{expected}."
                )
            return masks
        # Keep legacy fixtures/adapters supported through the structured path.
        cls._copy_action_masks(masks)
        return masks

    def _get_action_masks(self, *, detach_arrays):
        if self._last_action_masks is None:
            raise RuntimeError("Execute reset() antes de solicitar action masks.")

        masks = self._copy_action_masks(
            self._last_action_masks, detach_arrays=detach_arrays
        )
        if os.environ.get("TFT_ABLATE_ITEM_ACTIONS") == "1":
            # Evaluation-only ablation: suppress item equip/transfer and craft
            # actions. Copy only the type mask that is actually modified.
            for player_idx, player_masks in enumerate(masks):
                type_mask = (
                    player_masks["type_mask"]
                    if detach_arrays
                    else player_masks["type_mask"].copy()
                )
                legal_types = np.flatnonzero(type_mask)
                mandatory_anvil_choice = (
                    len(legal_types) == 1 and int(legal_types[0]) == 7
                )
                if not mandatory_anvil_choice:
                    type_mask[7] = False
                    type_mask[8] = False
                if not bool(type_mask.any()):
                    raise RuntimeError(
                        "A ablação de ações de item removeu todas as ações legais "
                        f"do snapshot nativo para o jogador {player_idx}; "
                        "nenhuma ação substituta será inventada."
                    )
                player_masks["type_mask"] = type_mask

        if not detach_arrays:
            # The pybind arrays are Python-owned snapshots. Keep their buffers
            # alive through the returned references and forbid consumer mutation;
            # a later step replaces the wrapper's references, never overwrites
            # these arrays.
            for player_masks in masks:
                for value in player_masks.values():
                    value.flags.writeable = False
        return masks

    def get_action_masks(self):
        """Return detached masks for callers that may retain or mutate them."""
        return self._get_action_masks(detach_arrays=True)

    def get_action_masks_for_training(self):
        """Compatibility mapping API for callers outside the optimized Trainer path."""
        return self._get_action_masks(detach_arrays=False)

    def get_packed_action_masks_for_training(self):
        """Borrow the contiguous native mask matrix without rebuilding player dictionaries."""
        if self._last_action_masks is None:
            raise RuntimeError("Execute reset() antes de solicitar action masks.")

        packed = self._last_action_masks
        if not isinstance(packed, np.ndarray):
            # Legacy fixtures/engines remain supported, but production native
            # results use the packed branch and never materialize these mappings.
            players = self._copy_action_masks(packed, detach_arrays=False)
            packed = np.empty(
                (self.PLAYERS_PER_LOBBY, self._PACKED_ACTION_MASK_WIDTH),
                dtype=np.bool_,
            )
            for player_index, player_masks in enumerate(players):
                offset = 0
                for key, shape in self._PACKED_ACTION_MASK_LAYOUT:
                    width = int(np.prod(shape))
                    raw_mask = np.asarray(player_masks[key])
                    if raw_mask.shape != shape:
                        raise RuntimeError(
                            f"Máscara legada '{key}' inválida para jogador {player_index}: "
                            f"shape={raw_mask.shape}, esperado={shape}."
                        )
                    if not (
                        np.issubdtype(raw_mask.dtype, np.bool_)
                        or np.issubdtype(raw_mask.dtype, np.number)
                    ):
                        raise TypeError(f"Máscara legada '{key}' possui dtype inválido.")
                    if not np.issubdtype(raw_mask.dtype, np.bool_):
                        if not np.all(np.isfinite(raw_mask)) or not np.all(
                            (raw_mask == 0) | (raw_mask == 1)
                        ):
                            raise ValueError(
                                f"Máscara legada '{key}' deve conter somente valores finitos 0/1."
                            )
                    packed[player_index, offset:offset + width] = raw_mask.astype(
                        np.bool_, copy=False
                    ).reshape(-1)
                    offset += width

        expected_shape = (
            self.PLAYERS_PER_LOBBY,
            self._PACKED_ACTION_MASK_WIDTH,
        )
        if packed.dtype != np.bool_ or packed.shape != expected_shape:
            raise RuntimeError(
                "Buffer compacto de action masks inválido: "
                f"dtype={packed.dtype}, shape={packed.shape}, esperado bool{expected_shape}."
            )

        if os.environ.get("TFT_ABLATE_ITEM_ACTIONS") == "1":
            # The first nine packed values are the type mask. Copy only when
            # this explicit evaluation ablation changes those values.
            packed = packed.copy()
            for player_idx in range(self.PLAYERS_PER_LOBBY):
                type_mask = packed[player_idx, :9]
                legal_types = np.flatnonzero(type_mask)
                mandatory_anvil_choice = (
                    len(legal_types) == 1 and int(legal_types[0]) == 7
                )
                if not mandatory_anvil_choice:
                    type_mask[7] = False
                    type_mask[8] = False
                if not bool(type_mask.any()):
                    raise RuntimeError(
                        "A ablação de ações de item removeu todas as ações legais "
                        f"do snapshot nativo para o jogador {player_idx}; "
                        "nenhuma ação substituta será inventada."
                    )

        packed.flags.writeable = False
        return packed

    def get_snapshot_metadata(self):
        """Return non-neural metadata for the exact observation/mask snapshot."""
        if self._last_snapshot_metadata is None:
            raise RuntimeError("Execute reset() antes de solicitar snapshot metadata.")
        return copy.deepcopy(self._last_snapshot_metadata)

    def get_anti_loop_metrics(self):
        return dict(self._engine.get_anti_loop_metrics())


    def close(self):
        if not self._closed:
            if self._owns_engine:
                self._engine.close()
            self._closed = True

    def get_public_state(self):
        """Read-only public lobby snapshot exposed by the native engine."""
        return self._engine.get_public_state()

    def get_composition_diagnostics_jsonl(self):
        return list(self._engine.get_composition_diagnostics_jsonl())

    def set_strategic_direction_pivot_audit_path(self, path):
        """Configure the session-local unified strategic Shadow JSONL sidecar."""
        self._engine.set_strategic_direction_pivot_audit_path(str(path))

    def get_audit_snapshot(self):
        """Read-only board/bench/shop and mask snapshot for the observer."""
        return self._engine.get_audit_snapshot()
