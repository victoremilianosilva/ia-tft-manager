"""TFT round scheduling regression tests (Set 18 standard calendar)."""

from lobby.TFTLobby import TFTLobby


def test_opening_rounds_do_not_count_as_pvp():
    for round_number in (1, 2, 3, 4):
        assert not TFTLobby.is_pvp_round(round_number)


def test_pvp_and_non_pvp_rounds_follow_stage_pattern():
    # 2-1, 2-2, 2-3, 2-5, 2-6 are PvP.
    for round_number in (5, 6, 7, 9, 10):
        assert TFTLobby.is_pvp_round(round_number)

    # 2-4 is carousel; 2-7 is PvE.
    assert not TFTLobby.is_pvp_round(8)
    assert not TFTLobby.is_pvp_round(11)

    # The pattern repeats on later stages: 3-1 PvP, 3-4 carousel, 3-7 PvE.
    assert TFTLobby.is_pvp_round(12)
    assert not TFTLobby.is_pvp_round(15)
    assert not TFTLobby.is_pvp_round(18)


def test_stage_mapping_accounts_for_short_first_stage():
    assert [TFTLobby.stage_for_round(r) for r in range(1, 5)] == [1, 1, 1, 1]
    assert all(TFTLobby.stage_for_round(r) == 2 for r in range(5, 12))
    assert TFTLobby.stage_for_round(12) == 3
