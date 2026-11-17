
import numpy as np
import pytest
ACTION_DIMS = (9, 5, 9, 28, 28, 28)
try:
    from tft_engine import TFTLobby
except ImportError:
    pytest.skip(
        "tft_engine ainda nao foi compilado.",
        allow_module_level=True,
    )


def test_lobby_reset_contract():
    engine = TFTLobby(seed=2026)

    try:
        result = engine.reset()

        assert "observations" in result
        assert "action_masks" in result

        observations = result["observations"]

        assert isinstance(observations, np.ndarray)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert observations.shape[1] > 0

        assert len(result["action_masks"]) == 8
    finally:
        engine.close()


def test_lobby_step_contract():
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        # PASS deve ser substituido pelo indice real da acao
        # neutra definido pela implementacao C++.
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]

        # Cada rodada de treinamento exige 15 ações por jogador; PASS conta como ação.
        result = None
        for _ in range(15):
            result = engine.step(actions)

        assert result["observations"].shape == (
            8,
            engine.observation_dim,
        )
        assert result["rewards"].shape == (8,)
        assert result["dones"].shape == (8,)
        assert len(result["action_masks"]) == 8
        assert isinstance(result["lobby_done"], bool)
        assert len(result["action_traces"]) == 8
        for player_id, trace in enumerate(result["action_traces"]):
            assert trace["requested_action"] == actions[player_id]
            assert trace["effective_action"] == actions[player_id]
            assert trace["handler_applied"] is True
            assert trace["status_reason"] == "applied"

        # O estado público deve refletir o resultado do step.
        state = engine.get_public_state()

        assert state["round"] == 2
        assert state["round_index"] == 1
        assert state["stage"] == 1

        # O índice 6 do core contém a rodada normalizada pelo contrato Python.
        assert np.allclose(result["observations"][:, 6], 2.0 / 12.0)
        
    finally:
        engine.close()


def test_public_state_matches_python_lobby_contract():
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()
        state = engine.get_public_state()

        assert isinstance(state, dict)

        expected_keys = {
            "stage",
            "round",
            "round_index",
            "finished",
            "winner_id",
            "ranking",
            "alive_players",
            "players",
        }
        assert expected_keys.issubset(state.keys())

        assert state["stage"] == 1
        assert state["round"] == 1
        assert state["round_index"] == 0
        assert state["finished"] is False
        assert state["winner_id"] is None
        assert state["ranking"] == []
        assert state["alive_players"] == list(range(8))

        players = state["players"]
        assert isinstance(players, list)
        assert len(players) == 8

        assert [
            player["player_id"] for player in players
        ] == list(range(8))

        expected_player_keys = {
            "player_id", "hp", "gold", "level", "xp",
            "alive", "eliminated", "wins", "losses",
            "placement", "opponent_id", "damage_taken",
        }
        assert expected_player_keys.issubset(players[0].keys())

    finally:
        engine.close()

def test_public_round_and_stage_remain_consistent():
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]

        # Sete rodadas completas (15 ações por jogador) levam à rodada pública 8.
        for _ in range(7 * 15):
            engine.step(actions)

        state = engine.get_public_state()

        assert state["round"] == 8
        assert state["round_index"] == 7
        assert state["stage"] == 2

    finally:
        engine.close()


def test_action_dimensions_accept_highest_valid_indices():
    """Cada componente aceita seu maior índice válido."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        # PASS ignores legacy arguments, so their highest bounded indices
        # exercise the original five argument domains without fabricating an
        # item command whose arguments have type-specific semantics.
        actions = [
            [6, ACTION_DIMS[1] - 1, ACTION_DIMS[2] - 1,
             ACTION_DIMS[3] - 1, ACTION_DIMS[4] - 1, ACTION_DIMS[5] - 1]
            for _ in range(8)
        ]

        result = engine.step(actions)

        assert result["observations"].shape == (
            8,
            engine.observation_dim,
        )
    finally:
        engine.close()


@pytest.mark.parametrize(
    ("component", "invalid_value"),
    [
        (component, invalid_value)
        for component, dimension in enumerate(ACTION_DIMS)
        for invalid_value in (-1, dimension)
    ],
)
def test_action_dimensions_reject_out_of_range_indices(
    component,
    invalid_value,
):
    """Cada dimensão rejeita índices negativos e acima do limite."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0][component] = invalid_value

        with pytest.raises(
            ValueError,
            match="Componente de acao fora dos limites",
        ):
            engine.step(actions)

        # A ação inválida não deve avançar a partida.
        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


