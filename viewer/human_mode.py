"""Interactive human-play Viewer, isolated from PPO training and native engine code.

Run with: python -m viewer.human_main
The human controls one seat through the same native action masks used by the agents.
Each submitted human action is batched with one inference action for each other living seat.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtWidgets import (
    QApplication, QComboBox, QFileDialog, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QScrollArea,
    QSpinBox, QPlainTextEdit, QVBoxLayout, QWidget,
)

from viewer.session import ViewerSession, ACTION_NAMES, ROOT
from viewer.main import APP_STYLE, ChampionIconLoader, ChampionCell, PlayerCard


def _by_id(rows, player_id):
    return next((row for row in (rows or []) if int(row.get("player_id", -1)) == player_id), {})


def _occupied(unit):
    return bool(unit and unit.get("occupied", False))


def _name(unit):
    if not _occupied(unit):
        return "Vazio"
    return str(unit.get("name") or unit.get("champion_id") or unit.get("apiName") or "Unidade")


class InteractiveCell(ChampionCell):
    clicked = Signal(int, str)

    def __init__(self, index: int, area: str, parent=None):
        super().__init__(48, 48, parent)
        self.index = int(index)
        self.area = str(area)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.index, self.area)
        super().mousePressEvent(event)


class HumanDemonstrationWindow(QMainWindow):
    """Human-controlled seat versus seven frozen-policy agents."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TFT Viewer — Jogar contra 7 agentes")
        self.resize(1480, 980)
        self.session = ViewerSession()
        self.human_player = 0
        self.selected_source = None
        self.selected_item = None
        self.first_component = None
        self._second_component = None
        self._action_queue = []
        self._round_key = None
        self._round_started_at = None
        self._next_step_at = None
        self._deadline_action_flushed = False
        self._step_interval_seconds = 0.7
        self.icon_loader = ChampionIconLoader(ROOT / "data" / "units_gerado.json", self)
        self.icon_loader.loaded.connect(self._render)
        self._build_ui()
        self.preparation_timer = QTimer(self)
        self.preparation_timer.setInterval(100)
        self.preparation_timer.timeout.connect(self._on_preparation_tick)

    def _build_ui(self):
        page = QWidget()
        outer = QVBoxLayout(page)
        top = QHBoxLayout()
        self.checkpoint = QLineEdit(str(ROOT / "checkpoints" / "latest.pt"))
        browse = QPushButton("Checkpoint…")
        browse.clicked.connect(self._browse_checkpoint)
        self.seed = QSpinBox()
        self.seed.setRange(0, 2_147_483_647)
        self.seed.setValue(20261106)
        self.seat = QComboBox()
        self.seat.addItems([f"JOGADOR {i + 1}" for i in range(8)])
        self.seat.currentIndexChanged.connect(self._seat_changed)
        self.load_button = QPushButton("Nova partida")
        self.load_button.clicked.connect(self._load_match)
        top.addWidget(QLabel("Checkpoint"))
        top.addWidget(self.checkpoint, 1)
        top.addWidget(browse)
        top.addWidget(QLabel("Seed"))
        top.addWidget(self.seed)
        top.addWidget(QLabel("Seu assento"))
        top.addWidget(self.seat)
        top.addWidget(self.load_button)
        outer.addLayout(top)

        self.status = QLabel("Carregue o checkpoint. Você controla um jogador; os outros sete são controlados pela policy.")
        self.status.setWordWrap(True)
        outer.addWidget(self.status)
        self.phase_clock = QLabel("Preparação: aguardando partida")
        self.phase_clock.setStyleSheet("font-size:12pt;font-weight:700;color:#fbbf24;")
        outer.addWidget(self.phase_clock)

        self.cards = []
        cards_box = QGroupBox("Lobby — visão geral dos 8 jogadores")
        cards_layout = QGridLayout(cards_box)
        for player_id in range(8):
            card = PlayerCard(player_id)
            card.selected.connect(self._select_card)
            card.composition_requested.connect(self._show_composition)
            self.cards.append(card)
            cards_layout.addWidget(card, player_id // 4, player_id % 4)
        outer.addWidget(cards_box)

        self.player_header = QLabel("Seu tabuleiro aparecerá aqui.")
        self.player_header.setStyleSheet("font-size:14pt;font-weight:800;color:#60a5fa;")
        outer.addWidget(self.player_header)

        controls = QHBoxLayout()
        self.xp_button = QPushButton("Comprar XP")
        self.xp_button.clicked.connect(lambda: self._perform([2, 0, 0, 0, 0, 0], "BUY_XP"))
        self.roll_button = QPushButton("Atualizar loja")
        self.roll_button.clicked.connect(lambda: self._perform([1, 0, 0, 0, 0, 0], "REROLL"))
        self.sell_button = QPushButton("Vender unidade selecionada")
        self.sell_button.clicked.connect(self._sell_selected)
        for widget in (self.xp_button, self.roll_button, self.sell_button):
            controls.addWidget(widget)
        outer.addLayout(controls)

        shop_box = QGroupBox("LOJA — clique em um campeão para comprar")
        self.shop_box = shop_box
        self.shop_layout = QHBoxLayout(shop_box)
        self.shop_cells = []
        for slot in range(5):
            cell = InteractiveCell(slot, "shop")
            cell.clicked.connect(self._cell_clicked)
            self.shop_cells.append(cell)
            self.shop_layout.addWidget(cell)
        outer.addWidget(shop_box)

        middle = QHBoxLayout()
        board_box = QGroupBox("TABULEIRO 7 × 4 — selecione uma unidade e depois o destino")
        self.board_layout = QGridLayout(board_box)
        self.board_cells = []
        for index in range(28):
            cell = InteractiveCell(index, "board")
            cell.clicked.connect(self._cell_clicked)
            self.board_layout.addWidget(cell, index // 7, index % 7)
            self.board_cells.append(cell)
        middle.addWidget(board_box, 4)

        side = QVBoxLayout()
        bench_box = QGroupBox("BANCO — clique para selecionar / mover")
        self.bench_layout = QGridLayout(bench_box)
        self.bench_cells = []
        for slot in range(9):
            cell = InteractiveCell(slot, "bench")
            cell.clicked.connect(self._cell_clicked)
            self.bench_layout.addWidget(cell, slot // 5, slot % 5)
            self.bench_cells.append(cell)
        side.addWidget(bench_box)

        items_box = QGroupBox("ITENS — selecione item e clique no campeão-alvo")
        items_layout = QVBoxLayout(items_box)
        self.items_label = QLabel("Inventário ainda não carregado.")
        self.items_label.setWordWrap(True)
        items_layout.addWidget(self.items_label)
        self.item_buttons = QHBoxLayout()
        self.component_buttons = QHBoxLayout()
        items_layout.addLayout(self.item_buttons)
        items_layout.addLayout(self.component_buttons)
        side.addWidget(items_box)
        middle.addLayout(side, 3)
        outer.addLayout(middle, 1)

        self.note = QLineEdit()
        self.note.setPlaceholderText("Anotação opcional: por que você tomou essa decisão?")
        outer.addWidget(self.note)
        self.selection_label = QLabel("Aguardando partida.")
        self.selection_label.setWordWrap(True)
        outer.addWidget(self.selection_label)
        self.events = QPlainTextEdit()
        self.events.setReadOnly(True)
        self.events.setMaximumHeight(105)
        outer.addWidget(self.events)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(page)
        self.setCentralWidget(scroll)
        self.setStyleSheet(APP_STYLE)

    def _browse_checkpoint(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Selecionar checkpoint", str(ROOT),
            "Checkpoints (*.pt *.pth *.ckpt);;Todos os arquivos (*)",
        )
        if path:
            self.checkpoint.setText(path)

    def _seat_changed(self, seat):
        if self.session.started:
            self.seat.setCurrentIndex(self.human_player)
            return
        self.human_player = int(seat)

    def _select_card(self, player_id):
        for card in self.cards:
            card.set_selected(card.player_id == player_id)
        if player_id != self.human_player:
            self.status.setText(
                f"Jogador {player_id + 1} é controlado pela IA. Seu assento humano continua sendo o jogador {self.human_player + 1}."
            )

    def _load_match(self):
        self.preparation_timer.stop()
        try:
            snapshot = self.session.load_checkpoint(
                self.checkpoint.text().strip(), self.seed.value(), True,
                ROOT / "viewer" / "human_sessions", record=True,
            )
            # Same six-second preparation window as the normal Viewer.
            # Human actions are queued; the 700 ms cadence keeps agent decisions
            # synchronized with the regular Viewer instead of advancing a round per click.
            self.session.config.use_wall_clock_preparation = True
            self._action_queue.clear()
            self._round_key = (
                int(self.session.public_state.get("round", 1) or 1),
                int(self.session.public_state.get("stage", 1) or 1),
            )
            self._round_started_at = time.monotonic()
            self._next_step_at = self._round_started_at + self._step_interval_seconds
            self._deadline_action_flushed = False
            self.preparation_timer.start()
            self.seat.setEnabled(False)
            self.load_button.setText("Reiniciar partida")
            self.events.appendPlainText(
                f"Sessão {self.session.match_id} | checkpoint SHA-256 {self.session.checkpoint_sha256}"
            )
            self.events.appendPlainText(f"Logs: {self.session._session_dir}")
            self._render(snapshot)
            self.status.setText(
                "Partida ativa: suas ações são enviadas à engine junto com uma ação de cada um dos outros 7 agentes vivos. "
                "Os pesos do checkpoint permanecem congelados."
            )
        except Exception as exc:
            QMessageBox.critical(self, "Falha ao iniciar partida", str(exc))

    def _human_audit(self):
        return _by_id(self.session.audit_snapshot.get("players", []), self.human_player)

    def _human_public(self):
        return _by_id(self.session.public_state.get("players", []), self.human_player)

    @staticmethod
    def _mask_ok(mask, key, *indices):
        value = mask.get(key)
        try:
            for index in indices:
                if int(index) < 0 or int(index) >= len(value):
                    return False
                value = value[int(index)]
            return bool(value)
        except (TypeError, IndexError, KeyError):
            return False

    def _legal(self, action):
        mask = self.session.masks[self.human_player]
        kind = int(action[0])
        types = mask.get("type_mask")
        if types is not None and (kind >= len(types) or not bool(types[kind])):
            return False
        if kind == 0:
            return self._mask_ok(mask, "shop_mask", action[1])
        if kind == 3:
            return self._mask_ok(mask, "bench_to_board_target_masks", action[2], action[3])
        if kind == 4:
            return self._mask_ok(mask, "board_move_target_masks", action[4], action[5])
        if kind == 5:
            return self._mask_ok(mask, "bench_source_mask", action[2])
        if kind == 7:
            return self._mask_ok(mask, "item_inventory_mask", action[1]) and self._mask_ok(mask, "item_target_mask", action[2])
        if kind == 8:
            return (
                self._mask_ok(mask, "item_component_first_mask", action[1])
                and self._mask_ok(mask, "item_component_pair_masks", action[1], action[2])
                and self._mask_ok(mask, "item_target_mask", action[3])
            )
        return True

    def _perform(self, human_action, action_label=None):
        """Queue a click; the shared preparation clock controls when it reaches the engine."""
        s = self.session
        if not s.started or s.finished or s.lobby is None:
            return
        if not _by_id(s.public_state.get("players", []), self.human_player).get("alive", True):
            QMessageBox.information(self, "Jogador eliminado", "Seu jogador já foi eliminado.")
            return
        if self._round_started_at is not None:
            elapsed = time.monotonic() - self._round_started_at
            if elapsed >= float(s.config.preparation_seconds) and self._deadline_action_flushed:
                self.selection_label.setText("O tempo de preparação terminou; a ação ficará para a próxima rodada.")
                return
        self._action_queue.append((list(map(int, human_action)), str(action_label or ACTION_NAMES.get(int(human_action[0]), "UNKNOWN")), self.note.text().strip()))
        self.selection_label.setText(
            f"Ação enfileirada ({len(self._action_queue)}). Será executada durante a preparação, sem encerrar a rodada."
        )

    def _reset_round_clock(self):
        s = self.session
        self._round_key = (
            int(s.public_state.get("round", 1) or 1),
            int(s.public_state.get("stage", 1) or 1),
        )
        self._round_started_at = time.monotonic()
        self._next_step_at = self._round_started_at + self._step_interval_seconds
        self._deadline_action_flushed = False
        self._action_queue.clear()

    def _on_preparation_tick(self):
        s = self.session
        if not s.started or s.finished or s.lobby is None or self._round_started_at is None:
            self.preparation_timer.stop()
            return

        current_key = (
            int(s.public_state.get("round", 1) or 1),
            int(s.public_state.get("stage", 1) or 1),
        )
        if current_key != self._round_key:
            self._reset_round_clock()

        now = time.monotonic()
        elapsed = now - self._round_started_at
        duration = float(s.config.preparation_seconds)
        remaining = max(0.0, duration - elapsed)
        self.phase_clock.setText(
            f"RODADA {current_key[0]} · Preparação: {remaining:0.1f}s"
        )

        timer_expired = elapsed >= duration
        queued = None
        if timer_expired:
            # Honor one click made just before the deadline; then resolve the round
            # on the following timer pulse. Do not let a backlog extend preparation.
            if self._action_queue and not self._deadline_action_flushed:
                queued = self._action_queue.pop(0)
                self._deadline_action_flushed = True
                timer_expired = False
            else:
                self._action_queue.clear()
        elif now < (self._next_step_at or now):
            return

        if not timer_expired and queued is None and self._action_queue:
            queued = self._action_queue.pop(0)
        if not timer_expired and queued is None and now < (self._next_step_at or now):
            return

        self._next_step_at = now + self._step_interval_seconds
        self._execute_step(queued, timer_expired=timer_expired)

    def _execute_step(self, queued_action=None, *, timer_expired=False):
        s = self.session
        if not s.started or s.finished or s.lobby is None:
            return

        before = s._snapshot_for_event()
        masks_before = s.masks
        human_mask = masks_before[self.human_player]
        human_action = queued_action[0] if queued_action else [6, 0, 0, 0, 0, 0]
        human_label = queued_action[1] if queued_action else "PASS"
        human_note = queued_action[2] if queued_action else ""
        human_is_action = queued_action is not None

        if human_is_action and not self._legal(human_action):
            QMessageBox.information(
                self, "Ação indisponível",
                "A ação deixou de ser válida antes de chegar à engine; ela foi descartada.",
            )
            human_action = [6, 0, 0, 0, 0, 0]
            human_label = "PASS"
            human_note = ""
            human_is_action = False

        actions, diagnostics = [], []
        for seat in range(8):
            player = _by_id(s.public_state.get("players", []), seat)
            if not player.get("alive", True):
                action = [6, 0, 0, 0, 0, 0]
                diagnostic = {"action_name": "PASS", "action": action, "status": "eliminated_seat"}
            elif timer_expired:
                # Mirror the normal Viewer timeout: idle seats PASS. A mandatory
                # pending anvil is the only exception and is resolved by frozen policy.
                seat_mask = masks_before[seat]
                type_mask = seat_mask.get("type_mask")
                pending_choice = (
                    type_mask is not None
                    and len(type_mask) > 7
                    and bool(type_mask[7])
                    and sum(bool(value) for value in type_mask) == 1
                )
                if pending_choice:
                    action, diagnostic = s._action_for_player(seat)
                    diagnostic = {**diagnostic, "source": "automatic_pending_choice"}
                else:
                    action = [6, 0, 0, 0, 0, 0]
                    diagnostic = {"action_name": "PASS", "action": action, "status": "preparation_timeout"}
            elif seat == self.human_player:
                action = human_action
                diagnostic = {
                    "action_name": human_label,
                    "action": action,
                    "source": "human" if human_is_action else "human_idle",
                    "human_note": human_note,
                }
            else:
                action, diagnostic = s._action_for_player(seat)
                diagnostic = {**diagnostic, "source": "frozen_policy"}
            actions.append(action)
            diagnostics.append(diagnostic)

        if human_is_action:
            s._emit("human_decision", {
                "player_id": self.human_player,
                "action": human_action,
                "action_name": human_label,
                "human_note": human_note,
                "state_before": before,
                "action_masks_before": human_mask,
                "available_actions_mask": human_mask.get("type_mask"),
            })

        try:
            obs, rewards, done, info = s.lobby.step(
                actions,
                timer_enabled=True,
                timer_expired=bool(timer_expired),
            )
        except Exception as exc:
            QMessageBox.critical(self, "Erro da engine", str(exc))
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
            "human_player_id": self.human_player,
            "human_action_was_submitted": human_is_action,
            "preparation_timer_expired": bool(timer_expired),
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

        self.events.appendPlainText(
            f"Passo {s.step_count} · {'ação humana: ' + human_label if human_is_action else 'agentes / espera'} · "
            f"eventos: {', '.join(map(str, info.get('events', [])))}"
        )
        if human_is_action:
            self.note.clear()
        self.selected_source = None
        self.selected_item = None
        self.first_component = None
        self._second_component = None

        if s.finished:
            self.preparation_timer.stop()
            self.phase_clock.setText("PARTIDA FINALIZADA")
        elif any(str(event).strip() == "ROUND_RESOLVED" for event in info.get("events", [])):
            self._reset_round_clock()
        self._render(after)

    def _cell_clicked(self, index, area):
        if not self.session.started or self.session.finished:
            return
        audit = self._human_audit()
        if area == "shop":
            self._perform([0, index, 0, 0, 0, 0], "BUY")
            return
        if area in ("bench", "board"):
            if self.selected_item is not None:
                target = index if area == "board" else 28 + index
                self._perform([7, self.selected_item, target, 0, 0, 0], "EQUIP_FROM_INVENTORY")
                return
            if self.first_component is not None:
                target = index if area == "board" else 28 + index
                self._perform([8, self.first_component, self._second_component, target, 0, 0], "CRAFT_AND_EQUIP")
                return
            if self.selected_source is None:
                units = audit.get("bench" if area == "bench" else "board", [])
                if index >= len(units) or not _occupied(units[index]):
                    return
                self.selected_source = (area, index)
                self.selection_label.setText(f"Selecionado: {_name(units[index])} · {area} slot {index}. Agora clique no destino.")
                return
            source_area, source_index = self.selected_source
            if source_area == "bench" and area == "board":
                self._perform([3, 0, source_index, index, 0, 0], "MOVE_BENCH")
            elif source_area == "board" and area == "board":
                self._perform([4, 0, 0, 0, source_index, index], "MOVE_BOARD")
            elif source_area == "bench" and area == "bench":
                self.selection_label.setText("Mover entre slots do banco não é uma ação exposta pelo contrato nativo atual.")
            else:
                self.selection_label.setText("Para mover uma unidade do tabuleiro, escolha outra casa do tabuleiro.")
            return

    def _sell_selected(self):
        if not self.selected_source or self.selected_source[0] != "bench":
            QMessageBox.information(self, "Vender", "Selecione primeiro uma unidade no banco.")
            return
        self._perform([5, 0, self.selected_source[1], 0, 0, 0], "SELL")

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def _render_items(self, audit):
        self._clear_layout(self.item_buttons)
        self._clear_layout(self.component_buttons)
        inventory = list(audit.get("item_inventory", []) or [])
        components = list(audit.get("item_components", []) or [])
        self.items_label.setText(
            f"Itens completos: {', '.join(map(str, inventory)) or 'nenhum'}\n"
            f"Componentes: {', '.join(map(str, components)) or 'nenhum'}"
        )
        for index, item in enumerate(inventory):
            button = QPushButton(f"{index}: {item}")
            button.clicked.connect(lambda _=False, slot=index: self._select_item(slot))
            self.item_buttons.addWidget(button)
        for index, item in enumerate(components):
            button = QPushButton(f"{index}: {item}")
            button.clicked.connect(lambda _=False, slot=index: self._select_component(slot))
            self.component_buttons.addWidget(button)

    def _select_item(self, slot):
        mask = self.session.masks[self.human_player]
        if not self._mask_ok(mask, "item_inventory_mask", slot):
            QMessageBox.information(self, "Item indisponível", "Esse item não está liberado pela máscara nativa.")
            return
        self.selected_item = slot
        self.first_component = None
        self.selection_label.setText(f"Item {slot} selecionado. Clique em um campeão do banco ou tabuleiro para equipar.")

    def _select_component(self, slot):
        mask = self.session.masks[self.human_player]
        if self.first_component is None:
            if not self._mask_ok(mask, "item_component_first_mask", slot):
                QMessageBox.information(self, "Componente indisponível", "Esse componente não está liberado pela máscara nativa.")
                return
            self.first_component = slot
            self.selection_label.setText(f"Primeiro componente {slot} selecionado. Escolha o segundo componente.")
            return
        self._second_component = slot
        if not self._mask_ok(mask, "item_component_pair_masks", self.first_component, slot):
            QMessageBox.information(self, "Combinação indisponível", "A engine não permite essa combinação.")
            self._second_component = None
            return
        self.selected_item = None
        self.selection_label.setText("Receita selecionada. Clique no campeão-alvo para criar e equipar.")

    def _render(self, _snapshot=None):
        if not self.session.started:
            return
        s = self.session
        public_players = {int(p.get("player_id", i)): p for i, p in enumerate(s.public_state.get("players", []))}
        audit_players = {int(p.get("player_id", i)): p for i, p in enumerate(s.audit_snapshot.get("players", []))}
        for player_id, card in enumerate(self.cards):
            card.update_player(
                public_players.get(player_id, {}), audit_players.get(player_id, {}),
                s.last_actions[player_id] if player_id < len(s.last_actions) else None,
                self.icon_loader, s.finished, s.public_state.get("winner_id"),
            )
            card.set_selected(player_id == self.human_player)
        audit = audit_players.get(self.human_player, {})
        player = public_players.get(self.human_player, {})
        self.player_header.setText(
            f"JOGADOR {self.human_player + 1} · ROUND {s.public_state.get('round', '?')} · "
            f"HP {player.get('hp', '?')} · OURO {player.get('gold', '?')} · "
            f"NÍVEL {player.get('level', '?')} · XP {player.get('xp', '?')}"
        )
        for cells, units in (
            (self.shop_cells, audit.get("shop", [])),
            (self.bench_cells, audit.get("bench", [])),
            (self.board_cells, audit.get("board", [])),
        ):
            for index, cell in enumerate(cells):
                unit = units[index] if index < len(units) else None
                cell.set_unit(unit if _occupied(unit) else None, self.icon_loader)
        self._render_items(audit)
        alive = bool(player.get("alive", True))
        masks = s.masks[self.human_player] if s.masks else {}
        type_mask = masks.get("type_mask", [])
        self.xp_button.setEnabled(not s.finished and alive and len(type_mask) > 2 and bool(type_mask[2]))
        self.roll_button.setEnabled(not s.finished and alive and len(type_mask) > 1 and bool(type_mask[1]))
        self.sell_button.setEnabled(not s.finished and alive)
        shop_mask = masks.get("shop_mask", [])
        shop_units = audit.get("shop", []) or []
        shop_has_offers = any(_occupied(unit) for unit in shop_units)
        shop_buy_legal = any(
            _occupied(unit) and slot < len(shop_mask) and bool(shop_mask[slot])
            for slot, unit in enumerate(shop_units)
        )
        for slot, cell in enumerate(self.shop_cells):
            has_offer = slot < len(shop_units) and _occupied(shop_units[slot])
            legal_offer = slot < len(shop_mask) and bool(shop_mask[slot])
            cell.setEnabled(not s.finished and alive and has_offer and legal_offer)
        if hasattr(self, "shop_box"):
            if shop_buy_legal:
                self.shop_box.setTitle("LOJA — clique em um campeão para comprar")
            elif shop_has_offers:
                self.shop_box.setTitle("LOJA — ofertas visíveis, mas nenhuma compra está liberada pela máscara")
            elif int(s.public_state.get("round", 1) or 1) == 1:
                self.shop_box.setTitle("LOJA — sem ofertas no snapshot inicial 1-1")
            else:
                self.shop_box.setTitle("LOJA — sem ofertas disponíveis neste momento")
        if s.finished:
            self.status.setText(f"Partida finalizada · ranking: {s.public_state.get('ranking', [])}")
        else:
            self.status.setText(
                "Clique na loja para comprar; Comprar XP/Atualizar loja para economia; selecione uma unidade e depois o destino; "
                "selecione item/componente e depois o alvo. Cada ação sua executa também as decisões dos outros sete agentes."
            )
        # Carousel support is shown only when the native public snapshot actually exposes it.
        carousel = s.public_state.get("carousel") or s.public_state.get("carousel_state")
        if carousel:
            self.selection_label.setText(
                "A engine expôs estado de carrossel, mas ainda não há ação de escolha de carrossel no contrato de ações nativo."
            )
        else:
            self.selection_label.setText(
                "Movimentação: clique na unidade e depois no destino. Itens: selecione na bag e clique no campeão."
            )

    def _show_composition(self, player_id):
        QMessageBox.information(
            self, "Composição planejada",
            "Abra o Viewer normal para consultar o detalhe do planner. Nesta tela, os oito tabuleiros e estados são atualizados ao vivo.",
        )

    def closeEvent(self, event):
        self.preparation_timer.stop()
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
