
import numpy as np
import pytest
import torch

from trainer import Trainer


@pytest.fixture
def trainer():
    """Cria um Trainer sem inicializar ambientes ou o modelo."""
    instance = Trainer.__new__(Trainer)
    instance.num_envs = 1
    instance.num_agents = Trainer.PLAYERS_PER_LOBBY
    instance.device = torch.device("cpu")
    return instance


def create_valid_masks():
    """Cria máscaras válidas para os 8 jogadores de uma lobby."""
    player_masks = []

    for _ in range(Trainer.PLAYERS_PER_LOBBY):
        player_masks.append({
            "type_mask": np.array(
                [1, 0, 0, 0, 0, 0, 1, 0, 0], dtype=np.float32
            ),
            "shop_mask": np.ones(5, dtype=np.float32),
            "bench_source_mask": np.ones(9, dtype=np.float32),
            "board_target_mask": np.ones(28, dtype=np.float32),
            "board_source_mask": np.ones(28, dtype=np.float32),
            "board_move_target_masks": np.ones(
                (28, 28), dtype=np.float32
            ),
            "bench_move_source_mask": np.ones(
                9, dtype=np.float32
            ),
            "bench_to_board_target_masks": np.ones(
                (9, 28), dtype=np.float32
            ),
            "item_inventory_mask": np.zeros(9, dtype=np.float32),
            "item_component_first_mask": np.zeros(9, dtype=np.float32),
            "item_component_pair_masks": np.zeros((9, 9), dtype=np.float32),
            "item_target_mask": np.zeros(37, dtype=np.float32),
        })

    return [player_masks]


def test_valid_masks_are_converted_to_bool_tensors(trainer):
    masks = trainer._flatten_masks(create_valid_masks())

    assert set(masks.keys()) == set(Trainer.MASK_SHAPES.keys())

    for key, shape in Trainer.MASK_SHAPES.items():
        assert isinstance(masks[key], torch.Tensor)
        assert masks[key].dtype == torch.bool
        assert tuple(masks[key].shape) == (
            Trainer.PLAYERS_PER_LOBBY,
            *shape,
        )


def test_item_actions_are_audited_against_their_conditional_masks(trainer):
    masks = trainer._flatten_masks(create_valid_masks())
    actions = torch.tensor([[6, 0, 0, 0, 0, 0] for _ in range(8)], dtype=torch.long)

    masks["type_mask"][0, 7] = True
    masks["item_inventory_mask"][0, 2] = True
    masks["item_target_mask"][0, 36] = True
    actions[0] = torch.tensor([7, 2, 36, 0, 0, 0])

    masks["type_mask"][1, 8] = True
    masks["item_component_first_mask"][1, 1] = True
    masks["item_component_pair_masks"][1, 1, 2] = True
    masks["item_target_mask"][1, 4] = True
    actions[1] = torch.tensor([8, 1, 2, 4, 0, 0])

    valid = trainer._audit_selected_action_masks(actions, masks)
    assert valid["selected_invalid"] == 0

    actions[1, 2] = 3
    invalid = trainer._audit_selected_action_masks(actions, masks)
    assert invalid["conditional_invalid"] == 1
    assert invalid["selected_invalid"] == 1


def test_rejects_wrong_mask_dimensions(trainer):
    gym_masks = create_valid_masks()
    gym_masks[0][0]["shop_mask"] = np.ones(4)

    with pytest.raises(ValueError, match="shop_mask"):
        trainer._flatten_masks(gym_masks)


def test_rejects_string_mask_type(trainer):
    gym_masks = create_valid_masks()
    gym_masks[0][0]["shop_mask"] = np.array(["x"] * 5)

    with pytest.raises(TypeError):
        trainer._flatten_masks(gym_masks)


@pytest.mark.parametrize("invalid_value", [2, -1, 0.5])
def test_rejects_values_other_than_zero_or_one(
    trainer, invalid_value
):
    gym_masks = create_valid_masks()
    gym_masks[0][0]["shop_mask"] = np.array(
        [1, 0, invalid_value, 1, 0],
        dtype=np.float32,
    )

    with pytest.raises(ValueError):
        trainer._flatten_masks(gym_masks)


@pytest.mark.parametrize("invalid_value", [np.nan, np.inf, -np.inf])
def test_rejects_nan_and_infinity(trainer, invalid_value):
    gym_masks = create_valid_masks()
    gym_masks[0][0]["shop_mask"] = np.array(
        [1, 0, invalid_value, 1, 0],
        dtype=np.float32,
    )

    with pytest.raises(ValueError):
        trainer._flatten_masks(gym_masks)


def test_rejects_missing_required_mask(trainer):
    gym_masks = create_valid_masks()
    del gym_masks[0][0]["shop_mask"]

    with pytest.raises(KeyError):
        trainer._flatten_masks(gym_masks)


def test_rejects_wrong_number_of_lobbies(trainer):
    gym_masks = create_valid_masks()
    gym_masks.append(create_valid_masks()[0])

    with pytest.raises(ValueError, match="Número de máscaras"):
        trainer._flatten_masks(gym_masks)


def test_rejects_wrong_number_of_players(trainer):
    gym_masks = create_valid_masks()
    gym_masks[0].pop()

    with pytest.raises(ValueError, match="jogadores"):
        trainer._flatten_masks(gym_masks)
