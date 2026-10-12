"""Testes de integração do contrato das máscaras de ação."""

import numpy as np
import pytest

from lobby.TFTLobby import TFTLobby


EXPECTED_SHAPES = {
    "type_mask": (7,),
    "shop_mask": (5,),
    "bench_source_mask": (9,),
    "board_target_mask": (28,),
    "board_source_mask": (28,),
    "board_move_target_masks": (28, 28),
    "bench_move_source_mask": (9,),
    "bench_to_board_target_masks": (9, 28),
}


def assert_mask_contract(masks):
    """Valida formato, tipo e existência de opções permitidas."""

    assert set(masks) == set(EXPECTED_SHAPES)

    for name, expected_shape in EXPECTED_SHAPES.items():
        mask = masks[name]

        assert mask.shape == expected_shape, (
            f"{name}: esperado {expected_shape}, recebido {mask.shape}"
        )
        assert mask.dtype == np.bool_, (
            f"{name}: esperado bool, recebido {mask.dtype}"
        )
        assert mask.any(), f"{name} não possui nenhuma opção válida"


def test_dead_player_only_has_pass_available():
    """Jogadores eliminados só podem escolher PASS."""

    masks = TFTLobby._dead_player_mask()

    assert_mask_contract(masks)

    assert np.flatnonzero(masks["type_mask"]).tolist() == [6]


def test_dead_player_dummy_masks_are_safe():
    """As máscaras auxiliares do jogador morto têm fallback válido."""

    masks = TFTLobby._dead_player_mask()

    assert np.flatnonzero(masks["shop_mask"]).tolist() == [0]
    assert np.flatnonzero(masks["bench_source_mask"]).tolist() == [0]
    assert np.flatnonzero(masks["board_source_mask"]).tolist() == [0]

    assert masks["board_move_target_masks"][0, 0]
    assert masks["bench_to_board_target_masks"][0, 0]


def test_lobby_masks_follow_contract_for_all_players():
    """Confere as máscaras reais produzidas por uma lobby."""

    lobby = TFTLobby(seed=123)
    masks_by_player = lobby.get_action_masks()

    assert len(masks_by_player) == lobby.PLAYERS_PER_LOBBY

    for masks in masks_by_player:
        assert_mask_contract(masks)

        # Toda ação do tipo MOVE_BOARD precisa ter uma origem
        # e um destino realmente permitido.
        if masks["type_mask"][4]:
            valid_sources = np.flatnonzero(masks["board_source_mask"])

            assert any(
                masks["board_move_target_masks"][source].any()
                for source in valid_sources
            ), "MOVE_BOARD habilitado sem destino válido"

        # Toda ação MOVE_BENCH precisa ter uma origem e destino.
        if masks["type_mask"][3]:
            valid_sources = np.flatnonzero(
                masks["bench_move_source_mask"]
            )

            assert any(
                masks["bench_to_board_target_masks"][source].any()
                for source in valid_sources
            ), "MOVE_BENCH habilitado sem destino válido"


def test_board_move_masks_never_allow_self_move_for_real_sources():
    """Uma origem ocupada não pode ter ela própria como destino."""

    lobby = TFTLobby(seed=456)

    for player in lobby.players:
        if not player.alive:
            continue

        manager = player.env.action_mask_manager
        board = manager._get_board()
        masks = lobby.get_action_masks()[player.player_id]

        for source, unit in enumerate(board[:28]):
            if unit is None:
                continue

            if masks["board_source_mask"][source]:
                assert not masks["board_move_target_masks"][source, source], (
                    f"Movimento próprio permitido na posição {source}"
                )