@pytest.mark.parametrize(
    "actions",
    [
        [[6, 0, 0, 0, 0, 0] for _ in range(7)],
        [[6, 0, 0, 0, 0] for _ in range(8)],
        [[6, 0, 0, 0, 0, 0, 0] for _ in range(8)],
    ],
)
def test_step_rejects_wrong_action_shape(actions):
    """O binding exige 8 jogadores e 6 componentes por ação."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises(ValueError):
            engine.step(actions)

        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


def test_observation_reward_done_and_mask_formats():
    engine = TFTLobby(seed=2026)

    try:
        reset_result = engine.reset()

        # Observações do reset.
        observations = reset_result["observations"]
        assert isinstance(observations, np.ndarray)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert observations.dtype == np.float32

        # Máscaras retornadas pelo reset.
        masks = reset_result["action_masks"]
        assert len(masks) == 8

        expected_shapes = {
            "type_mask": (9,),
            "shop_mask": (5,),
            "bench_source_mask": (9,),
            "board_target_mask": (28,),
            "board_source_mask": (28,),
            "board_move_target_masks": (28, 28),
            "bench_move_source_mask": (9,),
            "bench_to_board_target_masks": (9, 28),
            "item_inventory_mask": (9,),
            "item_component_first_mask": (10,),
            "item_component_pair_masks": (10, 10),
            "item_target_mask": (37,),
        }

        for player_masks in masks:
            assert isinstance(player_masks, dict)

            for name, shape in expected_shapes.items():
                mask = player_masks[name]
                assert isinstance(mask, np.ndarray), name
                assert mask.shape == shape, name
                assert mask.dtype == np.bool_, name

        # Resultado do step.
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        step_result = engine.step(actions)

        assert step_result["observations"].shape == (
            8,
            engine.observation_dim,
        )
        assert step_result["observations"].dtype == np.float32

        assert step_result["rewards"].shape == (8,)
        assert step_result["rewards"].dtype == np.float32

        assert step_result["dones"].shape == (8,)
        assert step_result["dones"].dtype == np.bool_

        assert len(step_result["action_masks"]) == 8

    finally:
        engine.close()

def test_reset_accepts_missing_seed():
    """reset() e reset(seed=None) devem funcionar."""
    engine = TFTLobby(seed=2026)

    try:
        result_default = engine.reset()
        assert result_default["observations"].shape == (
            8,
            engine.observation_dim,
        )

        result_none = engine.reset(seed=None)
        assert result_none["observations"].shape == (
            8,
            engine.observation_dim,
        )

        # Cada reset inicia um novo episódio.
        assert result_none["episode_id"] > result_default["episode_id"]

    finally:
        engine.close()


@pytest.mark.parametrize(
    "invalid_seed",
    [
        -1,
        "seed_invalida",
        1.5,
    ],
)
def test_reset_rejects_invalid_seed(invalid_seed):
    """Seeds inválidas devem gerar erro Python controlado."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        previous_episode_id = engine.episode_id
        previous_state = engine.get_public_state()

        with pytest.raises((TypeError, ValueError, OverflowError)):
            engine.reset(seed=invalid_seed)

        # Uma falha de validação não deve reiniciar o episódio.
        assert engine.episode_id == previous_episode_id
        assert engine.get_public_state()["round"] == (
            previous_state["round"]
        )

    finally:
        engine.close()


