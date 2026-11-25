#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261124.

Writes one image to /output/entry.png.

Deterministic by design: no network, no randomness, no timestamps,
no generated content. It copies the bundled entry.png byte-for-byte,
so running it twice produces identical output.
"""
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1

    destinations = [
        Path("/output") / "entry.png",
        Path(__file__).resolve().parent / "output" / "entry.png",
    ]

    last_error = None
    for dest in destinations:
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE, dest)
            print(f"wrote {dest}")
            return 0
        except OSError as exc:
            last_error = exc
            continue

    print(f"could not write output: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
