"""Converte o estado dos managers Python para o PlayerState nativo.

Este módulo é responsável somente pela conversão e validação dos dados.
Não executa ações, não gera máscaras e não modifica o estado do jogo.
"""

from __future__ import annotations

import importlib
from typing import Any

from config.GameConfig import GameConfig


BOARD_SIZE = 28
BENCH_SIZE = 9
SHOP_SIZE = 5

INT32_MAX = (2**31) - 1
INT64_MIN = -(2**63)
INT64_MAX = (2**63) - 1
UINT8_MAX = (2**8) - 1


def _as_int(value: Any, field: str) -> int:
    """Converte um valor inteiro sem aceitar bool ou truncar floats."""
    if isinstance(value, bool):
        raise ValueError(f"{field}: valor booleano não é permitido.")

    if isinstance(value, float) and not value.is_integer():
        raise ValueError(f"{field}: era esperado um número inteiro.")

    try:
        converted = int(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(
            f"{field}: valor inteiro inválido: {value!r}."
        ) from exc

    return converted


def _as_int_in_range(
    value: Any,
    field: str,
    minimum: int,
    maximum: int,
) -> int:
    """Converte e valida os limites de um inteiro."""
    converted = _as_int(value, field)

    if not minimum <= converted <= maximum:
        raise ValueError(
            f"{field}: {converted} fora do intervalo "
            f"permitido [{minimum}, {maximum}]."
        )

    return converted


def _read_slots(
    manager: Any,
    attribute: str,
    expected_size: int,
    field: str,
) -> list:
    """Lê uma lista de slots e exige a dimensão esperada."""
    slots = getattr(manager, attribute, None)

    if not isinstance(slots, (list, tuple)):
        raise ValueError(
            f"{field}: esperado list ou tuple; "
            f"recebido {type(slots).__name__}."
        )

    if len(slots) != expected_size:
        raise ValueError(
            f"{field}: dimensão inválida. "
            f"Esperado {expected_size}, recebido {len(slots)}."
        )

    return list(slots)


def _create_unit_snapshot(
    native_module: Any,
    unit: Any,
    field: str,
    *,
    is_shop_unit: bool = False,
):
    """Converte um dicionário de unidade para UnitSnapshot."""
    if unit is None:
        return None

    if not isinstance(unit, dict):
        raise ValueError(
            f"{field}: esperado dicionário ou None; "
            f"recebido {type(unit).__name__}."
        )

    identity = native_module.UnitIdentity()

    raw_uuid = unit.get("uuid")
    if raw_uuid is not None:
        identity.uuid = str(raw_uuid)
    else:
        raw_id = unit.get("id")

        # O tipo nativo usa int64 para IDs numéricos.
        # IDs textuais do catálogo não são convertidos artificialmente.
        if isinstance(raw_id, int) and not isinstance(raw_id, bool):
            identity.id = _as_int_in_range(
                raw_id,
                f"{field}.id",
                INT64_MIN,
                INT64_MAX,
            )

    identity.star = _as_int_in_range(
        unit.get("star", 1),
        f"{field}.star",
        1,
        UINT8_MAX,
    )

    snapshot = native_module.UnitSnapshot()
    snapshot.identity = identity

    snapshot.cost = _as_int_in_range(
        unit.get("cost", 1),
        f"{field}.cost",
        0,
        UINT8_MAX,
    )

    # O campo "available" participa da validação de compra da loja.
    # Para board e bench, o campo não interfere nas máscaras atuais.
    snapshot.available = (
        bool(unit.get("available", True))
        if is_shop_unit
        else True
    )

    return snapshot


def build_player_state(
    env: Any,
    *,
    is_alive: bool = True,
    native_module: Any | None = None,
):
    """Cria um PlayerState nativo a partir de um MiniTFTEnv.

    Args:
        env:
            Instância do ambiente que contém os managers do jogador.
        is_alive:
            Estado de vida fornecido pelo chamador. A lobby pode
            passá-lo explicitamente para refletir eliminações.
        native_module:
            Módulo decision_engine já importado. Se omitido,
            o módulo será carregado pelo importlib.

    Returns:
        Instância nativa de decision_engine.PlayerState.

    Raises:
        RuntimeError:
            Se a extensão nativa não puder ser importada.
        ValueError:
            Se os dados ou dimensões do estado forem inconsistentes.
    """
    if native_module is None:
        try:
            native_module = importlib.import_module("decision_engine")
        except ImportError as exc:
            raise RuntimeError(
                "Não foi possível importar 'decision_engine'. "
                "Compile a extensão C++ e verifique o ambiente Python."
            ) from exc

    required_managers = (
        "board_manager",
        "bench_manager",
        "shop_manager",
        "economy_manager",
    )

    for manager_name in required_managers:
        if getattr(env, manager_name, None) is None:
            raise ValueError(
                f"Não foi encontrado o manager obrigatório: "
                f"env.{manager_name}."
            )

    board = _read_slots(
        env.board_manager,
        "board",
        BOARD_SIZE,
        "board",
    )
    bench = _read_slots(
        env.bench_manager,
        "bench",
        BENCH_SIZE,
        "bench",
    )
    shop = _read_slots(
        env.shop_manager,
        "shop",
        SHOP_SIZE,
        "shop",
    )

    economy = env.economy_manager

    gold = _as_int_in_range(
        economy.gold, "economy.gold", 0, INT32_MAX
    )
    level = _as_int_in_range(
        economy.level, "economy.level", 1, INT32_MAX
    )
    xp = _as_int_in_range(
        economy.xp, "economy.xp", 0, INT32_MAX
    )

    max_level = _as_int_in_range(
        GameConfig.MAX_LEVEL,
        "GameConfig.MAX_LEVEL",
        1,
        INT32_MAX,
    )

    if level > max_level:
        raise ValueError(
            f"economy.level ({level}) não pode exceder "
            f"GameConfig.MAX_LEVEL ({max_level})."
        )

    player_id = _as_int_in_range(
        getattr(env, "player_id", 0),
        "env.player_id",
        INT64_MIN,
        INT64_MAX,
    )

    state = native_module.PlayerState()
    state.player_id = player_id
    state.is_alive = bool(is_alive)

    native_economy = native_module.EconomyState()
    native_economy.gold = gold
    native_economy.level = level
    native_economy.current_xp = xp
    native_economy.max_level = max_level
    native_economy.xp_to_next_level = _as_int_in_range(
        GameConfig.get_xp_to_next(level),
        "economy.xp_to_next_level",
        0,
        INT32_MAX,
    )
    native_economy.reroll_cost = _as_int_in_range(
        GameConfig.REROLL_COST,
        "GameConfig.REROLL_COST",
        0,
        INT32_MAX,
    )
    native_economy.xp_purchase_cost = _as_int_in_range(
        GameConfig.BUY_XP_COST,
        "GameConfig.BUY_XP_COST",
        0,
        INT32_MAX,
    )
    state.economy = native_economy

    state.board = [
        _create_unit_snapshot(
            native_module,
            unit,
            f"board[{index}]",
        )
        for index, unit in enumerate(board)
    ]

    state.bench = [
        _create_unit_snapshot(
            native_module,
            unit,
            f"bench[{index}]",
        )
        for index, unit in enumerate(bench)
    ]

    state.shop = [
        _create_unit_snapshot(
            native_module,
            unit,
            f"shop[{index}]",
            is_shop_unit=True,
        )
        for index, unit in enumerate(shop)
    ]

    return state