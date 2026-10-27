#!/usr/bin/env python3
"""Fetch OP.GG TFT meta decks and maintain a normalized local JSON snapshot.

The MCP is contacted only by this preparation script, never by the C++ engine.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import sys
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mcp import ClientSession
import mcp.client.session as mcp_client_session

try:
    from mcp.client.streamable_http import streamable_http_client
except ImportError:  # MCP SDK 1.x compatibility
    from mcp.client.streamable_http import streamablehttp_client as streamable_http_client

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "data" / "opgg_tft_meta.json"
DEFAULT_RAW = ROOT / "data" / "opgg_tft_meta_raw.json"
DEFAULT_URL = "https://mcp-api.op.gg/mcp"
TOOL_NAME = "tft_list_meta_decks"


def _field(obj: Any, *names: str, default: Any = None) -> Any:
    for name in names:
        if isinstance(obj, dict) and name in obj:
            return obj[name]
        if hasattr(obj, name):
            return getattr(obj, name)
    return default


def _install_schema_compatibility() -> None:
    """Work around OP.GG's non-object outputSchema metadata in MCP SDK validation."""
    methods = getattr(mcp_client_session, "_methods", None)
    original = getattr(methods, "validate_server_result", None)
    if methods is None or original is None or getattr(original, "_opgg_compat_wrapper", False):
        return

    def validate_with_compat(method: Any, version: Any, raw: Any, *args: Any, **kwargs: Any) -> Any:
        if "tools/list" in str(method).lower() and isinstance(raw, dict):
            tools = raw.get("tools")
            if isinstance(tools, list):
                cleaned = []
                changed = False
                for entry in tools:
                    if not isinstance(entry, dict):
                        cleaned.append(entry)
                        continue
                    item = dict(entry)
                    for key in ("outputSchema", "output_schema"):
                        schema = item.get(key)
                        if isinstance(schema, dict) and schema.get("type") != "object":
                            item.pop(key, None)
                            changed = True
                    cleaned.append(item)
                if changed:
                    raw = dict(raw)
                    raw["tools"] = cleaned
        return original(method, version, raw, *args, **kwargs)

    validate_with_compat._opgg_compat_wrapper = True  # type: ignore[attr-defined]
    methods.validate_server_result = validate_with_compat


async def fetch_meta(url: str) -> dict[str, Any]:
    _install_schema_compatibility()
    async with streamable_http_client(url) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
            tools_result = await session.list_tools()
            tools = _field(tools_result, "tools", default=[]) or []
            tool = next((t for t in tools if _field(t, "name") == TOOL_NAME), None)
            if tool is None:
                names = ", ".join(str(_field(t, "name", default="?")) for t in tools)
                raise RuntimeError(f"{TOOL_NAME} não encontrado. Ferramentas disponíveis: {names}")
            schema = _field(tool, "input_schema", "inputSchema", default={}) or {}
            required = schema.get("required", [])
            if required:
                raise RuntimeError(
                    f"{TOOL_NAME} exige argumentos {required}; verifique o schema antes de coletar."
                )
            result = await session.call_tool(TOOL_NAME, arguments={})
            if _field(result, "is_error", "isError", default=False):
                raise RuntimeError("O MCP retornou erro ao consultar tft_list_meta_decks.")
            structured = _field(result, "structured_content", "structuredContent")
            if structured is not None:
                if isinstance(structured, dict):
                    return structured
                if isinstance(structured, list):
                    return {"result": structured}
            text_parts = []
            for item in _field(result, "content", default=[]) or []:
                item_text = _field(item, "text")
                if item_text:
                    text_parts.append(item_text)
            for item_text in text_parts:
                try:
                    parsed = json.loads(item_text)
                    if isinstance(parsed, dict):
                        return parsed
                    if isinstance(parsed, list):
                        return {"result": parsed}
                except json.JSONDecodeError:
                    continue
            raise RuntimeError("A resposta do MCP não continha JSON estruturado reconhecível.")


def _list(value: Any) -> list:
    return value if isinstance(value, list) else []


