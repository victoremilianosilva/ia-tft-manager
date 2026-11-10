"""Local Streamlit viewer for fine-tuning JSONL traces and Markdown reports."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUN = ROOT / "economy_finetuning" / "runs" / "latest"


@st.cache_data(show_spinner=False)
def load_jsonl(path_text: str, limit: int = 200_000):
    path = Path(path_text)
    rows = []
    if not path.is_file():
        return pd.DataFrame()
    with path.open("r", encoding="utf-8") as stream:
        for index, line in enumerate(stream):
            if index >= limit:
                break
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return pd.json_normalize(rows, sep=".")


def main():
    st.set_page_config(page_title="TFT Economy Fine-tuning", layout="wide")
    st.title("TFT Economy Fine-tuning Analyzer")
    st.caption("Comparação offline entre checkpoint original e fine-tuned. Os números vêm dos JSONL locais.")
    run_dir = Path(st.text_input("Diretório da execução", str(DEFAULT_RUN))).expanduser()
    logs = run_dir / "logs"
    reports = run_dir / "reports"
    trace_path = logs / "decision_trace.jsonl"
    scenarios_path = logs / "scenario_results.jsonl"
    updates_path = logs / "training_metrics.jsonl"

    trace = load_jsonl(str(trace_path))
    updates = load_jsonl(str(updates_path))
    scenarios = load_jsonl(str(scenarios_path))

    if trace.empty:
        st.warning(f"Nenhum decision_trace.jsonl encontrado em {trace_path}. Execute o fine-tuning primeiro.")
    else:
        total = len(trace)
        different = (
            trace.apply(
                lambda row: row.get("original_action") != row.get("finetuned_action"),
                axis=1,
            ).sum()
        )
        c1, c2, c3 = st.columns(3)
        c1.metric("Estados comparados", f"{total:,}")
        c2.metric("Ações divergentes", f"{int(different):,}")
        c3.metric("Taxa de divergência", f"{different / max(1, total):.1%}")

        st.subheader("Mudança na distribuição de ações")
        def action_name(value):
            names = ["BUY", "REROLL", "BUY_XP", "MOVE_BENCH", "MOVE_BOARD",
                     "SELL", "PASS", "EQUIP_FROM_INVENTORY", "CRAFT_AND_EQUIP"]
            try:
                return names[int(value[0])]
            except (TypeError, ValueError, IndexError):
                return "UNKNOWN"
        original_counts = trace["original_action"].map(action_name).value_counts()
        tuned_counts = trace["finetuned_action"].map(action_name).value_counts()
        action_frame = pd.concat(
            [original_counts.rename("Original"), tuned_counts.rename("Fine-tuned")],
            axis=1,
        ).fillna(0)
        st.bar_chart(action_frame)

        st.subheader("Investigar divergências")
        divergent = trace[
            trace.apply(lambda row: row.get("original_action") != row.get("finetuned_action"), axis=1)
        ].copy()
        if not divergent.empty:
            scenario_values = sorted({
                item for values in divergent.get("scenario_ids", [])
                if isinstance(values, list) for item in values
            })
            selected = st.multiselect("Filtrar cenários", scenario_values, default=scenario_values)
            if selected:
                divergent = divergent[
                    divergent["scenario_ids"].apply(
                        lambda values: isinstance(values, list) and bool(set(values) & set(selected))
                    )
                ]
            display_columns = [
                column for column in [
                    "step", "update", "player_id", "state.hp", "state.gold",
                    "state.level", "state.stage", "state.strategy_name",
                    "scenario_ids", "original_action", "finetuned_action",
                ] if column in divergent.columns
            ]
            st.dataframe(divergent[display_columns], use_container_width=True, hide_index=True)
            st.download_button(
                "Exportar divergências filtradas",
                divergent.to_csv(index=False).encode("utf-8"),
                file_name="decision_differences.csv",
                mime="text/csv",
            )

        st.subheader("Distribuições de política")
        if "original_type_probabilities" in trace.columns:
            st.caption("Distribuições da cabeça de tipo; valores condicionais de slots não são representados neste gráfico.")
            st.dataframe(
                trace[["step", "player_id", "original_type_probabilities", "finetuned_type_probabilities"]].head(500),
                use_container_width=True,
                hide_index=True,
            )

    if not updates.empty:
        st.subheader("Evolução do treinamento")
        numeric = updates.select_dtypes(include="number")
        if not numeric.empty:
            chart_cols = [column for column in ["mean_reward", "matched_transitions", "approx_kl_max"] if column in numeric]
            if chart_cols:
                st.line_chart(numeric[chart_cols])

    if not scenarios.empty:
        st.subheader("Resultados de episódios")
        st.dataframe(scenarios, use_container_width=True, hide_index=True)

    report_candidates = [
        reports / "ECONOMY_FINETUNING_AUDIT.md",
        ROOT / "economy_finetuning" / "reports" / "ECONOMY_FINETUNING_AUDIT.md",
    ]
    report_path = next((candidate for candidate in report_candidates if candidate.is_file()), None)
    if report_path is not None:
        st.subheader("Auditoria Markdown")
        st.markdown(report_path.read_text(encoding="utf-8"))
    else:
        st.info("A auditoria Markdown ainda não foi gerada. Execute economy_finetuning/audit.py.")


if __name__ == "__main__":
    main()
