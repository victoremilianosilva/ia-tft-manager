"""Standalone human-demonstration Viewer.

This module intentionally lives beside the existing evaluation Viewer. It reuses
its read-only checkpoint/session loader and the Python lobby adapter, but never
constructs a Trainer, optimizer, or PPO update.
Run with: python -m viewer.human_main
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QComboBox, QFileDialog, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QSpinBox,
    QPlainTextEdit, QVBoxLayout, QWidget,
)

from viewer.session import ViewerSession, ACTION_NAMES, ROOT

ACTION_HELP = {
    0: "BUY — a=shop slot",
    1: "REROLL — sem argumentos",
    2: "BUY_XP — sem argumentos",
    3: "MOVE_BENCH — b=bench source, c=board target",
    4: "MOVE_BOARD — d=board source, e=board target",
    5: "SELL — b=bench slot (ou índice aceito pelo contrato nativo)",
    6: "PASS — encerra sua decisão neste passo",
    7: "EQUIP_FROM_INVENTORY — a=item slot, b=item target",
    8: "CRAFT_AND_EQUIP — a=component 1, b=component 2, c=item target",
}


def _player(items: list[dict], player_id: int) -> dict:
    return next((p for p in items if int(p.get("player_id", -1)) == player_id), {})


def _unit_name(unit: dict | None) -> str:
    if not unit or not unit.get("occupied", False):
        return "·"
    name = unit.get("champion_id") or unit.get("apiName") or unit.get("api_name") or "?"
    return f"{name} {'★' * max(1, min(3, int(unit.get('star', 1) or 1)))}"


def _format_player(public: dict, audit: dict, player_id: int) -> str:
    p = _player(public.get("players", []), player_id)
    a = _player(audit.get("players", []), player_id)
    lines = [
        f"RODADA {public.get('round', '?')}  |  jogador {player_id + 1}/8",
        f"HP: {p.get('hp', a.get('hp', '?'))}    Ouro: {p.get('gold', a.get('gold', '?'))}    "
        f"Nível: {p.get('level', a.get('level', '?'))}    XP: {p.get('xp', a.get('xp', '?'))}",
        "",
        "LOJA",
    ]
    shop = a.get("shop", p.get("shop", [])) or []
    lines.extend(f"  [{i}] {_unit_name(u)}  custo={u.get('cost', '?')}" for i, u in enumerate(shop))
    if not shop:
        lines.append("  (sem dados da loja)")
    lines += ["", "BANCO"]
    bench = a.get("bench", []) or []
    lines.extend(f"  [{i}] {_unit_name(u)}" for i, u in enumerate(bench))
    if not bench:
        lines.append("  (vazio)")
    lines += ["", "TABULEIRO (4 × 7; índices 0–27)"]
    board = a.get("board", []) or []
    for row in range(4):
        start = row * 7
        cells = [f"{i}:{_unit_name(board[i])}" for i in range(start, min(start + 7, len(board)))]
        lines.append("  " + " | ".join(cells))
    if not board:
        lines.append("  (sem dados do tabuleiro)")
    lines += ["", "ESTRATÉGIA", json.dumps(a.get("strategy_info", {}), ensure_ascii=False, indent=2)]
    return "\n".join(lines)


class HumanDemonstrationWindow(QMainWindow):
    """One human-controlled seat against seven frozen-policy agents."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TFT — Human Demonstration Viewer")
        self.resize(1180, 820)
        self.session = ViewerSession()
        self.human_player = 0
        self._build_ui()

    def _build_ui(self):
        root = QWidget()
        layout = QVBoxLayout(root)

        header = QHBoxLayout()
        self.checkpoint = QLineEdit(str(ROOT / "checkpoints" / "latest.pt"))
        browse = QPushButton("Checkpoint…")
        browse.clicked.connect(self._browse_checkpoint)
        self.seed = QSpinBox()
        self.seed.setRange(0, 2_000_000_000)
        self.seed.setValue(20261106)
        self.seat = QComboBox()
        self.seat.addItems([f"Jogador {i + 1}" for i in range(8)])
        self.seat.currentIndexChanged.connect(self._seat_changed)
        self.load_button = QPushButton("Nova partida")
        self.load_button.clicked.connect(self._load_match)
        header.addWidget(QLabel("Checkpoint"))
        header.addWidget(self.checkpoint, 1)
        header.addWidget(browse)
        header.addWidget(QLabel("Seed"))
        header.addWidget(self.seed)
        header.addWidget(QLabel("Seu assento"))
        header.addWidget(self.seat)
        header.addWidget(self.load_button)
        layout.addLayout(header)

        self.status = QLabel("Carregue um checkpoint para iniciar. Um assento será seu; os outros sete usarão a policy.")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)

        body = QHBoxLayout()
        self.state = QPlainTextEdit()
        self.state.setReadOnly(True)
        self.state.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        body.addWidget(self.state, 3)

        right = QVBoxLayout()
        action_box = QGroupBox("Sua decisão")
        form = QFormLayout(action_box)
        self.action = QComboBox()
        self.action.currentIndexChanged.connect(self._action_changed)
        form.addRow("Ação", self.action)

        self.args = []
        for label in ("Argumento A", "Argumento B", "Argumento C", "Argumento D", "Argumento E"):
            spin = QSpinBox()
            spin.setRange(0, 99)
            spin.setValue(0)
            self.args.append(spin)
            form.addRow(label, spin)
        self.action_help = QLabel(ACTION_HELP[0])
        self.action_help.setWordWrap(True)
        form.addRow(self.action_help)
        right.addWidget(action_box)

        self.note = QLineEdit()
        self.note.setPlaceholderText("Por que você tomou essa decisão? (opcional)")
        right.addWidget(QLabel("Sua justificativa (opcional)"))
        right.addWidget(self.note)
        self.submit = QPushButton("Executar minha decisão + 7 agentes")
        self.submit.clicked.connect(self._submit_action)
        self.submit.setEnabled(False)
        right.addWidget(self.submit)
        self.legal = QPlainTextEdit()
        self.legal.setReadOnly(True)
        self.legal.setMaximumHeight(210)
        right.addWidget(QLabel("Máscaras de ações legais (referência)"))
        right.addWidget(self.legal)
        right.addStretch(1)
        body.addLayout(right, 2)
        layout.addLayout(body, 1)

        self.events = QPlainTextEdit()
        self.events.setReadOnly(True)
        self.events.setMaximumHeight(130)
        layout.addWidget(QLabel("Registro da sessão"))
        layout.addWidget(self.events)
        self.setCentralWidget(root)
        self._action_changed()

    def _browse_checkpoint(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Selecionar checkpoint PPO", str(ROOT),
            "Checkpoints (*.pt *.pth *.ckpt);;Todos os arquivos (*)",
        )
        if path:
            self.checkpoint.setText(path)

    def _seat_changed(self, seat: int):
        self.human_player = int(seat)
        if self.session.started:
            self._render()

    def _action_changed(self, *_):
        action_id = int(self.action.currentData() or 0)
        self.action_help.setText(ACTION_HELP.get(action_id, "Ação sem descrição."))

    def _load_match(self):
        try:
            snapshot = self.session.load_checkpoint(
                self.checkpoint.text().strip(), self.seed.value(), True,
                ROOT / "viewer" / "human_sessions", record=True,
            )
            self.session.config.use_wall_clock_preparation = False
            self.events.appendPlainText(
                f"Sessão {self.session.match_id} | checkpoint SHA-256 {self.session.checkpoint_sha256}"
            )
            self.events.appendPlainText(f"Gravação: {self.session._session_dir}")
            self.submit.setEnabled(True)
            self._render(snapshot)
            self.status.setText(
                "Partida ativa. Cada clique executa uma ação sua e uma ação de cada agente vivo. "
                "A policy está em eval(), sem gradientes e sem atualização de pesos."
            )
        except Exception as exc:
            QMessageBox.critical(self, "Não foi possível iniciar", str(exc))

    def _current_masks(self) -> dict:
        if not self.session.masks:
            return {}
        return self.session.masks[self.human_player]

    def _render(self, _snapshot: dict | None = None):
        if not self.session.started:
            return
        self.state.setPlainText(_format_player(
            self.session.public_state, self.session.audit_snapshot, self.human_player,
        ))
        masks = self._current_masks()
        rendered = {}
        for key, value in masks.items():
            try:
                rendered[key] = np.asarray(value).astype(int).tolist()
            except (TypeError, ValueError):
                rendered[key] = str(value)
        self.legal.setPlainText(json.dumps(rendered, ensure_ascii=False, indent=2))
        type_mask = masks.get("type_mask")
        if type_mask is not None:
            allowed = [int(i) for i, flag in enumerate(type_mask) if bool(flag)]
            previous = self.action.currentData()
            self.action.blockSignals(True)
            self.action.clear()
            for action_id in allowed:
                name = ACTION_NAMES.get(action_id, f"UNKNOWN_{action_id}")
                self.action.addItem(f"{name} ({action_id})", action_id)
            if previous in allowed:
                self.action.setCurrentIndex(allowed.index(previous))
            self.action.blockSignals(False)
            self._action_changed()
        self.submit.setEnabled(not self.session.finished)
        if self.session.finished:
            self.status.setText("Partida finalizada. A sessão e as demonstrações foram gravadas.")
            self.events.appendPlainText(
                f"Classificação final: {self.session.public_state.get('ranking', [])}"
            )

    def _submit_action(self):
        s = self.session
        if not s.started or s.finished or s.lobby is None:
            return
        player_id = self.human_player
        public_players = s.public_state.get("players", [])
        human_state = _player(public_players, player_id)
        if not human_state.get("alive", True):
            QMessageBox.information(self, "Assento eliminado", "Este jogador já foi eliminado.")
            return

        action_type = int(self.action.currentData())
        action = [action_type] + [int(spin.value()) for spin in self.args]
        masks_before = s.masks
        human_mask = masks_before[player_id]
        type_mask = human_mask.get("type_mask")
        if type_mask is not None and (action_type >= len(type_mask) or not bool(type_mask[action_type])):
            QMessageBox.warning(self, "Ação indisponível", "Essa categoria de ação não está liberada pela máscara nativa.")
            return

        before = s._snapshot_for_event()
        actions, diagnostics = [], []
        for seat in range(8):
            player = _player(public_players, seat)
            if not player.get("alive", True):
                bot_action = [6, 0, 0, 0, 0, 0]
                diag = {"action_name": "PASS", "action": bot_action, "status": "eliminated_seat"}
            elif seat == player_id:
                bot_action = action
                diag = {
                    "action_name": ACTION_NAMES.get(action_type, "UNKNOWN"),
                    "action": action,
                    "source": "human",
                    "human_note": self.note.text().strip(),
                }
            else:
                bot_action, diag = s._action_for_player(seat)
                diag = {**diag, "source": "frozen_policy"}
            actions.append(bot_action)
            diagnostics.append(diag)

        s._emit("human_decision", {
            "player_id": player_id,
            "action": action,
            "action_name": ACTION_NAMES.get(action_type, "UNKNOWN"),
            "human_note": self.note.text().strip(),
            "state_before": before,
            "action_masks_before": human_mask,
            "available_actions_mask": type_mask,
        })
        try:
            obs, rewards, done, info = s.lobby.step(actions)
        except Exception as exc:
            QMessageBox.critical(self, "Falha ao executar ação", str(exc))
            return

        s.obs = obs
        s.last_actions = actions
        s.last_policy = diagnostics
        s.last_rewards = np.asarray(rewards, dtype=np.float32)
        s.last_info = info
        s.masks = s.lobby.get_action_masks()
        s.public_state = s.lobby.get_public_state()
        s._refresh_audit_snapshot()
        s.finished = bool(done or s.public_state.get("finished", False))
        s.step_count += 1
        after = s._snapshot_for_event()
        s._emit("step_completed", {
            "actions_submitted": actions,
            "rewards": s.last_rewards,
            "action_rewards": info.get("action_rewards"),
            "combat_rewards": info.get("combat_rewards"),
            "placement_rewards": info.get("placement_rewards"),
            "engine_events": info.get("events", []),
            "before": before,
            "after": after,
            "players": after.get("players", []),
            "human_player_id": player_id,
        })
        if s._player_log_writer is not None:
            s._player_log_writer.record_step(
                before=before, after=after, actions=actions, diagnostics=diagnostics,
                rewards=s.last_rewards, info=info,
                action_masks_before=masks_before, action_masks_after=s.masks,
                step=s.step_count, finished=s.finished,
            )
        if s.finished:
            s._emit("match_finished", {
                "ranking": s.public_state.get("ranking", []),
                "winner_id": s.public_state.get("winner_id"),
                "final_snapshot": after,
            })
            s._flush_close_log()
        self.note.clear()
        self.events.appendPlainText(
            f"Passo {s.step_count} | sua ação: {ACTION_NAMES.get(action_type)} {action} | "
            f"eventos: {', '.join(map(str, info.get('events', [])))}"
        )
        self._render(after)

    def closeEvent(self, event):
        try:
            self.session.close()
        finally:
            event.accept()


def main():
    app = QApplication([])
    window = HumanDemonstrationWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
