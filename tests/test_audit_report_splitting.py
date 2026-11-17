from pathlib import Path

import pytest

from scripts.audit_viewer_match import (
    finalize_markdown_documents,
    split_markdown_into_three_parts,
)
from scripts.strategic_economic_comparison import classify_candidate_selection


def test_selection_integrity_distinguishes_not_applicable_and_real_failures():
    assert classify_candidate_selection(0, [], -1) == "NOT_APPLICABLE"
    assert classify_candidate_selection(2, [], 7) == "INCOMPLETE"
    assert classify_candidate_selection(2, [7], None) == "INCOMPLETE"
    assert classify_candidate_selection(2, [7], 7) == "CONSISTENT"
    assert classify_candidate_selection(2, [8], 7) == "INCONSISTENT"
    assert classify_candidate_selection(0, [7], 7) == "INCONSISTENT"


def test_split_preserves_exact_content_and_keeps_tables_inside_sections():
    source = (
        "# Relatório\n\nIntrodução preservada.\n\n"
        "## Seção A\n\n| Coluna | Valor |\n|---|---|\n| A | 1 |\n\n"
        "## Seção B\n\nTexto B.\n\n"
        "## Seção C\n\n| Campo | Valor |\n|---|---|\n| C | 3 |\n"
    )
    parts = split_markdown_into_three_parts(source)
    assert len(parts) == 3
    assert "".join(parts) == source
    assert all(part.strip() for part in parts)
    assert "| A | 1 |" in parts[0]
    assert "| C | 3 |" in parts[2]


def test_finalizer_writes_six_parts_updates_indexes_and_removes_monoliths(tmp_path: Path):
    general = "# Geral\n\n## A\nA\n\n## B\nB\n\n## C\nC\n"
    actions = "# Ações\n\n## A\nA\n\n## B\nB\n\n## C\nC\n"
    (tmp_path / "audit_report_geral.md").write_text("old general", encoding="utf-8")
    (tmp_path / "audit_acoes.md").write_text("old actions", encoding="utf-8")
    docs = {
        "audit_report_geral.md": general,
        "audit_acoes.md": actions,
        "audit_report.md": (
            "- [Resumo geral](audit_report_geral.md)\n"
            "- [Action Evaluator](audit_acoes.md)\n"
        ),
        "audit_report_completo.md": (
            "- [Resumo geral](audit_report_geral.md)\n"
            "- [Action Evaluator](audit_acoes.md)\n"
        ),
        "audit_ppo.md": "# PPO\n",
    }

    written = finalize_markdown_documents(tmp_path, docs)

    assert len([name for name in written if "parte_" in name]) == 6
    assert not (tmp_path / "audit_report_geral.md").exists()
    assert not (tmp_path / "audit_acoes.md").exists()
    assert "".join((tmp_path / f"audit_report_geral_parte_{i}.md").read_text(encoding="utf-8") for i in range(1, 4)) == general
    assert "".join((tmp_path / f"audit_acoes_parte_{i}.md").read_text(encoding="utf-8") for i in range(1, 4)) == actions
    index = (tmp_path / "audit_report.md").read_text(encoding="utf-8")
    assert "audit_report_geral_parte_1.md" in index
    assert "audit_acoes_parte_3.md" in index


def test_failed_split_keeps_original_reports(tmp_path: Path):
    original = "# Relatório sem seções suficientes\n\nSó um bloco.\n"
    (tmp_path / "audit_acoes.md").write_text(original, encoding="utf-8")
    docs = {"audit_acoes.md": original}

    with pytest.raises(ValueError):
        finalize_markdown_documents(tmp_path, docs)

    assert (tmp_path / "audit_acoes.md").read_text(encoding="utf-8") == original
