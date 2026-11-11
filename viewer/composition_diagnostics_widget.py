"""Read-only Qt tab for browsing and auditing Composition Intelligence JSONL."""
from __future__ import annotations

import json
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QFileDialog, QComboBox, QPlainTextEdit, QSplitter,
)

from viewer.composition_diagnostics import (
    audit_diagnostic_records, format_diagnostic_audit, load_diagnostic_jsonl,
)


class CompositionDiagnosticsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.records: list[dict] = []
        self.source_path: Path | None = None
        root = QVBoxLayout(self)
        header = QHBoxLayout()
        header.addWidget(QLabel("Arquivo de diagnósticos JSONL:"))
        self.path_input = QLineEdit()
        self.path_input.setReadOnly(True)
        self.path_input.setPlaceholderText("Selecione um JSONL exportado pelo CompositionDiagnosticRecorder")
        header.addWidget(self.path_input, 1)
        self.open_button = QPushButton("Abrir JSONL")
        self.open_button.clicked.connect(self._choose_file)
        header.addWidget(self.open_button)
        self.reload_button = QPushButton("Recarregar")
        self.reload_button.clicked.connect(self.reload)
        header.addWidget(self.reload_button)
        root.addLayout(header)
        self.status = QLabel(
            "Aguardando arquivo. O Viewer não gera snapshots de Composition Intelligence por conta própria; "
            "carregue o JSONL exportado pelo recorder."
        )
        self.status.setWordWrap(True)
        self.status.setObjectName("muted")
        root.addWidget(self.status)
        self.snapshot_selector = QComboBox()
        self.snapshot_selector.currentIndexChanged.connect(self._show_selected_snapshot)
        root.addWidget(self.snapshot_selector)
        splitter = QSplitter(Qt.Orientation.Vertical)
        self.audit_view = QPlainTextEdit()
        self.audit_view.setReadOnly(True)
        self.snapshot_view = QPlainTextEdit()
        self.snapshot_view.setReadOnly(True)
        splitter.addWidget(self.audit_view)
        splitter.addWidget(self.snapshot_view)
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 3)
        root.addWidget(splitter, 1)

    def set_session_directory(self, directory: str | Path | None):
        if directory is None:
            return
        candidate = Path(directory) / "composition_diagnostics.jsonl"
        if candidate.is_file():
            self.path_input.setText(str(candidate))
            self.reload()
        else:
            self.status.setText(
                f"Sessão: {directory}. Ainda não existe composition_diagnostics.jsonl nesta sessão. "
                "A arquitetura permanece shadow/read-only; importe um arquivo quando o recorder o produzir."
            )

    def _choose_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Abrir auditoria Composition Intelligence", str(Path.home()),
            "JSONL (*.jsonl *.ndjson);;Todos os arquivos (*)",
        )
        if path:
            self.path_input.setText(path)
            self.reload()

    def reload(self):
        raw_path = self.path_input.text().strip()
        if not raw_path:
            self.status.setText("Selecione um arquivo JSONL.")
            return
        path = Path(raw_path).expanduser()
        if not path.is_file():
            self.status.setText(f"Arquivo não encontrado: {path}")
            return
        try:
            self.records, errors = load_diagnostic_jsonl(path)
        except OSError as exc:
            self.status.setText(f"Não foi possível ler o arquivo: {exc}")
            return
        self.source_path = path
        report = audit_diagnostic_records(self.records, errors)
        self.audit_view.setPlainText(format_diagnostic_audit(self.records, report))
        self.snapshot_selector.blockSignals(True)
        self.snapshot_selector.clear()
        for index, record in enumerate(self.records):
            self.snapshot_selector.addItem(
                f"#{record.get('sequence', index + 1)} · R{record.get('round', '?')} · "
                f"{record.get('composition_id') or 'sem composição'} v{record.get('composition_version', '?')} "
                f"{'· STALE' if record.get('stale') else ''}", index,
            )
        self.snapshot_selector.blockSignals(False)
        self.status.setText(
            f"{len(self.records)} snapshots carregados de {path.name}; "
            f"{len(errors)} linhas inválidas/ignoradas. Visualização somente leitura."
        )
        self._show_selected_snapshot(self.snapshot_selector.currentIndex())

    def _show_selected_snapshot(self, combo_index: int):
        if combo_index < 0 or combo_index >= len(self.records):
            self.snapshot_view.clear()
            return
        record = self.records[combo_index]
        sections = {
            "ENVELOPE": {key: value for key, value in record.items() if key != "diagnostics"},
            "CLASSIFICATION": record.get("classification", {}),
            "DIAGNOSTICS": record.get("diagnostics", {}),
        }
        self.snapshot_view.setPlainText(json.dumps(sections, ensure_ascii=False, indent=2))
