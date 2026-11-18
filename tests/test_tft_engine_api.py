
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


def test_stage_one_pve_reward_is_direct_component_grant_not_anvil_choice():
    """The stage-one PvE reward reaches inventory directly and does not enqueue an anvil."""
    engine = TFTLobby(seed=20261122)

    try:
        engine.reset()
        native = engine
        before = native.get_audit_snapshot()
        before_player = before["players"][0]
        assert before_player["item_components"] == []
        assert before_player["pending_anvil"] is False
        assert before_player["pending_anvil_options"] == []

        pass_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        # Each call contributes one action per player; fifteen actions resolve
        # one preparation round. Stage 1 round 4 is the component-loot round.
        for _ in range(4 * 15):
            result = engine.step(pass_actions)

        after = native.get_audit_snapshot()
        player = after["players"][0]
        assert after["round"] == 5, "The trace must resolve exactly through stage 1 round 4."
        assert player["item_components"], (
            "The stage-one PvE producer must grant at least one component directly to inventory."
        )
        assert player["item_component_counts"]
        assert sum(row["count"] for row in player["item_component_counts"]) == len(
            player["item_components"]
        )
        assert player["pending_anvil"] is False
        assert player["pending_anvil_sequence"] == 0
        assert player["pending_anvil_options"] == []
    finally:
        engine.close()


def test_shop_offer_revision_is_published_across_reroll_and_purchase():
    """Shop offer revisions in the audit snapshot track real reroll and purchase actions."""
    engine = TFTLobby(seed=20261121)

    try:
        engine.reset()
        native = engine
        assert native.set_player_economy_for_testing(0, 20, 5, 0)

        before_reroll = native.get_audit_snapshot()["players"][0]
        occupied_slots = [
            index for index, offer in enumerate(before_reroll["shop"])
            if offer["occupied"]
        ]
        assert occupied_slots, "Reset should publish at least one shop offer."
        reroll_slot = occupied_slots[0]
        initial_revision = int(before_reroll["shop_offer_revisions"][reroll_slot])
        initial_uuid = before_reroll["shop"][reroll_slot]["uuid"]
        assert initial_revision > 0
        assert initial_uuid

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [1, 0, 0, 0, 0, 0]
        engine.step(actions)

        after_reroll = native.get_audit_snapshot()["players"][0]
        rerolled_revision = int(after_reroll["shop_offer_revisions"][reroll_slot])
        assert rerolled_revision > initial_revision, (
            "A real reroll must advance the published revision for the replaced slot."
        )
        assert not any(
            offer["occupied"] and offer["uuid"] == initial_uuid
            for offer in after_reroll["shop"]
        ), "The replaced shop UnitInstance must no longer be offered."

        purchase_slot = next(
            index for index, offer in enumerate(after_reroll["shop"])
            if offer["occupied"]
        )
        purchase_revision = int(after_reroll["shop_offer_revisions"][purchase_slot])
        purchased_uuid = after_reroll["shop"][purchase_slot]["uuid"]
        assert purchase_revision > 0 and purchased_uuid

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [0, purchase_slot, 0, 0, 0, 0]
        engine.step(actions)

        after_purchase = native.get_audit_snapshot()["players"][0]
        retired_offer_revision = int(
            after_purchase["shop_offer_revisions"][purchase_slot]
        )
        assert retired_offer_revision > purchase_revision, (
            "A real purchase must advance the published revision and retire the offer."
        )
        assert not after_purchase["shop"][purchase_slot]["occupied"]
        assert not any(
            offer["occupied"] and offer["uuid"] == purchased_uuid
            for offer in after_purchase["shop"]
        )
    finally:
        engine.close()


def test_buying_third_copy_auto_upgrades_and_preserves_purchased_identity():
    """The purchased shop copy survives as the upgraded unit; consumed copies retire."""
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

        before = native.get_audit_snapshot()["players"][0]
        board_uuid = before["board"][0]["uuid"]
        bench_uuid = before["bench"][0]["uuid"]
        purchased_uuid = before["shop"][0]["uuid"]
        assert board_uuid and bench_uuid and purchased_uuid
        assert len({board_uuid, bench_uuid, purchased_uuid}) == 3

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [0, 0, 0, 0, 0, 0]
        engine.step(actions)

        after = native.get_audit_snapshot()["players"][0]
        two_star = [
            unit for unit in list(after["board"]) + list(after["bench"])
            if unit["occupied"] and unit["champion_id"] == champion_id and unit["star"] == 2
        ]
        assert len(two_star) == 1, "The three 1-star copies should produce one 2-star unit."
        assert two_star[0]["uuid"] == purchased_uuid, (
            "The purchased shop UnitInstance must remain the physical identity of the upgrade."
        )

        active_uuids = {
            unit["uuid"]
            for location in ("board", "bench", "shop")
            for unit in after[location]
            if unit["occupied"]
        }
        assert purchased_uuid in active_uuids
        assert board_uuid not in active_uuids
        assert bench_uuid not in active_uuids
        assert not after["shop"][0]["occupied"]
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



