"""Desktop TFT Viewer — PySide6."""
from __future__ import annotations

import hashlib
import json
import sys
import traceback
from pathlib import Path

import numpy as np
import torch
from PySide6.QtCore import Qt, QTimer, Signal, QObject, QThread, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
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


def _compact_unit(unit):
    if not unit or not unit.get("occupied", True):
        return "·"
    name = str(unit.get("champion_id") or unit.get("apiName") or unit.get("api_name") or "?")
    short_name = name.split("_")[-1][:6]
    star = int(unit.get("star", 1) or 1)
    return f"{short_name}{star}★"


class ChampionIconLoader(QObject):
    """Loads champion portraits asynchronously and caches them on disk.

    The unit catalog contains CommunityDragon texture asset paths (.tex), not
    image URLs. These paths are resolved to their public PNG equivalents.
    """
    loaded = Signal(str)

    def __init__(self, catalog_path: Path, parent=None):
        super().__init__(parent)
        self._network = QNetworkAccessManager(self)
        self._pixmaps: dict[str, QPixmap] = {}
        self._pending: dict[str, tuple[list[str], int]] = {}
        self._failed: set[str] = set()
        self._assets: dict[str, tuple[str, list[str]]] = {}
        self._cache_dir = Path.home() / ".tft-viewer" / "champion-icons"
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            catalog = []

        for unit in catalog if isinstance(catalog, list) else []:
            if not isinstance(unit, dict):
                continue
            api_name = str(unit.get("apiName") or unit.get("characterName") or unit.get("name") or "")
            if not api_name:
                continue
            paths = []
            for field in ("tileIcon", "squareIcon", "icon"):
                value = unit.get(field)
                if not isinstance(value, str) or not value.strip():
                    continue
                asset_path = value.strip().replace("\\", "/").lstrip("/")
                if asset_path.lower().endswith(".tex"):
                    asset_path = asset_path[:-4] + ".png"
                elif not asset_path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                    continue
                # The JSON uses client asset paths; CommunityDragon publishes
                # the corresponding game assets as normal image files.
                url = "https://raw.communitydragon.org/latest/game/" + asset_path.lower()
                if url not in paths:
                    paths.append(url)
            if not paths:
                continue
            record = (api_name, paths)
            for alias in (api_name, unit.get("characterName"), unit.get("name")):
                if isinstance(alias, str) and alias:
                    self._assets[alias.casefold()] = record

    def pixmap_for(self, champion_id: str) -> QPixmap | None:
        record = self._assets.get(str(champion_id or "").casefold())
        if record is None:
            return None
        canonical, urls = record
        if canonical in self._pixmaps:
            return self._pixmaps[canonical]
        if canonical in self._failed or canonical in self._pending:
            return None

        # Reuse the first successfully cached URL if it exists.
        self._pending[canonical] = (urls, 0)
        self._try_url(canonical, urls, 0)
        return None

    def _try_url(self, canonical: str, urls: list[str], index: int):
        if index >= len(urls):
            self._pending.pop(canonical, None)
            self._failed.add(canonical)
            self.loaded.emit(canonical)
            return
        url = urls[index]
        cache_name = hashlib.sha256(url.encode("utf-8")).hexdigest() + ".img"
        cache_path = self._cache_dir / cache_name
        if cache_path.is_file():
            pixmap = QPixmap()
            if pixmap.loadFromData(cache_path.read_bytes()) and not pixmap.isNull():
                self._pixmaps[canonical] = pixmap
                self._pending.pop(canonical, None)
                self.loaded.emit(canonical)
                return

        self._pending[canonical] = (urls, index)
        request = QNetworkRequest(QUrl(url))
        reply = self._network.get(request)
        reply.finished.connect(
            lambda key=canonical, candidates=urls, candidate_index=index,
                   network_reply=reply, disk_path=cache_path:
                self._on_download_finished(
                    key, candidates, candidate_index, network_reply, disk_path
                )
        )

    def _on_download_finished(self, canonical, urls, index, reply, cache_path):
        data = bytes(reply.readAll())
        success = reply.error() == QNetworkReply.NetworkError.NoError
        reply.deleteLater()
        if success:
            pixmap = QPixmap()
            if pixmap.loadFromData(data) and not pixmap.isNull():
                try:
                    cache_path.write_bytes(data)
                except OSError:
                    pass
                self._pixmaps[canonical] = pixmap
                self._pending.pop(canonical, None)
                self.loaded.emit(canonical)
                return
        self._try_url(canonical, urls, index + 1)


