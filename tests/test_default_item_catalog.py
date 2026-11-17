"""Regression test: the wrapper loads the generated item catalog by default."""

from cpp_lobby_env import CppTFTLobbyWrapper


def test_generated_set18_catalog_is_loaded_by_default():
    lobby = CppTFTLobbyWrapper(seed=20261026)
    try:
        # A real component ID from data/itens.json.
        assert lobby.grant_item_component(0, "DA_Component_BFSword") is True
        assert lobby.grant_item_component(0, "NOT_A_REAL_TFT_COMPONENT") is False
    finally:
        lobby.close()