def test_step_rejects_missing_actions():
    """step(None) deve falhar sem avançar a rodada."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises((TypeError, ValueError)):
            engine.step(None)

        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0

    finally:
        engine.close()


def test_engine_rejects_operations_after_close():
    """Operações após close() devem falhar de forma controlada."""
    engine = TFTLobby(seed=2026)
    engine.reset()
    engine.close()

    actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]

    with pytest.raises(RuntimeError, match="fechado"):
        engine.reset()

    with pytest.raises(RuntimeError, match="fechado"):
        engine.step(actions)

    with pytest.raises(RuntimeError, match="fechado"):
        engine.get_public_state()


def test_default_action_masks_have_valid_fallbacks():
    engine = TFTLobby(seed=2026)

    try:
        result = engine.reset()
        masks_by_player = result["action_masks"]

        assert len(masks_by_player) == 8

        for masks in masks_by_player:
            # Toda dimensão categórica precisa ter
            # pelo menos uma opção válida.
            assert masks["type_mask"].any()
            assert masks["shop_mask"].any()
            assert masks["bench_source_mask"].any()
            assert masks["board_target_mask"].any()
            assert masks["board_source_mask"].any()
            assert masks["bench_move_source_mask"].any()

            assert masks["board_move_target_masks"].shape == (28, 28)
            assert masks["board_move_target_masks"].any()

            assert masks["bench_to_board_target_masks"].shape == (9, 28)
            assert masks["bench_to_board_target_masks"].any()

            # A unidade inicial no banco habilita mover/vender, além de PASS.
            assert masks["type_mask"].tolist() == [
                False, False, False, True, False, True, True, False, False
            ]

    finally:
        engine.close()


def test_step_rejects_none_without_advancing_round():
    """Entrada ausente deve gerar erro sem alterar o estado."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises(TypeError):
            engine.step(None)

        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


