"""Extrai as traits do último set disponível para um catálogo separado.

Uso:
    python tests/diagnostico/_trait_data.py

O JSON de origem nunca é alterado. O script aceita formatos comuns:
- {"traits": [...]}
- {"sets": {"17": {"traits": [...]}}}
- {"setData": [{"number": 17, "traits": [...]}]}
- listas/objetos aninhados com traits identificáveis por apiName TFT<N>_...
"""

import json
import re
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TESTS_DIR.parent

SOURCE_FILE = TESTS_DIR / "traits.json"
OUTPUT_FILE = PROJECT_ROOT / "traits_gerado.json"
REPORT_FILE = PROJECT_ROOT / "relatorio_traits_gerado.txt"

# None detecta automaticamente o maior número de set presente na fonte.
SET_DESEJADO = None


def load_json(path):
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    with path.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def set_number_from_api_name(value):
    if not isinstance(value, str):
        return None
    match = re.match(r"^TFT(\d+)_", value, re.IGNORECASE)
    return match.group(1) if match else None


def find_trait_lists(data):
    """Retorna listas de traits encontradas em estruturas conhecidas/aninhadas."""
    found = []

    def walk(value, path="$"):
        if isinstance(value, dict):
            traits = value.get("traits")
            if isinstance(traits, list) and traits and all(
                isinstance(item, dict) for item in traits
            ):
                found.append((path + ".traits", traits))

            # Alguns dumps armazenam traits em "champions" ou "units", mas
            # não os tratamos como catálogo de traits: percorremos só estruturas.
            for key, child in value.items():
                if isinstance(child, (dict, list)):
                    walk(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                if isinstance(child, (dict, list)):
                    walk(child, f"{path}[{index}]")

    walk(data)
    # Elimina duplicatas da mesma lista encontrada por caminhos repetidos.
    unique = []
    seen_ids = set()
    for path, traits in found:
        identity = id(traits)
        if identity not in seen_ids:
            seen_ids.add(identity)
            unique.append((path, traits))
    return unique


def collect_traits(data):
    """Seleciona uma lista de traits e determina o set mais recente."""
    candidates = find_trait_lists(data)
    if not candidates:
        raise ValueError(
            "Nenhuma lista de traits foi encontrada. Esperava uma lista "
            "em 'traits', 'sets' ou 'setData'."
        )

    # Cada lista recebe um set inferido pelos apiName. Listas sem IDs de set
    # ficam como fallback, mas não podem vencer uma lista com set identificado.
    ranked = []
    for path, traits in candidates:
        numbers = [
            int(number)
            for trait in traits
            if (number := set_number_from_api_name(trait.get("apiName"))) is not None
        ]
        set_number = max(numbers) if numbers else None
        ranked.append((set_number, path, traits))

    if SET_DESEJADO is not None:
        desired = int(SET_DESEJADO)
        matching = [
            (path, traits)
            for set_number, path, traits in ranked
            if set_number == desired
            and any(
                set_number_from_api_name(t.get("apiName")) == str(desired)
                for t in traits
            )
        ]
        if not matching:
            raise ValueError(f"Set {desired} não encontrado no catálogo de traits.")
        # Prefere a lista com mais registros entre as candidatas do set pedido.
        return str(desired), max(matching, key=lambda item: len(item[1]))

    identified = [item for item in ranked if item[0] is not None]
    if not identified:
        raise ValueError(
            "Não foi possível detectar o número do set: os apiName das traits "
            "não seguem o padrão TFT<N>_..."
        )

    latest_set = max(item[0] for item in identified)
    matching = [
        (path, traits)
        for set_number, path, traits in identified
        if set_number == latest_set
        and any(
            set_number_from_api_name(t.get("apiName")) == str(latest_set)
            for t in traits
        )
    ]
    return str(latest_set), max(matching, key=lambda item: len(item[1]))


def validate_traits(traits, selected_set):
    errors = []
    warnings = []
    seen = set()

    for index, trait in enumerate(traits):
        label = trait.get("name") or trait.get("apiName") or f"índice {index}"
        api_name = trait.get("apiName")

        if not isinstance(api_name, str) or not api_name.strip():
            errors.append(f"{label}: apiName ausente ou inválido")
        else:
            if api_name in seen:
                errors.append(f"{label}: apiName duplicado ({api_name})")
            seen.add(api_name)

            trait_set = set_number_from_api_name(api_name)
            if trait_set is not None and trait_set != selected_set:
                warnings.append(
                    f"{label}: apiName pertence ao set {trait_set}, "
                    f"não ao set selecionado {selected_set}"
                )

        if not isinstance(trait.get("name"), str) or not trait["name"].strip():
            warnings.append(f"{label}: nome legível ausente")

        effects = trait.get("effects")
        if effects is not None and not isinstance(effects, list):
            errors.append(f"{label}: 'effects' deve ser uma lista")

        units = trait.get("units")
        if units is not None:
            if not isinstance(units, list):
                errors.append(f"{label}: 'units' deve ser uma lista")
            else:
                for unit_index, unit in enumerate(units):
                    if not isinstance(unit, dict):
                        errors.append(
                            f"{label}: units[{unit_index}] não é um objeto"
                        )
                    elif not isinstance(unit.get("unit"), str):
                        warnings.append(
                            f"{label}: units[{unit_index}] não tem campo 'unit' textual"
                        )

        if not any(key in trait for key in ("effects", "desc", "units")):
            warnings.append(
                f"{label}: sem 'effects', 'desc' ou 'units'; confira a estrutura da fonte"
            )

    if errors:
        preview = "\n".join(f"  - {error}" for error in errors[:30])
        suffix = (
            f"\n  ... e mais {len(errors) - 30} erro(s)"
            if len(errors) > 30 else ""
        )
        raise ValueError(
            f"Validação das traits falhou com {len(errors)} erro(s):\n"
            f"{preview}{suffix}"
        )

    return warnings


def main():
    print(f"Lendo arquivo: {SOURCE_FILE}")
    data = load_json(SOURCE_FILE)
    selected_set, (source_path, traits) = collect_traits(data)
    warnings = validate_traits(traits, selected_set)

    # Preserva os campos originais de cada trait, sem reescrever descrições,
    # efeitos, variáveis, ícones ou vínculos com unidades.
    generated = [dict(trait) for trait in traits]

    api_names = [trait["apiName"] for trait in generated]
    if not generated:
        raise RuntimeError("Nenhuma trait foi gerada.")
    if len(api_names) != len(set(api_names)):
        raise RuntimeError("Existem apiName duplicados; arquivo não foi salvo.")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(generated, file, ensure_ascii=False, indent=2)

    report = [
        f"Relatório de geração — Traits do set {selected_set}",
        "=" * 70,
        f"Fonte: {SOURCE_FILE}",
        f"Caminho da lista selecionada: {source_path}",
        f"Traits geradas: {len(generated)}",
        f"apiName únicos: {len(set(api_names))}",
        f"Traits com effects: {sum(isinstance(t.get('effects'), list) for t in generated)}",
        f"Traits com units: {sum(isinstance(t.get('units'), list) for t in generated)}",
        f"Traits com desc: {sum(isinstance(t.get('desc'), str) for t in generated)}",
        "",
        "Avisos:",
    ]
    report.extend(f"- {warning}" for warning in warnings)
    if not warnings:
        report.append("- Nenhum")
    report.extend([
        "",
        "Observações:",
        "- O maior número de set identificado nos apiName foi selecionado automaticamente.",
        "- Os registros originais das traits foram preservados.",
        "- O arquivo de origem não foi modificado.",
    ])
    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")

    print("\n========== GERAÇÃO CONCLUÍDA ==========")
    print(f"Set selecionado: {selected_set}")
    print(f"Lista selecionada: {source_path}")
    print(f"Traits geradas: {len(generated)}")
    print(f"Avisos de validação: {len(warnings)}")
    print(f"JSON gerado: {OUTPUT_FILE}")
    print(f"Relatório: {REPORT_FILE}")
    print("O arquivo de origem permanece intacto.")


if __name__ == "__main__":
    main()
