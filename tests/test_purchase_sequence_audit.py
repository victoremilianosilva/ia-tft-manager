from scripts.audit_viewer_match import audit_purchase_sequences


def _unit(champion="", *, cost=1, star=1, impact=2.0, occupied=True):
    return {
        "occupied": occupied, "champion_id": champion, "name": champion,
        "cost": cost, "star": star, "impact": impact, "uuid": champion + "-uuid",
    }


def _state(gold, *, bench=None, shop=None, board=None, comp="Trait", core_units=None):
    def padded(values, size):
        values = list(values or [])
        return values + [_unit(occupied=False) for _ in range(max(0, size - len(values)))]
    return {
        "gold": gold, "comp_direction": comp, "core_units": list(core_units or []),
        "bench": padded(bench, 9),
        "shop": padded(shop, 5),
        "board": padded(board, 28),
        "active_traits": {},
    }


def _entry(seq, step, action, name, before, after):
    return {
        "sequence_id": seq, "step": step, "round": "1-1", "event_type": "action",
        "payload": {
            "action": action, "action_name": name,
            "state_before": before, "state_after": after,
            "composition_diagnostics": {"unit_fit": {"focus_fit_score": 0.0}},
        },
    }


def test_detects_purchase_reversed_within_two_actions_and_counts_net_gold():
    briar = _unit("Briar", cost=1)
    bought = _entry(
        1, 1, [0, 0, 0, 0, 0, 0], "BUY",
        _state(10, shop=[briar]),
        _state(9, bench=[briar], shop=[briar]),
    )
    passed = _entry(2, 2, [6, 0, 0, 0, 0, 0], "PASS",
                    _state(9, bench=[briar]), _state(9, bench=[briar]))
    sold = _entry(
        3, 3, [5, 0, 0, 0, 0, 0], "SELL",
        _state(9, bench=[briar]),
        _state(10, bench=[]),
    )
    report = {"issues": []}
    audit_purchase_sequences([bought, passed, sold], "Jogador 1", report)

    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["buys"] == 1
    assert metrics["sells"] == 1
    assert metrics["reversed_1"] == 0
    assert metrics["reversed_2"] == 1
    assert metrics["reversed_4"] == 1
    assert metrics["net_gold_lost_reversed"] == 0
    assert metrics["classified_sales"]["PURCHASE_REVERSED"] == 1
    assert any(issue["code"] == "PURCHASE_REVERSED" for issue in report["issues"])


def test_does_not_classify_sale_after_composition_transition_as_reversal():
    briar = _unit("Briar", cost=1)
    bought = _entry(1, 1, [0, 0, 0, 0, 0, 0], "BUY",
                    _state(10, shop=[briar], comp="Trait"),
                    _state(9, bench=[briar], comp="Trait"))
    sold = _entry(2, 2, [5, 0, 0, 0, 0, 0], "SELL",
                  _state(9, bench=[briar], comp="Other"),
                  _state(10, bench=[], comp="Other"))
    report = {"issues": []}
    audit_purchase_sequences([bought, sold], "Jogador 1", report)

    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["reversed_1"] == 0
    assert metrics["classified_sales"]["COMP_TRANSITION"] == 1
    assert not any(issue["code"] == "PURCHASE_REVERSED" for issue in report["issues"])


