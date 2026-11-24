#!/usr/bin/env python3
"""Ingest complete Overwolf GEP captures into immutable match datasets."""
from __future__ import annotations

import argparse
from pathlib import Path

from replay.gep_ingest import build_gep_dataset_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("captures", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--split-seed", default="tft-gep-split-v1")
    args = parser.parse_args()
    manifest = build_gep_dataset_manifest(
        args.captures, args.output, split_seed=args.split_seed
    )
    print(
        f"Dataset {manifest['dataset_version']}: "
        f"{manifest['match_count']} live matches / {manifest['replay_count']} artifacts"
    )
    print(f"Manifest: {args.output}")
    print("Mode: observational only; no deterministic replay or combat-damage telemetry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
