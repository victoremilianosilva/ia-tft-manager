"""Desktop TFT Viewer — PySide6."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import torch
from PySide6.QtCore import Qt, QTimer, Signal, QObject, QThread
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame, QLabel, QPushButton, QComboBox, QCheckBox, QDoubleSpinBox,
    QSpinBox, QFileDialog, QLineEdit, QPlainTextEdit, QSplitter, QTabWidget,
    QMessageBox, QScrollArea, QGroupBox, QProgressBar, QSlider, QFormLayout,
)

from viewer.session import ViewerSession, unit_label, ACTION_NAMES, ROOT

APP_STYLE = """
QMainWindow, QWidget { background: #0b1020; color: #e5e7eb; font-family: 'Segoe UI'; font-size: 10pt; }
QFrame#playerCard, QGroupBox { background: #121b2d; border: 1px solid #293751; border-radius: 9px; }
QFrame#playerCard[selected="true"] { border: 2px solid #60a5fa; }
QLabel#muted { color: #94a3b8; }
QPushButton { background: #1d2b44; border: 1px solid #344765; border-radius: 6px; padding: 7px 12px; }
QPushButton:hover { background: #293b5c; }
QPushButton:disabled { color: #64748b; background: #111827; }
QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QPlainTextEdit { background: #0f172a; border: 1px solid #334155; border-radius: 5px; padding: 5px; }
QTabWidget::pane { border: 1px solid #293751; }
QTabBar::tab { background: #111827; padding: 8px 12px; }
QTabBar::tab:selected { background: #24344e; }
QProgressBar { background: #0f172a; border: 1px solid #334155; border-radius: 4px; text-align: center; }
QProgressBar::chunk { background: #38bdf8; }
"""

def _value(player, *keys, default=0):
    for key in keys:
        if key in player and player[key] is not None:
            return player[key]
    return default


def _format_unit(unit):
    return unit_label(unit) or "·"


class StepWorker(QObject):
    completed = Signal(object)
    failed = Signal(str)

    def __init__(self, session):
        super().__init__()
        self.session = session

    def run(self):
        try:
            self.completed.emit(self.session.step())
        except Exception as exc:
            self.failed.emit(str(exc))


class PlayerCard(QFrame):
    selected = Signal(int)

    def __init__(self, player_id: int, parent=None):
        super().__init__(parent)
        self.player_id = player_id
        self.setObjectName("playerCard")
        self.setProperty("selected", False)
        root = QVBoxLayout(self)
        root.setContentsMargins(8, 8, 8, 8)
        root.setSpacing(5)
        header = QHBoxLayout()
        self.name = QLabel(f"JOGADOR {player_id + 1}")
        self.name.setStyleSheet("font-weight: 700; color: #93c5fd;")
        self.status = QLabel("AGUARDANDO")
        self.status.setObjectName("muted")
        header.addWidget(self.name)
        header.addStretch()
        header.addWidget(self.status)
        root.addLayout(header)
        self.metrics = QLabel("HP —   OURO —   NV —   XP —")
        self.metrics.setObjectName("muted")
        root.addWidget(self.metrics)
        self.board = QGridLayout()
        self.board.setSpacing(2)
        self.cells = []
        for row in range(4):
            for col in range(7):
                cell = QLabel("·")
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setMinimumSize(27, 22)
                cell.setToolTip(f"Linha {row + 1}, coluna {col + 1}")
                cell.setStyleSheet("background:#18263b;border:1px solid #293751;border-radius:3px;font-size:8pt;")
                self.board.addWidget(cell, row, col)
                self.cells.append(cell)
        root.addLayout(self.board)
        self.last_action = QLabel("Última ação: —")
        self.last_action.setWordWrap(True)
        self.last_action.setObjectName("muted")
        root.addWidget(self.last_action)
        self.clicked = False

    def mousePressEvent(self, event):
        self.selected.emit(self.player_id)
        super().mousePressEvent(event)

    def set_selected(self, selected):
        self.setProperty("selected", bool(selected))
        self.style().unpolish(self)
        self.style().polish(self)

    def update_player(self, player, audit, action, finished=False):
        self.status.setText("ELIMINADO" if player.get("eliminated") or not player.get("alive", True) else ("FINALIZADO" if finished else "VIVO"))
        hp = _value(player, "hp", default="?")
        gold = _value(player, "gold", default="?")
        level = _value(player, "level", default="?")
        xp = _value(player, "xp", default="?")
        self.metrics.setText(f"HP {hp}   OURO {gold}   NV {level}   XP {xp}")
        board = audit.get("board", [])
        for i, cell in enumerate(self.cells):
            unit = board[i] if i < len(board) else None
            occupied = unit and unit.get("occupied", False)
            cell.setText(_format_unit(unit) if occupied else "·")
            cell.setStyleSheet(
                "background:#164e63;border:1px solid #0e7490;border-radius:3px;font-size:8pt;"
                if occupied else
                "background:#18263b;border:1px solid #293751;border-radius:3px;font-size:8pt;"
            )
            if occupied:
                cell.setToolTip(f"Posição {i}: {unit.get('champion_id')} | ⭐ {unit.get('star')} | UUID {unit.get('uuid')}")
            else:
                cell.setToolTip(f"Posição {i} vazia")
        if action:
            name = ACTION_NAMES.get(action[0], "UNKNOWN")
            self.last_action.setText(f"Última ação: {name} {action[1:]}")
        else:
            self.last_action.setText("Última ação: —")


class ViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TFT Viewer — PPO Observer")
        self.resize(1600, 1000)
        self.session = ViewerSession()
        self.selected_player = 0
        self._step_thread = None
        self._step_worker = None
        self._step_round_target = None
        self.play_timer = QTimer(self)
        self.play_timer.timeout.connect(self._on_play_tick)
        self._build_ui()
        self._log("Visualizador pronto. Selecione um checkpoint treinado para iniciar.")
        self._set_running(False)

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)

        top = QHBoxLayout()
        title = QLabel("TFT VIEWER")
        title.setStyleSheet("font-size:20pt;font-weight:800;color:#60a5fa;")
        subtitle = QLabel("8 agentes PPO · inferência somente · engine C++")
        subtitle.setObjectName("muted")
        top.addWidget(title)
        top.addWidget(subtitle)
        top.addStretch()
        self.round_label = QLabel("SEM PARTIDA")
        self.round_label.setStyleSheet("font-weight:700;color:#fbbf24;")
        top.addWidget(self.round_label)
        layout.addLayout(top)

        config = QGroupBox("Sessão de avaliação")
        form = QHBoxLayout(config)
        self.checkpoint = QLineEdit()
        self.checkpoint.setPlaceholderText("Checkpoint .pth / .pt")
        browse = QPushButton("Selecionar checkpoint…")
        browse.clicked.connect(self._choose_checkpoint)
        self.seed = QSpinBox()
        self.seed.setRange(0, 2_147_483_647)
        self.seed.setValue(20261016)
        self.deterministic = QCheckBox("Inferência determinística")
        self.deterministic.setChecked(True)
        self.record = QCheckBox("Gravar replay JSONL")
        self.record.setChecked(True)
        self.output_dir = QLineEdit(str(ROOT / "viewer" / "sessions"))
        output_browse = QPushButton("Pasta…")
        output_browse.clicked.connect(self._choose_output)
        form.addWidget(QLabel("Checkpoint"))
        form.addWidget(self.checkpoint, 3)
        form.addWidget(browse)
        form.addWidget(QLabel("Seed"))
        form.addWidget(self.seed)
        form.addWidget(self.deterministic)
        form.addWidget(self.record)
        form.addWidget(self.output_dir, 2)
        form.addWidget(output_browse)
        self.load_button = QPushButton("Carregar modelo")
        self.load_button.clicked.connect(self._load_session)
        form.addWidget(self.load_button)
        layout.addWidget(config)

        controls = QHBoxLayout()
        self.start_button = QPushButton("▶ Iniciar")
        self.start_button.clicked.connect(self._start_play)
        self.pause_button = QPushButton("Ⅱ Pausar")
        self.pause_button.clicked.connect(self._pause_play)
        self.step_button = QPushButton("⏭ Avançar passo conjunto")
        self.step_button.clicked.connect(self._step_once)
        self.round_button = QPushButton("⏩ Avançar rodada")
        self.round_button.clicked.connect(self._step_round)
        self.speed = QComboBox()
        self.speed.addItems(["0.25×", "0.5×", "1×", "2×", "4×"])
        self.speed.setCurrentText("1×")
        self.speed.currentTextChanged.connect(self._speed_changed)
        self.replay_button = QPushButton("Abrir replay…")
        self.replay_button.clicked.connect(self._open_replay)
        controls.addWidget(self.start_button)
        controls.addWidget(self.pause_button)
        controls.addWidget(self.step_button)
        controls.addWidget(self.round_button)
        controls.addWidget(QLabel("Velocidade visual"))
        controls.addWidget(self.speed)
        controls.addStretch()
        controls.addWidget(self.replay_button)
        layout.addLayout(controls)

        self.replay_slider = QSlider(Qt.Orientation.Horizontal)
        self.replay_slider.setRange(0, 0)
        self.replay_slider.setVisible(False)
        self.replay_slider.valueChanged.connect(self._show_replay_event)
        layout.addWidget(self.replay_slider)

        split = QSplitter(Qt.Orientation.Vertical)
        top_panel = QWidget()
        top_layout = QVBoxLayout(top_panel)
        top_layout.setContentsMargins(0, 0, 0, 0)
        self.cards = []
        grid = QGridLayout()
        grid.setSpacing(8)
        for player_id in range(8):
            card = PlayerCard(player_id)
            card.selected.connect(self._select_player)
            self.cards.append(card)
            grid.addWidget(card, player_id // 4, player_id % 4)
        top_layout.addLayout(grid)
        split.addWidget(top_panel)

        bottom_panel = QWidget()
        bottom_layout = QVBoxLayout(bottom_panel)
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget()
        detail_tab = QWidget()
        detail_layout = QHBoxLayout(detail_tab)
        self.detail_board = QGridLayout()
        self.detail_cells = []
        board_frame = QGroupBox("Tabuleiro ampliado · 7×4")
        board_layout = QVBoxLayout(board_frame)
        board_layout.addLayout(self.detail_board)
        for row in range(4):
            for col in range(7):
                cell = QLabel("·")
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setMinimumSize(62, 45)
                cell.setStyleSheet("background:#18263b;border:1px solid #334155;border-radius:4px;")
                cell.setToolTip(f"Posição {row * 7 + col}")
                self.detail_board.addWidget(cell, row, col)
                self.detail_cells.append(cell)
        detail_layout.addWidget(board_frame, 2)
        side = QVBoxLayout()
        self.player_summary = QLabel("Selecione um jogador.")
        self.player_summary.setWordWrap(True)
        side.addWidget(self.player_summary)
        self.roster = QPlainTextEdit()
        self.roster.setReadOnly(True)
        side.addWidget(self.roster, 1)
        self.policy_log = QPlainTextEdit()
        self.policy_log.setReadOnly(True)
        side.addWidget(QLabel("Diagnóstico da política"))
        side.addWidget(self.policy_log, 2)
        detail_layout.addLayout(side, 1)
        self.tabs.addTab(detail_tab, "Jogador selecionado")

        combat_tab = QWidget()
        combat_layout = QVBoxLayout(combat_tab)
        self.combat_title = QLabel("Combate detalhado")
        combat_layout.addWidget(self.combat_title)
        self.combat_units = QPlainTextEdit()
        self.combat_units.setReadOnly(True)
        combat_layout.addWidget(self.combat_units, 1)
        self.combat_events = QPlainTextEdit()
        self.combat_events.setReadOnly(True)
        combat_layout.addWidget(QLabel("Eventos fornecidos pela engine"))
        combat_layout.addWidget(self.combat_events, 1)
        self.tabs.addTab(combat_tab, "Combate / timeline")

        logs_tab = QWidget()
        logs_layout = QVBoxLayout(logs_tab)
        filters = QHBoxLayout()
        self.log_player_filter = QComboBox()
        self.log_player_filter.addItems(["Todos os jogadores"] + [f"Jogador {i + 1}" for i in range(8)])
        self.log_player_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_type_filter = QComboBox()
        self.log_type_filter.addItems(["Todos os eventos", "decision_batch", "step_completed", "match_started", "match_finished"])
        self.log_type_filter.currentIndexChanged.connect(self._refresh_log_view)
        filters.addWidget(self.log_player_filter)
        filters.addWidget(self.log_type_filter)
        logs_layout.addLayout(filters)
        self.events_log = QPlainTextEdit()
        self.events_log.setReadOnly(True)
        logs_layout.addWidget(self.events_log)
        self.tabs.addTab(logs_tab, "Eventos / auditoria")
        split.addWidget(self.tabs)
        split.setSizes([520, 430])
        layout.addWidget(split, 1)

        footer = QHBoxLayout()
        self.status_label = QLabel("Aguardando checkpoint")
        self.status_label.setObjectName("muted")
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setVisible(False)
        footer.addWidget(self.status_label, 2)
        footer.addWidget(self.progress, 1)
        layout.addLayout(footer)
        self.setStyleSheet(APP_STYLE)

    def _choose_checkpoint(self):
        path, _ = QFileDialog.getOpenFileName(self, "Selecionar checkpoint PPO", str(ROOT), "Checkpoints (*.pth *.pt *.ckpt);;Todos os arquivos (*)")
        if path:
            self.checkpoint.setText(path)

    def _choose_output(self):
        path = QFileDialog.getExistingDirectory(self, "Pasta de gravação", self.output_dir.text())
        if path:
            self.output_dir.setText(path)

    def _load_session(self):
        if not self.checkpoint.text().strip():
            QMessageBox.warning(self, "Checkpoint necessário", "Selecione um checkpoint PPO treinado.")
            return
        try:
            snapshot = self.session.load_checkpoint(
                self.checkpoint.text().strip(), self.seed.value(),
                self.deterministic.isChecked(), self.output_dir.text(),
                record=self.record.isChecked(),
            )
            self._log(f"Checkpoint carregado: SHA-256 {self.session.checkpoint_sha256}")
            self._log("Modo de inferência: " + ("determinístico" if self.deterministic.isChecked() else "estocástico"))
            self._render_snapshot(snapshot)
            self._set_running(True)
            self.status_label.setText("Modelo em eval() · gradientes desativados · sem PPOTrainer/optimizer")
        except Exception as exc:
            QMessageBox.critical(self, "Falha ao carregar sessão", str(exc))
            self._log(f"ERRO ao carregar sessão: {exc}")

    def _start_play(self):
        if not self.session.started:
            self._load_session()
            if not self.session.started:
                return
        interval = self._interval_ms()
        self.play_timer.start(interval)
        self.status_label.setText("Execução automática; a pausa ocorre entre passos conjuntos do lobby.")

    def _pause_play(self):
        self.play_timer.stop()
        self.status_label.setText("Pausado entre passos conjuntos.")

    def _step_once(self):
        if not self.session.started:
            QMessageBox.information(self, "Sessão necessária", "Carregue um checkpoint antes de avançar.")
            return
        self.play_timer.stop()
        self._advance_once()

    def _step_round(self):
        if not self.session.started:
            return
        self.play_timer.stop()
        self._step_round_target = self.session.public_state.get("round", 0)
        self._advance_once()

    def _on_play_tick(self):
        self._advance_once()

    def _advance_once(self):
        if self._step_thread is not None and self._step_thread.isRunning():
            return
        if not self.session.started or self.session.finished:
            return
        self._step_thread = QThread(self)
        self._step_worker = StepWorker(self.session)
        self._step_worker.moveToThread(self._step_thread)
        self._step_thread.started.connect(self._step_worker.run)
        self._step_worker.completed.connect(self._on_step_completed)
        self._step_worker.failed.connect(self._on_step_failed)
        self._step_worker.completed.connect(self._step_thread.quit)
        self._step_worker.failed.connect(self._step_thread.quit)
        self._step_thread.finished.connect(self._cleanup_step_worker)
        self._step_thread.start()

    def _on_step_completed(self, snapshot):
        self._render_snapshot(snapshot)
        if self.session.finished:
            self.play_timer.stop()
            self._step_round_target = None
            self.status_label.setText("Partida encerrada. Replay salvo; inferência não alterou os pesos.")
        elif self._step_round_target is not None:
            current_round = self.session.public_state.get("round", 0)
            if current_round == self._step_round_target:
                QTimer.singleShot(10, self._advance_once)
            else:
                self._step_round_target = None
                self.status_label.setText(f"Rodada avançada para {current_round}.")

    def _on_step_failed(self, message):
        self.play_timer.stop()
        self._step_round_target = None
        QMessageBox.critical(self, "Erro durante a partida", message)
        self._log(f"ERRO de execução: {message}")

    def _cleanup_step_worker(self):
        if self._step_worker is not None:
            self._step_worker.deleteLater()
        if self._step_thread is not None:
            self._step_thread.deleteLater()
        self._step_worker = None
        self._step_thread = None

    def _interval_ms(self):
        speed = float(self.speed.currentText().replace("×", ""))
        return max(20, int(700 / speed))

    def _speed_changed(self, _):
        if self.play_timer.isActive():
            self.play_timer.start(self._interval_ms())

    def _select_player(self, player_id: int):
        self.selected_player = player_id
        for card in self.cards:
            card.set_selected(card.player_id == player_id)
        self._render_selected_player()
        self.tabs.setCurrentIndex(0)

    def _render_snapshot(self, _snapshot=None):
        state_players = self.session.public_state.get("players", [])
        audit_players = self.session.audit_snapshot.get("players", [])
        by_id = {int(p.get("player_id", i)): p for i, p in enumerate(state_players)}
        audit_by_id = {int(p.get("player_id", i)): p for i, p in enumerate(audit_players)}
        for i, card in enumerate(self.cards):
            card.update_player(by_id.get(i, {}), audit_by_id.get(i, {}), self.session.last_actions[i], self.session.finished)
            card.set_selected(i == self.selected_player)
        self.round_label.setText(
            f"ROUND {self.session.public_state.get('round', 0)} · STAGE {self.session.public_state.get('stage', 1)}"
            + (" · FINALIZADO" if self.session.finished else "")
        )
        self._render_selected_player()
        self._render_combat()
        self._refresh_log_view()

    def _render_selected_player(self):
        i = self.selected_player
        state_players = self.session.public_state.get("players", [])
        audit_players = self.session.audit_snapshot.get("players", [])
        player = next((p for p in state_players if int(p.get("player_id", -1)) == i), {})
        audit = next((p for p in audit_players if int(p.get("player_id", -1)) == i), {})
        board = audit.get("board", [])
        for index, cell in enumerate(self.detail_cells):
            unit = board[index] if index < len(board) else None
            occupied = unit and unit.get("occupied", False)
            cell.setText(_format_unit(unit) if occupied else "·")
            cell.setToolTip(f"Posição {index}: {unit.get('champion_id') if occupied else 'vazia'}")
        self.player_summary.setText(
            f"JOGADOR {i + 1}\nHP: {_value(player, 'hp', default='—')}\n"
            f"Ouro: {_value(player, 'gold', default='—')}\nNível: {_value(player, 'level', default='—')} · "
            f"XP: {_value(player, 'xp', default='—')}\nColocação: {_value(player, 'placement', default='—')}\n"
            f"Sinergias/traços detalhados: indisponíveis no snapshot público atual."
        )
        lines = ["TABULEIRO:"]
        lines.extend(f"  {index:02d}: {unit_label(u)}" for index, u in enumerate(board) if u and u.get("occupied"))
        lines.append("\nBANCO:")
        lines.extend(f"  {index:02d}: {unit_label(u)}" for index, u in enumerate(audit.get("bench", [])) if u and u.get("occupied"))
        lines.append("\nLOJA:")
        lines.extend(f"  {index:02d}: {unit_label(u)}" for index, u in enumerate(audit.get("shop", [])) if u and u.get("occupied"))
        self.roster.setPlainText("\n".join(lines))
        diag = self.session.last_policy[i] if i < len(self.session.last_policy) else {}
        if diag:
            self.policy_log.setPlainText(json.dumps(diag, ensure_ascii=False, indent=2))
        else:
            self.policy_log.setPlainText("Sem diagnóstico de decisão para este assento neste passo.")
        self._refresh_log_view()

    def _render_combat(self):
        state_players = self.session.public_state.get("players", [])
        selected = next((p for p in state_players if int(p.get("player_id", -1)) == self.selected_player), {})
        matchups = self.session.public_state.get("matchups", [])
        self.combat_title.setText(
            f"Confronto do jogador {self.selected_player + 1} · round {self.session.public_state.get('round', 0)}"
        )
        if matchups:
            self.combat_units.setPlainText(json.dumps(matchups, ensure_ascii=False, indent=2))
        else:
            self.combat_units.setPlainText(
                "A engine não fornece, neste snapshot, um roster de combate pareado com posições/HP por evento. "
                "Nenhum HP, trajetória ou habilidade é inferido artificialmente.\n\n"
                + json.dumps({"jogador_selecionado": selected, "eventos_reais": self.session.last_info.get("events", [])}, ensure_ascii=False, indent=2)
            )
        self.combat_events.setPlainText(json.dumps(self.session.last_info.get("events", []), ensure_ascii=False, indent=2))

    def _log(self, message: str):
        self.events_log.appendPlainText(message)

    def _refresh_log_view(self):
        # Human-readable live audit summary; raw JSONL remains the authoritative full event stream.
        if not hasattr(self, "events_log"):
            return
        player_filter = self.log_player_filter.currentIndex() - 1 if hasattr(self, "log_player_filter") else -1
        type_filter = self.log_type_filter.currentText() if hasattr(self, "log_type_filter") else "Todos os eventos"
        # Session's visible recent events are rebuilt from the persisted JSONL when available.
        events = self.session.replay_events[:]
        if self.session._metadata_path:
            event_file = self.session._metadata_path.parent / "events.jsonl"
            if event_file.is_file():
                try:
                    events = [json.loads(line) for line in event_file.read_text(encoding="utf-8").splitlines() if line.strip()]
                except (OSError, json.JSONDecodeError):
                    events = []
        filtered = []
        for event in events:
            if type_filter != "Todos os eventos" and event.get("event_type") != type_filter:
                continue
            if player_filter >= 0:
                players = event.get("payload", {}).get("players", [])
                if not any(int(p.get("player_id", -1)) == player_filter for p in players):
                    continue
            filtered.append(event)
        self.events_log.setPlainText("\n".join(
            f"#{e.get('sequence_id')} · {e.get('event_type')} · R{e.get('round')} S{e.get('stage')}"
            for e in filtered[-500:]
        ) or "Nenhum evento corresponde aos filtros.")

    def _open_replay(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir replay JSONL", str(ROOT / "viewer" / "sessions"), "JSONL (*.jsonl);;Todos os arquivos (*)")
        if not path:
            return
        try:
            count = self.session.load_replay(path)
            self._log(f"Replay carregado: {count} eventos.")
            self.status_label.setText("Modo replay: leitura dos eventos gravados, sem executar política.")
            self._set_running(False)
            self.replay_events = self.session.replay_events
            self.replay_slider.setRange(0, max(0, count - 1))
            self.replay_slider.setValue(0)
            self.replay_slider.setVisible(True)
            self._show_replay_event(0)
        except Exception as exc:
            QMessageBox.critical(self, "Replay inválido", str(exc))

    def _show_replay_event(self, index):
        event = self.session.replay_event(index)
        if event is None:
            return
        self.replay_slider.blockSignals(True)
        self.replay_slider.setValue(index)
        self.replay_slider.blockSignals(False)
        self.events_log.setPlainText(json.dumps(event, ensure_ascii=False, indent=2))
        self.round_label.setText(f"REPLAY · evento {event.get('sequence_id')} · {event.get('event_type')}")

    def _set_running(self, enabled):
        self.start_button.setEnabled(enabled)
        self.pause_button.setEnabled(enabled)
        self.step_button.setEnabled(enabled)
        self.round_button.setEnabled(enabled)

    def closeEvent(self, event):
        self.play_timer.stop()
        if self._step_thread is not None and self._step_thread.isRunning():
            self._step_thread.quit()
            self._step_thread.wait(5000)
        self.session.close()
        super().closeEvent(event)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = ViewerWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
