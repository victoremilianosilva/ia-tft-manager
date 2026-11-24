#!/usr/bin/env python3
"""Build Set 18 trait-to-unit membership from the normalized champion catalog.

The trait source carries authoritative trait identity and tier data; the unit
catalog carries the roster membership. This script joins those two sources
without guessing from descriptions or display-name substrings.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def build_trait_catalog(traits_payload: dict[str, Any],
                        units_payload: list[dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(traits_payload, dict) or not isinstance(traits_payload.get("traits"), list):
        raise ValueError("Trait source must contain a traits array")
    if not isinstance(units_payload, list):
        raise ValueError("Unit source must be an array")

    aliases: dict[str, str] = {}
    traits_by_id: dict[str, dict[str, Any]] = {}
    for trait in traits_payload["traits"]:
        if not isinstance(trait, dict):
            raise ValueError("Trait entries must be objects")
        api_name = trait.get("apiName")
        if not isinstance(api_name, str) or not api_name.strip():
            raise ValueError("Every trait requires a non-empty apiName")
        if api_name in traits_by_id:
            raise ValueError(f"Duplicate trait apiName: {api_name}")
        traits_by_id[api_name] = trait
        for alias in (trait.get("name"), trait.get("en_name")):
            if not isinstance(alias, str) or not alias.strip():
                continue
            previous = aliases.get(alias)
            if previous is not None and previous != api_name:
                raise ValueError(f"Ambiguous trait display name: {alias}")
            aliases[alias] = api_name

    membership: dict[str, set[str]] = {api_name: set() for api_name in traits_by_id}
    for unit in units_payload:
        if not isinstance(unit, dict):
            raise ValueError("Unit entries must be objects")
        unit_id = unit.get("apiName")
        if not isinstance(unit_id, str) or not unit_id.strip():
            raise ValueError("Every unit requires a non-empty apiName")
        unit_traits = unit.get("traits", [])
        if not isinstance(unit_traits, list) or any(not isinstance(x, str) for x in unit_traits):
            raise ValueError(f"Invalid traits list for unit {unit_id}")
        for trait_name in unit_traits:
            trait_id = aliases.get(trait_name)
            if trait_id is None:
                raise ValueError(f"Unit {unit_id} references unknown trait {trait_name}")
            membership[trait_id].add(unit_id)

    result = dict(traits_payload)
    result["traits"] = []
    for source_trait in traits_payload["traits"]:
        trait = dict(source_trait)
        unit_ids = sorted(membership[trait["apiName"]])
        trait["units"] = unit_ids
        trait["unit_mapping_source"] = "data/units_gerado.json"
        trait["unit_mapping_status"] = "mapped" if unit_ids else "unmapped_source_trait"
        result["traits"].append(trait)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--traits", type=Path, default=Path("data/traits.json"))
    parser.add_argument("--units", type=Path, default=Path("data/units_gerado.json"))
    parser.add_argument("--output", type=Path, default=Path("data/traits.json"))
    parser.add_argument("--check", action="store_true",
                        help="fail when output differs instead of writing it")
    args = parser.parse_args()

    source = json.loads(args.traits.read_text(encoding="utf-8"))
    units = json.loads(args.units.read_text(encoding="utf-8"))
    generated = build_trait_catalog(source, units)
    rendered = json.dumps(generated, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        current = args.output.read_text(encoding="utf-8")
        if current != rendered:
            raise SystemExit(f"{args.output} is stale; run scripts/generate_trait_catalog.py")
        print(f"{args.output}: up to date")
    else:
        args.output.write_text(rendered, encoding="utf-8")
        mapped = sum(bool(t["units"]) for t in generated["traits"])
        print(f"Wrote {args.output}: {mapped}/{len(generated['traits'])} traits mapped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
