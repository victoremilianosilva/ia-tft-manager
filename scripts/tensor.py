import json
from pathlib import Path
from tensorboard.backend.event_processing.event_accumulator import (
    EventAccumulator,
)

# Ajuste para a pasta que contém os eventos do TensorBoard.
LOG_DIR = Path("runs")
OUTPUT = Path("tensorboard_export.json")

result = {}

for event_file in LOG_DIR.rglob("events.out.tfevents.*"):
    accumulator = EventAccumulator(str(event_file))
    accumulator.Reload()

    run_name = str(event_file.parent)
    result[run_name] = {}

    for tag in accumulator.Tags().get("scalars", []):
        values = accumulator.Scalars(tag)

        result[run_name][tag] = [
            {
                "step": item.step,
                "value": item.value,
                "wall_time": item.wall_time,
            }
            for item in values
        ]

with OUTPUT.open("w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=2)

print(f"Exportação concluída: {OUTPUT.resolve()}")