def _number(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
        return number if number == number and abs(number) != float("inf") else default
    except (TypeError, ValueError):
        return default


def _normalize_unit(unit: Any) -> dict[str, Any] | None:
    if not isinstance(unit, dict):
        return None
    key = str(unit.get("key") or unit.get("characterId") or unit.get("character_id") or unit.get("apiName") or unit.get("api_name") or unit.get("name") or "").strip()
    if not key:
        return None
    cell = unit.get("cell") if isinstance(unit.get("cell"), dict) else {}
    return {
        "key": key,
        "items": [str(x) for x in _list(unit.get("items"))],
        "tier": int(_number(unit.get("tier"), 0)),
        "cell": {"x": int(_number(cell.get("x"), -1)), "y": int(_number(cell.get("y"), -1))},
        "is_core": bool(unit.get("isCore", unit.get("is_core", False))),
        "priority": int(_number(unit.get("priority"), 0)),
    }


def _normalize_snapshot(snapshot: Any) -> dict[str, Any] | None:
    if not isinstance(snapshot, dict):
        return None
    units = [normalized for unit in _list(snapshot.get("units"))
             if (normalized := _normalize_unit(unit)) is not None]
    traits = []
    for trait in _list(snapshot.get("traits")):
        if isinstance(trait, dict):
            traits.append({
                "key": str(trait.get("key") or trait.get("name") or ""),
                "style": trait.get("style"),
                "num_units": int(_number(trait.get("numUnits", trait.get("num_units")), 0)),
            })
    return {
        "level": int(_number(snapshot.get("level"), 0)),
        "units": units,
        "traits": traits,
        "play": _number(snapshot.get("play")),
        "win": _number(snapshot.get("win")),
        "lose": _number(snapshot.get("lose")),
    }


def _normalize_stats(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {}
    result = {}
    for key in ("totalCount", "compsCount", "avgPlacement", "winCount", "top4Count",
                "winRate", "top4Rate", "pickRate"):
        if key in value:
            result[key] = _number(value[key]) if key not in ("totalCount", "compsCount", "winCount", "top4Count") else int(_number(value[key]))
    return result


def normalize_payload(raw: dict[str, Any]) -> dict[str, Any]:
    data = raw.get("data")
    if isinstance(data, dict):
        data = data.get("decks", data.get("compositions", data.get("items")))
    if not isinstance(data, list):
        data = raw.get("compositions", raw.get("decks", raw.get("result")))
    if not isinstance(data, list):
        raise ValueError("Resposta do MCP sem lista de composições em data/decks/compositions.")
    metadata = raw.get("metadata") if isinstance(raw.get("metadata"), dict) else {}
    compositions = []
    for entry in data:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if isinstance(name, dict):
            name = name.get("pt_BR") or name.get("en_US") or next(iter(name.values()), "")
        units = [normalized for unit in _list(entry.get("units"))
                 if (normalized := _normalize_unit(unit)) is not None]
        stats = entry.get("stat") if isinstance(entry.get("stat"), dict) else {}
        compositions.append({
            "id": str(entry.get("id") or ""),
            "name": str(name or entry.get("id") or "Unnamed composition"),
            "cost": int(_number(entry.get("cost"), 0)),
            "team_code": str(entry.get("teamCode") or entry.get("team_code") or ""),
            "units": units,
            "traits": [{
                "key": str(t.get("key") or ""),
                "style": t.get("style"),
                "num_units": int(_number(t.get("numUnits", t.get("num_units")), 0)),
            } for t in _list(entry.get("traits")) if isinstance(t, dict)],
            "badge": entry.get("badge"),
            "statistics": {
                "deck": _normalize_stats(stats.get("deck")),
                "label": _normalize_stats(stats.get("label")),
            },
            "early_game": _normalize_snapshot(entry.get("early")),
            "mid_game": _normalize_snapshot(entry.get("middle")),
        })
    if not compositions:
        raise ValueError("A resposta do MCP não produziu nenhuma composição válida.")
    return {
        "schema_version": 1,
        "source": "op.gg",
        "tool": TOOL_NAME,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "metadata": metadata,
        "compositions": compositions,
    }


def _is_fresh(path: Path, max_age_hours: float) -> bool:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        stamp = datetime.fromisoformat(str(payload["fetched_at"]).replace("Z", "+00:00"))
        age = (datetime.now(timezone.utc) - stamp).total_seconds()
        return 0 <= age < max_age_hours * 3600 and bool(payload.get("compositions"))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        return False


def _atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                     delete=False, suffix=".tmp") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temp_path = Path(handle.name)
    os.replace(temp_path, path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--raw-output", type=Path, default=DEFAULT_RAW)
    parser.add_argument("--if-stale", action="store_true", help="Reuse a recent valid catalog without a network call.")
    parser.add_argument("--max-age-hours", type=float, default=12.0)
    parser.add_argument("--offline", action="store_true", help="Never call the MCP; require an existing valid catalog.")
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    if args.max_age_hours < 0:
        print("--max-age-hours deve ser >= 0.", file=sys.stderr)
        return 2
    if args.if_stale and _is_fresh(args.output, args.max_age_hours):
        print(f"Catálogo OP.GG ainda válido; reutilizando {args.output}")
        return 0
    if args.offline:
        if args.output.is_file() and _is_fresh(args.output, 1e12):
            print(f"Modo offline: usando catálogo existente {args.output}")
            return 0
        print(f"Modo offline sem catálogo válido em {args.output}", file=sys.stderr)
        return 1
    try:
        raw = await fetch_meta(args.url)
        normalized = normalize_payload(raw)
        # Save raw and normalized data only after the response passed validation.
        _atomic_json(args.raw_output, raw)
        _atomic_json(args.output, normalized)
        digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
        print(f"Catálogo OP.GG atualizado: {len(normalized['compositions'])} comps | SHA-256 {digest[:16]} | {args.output}")
        return 0
    except Exception as exc:
        print(f"Falha ao atualizar catálogo OP.GG: {exc!r}", file=sys.stderr)
        print("Detalhes da exceção (incluindo subexceções de TaskGroup):", file=sys.stderr)
        traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr, chain=True)
        if args.output.is_file():
            try:
                existing = json.loads(args.output.read_text(encoding="utf-8"))
                if existing.get("schema_version") == 1 and existing.get("compositions"):
                    print("Usando último catálogo válido; nenhum arquivo anterior foi substituído.", file=sys.stderr)
                    return 0
            except (OSError, ValueError, json.JSONDecodeError):
                pass
        return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
