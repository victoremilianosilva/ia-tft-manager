import pytest
import torch

from economy_finetuning.scenario_generator import (
    SCENARIOS,
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

    assert state == {
        "hp": 55.0,
        "gold": 40.0,
        "level": 6.0,
        "stage": 3,
        "round_number": 21.0,
        "win_streak": 3.0,
        "loss_streak": 1.0,
        "player_id": 3,
    }
    assert "strategy" not in state


def test_scenario_matching_does_not_depend_on_legacy_strategy_selectors():
    state = decode_semantic_observation(_semantic_batch(), player_id=0)
    reserve_scenario = next(item for item in SCENARIOS if item.scenario_id == "econ_gold_reserve")

    assert reserve_scenario.strategies == (0,)  # historical metadata only
    assert reserve_scenario.matches(state)
    assert reserve_scenario.to_dict()["strategies"] == []


def test_semantic_scenario_decoder_rejects_nonfinite_or_misaligned_rows():
    numeric = _semantic_batch()["numeric"].clone()
    numeric[2, 5] = float("nan")
    with pytest.raises(ValueError, match="NaN or infinity"):
        decode_semantic_observation({"numeric": numeric}, player_id=2)

    with pytest.raises(ValueError, match="outside the v6 batch"):
        decode_semantic_observation(_semantic_batch(), player_id=8)
