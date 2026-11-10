from scripts.audit_native_ppo_loops import _cycle_signature


def player(gold=10, level=5):
    return {
        "board": [{"occupied": True, "uuid": "unit-1", "champion_id": "TFT_Test",
                   "star": 1, "item_ids": []}],
        "bench": [{"occupied": False}],
        "item_components": [],
        "item_inventory": [],
        "gold": gold,
        "xp": 0,
        "level": level,
    }


def test_cycle_signature_is_deterministic_and_includes_economy_and_strategy():
    strategy = {
        "composition_direction": "Invoker",
        "composition_locked": True,
        "composition_focus": "TFT_Test",
        "composition_strength": 4.0,
        "core_units": ["TFT_Test"],
        "active_traits": {"Invoker": 2},
    }
    first = _cycle_signature(player(), strategy)
    assert first == _cycle_signature(player(), dict(strategy))
    assert first != _cycle_signature(player(gold=9), strategy)
    assert first != _cycle_signature(player(level=6), strategy)
    assert first != _cycle_signature(player(), {**strategy, "composition_direction": "Vanguard"})
    assert first != _cycle_signature(player(), {**strategy, "active_traits": {"Invoker": 4}})


def test_cycle_signature_tracks_unit_identity_even_when_champion_matches():
    strategy = {"composition_direction": "Invoker"}
    a = player()
    b = player()
    b["board"][0]["uuid"] = "unit-2"
    assert _cycle_signature(a, strategy) != _cycle_signature(b, strategy)
