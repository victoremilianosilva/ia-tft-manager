"""Regression test: the wrapper loads the generated item catalog by default."""

from cpp_lobby_env import CppTFTLobbyWrapper


def test_generated_set17_catalog_is_loaded_by_default():
    lobby = CppTFTLobbyWrapper(seed=20261026)
    try:
        # A real component ID from data/item_catalog_set17.json.
        assert lobby.grant_item_component(0, "TFT_Item_BFSword") is True
        assert lobby.grant_item_component(0, "NOT_A_REAL_TFT_COMPONENT") is False
    finally:
        lobby.close()