def test_selling_purchased_unit_retires_uuid_and_returns_copy_to_pool():
    """A real purchase followed by sale retires its UUID and restores one pool copy."""
    engine = TFTLobby(seed=20261117)

    try:
        engine.reset()
        native = engine
        before = native.get_audit_snapshot()
        player = before["players"][0]
        owned_champions = {
            unit["champion_id"]
            for location in ("board", "bench")
            for unit in player[location]
            if unit["occupied"]
        }
        offer_slot = next(
            (
                slot for slot, unit in enumerate(player["shop"])
                if unit["occupied"] and unit["champion_id"] not in owned_champions
            ),
            None,
        )
        assert offer_slot is not None, "A non-duplicate shop offer is required for the sale lifecycle test."

        offer = player["shop"][offer_slot]
        champion_id = offer["champion_id"]
        champion_internal_id = native.get_champion_id_map()[champion_id]
        purchased_uuid = offer["uuid"]
        assert purchased_uuid

        pool_row_before = next(
            row for row in before["shared_pool"]["champions"]
            if row["champion_internal_id"] == champion_internal_id
        )
        available_before = pool_row_before["available_count"]

        assert native.set_player_economy_for_testing(0, 20, 3, 0)
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [0, offer_slot, 0, 0, 0, 0]
        engine.step(actions)

        after_buy_snapshot = native.get_audit_snapshot()
        after_buy = after_buy_snapshot["players"][0]
        pool_after_buy = after_buy_snapshot["shared_pool"]
        assert pool_after_buy["engine_instance_id"] == before["engine_instance_id"]
        assert pool_after_buy["episode_id"] == before["episode_id"]
        assert pool_after_buy["snapshot_sequence"] == after_buy_snapshot["snapshot_sequence"]
        assert pool_after_buy["player_decision_sequences"] == after_buy_snapshot["player_decision_sequences"]
        assert pool_after_buy["snapshot_sequence"] > before["snapshot_sequence"]
        pool_row_after_buy = next(
            row for row in pool_after_buy["champions"]
            if row["champion_internal_id"] == champion_internal_id
        )
        # The shop offer was already reserved from the shared pool before this
        # BUY action; purchasing it transfers ownership but does not decrement
        # the pool a second time.
        assert pool_row_after_buy["available_count"] == available_before

        purchased_bench_slots = [
            slot for slot, unit in enumerate(after_buy["bench"])
            if unit["occupied"] and unit["uuid"] == purchased_uuid
        ]
        assert len(purchased_bench_slots) == 1, (
            "The purchased shop UnitInstance should move to the bench without changing identity."
        )
        bench_slot = purchased_bench_slots[0]

        sell_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        sell_actions[0] = [5, 0, bench_slot, 0, 0, 0]
        engine.step(sell_actions)

        after_sell = native.get_audit_snapshot()
        sold_player = after_sell["players"][0]
        pool_after_sell = after_sell["shared_pool"]
        assert pool_after_sell["engine_instance_id"] == before["engine_instance_id"]
        assert pool_after_sell["episode_id"] == before["episode_id"]
        assert pool_after_sell["snapshot_sequence"] == after_sell["snapshot_sequence"]
        assert pool_after_sell["player_decision_sequences"] == after_sell["player_decision_sequences"]
        assert pool_after_sell["snapshot_sequence"] > pool_after_buy["snapshot_sequence"]
        active_uuids = {
            unit["uuid"]
            for location in ("board", "bench", "shop")
            for unit in sold_player[location]
            if unit["occupied"]
        }
        assert purchased_uuid not in active_uuids

        pool_row_after = next(
            row for row in pool_after_sell["champions"]
            if row["champion_internal_id"] == champion_internal_id
        )
        # Selling the owned copy returns exactly one unit to the shared pool.
        assert pool_row_after["available_count"] == available_before + 1
        assert not sold_player["bench"][bench_slot]["occupied"]
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
            assert structured["contract_version"] == 2
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
        initial_components = reset["native_state_snapshot"]["players"][0]["item_component_counts"]
        component_id = reset["native_state_snapshot"]["players"][0]["item_component_catalog"][0]
        initial_component_count = next(
            (row["count"] for row in initial_components if row["catalog_id"] == component_id),
            0,
        )
        assert engine.add_item_component_for_testing(0, component_id)
        assert engine.set_player_hp_for_testing(0, 0.0)

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        result = None
        # Rounds 1-1 through 1-4 are PvE; elimination is evaluated on the first PvP round (2-1).
        for _ in range(5):
            result = engine.step(actions, timer_enabled=True, timer_expired=True)
            player = result["native_state_snapshot"]["players"][0]
            if player["item_ownership_retired"]:
                break

        assert result is not None
        player = result["native_state_snapshot"]["players"][0]
        assert player["item_ownership_retired"] is True
        assert player["item_components"] == []
        assert player["item_component_counts"] == []
        retired_components = {
            row["catalog_id"]: row["count"]
            for row in player["retired_item_component_counts"]
        }
        # The match may award additional components before the first PvP elimination.
        # The explicitly injected copy must still be present in the terminal aggregate.
        assert retired_components[component_id] >= initial_component_count + 1
        assert all(count > 0 for count in retired_components.values())
        assert player["item_inventory"] == []
        assert player["item_inventory_counts"] == []
        assert player["equipped_items"] == []
        assert player["pending_anvil"] is False
        assert player["pending_anvil_options"] == []
        assert all(not unit["occupied"] for unit in player["board"])
        assert all(not unit["occupied"] for unit in player["bench"])
        assert all(
            not result["native_state_snapshot"]["players"][other]["item_ownership_retired"]
            for other in range(1, 8)
        )
    finally:
        engine.close()


