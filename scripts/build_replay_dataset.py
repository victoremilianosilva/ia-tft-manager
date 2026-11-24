#!/usr/bin/env python3
"""Build an immutable, match-disjoint dataset manifest from completed replays."""
from __future__ import annotations

import argparse
from pathlib import Path

from replay.recorder import build_dataset_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("replays", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--split-seed", default="tft-replay-split-v1")
    args = parser.parse_args()
    manifest = build_dataset_manifest(
        args.replays, args.output, split_seed=args.split_seed
    )
    print(
        f"Dataset {manifest['dataset_version']}: "
        f"{manifest['match_count']} matches / {manifest['replay_count']} replays"
    )
    print(f"Manifest: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
