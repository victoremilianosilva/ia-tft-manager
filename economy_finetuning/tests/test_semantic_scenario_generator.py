import pytest
import torch

from economy_finetuning.scenario_generator import (
    SCENARIOS,
    decode_observation,
    decode_semantic_observation,
)


def _semantic_batch():
    numeric = torch.zeros((8, 52), dtype=torch.float32)
    numeric[:, 0] = 0.55
    numeric[:, 5] = 0.20  # 40 gold
    numeric[:, 6] = 0.60  # level 6
    numeric[:, 8] = 0.30  # 3 win streak
    numeric[:, 9] = 0.10  # 1 loss streak
    numeric[:, 15] = 3.0 / 7.0
    numeric[:, 16] = 21.0 / 50.0
    return {"numeric": numeric}


def test_finetuning_scenarios_decode_authoritative_semantic_global_facts():
    state = decode_semantic_observation(_semantic_batch(), player_id=3)

    assert state == pytest.approx({
        "hp": 55.0,
        "gold": 40.0,
        "level": 6.0,
        "stage": 3,
        "round_number": 21.0,
        "win_streak": 3.0,
        "loss_streak": 1.0,
        "player_id": 3,
    })
    assert "strategy" not in state


def test_scenario_matching_does_not_depend_on_legacy_strategy_selectors():
    state = decode_semantic_observation(_semantic_batch(), player_id=0)
    reserve_scenario = next(item for item in SCENARIOS if item.scenario_id == "econ_gold_reserve")

    assert reserve_scenario.strategies == ()
    assert reserve_scenario.matches(state)
    assert reserve_scenario.to_dict()["strategies"] == []


def test_semantic_scenario_decoder_rejects_nonfinite_or_misaligned_rows():
    numeric = _semantic_batch()["numeric"].clone()
    numeric[2, 5] = float("nan")
    with pytest.raises(ValueError, match="NaN or infinity"):
        decode_semantic_observation({"numeric": numeric}, player_id=2)

    with pytest.raises(ValueError, match="outside the v6 batch"):
        decode_semantic_observation(_semantic_batch(), player_id=8)


def test_semantic_scenario_decoder_uses_native_player_identity_not_batch_position():
    semantic = _semantic_batch()
    semantic["numeric"][7, 5] = 0.45
    semantic["snapshot_metadata"] = [
        {"player_id": index} for index in [7, 6, 5, 4, 3, 2, 1, 0]
    ]

    state = decode_semantic_observation(semantic, player_id=0)
    assert state["player_id"] == 0
    assert state["gold"] == 90.0


def test_legacy_compact_decoder_never_interprets_board_offsets_as_strategy():
    observation = [0.5, 0.4, 0.6, 0.0, 0.2, 0.1, 0.5, 0.0, 0.0, 0.0]
    state = decode_observation(observation, player_id=2)
    assert state["hp"] == 50.0
    assert "strategy" not in state
    assert "strategy_name" not in state
