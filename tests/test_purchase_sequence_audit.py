from audit_viewer_match import audit_purchase_sequences


def _unit(champion="", *, cost=1, star=1, impact=2.0, occupied=True):
    return {
        "occupied": occupied, "champion_id": champion, "name": champion,
        "cost": cost, "star": star, "impact": impact, "uuid": champion + "-uuid",
    }


def _state(gold, *, bench=None, shop=None, board=None, comp="Trait"):
    return {
        "gold": gold, "comp_direction": comp,
        "bench": bench if bench is not None else [],
        "shop": shop if shop is not None else [],
        "board": board if board is not None else [],
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
