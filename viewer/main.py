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
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QBoxLayout, QGridLayout,
    QFrame, QLabel, QPushButton, QComboBox, QCheckBox, QDoubleSpinBox,
    QSpinBox, QFileDialog, QLineEdit, QPlainTextEdit, QSplitter, QTabWidget,
    QMessageBox, QScrollArea, QGroupBox, QProgressBar, QSlider, QFormLayout, QDialog,
)

from viewer.session import ViewerSession, unit_label, ACTION_NAMES, ROOT
from viewer.composition_plan import summarize_planned_traits, suggest_initial_positions, is_position_misplaced

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


def _composition_focus_weights_text(strategy):
    weights = strategy.get("composition_focus_weights") or {}
    if not isinstance(weights, dict):
        return "—"
    ranked = sorted(weights.items(), key=lambda item: float(item[1] or 0.0), reverse=True)[:5]
    return ", ".join(f"{name} {float(weight or 0.0):.2f}" for name, weight in ranked) or "—"


def _composition_status_text(strategy):
    locked = bool(strategy.get("composition_locked", False))
    lock_text = "LOCKED" if locked else "OPEN"
    strength = float(strategy.get("composition_strength", 0.0) or 0.0)
    direction = strategy.get("composition_direction") or "—"
    focus = strategy.get("composition_focus") or "—"
    weights = _composition_focus_weights_text(strategy)
    return (
        f"Comp direction: {direction} | Lock: {lock_text} | "
        f"Strength: {strength:.2f} | Focus: {focus} | Focus weights: {weights}"
    )


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
        self._profiles: dict[str, dict] = {}
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
            profile = dict(unit.get("combat_profile") or {})
            profile.setdefault("role_name", unit.get("role_name") or "")
            for alias in (api_name, unit.get("characterName"), unit.get("name")):
                if isinstance(alias, str) and alias:
                    self._profiles[alias.casefold()] = profile
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

    def profile_for(self, champion_id: str) -> dict:
        return self._profiles.get(str(champion_id or "").casefold(), {})

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

    ROW_BACKGROUNDS = ("#183b3a", "#173044", "#292747", "#30213d")

    def __init__(self, min_width: int, min_height: int, parent=None):
        super().__init__(parent)
        initial_size = max(20, int(min_width), int(min_height))
        self.setFixedSize(initial_size, initial_size)
        self.setObjectName("championCell")
        self._board_row = 0
        self._position_warning = False
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self._champion_id = ""
        self._last_unit = None
        self._icon_loader = None
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

    def set_square_size(self, size: int):
        """Keep the tile and rendered portrait square at the chosen pixel size."""
        size = max(20, int(size))
        if self.width() == size and self.height() == size:
            return
        self.setFixedSize(size, size)
        if self._icon_loader is not None:
            # Re-scale an already loaded portrait as soon as the cell changes size.
            self.set_unit(self._last_unit, self._icon_loader)

    def set_board_row(self, row: int):
        self._board_row = max(0, min(3, int(row)))
        self._apply_cell_style()
        
    def _apply_cell_style(self, cost_color: str | None = None):
        background = self.ROW_BACKGROUNDS[self._board_row]
        if self._position_warning:
            # The red ring is intentionally independent of cost color.
            border, border_width, radius = "#ef4444", 3, max(8, self.width() // 2)
        elif cost_color:
            border, border_width, radius = cost_color, 2, 4
        else:
            border, border_width, radius = "#3b506b", 1, 4
        self.setStyleSheet(
            f"QFrame#championCell {{ background:{background};"
            f"border:{border_width}px solid {border};border-radius:{radius}px; }}"
        )
        # Keep the champion portrait inside the warning ring so the red circle
        # remains visible even at the smallest responsive cell size.
        margin = 4 if self._position_warning else 1
        self.layout().setContentsMargins(margin, margin, margin, margin)

    def _set_empty_style(self):
        self._position_warning = False
        self._apply_cell_style()
        self.image.setPixmap(QPixmap())
        self.image.setText("·")
        self.image.setStyleSheet("background:transparent;border:0;color:#94a3b8;font-size:8pt;")
        self.stars.setText("")

    def set_unit(self, unit: dict | None, icon_loader: ChampionIconLoader,
                 position_warning: bool = False):
        self._last_unit = dict(unit) if unit and unit.get("occupied", False) else None
        self._icon_loader = icon_loader
        self._position_warning = bool(position_warning and self._last_unit)
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
        self._apply_cell_style(border)
        role = icon_loader.profile_for(champion_id).get("role_name") or "papel desconhecido"
        warning_text = " · POSICIONAMENTO SUSPEITO (linha frontal/traseira)" if self._position_warning else ""
        self.setToolTip(f"{champion_id} · {role} · {'★' * star} · custo {cost or '?'}{warning_text}")
        pixmap = icon_loader.pixmap_for(champion_id)
        if pixmap is not None and not pixmap.isNull():
            size = max(16, min(self.width(), self.height()) - 4)
            self.image.setStyleSheet("background:transparent;border:0;")
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
    composition_requested = Signal(int)

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
        strategy_row = QHBoxLayout()
        self.strategy_line = QLabel("Strategy: — | Comp direction: —")
        self.strategy_line.setWordWrap(True)
        self.strategy_line.setObjectName("muted")
        strategy_row.addWidget(self.strategy_line, 1)
        self.composition_button = QPushButton("Ver composição")
        self.composition_button.setToolTip("Ver unidades planejadas, sinergias e prévia de posicionamento")
        self.composition_button.setVisible(False)
        self.composition_button.setMaximumWidth(150)
        self.composition_button.clicked.connect(
            lambda _checked=False: self.composition_requested.emit(self.player_id)
        )
        strategy_row.addWidget(self.composition_button, 0, Qt.AlignmentFlag.AlignVCenter)
        root.addLayout(strategy_row)
        self.board = QGridLayout()
        self.board.setContentsMargins(0, 0, 0, 0)
        self.board.setSpacing(2)
        for col in range(7):
            self.board.setColumnStretch(col, 1)
        self.cells = []
        for row in range(4):
            for col in range(7):
                cell = ChampionCell(27, 27)
                cell.set_board_row(row)
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
        strategy = audit.get("strategy_info") or {}
        strategy_name = strategy.get("strategy_name") or "ECON"
        self.strategy_line.setText(
            f"Strategy: {strategy_name}\n{_composition_status_text(strategy)}"
        )
        has_plan = bool(strategy.get("planned_units"))
        self.composition_button.setVisible(has_plan)
        self.composition_button.setEnabled(has_plan)
        board = audit.get("board", [])
        for i, cell in enumerate(self.cells):
            unit = board[i] if i < len(board) else None
            occupied = unit and unit.get("occupied", False)
            row = i // 7
            profile = icon_loader.profile_for(
                (unit or {}).get("champion_id") or (unit or {}).get("apiName") or (unit or {}).get("api_name") or ""
            ) if occupied else {}
            role_unit = {
                "role_name": profile.get("role_name", ""),
                "combat_profile": profile,
            }
            misplaced = bool(occupied and is_position_misplaced(role_unit, row))
            cell.set_unit(unit if occupied else None, icon_loader, position_warning=misplaced)
            if occupied:
                location = "FRONT" if row <= 1 else "BACK"
                warning = " · ⚠ POSIÇÃO INADEQUADA" if misplaced else ""
                cell.setToolTip(
                    f"Posição {i} · {location}: {unit.get('champion_id')} | "
                    f"papel {profile.get('role_name') or 'desconhecido'} | "
                    f"⭐ {unit.get('star')} | UUID {unit.get('uuid')}{warning}"
                )
            else:
                cell.setToolTip(f"Posição {i} vazia · {'FRONT' if row <= 1 else 'BACK'}")
        if action:
            name = ACTION_NAMES.get(action[0], "UNKNOWN")
            self.last_action.setText(f"Última ação: {name} {action[1:]}")
        else:
            self.last_action.setText("Última ação: —")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        QTimer.singleShot(0, self._sync_board_cell_size)

    def _sync_board_cell_size(self):
        width = self.board.geometry().width()
        if width <= 0:
            return
        gap = max(0, self.board.horizontalSpacing())
        size = max(16, min(38, (width - gap * 6) // 7))
        for cell in self.cells:
            cell.set_square_size(size)


class ViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TFT Viewer — PPO Observer")
        self.resize(1280, 820)
        self.setMinimumSize(640, 480)
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
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        central = QWidget()
        central.setMinimumWidth(0)
        self.scroll_area.setWidget(central)
        self.setCentralWidget(self.scroll_area)
        self.content_widget = central
        layout = QVBoxLayout(central)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)

        top = QHBoxLayout()
        title = QLabel("TFT VIEWER")
        title.setStyleSheet("font-size:20pt;font-weight:800;color:#60a5fa;")
        self.viewer_title = title
        self.viewer_subtitle = QLabel("8 agentes PPO · inferência somente · engine C++")
        self.viewer_subtitle.setObjectName("muted")
        self.viewer_subtitle.setWordWrap(True)
        top.addWidget(title)
        top.addWidget(self.viewer_subtitle)
        top.addStretch()
        self.round_label = QLabel("SEM PARTIDA")
        self.round_label.setStyleSheet("font-weight:700;color:#fbbf24;")
        top.addWidget(self.round_label)
        layout.addLayout(top)

        config = QGroupBox("Sessão de avaliação")
        form = QGridLayout(config)
        self.checkpoint = QLineEdit()
        self.checkpoint.setMinimumWidth(0)
        self.checkpoint.setPlaceholderText("Checkpoint .pth / .pt")
        browse = QPushButton("Selecionar checkpoint…")
        browse.clicked.connect(self._choose_checkpoint)
        self.seed = QSpinBox()
        self.seed.setRange(0, 2_147_483_647)
        self.seed.setValue(20261016)
        self.deterministic = QCheckBox("Inferência determinística")
        self.deterministic.setChecked(True)
        self.record = QCheckBox("Salvar logs JSON por jogador")
        self.record.setChecked(True)
        self.output_dir = QLineEdit(str(ROOT / "viewer" / "sessions"))
        self.output_dir.setMinimumWidth(0)
        output_browse = QPushButton("Pasta…")
        output_browse.clicked.connect(self._choose_output)
        self.load_button = QPushButton("Carregar modelo")
        self.load_button.clicked.connect(self._load_session)

        form.addWidget(QLabel("Checkpoint"), 0, 0)
        form.addWidget(self.checkpoint, 0, 1, 1, 3)
        form.addWidget(browse, 0, 4)
        form.addWidget(self.load_button, 0, 5)
        form.addWidget(QLabel("Seed"), 1, 0)
        form.addWidget(self.seed, 1, 1)
        form.addWidget(self.deterministic, 1, 2, 1, 2)
        form.addWidget(self.record, 1, 4, 1, 2)
        form.addWidget(QLabel("Pasta de gravação"), 2, 0)
        form.addWidget(self.output_dir, 2, 1, 1, 4)
        form.addWidget(output_browse, 2, 5)
        for column in (1, 2, 3, 4):
            form.setColumnStretch(column, 1 if column < 4 else 0)
        layout.addWidget(config)

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
        speed_group = QWidget()
        speed_layout = QHBoxLayout(speed_group)
        speed_layout.setContentsMargins(0, 0, 0, 0)
        speed_layout.addWidget(QLabel("Velocidade visual"))
        speed_layout.addWidget(self.speed)
        self.replay_button = QPushButton("Abrir replay…")
        self.replay_button.clicked.connect(self._open_replay)
        self.control_items = [
            self.start_button, self.pause_button, self.step_button,
            self.round_button, speed_group, self.replay_button,
        ]
        self.controls_layout = QGridLayout()
        layout.addLayout(self.controls_layout)

        self.replay_slider = QSlider(Qt.Orientation.Horizontal)
        self.replay_slider.setRange(0, 0)
        self.replay_slider.setVisible(False)
        self.replay_slider.valueChanged.connect(self._show_replay_event)
        layout.addWidget(self.replay_slider)

        split = QSplitter(Qt.Orientation.Vertical)
        self.main_splitter = split
        split.setChildrenCollapsible(False)
        split.setHandleWidth(8)
        top_panel = QWidget()
        top_layout = QVBoxLayout(top_panel)
        top_layout.setContentsMargins(0, 0, 0, 0)
        self.cards = []
        self.player_grid = QGridLayout()
        self.player_grid.setContentsMargins(0, 0, 0, 0)
        self.player_grid.setSpacing(8)
        for player_id in range(8):
            card = PlayerCard(player_id)
            card.selected.connect(self._select_player)
            card.composition_requested.connect(self._show_composition_dialog)
            self.cards.append(card)
        top_layout.addLayout(self.player_grid)
        top_panel.setMinimumWidth(0)
        split.addWidget(top_panel)

        bottom_panel = QWidget()
        bottom_layout = QVBoxLayout(bottom_panel)
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget()
        detail_tab = QWidget()
        self.detail_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight, detail_tab)
        self.detail_board = QGridLayout()
        self.detail_board.setContentsMargins(0, 0, 0, 0)
        self.detail_board.setHorizontalSpacing(3)
        self.detail_board.setVerticalSpacing(3)
        for col in range(7):
            self.detail_board.setColumnStretch(col, 1)
        self.detail_cells = []
        self.detail_board_frame = QGroupBox("Tabuleiro ampliado · 7×4")
        board_frame = self.detail_board_frame
        board_layout = QVBoxLayout(board_frame)
        board_layout.addLayout(self.detail_board)
        for row in range(4):
            for col in range(7):
                cell = ChampionCell(62, 62)
                cell.setToolTip(f"Posição {row * 7 + col}")
                self.detail_board.addWidget(cell, row, col)
                self.detail_cells.append(cell)
        self.detail_layout.addWidget(board_frame, 2)
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
        self.detail_layout.addLayout(side, 1)
        self.tabs.addTab(detail_tab, "Jogador selecionado")

        combat_tab = QWidget()
        combat_layout = QVBoxLayout(combat_tab)
        self.combat_title = QLabel("Último confronto registrado")
        self.combat_title.setStyleSheet("font-weight:700;color:#fbbf24;font-size:12pt;")
        combat_layout.addWidget(self.combat_title)

        # Dois tabuleiros para tornar visível o pareamento real da engine.
        # O adversário é espelhado horizontalmente para representar equipes frente a frente.
        self.combat_matchup_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        self.combat_team_labels = []
        self.combat_board_cells = []
        self.combat_board_layouts = []
        self.combat_panels = []
        for team_index in range(2):
            panel = QFrame()
            panel.setObjectName("playerCard")
            self.combat_panels.append(panel)
            panel_layout = QVBoxLayout(panel)
            team_label = QLabel("Aguardando pareamento")
            team_label.setStyleSheet("font-weight:700;color:#93c5fd;")
            panel_layout.addWidget(team_label)
            board = QGridLayout()
            board.setContentsMargins(0, 0, 0, 0)
            board.setSpacing(3)
            for col in range(7):
                board.setColumnStretch(col, 1)
            cells = []
            for row in range(4):
                for col in range(7):
                    cell = ChampionCell(42, 42)
                    board.addWidget(cell, row, col)
                    cells.append(cell)
            panel_layout.addLayout(board)
            self.combat_matchup_layout.addWidget(panel)
            self.combat_team_labels.append(team_label)
            self.combat_board_cells.append(cells)
            self.combat_board_layouts.append(board)
        combat_layout.addLayout(self.combat_matchup_layout, 2)

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
        self.log_filters_layout = QGridLayout()
        self.log_filter_widgets = []
        self.log_player_filter = QComboBox()
        self.log_player_filter.addItems(["Todos os jogadores"] + [f"Jogador {i + 1}" for i in range(8)])
        self.log_player_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_type_filter = QComboBox()
        self.log_type_filter.addItems([
            "Todos os eventos", "action", "evolution", "round_finished",
            "board_view", "bench_view", "shop_view", "synergy_up",
            "synergy_down", "position_analysis", "decision_batch",
            "step_completed", "match_started", "match_finished",
            "diagnostic_warning", "diagnostic_error", "action_rejected", "action_failed",
        ])
        self.log_type_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_round_filter = QComboBox()
        self.log_round_filter.addItems(["Todos os rounds"])
        self.log_round_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_severity_filter = QComboBox()
        self.log_severity_filter.addItems(["Todas as gravidades", "Info", "Warning", "Error"])
        self.log_severity_filter.currentIndexChanged.connect(self._refresh_log_view)
        self.log_filter_widgets = [
            self.log_player_filter, self.log_type_filter,
            self.log_round_filter, self.log_severity_filter,
        ]
        for combo in self.log_filter_widgets:
            combo.setMinimumWidth(0)
        logs_layout.addLayout(self.log_filters_layout)
        self.events_log = QPlainTextEdit()
        self.events_log.setReadOnly(True)
        logs_layout.addWidget(self.events_log)
        self.tabs.addTab(logs_tab, "Eventos / auditoria")
        # Player details are now opened in a modal from the player card.
        # Keep the legacy widgets alive for snapshot updates, but remove the fixed bottom panel.
        self.tabs.removeTab(0)
        split.addWidget(self.tabs)
        # Let the splitter use the space left after the header/config/controls.
        # Sizing it from the entire scroll viewport double-counted those sections
        # and forced the page to scroll, hiding part of the viewer.
        split.setStretchFactor(0, 2)
        split.setStretchFactor(1, 3)
        split.setMinimumHeight(0)
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

        # Avoid horizontal scrolling in text views as well as in the page.
        for text_view in self.findChildren(QPlainTextEdit):
            text_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            text_view.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self._update_responsive_layout()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, "player_grid"):
            self._update_responsive_layout()

    @staticmethod
    def _reflow_grid(layout, widgets, columns):
        while layout.count():
            layout.takeAt(0)
        # Clear only previously-created columns; do not create extra empty
        # columns that could reserve spacing or trigger horizontal clipping.
        for column in range(layout.columnCount()):
            layout.setColumnStretch(column, 0)
        for column in range(columns):
            layout.setColumnStretch(column, 1)
        for index, widget in enumerate(widgets):
            layout.addWidget(widget, index // columns, index % columns)

    @staticmethod
    def _fit_square_cells(grid_layout, cells, max_size=96):
        width = grid_layout.geometry().width()
        if width <= 0:
            return
        gap = max(0, grid_layout.horizontalSpacing())
        size = max(20, min(max_size, (width - gap * 6) // 7))
        for cell in cells:
            cell.set_square_size(size)

    @staticmethod
    def _set_cell_squares(cells, size):
        for cell in cells:
            cell.set_square_size(size)

    def _sync_all_board_cells(self):
        for card in getattr(self, "cards", []):
            card._sync_board_cell_size()
        if hasattr(self, "detail_board"):
            self._fit_square_cells(self.detail_board, self.detail_cells, max_size=144)
        for board, cells in zip(
            getattr(self, "combat_board_layouts", []),
            getattr(self, "combat_board_cells", []),
        ):
            self._fit_square_cells(board, cells, max_size=128)

    def _update_responsive_layout(self):
        if not hasattr(self, "scroll_area") or not hasattr(self, "player_grid"):
            return
        width = max(1, self.scroll_area.viewport().width())

        # Fewer columns on compact screens give each unit portrait more room.
        player_columns = 1 if width < 720 else 2 if width < 1050 else 3 if width < 1450 else 4
        if getattr(self, "_player_columns", None) != player_columns:
            self._player_columns = player_columns
            self._reflow_grid(self.player_grid, self.cards, player_columns)

        control_columns = 2 if width < 760 else 3 if width < 1080 else 6
        if getattr(self, "_control_columns", None) != control_columns:
            self._control_columns = control_columns
            self._reflow_grid(self.controls_layout, self.control_items, control_columns)

        filter_columns = 2 if width < 900 else 4
        if getattr(self, "_filter_columns", None) != filter_columns:
            self._filter_columns = filter_columns
            self._reflow_grid(self.log_filters_layout, self.log_filter_widgets, filter_columns)

        detail_direction = (
            QBoxLayout.Direction.LeftToRight
            if width >= 1080 else QBoxLayout.Direction.TopToBottom
        )
        if self.detail_layout.direction() != detail_direction:
            self.detail_layout.setDirection(detail_direction)

        combat_direction = (
            QBoxLayout.Direction.LeftToRight
            if width >= 1080 else QBoxLayout.Direction.TopToBottom
        )
        if self.combat_matchup_layout.direction() != combat_direction:
            self.combat_matchup_layout.setDirection(combat_direction)

        # Resize fixed-size cells before Qt recomputes parent minimum widths.
        # This prevents large portraits from temporarily forcing horizontal overflow
        # when a window is dragged from a wide monitor onto a smaller one.
        grid_width = max(1, width - 24)
        card_width = max(1, (grid_width - (player_columns - 1) * 8) // player_columns)
        # Fit each board to its actual card width instead of forcing overflow.
        # Overview cards are a compact dashboard, not a second enlarged board.
        # Keep four board rows short enough that all eight seats remain visible.
        overview_size = max(16, min(38, (card_width - 16 - 12) // 7))
        for card in self.cards:
            self._set_cell_squares(card.cells, overview_size)

        if width < 1080:
            detail_grid_width = width - 70
            combat_grid_width = width - 50
        else:
            detail_grid_width = int(width * 0.63) - 40
            combat_grid_width = width // 2 - 45
        detail_size = max(12, min(144, (detail_grid_width - 18) // 7))
        combat_size = max(12, min(128, (combat_grid_width - 18) // 7))
        self._set_cell_squares(self.detail_cells, detail_size)
        for cells in self.combat_board_cells:
            self._set_cell_squares(cells, combat_size)

        compact = width < 820
        self.viewer_subtitle.setVisible(not compact)
        self.viewer_title.setStyleSheet(
            "font-size:16pt;font-weight:800;color:#60a5fa;"
            if compact else "font-size:20pt;font-weight:800;color:#60a5fa;"
        )
        QTimer.singleShot(0, self._sync_all_board_cells)

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
            if self.session._session_dir is not None:
                self._log(f"Logs individuais por jogador: {self.session._session_dir}")
                for player_number in range(1, 9):
                    self._log(f"  • player_{player_number}_log.tft")
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
            self.status_label.setText("Partida encerrada. Logs JSON por jogador salvos; inferência não alterou os pesos.")
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
        self._show_player_dialog(player_id)

    def _show_player_dialog(self, player_id: int):
        """Show the selected seat's existing snapshot, inventory, diagnostics and log."""
        state_players = self.session.public_state.get("players", [])
        audit_players = self.session.audit_snapshot.get("players", [])
        player = next((p for p in state_players if int(p.get("player_id", -1)) == player_id), {})
        audit = next((p for p in audit_players if int(p.get("player_id", -1)) == player_id), {})
        previous_dialog = getattr(self, "_player_dialog", None)
        if previous_dialog is not None:
            previous_dialog.close()
        dialog = QDialog(self)
        self._player_dialog = dialog
        dialog.setWindowTitle(f"Jogador {player_id + 1} · detalhes e log")
        dialog.setModal(True)
        dialog.setMinimumSize(560, 480)
        screen = self.screen().availableGeometry() if self.screen() else self.geometry()
        dialog.resize(min(980, max(560, int(screen.width() * 0.72))),
                      min(820, max(480, int(screen.height() * 0.82))))
        outer = QVBoxLayout(dialog)
        header = QLabel(f"JOGADOR {player_id + 1} · ROUND {self.session.public_state.get('round', 0)}")
        header.setStyleSheet("font-size:16pt;font-weight:800;color:#60a5fa;")
        outer.addWidget(header)
        strategy = audit.get("strategy_info") or {}
        summary = QLabel(
            f"HP: {_value(player, 'hp', default='—')}   ·   Ouro: {_value(player, 'gold', default='—')}   ·   "
            f"Nível: {_value(player, 'level', default='—')}   ·   XP: {_value(player, 'xp', default='—')}\n"
            f"Colocação: {_value(player, 'placement', default='—')}   ·   "
            f"Status: {'ELIMINADO' if player.get('eliminated') or not player.get('alive', True) else 'VIVO'}\n"
            f"Strategy: {strategy.get('strategy_name', 'ECON')}\n"
            f"{_composition_status_text(strategy)}"
        )
        summary.setWordWrap(True)
        outer.addWidget(summary)
        details = QTabWidget()
        roster_view = QPlainTextEdit()
        roster_view.setReadOnly(True)
        roster_lines = ["TABULEIRO:"]
        roster_lines.extend(f"  {index:02d}: {unit_label(unit)}" for index, unit in enumerate(audit.get("board", [])) if unit and unit.get("occupied"))
        roster_lines.append("\nBANCO:")
        roster_lines.extend(f"  {index:02d}: {unit_label(unit)}" for index, unit in enumerate(audit.get("bench", [])) if unit and unit.get("occupied"))
        roster_lines.append("\nLOJA:")
        roster_lines.extend(f"  {index:02d}: {unit_label(unit)}" for index, unit in enumerate(audit.get("shop", [])) if unit and unit.get("occupied"))
        roster_view.setPlainText("\n".join(roster_lines))
        details.addTab(roster_view, "Tabuleiro / banco / loja")
        diagnostic_view = QPlainTextEdit()
        diagnostic_view.setReadOnly(True)
        diag = self.session.last_policy[player_id] if player_id < len(self.session.last_policy) else {}
        diagnostic_view.setPlainText(json.dumps(diag, ensure_ascii=False, indent=2) if diag else "Sem diagnóstico de decisão neste passo.")
        details.addTab(diagnostic_view, "Diagnóstico da política")
        player_log_view = QPlainTextEdit()
        player_log_view.setReadOnly(True)
        log_path = (self.session._session_dir / f"player_{player_id + 1}_log.json") if self.session._session_dir else None
        log_text = "Ainda não há arquivo de log individual para esta sessão. Ative 'Salvar logs JSON por jogador' antes de iniciar para registrar o histórico."
        if log_path and log_path.exists():
            try:
                log_document = json.loads(log_path.read_text(encoding="utf-8"))
                entries = log_document.get("entries", [])
                lines = []
                for entry in entries[-250:]:
                    timestamp = entry.get("timestamp_iso") or entry.get("timestamp") or ""
                    event_type = entry.get("event_type") or entry.get("tag") or "evento"
                    message = entry.get("text") or ""
                    lines.append(f"[{timestamp}] {event_type}\n{message}")
                    payload = entry.get("payload")
                    if payload:
                        lines.append(json.dumps(payload, ensure_ascii=False, indent=2))
                log_text = "\n\n".join(lines) if lines else "O log individual existe, mas ainda não contém eventos."
            except (OSError, ValueError, TypeError) as exc:
                log_text = f"Não foi possível ler o log individual: {exc}"
        player_log_view.setPlainText(log_text)
        details.addTab(player_log_view, "Log do jogador")
        outer.addWidget(details, 1)
        close_button = QPushButton("Fechar")
        close_button.clicked.connect(dialog.accept)
        outer.addWidget(close_button, 0, Qt.AlignmentFlag.AlignRight)
        dialog.finished.connect(lambda _result, current=dialog: self._on_player_dialog_finished(current))
        dialog.show()

    def _show_composition_dialog(self, player_id: int):
        """Show the planner's target lineup without changing policy or engine state."""
        audit_players = self.session.audit_snapshot.get("players", [])
        audit = next((p for p in audit_players if int(p.get("player_id", -1)) == player_id), {})
        strategy = audit.get("strategy_info") or {}
        planned_names = strategy.get("planned_units") or []
        if not planned_names:
            QMessageBox.information(
                self, "Composição indisponível",
                "A engine ainda não forneceu uma composição planejada para este jogador."
            )
            return

        catalog = {}
        try:
            raw_catalog = json.loads((ROOT / "units_gerado.json").read_text(encoding="utf-8"))
            for unit in raw_catalog if isinstance(raw_catalog, list) else []:
                if not isinstance(unit, dict):
                    continue
                for alias in (unit.get("apiName"), unit.get("characterName"), unit.get("name")):
                    if alias:
                        catalog[str(alias).casefold()] = unit
        except (OSError, json.JSONDecodeError):
            catalog = {}

        planned_ids = strategy.get("planned_unit_ids") or []
        carry_id = strategy.get("planned_main_carry_id", -1)
        planned = []
        for index, raw_name in enumerate(planned_names):
            name = str(raw_name)
            record = catalog.get(name.casefold(), {})
            profile = record.get("combat_profile") or {}
            planned_id = planned_ids[index] if index < len(planned_ids) else None
            planned.append({
                "occupied": True,
                "champion_id": name,
                "apiName": name,
                "internal_id": planned_id,
                "star": 1,
                "cost": int(record.get("cost", 0) or 0),
                "name": record.get("name") or name,
                "traits": record.get("traits") or [],
                "role_name": profile.get("role_name") or record.get("role_name") or "função não informada",
                "combat_profile": profile,
            })

        carry = next((unit for unit in planned if unit.get("internal_id") == carry_id), None)
        previous_dialog = getattr(self, "_composition_dialog", None)
        if previous_dialog is not None:
            previous_dialog.close()
        dialog = QDialog(self)
        self._composition_dialog = dialog
        dialog.setWindowTitle(f"Composição planejada · Jogador {player_id + 1}")
        dialog.setModal(True)
        screen = self.screen().availableGeometry() if self.screen() else self.geometry()
        dialog.resize(min(1000, max(650, int(screen.width() * 0.78))),
                      min(820, max(560, int(screen.height() * 0.84))))
        outer = QVBoxLayout(dialog)

        direction = strategy.get("composition_direction") or "Direção ainda não definida"
        heading = QLabel(f"Direção: {direction}   ·   Unidades planejadas: {len(planned)}")
        heading.setStyleSheet("font-size:15pt;font-weight:800;color:#93c5fd;")
        outer.addWidget(heading)
        score = float(strategy.get("planned_composition_score", 0.0) or 0.0)
        score_label = QLabel(
            f"Carry principal: {carry['name'] if carry else 'não identificado'}"
            f"   ·   Pontuação interna do plano: {score:.2f}"
        )
        score_label.setObjectName("muted")
        outer.addWidget(score_label)

        tabs = QTabWidget()
        lineup_tab = QWidget()
        lineup_layout = QVBoxLayout(lineup_tab)
        lineup_scroll = QScrollArea()
        lineup_scroll.setWidgetResizable(True)
        lineup_content = QWidget()
        lineup_grid = QGridLayout(lineup_content)
        lineup_grid.setSpacing(10)
        for index, unit in enumerate(planned):
            tile = QFrame()
            tile.setObjectName("playerCard")
            tile_layout = QVBoxLayout(tile)
            portrait = ChampionCell(72, 72)
            portrait.set_unit(unit, self.icon_loader)
            tile_layout.addWidget(portrait, 0, Qt.AlignmentFlag.AlignHCenter)
            name_label = QLabel(unit["name"])
            name_label.setWordWrap(True)
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            name_label.setStyleSheet("font-weight:700;")
            tile_layout.addWidget(name_label)
            role_label = QLabel(unit["role_name"])
            role_label.setObjectName("muted")
            role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            tile_layout.addWidget(role_label)
            traits_label = QLabel(" · ".join(unit["traits"]) or "Sem traits no catálogo")
            traits_label.setWordWrap(True)
            traits_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            tile_layout.addWidget(traits_label)
            if unit is carry:
                carry_label = QLabel("CARRY PRINCIPAL")
                carry_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                carry_label.setStyleSheet("font-weight:800;color:#fbbf24;")
                tile_layout.addWidget(carry_label)
            lineup_grid.addWidget(tile, index // 4, index % 4)
        lineup_scroll.setWidget(lineup_content)
        lineup_layout.addWidget(lineup_scroll)
        tabs.addTab(lineup_tab, "Unidades")

        traits_tab = QWidget()
        traits_layout = QVBoxLayout(traits_tab)
        trait_rows = summarize_planned_traits(planned, strategy.get("planned_traits") or [])
        if trait_rows:
            for trait_name, count, is_core in trait_rows:
                marker = "  ·  PRIORIDADE DO PLANNER" if is_core else ""
                trait_label = QLabel(f"{trait_name}  ×{count}{marker}")
                trait_label.setWordWrap(True)
                if is_core:
                    trait_label.setStyleSheet("font-weight:700;color:#93c5fd;")
                traits_layout.addWidget(trait_label)
        else:
            traits_layout.addWidget(QLabel("O catálogo não forneceu traits para as unidades planejadas."))
        traits_note = QLabel(
            "As contagens vêm das unidades do plano. Os marcos exatos de ativação não são expostos "
            "no diagnóstico atual; traits destacadas são as priorizadas pelo planner."
        )
        traits_note.setWordWrap(True)
        traits_note.setObjectName("muted")
        traits_layout.addWidget(traits_note)
        traits_layout.addStretch()
        tabs.addTab(traits_tab, "Sinergias")

        position_tab = QWidget()
        position_layout = QVBoxLayout(position_tab)
        position_note = QLabel(
            "Prévia inicial sugerida a partir dos perfis de combate das unidades. "
            "A engine ainda não exporta coordenadas de formação planejada; esta visualização "
            "é uma sugestão explicativa, não uma ordem fixa nem uma alteração nas ações da IA."
        )
        position_note.setWordWrap(True)
        position_note.setObjectName("muted")
        position_layout.addWidget(position_note)
        board_frame = QGroupBox("Formação sugerida · tabuleiro 7×4")
        board_layout = QGridLayout(board_frame)
        board_layout.setSpacing(4)
        for column in range(7):
            board_layout.setColumnStretch(column, 1)
        suggested = suggest_initial_positions(planned)
        for index in range(28):
            cell = ChampionCell(62, 62)
            unit = suggested.get(index)
            cell.set_unit(unit, self.icon_loader)
            cell.setToolTip(
                f"Linha {index // 7 + 1}, coluna {index % 7 + 1}: "
                f"{unit['name'] if unit else 'vazio'}"
            )
            board_layout.addWidget(cell, index // 7, index % 7)
        position_layout.addWidget(board_frame)
        position_layout.addStretch()
        tabs.addTab(position_tab, "Posicionamento inicial")

        outer.addWidget(tabs, 1)
        footer = QHBoxLayout()
        footer.addStretch()
        close_button = QPushButton("Fechar")
        close_button.clicked.connect(dialog.accept)
        footer.addWidget(close_button)
        outer.addLayout(footer)
        dialog.finished.connect(
            lambda _result, current=dialog: self._on_composition_dialog_finished(current)
        )
        dialog.show()

    def _on_composition_dialog_finished(self, dialog):
        if getattr(self, "_composition_dialog", None) is dialog:
            self._composition_dialog = None
        dialog.deleteLater()

    def _on_player_dialog_finished(self, dialog):
        if getattr(self, "_player_dialog", None) is dialog:
            self._player_dialog = None
        dialog.deleteLater()

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
        strategy = audit.get("strategy_info") or {}
        active_traits = strategy.get("active_traits") or {}
        traits_text = ", ".join(f"{name}({count})" for name, count in sorted(active_traits.items())) or "—"
        core_traits_text = ", ".join(strategy.get("core_traits") or []) or "—"
        self.player_summary.setText(
            f"JOGADOR {i + 1}\nHP: {_value(player, 'hp', default='—')}\n"
            f"Ouro: {_value(player, 'gold', default='—')}\nNível: {_value(player, 'level', default='—')} · "
            f"XP: {_value(player, 'xp', default='—')}\nColocação: {_value(player, 'placement', default='—')}\n"
            f"Strategy: {strategy.get('strategy_name', 'ECON')} · "
            f"Confiança: {float(strategy.get('confidence', 0.0) or 0.0):.2f}\n"
            f"{_composition_status_text(strategy)}\n"
            f"Core traits: {core_traits_text}\nTraits ativos: {traits_text}"
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
                f"JOGADOR {self.selected_player + 1} · sem combate ativo/pareamento informado"
            )
            self.combat_team_labels[0].setText(f"JOGADOR {self.selected_player + 1} · formação atual")
            self.combat_team_labels[1].setText("LADO ADVERSÁRIO · sem combate")
            self._render_combat_board(0, selected_audit.get("board", []), mirror=False)
            self._clear_combat_board(1)
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
        for team_index in range(len(self.combat_board_cells)):
            self._clear_combat_board(team_index)

    def _clear_combat_board(self, team_index):
        for cell in self.combat_board_cells[team_index]:
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
        # Human-readable live audit summary. New sessions persist independent JSON logs per player;
        # live_events is the in-memory stream used by these filters.
        if not hasattr(self, "events_log"):
            return
        player_filter = self.log_player_filter.currentIndex() - 1 if hasattr(self, "log_player_filter") else -1
        type_filter = self.log_type_filter.currentText() if hasattr(self, "log_type_filter") else "Todos os eventos"
        round_filter = self.log_round_filter.currentText() if hasattr(self, "log_round_filter") else "Todos os rounds"
        severity_filter = self.log_severity_filter.currentText() if hasattr(self, "log_severity_filter") else "Todas as gravidades"
        # Live audit remains in memory; each seat's human-readable history is
        # independently persisted as player_N_log.json by ViewerSession.
        events = (self.session.replay_events[:] if self.session.replay_mode
                  else self.session.live_events[:])
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
                if "player_id" in event:
                    if int(event.get("player_id", -1)) != player_filter:
                        continue
                else:
                    players = event.get("payload", {}).get("players", [])
                    if not any(int(p.get("player_id", -1)) == player_filter for p in players):
                        continue
            filtered.append(event)
        self.events_log.setPlainText("\n".join(
            f"#{e.get('sequence_id')} · {e.get('event_type')} · R{e.get('round')} S{e.get('stage')}"
            for e in filtered[-500:]
        ) or "Nenhum evento corresponde aos filtros.")

    def _open_replay(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Abrir log de jogador / replay legado",
            str(ROOT / "viewer" / "sessions"),
            "Logs JSON por jogador (*.json);;Replay JSONL legado (*.jsonl);;Todos os arquivos (*)",
        )
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
        readable_text = event.get("text")
        payload = event.get("payload", {})
        if readable_text:
            detail = str(readable_text).rstrip()
            if payload:
                detail += "\n\nDETALHES ESTRUTURADOS\n" + json.dumps(payload, ensure_ascii=False, indent=2)
            self.events_log.setPlainText(detail)
        else:
            self.events_log.setPlainText(json.dumps(event, ensure_ascii=False, indent=2))
        player_number = event.get("player_number")
        player_prefix = f"JOGADOR {player_number} · " if player_number else ""
        self.round_label.setText(
            f"REPLAY · {player_prefix}evento {event.get('sequence_id')} · {event.get('event_type')}"
        )

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
