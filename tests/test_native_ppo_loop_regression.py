"""Integration regressions for native action masks and PPO strategy signals.

Champion identities are loaded from the active production catalog so these tests
remain valid when the TFT set changes.
"""
import json
from pathlib import Path

from cpp_lobby_env import CppTFTLobbyWrapper


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "units_gerado.json"


def _active_champion_ids(count: int = 2) -> list[str]:
    with CATALOG_PATH.open(encoding="utf-8") as source:
        catalog = json.load(source)
    ids = [
        str(unit.get("apiName", "")).strip()
        for unit in catalog
        if str(unit.get("apiName", "")).strip()
    ]
    # Preserve catalog order while avoiding duplicate identifiers.
    ids = list(dict.fromkeys(ids))
    if len(ids) < count:
        raise AssertionError(
            f"Active champion catalog needs at least {count} unique API IDs; got {len(ids)}"
        )
    return ids[:count]


def _state_signature(player):
    def slots(units):
        return tuple(
            (u.get("champion_id"), u.get("uuid"), int(u.get("star", 0)))
            if u.get("occupied") else None
            for u in units
        )
    return slots(player["board"]), slots(player["bench"])


def _move_action(source, target):
    # PPO action layout: type, shop, bench, board_target, board_source, move_target.
    return [4, 0, 0, target, source, target]


def test_native_mask_blocks_reverse_swap_and_executor_rejects_forced_reverse():
    first_champion, second_champion = _active_champion_ids(2)
    lobby = CppTFTLobbyWrapper(seed=20261022)
    try:
        lobby.reset(seed=20261022)
        native = lobby._engine

        assert native.set_player_economy_for_testing(0, 10, 3, 0)
        assert native.set_unit_for_testing(0, True, 3, first_champion, 1)
        assert native.set_unit_for_testing(0, True, 10, second_champion, 1)

        before = lobby.get_audit_snapshot()["players"][0]
        before_signature = _state_signature(before)
        forward_masks = lobby.get_action_masks()[0]
        assert bool(forward_masks["type_mask"][4])
        assert bool(forward_masks["board_move_target_masks"][3][10]), (
            "O movimento inicial deve ser elegível na máscara nativa."
        )

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = _move_action(3, 10)
        lobby.step(actions)

        after_forward = lobby.get_audit_snapshot()["players"][0]
        assert _state_signature(after_forward) != before_signature, (
            "A engine não aplicou o primeiro movimento autorizado; "
            f"before={before_signature!r}, after={_state_signature(after_forward)!r}"
        )

        reverse_masks = lobby.get_action_masks()[0]
        reverse_allowed = bool(reverse_masks["board_move_target_masks"][10][3])
        assert not reverse_allowed, (
            "A máscara C++ permitiu a reversão imediata 10->3. "
            f"mask[10][3]={int(reverse_masks['board_move_target_masks'][10][3])}; "
            f"board={_state_signature(after_forward)!r}"
        )

        # Bypass the policy mask to exercise the executor's second line of defense.
        before_forced_reverse = _state_signature(after_forward)
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = _move_action(10, 3)
        lobby.step(actions)
        after_forced_reverse = lobby.get_audit_snapshot()["players"][0]
        assert _state_signature(after_forced_reverse) == before_forced_reverse, (
            "A execução C++ aceitou uma reversão que a máscara deveria bloquear. "
            f"before={before_forced_reverse!r}, after={_state_signature(after_forced_reverse)!r}"
        )
    finally:
        lobby.close()


def test_native_composition_score_rewards_two_star_upgrade_separately():
    champion_id = _active_champion_ids(1)[0]
    lobby = CppTFTLobbyWrapper(seed=20261023)
    try:
        lobby.reset(seed=20261023)
        native = lobby._engine

        one_star = float(native.get_unit_comp_score(0, champion_id, 1))
        two_star = float(native.get_unit_comp_score(0, champion_id, 2))
        three_star = float(native.get_unit_comp_score(0, champion_id, 3))

        assert two_star > one_star, (
            f"O sinal estratégico nativo não valoriza {champion_id} 2★ acima de 1★: "
            f"1★={one_star}, 2★={two_star}"
        )
        assert three_star > two_star, (
            f"O sinal estratégico nativo não valoriza {champion_id} 3★ acima de 2★: "
            f"2★={two_star}, 3★={three_star}"
        )
    finally:
        lobby.close()
