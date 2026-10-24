
import csv
from pathlib import Path
from tensorboard.backend.event_processing.event_accumulator import (
    EventAccumulator,
)

LOG_DIR = Path("tft_logs")
OUTPUT = Path("tft_logs_export.csv")

# Busca arquivos de eventos em tft_logs e subpastas.
event_files = list(LOG_DIR.rglob("events.out.tfevents.*"))

if not event_files:
    raise SystemExit(
        f"Nenhum arquivo TensorBoard encontrado em: {LOG_DIR.resolve()}"
    )

# Seleciona o arquivo modificado mais recentemente.
latest_file = max(event_files, key=lambda path: path.stat().st_mtime)

print(f"📂 Arquivo selecionado: {latest_file}")
print("📊 Carregando métricas...")

accumulator = EventAccumulator(
    str(latest_file),
    size_guidance={"scalars": 0},
)
accumulator.Reload()

rows = []

for tag in accumulator.Tags().get("scalars", []):
    for item in accumulator.Scalars(tag):
        rows.append({
            "tag": tag,
            "step": item.step,
            "value": item.value,
            "wall_time": item.wall_time,
        })

if not rows:
    raise SystemExit("Nenhuma métrica escalar encontrada no arquivo.")

# Exporta ao lado do script.
with OUTPUT.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["tag", "step", "value", "wall_time"],
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"\n✅ Total de amostras exportadas: {len(rows)}")
print(f"📄 CSV gerado: {OUTPUT.resolve()}")