@pytest.mark.parametrize(
    ("seed", "expected_error"),
    [
        ("2026", TypeError),  # Texto não é aceito.
        (True, TypeError),    # Booleano não é aceito.
        (-1, ValueError),     # Seed negativa.
        (2**64, ValueError),  # Acima do limite de uint64.
    ],
)
def test_reset_rejects_invalid_seed(seed, expected_error):
    """O reset deve rejeitar seeds inválidas."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises(expected_error):
            engine.reset(seed=seed)

        # O reset inválido não deve iniciar outra rodada.
        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


def test_operations_after_close_raise_runtime_error():
    """O motor fechado não deve aceitar novas operações."""
    engine = TFTLobby(seed=2026)
    engine.reset()
    engine.close()

    with pytest.raises(RuntimeError):
        engine.reset()

    with pytest.raises(RuntimeError):
        engine.step([[6, 0, 0, 0, 0, 0] for _ in range(8)])


def test_anti_loop_history_is_scoped_to_each_preparation():
    """The public step advances a round, so per-preparation move history resets."""
    engine = TFTLobby(seed=20261016)

    try:
        engine.reset()
        native = engine
        audit = native.get_audit_snapshot()
        starter_id = audit["players"][0]["bench"][0]["champion_id"]
        assert starter_id

        assert native.set_player_economy_for_testing(0, 20, 5, 0)
        assert native.set_unit_for_testing(0, True, 0, starter_id, 1)
        assert native.set_unit_for_testing(0, True, 1, starter_id, 1)
        assert native.set_unit_for_testing(0, True, 2, starter_id, 1)

        def move(source, target):
            actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
            actions[0] = [4, 0, 0, 0, source, target]
            engine.step(actions)

        # Each public engine.step advances to the next round. The native
        # AntiLoopEngine intentionally clears local move history at that
        # boundary; multi-move cycle detection is tested directly in C++.
        move(0, 3)
        move(1, 4)
        move(3, 5)

        masks = native.get_action_masks()[0]
        assert bool(masks["board_move_target_masks"][5][0]), (
            "A move must not be blocked using stale per-preparation history "
            "after the engine has advanced to a new round."
        )

    finally:
        engine.close()


def test_buying_third_copy_auto_upgrades_to_two_star():
    """Three copies split between board, bench, and shop must merge on purchase."""
    engine = TFTLobby(seed=20261016)

    try:
        engine.reset()
        native = engine
        audit = native.get_audit_snapshot()
        champion_id = audit["players"][0]["shop"][0]["champion_id"]
        assert champion_id

        assert native.set_player_economy_for_testing(0, 20, 3, 0)
        assert native.set_unit_for_testing(0, True, 0, champion_id, 1)
        assert native.set_unit_for_testing(0, False, 0, champion_id, 1)
        assert native.set_shop_offer_for_testing(0, 0, champion_id)

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [0, 0, 0, 0, 0, 0]
        engine.step(actions)

        after = native.get_audit_snapshot()["players"][0]
        two_star = [
            unit for unit in list(after["board"]) + list(after["bench"])
            if unit["occupied"] and unit["champion_id"] == champion_id and unit["star"] == 2
        ]
        assert two_star, "The third 1-star copy should auto-upgrade into a 2-star unit."
    finally:
        engine.close()


def test_native_champion_id_map_matches_loaded_units_catalog():
    """The public mapping must preserve the exact native catalog array indices."""
    import json
    from pathlib import Path

    engine = TFTLobby(seed=2026)
    try:
        engine.reset()
        mapping = engine.get_champion_id_map()
        catalog_path = Path(__file__).resolve().parents[1] / "data" / "units_gerado.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))

        expected = {
            champion["apiName"]: index
            for index, champion in enumerate(catalog)
            if isinstance(champion, dict) and champion.get("apiName")
        }
        assert mapping == expected
        assert len(mapping) == len(set(mapping.values()))
        assert all(isinstance(value, int) and value >= 0 for value in mapping.values())
    finally:
        engine.close()


def test_opgg_adapter_resolves_units_through_native_catalog():
    """OP.GG keys must become the same internal IDs used by the engine."""
    import json
    from pathlib import Path

    engine = TFTLobby(seed=2026)
    try:
        engine.reset()
        root = Path(__file__).resolve().parents[1]
        opgg = json.loads((root / "data" / "opgg_tft_meta.json").read_text(encoding="utf-8"))
        adapted = json.loads(engine.adapt_opgg_compositions_json(
            json.dumps(opgg, ensure_ascii=False)
        ))
        assert isinstance(adapted, dict)
        assert isinstance(adapted.get("candidates"), list)
        assert isinstance(adapted.get("diagnostics"), list)
        mapping = engine.get_champion_id_map()
        for candidate in adapted["candidates"]:
            assert candidate["units"]
            assert all(
                isinstance(unit["champion_id"], int)
                and unit["champion_id"] in mapping.values()
                for unit in candidate["units"]
            )
    finally:
        engine.close()


def test_composition_intelligence_emits_per_player_shadow_diagnostics(monkeypatch):
    import json
    monkeypatch.setenv("TFT_COMPOSITION_INTELLIGENCE_SHADOW", "1")

    engine = TFTLobby(seed=20261111)
    try:
        engine.reset()
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        for _ in range(3):
            engine.step(actions)

        lines = engine.get_composition_diagnostics_jsonl()
        assert isinstance(lines, list)
        assert lines, "native shadow runtime must emit diagnostic snapshots"
        records = [json.loads(line) for line in lines]
        assert all(record.get("schema_version") == 1 for record in records)
        sequences = [record["sequence"] for record in records]
        assert sequences == sorted(sequences)
        assert len(sequences) == len(set(sequences))
        assert {record.get("player_id") for record in records} == set(range(8))
        for record in records:
            assert isinstance(record.get("round"), int)
            assert isinstance(record.get("diagnostics"), dict)
            assert "composition_decision" in record["diagnostics"]
            assert "unit_intentions" in record["diagnostics"]
            assert "lineup_plan" in record["diagnostics"]
            assert "action_recommendation" in record["diagnostics"]
    finally:
        engine.close()



def test_engine_instance_identity_is_distinct_from_seed_and_episode():
    first = TFTLobby(seed=2026)
    second = TFTLobby(seed=2026)
    try:
        first_reset = first.reset()
        second_reset = second.reset()

        first_id = first_reset["engine_instance_id"]
        second_id = second_reset["engine_instance_id"]

        assert isinstance(first_id, str)
        assert len(first_id) == 36
        assert first_id != second_id
        assert first.engine_instance_id == first_id
        assert second.engine_instance_id == second_id
        assert first_reset["episode_id"] == second_reset["episode_id"] == 1
        assert first_reset["decision_sequence"] == second_reset["decision_sequence"] == 1
        assert first_reset["player_decision_sequences"] == [1] * 8
        assert second_reset["player_decision_sequences"] == [1] * 8
        for reset in (first_reset, second_reset):
            structured = reset["native_state_snapshot"]
            assert structured["contract_id"] == "tft.native-state-snapshot"
            assert structured["contract_version"] == 1
            assert structured["source_namespace"] == "tft.engine.observation-snapshot"
            assert structured["engine_instance_id"] == reset["engine_instance_id"]
            assert structured["episode_id"] == reset["episode_id"]
            assert structured["snapshot_sequence"] == reset["decision_sequence"]
            assert structured["player_decision_sequences"] == reset["player_decision_sequences"]
            pool = structured["shared_pool"]
            assert pool["contract_id"] == "tft.shared-champion-pool-snapshot"
            assert pool["contract_version"] == 1
            assert pool["source_namespace"] == "tft.engine.observation-snapshot"
            assert pool["producer"] == "UnitPool::available"
            assert pool["engine_instance_id"] == reset["engine_instance_id"]
            assert pool["episode_id"] == reset["episode_id"]
            assert pool["snapshot_sequence"] == reset["decision_sequence"]
            assert pool["player_decision_sequences"] == reset["player_decision_sequences"]
            assert pool["total_available"] == sum(row["available_count"] for row in pool["champions"])
            assert pool["total_available"] == first.pool_total_available()
            assert len(pool["champions"]) > 0
            for row in pool["champions"]:
                assert row["available_count"] == first.pool_available(row["champion_internal_id"])
                assert row["initial_count"] == first.pool_initial_count(row["champion_internal_id"])
            assert len(structured["players"]) == 8
            assert isinstance(structured["players"][0]["item_component_counts"], list)
            assert isinstance(structured["players"][0]["item_inventory_counts"], list)
            assert isinstance(structured["players"][0]["equipped_items"], list)
            assert len(structured["players"][0]["board"]) == 28
            starter = structured["players"][0]["bench"][0]
            assert starter["occupied"]
            assert starter["champion_id"]
            assert starter["uuid"]

        first_step = first.step([[6, 0, 0, 0, 0, 0] for _ in range(8)])
        assert first_step["engine_instance_id"] == first_id
        assert first_step["episode_id"] == first_reset["episode_id"]
        assert first_step["decision_sequence"] == 2
        assert first_step["player_decision_sequences"] == [2] * 8
        assert first_step["native_state_snapshot"]["snapshot_sequence"] == first_step["decision_sequence"]
        assert first_step["native_state_snapshot"]["players"][0]["bench"][0]["uuid"] == starter["uuid"]

        next_reset = first.reset()
        assert next_reset["engine_instance_id"] == first_id
        assert next_reset["episode_id"] > first_reset["episode_id"]
        assert next_reset["decision_sequence"] == 3
        assert next_reset["player_decision_sequences"] == [3] * 8
        assert next_reset["native_state_snapshot"]["snapshot_sequence"] == next_reset["decision_sequence"]
    finally:
        first.close()
        second.close()


def test_elimination_retires_item_ownership_in_native_snapshot():
    engine = TFTLobby(seed=20261117)
    try:
        reset = engine.reset()
        component_id = reset["native_state_snapshot"]["players"][0]["item_component_catalog"][0]
        assert engine.add_item_component_for_testing(0, component_id)
        assert engine.set_player_hp_for_testing(0, 0.1)

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        result = None
        for _ in range(4):
            result = engine.step(actions, timer_enabled=True, timer_expired=True)
            player = result["native_state_snapshot"]["players"][0]
            if player["item_ownership_retired"]:
                break

        assert result is not None
        player = result["native_state_snapshot"]["players"][0]
        assert player["item_ownership_retired"] is True
        assert player["item_components"] == []
        assert player["item_component_counts"] == []
        assert player["retired_item_component_counts"] == [
            {"catalog_id": component_id, "count": 1}
        ]
        assert player["retired_item_inventory_counts"] == []
        assert player["retired_equipped_item_counts"] == []
        assert player["pending_anvil"] is False
        assert player["retired_pending_anvils"] == []
        assert all(not unit["occupied"] for unit in player["board"])
        assert all(not unit["occupied"] for unit in player["bench"])
        assert all(
            not result["native_state_snapshot"]["players"][other]["item_ownership_retired"]
            for other in range(1, 8)
        )
    finally:
        engine.close()
