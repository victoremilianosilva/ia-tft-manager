from cpp_lobby_env import _NativeSnapshotMapping, _NativeSnapshotPlayers


class _FakeSnapshotHandle:
    def __init__(self):
        self.keys_calls = 0
        self.player_count_calls = 0
        self.player_calls = []

    def keys(self):
        self.keys_calls += 1
        return ["contract_id", "players", "round"]

    def player_count(self):
        self.player_count_calls += 1
        return 2

    def player(self, index):
        self.player_calls.append(index)
        return {"player_id": index, "alive": True}


def test_native_snapshot_mapping_caches_immutable_keys_and_membership():
    handle = _FakeSnapshotHandle()
    snapshot = _NativeSnapshotMapping(handle)

    assert handle.keys_calls == 1
    assert len(snapshot) == 3
    assert list(snapshot) == ["contract_id", "players", "round"]
    assert "players" in snapshot
    assert "missing" not in snapshot
    assert snapshot.keys() == ["contract_id", "players", "round"]
    assert handle.keys_calls == 1


def test_native_snapshot_players_cache_fixed_count_and_materialized_player_views():
    handle = _FakeSnapshotHandle()
    players = _NativeSnapshotPlayers(handle)

    assert handle.player_count_calls == 1
    assert len(players) == 2
    assert players[0]["player_id"] == 0
    assert players[0]["alive"] is True
    assert players[-1]["player_id"] == 1
    assert players[0] is players[0]
    assert handle.player_count_calls == 1
    assert handle.player_calls == [0, 1]
