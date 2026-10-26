#!/usr/bin/env python3
"""Generate the Set 18 champion, trait and item catalogs from CommunityDragon.

Source: https://raw.communitydragon.org/latest/cdragon/tft/en_us.json
The source is downloaded only when this script is run; generated files are
versioned so training does not depend on runtime network access.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path
from typing import Any

SOURCE_URL = "https://raw.communitydragon.org/latest/cdragon/tft/en_us.json"
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load_source(path: Path | None) -> dict[str, Any]:
    if path is not None:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    else:
        request = urllib.request.Request(
            SOURCE_URL, headers={"User-Agent": "TFT-AI-set-data-generator/1.0"}
        )
        with urllib.request.urlopen(request, timeout=90) as response:
            data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("setData"), list):
        raise ValueError("Fonte inválida: esperava um CommunityDragon TFT JSON com setData.")
    return data


def select_set(source: dict[str, Any], set_number: int) -> tuple[str, list[dict[str, Any]]]:
    entries = [
        entry for entry in source["setData"]
        if isinstance(entry, dict) and str(entry.get("number")) == str(set_number)
    ]
    if not entries:
        raise ValueError(f"Set {set_number} não encontrado na fonte.")
    names = {str(entry.get("name", "")) for entry in entries}
    if len(names) != 1:
        raise ValueError(f"Set {set_number} ambíguo: {sorted(names)}")
    return names.pop(), entries


def _number(value: Any, default: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return default
    return float(value)


def build_units(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_api: dict[str, dict[str, Any]] = {}
    trait_names: dict[str, str] = {}
    for entry in entries:
        for trait in entry.get("traits", []):
            if isinstance(trait, dict) and trait.get("apiName"):
                trait_names[str(trait["apiName"])] = str(trait.get("name") or trait["apiName"])
        for champ in entry.get("champions", []):
            if not isinstance(champ, dict):
                continue
            api = str(champ.get("apiName") or "")
            cost = champ.get("cost")
            name = str(champ.get("name") or "").strip()
            traits = champ.get("traits")
            if not api or not name or not isinstance(cost, int) or not 1 <= cost <= 5:
                continue
            if not isinstance(traits, list) or not traits:
                continue
            # SetData can contain multiple mode variants. Prefer the most complete
            # entry for a champion and de-duplicate by the canonical API name.
            old = by_api.get(api)
            if old is not None and len(old.get("traits", [])) >= len(traits):
                continue
            stats = champ.get("stats") if isinstance(champ.get("stats"), dict) else {}
            ability = champ.get("ability") if isinstance(champ.get("ability"), dict) else {}
            api_traits = [str(trait) for trait in traits if isinstance(trait, str)]
            by_api[api] = {
                "apiName": api,
                "characterName": str(champ.get("characterName") or api),
                "name": name,
                "cost": cost,
                "icon": str(champ.get("icon") or ""),
                "squareIcon": str(champ.get("squareIcon") or champ.get("icon") or ""),
                "tileIcon": str(champ.get("tileIcon") or champ.get("squareIcon") or champ.get("icon") or ""),
                "traits": api_traits,
                "stats": {
                    "max_hp": _number(stats.get("hp")),
                    "attack_damage": _number(stats.get("damage")),
                    "attack_speed": _number(stats.get("attackSpeed")),
                    "armor": _number(stats.get("armor")),
                    "magic_resist": _number(stats.get("magicResist")),
                    "attack_range": _number(stats.get("range")),
                    "max_mana": _number(stats.get("mana")),
                    "initial_mana": _number(stats.get("initialMana")),
                },
                "ability": {
                    "name": str(ability.get("name") or ""),
                    "desc": str(ability.get("desc") or ""),
                    "icon": str(ability.get("icon") or ""),
                    "variables": ability.get("variables") if isinstance(ability.get("variables"), list) else [],
                },
                "role": 3,
                "role_name": "fighter",
            }
    units = list(by_api.values())
    if not units:
        raise ValueError("Nenhum campeão jogável (custo 1–5 com traits) foi encontrado.")
    units.sort(key=lambda unit: (unit["cost"], unit["name"].casefold(), unit["apiName"]))
    for unit in units:
        unit["traits"] = [trait_names.get(api, api) for api in unit["traits"]]
    return units


def build_traits(entries: list[dict[str, Any]], units: list[dict[str, Any]]) -> dict[str, Any]:
    unit_by_api = {unit["apiName"]: unit for unit in units}
    traits: dict[str, dict[str, Any]] = {}
    for entry in entries:
        for trait in entry.get("traits", []):
            if not isinstance(trait, dict):
                continue
            api = str(trait.get("apiName") or "")
            if not api:
                continue
            # Merge trait records across same-set variants; later duplicates are
            # only used if they add breakpoints or description data.
            current = traits.get(api)
            if current is None or len(trait.get("effects", [])) > len(current.get("effects", [])):
                traits[api] = {
                    "apiName": api,
                    "name": str(trait.get("name") or api),
                    "desc": str(trait.get("desc") or ""),
                    "icon": str(trait.get("icon") or ""),
                    "effects": trait.get("effects") if isinstance(trait.get("effects"), list) else [],
                    "units": [],
                    "en_name": str(trait.get("name") or api),
                }
    for unit in units:
        # Resolve back to source API traits by matching the unit record in the
        # selected set entries; never guess from localized display names.
        for entry in entries:
            for champ in entry.get("champions", []):
                if isinstance(champ, dict) and champ.get("apiName") == unit["apiName"]:
                    for api in champ.get("traits", []):
                        if api in traits:
                            item = {"unit": unit["apiName"], "unit_cost": unit["cost"]}
                            if item not in traits[api]["units"]:
                                traits[api]["units"].append(item)
    for trait in traits.values():
        trait["units"].sort(key=lambda item: (item["unit_cost"], item["unit"]))
    return {"traits": sorted(traits.values(), key=lambda item: item["apiName"])}


def item_catalog_filename(set_number: int) -> str:
    """Use the generic active-set catalog filename for Set 18."""
    return "itens.json" if int(set_number) == 18 else f"item_catalog_set{int(set_number)}.json"


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Migra os dados de campeões, traits e itens do TFT Set 18.")
    parser.add_argument("--set", type=int, default=18, help="Número do set (padrão: 18).")
    parser.add_argument("--input", type=Path, help="JSON CommunityDragon local; se omitido, baixa a fonte latest.")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data", help="Diretório de saída.")
    args = parser.parse_args(argv)
    try:
        source = load_source(args.input)
        set_name, entries = select_set(source, args.set)
        units = build_units(entries)
        traits = build_traits(entries, units)
        # Reuse the project's canonical item normalizer so recipes, effects,
        # and schema match the engine's existing ItemCatalog contract.
        from scripts.generate_item_catalog import build_catalog
        items = build_catalog(source, str(args.set))
        out = args.output_dir
        write_json(out / "units_gerado.json", units)
        write_json(out / "traits.json", traits)
        write_json(out / item_catalog_filename(args.set), items)
        manifest = {
            "set": args.set,
            "name": set_name,
            "source": SOURCE_URL if args.input is None else str(args.input),
            "champions": len(units),
            "traits": len(traits["traits"]),
            "craftable_items": len(items["items"]),
            "components": len(items["components"]),
            "note": "Generated from CommunityDragon; item combat effects not represented by the engine remain source metadata, not simulated effects.",
        }
        write_json(out / f"set{args.set}_manifest.json", manifest)
    except (OSError, ValueError, json.JSONDecodeError, TimeoutError) as exc:
        print(f"Falha na migração do set: {exc}", file=sys.stderr)
        return 2
    print(
        f"Set {args.set} ({set_name}): {len(units)} campeões, "
        f"{len(traits['traits'])} traits, {len(items['components'])} componentes, "
        f"{len(items['items'])} itens craftáveis."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