def test_native_snapshot_v2_exposes_unit_traits_and_board_geometry():
    engine = TFTLobby(seed=20261119)
    try:
        reset = engine.reset()
        snapshot = reset["native_state_snapshot"]
        assert snapshot["contract_id"] == "tft.native-state-snapshot"
        assert snapshot["contract_version"] == 2
        assert snapshot["board_geometry_id"] == "tft.board-grid.rectangular-4x7"
        assert snapshot["board_geometry_version"] == 1
        assert snapshot["board_rows"] == 4
        assert snapshot["board_columns"] == 7
        assert snapshot["board_position_formula"] == "row=slot/7;column=slot%7"

        player = snapshot["players"][0]
        starter = next(unit for unit in player["bench"] if unit["occupied"])
        assert isinstance(starter["trait_names"], list)
        assert all(isinstance(trait, str) and trait for trait in starter["trait_names"])
        assert len(starter["trait_names"]) == len(set(starter["trait_names"]))

        active_uuids = [
            unit["uuid"]
            for owner in snapshot["players"]
            for location in ("board", "bench", "shop")
            for unit in owner[location]
            if unit["occupied"]
        ]
        assert active_uuids
        assert len(active_uuids) == len(set(active_uuids))
    finally:
        engine.close()


def test_unit_instance_uuid_is_preserved_across_bench_and_board_moves():
    """Physical unit identity follows the same copy as its location changes."""
    engine = TFTLobby(seed=20261118)
    try:
        reset_result = engine.reset()
        initial = engine.get_audit_snapshot()["players"][0]
        starter = initial["bench"][0]
        assert starter["occupied"]
        unit_uuid = starter["uuid"]
        assert isinstance(unit_uuid, str) and unit_uuid

        # Deploy the starter from bench to a currently legal board slot.
        masks = engine.get_action_masks()[0]
        board_target = next(
            (index for index, allowed in enumerate(masks["bench_to_board_target_masks"][0])
             if bool(allowed)),
            None,
        )
        assert board_target is not None
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [3, 0, 0, board_target, 0, 0]
        deploy_result = engine.step(actions)

        deployed = engine.get_audit_snapshot()["players"][0]
        assert deployed["bench"][0]["occupied"] is False
        assert deployed["board"][board_target]["occupied"] is True
        assert deployed["board"][board_target]["uuid"] == unit_uuid

        # A preparation round requires 15 actions per player. Finish the
        # remaining 14 actions with PASS before moving the unit in round 2.
        pass_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        round_two_result = None
        for _ in range(14):
            round_two_result = engine.step(pass_actions)

        assert round_two_result is not None
        assert round_two_result["round"] == 2
        assert round_two_result["decision_sequence"] == deploy_result["decision_sequence"] + 14
        assert round_two_result["player_decision_sequences"] == [16] * 8

        # Move that same physical UnitInstance during the next preparation round.
        masks = engine.get_action_masks()[0]
        board_move_targets = masks["board_move_target_masks"][board_target]
        destination = next(
            (index for index, allowed in enumerate(board_move_targets)
             if index != board_target and bool(allowed)),
            None,
        )
        assert destination is not None
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [4, 0, 0, 0, board_target, destination]
        move_result = engine.step(actions)

        moved = engine.get_audit_snapshot()["players"][0]
        assert moved["board"][board_target]["occupied"] is False
        assert moved["board"][destination]["occupied"] is True
        assert moved["board"][destination]["uuid"] == unit_uuid

        # Both transitions remain bound to one Engine/episode; the native
        # sequence advances through the round boundary without losing identity.
        assert deploy_result["engine_instance_id"] == reset_result["engine_instance_id"]
        assert move_result["engine_instance_id"] == reset_result["engine_instance_id"]
        assert deploy_result["episode_id"] == reset_result["episode_id"]
        assert move_result["episode_id"] == reset_result["episode_id"]
        assert deploy_result["decision_sequence"] == reset_result["decision_sequence"] + 1
        assert move_result["decision_sequence"] == round_two_result["decision_sequence"] + 1
        assert deploy_result["player_decision_sequences"] == [2] * 8
        assert move_result["player_decision_sequences"] == [17] * 8
        assert deploy_result["native_state_snapshot"]["snapshot_sequence"] == deploy_result["decision_sequence"]
        assert round_two_result["native_state_snapshot"]["snapshot_sequence"] == round_two_result["decision_sequence"]
        assert move_result["native_state_snapshot"]["snapshot_sequence"] == move_result["decision_sequence"]
        assert deploy_result["round"] == 1
        assert move_result["round"] == 2
    finally:
        engine.close()


