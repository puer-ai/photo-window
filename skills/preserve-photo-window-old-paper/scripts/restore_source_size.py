#!/usr/bin/env python3
"""Resize a generated image to the exact pixel dimensions of a source image."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Restore a generated image to the exact dimensions of a source image."
    )
    parser.add_argument("--input", required=True, type=Path, help="Generated image path")
    parser.add_argument("--source", required=True, type=Path, help="Source image path")
    parser.add_argument("--output", required=True, type=Path, help="Output PNG path")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing output")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input.expanduser().resolve(strict=True)
    source_path = args.source.expanduser().resolve(strict=True)
    output_path = args.output.expanduser().resolve()

    if output_path.suffix.lower() != ".png":
        raise SystemExit("--output must use the .png extension")
    if output_path.exists() and not args.force:
        raise SystemExit(
            f"Output already exists: {output_path}. Choose a new path or pass --force."
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(source_path) as source_image:
        source_image.seek(0)
        target_size = source_image.size

    with Image.open(input_path) as input_image:
        input_image.seek(0)
        restored = input_image.resize(target_size, Image.Resampling.LANCZOS)
        restored.save(output_path, format="PNG", optimize=True)

    with Image.open(output_path) as verification_image:
        width, height = verification_image.size

    print(f"Output: {output_path}")
    print(f"Dimensions: {width}x{height}")


if __name__ == "__main__":
    main()
