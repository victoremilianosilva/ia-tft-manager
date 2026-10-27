#!/usr/bin/env python3
"""Generate the engine's normalized item catalog from CommunityDragon TFT JSON.

The source file contains multiple sets and may contain repeated setData entries
for different game modes. Entries with the same set name/number are merged.
Only recipes explicitly listed by the selected set are exported.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

CARRY_EFFECTS = {
    "AD", "AD_NotStatBar", "AS", "AP", "AP_NotStatBar", "CritChance",
    "CritDamageToGive", "BonusDamage", "Damage", "DamageAmp", "StackingAD",
    "StackingSP", "AttackSpeedPerStack", "APPerInterval", "ManaRegen",
    "ManaOnCrit", "FlatManaRestore", "BaseManaOnHit", "CombatStartMana",
    "ADOnAttack", "ASCapstone", "ModifiedADAP", "BacklineADAP",
}
TANK_EFFECTS = {
    "Health", "BonusPercentHP", "PercentMaxHP", "Armor", "MagicResist",
    "MR", "DamageReduction", "AutoDamageReduction", "ShieldSize",
    "ShieldHealthPercent", "PercentHealthShield", "BaseDurability",
    "EmpoweredDurability", "BonusResists", "FrontlineResists",
    "ArmorPerEnemy", "MRPerEnemy", "MissingHealthRestore",
}
SUPPORT_EFFECTS = {
    "AllyHealing", "ShieldBonusAP", "ShieldDuration", "GrievousWoundsPercent",
    "HealingReductionPct", "MRShred", "ArmorReductionPercent",
    "ArmorBreakDuration", "BuffDamageAmp", "ManaPercIncrease", "HealTickRate",
    "MaxHeal", "MissingHealthHeal",
}
UTILITY_EFFECTS = {
    "MaxArmySizeIncrease", "PercentGoldChance", "HexRange", "HexRangeIncrease",
    "MonsterCap", "SizeIncrease", "MaxStacks", "Duration", "Timer",
    "StealthDuration",
}


def _finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _effect_value(effects: dict[str, Any], *keys: str) -> float:
    for key in keys:
        value = effects.get(key)
        if _finite_number(value):
            return float(value)
    return 0.0


def _nonnegative_effect(effects: dict[str, Any], *keys: str) -> float:
    value = _effect_value(effects, *keys)
    return value if value >= 0.0 else 0.0


def _percent_fraction(effects: dict[str, Any], *keys: str) -> float:
    """Normalize percentage points (35) and fractions (0.35) to fractions."""
    value = _nonnegative_effect(effects, *keys)
    return value / 100.0 if value > 1.0 else value


def _conditional_reduction(effects: dict[str, Any]) -> float:
    # Large source values can describe conditional effects, not permanent stats.
    value = _effect_value(effects, "DamageReduction")
    return value if 0.0 <= value <= 1.0 else 0.0


def _role_weights(item_id: str, effects: dict[str, Any]) -> dict[str, float]:
    """Produce explicitly heuristic role weights from non-zero source effects."""
    active = {
        key for key, value in effects.items()
        if _finite_number(value) and float(value) != 0.0
    }
    scores = {
        "carry": float(len(active & CARRY_EFFECTS)),
        "tank": float(len(active & TANK_EFFECTS)),
        "support": float(len(active & SUPPORT_EFFECTS)),
        "utility": float(len(active & UTILITY_EFFECTS)),
    }
    normalized_id = item_id.lower()
    if any(token in normalized_id for token in ("emblem", "tactician", "forceofnature", "thiefsgloves")):
        scores["utility"] += 2.0
    peak = max(scores.values(), default=0.0)
    if peak <= 0.0:
        return {role: 0.0 for role in scores}
    return {role: round(score / peak, 6) for role, score in scores.items()}


def _normalise_combat_effects(effects: dict[str, Any]) -> list[dict[str, Any]]:
    """Translate source effect keys into the combat engine's generic contract.

    This intentionally maps only source semantics the simulator supports.
    Unmodeled passives remain in source_effects for diagnostics rather than
    being guessed or silently treated as permanent stats.
    """
    generated: list[dict[str, Any]] = []
    ad = _percent_fraction(effects, "AD", "BonusAD")
    if ad > 0.0:
        generated.append({
            "trigger": "combat_start",
            "operation": "add_stat",
            "stat": "attack_damage",
            "target": "self",
            "value": ad,
            "percent_of_stat": True,
        })
    mana_regen = _nonnegative_effect(effects, "ManaRegen")
    if mana_regen > 0.0:
        generated.append({
            "trigger": "combat_start",
            "operation": "mana_regen",
            "value": mana_regen,
        })
    return generated


def _normalise_stats(effects: dict[str, Any]) -> dict[str, float]:
    # Source AD is a percentage of base attack damage. The engine contract
    # expects flat attack_damage, so AD is preserved raw but not converted.
    return {
        "attack_damage": 0.0,
        "attack_speed": _percent_fraction(effects, "AS", "AttackSpeed"),
        "ability_power": _nonnegative_effect(effects, "AP", "AbilityPower"),
        "critical_strike_chance": _percent_fraction(effects, "CritChance", "CriticalStrikeChance"),
        "critical_strike_damage": _percent_fraction(effects, "CritDamage", "CriticalStrikeDamage"),
        "health": _nonnegative_effect(effects, "Health", "HP", "BonusHealth"),
        "armor": _nonnegative_effect(effects, "Armor"),
        "magic_resist": _nonnegative_effect(effects, "MagicResist", "MR"),
        "mana": _nonnegative_effect(effects, "Mana"),
        "omnivamp": _percent_fraction(effects, "StatOmnivamp", "Omnivamp"),
        "damage_amplification": _percent_fraction(effects, "DamageAmp", "DamageAmplification"),
        "damage_reduction": _conditional_reduction(effects),
    }


def _is_consumable(item: dict[str, Any]) -> bool:
    """Return whether CommunityDragon marks this item as a consumable."""
    tags = item.get("tags")
    if not isinstance(tags, list):
        return False
    return any(isinstance(tag, str) and tag.strip().casefold() == "consumable" for tag in tags)

def _has_tag(item: dict[str, Any], expected_tag: str) -> bool:
    """Match a CommunityDragon tag without depending on casing or whitespace."""
    tags = item.get("tags")
    if not isinstance(tags, list):
        return False
    expected = expected_tag.strip().casefold()
    return any(
        isinstance(tag, str) and tag.strip().casefold() == expected
        for tag in tags
    )


def _is_component(item: dict[str, Any] | None) -> bool:
    """Only source items explicitly tagged 'component' are base components."""
    return item is not None and _has_tag(item, "component")


def default_catalog_output_path(set_selector: str) -> Path:
    """Use the generic active-set catalog name for Set 18."""
    slug = re.sub(r"[^a-z0-9]+", "_", str(set_selector).strip().lower()).strip("_")
    if slug in {"18", "set18"}:
        return Path("data") / "itens.json"
    return Path("data") / f"item_catalog_{slug}.json"


def item_effects_candidates(set_selector: str) -> list[Path]:
    """Resolve set-specific overrides, using the generic file for Set 18."""
    slug = re.sub(r"[^a-z0-9]+", "_", str(set_selector).strip().lower()).strip("_")
    if slug in {"18", "set18"}:
        return [Path("data") / "item_effects.json"]
    candidates = [Path("data") / f"item_effects_{slug}.json"]
    if slug.isdigit():
        candidates.append(Path("data") / f"item_effects_set{slug}.json")
    return candidates


def _selector_matches(selector: str, entry: dict[str, Any]) -> bool:
    name = str(entry.get("name", "")).strip()
    number = entry.get("number")
    lowered = selector.strip().lower()
    return (
        name.lower() == lowered
        or (number is not None and str(number).lower() == lowered)
        or (number is not None and f"set{number}".lower() == lowered)
    )


def build_catalog(
    source: dict[str, Any],
    set_selector: str,
    trait_item_metadata: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    if not isinstance(source, dict):
        raise ValueError("O JSON de origem precisa ser um objeto.")
    if not isinstance(source.get("items"), list) or not isinstance(source.get("setData"), list):
        raise ValueError("O arquivo não parece ser um CommunityDragon TFT JSON: esperava 'items' e 'setData'.")

    matching = [entry for entry in source["setData"] if isinstance(entry, dict) and _selector_matches(set_selector, entry)]
    if not matching:
        available = sorted({
            f"{entry.get('number')} ({entry.get('name')})"
            for entry in source["setData"] if isinstance(entry, dict)
        })
        raise ValueError(f"Set '{set_selector}' não encontrado. Sets disponíveis: {', '.join(available)}")

    identities = {(str(entry.get("number")), str(entry.get("name"))) for entry in matching}
    if len(identities) > 1:
        choices = ", ".join(f"{number} ({name})" for number, name in sorted(identities))
        raise ValueError(f"Seletor ambíguo '{set_selector}'. Especifique o nome do set: {choices}")

    set_number, set_name = next(iter(identities))
    selected_entries = [
        entry for entry in source["setData"]
        if isinstance(entry, dict)
        and (str(entry.get("number")), str(entry.get("name"))) == (set_number, set_name)
    ]
    set_item_ids = {
        item_id for entry in selected_entries for item_id in (entry.get("items") or [])
        if isinstance(item_id, str) and item_id
    }

    item_by_id: dict[str, dict[str, Any]] = {}
    for item in source["items"]:
        if not isinstance(item, dict):
            continue
        api_name = item.get("apiName")
        if isinstance(api_name, str) and api_name:
            if api_name in item_by_id:
                raise ValueError(f"ID apiName duplicado na origem: {api_name}")
            item_by_id[api_name] = item

    selected_records = [
        item_by_id[item_id]
        for item_id in sorted(set_item_ids)
        if item_id in item_by_id and not _is_consumable(item_by_id[item_id])
    ]
    craftable: list[dict[str, Any]] = []
    for item in selected_records:
        item_id = str(item.get("apiName") or "")
        # This engine catalog intentionally uses the DA_ item family only.
        # TFT_Item_* records are aliases/parallel records and must not create
        # duplicate component dimensions or recipes in the action space.
        if not item_id.startswith("DA_"):
            continue
        recipe = item.get("composition")
        if item.get("isAugment") is True or not isinstance(recipe, list) or len(recipe) != 2:
            continue
        if not all(isinstance(component_id, str) and component_id for component_id in recipe):
            raise ValueError(f"Receita inválida em {item_id or '<sem ID>'}: {recipe!r}")
        # A completed DA_ item is craftable only when both ingredients are
        # actual DA_Component_* records tagged as components.
        if any(
            not component_id.startswith("DA_Component_")
            or not _is_component(item_by_id.get(component_id))
            for component_id in recipe
        ):
            continue
        craftable.append(item)
    if not craftable:
        raise ValueError(f"Nenhum item DA_ com receita de dois componentes DA_Component_* encontrado no set {set_name}.")

    component_ids = sorted({
        component_id
        for item in craftable
        for component_id in item["composition"]
    })

    if len(component_ids) > 10:
        raise ValueError(f"O set {set_name} usa {len(component_ids)} componentes; a cabeça de ações da engine aceita no máximo 10.")

    components = []
    for component_id in component_ids:
        component = item_by_id.get(component_id)
        if component is None:
            raise ValueError(f"Componente referenciado por uma receita, mas ausente na origem: {component_id}")
        components.append({
            "id": component_id,
            "name": str(component.get("name") or component_id),
            "source_api_name": component_id,
            "source_effects": component.get("effects") or {},
        })

    recipes: dict[tuple[str, str], str] = {}
    output_items = []
    for source_item in sorted(craftable, key=lambda item: str(item.get("apiName", ""))):
        item_id = str(source_item.get("apiName") or "")
        name = str(source_item.get("name") or "")
        recipe = list(source_item["composition"])
        if not item_id or not name:
            raise ValueError(f"Item sem apiName ou name: {source_item!r}")
        recipe_key = tuple(sorted(recipe))
        if recipe_key in recipes:
            raise ValueError(
                "A engine schema_version=1 não aceita receitas duplicadas: "
                f"{recipes[recipe_key]} e {item_id} usam {recipe_key}."
            )
        recipes[recipe_key] = item_id
        effects = source_item.get("effects")
        if not isinstance(effects, dict):
            effects = {}
        output_item = {
            "id": item_id,
            "name": name,
            "recipe_components": recipe,
            "stats": _normalise_stats(effects),
            "weights": _role_weights(item_id, effects),
            "source_api_name": item_id,
            "source_description": source_item.get("desc") or "",
            "source_icon": source_item.get("icon") or "",
            "source_effects": effects,
            "combat_effects": _normalise_combat_effects(effects),
            "weight_basis": "heuristic_from_CommunityDragon_effect_keys",
        }
        # Special/trait mechanics are set data, not API-name branches in C++.
        metadata = (trait_item_metadata or {}).get(item_id)
        if metadata:
            # Only allow combat metadata fields; never let an override replace
            # source identity, recipe, stats, or provenance.
            for key in ("grants_trait", "granted_trait_active_count", "combat_effects", "deferred_stats"):
                if key in metadata:
                    if key == "combat_effects":
                        # Preserve source-derived generic effects alongside
                        # explicitly modeled set mechanics.
                        output_item[key] = output_item["combat_effects"] + metadata[key]
                    else:
                        output_item[key] = metadata[key]
        output_items.append(output_item)

    return {
        "schema_version": 1,
        "set_id": set_name,
        "source": "CommunityDragon",
        "source_file_format": "cdragon/tft JSON",
        "source_set_number": int(set_number) if set_number.isdigit() else set_number,
        "source_set_name": set_name,
        "source_set_entries_merged": len(selected_entries),
        "components": components,
        "items": output_items,
        "normalization_notes": [
            "Percentual values used by supported numeric fields are normalized to fractions where source semantics are clear.",
            "Source AD is a percentage of base attack damage and is preserved in source_effects; it is not converted to flat attack_damage.",
            "Conditional/passive effects are preserved in source_effects and are not guessed as permanent combat stats.",
            "Role weights are heuristics inferred from effect keys, not official Riot role labels.",
            "The catalog does not implement effects in CombatEngine; each effect must be supported separately.",
        ],
    }


def validate_catalog_semantics(catalog: dict[str, Any]) -> None:
    """Reject structurally valid catalogs that would make finished items inert.

    Emblems are excluded from the numeric/effect coverage denominator because
    their value is the granted trait. Raw source_effects alone do not count as
    implemented effects: the combat simulator must receive normalized stats or
    an explicit combat_effects operation.
    """
    items = catalog.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError("Catálogo sem itens craftáveis.")

    ordinary = [
        item for item in items
        if isinstance(item, dict) and not item.get("grants_trait")
    ]
    if not ordinary:
        raise ValueError("Catálogo não contém itens craftáveis comuns para validar.")

    stat_keys = (
        "attack_damage", "attack_speed", "ability_power",
        "critical_strike_chance", "critical_strike_damage", "health",
        "armor", "magic_resist", "mana", "omnivamp",
        "damage_amplification", "damage_reduction",
    )

    def has_applied_value(item: dict[str, Any]) -> bool:
        stats = item.get("stats") if isinstance(item.get("stats"), dict) else {}
        has_stats = any(
            _finite_number(stats.get(key)) and float(stats[key]) != 0.0
            for key in stat_keys
        )
        effects = item.get("combat_effects")
        has_effects = isinstance(effects, list) and bool(effects)
        return has_stats or has_effects

    usable = sum(1 for item in ordinary if has_applied_value(item))
    minimum = max(1, math.ceil(len(ordinary) * 0.5))
    if usable < minimum:
        raise ValueError(
            "Catálogo aparentemente válido, mas sem efeitos de combate aplicáveis: "
            f"{usable}/{len(ordinary)} itens comuns têm atributos/effects suportados; "
            f"mínimo esperado={minimum}. Verifique a normalização da fonte."
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Gera um catálogo JSON de itens craftáveis de um set a partir de itens.json (CommunityDragon)."
    )
    parser.add_argument("--set", dest="set_selector", required=True, help="Número ou nome do set, por exemplo: 16 ou Set16.")
    parser.add_argument("--input", default="itens.json", help="JSON original do CommunityDragon (padrão: itens.json).")
    parser.add_argument("--output", help="Arquivo de saída. Set 18 usa data/itens.json por padrão; outros sets usam data/item_catalog_<set>.json.")
    args = parser.parse_args(argv)
    source_path = Path(args.input)
    if not source_path.is_file():
        parser.error(f"Arquivo de entrada não encontrado: {source_path}")
    try:
        with source_path.open("r", encoding="utf-8") as handle:
            source = json.load(handle)
        set_slug = re.sub(r"[^a-z0-9]+", "_", args.set_selector.lower()).strip("_")
        metadata_candidates = item_effects_candidates(args.set_selector)
        trait_item_metadata: dict[str, dict[str, Any]] = {}
        metadata_path = next((path for path in metadata_candidates if path.is_file()), None)
        if metadata_path is not None:
            with metadata_path.open("r", encoding="utf-8") as handle:
                metadata_document = json.load(handle)
            raw_metadata = metadata_document.get("items", {})
            if isinstance(raw_metadata, dict):
                trait_item_metadata = {
                    str(item_id): metadata for item_id, metadata in raw_metadata.items()
                    if isinstance(item_id, str) and isinstance(metadata, dict)
                }
        catalog = build_catalog(source, args.set_selector, trait_item_metadata)
        validate_catalog_semantics(catalog)
        output_path = Path(args.output) if args.output else default_catalog_output_path(args.set_selector)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(catalog, handle, ensure_ascii=False, indent=2, allow_nan=False)
            handle.write("\n")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Erro ao gerar catálogo: {exc}", file=sys.stderr)
        return 2
    print(
        f"Catálogo gerado: {output_path} | set={catalog['set_id']} "
        f"| componentes={len(catalog['components'])} | itens craftáveis={len(catalog['items'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
