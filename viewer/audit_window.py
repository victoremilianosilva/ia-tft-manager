"""Tela de auditoria completa de uma sessão TFT, integrada ao Viewer."""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QFileDialog, QLineEdit, QTabWidget, QPlainTextEdit,
    QTableWidget, QTableWidgetItem, QMessageBox, QSplitter, QScrollArea, QFrame,
)

ROOT = Path(__file__).resolve().parents[1]


def _fmt(value):
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.3f}"
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


class BarChart(QWidget):
    """Small dependency-free chart; keeps the audit UI usable without matplotlib."""
    def __init__(self, title="", values=None, parent=None):
        super().__init__(parent)
        self.title = title
        self.values = list(values or [])
        self.setMinimumHeight(220)
        self.setMinimumWidth(300)

    def set_data(self, title, values):
        self.title, self.values = title, list(values or [])
        self.update()

    def paintEvent(self, _event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QColor("#e5e7eb"))
        painter.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        painter.drawText(12, 22, self.title)
        if not self.values:
            painter.setPen(QColor("#94a3b8"))
            painter.drawText(12, 52, "Sem dados suficientes para este gráfico.")
            return
        values = [(str(label), float(value or 0)) for label, value in self.values[:16]]
        max_value = max([abs(v) for _, v in values] + [1.0])
        left, right = 155, max(180, self.width() - 24)
        top, row_h = 38, max(18, min(30, (self.height() - 48) // len(values)))
        plot_w = max(20, right - left)
        for i, (label, value) in enumerate(values):
            y = top + i * row_h
            painter.setPen(QColor("#cbd5e1"))
            painter.setFont(QFont("Segoe UI", 8))
            short = label if len(label) < 23 else label[:20] + "…"
            painter.drawText(10, y + 13, short)
            width = int(plot_w * abs(value) / max_value)
            painter.fillRect(left, y + 2, max(1, width), max(8, row_h - 6),
                             QColor("#38bdf8") if value >= 0 else QColor("#fb7185"))
            painter.setPen(QColor("#e5e7eb"))
            painter.drawText(min(right - 28, left + width + 5), y + 13, f"{value:.2f}"[:10])


class AuditWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("TFT — Auditoria completa de partida")
        self.resize(1180, 820)
        self.setMinimumSize(820, 560)
        self.session_dir: Path | None = None
        self.report: dict = {}
        self.report_md = ""
        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)

        header = QHBoxLayout()
        header.addWidget(QLabel("Pasta da partida"))
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("Selecione viewer/sessions/match-…")
        header.addWidget(self.path_edit, 1)
        browse = QPushButton("Selecionar pasta…")
        browse.clicked.connect(self.choose_folder)
        header.addWidget(browse)
        self.audit_button = QPushButton("Executar auditoria")
        self.audit_button.clicked.connect(self.run_audit)
        header.addWidget(self.audit_button)
        layout.addLayout(header)

        self.status = QLabel("Logs novos incluem estado antes/depois, máscaras legais, diagnóstico da política, recompensas por canal e UUIDs. Partidas antigas são auditadas conforme os campos registrados.")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs, 1)
        self._build_empty_tabs()

    def _build_empty_tabs(self):
        for title in ("Visão geral", "Economia", "Estratégia", "Composição", "Tabuleiro", "Itens", "Loops e movimentos", "Qualidade dos dados", "Achados"):
            page = QWidget()
            box = QVBoxLayout(page)
            label = QLabel("Execute a auditoria para carregar os dados desta aba.")
            label.setWordWrap(True)
            label.setObjectName("muted")
            box.addWidget(label)
            box.addStretch()
            self.tabs.addTab(page, title)

    def choose_folder(self):
        initial = self.path_edit.text().strip() or str(ROOT / "viewer" / "sessions")
        folder = QFileDialog.getExistingDirectory(self, "Selecionar pasta da partida", initial)
        if folder:
            self.path_edit.setText(folder)

    def run_audit(self):
        raw = self.path_edit.text().strip()
        folder = Path(raw).expanduser() if raw else None
        if folder is None or not folder.is_dir():
            QMessageBox.warning(self, "Pasta inválida", "Selecione uma pasta de partida existente.")
            return
        logs = list(folder.glob("player_*_log.json"))
        if not logs:
            logs = list(folder.glob("player_*_log.tft"))
        if not logs:
            logs = list(folder.rglob("player_*_log.json"))
        if not logs:
            logs = list(folder.rglob("player_*_log.tft"))
        if not logs:
            QMessageBox.warning(self, "Logs não encontrados", "A pasta não contém registros de partida compatíveis para auditoria.")
            return
        self.audit_button.setEnabled(False)
        self.status.setText(f"Analisando {len(logs)} arquivos em {folder}…")
        QApplication.processEvents()
        out_dir = folder / "audit"
        command = [
            sys.executable, str(ROOT / "scripts" / "audit_viewer_match.py"),
            str(folder), "--out-dir", str(out_dir),
        ]
        try:
            completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
            report_path = out_dir / "audit_report.json"
            md_path = out_dir / "audit_report.md"
            if not report_path.is_file():
                detail = (completed.stderr or completed.stdout or "O auditor não gerou o relatório.")[-6000:]
                raise RuntimeError(detail)
            self.report = json.loads(report_path.read_text(encoding="utf-8"))
            self.report_md = md_path.read_text(encoding="utf-8") if md_path.is_file() else completed.stdout
            self.session_dir = folder
            self._render_report()
            issues = self.report.get("issues", [])
            counts = Counter(x.get("severity", "UNKNOWN") for x in issues)
            self.status.setText(
                f"Concluído · {len(self.report.get('log_files', []))} arquivos · "
                f"{len(self.report.get('players_seen', []))}/8 jogadores · "
                f"{self.report.get('entries_read', 0)} entradas estruturadas · "
                f"{len(issues)} achados (CRITICAL {counts['CRITICAL']}, HIGH {counts['HIGH']}, "
                f"MEDIUM {counts['MEDIUM']}, LOW {counts['LOW']}). "
                f"Relatórios completos salvos em {out_dir}"
            )
            if completed.returncode not in (0, 1):
                self.status.setText(self.status.text() + f" · auditor retornou código {completed.returncode}")
        except Exception as exc:
            QMessageBox.critical(self, "Falha na auditoria", str(exc))
            self.status.setText("A auditoria falhou. Veja a mensagem de erro.")
        finally:
            self.audit_button.setEnabled(True)

    def _replace_tabs(self):
        while self.tabs.count():
            page = self.tabs.widget(0)
            self.tabs.removeTab(0)
            page.deleteLater()

    def _page(self, title):
        page = QWidget()
        layout = QVBoxLayout(page)
        self.tabs.addTab(page, title)
        return layout

    def _add_chart(self, layout, title, values):
        chart = BarChart(title, values)
        layout.addWidget(chart)

    def _add_text(self, layout, text):
        box = QPlainTextEdit()
        box.setReadOnly(True)
        box.setPlainText(text)
        layout.addWidget(box, 1)

    def _render_report(self):
        self._replace_tabs()
        report = self.report
        issues = report.get("issues", [])
        counts = Counter(x.get("severity", "UNKNOWN") for x in issues)

        layout = self._page("Visão geral")
        overview = [
            f"Origem: {report.get('source', '—')}",
            f"Arquivos: {len(set(report.get('log_files', [])))}",
            f"Jogadores: {', '.join(map(str, report.get('players_seen', []))) or 'nenhum'}",
            f"Entradas estruturadas: {report.get('entries_read', 0)}",
            f"Diagnósticos ausentes: {report.get('diagnostics_missing', 0)}",
            f"Decisões reconstruídas: {len(report.get('decision_timeline', []))}",
            f"Snapshots de máscaras: {sum(x.get('mask_snapshots', 0) for x in report.get('decision_audit_metrics', {}).values())}",
            f"Canais de recompensa completos: {sum(x.get('reward_channels_complete', 0) for x in report.get('decision_audit_metrics', {}).values())}",
            f"Achados totais: {len(issues)}",
            f"Severidade: CRITICAL={counts['CRITICAL']} | HIGH={counts['HIGH']} | MEDIUM={counts['MEDIUM']} | LOW={counts['LOW']}",
            "", "O relatório completo inclui evidências e limitações; alertas são pistas para investigação, não causalidade automática."
        ]
        self._add_text(layout, "\n".join(overview))
        self._add_chart(layout, "Achados por severidade", list(counts.items()))

        layout = self._page("Decisões")
        decisions = report.get("decision_timeline", [])
        summary = []
        for player, data in sorted(report.get("decision_audit_metrics", {}).items()):
            summary.append(f"{player}: ações={data.get('actions', 0)} | máscaras={data.get('mask_snapshots', 0)} | tipo bloqueado={data.get('chosen_type_disabled', 0)} | falhas de parâmetros={data.get('full_action_validation_failed', 0)} | estado completo={data.get('decision_state_complete', 0)} | recompensas completas={data.get('reward_channels_complete', 0)}")
        self._add_text(layout, "\n".join(summary) or "Sem timeline estruturada; logs legados podem não conter contexto completo.")
        table = QTableWidget(len(decisions), 16)
        table.setHorizontalHeaderLabels(["Jogador", "Round", "Step", "Ação", "Estratégia", "HP", "Nível", "Ouro", "Juros", "Força", "Direção/foco", "Tipos legais", "Tipo permitido", "Parâmetros válidos", "Rew ação/combate/colocação", "UUIDs adicionados/removidos"])
        table.setAlternatingRowColors(True)
        for row, d in enumerate(decisions):
            c, m, r, u = d.get("decision_context") or {}, d.get("legal_action_audit") or {}, d.get("reward_components") or {}, d.get("unit_changes") or {}
            legal = ", ".join(str(x.get("name", x.get("id"))) for x in m.get("legal_action_types", [])) or "—"
            ids = "+" + ",".join(str(x.get("uuid")) for x in u.get("added", [])) + " / -" + ",".join(str(x.get("uuid")) for x in u.get("removed", []))
            values = [d.get("player"), d.get("round"), d.get("step"), d.get("action_name") or d.get("raw_action"), d.get("strategy"), c.get("hp"), c.get("level"), c.get("gold"), c.get("interest_if_resolved_now"), c.get("board_power"), f"{c.get('composition_direction') or '—'} / {c.get('composition_focus') or '—'}", legal, m.get("chosen_type_enabled"), m.get("chosen_action_fully_validated"), " / ".join(_fmt(r.get(k)) for k in ("action", "combat", "placement")), ids]
            for col, value in enumerate(values):
                item = QTableWidgetItem(_fmt(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                table.setItem(row, col, item)
        table.horizontalHeader().setStretchLastSection(True)
        table.resizeColumnsToContents()
        layout.addWidget(table, 1)

        layout = self._page("Máscaras & política")
        rows = []
        table = QTableWidget(len(decisions), 9)
        table.setHorizontalHeaderLabels(["Jogador", "Round", "Step", "Ação", "Status", "Tipos legais", "Tipo permitido", "Validação completa", "Entropia / Value"])
        for row, d in enumerate(decisions):
            m, p = d.get("legal_action_audit") or {}, d.get("policy_diagnostics") or {}
            values = [d.get("player"), d.get("round"), d.get("step"), d.get("action_name"), p.get("status", m.get("policy_status", "—")), ", ".join(str(x.get("name", x.get("id"))) for x in m.get("legal_action_types", [])), m.get("chosen_type_enabled"), m.get("chosen_action_fully_validated"), f"{_fmt(p.get('entropy'))} / {_fmt(p.get('value_estimate'))}"]
            for col, value in enumerate(values):
                item = QTableWidgetItem(_fmt(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                table.setItem(row, col, item)
            rows.append((d, m, p))
        table.horizontalHeader().setStretchLastSection(True)
        table.resizeColumnsToContents()
        details = QPlainTextEdit()
        details.setReadOnly(True)
        def show_details(row, _col):
            if 0 <= row < len(rows):
                d, m, p = rows[row]
                details.setPlainText(json.dumps({
                    "decision_context": d.get("decision_context"), "action": d.get("action"),
                    "legal_action_audit": m, "policy_diagnostics": p,
                    "action_mask_after": d.get("action_mask_after"),
                    "reward_components": d.get("reward_components"),
                    "economic_diagnostics": d.get("economic_diagnostics"),
                    "unit_changes": d.get("unit_changes"),
                }, ensure_ascii=False, indent=2))
        table.cellClicked.connect(show_details)
        layout.addWidget(table, 2)
        layout.addWidget(QLabel("Máscara bruta, distribuição da política, estado e recompensa da decisão selecionada:"))
        layout.addWidget(details, 2)
        if table.rowCount():
            show_details(0, 0)

        layout = self._page("Economia")
        econ = report.get("economic_action_metrics", {})
        econ_text = []
        action_totals = Counter()
        for player, data in sorted(econ.items()):
            econ_text.append(f"{player}: ações={data.get('actions')} | gasto={data.get('gold_spent')} | recuperado={data.get('gold_recovered')} | juros potenciais perdidos={data.get('potential_interest_lost')} | XP sem level-up={data.get('xp_without_level_up')} | XP level-up não aproveitado={data.get('xp_level_up_unused')} | reroll sem ganho imediato={data.get('rerolls_without_immediate_gain')} | reroll seguido de PASS={data.get('rerolls_followed_by_pass')} | ouro final={data.get('final_gold')}")
            for action, vals in (data.get("by_action") or {}).items():
                action_totals[action] += int(vals.get("actions", 0) or 0)
        self._add_chart(layout, "Ações econômicas por tipo", list(action_totals.items()))
        self._add_text(layout, "\n".join(econ_text) or "Sem economic_diagnostics estruturado. Para maior precisão, grave partidas com o snapshot atual da engine.")

        layout = self._page("Estratégia")
        comp_metrics = report.get("composition_direction_metrics", {})
        progression = report.get("team_progression_metrics", {})
        strategy_lines = []
        for player, data in sorted(progression.items()):
            strategy_lines.append(f"{player}: nível final={data.get('final_level')} | HP final={data.get('final_hp')} | ouro final={data.get('final_gold')} | colocação={data.get('final_placement')} | mudanças de comp={data.get('composition_direction_changes')} | ganhos de qualidade={data.get('positioning_improved_actions')} | pioras={data.get('positioning_worsened_actions')}")
        for player, data in sorted(comp_metrics.items()):
            strategy_lines.append(f"{player}: mudanças de direção={data.get('direction_changes')} | com ganho mensurável={data.get('changes_with_measurable_gain')} | sem ganho mensurável={data.get('changes_without_measurable_gain')} | taxa sem ganho={data.get('rate_without_measurable_gain')}")
        self._add_chart(layout, "Mudanças de composição por jogador", [(p, d.get("direction_changes", 0)) for p, d in sorted(comp_metrics.items())])
        self._add_text(layout, "\n".join(strategy_lines) or "Sem métricas estratégicas estruturadas.")

        layout = self._page("Composição")
        purchase = report.get("purchase_sequence_metrics", {})
        lines = []
        for player, data in sorted(purchase.items()):
            classes = data.get("classified_sales", {})
            lines.append(f"{player}: compras={data.get('buys')} | vendas={data.get('sells')} | reversões={data.get('reversed_1')} em ≤1 ação / {data.get('reversed_2')} em ≤2 / {data.get('reversed_4')} em ≤4 | ouro perdido={data.get('net_gold_lost_reversed')} | upgrades={data.get('upgrade_completing_buys')} | vendas core/par={data.get('core_or_pair_sales')} | classificação={classes}")
        self._add_chart(layout, "Compras por jogador", [(p, d.get("buys", 0)) for p, d in sorted(purchase.items())])
        self._add_text(layout, "\n".join(lines) or "Sem snapshots suficientes para correlacionar compras e vendas.")

        layout = self._page("Tabuleiro")
        board = report.get("board_quality_metrics", {})
        board_lines = []
        for player, data in sorted(board.items()):
            board_lines.append(f"{player}: ações avaliadas={data.get('actions_with_metrics')} | ganhos={data.get('positive_quality_delta')} | pioras={data.get('negative_quality_delta')} | neutras={data.get('neutral_quality_delta')} | Δ qualidade média={data.get('mean_quality_delta')} | Δ estrutural={data.get('mean_structural_delta')} | Δ quando combate positivo={data.get('mean_quality_delta_when_combat_reward_positive')} | Δ quando combate negativo={data.get('mean_quality_delta_when_combat_reward_negative')}")
        self._add_chart(layout, "Variação média de qualidade do tabuleiro", [(p, d.get("mean_quality_delta", 0)) for p, d in sorted(board.items())])
        self._add_text(layout, "\n".join(board_lines) or "Sem métricas de qualidade/posicionamento nos snapshots.")

        layout = self._page("Itens")
        item_lines = []
        text_metrics = report.get("text_log_metrics", {})
        for player, data in sorted(text_metrics.items()):
            action_counts = data.get("action_counts", {})
            item_lines.append(
                f"{player}: snapshots de inventário={data.get('item_snapshots', 0)} | "
                f"snapshots com itens/componentes={data.get('item_nonempty_snapshots', 0)} | "
                f"ações de item identificadas={action_counts.get('ITEM', 0)}"
            )
            item_events = [event for event in data.get("timeline", []) if event.get("action") == "ITEM"]
            for event in item_events[:100]:
                item_lines.append(
                    f"  linha {event.get('line')} · round {event.get('round')} · "
                    f"{event.get('raw_action')} · recompensa {event.get('reward')}"
                )
        self._add_text(layout, "\n".join(item_lines) or "Nenhum snapshot textual de itens encontrado. Os logs antigos podem registrar apenas componentes/itens visíveis no fim do round, sem histórico completo de bigorna, transferência ou equipamento.")

        layout = self._page("Loops e movimentos")
        movement_issues = [x for x in issues if "LOOP" in str(x.get("code", "")).upper() or "MOVE" in str(x.get("code", "")).upper() or "CYCLE" in str(x.get("code", "")).upper()]
        self._add_chart(layout, "Achados de loops/movimentos por severidade", list(Counter(x.get("severity", "UNKNOWN") for x in movement_issues).items()))
        self._add_text(layout, "\n".join(
            f"[{x.get('severity')}] jogador {x.get('player')} rodada {x.get('round')} step {x.get('step')}: {x.get('code')} — {x.get('message')} | evidência={_fmt(x.get('evidence'))}"
            for x in movement_issues
        ) or "Nenhum ciclo textual/estrutural identificado nos dados disponíveis. Ciclos de estado exatos exigem snapshots estruturados.")

        layout = self._page("Qualidade dos dados")
        self._add_text(layout, "\n".join([
            f"Arquivos registrados: {len(report.get('log_files', []))}",
            f"Jogadores únicos: {len(report.get('players_seen', []))}/8",
            f"Entradas estruturadas lidas: {report.get('entries_read', 0)}",
            f"Diagnósticos ausentes: {report.get('diagnostics_missing', 0)}",
            "", "Limitações registradas pelo analisador:",
            *[f"- {note}" for note in report.get("notes", [])],
            "", "Importante: uma métrica ausente é marcada como não disponível; não deve ser interpretada como zero.",
            "Logs legados em texto não registram a máscara completa de ações legais nem os canais de recompensa separados; nesses casos a timeline contém recompensa total e flags de revisão, não uma prova de que a ação era ótima.",
            f"Decisões reconstruídas: {len(report.get('decision_timeline', []))}"
        ]))
        layout = self._page("Achados")
        issue_rows = sorted(issues, key=lambda x: ({"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}.get(x.get("severity"), 4), str(x.get("player")), str(x.get("step"))))
        table = QTableWidget(len(issue_rows), 7)
        table.setHorizontalHeaderLabels(["Severidade", "Jogador", "Round", "Step", "Código", "Descrição", "Evidência"])
        table.setWordWrap(True)
        table.setAlternatingRowColors(True)
        for row, issue in enumerate(issue_rows):
            values = [issue.get("severity"), issue.get("player"), issue.get("round"), issue.get("step"), issue.get("code"), issue.get("message"), _fmt(issue.get("evidence"))]
            for col, value in enumerate(values):
                item = QTableWidgetItem(_fmt(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                table.setItem(row, col, item)
        table.horizontalHeader().setStretchLastSection(True)
        table.resizeColumnsToContents()
        layout.addWidget(table)
        self.tabs.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = AuditWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