def test_core_and_pair_sales_are_counted_only_after_first_comp_direction():
    early = _unit("Briar", cost=1)
    core = _unit("Carry", cost=4)
    before_decision = _entry(
        1, 1, [5, 0, 0, 0, 0, 0], "SELL",
        _state(10, bench=[early], comp="", core_units=["Briar"]),
        _state(11, bench=[], comp="", core_units=["Briar"]),
    )
    decision = _entry(
        2, 2, [6, 0, 0, 0, 0, 0], "PASS",
        _state(11, board=[core], comp=""),
        _state(11, board=[core], comp="CarryTrait"),
    )
    after_decision = _entry(
        3, 3, [5, 0, 0, 0, 0, 0], "SELL",
        _state(11, bench=[core], comp="CarryTrait", core_units=["Carry"]),
        _state(15, bench=[], comp="CarryTrait", core_units=["Carry"]),
    )
    report = {"issues": []}
    audit_purchase_sequences([before_decision, decision, after_decision], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["composition_decision_found"] is True
    assert metrics["composition_decision_round"] == "1-1"
    assert metrics["core_pair_sales_before_comp_decision_ignored"] == 1
    assert metrics["core_unit_sales"] == 1
    assert metrics["core_or_pair_sales"] == 1
    assert sum(issue["code"] == "SOLD_CORE_UNIT" for issue in report["issues"]) == 1


def test_purchase_reversed_in_immediately_following_action_counts_reversed_1():
    briar = _unit("Briar", cost=1)
    bought = _entry(
        1, 1, [0, 0, 0, 0, 0, 0], "BUY",
        _state(10, shop=[briar]), _state(9, bench=[briar]),
    )
    sold = _entry(
        2, 2, [5, 0, 0, 0, 0, 0], "SELL",
        _state(9, bench=[briar]), _state(10, bench=[]),
    )
    report = {"issues": []}
    audit_purchase_sequences([bought, sold], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["reversed_1"] == 1
    assert metrics["reversed_2"] == 1
    assert metrics["reversed_4"] == 1



def test_pair_loss_is_champion_specific_not_global_pair_count():
    briar = _unit("Briar")
    nasus_a = _unit("Nasus")
    nasus_b = _unit("Nasus")
    decision = _entry(1, 1, [6, 0, 0, 0, 0, 0], "PASS",
                      _state(20, bench=[briar, nasus_a, nasus_b], comp=""),
                      _state(20, bench=[briar, nasus_a, nasus_b], comp="Trait"))
    sale = _entry(2, 2, [5, 0, 0, 0, 0, 0], "SELL",
                  _state(20, bench=[briar, nasus_a, nasus_b], comp="Trait"),
                  _state(21, bench=[nasus_a, nasus_b], comp="Trait"))
    report = {"issues": []}
    audit_purchase_sequences([decision, sale], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["core_or_pair_sales"] == 0
    assert metrics["confirmed_pair_path_losses"] == 0


def test_sale_of_one_star_copy_does_not_claim_pair_loss_when_two_star_copy_remains():
    briar_two = _unit("Briar", star=2)
    briar_one = _unit("Briar", star=1)
    decision = _entry(1, 1, [6, 0, 0, 0, 0, 0], "PASS",
                      _state(20, bench=[briar_two, briar_one], comp=""),
                      _state(20, bench=[briar_two, briar_one], comp="Trait"))
    sale = _entry(2, 2, [5, 0, 0, 0, 0, 0], "SELL",
                  _state(20, bench=[briar_two, briar_one], comp="Trait"),
                  _state(21, bench=[briar_two], comp="Trait"))
    report = {"issues": []}
    audit_purchase_sequences([decision, sale], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["core_or_pair_sales"] == 0


def test_core_match_is_exact_not_substring():
    lookalike = _unit("Carryover")
    decision = _entry(1, 1, [6, 0, 0, 0, 0, 0], "PASS",
                      _state(20, bench=[lookalike], comp=""),
                      _state(20, bench=[lookalike], comp="Trait"))
    sale = _entry(2, 2, [5, 0, 0, 0, 0, 0], "SELL",
                  _state(20, bench=[lookalike], comp="Trait", core_units=["Carry"]),
                  _state(21, bench=[], comp="Trait", core_units=["Carry"]))
    report = {"issues": []}
    audit_purchase_sequences([decision, sale], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["core_unit_sales"] == 0
    assert metrics["core_or_pair_sales"] == 0


def test_buy_sell_reversal_uses_acquired_uuid_not_shop_offer_uuid():
    shop_unit = _unit("Briar")
    acquired = _unit("Briar")
    acquired["uuid"] = "actual-purchased-unit"
    bought = _entry(1, 1, [0, 0, 0, 0, 0, 0], "BUY",
                    _state(10, shop=[shop_unit]),
                    _state(9, bench=[acquired]))
    passed = _entry(2, 2, [6, 0, 0, 0, 0, 0], "PASS",
                    _state(9, bench=[acquired]), _state(9, bench=[acquired]))
    sold = _entry(3, 3, [5, 0, 0, 0, 0, 0], "SELL",
                  _state(9, bench=[acquired]), _state(10, bench=[]))
    report = {"issues": []}
    audit_purchase_sequences([bought, passed, sold], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["reversed_2"] == 1
    assert metrics["purchase_records"][0]["uuid"] == "actual-purchased-unit"


def test_elimination_filter_keeps_death_causing_action_but_ignores_later_events():
    from scripts.audit_viewer_match import _active_entries_before_elimination

    alive_action = {
        "event_type": "action", "sequence_id": 1,
        "payload": {"state_before": {"alive": True}, "state_after": {"alive": False}},
    }
    after_death = {
        "event_type": "action", "sequence_id": 2,
        "payload": {"state_before": {"alive": False}, "state_after": {"alive": False}},
    }
    active, ignored = _active_entries_before_elimination([alive_action, after_death])
    assert active == [alive_action]
    assert ignored == 1


def test_real_pair_loss_requires_two_owned_one_star_copies_of_sold_champion():
    briar_a = _unit("Briar")
    briar_b = _unit("Briar")
    decision = _entry(1, 1, [6, 0, 0, 0, 0, 0], "PASS",
                      _state(20, bench=[briar_a, briar_b], comp=""),
                      _state(20, bench=[briar_a, briar_b], comp="Trait"))
    sale = _entry(2, 2, [5, 0, 1, 0, 0, 0], "SELL",
                  _state(20, bench=[briar_a, briar_b], comp="Trait"),
                  _state(21, bench=[briar_a], comp="Trait"))
    report = {"issues": []}
    audit_purchase_sequences([decision, sale], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["confirmed_pair_path_losses"] == 1
    assert metrics["core_or_pair_sales"] == 1
    assert any(issue["code"] == "SOLD_UPGRADE_PAIR_COPY" for issue in report["issues"])


def test_buy_sell_without_matching_uuid_is_ambiguous_not_confirmed_reversal():
    bought_unit = _unit("Briar")
    bought_unit["uuid"] = ""
    sold_unit = _unit("Briar")
    sold_unit["uuid"] = "unrelated-copy"
    bought = _entry(1, 1, [0, 0, 0, 0, 0, 0], "BUY",
                    _state(10, shop=[bought_unit]), _state(9, bench=[bought_unit]))
    sold = _entry(2, 2, [5, 0, 0, 0, 0, 0], "SELL",
                  _state(9, bench=[sold_unit]), _state(10, bench=[]))
    report = {"issues": []}
    audit_purchase_sequences([bought, sold], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["reversed_1"] == 0
    assert metrics["ambiguous_identity_sales"] == 1
    assert metrics["classified_sales"]["UNKNOWN"] == 1


def test_real_two_star_pair_loss_is_also_detected():
    briar_a = _unit("Briar", star=2)
    briar_b = _unit("Briar", star=2)
    decision = _entry(1, 1, [6, 0, 0, 0, 0, 0], "PASS",
                      _state(20, bench=[briar_a, briar_b], comp=""),
                      _state(20, bench=[briar_a, briar_b], comp="Trait"))
    sale = _entry(2, 2, [5, 0, 1, 0, 0, 0], "SELL",
                  _state(20, bench=[briar_a, briar_b], comp="Trait"),
                  _state(21, bench=[briar_a], comp="Trait"))
    report = {"issues": []}
    audit_purchase_sequences([decision, sale], "Jogador 1", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 1"]
    assert metrics["confirmed_pair_path_losses"] == 1
    assert metrics["core_or_pair_sales"] == 1
