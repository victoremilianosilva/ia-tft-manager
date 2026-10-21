
import json
from pathlib import Path

import pandas as pd
import streamlit as st
from tensorboard.backend.event_processing.event_accumulator import (
    EventAccumulator,
)

LOG_DIR = Path("tft_logs")

st.set_page_config(
    page_title="TFT Metrics Explorer",
    layout="wide",
)

st.title("TFT AI — Metrics Explorer")
st.caption("Explore, filtre e exporte métricas do treinamento.")

@st.cache_data
def load_metrics(log_dir: str):
    root = Path(log_dir)
    result = {}

    if not root.exists():
        return result

    for event_file in root.rglob("events.out.tfevents.*"):
        try:
            acc = EventAccumulator(
                str(event_file),
                size_guidance={"scalars": 0},
            )
            acc.Reload()

            run_name = str(event_file.parent)

            for tag in acc.Tags().get("scalars", []):
                key = f"{run_name} :: {tag}"
                result.setdefault(key, [])

                result[key].extend(
                    {
                        "step": item.step,
                        "value": item.value,
                        "wall_time": item.wall_time,
                    }
                    for item in acc.Scalars(tag)
                )
        except Exception as exc:
            st.warning(f"Não foi possível ler {event_file}: {exc}")

    # Ordena e remove duplicatas exatas de step.
    for key in result:
        df = pd.DataFrame(result[key])
        if not df.empty:
            result[key] = (
                df.sort_values("wall_time")
                .drop_duplicates(subset=["step"], keep="last")
                .sort_values("step")
                .to_dict("records")
            )

    return result


data = load_metrics(str(LOG_DIR))

if not data:
    st.error(
        f"Nenhuma métrica encontrada em '{LOG_DIR}'. "
        "Verifique o caminho dos logs."
    )
    st.stop()

st.success(f"{len(data)} séries de métricas encontradas.")

metric_names = sorted(data.keys())

selected = st.multiselect(
    "Selecione uma ou várias métricas",
    options=metric_names,
    default=metric_names[: min(2, len(metric_names))],
)

if not selected:
    st.info("Selecione pelo menos uma métrica.")
    st.stop()

all_steps = [
    item["step"]
    for name in selected
    for item in data[name]
]

if not all_steps:
    st.warning("As métricas selecionadas não possuem dados.")
    st.stop()

min_step = int(min(all_steps))
max_step = int(max(all_steps))

col1, col2 = st.columns(2)

with col1:
    start_step = st.number_input(
        "Update inicial",
        min_value=min_step,
        max_value=max_step,
        value=min_step,
        step=1,
    )

with col2:
    end_step = st.number_input(
        "Update final",
        min_value=min_step,
        max_value=max_step,
        value=max_step,
        step=1,
    )

if start_step > end_step:
    st.error("O update inicial deve ser menor ou igual ao final.")
    st.stop()

filtered = {}

for name in selected:
    df = pd.DataFrame(data[name])

    df = df[
        df["step"].between(start_step, end_step)
    ].sort_values("step")

    if not df.empty:
        filtered[name] = df

st.subheader("Resultados")

if not filtered:
    st.warning("Nenhuma amostra encontrada nesse intervalo.")
    st.stop()

for name, df in filtered.items():
    with st.expander(name, expanded=True):
        c1, c2, c3 = st.columns(3)
        c1.metric("Amostras", len(df))
        c2.metric("Primeiro valor", f"{df.iloc[0]['value']:.6g}")
        c3.metric("Último valor", f"{df.iloc[-1]['value']:.6g}")

        st.line_chart(
            df.set_index("step")[["value"]],
            height=220,
        )

combined = pd.concat(
    [
        df.assign(metric=name)
        for name, df in filtered.items()
    ],
    ignore_index=True,
)

st.subheader("Exportação")

csv_bytes = combined[
    ["metric", "step", "value", "wall_time"]
].to_csv(index=False).encode("utf-8")

json_bytes = json.dumps(
    {
        name: df[
            ["step", "value", "wall_time"]
        ].to_dict("records")
        for name, df in filtered.items()
    },
    ensure_ascii=False,
    indent=2,
).encode("utf-8")

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "Baixar CSV",
        data=csv_bytes,
        file_name="tensorboard_metrics.csv",
        mime="text/csv",
        use_container_width=True,
    )

with col2:
    st.download_button(
        "Baixar JSON",
        data=json_bytes,
        file_name="tensorboard_metrics.json",
        mime="application/json",
        use_container_width=True,
    )

st.subheader("Tabela completa")
st.dataframe(
    combined[
        ["metric", "step", "value", "wall_time"]
    ],
    use_container_width=True,
    hide_index=True,
)