def test_selling_equipped_unit_returns_item_to_inventory_without_duplication():
    """Selling a unit detaches its equipment back to the player's item inventory."""
    engine = TFTLobby(seed=20261117)

    try:
        engine.reset()
        native = engine
        initial = native.get_audit_snapshot()["players"][0]
        starter_slot = next(
            (slot for slot, unit in enumerate(initial["bench"]) if unit["occupied"]),
            None,
        )
        assert starter_slot is not None
        sold_uuid = initial["bench"][starter_slot]["uuid"]
        assert sold_uuid

        item_id = "TFT_Item_AdaptiveHelm"
        assert native.add_completed_item_for_testing(0, item_id)

        # Item target indices use board slots first, then bench slots.
        equip_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        equip_actions[0] = [7, 0, 28 + starter_slot, 0, 0, 0]
        engine.step(equip_actions)

        after_equip = native.get_audit_snapshot()["players"][0]
        assert after_equip["item_inventory"] == []
        equipped = [
            row for row in after_equip["equipped_items"]
            if row["unit_uuid"] == sold_uuid and row["catalog_id"] == item_id
        ]
        assert len(equipped) == 1

        sell_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        sell_actions[0] = [5, 0, starter_slot, 0, 0, 0]
        engine.step(sell_actions)

        after_sale = native.get_audit_snapshot()["players"][0]
        active_uuids = {
            unit["uuid"]
            for location in ("board", "bench", "shop")
            for unit in after_sale[location]
            if unit["occupied"]
        }
        assert sold_uuid not in active_uuids
        assert after_sale["equipped_items"] == []
        assert after_sale["item_inventory"].count(item_id) == 1
    finally:
        engine.close()

