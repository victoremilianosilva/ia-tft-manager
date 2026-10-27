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
from typing import Any

from mcp import ClientSession

# MCP SDK 2.x renamed this function; keep compatibility with SDK 1.x.
try:
    from mcp.client.streamable_http import streamable_http_client as streamablehttp_client
except ImportError:  # pragma: no cover - exercised only with MCP SDK 1.x
    from mcp.client.streamable_http import streamablehttp_client

DEFAULT_URL = "https://mcp-api.op.gg/mcp"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"MCP Streamable HTTP endpoint (default: {DEFAULT_URL})",
    )
    parser.add_argument(
        "--call",
        dest="tool_name",
        help="Call a tool by name after connecting; omit to list available tools.",
    )
    parser.add_argument(
        "--arguments",
        help="Tool arguments as a JSON object. Check the tool schema first.",
    )
    return parser.parse_args()


def required_arguments(schema: dict[str, Any]) -> list[str]:
    required = schema.get("required", [])
    return [name for name in required if isinstance(name, str)]


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

    try:
        async with streamablehttp_client(args.url) as streams:
            # SDK 1.x yielded three values; SDK 2.x yields only read/write streams.
            read_stream, write_stream = streams[0], streams[1]
            async with ClientSession(read_stream, write_stream) as session:
                init_result = await session.initialize()
                print(f"Connected to MCP server: {args.url}")
                if getattr(init_result, "serverInfo", None):
                    info = init_result.serverInfo
                    print(f"Server: {info.name} {info.version}")

                tools_result = await session.list_tools()
                if not args.tool_name:
                    print(f"\nAvailable tools ({len(tools_result.tools)}):")
                    for tool in tools_result.tools:
                        print(f"\n- {tool.name}")
                        if tool.description:
                            print(f"  Description: {tool.description}")
                        print(
                            "  Input schema: "
                            + json.dumps(tool.inputSchema, ensure_ascii=False)
                        )
                    return 0

                tool = next(
                    (item for item in tools_result.tools if item.name == args.tool_name),
                    None,
                )
                if tool is None:
                    available = ", ".join(item.name for item in tools_result.tools)
                    print(
                        f"Tool not found: {args.tool_name}\nAvailable tools: {available}",
                        file=sys.stderr,
                    )
                    return 2

                required = required_arguments(tool.inputSchema or {})
                missing = [name for name in required if name not in tool_arguments]
                if missing:
                    print(f"Tool: {tool.name}")
                    print(f"Required arguments missing: {', '.join(missing)}")
                    print(
                        "Input schema: "
                        + json.dumps(tool.inputSchema, ensure_ascii=False, indent=2)
                    )
                    print(
                        "\nRerun with --arguments and provide the required fields, "
                        "for example: --arguments '{\"field\": \"value\"}'"
                    )
                    return 2

                print(f"\nCalling {tool.name} with:")
                print(json.dumps(tool_arguments, ensure_ascii=False, indent=2))
                result = await session.call_tool(tool.name, arguments=tool_arguments)
                print("\nTool result:")
                for item in result.content:
                    if getattr(item, "text", None) is not None:
                        print(item.text)
                    else:
                        print(repr(item))
                if getattr(result, "structuredContent", None) is not None:
                    print(
                        "\nStructured content:"
                        + json.dumps(
                            result.structuredContent,
                            ensure_ascii=False,
                            indent=2,
                            default=str,
                        )
                    )
                if getattr(result, "isError", False):
                    print("\nThe MCP tool reported an error.", file=sys.stderr)
                    return 1
                return 0
    except Exception as exc:
        print(f"MCP request failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        print(
            "Check network access, the endpoint, and the installed 'mcp' package.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(run()))