class ChampionCell(QFrame):
    """Small champion portrait cell with a star badge and text fallback."""

    COST_COLORS = {
        1: "#9ca3af", 2: "#22c55e", 3: "#60a5fa",
        4: "#a78bfa", 5: "#f59e0b", 6: "#f472b6",
    }

    def __init__(self, min_width: int, min_height: int, parent=None):
        super().__init__(parent)
        self.setMinimumSize(min_width, min_height)
        self.setObjectName("championCell")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self._champion_id = ""
        self.image = QLabel("·", self)
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image.setStyleSheet("background:transparent;border:0;color:#94a3b8;font-size:8pt;")
        self.stars = QLabel("", self)
        self.stars.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.stars.setStyleSheet(
            "background:rgba(3,7,18,190);color:#fde047;font-size:6pt;font-weight:700;"
            "padding:0 1px;border:0;"
        )
        layout = QGridLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(0)
        layout.addWidget(self.image, 0, 0)
        layout.addWidget(self.stars, 0, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        self._set_empty_style()

    def _set_empty_style(self):
        self.setStyleSheet("QFrame#championCell { background:#18263b;border:1px solid #293751;border-radius:3px; }")
        self.image.setPixmap(QPixmap())
        self.image.setText("·")
        self.stars.setText("")

    def set_unit(self, unit: dict | None, icon_loader: ChampionIconLoader):
        if not unit or not unit.get("occupied", False):
            self._champion_id = ""
            self._set_empty_style()
            self.setToolTip("Posição vazia")
            return

        champion_id = str(unit.get("champion_id") or unit.get("apiName") or unit.get("api_name") or "")
        self._champion_id = champion_id
        star = max(1, min(3, int(unit.get("star", 1) or 1)))
        cost = int(unit.get("cost", 0) or 0)
        border = self.COST_COLORS.get(cost, "#38bdf8")
        self.setStyleSheet(
            f"QFrame#championCell {{ background:#0f172a;border:2px solid {border};border-radius:4px; }}"
        )
        self.setToolTip(f"{champion_id} · {'★' * star} · custo {cost or '?'}")
        pixmap = icon_loader.pixmap_for(champion_id)
        if pixmap is not None and not pixmap.isNull():
            size = max(16, min(self.width() - 4, self.height() - 4))
            self.image.setText("")
            self.image.setPixmap(pixmap.scaled(
                size, size,
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation,
            ))
            self.stars.setText("★" * star)
        else:
            self.image.setPixmap(QPixmap())
            self.image.setText(_compact_unit(unit))
            self.image.setStyleSheet(
                "background:transparent;border:0;color:#e5e7eb;font-size:7pt;font-weight:700;"
            )
            self.stars.setText("")


class StepWorker(QObject):
    completed = Signal(object)
    failed = Signal(str)

    def __init__(self, session):
        super().__init__()
        self.session = session

    def run(self):
        try:
            self.completed.emit(self.session.step())
        except Exception:
            self.failed.emit(traceback.format_exc())


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
                cell = ChampionCell(27, 22)
                cell.setToolTip(f"Linha {row + 1}, coluna {col + 1}")
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

    def update_player(self, player, audit, action, icon_loader, finished=False):
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
            cell.set_unit(unit if occupied else None, icon_loader)
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
        self.icon_loader = ChampionIconLoader(ROOT / "units_gerado.json", self)
        self.icon_loader.loaded.connect(self._on_champion_icon_loaded)
        self._step_thread = None
        self._step_worker = None
        self._step_round_target = None
        self._close_when_step_done = False
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
                cell = ChampionCell(62, 45)
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
        self.combat_title = QLabel("Último confronto registrado")
        self.combat_title.setStyleSheet("font-weight:700;color:#fbbf24;font-size:12pt;")
        combat_layout.addWidget(self.combat_title)

        # Dois tabuleiros para tornar visível o pareamento real da engine.
        # O adversário é espelhado horizontalmente para representar equipes frente a frente.
        matchup_row = QHBoxLayout()
        self.combat_team_labels = []
        self.combat_board_cells = []
        for team_index in range(2):
            panel = QFrame()
            panel.setObjectName("playerCard")
            panel_layout = QVBoxLayout(panel)
            team_label = QLabel("Aguardando pareamento")
            team_label.setStyleSheet("font-weight:700;color:#93c5fd;")
            panel_layout.addWidget(team_label)
            board = QGridLayout()
            board.setSpacing(3)
            cells = []
            for row in range(4):
                for col in range(7):
                    cell = ChampionCell(42, 30)
                    board.addWidget(cell, row, col)
                    cells.append(cell)
            panel_layout.addLayout(board)
            matchup_row.addWidget(panel)
            self.combat_team_labels.append(team_label)
            self.combat_board_cells.append(cells)
        combat_layout.addLayout(matchup_row, 2)

        self.combat_units = QPlainTextEdit()
        self.combat_units.setReadOnly(True)
        self.combat_units.setMaximumHeight(105)
        combat_layout.addWidget(self.combat_units)
        combat_layout.addWidget(QLabel("Eventos reais emitidos pela engine"))
        self.combat_events = QPlainTextEdit()
        self.combat_events.setReadOnly(True)
        combat_layout.addWidget(self.combat_events, 1)
        self.tabs.addTab(combat_tab, "Combate / timeline")

        logs_tab = QWidget()
        logs_layout = QVBoxLayout(logs_tab)
        filters = QHBoxLayout()
        self.log_player_filter = QComboBox()
        self.log_player_filter.addItems(["Todos os jogadores"] + [f"Jogador {i + 1}" for i in range(8)])
        self.log_player_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_type_filter = QComboBox()
        self.log_type_filter.addItems([
            "Todos os eventos", "decision_batch", "step_completed",
            "match_started", "match_finished", "diagnostic_warning",
            "diagnostic_error", "action_rejected", "action_failed",
        ])
        self.log_type_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_round_filter = QComboBox()
        self.log_round_filter.addItems(["Todos os rounds"])
        self.log_round_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_severity_filter = QComboBox()
        self.log_severity_filter.addItems(["Todas as gravidades", "Info", "Warning", "Error"])
        self.log_severity_filter.currentIndexChanged.connect(self._refresh_log_view)
        filters.addWidget(self.log_player_filter)
        filters.addWidget(self.log_type_filter)
        filters.addWidget(self.log_round_filter)
        filters.addWidget(self.log_severity_filter)
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
        # Do not replace the active reference until QThread.finished has been
        # handled on the GUI thread. isRunning() may be false before that
        # cleanup callback runs, which otherwise creates a close/use-after-free
        # race between consecutive steps.
        if self._step_thread is not None:
            return
        if not self.session.started or self.session.finished:
            return

        thread = QThread(self)
        worker = StepWorker(self.session)
        self._step_thread = thread
        self._step_worker = worker
        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.completed.connect(self._on_step_completed)
        worker.failed.connect(self._on_step_failed)
        # QThread.quit() is thread-safe. DirectConnection asks the event loop
        # to exit directly, without queueing behind the long-running worker slot.
        worker.completed.connect(thread.quit, Qt.ConnectionType.DirectConnection)
        worker.failed.connect(thread.quit, Qt.ConnectionType.DirectConnection)
        thread.finished.connect(self._cleanup_step_worker)
        thread.start()

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
        # Only release the exact thread that emitted finished. This avoids a
        # stale queued cleanup callback touching a newer worker/thread pair.
        thread = self.sender()
        if thread is None or thread is not self._step_thread:
            return

        worker = self._step_worker
        self._step_worker = None
        self._step_thread = None

        if worker is not None:
            worker.deleteLater()
        thread.deleteLater()

        if self._close_when_step_done:
            self._close_when_step_done = False
            QTimer.singleShot(0, self.close)

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
        events = self.session.last_info.get("events", [])
        in_combat = any(
            "COMBAT" in str(item).upper() or "ELIMINATED" in str(item).upper()
            for item in events
        )
        self.tabs.setCurrentIndex(1 if in_combat else 0)

    def _render_snapshot(self, _snapshot=None):
        state_players = self.session.public_state.get("players", [])
        audit_players = self.session.audit_snapshot.get("players", [])
        by_id = {int(p.get("player_id", i)): p for i, p in enumerate(state_players)}
        audit_by_id = {int(p.get("player_id", i)): p for i, p in enumerate(audit_players)}
        for i, card in enumerate(self.cards):
            card.update_player(
                by_id.get(i, {}), audit_by_id.get(i, {}), self.session.last_actions[i],
                self.icon_loader, self.session.finished
            )
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
            cell.set_unit(unit if occupied else None, self.icon_loader)
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
        audit_players = self.session.audit_snapshot.get("players", [])
        selected = next(
            (p for p in state_players if int(p.get("player_id", -1)) == self.selected_player), {}
        )
        selected_audit = next(
            (p for p in audit_players if int(p.get("player_id", -1)) == self.selected_player), {}
        )
        opponent_id = selected.get("opponent_id")
        try:
            opponent_id = int(opponent_id) if opponent_id is not None else None
        except (TypeError, ValueError):
            opponent_id = None

        if opponent_id is None:
            self.combat_title.setText(
                f"Jogador {self.selected_player + 1} · nenhum confronto registrado ainda"
            )
            self.combat_team_labels[0].setText(f"JOGADOR {self.selected_player + 1} · formação atual")
            self.combat_team_labels[1].setText("Adversário ainda não informado pela engine")
            self._clear_combat_boards()
            self.combat_units.setPlainText(
                "O pareamento só fica disponível depois que a engine resolve a primeira rodada de combate.\n"
                "A interface consulta o campo opponent_id real do estado público; ela não sorteia "
                "nem deduz adversários."
            )
        else:
            opponent = next(
                (p for p in state_players if int(p.get("player_id", -1)) == opponent_id), {}
            )
            opponent_audit = next(
                (p for p in audit_players if int(p.get("player_id", -1)) == opponent_id), {}
            )
            round_number = self.session.public_state.get("round", 0)
            self.combat_title.setText(
                f"ÚLTIMO CONFRONTO · JOGADOR {self.selected_player + 1} vs JOGADOR {opponent_id + 1}"
                f" · rodada atual {round_number}"
            )
            self.combat_team_labels[0].setText(
                f"JOGADOR {self.selected_player + 1} · HP {_value(selected, 'hp', default='—')}"
                f" · {'VIVO' if selected.get('alive', True) else 'ELIMINADO'}"
            )
            self.combat_team_labels[1].setText(
                f"JOGADOR {opponent_id + 1} · HP {_value(opponent, 'hp', default='—')}"
                f" · {'VIVO' if opponent.get('alive', True) else 'ELIMINADO'}"
            )
            self._render_combat_board(0, selected_audit.get("board", []), mirror=False)
            self._render_combat_board(1, opponent_audit.get("board", []), mirror=True)
            self.combat_units.setPlainText(
                f"Pareamento lido de PlayerInfo.opponent_id: {self.selected_player} ↔ {opponent_id}.\n"
                f"Placar do histórico: jogador {self.selected_player + 1} — "
                f"{_value(selected, 'wins', default=0)} vitória(s), {_value(selected, 'losses', default=0)} derrota(s); "
                f"jogador {opponent_id + 1} — {_value(opponent, 'wins', default=0)} vitória(s), "
                f"{_value(opponent, 'losses', default=0)} derrota(s).\n"
                "Os tabuleiros mostram as formações reais registradas. A engine ainda não exporta snapshots "
                "de HP/mana por frame; portanto, estes quadros não simulam uma animação inventada."
            )

        raw_events = self.session.last_info.get("events", [])
        if not raw_events:
            raw_events = ["Nenhum evento novo de combate retornado neste passo."]
        self.combat_events.setPlainText("\n".join(str(event) for event in raw_events))

    def _clear_combat_boards(self):
        for cells in self.combat_board_cells:
            for cell in cells:
                cell.set_unit(None, self.icon_loader)
                cell.setToolTip("Sem confronto disponível")

    def _render_combat_board(self, team_index, board_units, mirror=False):
        cells = self.combat_board_cells[team_index]
        for row in range(4):
            for col in range(7):
                source_col = 6 - col if mirror else col
                source_index = row * 7 + source_col
                unit = board_units[source_index] if source_index < len(board_units) else None
                cell = cells[row * 7 + col]
                occupied = bool(unit and unit.get("occupied", False))
                cell.set_unit(unit if occupied else None, self.icon_loader)
                cell.setToolTip(
                    f"Posição original {source_index}: {unit.get('champion_id')} · "
                    f"{unit.get('star', 1)} estrela(s)"
                    if occupied else f"Posição original {source_index}: vazia"
                )

    def _on_champion_icon_loaded(self, _champion_id: str):
        # Download is async; repaint existing cells when a cached portrait arrives.
        if hasattr(self, "cards"):
            self._render_snapshot()

    def _log(self, message: str):
        self.events_log.appendPlainText(message)

    def _refresh_log_view(self):
        # Human-readable live audit summary; raw JSONL remains the authoritative full event stream.
        if not hasattr(self, "events_log"):
            return
        player_filter = self.log_player_filter.currentIndex() - 1 if hasattr(self, "log_player_filter") else -1
        type_filter = self.log_type_filter.currentText() if hasattr(self, "log_type_filter") else "Todos os eventos"
        round_filter = self.log_round_filter.currentText() if hasattr(self, "log_round_filter") else "Todos os rounds"
        severity_filter = self.log_severity_filter.currentText() if hasattr(self, "log_severity_filter") else "Todas as gravidades"
        # Session's visible recent events are rebuilt from the persisted JSONL when available.
        events = (self.session.replay_events[:] if self.session.replay_mode
                  else self.session.live_events[:])
        if self.session._metadata_path:
            event_file = self.session._metadata_path.parent / "events.jsonl"
            if event_file.is_file():
                try:
                    events = [json.loads(line) for line in event_file.read_text(encoding="utf-8").splitlines() if line.strip()]
                except (OSError, json.JSONDecodeError):
                    events = []
        available_rounds = sorted({int(e.get("round", 0)) for e in events})
        current_round = self.log_round_filter.currentText() if hasattr(self, "log_round_filter") else "Todos os rounds"
        if hasattr(self, "log_round_filter"):
            desired = ["Todos os rounds"] + [str(value) for value in available_rounds]
            if [self.log_round_filter.itemText(i) for i in range(self.log_round_filter.count())] != desired:
                self.log_round_filter.blockSignals(True)
                self.log_round_filter.clear()
                self.log_round_filter.addItems(desired)
                self.log_round_filter.setCurrentText(current_round if current_round in desired else "Todos os rounds")
                self.log_round_filter.blockSignals(False)
        filtered = []
        def event_severity(event):
            kind = event.get("event_type", "")
            if kind in {"diagnostic_error", "action_failed"}:
                return "Error"
            if kind in {"diagnostic_warning", "action_rejected", "anti_loop_detected", "anti_loop_blocked"}:
                return "Warning"
            return "Info"
        for event in events:
            if type_filter != "Todos os eventos" and event.get("event_type") != type_filter:
                continue
            if round_filter != "Todos os rounds" and str(event.get("round", 0)) != round_filter:
                continue
            if severity_filter != "Todas as gravidades" and event_severity(event) != severity_filter:
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
        if self._step_thread is not None:
            # A native step may be executing inside C++; do not close its
            # engine concurrently or destroy its QThread after an arbitrary
            # timeout. Defer closing until the worker actually exits.
            self._close_when_step_done = True
            self._set_running(False)
            self.status_label.setText(
                "Finalizando o passo atual com segurança antes de fechar…"
            )
            if self._step_thread.isRunning():
                self._step_thread.quit()
            event.ignore()
            return

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