def test_same_seed_replays_game_state_without_reusing_engine_identity():
    """Equivalent action traces replay game state while isolating Engine-local UUIDs."""
    first = TFTLobby(seed=20261120)
    second = TFTLobby(seed=20261120)
    try:
        first_reset = first.reset()
        second_reset = second.reset()

        assert first_reset["engine_instance_id"] != second_reset["engine_instance_id"]
        assert first_reset["episode_id"] == second_reset["episode_id"]
        first_state = first.get_audit_snapshot()
        second_state = second.get_audit_snapshot()
        first_initial_uuid = first_state["players"][0]["bench"][0]["uuid"]
        second_initial_uuid = second_state["players"][0]["bench"][0]["uuid"]
        assert first_initial_uuid
        assert second_initial_uuid

        # Choose the same legal deployment target from equivalent initial states.
        first_masks = first.get_action_masks()[0]
        second_masks = second.get_action_masks()[0]
        target = next(
            (index for index, allowed in enumerate(first_masks["bench_to_board_target_masks"][0])
             if bool(allowed)),
            None,
        )
        assert target is not None
        assert bool(second_masks["bench_to_board_target_masks"][0][target])

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [3, 0, 0, target, 0, 0]
        first_deploy = first.step(actions)
        second_deploy = second.step(actions)

        first_after_deploy = first.get_audit_snapshot()
        second_after_deploy = second.get_audit_snapshot()
        first_uuid = first_after_deploy["players"][0]["board"][target]["uuid"]
        second_uuid = second_after_deploy["players"][0]["board"][target]["uuid"]
        assert first_uuid == first_initial_uuid
        assert second_uuid == second_initial_uuid

        # The action trace is equivalent, but each result remains bound to its
        # own Engine instance and the same episode/decision sequence.
        assert first_deploy["engine_instance_id"] == first_reset["engine_instance_id"]
        assert second_deploy["engine_instance_id"] == second_reset["engine_instance_id"]
        assert first_deploy["engine_instance_id"] != second_deploy["engine_instance_id"]
        assert first_deploy["episode_id"] == second_deploy["episode_id"]
        assert first_deploy["decision_sequence"] == second_deploy["decision_sequence"] == 2
        assert first_deploy["player_decision_sequences"] == [2] * 8
        assert second_deploy["player_decision_sequences"] == [2] * 8

        # Compare semantic state recursively because the native audit
        # snapshot nests NumPy arrays inside player/pool structures.
        def assert_same_value(left, right):
            if isinstance(left, np.ndarray):
                assert isinstance(right, np.ndarray)
                assert left.shape == right.shape
                if left.dtype.kind in "OUS":
                    for index in np.ndindex(left.shape):
                        assert_same_value(left[index], right[index])
                else:
                    np.testing.assert_array_equal(left, right)
            elif isinstance(left, str) and isinstance(right, str):
                def is_uuid(value):
                    return (
                        len(value) == 36
                        and value[8] == "-"
                        and value[13] == "-"
                        and value[18] == "-"
                        and value[23] == "-"
                    )
                if is_uuid(left) and is_uuid(right):
                    return
                assert left == right
            elif isinstance(left, dict):
                assert isinstance(right, dict)
                assert left.keys() == right.keys()
                for key in left:
                    # Unit UUIDs are Engine-local identity, not seeded game state.
                    if key == "uuid" or key.endswith("_uuid"):
                        continue
                    assert_same_value(left[key], right[key])
            elif isinstance(left, (list, tuple)):
                assert isinstance(right, type(left))
                assert len(left) == len(right)
                for left_item, right_item in zip(left, right):
                    assert_same_value(left_item, right_item)
            else:
                assert left == right

        # Engine identity is deliberately distinct and excluded from semantic
        # game-state equivalence; all player and shared-pool data must match.
        assert_same_value(first_after_deploy["players"][0], second_after_deploy["players"][0])
        assert_same_value(first_after_deploy["shared_pool"], second_after_deploy["shared_pool"])
    finally:
        first.close()
        second.close()


def test_audit_snapshot_publishes_player_survival_and_standing():
    """Native player HP/liveness/record and optional standings share the audit snapshot identity."""
    engine = TFTLobby(seed=20261118)

    try:
        reset = engine.reset()
        snapshot = engine.get_audit_snapshot()

        assert snapshot["engine_instance_id"] == reset["engine_instance_id"]
        assert snapshot["episode_id"] == reset["episode_id"]
        assert snapshot["snapshot_sequence"] == reset["decision_sequence"]
        assert snapshot["player_decision_sequences"] == reset["player_decision_sequences"]
        assert len(snapshot["players"]) == 8

        for player_id, player in enumerate(snapshot["players"]):
            assert player["player_id"] == player_id
            assert player["hp"] == 100.0
            assert player["alive"] is True
            assert player["wins"] == 0
            assert player["losses"] == 0
            assert player["placement"] is None
            assert player["opponent_id"] is None
    finally:
        engine.close()


def test_audit_snapshot_publishes_accumulated_player_damage():
    """Accumulated lobby damage is copied from the authoritative player state."""
    engine = TFTLobby(seed=20261119)

    try:
        engine.reset()
        initial = engine.get_audit_snapshot()
        assert all(player["damage_taken"] == 0.0 for player in initial["players"])

        pass_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        # Resolve opening PvE rounds and the first PvP preparation/combat cycle.
        for _ in range(5 * 15):
            engine.step(pass_actions)

        after = engine.get_audit_snapshot()
        assert after["snapshot_sequence"] > initial["snapshot_sequence"]
        assert after["episode_id"] == initial["episode_id"]
        assert all(
            isinstance(player["damage_taken"], (int, float))
            and player["damage_taken"] >= 0.0
            for player in after["players"]
        )
        assert sum(player["damage_taken"] for player in after["players"]) > 0.0, (
            "At least one resolved PvP matchup must publish accumulated player damage."
        )
    finally:
        engine.close()
