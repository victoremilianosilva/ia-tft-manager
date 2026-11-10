#!/usr/bin/env python3
"""Inspect and call the OP.GG TFT MCP server.

Install:
    python -m pip install mcp

List available tools and their input schemas:
    python scripts/test_opgg_mcp.py

Call a tool with no required arguments:
    python scripts/test_opgg_mcp.py --call tft_list_meta_decks

Call a tool with arguments discovered from its schema:
    python scripts/test_opgg_mcp.py --call TOOL_NAME --arguments '{"key": "value"}'

This is a diagnostic script. It does not modify the TFT engine or save data.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import traceback
from typing import Any

from mcp import ClientSession
import mcp.client.session as mcp_client_session

try:
    from mcp.client.streamable_http import streamable_http_client as streamablehttp_client
except ImportError:  # pragma: no cover - exercised only with MCP SDK 1.x
    from mcp.client.streamable_http import streamablehttp_client

DEFAULT_URL = "https://mcp-api.op.gg/mcp"


def field(obj: Any, *names: str, default: Any = None) -> Any:
    """Read a model field across MCP SDK camelCase/snake_case versions."""
    for name in names:
        if isinstance(obj, dict) and name in obj:
            return obj[name]
        if hasattr(obj, name):
            return getattr(obj, name)
    return default


def install_opgg_schema_compatibility() -> bool:
    """Ignore only incompatible outputSchema metadata in OP.GG tools/list locally."""
    methods = getattr(mcp_client_session, "_methods", None)
    original = getattr(methods, "validate_server_result", None)
    if methods is None or original is None:
        return False
    if getattr(original, "_opgg_compat_wrapper", False):
        return True

    def validate_with_opgg_compat(method: Any, version: Any, raw: Any, *args: Any, **kwargs: Any) -> Any:
        # The SDK passes decoded JSON here. Remove only non-object output schemas,
        # which this script does not need; leave tool names and input schemas intact.
        method_text = str(method).lower()
        if "tools/list" in method_text and isinstance(raw, dict):
            tools = raw.get("tools")
            if isinstance(tools, list):
                cleaned_tools = []
                changed = False
                for entry in tools:
                    if not isinstance(entry, dict):
                        cleaned_tools.append(entry)
                        continue
                    item = dict(entry)
                    for key in ("outputSchema", "output_schema"):
                        schema = item.get(key)
                        if isinstance(schema, dict) and schema.get("type") != "object":
                            item.pop(key, None)
                            changed = True
                    cleaned_tools.append(item)
                if changed:
                    raw = dict(raw)
                    raw["tools"] = cleaned_tools
                    print(
                        "Compatibility note: ignored incompatible OP.GG output-schema "
                        "metadata locally; tool input schemas were preserved.",
                        file=sys.stderr,
                    )
        return original(method, version, raw, *args, **kwargs)

    validate_with_opgg_compat._opgg_compat_wrapper = True  # type: ignore[attr-defined]
    methods.validate_server_result = validate_with_opgg_compat
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL, help=f"MCP endpoint (default: {DEFAULT_URL})")
    parser.add_argument("--call", dest="tool_name", help="Call a tool by name; omit to list tools.")
    parser.add_argument("--arguments", help="Tool arguments as a JSON object.")
    return parser.parse_args()


def required_arguments(schema: dict[str, Any]) -> list[str]:
    required = schema.get("required", [])
    return [name for name in required if isinstance(name, str)]


def print_nested_exception(exc: BaseException, indent: int = 0) -> None:
    prefix = " " * indent
    nested_exceptions = getattr(exc, "exceptions", None)
    if nested_exceptions is not None:
        print(f"{prefix}{type(exc).__name__}: {exc}", file=sys.stderr)
        for nested in nested_exceptions:
            print_nested_exception(nested, indent + 2)
        return
    print(f"{prefix}{type(exc).__name__}: {exc}", file=sys.stderr)
    if exc.__traceback__ is not None:
        traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr)


async def run() -> int:
    args = parse_args()
    if args.arguments is None:
        tool_arguments: dict[str, Any] = {}
    else:
        try:
            parsed = json.loads(args.arguments)
        except json.JSONDecodeError as exc:
            print(f"Invalid JSON for --arguments: {exc}", file=sys.stderr)
            return 2
        if not isinstance(parsed, dict):
            print("--arguments must be a JSON object.", file=sys.stderr)
            return 2
        tool_arguments = parsed

    if not install_opgg_schema_compatibility():
        print("Warning: MCP SDK validator compatibility hook unavailable.", file=sys.stderr)

    stage = "opening HTTP transport"
    try:
        async with streamablehttp_client(args.url) as streams:
            read_stream, write_stream = streams[0], streams[1]
            stage = "initializing MCP session"
            async with ClientSession(read_stream, write_stream) as session:
                init_result = await session.initialize()
                print(f"Connected to MCP server: {args.url}")
                info = field(init_result, "serverInfo", "server_info")
                if info:
                    print(f"Server: {field(info, 'name', default='unknown')} {field(info, 'version', default='')}")

                stage = "requesting tools/list"
                tools_result = await session.list_tools()
                tools = field(tools_result, "tools", default=[])
                if not args.tool_name:
                    print(f"\nAvailable tools ({len(tools)}):")
                    for tool in tools:
                        print(f"\n- {field(tool, 'name', default='(unnamed)')}")
                        description = field(tool, "description")
                        if description:
                            print(f"  Description: {description}")
                        schema = field(tool, "input_schema", "inputSchema", default={}) or {}
                        print("  Input schema: " + json.dumps(schema, ensure_ascii=False))
                    return 0

                tool = next((item for item in tools if field(item, "name") == args.tool_name), None)
                if tool is None:
                    available = ", ".join(str(field(item, "name", default="?")) for item in tools)
                    print(f"Tool not found: {args.tool_name}\nAvailable tools: {available}", file=sys.stderr)
                    return 2

                schema = field(tool, "input_schema", "inputSchema", default={}) or {}
                missing = [name for name in required_arguments(schema) if name not in tool_arguments]
                if missing:
                    print(f"Tool: {field(tool, 'name')}")
                    print(f"Required arguments missing: {', '.join(missing)}")
                    print("Input schema: " + json.dumps(schema, ensure_ascii=False, indent=2))
                    print("\nRerun with --arguments and provide the required fields.")
                    return 2

                print(f"\nCalling {field(tool, 'name')} with:")
                print(json.dumps(tool_arguments, ensure_ascii=False, indent=2))
                stage = f"calling tool {field(tool, 'name')}"
                result = await session.call_tool(field(tool, "name"), arguments=tool_arguments)
                print("\nTool result:")
                for item in field(result, "content", default=[]) or []:
                    item_text = field(item, "text")
                    print(item_text if item_text is not None else repr(item))
                structured = field(result, "structured_content", "structuredContent")
                if structured is not None:
                    print("\nStructured content:\n" + json.dumps(structured, ensure_ascii=False, indent=2, default=str))
                if field(result, "is_error", "isError", default=False):
                    print("\nThe MCP tool reported an error.", file=sys.stderr)
                    return 1
                return 0
    except Exception as exc:
        print(f"MCP request failed while {stage}:", file=sys.stderr)
        print_nested_exception(exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(run()))
