"""Offscreen integration tests for Viewer card/dialog without legacy StrategyInfo."""
from __future__ import annotations

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest

pytest.importorskip("PySide6")
from PySide6.QtWidgets import QApplication, QLabel, QMessageBox

from viewer.main import PlayerCard, ViewerWindow


class _IconLoader:
    catalog = []

    def profile_for(self, _champion_id):
        return {}

    def pixmap_for(self, _champion_id):
        return None


@pytest.fixture(scope="module")
def qt_app():
    app = QApplication.instance() or QApplication([])
    yield app


def _player_snapshot():
    return {
        "player_id": 0,
        "shadow_composition": {
            "status": "available",
            "sequence": 7,
            "round": 9,
            "composition_id": "viewer-native-comp",
            "composition_version": 4,
            "stale": False,
            "diagnostics": {
                "composition_decision": {
                    "decision": "KEEP",
                    "reason": "active composition remains supported",
                    "target_score": {"total": 2.5},
                },
                "lineup_plan": {
                    "status": "ready",
                    "selected_board": [
                        {
                            "champion_id": 101,
                            "priority": 0.9,
                            "owned": True,
                            "currently_on_board": True,
                            "star": 2,
                        },
                    ],
                },
                "unit_intentions": [],
                "action_recommendation": {"recommended_action": 1},
            },
        },
    }


def test_player_card_renders_native_projection_without_strategy_info(qt_app):
    audit = _player_snapshot()
    assert "strategy_info" not in audit

    card = PlayerCard(0)
    card.update_player(
        {"alive": True, "hp": 80, "gold": 20, "level": 5, "xp": 2},
        audit,
        [6, 0, 0, 0, 0, 0],
        _IconLoader(),
    )

    assert "viewer-native-comp v4" in card.strategy_line.text()
    assert card.composition_button.isHidden() is False
    assert card.composition_button.isEnabled() is True
    card.deleteLater()
    qt_app.processEvents()


def test_composition_dialog_uses_native_lineup_without_strategy_info(qt_app, monkeypatch):
    monkeypatch.setattr("viewer.main.ChampionIconLoader", _IconLoader)
    window = ViewerWindow()
    try:
        audit = _player_snapshot()
        assert "strategy_info" not in audit
        window.session.audit_snapshot = {"players": [audit]}
        window.session.champion_id_map = {}
        window.icon_loader = _IconLoader()

        window._show_composition_dialog(0)

        dialog = window._composition_dialog
        labels = [label.text() for label in dialog.findChildren(QLabel)]
        assert any("viewer-native-comp v4" in text for text in labels)
        assert any("Unidades planejadas: 1" in text for text in labels)
        dialog.close()
        dialog.deleteLater()
        qt_app.processEvents()
    finally:
        window.close()
        window.deleteLater()
        qt_app.processEvents()


def test_stale_native_projection_hides_card_action_and_blocks_dialog(qt_app, monkeypatch):
    audit = _player_snapshot()
    audit["shadow_composition"]["stale"] = True

    card = PlayerCard(0)
    card.update_player(
        {"alive": True, "hp": 80, "gold": 20, "level": 5, "xp": 2},
        audit,
        [6, 0, 0, 0, 0, 0],
        _IconLoader(),
    )
    assert card.composition_button.isHidden() is True
    assert "EVIDÊNCIA OBSOLETA" in card.strategy_line.text()
    card.deleteLater()
    qt_app.processEvents()

    monkeypatch.setattr("viewer.main.ChampionIconLoader", _IconLoader)
    window = ViewerWindow()
    messages = []
    monkeypatch.setattr(QMessageBox, "information", lambda *args: messages.append(args[2]))
    try:
        window.session.audit_snapshot = {"players": [audit]}
        window.session.champion_id_map = {}
        window._show_composition_dialog(0)
        assert messages and "não publicou" in messages[0]
        assert getattr(window, "_composition_dialog", None) is None
    finally:
        window.close()
        window.deleteLater()
        qt_app.processEvents()
