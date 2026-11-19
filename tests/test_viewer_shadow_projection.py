from viewer.shadow_projection import (
    shadow_diagnostics,
    shadow_lineup_entries,
    shadow_status_text,
)


def test_viewer_projection_uses_canonical_shadow_diagnostics_not_strategyinfo():
    player = {
        "strategy_info": {
            "strategy_name": "LEGACY",
            "planned_units": ["LegacyUnit"],
        },
        "shadow_composition": {
            "status": "available",
            "sequence": 12,
            "round": 10,
            "composition_id": "native-comp",
            "composition_version": 4,
            "stale": False,
            "diagnostics": {
                "composition_decision": {"decision": "KEEP"},
                "lineup_plan": {
                    "status": "ready",
                    "selected_board": [
                        {"champion_id": 101, "priority": 0.9, "owned": True},
                    ],
                },
                "action_recommendation": {"recommended_action": 6},
            },
        },
    }

    shadow, diagnostics = shadow_diagnostics(player)
    assert shadow["composition_id"] == "native-comp"
    assert diagnostics["composition_decision"]["decision"] == "KEEP"
    assert shadow_lineup_entries(player) == [
        {"champion_id": 101, "priority": 0.9, "owned": True},
    ]
    status = shadow_status_text(player)
    assert "KEEP" in status
    assert "native-comp v4" in status
    assert "LEGACY" not in status


def test_viewer_projection_reports_unavailable_shadow_without_legacy_fallback():
    player = {
        "strategy_info": {"strategy_name": "LEGACY"},
        "shadow_composition": {
            "status": "unavailable",
            "reason": "no_shadow_snapshot_for_player_in_current_episode",
        },
    }
    assert shadow_lineup_entries(player) == []
    assert shadow_status_text(player) == "Shadow: aguardando diagnóstico"



def test_viewer_never_offers_stale_shadow_lineup_as_current_plan():
    player = {
        "shadow_composition": {
            "status": "available",
            "stale": True,
            "composition_id": "stale-comp",
            "composition_version": 2,
            "diagnostics": {
                "composition_decision": {"decision": "KEEP"},
                "lineup_plan": {
                    "status": "ready",
                    "selected_board": [{"champion_id": 42}],
                },
            },
        }
    }
    assert shadow_lineup_entries(player) == []
    assert "EVIDÊNCIA OBSOLETA" in shadow_status_text(player)
