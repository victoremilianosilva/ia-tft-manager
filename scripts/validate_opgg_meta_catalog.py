#!/usr/bin/env python3
"""Validate OP.GG meta catalog freshness, set identity and local unit coverage."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_META = ROOT / "data" / "opgg_tft_meta.json"
DEFAULT_UNITS = ROOT / "data" / "units_gerado.json"


def _set_numbers(units: list[dict[str, Any]]) -> set[str]:
    found: set[str] = set()
    for unit in units:
        for key in ("apiName", "characterName", "api_name", "character_name"):
            value = unit.get(key)
            if not isinstance(value, str):
                continue
            match = re.match(r"^DA_(\d+)_", value)
            if match:
                found.add(match.group(1))
    return found


def validate_catalog(
    meta: dict[str, Any],
    units_doc: Any,
    *,
    max_age_hours: float = 168.0,
    min_coverage: float = 0.90,
    now: datetime | None = None,
) -> dict[str, Any]:
    if not isinstance(meta, dict) or meta.get("schema_version") != 1:
        raise ValueError("Catálogo OP.GG inválido: schema_version deve ser 1.")
    if meta.get("source") != "op.gg":
        raise ValueError("Catálogo OP.GG inválido: source incompatível.")
    compositions = meta.get("compositions")
    if not isinstance(compositions, list) or not compositions:
        raise ValueError("Catálogo OP.GG sem composições.")

    stamp_raw = meta.get("fetched_at")
    try:
        stamp = datetime.fromisoformat(str(stamp_raw).replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError) as exc:
        raise ValueError("Catálogo OP.GG sem fetched_at ISO-8601 válido.") from exc
    now = now or datetime.now(timezone.utc)
    age_hours = (now - stamp.astimezone(timezone.utc)).total_seconds() / 3600.0
    if age_hours < -1.0:
        raise ValueError("Catálogo OP.GG tem timestamp no futuro.")
    if age_hours > max_age_hours:
        raise ValueError(
            f"Catálogo OP.GG desatualizado: {age_hours:.1f}h > {max_age_hours:.1f}h."
        )

    if not isinstance(units_doc, list):
        raise ValueError("Catálogo local de unidades deve ser uma lista JSON.")
    local_keys: set[str] = set()
    for unit in units_doc:
        if not isinstance(unit, dict):
            continue
        for key in ("apiName", "characterName", "api_name", "character_name", "name"):
            value = unit.get(key)
            if isinstance(value, str) and value:
                local_keys.add(value)

    meta_keys: set[str] = set()
    set_ids: set[str] = set()
    for comp in compositions:
        if not isinstance(comp, dict):
            continue
        team_code = comp.get("team_code", "")
        if isinstance(team_code, str):
            match = re.search(r"TFTSet(\d+)", team_code)
            if match:
                set_ids.add(match.group(1))
        for group in ("units", "early_game", "mid_game"):
            value = comp.get(group)
            group_units = value.get("units", []) if isinstance(value, dict) else value
            if not isinstance(group_units, list):
                continue
            for unit in group_units:
                if isinstance(unit, dict) and isinstance(unit.get("key"), str) and unit["key"]:
                    meta_keys.add(unit["key"])

    local_set_ids = _set_numbers(units_doc)
    if len(set_ids) > 1:
        raise ValueError(f"Catálogo OP.GG mistura conjuntos: {sorted(set_ids)}.")
    if set_ids and local_set_ids and not set_ids.issubset(local_set_ids):
        raise ValueError(
            f"Conjunto OP.GG {sorted(set_ids)} incompatível com unidades locais "
            f"{sorted(local_set_ids)}."
        )

    mapped = meta_keys & local_keys
    coverage = len(mapped) / len(meta_keys) if meta_keys else 0.0
    report = {
        "composition_count": len(compositions),
        "meta_unique_unit_keys": len(meta_keys),
        "mapped_unit_keys": len(mapped),
        "unmapped_unit_keys": sorted(meta_keys - local_keys),
        "coverage": coverage,
        "meta_set_ids": sorted(set_ids),
        "local_set_ids": sorted(local_set_ids),
        "age_hours": age_hours,
    }
    if coverage < min_coverage:
        raise ValueError(
            f"Cobertura de unidades OP.GG insuficiente: {len(mapped)}/{len(meta_keys)} "
            f"({coverage:.1%}); mínimo={min_coverage:.1%}. Não use o catálogo."
        )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--meta", type=Path, default=DEFAULT_META)
    parser.add_argument("--units", type=Path, default=DEFAULT_UNITS)
    parser.add_argument("--max-age-hours", type=float, default=168.0)
    parser.add_argument("--min-coverage", type=float, default=0.90)
    args = parser.parse_args(argv)
    try:
        meta = json.loads(args.meta.read_text(encoding="utf-8"))
        units = json.loads(args.units.read_text(encoding="utf-8"))
        print(json.dumps(validate_catalog(meta, units, max_age_hours=args.max_age_hours,
                                          min_coverage=args.min_coverage),
                         ensure_ascii=False, indent=2))
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Catálogo OP.GG rejeitado: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
